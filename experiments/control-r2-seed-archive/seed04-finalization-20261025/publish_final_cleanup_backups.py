"""Publish and freshly read back the remaining recovery archives before any deletion."""
import base64,hashlib,json,shutil,subprocess
from pathlib import Path
B=Path(__file__).resolve().parent;LAB=B.parents[1]
GITROOT=LAB/'cores/Shienryu_B75_Preservation'
W=Path('\\\\?\\'+str(GITROOT.resolve()))
G=Path('C:/Users/djjoh/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe')
GH=Path('C:/Users/djjoh/AppData/Local/Programs/GitHub CLI/gh.exe')
REPO='repos/djjohnson13p/MiSTer-STV-Shienryu-Flip';BRANCH='lab/shienryu-control-r2-seed-archive'
ROOT='experiments/control-r2-seed-archive'
def git(*a):return subprocess.check_output([str(G),'-c','core.longpaths=true','-C',str(GITROOT),*a],text=True).strip()
def api(p):return json.loads(subprocess.check_output([str(GH),'api',REPO+p],text=True))
def sha(data):return hashlib.sha256(data).hexdigest()
assert git('branch','--show-current')==BRANCH and git('rev-parse','HEAD')=='0448080be42ece7dcbdef89fe421d8e0676ce7e3'
assert not git('diff','--cached','--name-only')
assert all(x.startswith('?? '+ROOT+'/') for x in git('status','--porcelain').splitlines())
assert api('/git/ref/tags/v1.1-share-20261022')['object']['sha']=='41da931c75b8d1f2d5159cc1ca3770f613c19007'
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']=='dddf174b48b0e6e36d8ba5797a4cb276cdf836f3'
groups=['row-predecessor-seed05-aggressive-hold-r1','legacy-newbase-trials-preservation-r1','mister-obsolete-shienryu-preservation-r1']
for name in groups:
 source=B/name;target=W/ROOT/name
 target.mkdir(parents=True,exist_ok=True)
 for f in sorted(source.iterdir()):
  if f.is_file():
   assert not f.is_symlink() and f.stat().st_size<100*1024**2
   if (target/f.name).exists():assert sha(f.read_bytes())==sha((target/f.name).read_bytes())
   else:shutil.copyfile(f,target/f.name)
   assert sha(f.read_bytes())==sha((target/f.name).read_bytes())
 (target/'.gitattributes').write_bytes(b'* -text\n')
closing=W/ROOT/'seed04-finalization-20261025';assert not closing.exists();closing.mkdir()
(closing/'.gitattributes').write_bytes(b'* -text\n')
extra=['ROOT-FINAL-CLEANUP-ARCHIVE-QC-R1.json','ROOT-SEED05-AGGRESSIVE-HOLD-NATIVE-REVIEW-R1.json',
 'INDEPENDENT-SEED05-AGGRESSIVE-HOLD-NATIVE-SOURCE-REVIEW-R1.json','INDEPENDENT-SEED05-AGGRESSIVE-HOLD-NATIVE-TIMING-REVIEW-R1.json',
 'AGENT-AGGRESSIVE-HOLD-PRESERVATION-RESTORE-VALIDATION-R1.json','AGENT-LEGACY-NEWBASE-PRESERVATION-R1.json',
 'SHIENRYU-AGGRESSIVE-HOLD-TRIAL-RESULT.md','ROOT-AGGRESSIVE-HOLD-PRESERVATION-CREATE-ADMISSION-R1.json',
 'review_aggressive_hold_native_r1.py','publish_final_cleanup_backups.py']
for n in extra:shutil.copyfile(B/n,closing/n)
pub=LAB/'research/shienryu-seed04-publication-r1'
for n in ['PROMOTION-MANIFEST.json','PREPARED-PUBLICATION.json','GITHUB-SEED04-PUBLICATION-VERIFIED.json',
 'ORIGINAL-RELEASE-BEFORE-PROMOTION.json','RELEASE-NOTES.md','prepare_publication.py','publish_publication.py']:
 shutil.copyfile(pub/n,closing/n)
