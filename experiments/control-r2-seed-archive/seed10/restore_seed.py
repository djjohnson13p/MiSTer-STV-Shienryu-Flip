"""Restore an exact preserved checkpoint into a new directory; standard library only."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, choices=(10,), required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    archive = Path(__file__).resolve().parent
    package = archive / 'frozen-package'
    review = read(archive / 'ROOT-PACKAGE-REVIEW.json')
    if digest(package / 'PACKAGE-INDEX.json') != review['package_index_sha256']:
        raise ValueError('Package index changed')
    index = read(package / 'PACKAGE-INDEX.json')
    for name, record in index['sidecars'].items():
        if digest(package / name) != record['sha256']:
            raise ValueError('Changed sidecar: ' + name)
    seed = f'seed{args.seed:02}'
    members = read(package / 'MEMBER-HASHES.json')
    snapshot = read(package / 'SEED10-ASM-SNAPSHOT.json')['files']
    base = seed + '/fit-checkpoint/tree/'
    overlay = seed + '/assembled-checkpoint-overlay/tree/'
    selected = [{**record, 'filename': name} for name, record in members['packages'].items()]
    for record in selected:
        path = package / record['filename']
        if digest(path) != record['sha256']:
            raise ValueError('Changed ZIP: ' + record['filename'])
    destination = args.out.resolve()
    destination.mkdir(parents=True, exist_ok=False)
    written = set()
    for prefix in (base, overlay):
        for record in selected:
            with zipfile.ZipFile(package / record['filename']) as zipped:
                for name, expected in record['members'].items():
                    if not name.startswith(prefix):
                        continue
                    relative = PurePosixPath(name[len(prefix):])
                    if relative.is_absolute() or '..' in relative.parts or '\\' in str(relative) or ':' in str(relative):
                        raise ValueError('Unsafe member: ' + name)
                    target = destination.joinpath(*relative.parts)
                    data = zipped.read(name)
                    if len(data) != expected['bytes'] or hashlib.sha256(data).hexdigest() != expected['sha256']:
                        raise ValueError('Changed member: ' + name)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open('wb' if prefix == overlay else 'xb') as stream:
                        stream.write(data)
                    written.add(relative.as_posix())
    if args.seed == 10:
        deleted = read(package / 'ASM-OVERLAY.json')['deleted']
        if deleted:
            raise ValueError('This fixed archive expects no deleted overlay members')
    if written != set(snapshot):
        raise ValueError('Restored member set differs from the saved checkpoint')
    for name, expected in snapshot.items():
        target = destination / name
        if target.stat().st_size != expected['bytes'] or digest(target) != expected['sha256']:
            raise ValueError('Restored checkpoint mismatch: ' + name)
    print(json.dumps({'seed': args.seed, 'restored_files': len(written),
                      'exact_checkpoint_verified': True, 'destination': str(destination),
                      'rbf_sha256': digest(destination / 'output_files/STV_DS.rbf')}))


if __name__ == '__main__':
    main()
