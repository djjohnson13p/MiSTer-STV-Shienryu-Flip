"""One local backup of the two closed legacy new-base trials; no native/Git/device actions."""
import hashlib,importlib.util,json,os,re,sys,zipfile
from pathlib import Path
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent
RESEARCH=BASE.parent
LAB=RESEARCH.parent.parent
PROVIDER=BASE/'archive_primitives.py'
PROVIDER_SHA='1f4def931bdef7ccf1ed7c52de6418582b2e2e1b1bcdd729867da077816d52b3'
NATIVE=('shienryu-upstream-q251-baseline-r1','shienryu-flip-q251-candidate-r1')
STA=('shienryu-upstream-sta-all-corners-r1','shienryu-flip-sta-all-corners-r1')
HARDWARE=('baseline-hardware-r1','candidate-hardware-r1')
EXTERNAL=('UPSTREAM-BUILD-PROVENANCE-REVIEW.json','ROOT-CANDIDATE-SOURCE-REVIEW-R1.json','ROOT-CANDIDATE-INITIAL-RESULT-R1.json','AGENT-CANDIDATE-TERMINAL-AUDIT-R1.json','AGENT-CANDIDATE-FIT-INPUT-INVENTORY-PROPOSAL-R1.json')
TAG='legacy-newbase-trials-r1'
def require(ok,message):
    if not ok:raise ValueError(message)
def sha(path):
    with path.open('rb')as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
require(sha(PROVIDER)==PROVIDER_SHA,'Reviewed ZIP primitive changed')
spec=importlib.util.spec_from_file_location('reviewed_legacy_archive_primitives',PROVIDER);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
SECRET_NAME=re.compile(r'(^|/)(\.git|\.ssh|credentials?|secrets?)(/|$)|(^|/)(id_rsa|id_ed25519)(\.|$)|\.(pem|pfx|p12|key)$',re.I)
TEXT={'.json','.md','.txt','.xml','.csv','.tsv','.log','.py','.ps1','.tcl','.v','.sv','.vhd','.qsf','.qip','.sdc','.rpt','.summary','.mra','.map'}
HW_SUFFIX={'.json','.png','.md','.txt','.xml','.csv','.tsv','.mra','.map'}
def snapshot(root):
    p.no_link(root);files={};git=[]
    for here,dirs,names in os.walk(root,followlinks=False):
        for name in sorted(dirs+names):
            f=Path(here)/name;p.no_link(f)
            if name=='.git':git.append(f.relative_to(root).as_posix())
            elif f.is_file():
                rel=f.relative_to(root).as_posix();p.relative(rel);files[rel]=p.info(f)
        dirs[:]=[d for d in dirs if d!='.git']
    return dict(sorted(files.items())),git
def safe_file(f,rel):
    if SECRET_NAME.search(rel):return False,'credential/Git path excluded'
    if f.suffix.lower()in TEXT and p.SECRET.search(f.read_bytes()):return False,'credential marker excluded'
    if f.suffix.lower()=='.zip':
        with zipfile.ZipFile(f)as z:
            require(z.testzip()is None,'Source archive CRC failed')
            for member in z.infolist():
                if member.is_dir():continue
                p.relative(member.filename)
                require(not SECRET_NAME.search(member.filename),'Credential/Git path inside source ZIP')
                if Path(member.filename).suffix.lower()in TEXT:require(not p.SECRET.search(z.read(member)),'Credential marker inside source ZIP')
    return True,None
