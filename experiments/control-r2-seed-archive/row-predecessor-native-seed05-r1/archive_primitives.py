"""Exact archive/hash primitives extracted from reviewed package_shienryu_seed.py; no seed/source/admission/package entry points."""
import hashlib,io,json,math,os,re,zipfile
from pathlib import Path,PurePosixPath
ZIP_LIMIT, RAW_PART_BUDGET = 100_000_000, 85_000_000

CHECKS = ("setup", "hold", "recovery", "removal")

SECRET = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    rb"\bghp_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}|"
    rb"\bxox[baprs]-[A-Za-z0-9-]{20,}")

def require(ok, message):
    if not ok:
        raise ValueError(message)

def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()

def info(path):
    return dict(bytes=path.stat().st_size, sha256=sha(path))

def save(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")

def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def relative(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and ".." not in p.parts
            and "\\" not in name and ":" not in name, "Unsafe relative path: " + name)
    return p

def no_link(path):
    st = path.lstat()
    require(not path.is_symlink() and not getattr(st, "st_file_attributes", 0) & 0x400,
            "Symlink/reparse point refused: " + str(path))

def snapshot(folder):
    no_link(folder)
    result = {}
    for root, dirs, files in os.walk(folder, followlinks=False):
        for name in sorted(dirs + files):
            path = Path(root) / name
            no_link(path)
            if path.is_file():
                rel = path.relative_to(folder).as_posix()
                relative(rel)
                result[rel] = info(path)
    return dict(sorted(result.items()))

def matrix_check(matrix):
    expected = {(m, t) for m in ("slow", "fast") for t in (-40, 0, 85, 100)}
    require(len(matrix) == 8 and {(r["model"], r["temperature_C"]) for r in matrix}
            == expected, "All eight actual conditions required")
    for row in matrix:
        require(set(row["checks"]) == set(CHECKS), "Missing timing check")
        for check in row["checks"].values():
            v = check["slack_ns"]
            require(isinstance(v, (int, float)) and not isinstance(v, bool)
                    and math.isfinite(v) and check["pass"] == (v >= 0),
                    "NA/nonfinite/inconsistent timing slack is not a pass")
        pw = row["minimum_pulse_width"]
        require(isinstance(pw["slack_ns"], (int, float))
                and math.isfinite(pw["slack_ns"]) and pw["reported_paths"] > 0
                and isinstance(pw["violated"], int) and pw["violated"] >= 0,
                "Applicable global MPW evidence required")

def partition(entries, budget=RAW_PART_BUDGET):
    batch, total = [], 0
    for name, path in sorted(entries.items()):
        relative(name)
        size = path.stat().st_size
        require(size < budget, "Single member exceeds raw part budget: " + name)
        if batch and total + size > budget:
            yield batch
            batch, total = [], 0
        batch.append((name, path))
        total += size
    if batch:
        yield batch

def write_zip(path, entries):
    entries = list(entries)
    records = {n: info(p) for n, p in entries}
    require(len(records) == len(entries), "Duplicate ZIP member")

    def build():
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for n, p in entries:
                relative(n)
                data = p.read_bytes()
                require(dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
                        == records[n], "Packaging input changed: " + n)
                zi = zipfile.ZipInfo(n, (1980, 1, 1, 0, 0, 0))
                zi.create_system, zi.external_attr = 3, 0o100644 << 16
                z.writestr(zi, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)
        return buf.getvalue()

    data = build()
    require(len(data) < ZIP_LIMIT and data == build(), "ZIP size/determinism failed")
    with path.open("xb") as stream:
        stream.write(data)
    with zipfile.ZipFile(path) as z:
        require(z.testzip() is None and z.namelist() == [n for n, _ in entries], "ZIP CRC/member inventory failed")
        for n, record in records.items():
            raw = z.read(n)
            require(dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()) == record,
                    "ZIP member hash failed: " + n)
    return dict(bytes=len(data), sha256=sha(path), member_count=len(records), members=records,
                all_member_sha_and_crc_verified=True, deterministic_second_serialization_identical=True)