(closing/'README.md').write_text('''# Shienryu project finalization

The user selected verified source7e9/seed4 as the current published build and requested removal of local development files and obsolete MiSTer variants. Current public release is v1.2-seed04-20261025; original v1.1 tag/release remains preserved.

The aggressive-hold experiment produced the same RBF bytes and timing as original6eb/seed5, so that approach stopped. The separate native recovery packages preserve its complete fit and assembled checkpoints, source, settings, tools, RBF/SOF and all118 STA reports. Legacy STVB/STVC full native trees and their137 STA reports are separately preserved and restored exactly. Six obsolete installed runtime files are also preserved byte-for-byte.

Optional copied post-STA working caches are excluded; original fitted/assembled checkpoints and all measured reports are preserved. These excluded derived copies and private transport helpers will be removed with the user-requested PC cleanup. Historical creation manifests saying files remained local describe creation time, not permanent retention. No credentials, external game/BIOS archives or personal saves are published here.

Deletion is permitted only after fresh remote byte verification. Goal removal follows completion of publication and cleanup. Seed4 remains experimental, with the two disclosed cold setup failures; this is not a claim of full timing closure.
''',encoding='utf-8')
paths=[ROOT+'/'+n for n in groups]+[ROOT+'/seed04-finalization-20261025']
git('-c','core.autocrlf=false','add','--',*paths)
names=git('diff','--cached','--name-only').splitlines();expected={}
for n in names:
 assert any(n.startswith(p+'/') for p in paths)
 data=(W/n).read_bytes();oid=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 assert git('rev-parse',':'+n)==oid
 expected[n]=dict(git_blob=oid,bytes=len(data),sha256=sha(data))
git('commit','-m','Preserve final Shienryu experiments and legacy checkpoints before requested cleanup')
head=git('rev-parse','HEAD')
git('push','origin','HEAD:refs/heads/'+BRANCH)
assert api('/git/ref/heads/'+BRANCH)['object']['sha']==head
tree=api('/git/trees/'+head+'?recursive=1');assert not tree.get('truncated')
entries={x['path']:x for x in tree['tree'] if x['type']=='blob'}
for i,(n,row) in enumerate(expected.items(),1):
 assert entries[n]['sha']==row['git_blob'] and entries[n]['size']==row['bytes']
 blob=api('/git/blobs/'+row['git_blob']);assert blob['encoding']=='base64'
 data=base64.b64decode(blob['content']);assert len(data)==row['bytes'] and sha(data)==row['sha256']
 print(json.dumps({'verified':i,'of':len(expected),'file':n,'bytes':len(data)}),flush=True)
assert api('/git/ref/heads/stv-flip-v1.1')['object']['sha']=='dddf174b48b0e6e36d8ba5797a4cb276cdf836f3'
assert api('/git/ref/tags/v1.1-share-20261022')['object']['sha']=='41da931c75b8d1f2d5159cc1ca3770f613c19007'
assert not git('status','--porcelain')
r=dict(state='ALL_REMAINING_RECOVERY_FILES_FRESH_REMOTE_BYTES_VERIFIED',commit=head,branch=BRANCH,
 files=expected,verified_file_count=len(expected),verified_bytes=sum(x['bytes'] for x in expected.values()),
 current_seed4_default_commit='dddf174b48b0e6e36d8ba5797a4cb276cdf836f3',original_tag_preserved=True,
 no_device_or_PC_deletion_performed=True)
out=B/'GITHUB-FINAL-CLEANUP-BACKUPS-VERIFIED.json'
with out.open('x',encoding='utf-8') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'COMPLETE':True,'commit':head,'files':len(expected),'bytes':r['verified_bytes'],'receipt_sha256':sha(out.read_bytes())}),flush=True)
