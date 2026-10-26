"""Prepare the requested default-branch replacement locally; no remote mutation."""
import hashlib,json,shutil,subprocess,zipfile
from pathlib import Path
P=Path(__file__).resolve().parent
LAB=P.parents[1]
R=LAB/'cores/Shienryu_B75_Preservation'
W=LAB/'cores/Shienryu_Seed04_Publish'
G=Path('C:/Users/djjoh/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe')
GH=Path('C:/Users/djjoh/AppData/Local/Programs/GitHub CLI/gh.exe')
REPO='repos/djjohnson13p/MiSTer-STV-Shienryu-Flip'
OLD='41da931c75b8d1f2d5159cc1ca3770f613c19007'
SOURCE='7e987bb9ef0361356be22be13551e4626902f3a7'
def git(root,*args):return subprocess.check_output([str(G),'-C',str(root),*args],text=True).strip()
def api(path):return json.loads(subprocess.check_output([str(GH),'api',REPO+path],text=True))
def sha(data):return hashlib.sha256(data).hexdigest()
def put(name,data):
 target=W/name;assert target.resolve().is_relative_to(W.resolve())
 target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
manifest=json.loads((P/'PROMOTION-MANIFEST.json').read_text())
assert sha((P/'PROMOTION-MANIFEST.json').read_bytes())=='fd526737c876a02bba05da9e3c5b15df4653b2e0eff6238d4bf616e6c7dd0f50'
for n,row in manifest['files'].items():
 data=(P/n).read_bytes();assert len(data)==row['bytes'] and sha(data)==row['sha256']
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']==OLD
tag=api('/git/ref/tags/v1.1-share-20261022');assert tag['object']['sha']==OLD
assert git(R,'remote','get-url','origin')=='https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip.git'
if not W.exists():
 git(R,'fetch','origin','refs/heads/stv-flip-v1.1:refs/remotes/origin/stv-flip-v1.1')
 git(R,'worktree','add','--detach',str(W.resolve()),OLD)
 # Keep the published branch history while replacing its source tree with the tested base.
 git(W,'restore','--source='+SOURCE,'--staged','--worktree','--','.')
else:
 # Explicit recovery from the local sparse-checkout validation stop, before any commit/push.
 assert git(W,'rev-parse','HEAD')==OLD and not (P/'PREPARED-PUBLICATION.json').exists()
compiled=json.loads((P/'source/COMPILED-SOURCE-MANIFEST.json').read_text())
with zipfile.ZipFile(P/'source/Shienryu-seed04-compiled-source.zip') as z:
 assert len(z.namelist())==204 and len(set(z.namelist()))==204
 for n in z.namelist():
  data=z.read(n);row=compiled['member_hashes'][n]
  assert len(data)==row['bytes'] and sha(data)==row['sha256']
  put(n,data)
obsolete=manifest['old_install_entries']+manifest['old_current_package_entries']+manifest['old_Shienryu_release_entries']
for n in obsolete:assert (W/n).resolve().is_relative_to(W.resolve())
git(W,'rm','--sparse','--ignore-unmatch','--',*obsolete)
for n in manifest['files']:put(n,(P/n).read_bytes())
put('.gitattributes',b'* -text\n')
assert (W/'sys/ascal.vhd').read_bytes()==subprocess.check_output([str(G),'-C',str(R),'show',SOURCE+':sys/ascal.vhd'])
assert sha((W/'STV_DS.qsf').read_bytes())==compiled['compiled_QSF_sha256']
assert (W/'build_id.v').read_bytes()==b'`define BUILD_DATE "261025"'
assert sha((W/'install/_Arcade/cores/SHYF0004.rbf').read_bytes())==manifest['RBF_sha256']
assert sha((W/'install/_Arcade/SHYF0004.mra').read_bytes())==manifest['MRA_sha256']
git(W,'-c','core.autocrlf=false','add','--all','--force','--','.')
# Check every staged blob against its raw local bytes, not autocrlf-normalized input.
staged={}
skip={line[2:] for line in git(W,'ls-files','-v').splitlines() if line.startswith('S ')}
source_tree={line.split('\t')[1]:line.split()[2] for line in git(R,'ls-tree','-r',SOURCE).splitlines()}
for line in git(W,'ls-files','--stage').splitlines():
 meta,n=line.split('\t');mode,oid,stage=meta.split();assert stage=='0'
 if (W/n).is_file():
  data=(W/n).read_bytes()
  assert oid==hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  staged[n]=dict(git_blob=oid,bytes=len(data),sha256=sha(data))
 else:
  assert n in skip and n.startswith('releases/') and oid==source_tree[n]
  staged[n]=dict(git_blob=oid,unchanged_sparse_source_asset=True)
assert all(n not in staged for n in obsolete)
git(W,'commit','-m','Publish verified Shienryu HDMI flip seed 4 as the current experimental build')
head=git(W,'rev-parse','HEAD');assert git(W,'rev-parse','HEAD^')==OLD
assert not git(W,'status','--porcelain')
record=dict(state='LOCAL_COMMIT_READY_FOR_EXPLICIT_PUBLICATION',worktree=str(W.resolve()),
 old_default=OLD,source_base=SOURCE,new_commit=head,default_branch='stv-flip-v1.1',
 files=staged,removed_superseded_current_paths=obsolete,payload_manifest_sha256=sha((P/'PROMOTION-MANIFEST.json').read_bytes()),
 original_tag_ref=tag,experimental=True,full_timing_closure=False,no_remote_mutation=True)
with (P/'PREPARED-PUBLICATION.json').open('x',encoding='utf-8') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps(dict(commit=head,source=SOURCE,staged_files=len(staged),removed_old_install_and_release_paths=len(obsolete),worktree=str(W))))
