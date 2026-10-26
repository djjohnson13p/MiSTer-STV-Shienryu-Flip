"""Publish the explicitly requested seed4 replacement and verify remote payload bytes."""
import base64,hashlib,json,subprocess
from pathlib import Path
P=Path(__file__).resolve().parent
record=json.loads((P/'PREPARED-PUBLICATION.json').read_text())
W=Path(record['worktree']);HEAD=record['new_commit'];OLD=record['old_default']
G=Path('C:/Users/djjoh/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe')
GH=Path('C:/Users/djjoh/AppData/Local/Programs/GitHub CLI/gh.exe')
REPO='repos/djjohnson13p/MiSTer-STV-Shienryu-Flip';SLUG='djjohnson13p/MiSTer-STV-Shienryu-Flip'
TAG='v1.2-seed04-20261025';BASE='https://github.com/'+SLUG
def git(*args):return subprocess.check_output([str(G),'-C',str(W),*args],text=True).strip()
def api(path):return json.loads(subprocess.check_output([str(GH),'api',REPO+path],text=True))
def sha(data):return hashlib.sha256(data).hexdigest()
def raw(oid):
 blob=api('/git/blobs/'+oid);assert blob['encoding']=='base64';return base64.b64decode(blob['content'])
assert git('rev-parse','HEAD')==HEAD and not git('status','--porcelain')
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']==OLD
assert api('/git/ref/tags/v1.1-share-20261022')['object']['sha']==OLD
old_release=api('/releases/421111543')
with (P/'ORIGINAL-RELEASE-BEFORE-PROMOTION.json').open('x',encoding='utf-8') as f:json.dump(old_release,f,indent=2);f.write('\n')
git('push','origin','HEAD:refs/heads/stv-flip-v1.1')
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']==HEAD
tree=api('/git/trees/'+HEAD+'?recursive=1');assert not tree.get('truncated')
entries={x['path']:x for x in tree['tree'] if x['type']=='blob'}
assert set(entries)==set(record['files'])
for n,row in record['files'].items():
 assert entries[n]['sha']==row['git_blob']
 if 'bytes' in row:assert entries[n]['size']==row['bytes']
assert all(n not in entries for n in record['removed_superseded_current_paths'])
critical=['README.md','STV_DS.qsf','build_id.v','install/_Arcade/SHYF0004.mra','install/_Arcade/cores/SHYF0004.rbf',
 'packages/MiSTer-STV-Shienryu-Flip-seed04-20261025.zip','source/Shienryu-seed04-compiled-source.zip','source/COMPILED-SOURCE-MANIFEST.json']
fresh={}
for n in critical:
 data=raw(entries[n]['sha']);row=record['files'][n]
 assert len(data)==row['bytes'] and sha(data)==row['sha256'];fresh[n]=row
notes='''Experimental Shienryu-only, HDMI-only, dual-SDRAM build. This seed4 supersedes the previous install package. Audio, video and180-degree flip were confirmed on a first-generation dual-RAM MiSTer Pi.

## Download and install

Download **MiSTer-STV-Shienryu-Flip-seed04-20261025.zip** below. Extract it and copy the contents of install/ to the SD-card root. Keep the supplied SHYF0004.rbf and SHYF0004.mra names together. Compatible shienryu.zip and stvbios.zip are required separately and are not included.

F12 → Audio & Video → Shienryu180 Flip → On/Off. Fresh settings default Off; use Save settings to retain your choice. Existing settings may retain On. The active HDMI game picture rotates180degrees; OSD orientation is separate. No90-degree or analog/direct-video feature is provided.

## Experimental timing

Full-range timing closure has not been achieved. All conditions below are1.1V; slack is ns. Recovery/removal/minimum pulse width pass all8. Negative setup slack fails.

| Model | C | Setup | Hold | Result |
|---|---:|---:|---:|---|
| Slow | -40 | -0.101 | +0.174 | Fail setup |
| Slow | 0 | -0.038 | +0.172 | Fail setup |
| Slow | 85 | +0.070 | +0.242 | Pass |
| Slow | 100 | +0.014 | +0.235 | Pass |
| Fast | -40 | +3.441 | +0.052 | Pass |
| Fast | 0 | +3.350 | +0.054 | Pass |
| Fast | 85 | +2.972 | +0.089 | Pass |
| Fast | 100 | +2.923 | +0.093 | Pass |

RBF SHA256:99654dbf7a472b610f840f9dbbb0087bc6f508ce3dfdfe2ffbd48e6df5396d11.

The compiled-source ZIP and manifest are attached; source is based on7e987bb9ef0361356be22be13551e4626902f3a7, Quartus25.1 Lite, seed4, fixed build date261025. Exact archived binaries/checkpoints can be restored; identical fresh recompilation is not claimed. The repository README records test scope and inherited timing qualifications. The earlier v1.1 release/tag remains available as historical recovery.
'''
notes_path=P/'RELEASE-NOTES.md';notes_path.write_text(notes,encoding='utf-8')
assets=[P/'packages/MiSTer-STV-Shienryu-Flip-seed04-20261025.zip',P/'packages/MiSTer-STV-Shienryu-Flip-seed04-20261025.zip.sha256',
 P/'source/Shienryu-seed04-compiled-source.zip',P/'source/COMPILED-SOURCE-MANIFEST.json',
 P/'install/_Arcade/cores/SHYF0004.rbf',P/'install/_Arcade/SHYF0004.mra',P/'SHA256SUMS']
subprocess.run([str(GH),'release','create',TAG,*map(str,assets),'--repo',SLUG,'--target',HEAD,
 '--title','Shienryu HDMI180 Flip — Seed4 (Experimental)','--prerelease','--notes-file',str(notes_path)],check=True)
release=api('/releases/tags/'+TAG);assert release['tag_name']==TAG and release['prerelease'] and not release['draft']
listed={x['name']:x for x in release['assets']};assert set(listed)=={x.name for x in assets}
for asset in assets:
 row=listed[asset.name];assert row['size']==asset.stat().st_size
 digest=row.get('digest');assert digest=='sha256:'+sha(asset.read_bytes()),('Missing/mismatched server digest',asset.name,digest)
notice='**Superseded by the [verified seed4 experimental release]('+BASE+'/releases/tag/'+TAG+').** The original v1.1 package and tag below remain preserved.\n\n'
old_body=P/'ORIGINAL-RELEASE-WITH-CURRENT-LINK.md';old_body.write_text(notice+old_release['body'],encoding='utf-8')
subprocess.run([str(GH),'release','edit','v1.1-share-20261022','--repo',SLUG,'--notes-file',str(old_body)],check=True)
assert api('/git/ref/tags/v1.1-share-20261022')['object']['sha']==OLD
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']==HEAD
receipt=dict(state='PUBLISHED_CURRENT_SEED4_AND_VERIFIED',commit=HEAD,default_branch='stv-flip-v1.1',
 release_url=release['html_url'],tag=TAG,old_tag_preserved=OLD,fresh_raw_GitHub_readbacks=fresh,
 all267_tree_blob_identities_verified=True,server_asset_SHA256_digests_verified={x.name:listed[x.name]['digest'] for x in assets},
 prior_current_install_paths_removed=record['removed_superseded_current_paths'],experimental=True,full_timing_closure=False,
 user_authorization='Push seed4 to our GitHub replacing existing; preserve history and then cleanup local files.')
with (P/'GITHUB-SEED04-PUBLICATION-VERIFIED.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(dict(commit=HEAD,release=release['html_url'],verified_assets=len(assets),old_tag_preserved=True)))