def main():
    require(not(BASE/'PACKAGE-INDEX.json').exists() and not list(BASE.glob('*.zip')),'Never overwrite or resume packages')
    roots={f'builds/{n}':LAB/'builds'/n for n in NATIVE+STA}
    roots.update({f'research/shienryu-timing-20261024/{n}':RESEARCH/n for n in HARDWARE})
    before={};git={};exclusions={};entries={};tree_maps={};native_proofs={}
    for name in NATIVE+STA:
        b=LAB/'builds'/name;r=load(b/'result.json');c=load(b/'terminal-task-cleanup.json')
        require(r['state']=='terminal' and r['flow_exit_code']==0 and r['all_job_processes_terminal'] and r['all_handles_closed'] and r['final_job_active_processes']==0 and r['errors']==[],'Native result not closed: '+name)
        require(c['exact_task_unregistered'] and c['all_job_processes_terminal'] and c['all_handles_closed'] and c['errors']==[],'Cleanup not complete: '+name)
        native_proofs[name]={k:r.get(k)for k in ('state','flow_exit_code','all_job_processes_terminal','all_handles_closed','final_job_active_processes','errors')}
        native_proofs[name].update(result_sha256=sha(b/'result.json'),cleanup_sha256=sha(b/'terminal-task-cleanup.json'),raw_scheduler_exit=load(b/'scheduler-action-exit.json')['exit_code'])
    for label,root in roots.items():
        actual,ignored=snapshot(root);before[label]=actual;git[label]=ignored
        for rel,row in actual.items():
            f=root/rel;key=label+'/'+rel
            reason='redundant copied STA working tree; exact complete inventory retained'if root.name in STA and rel.startswith('tree/')else None
            if root.name in HARDWARE and f.suffix.lower()not in HW_SUFFIX:reason='hardware JSON/PNG/metadata only; helper/runtime/binary omitted'
            allowed,safety=safe_file(f,rel)
            if not allowed:reason=safety
            if reason:exclusions[key]=dict(reason=reason,**row)
            else:entries[TAG+'/'+key]=f
        if root.name in NATIVE:tree_maps[root.name]={n[5:]:v for n,v in actual.items()if n.startswith('tree/')}
    for name in EXTERNAL:
        f=RESEARCH/name
        if f.exists():
            safe,reason=safe_file(f,name);require(safe,'Unsafe external review');entries[TAG+'/research/'+name]=f
    external_before={str(f):p.info(f)for f in entries.values()if f.parent==RESEARCH}
    p.save(BASE/'ORIGINAL-FULL-MEMBERSHIP.json',dict(roots=before,git_metadata_excluded=git))
    p.save(BASE/'EXCLUSIONS.json',dict(files=exclusions,git_metadata_excluded=git,STA_copied_working_trees_archived=False))
    p.save(BASE/'NATIVE-TREE-SNAPSHOTS.json',tree_maps)
    p.save(BASE/'NATIVE-TERMINAL-PROOFS.json',native_proofs)
    README='''# Legacy new-base STVB/STVC recovery backup — local draft

Preserves both original native build trees in full, including exact source ZIPs, source/QSF/SDC/PLL/generated date, map/fitted databases, programming RBF/SOF, reports and native controls. All non-tree evidence and every report from the two separate all-corner STA runs are retained. Their redundant copied working trees are excluded only with complete path/byte/SHA inventories. Hardware journals contain JSON/PNG/metadata; private transport helpers, runtime binaries and credential material are excluded and inventoried.

All ZIPs and sidecars are required. Every selected member is hashed and CRC/readback verified. Both original native trees are restored into new exclusive local directories and rehashed before the final index is written. Original memberships and hashes must remain unchanged. Git metadata is excluded. Exact inherited source MIF members remain intact; no external game/BIOS/runtime archive or credential is added, and no source-content legal-clearance claim is made.

This preserves experimental historical measurements, raw compiler/scheduler/integrity outcomes and hardware observations without timing/hardware acceptance. It does not prove bit-identical fresh compilation, relocated Quartus database usability or physical HDMI/audio behavior. No native tool, Git, device, deletion or upload action occurs. This local draft still requires independent Root QC and remote-byte verification before local cleanup.
'''
    (BASE/'README.md').write_text(README,encoding='utf-8',newline='\n')
    for f in BASE.iterdir():
        if f.is_file():entries[TAG+'/preservation/'+f.name]=f
    groups={}
    for member,f in entries.items():
        native=next((n for n in NATIVE if member.startswith(TAG+'/builds/'+n+'/tree/')),None)
        group='evidence'
        if native:
            rel=member.split('/tree/',1)[1];group=native+('-db'if rel.startswith('db/')else'-incremental-db'if rel.startswith('incremental_db/')else'-project-and-output')
        groups.setdefault(group,{})[member]=f
    packages={}
    for group,files in sorted(groups.items()):
        for number,part in enumerate(p.partition(files),1):
            name=f'legacy-newbase-{group}-{number:02}.zip';print('Creating '+name,flush=True);packages[name]=p.write_zip(BASE/name,part)
    union={};locations={}
    for name,pkg in packages.items():
        for member,row in pkg['members'].items():require(member not in union,'Duplicate member');union[member]=row;locations[member]=name
    require(union=={n:p.info(f)for n,f in entries.items()},'Archive union differs')
    restores={}
    for name,expected in tree_maps.items():
        target=RESEARCH/('legacy-newbase-restore-'+name+'-r1');require(not target.exists(),'Restore destination occupied');target.mkdir()
        prefix=TAG+'/builds/'+name+'/tree/'
        require({n[len(prefix):]:v for n,v in union.items()if n.startswith(prefix)}==expected,'Native tree archive mapping differs')
        for rel,row in expected.items():
            p.relative(rel);member=prefix+rel;dst=target/rel;require(dst.resolve().is_relative_to(target),'Restore path escaped');dst.parent.mkdir(parents=True,exist_ok=True)
            with zipfile.ZipFile(BASE/locations[member])as z:raw=z.read(member)
            with dst.open('xb')as f:f.write(raw)
            require(p.info(dst)==row,'Restored bytes differ')
        restored,_=snapshot(target);require(restored==expected,'Full restored membership differs')
        restores[name]=dict(target=str(target),file_count=len(expected),bytes=sum(x['bytes']for x in expected.values()),snapshot_map_sha256=p.digest(restored),every_restored_member_exact=True,programming={n:v for n,v in expected.items()if n.endswith(('.rbf','.sof'))})
    after={label:snapshot(root)[0]for label,root in roots.items()};require(after==before,'Original input membership/bytes changed')
    require(all(p.info(Path(n))==v for n,v in external_before.items()),'External review changed')
    p.save(BASE/'MEMBER-HASHES.json',dict(packages=packages))
    p.save(BASE/'RESTORE-VALIDATION.json',dict(reviewer='agent:/root/shienryu_build_admission',restores=restores,original_full_membership_before_after_exact=True,no_native_action=True,bit_identical_fresh_rebuild_demonstrated=False))
    p.save(BASE/'PACKAGE-INDEX.json',dict(state='LOCAL_DRAFT_PENDING_ROOT_QC_AND_REMOTE_VERIFICATION',package_count=len(packages),package_bytes=sum(x['bytes']for x in packages.values()),ZIP_members=len(union),packages={n:{k:v for k,v in row.items()if k!='members'}for n,row in packages.items()},sidecars={f.name:p.info(f)for f in BASE.iterdir()if f.is_file()and f.suffix!='.zip'},native_tree_counts={n:len(v)for n,v in tree_maps.items()},all_original_inputs_unchanged=True,STA_copied_working_trees_archived=False,restores=restores,remote_uploaded=False,timing_acceptance=False,hardware_acceptance=False))
    print(json.dumps(dict(index_sha256=sha(BASE/'PACKAGE-INDEX.json'),packages=len(packages),package_bytes=sum(x['bytes']for x in packages.values()),members=len(union),restores=restores),indent=2))
if __name__=='__main__':main()
