"""Fixed6eb preservation adapter. --plan reads metadata only; creation requires exact root review.
No project code, Git, Quartus, device, upload, deletion or original-tree write is executed.
"""
import argparse,hashlib,importlib.util,json,os,re,sys,zipfile
from pathlib import Path
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent
RESEARCH=BASE.parent
EXPERIMENT=RESEARCH/'row-predecessor-native-draft-r1'
OUTPUT=RESEARCH/'row-predecessor-native-preservation-r1'
PROVIDER=BASE/'archive_primitives.py'
PROVIDER_SHA='1f4def931bdef7ccf1ed7c52de6418582b2e2e1b1bcdd729867da077816d52b3'
SOURCE='6eb9367e2d64c18b0b109d221a0bc07d35d493b4'
VARIANT='73ca65c64ef89e037e3995ca1faa56e3f7b8a1480b1a2f20190fb3d17b41ef57'
RBF='483da40e9bf6a231bb393e793aa11b9fa3ac82a82b201437c6259a42cb3561fc'
SOF='3fd01dbefad46827ba07e59d861a3e4da434f7cfce7afc3bb05fc04a6e6b41f2'
GUARD='5d287472358720e99822c57a5b576508af60ef5c41db5131ffe2ea5b78ec04c9'
TAG='rowpred6eb-seed04'
GIB=1024**3
LIMITS=dict(wall_seconds=None,cleanup_reserve_seconds=20,job_private_bytes=10*GIB,tree_rss_bytes=9*GIB,
    admission_free_commit_bytes=12*GIB,continuous_free_commit_floor_bytes=2*GIB)

def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def require(ok,message):
    if not ok:raise ValueError(message)
def primitives():
    require(sha(PROVIDER)==PROVIDER_SHA,'Reviewed primitive provider changed')
    s=importlib.util.spec_from_file_location('reviewed_archive_primitives_only',PROVIDER);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    # Only path/hash/snapshot/matrix/partition/deterministic-ZIP primitives are called.
    # Fixed7e9 metadata/preflight/package/main are never called or rebound.
    return m
def metadata():
    p=primitives();bindings=load(BASE/'metadata-bindings.json')
    for path,h in bindings.items():require(sha(path)==h,'Bound control metadata changed: '+path)
    seal=load(EXPERIMENT/'preservation-index.json');members=seal['members']
    require(len(members)==2245 and SOURCE in seal['source_identity'],'Wrong experiment seal')
    trees={s:{n[len(s+'/tree/'):]:v for n,v in members.items() if n.startswith(s+'/tree/')} for s in ('full','sta')}
    require(len(trees['full'])==1051 and len(trees['sta'])==1065,'Checkpoint membership changed')
    require(trees['full']==load(EXPERIMENT/'stages/full/checkpoint.json'),'Full checkpoint differs from seal')
    result=load(EXPERIMENT/'experiment-result.json');fullq=load(EXPERIMENT/'stages/full/qualification.json');staq=load(EXPERIMENT/'stages/sta/qualification.json')
    require(result['source_commit']==SOURCE and result['variant_exact_sha256']==VARIANT and result['seed']==4 and result['BUILD_DATE']=='261025' and result['exit_code']==0,'Wrong native measurement')
    require(fullq['passed'] and fullq['full_fresh_pipeline'] and fullq['actual_placement_seed']==4 and fullq['new_map_fit_programming_outputs'],'Fresh map/fit/ASM qualification absent')
    require(fullq['no_post_fit_input'] and fullq['zero_requested_and_achieved_placement_and_routing'] and fullq['generated_date_exact261025'],'Native mechanism differs')
    for stage in ('full','sta'):
        r=load(EXPERIMENT/f'stages/{stage}/result.json');m=load(EXPERIMENT/f'stages/{stage}/stage-manifest.json')
        require(r['state']=='terminal' and r['flow_exit_code']==0 and r['all_job_processes_terminal'] and r['all_handles_closed'] and r['errors']==[],'Native stage not closed')
        require(r['baseline_commit']==SOURCE and r['launcher_sha256']==GUARD and r['limits']==m['limits']==LIMITS and r['command']==m['command'],'Native guard/source/command changed')
        require(r['input_hashes_before']==m['bound_inputs'],'Native input inventory differs')
        for name,h in r['input_hashes_after'].items():
            if not Path(name).is_absolute():p.relative(name);require(trees[stage][name]['sha256']==h,'Final stage input differs')
    cleanup=load(EXPERIMENT/'terminal-task-cleanup.json')
    require(cleanup['exact_registered_action_verified'] and cleanup['exact_task_unregistered'] and cleanup['all_job_processes_terminal'] and cleanup['all_handles_closed'] and cleanup['errors']==[],'Exact task cleanup missing')
    require(cleanup['remaining_owned_or_quartus_processes']==[] and cleanup['last_task_result']==0,'Task not clean')
    matrix=staq['timing_condition_matrix'];p.matrix_check(matrix);require(result['timing_condition_matrix']==matrix,'Timing matrices differ')
    require(staq['qualified_clean_candidate'] is False,'Do not relabel this failed experiment')
    for name,h in [('sys/ascal.vhd',VARIANT),('output_files/STV_DS.rbf',RBF),('output_files/STV_DS.sof',SOF)]:
        require(trees['full'][name]['sha256']==trees['sta'][name]['sha256']==h,'Source/programming identity differs')
    reports={n[len('sta/reports/'):]:v for n,v in members.items() if n.startswith('sta/reports/')}
    require(len(reports)==117,'Actual STA report count changed')
    delta={n:v for n,v in trees['sta'].items() if trees['full'].get(n)!=v};deleted=sorted(set(trees['full'])-set(trees['sta']))
    require(len(delta)==19 and not deleted and all(n.startswith('db/') for n in delta),'STA derived-cache delta differs')
    source=load(EXPERIMENT/'input-manifest.json')['source_files'];require(len(source)==203,'Wrong compiled source subset')
    for n,row in source.items():
        expected=fullq['source_differences'].get(n,{}).get('after',row['sha256'])
        require(trees['full'][n]['sha256']==trees['sta'][n]['sha256']==expected,'Source/clock/SDC/PLL changed: '+n)
    return dict(p=p,bindings=bindings,seal=seal,members=members,trees=trees,result=result,matrix=matrix,reports=reports,delta=delta)
def partitions(rows,budget=85_000_000):
    chunks=[];count=total=0
    for n,v in sorted(rows.items()):
        require(v['bytes']<budget,'A checkpoint member exceeds the established raw budget')
        if total and total+v['bytes']>budget:chunks.append(dict(members=count,raw_bytes=total));count=total=0
        total+=v['bytes'];count+=1
    if total:chunks.append(dict(members=count,raw_bytes=total))
    return chunks
def plan(ctx):
    full=ctx['trees']['full'];groups={g:{n:v for n,v in full.items() if (n.startswith(prefix) if prefix else not n.startswith(('db/','incremental_db/')))} for g,prefix in [('checkpoint-db','db/'),('checkpoint-incremental-db','incremental_db/'),('checkpoint-project-and-outputs','')]}
    return dict(state='PLAN_ONLY_NO_DB_BYTES_PACKAGES_GIT_NATIVE_DEVICE_OR_ORIGINAL_WRITES',source_commit=SOURCE,seed=4,BUILD_DATE='261025',output=str(OUTPUT),
        checkpoint_files=1051,checkpoint_parts={g:partitions(v) for g,v in groups.items()},programming_package='One dedicated ZIP; genuine integrated-fullflow RBF/SOF, not inherited seed outputs',
        evidence_package='One source/control/evidence ZIP including all117 reports, all native logs/admissions/tools, frozen adapter, source receipts, peer terminal receipt and full1065-file STA hash snapshot',
        expected_ZIPs=7,STA_cache_bytes_excluded=sum(v['bytes'] for v in ctx['delta'].values()),STA_cache_files_excluded=19,
        exact_restore_scope='Full1051-file fresh source/map/fit/ASM checkpoint and every archived report/control member; not all2245 native-stage files or STA working DB',
        peer_terminal_review='INDEPENDENT-ROW-PREDECESSOR-NATIVE-R1-REVIEW.json included and pinned',constraint_cone_review='Actual cone review and root final terminal review included and pinned',
        no_timing_hardware_or_identical_rebuild_acceptance=True)
def root_review(path,digest):
    require(Path(path).is_absolute() and re.fullmatch('[0-9a-f]{64}',digest or '') and sha(path)==digest,'Actual absolute root review/hash required')
    r=load(path);require(r['reviewer']=='root' and r['decision']=='ACCEPTED_6EB_NATIVE_PRESERVATION_PACKAGER','Wrong root package admission')
    require(r['script_sha256']==sha(__file__) and r['metadata_bindings_sha256']==sha(BASE/'metadata-bindings.json') and r['provider_sha256']==PROVIDER_SHA,'Packager bindings differ')
    require(r['source_commit']==SOURCE and r['RBF_sha256']==RBF and r['full_checkpoint_files']==1051 and r['STA_reports']==117,'Wrong preservation scope')
    require(r['derived_STA_caches_excluded'] is True and r['not_all2245_files_remote_restorable'] is True,'STA omission must be explicit')
    extra={}
    for item in r['additional_review_files']:
        p=Path(item['path']);require(p.is_absolute() and p.resolve().parent==RESEARCH and sha(p)==item['sha256'],'Additional actual review changed')
        extra[p]=item['sha256']
    return r,extra
def create(ctx,review_path,review_sha):
    p=ctx['p'];review,extra=root_review(review_path,review_sha)
    require(not OUTPUT.exists(),'Preserve occupied package output; never overwrite or resume')
    # Creation, unlike --plan, verifies all local stage bytes before/after reading any archive inputs.
    before=p.snapshot(EXPERIMENT/'stages');require(before==ctx['members'],'Original stage bytes/membership changed')
    require((EXPERIMENT/'stages/full/tree/build_id.v').read_bytes()==b'`define BUILD_DATE "261025"','Date bytes changed')
    OUTPUT.mkdir();full=ctx['trees']['full'];packages={};fullprefix=TAG+'/checkpoint/tree/'
    p.save(OUTPUT/'FULL-SNAPSHOT.json',dict(files=full,file_count=1051,snapshot_sha256=p.digest(full)))
    p.save(OUTPUT/'STA-HASH-SNAPSHOT.json',dict(files=ctx['trees']['sta'],file_count=1065,derived_cache_delta=ctx['delta'],
        actual_STA_working_database_archived=False,derived_cache_files_remain_local=True))
    p.save(OUTPUT/'SEALED-LOCAL-STAGE-INDEX.json',ctx['seal'])
    manifest=dict(state='LOCAL_DRAFT_PENDING_ROOT_PACKAGE_REVIEW',source_commit=SOURCE,variant_exact_sha256=VARIANT,seed=4,BUILD_DATE='261025',
        native_matrix=ctx['matrix'],RBF=ctx['result']['RBF'],SOF=ctx['result']['SOF'],root_member_review_sha256=ctx['bindings'][str(RESEARCH/'ROOT-ROW-PREDECESSOR-NATIVE-MEMBER-REVIEW-R1.json')],
        root_create_admission_sha256=review_sha,additional_actual_reviews={str(k):v for k,v in extra.items()},
        terminal_and_cone_reviews={Path(k).name:v for k,v in ctx['bindings'].items() if any(t in Path(k).name for t in ('NATIVE-R1-REVIEW','NATIVE-CONE-REVIEW','NATIVE-FINAL-REVIEW','NATIVE-MEMBER-REVIEW'))},
        constraint_cone_review_status='Actual peer terminal, cone, root member and root final receipts included',
        full_checkpoint_files_archived=1051,STA_reports_archived=117,STA_cache_files_excluded=19,all2245_native_stage_files_remote_restorable=False,
        timing_acceptance=False,hardware_acceptance=False,remote_uploaded=False,bit_identical_rebuild_demonstrated=False)
    p.save(OUTPUT/'PRESERVATION-MANIFEST.json',manifest)
    text=['#6eb row-predecessor seed4 â€” failed experimental timing trial','',
        'Exact fresh fullflow source/map/fit/ASM checkpoint1051files retained. Dedicated programming ZIP is genuine integrated-ASM output.',
        'All117 actual all8 STA reports and native control/log evidence retained. The full1065-file STA snapshot is a hash inventory.',
        'Nineteen redundant derived STA-cache files remain local and are NOT archived. Do not claim all2245 native-stage files remotely restorable.',
        'Restore full checkpoint to a new empty directory using preserve.py --restore with a root-reviewed PACKAGE-INDEX SHA256. No overlay, delete, native build or project code runs.',
        'Exact existing binary/checkpoint restoration is supported; bit-identical recompilation, relocated DB tool usability, timing and hardware acceptance are not claimed.',
        'Keep all7ZIPs and every indexed sidecar. Missing final PACKAGE-INDEX.json means incomplete output. No upload is performed.',
        'Source6eb9367e2d64c18b0b109d221a0bc07d35d493b4, seed4, date261025; compare source7e9 seed4 separately. Overall timing is worse; original and baseline4 stay preserved.','',
        '|Model|C|Setup|Hold|Recovery|Removal|MPW|Result|','|---|---:|---:|---:|---:|---:|---:|---|']
    for row in ctx['matrix']:
        c=row['checks'];pw=row['minimum_pulse_width'];failed=[k for k in p.CHECKS if not c[k]['pass']]
        if pw['slack_ns']<0 or pw['violated']:failed.append('MPW')
        text.append('|'+ '|'.join([row['model'],str(row['temperature_C']),*[f"{c[k]['slack_ns']:+.3f}"for k in p.CHECKS],f"{pw['slack_ns']:+.3f}",'Fail '+','.join(failed)if failed else'Pass'])+'|')
    with(OUTPUT/'README.md').open('x',encoding='utf-8')as f:f.write('\n'.join(text)+'\n')
    groups={}
    for n in full:
        g='checkpoint-db'if n.startswith('db/')else'checkpoint-incremental-db'if n.startswith('incremental_db/')else'checkpoint-project-and-outputs'
        groups.setdefault(g,{})[fullprefix+n]=EXPERIMENT/'stages/full/tree'/n
    groups['programming']={TAG+'/programming/STV_DS.'+ext:EXPERIMENT/('stages/full/tree/output_files/STV_DS.'+ext)for ext in ('rbf','sof')}
    evidence={}
    for root,dirs,files in os.walk(EXPERIMENT,followlinks=False):
        if Path(root)==EXPERIMENT:dirs[:]=[d for d in dirs if d!='stages']
        for n in files:
            f=Path(root)/n;p.no_link(f);evidence[TAG+'/evidence/experiment/'+f.relative_to(EXPERIMENT).as_posix()]=f
    for n in ctx['members']:
        if '/tree/'not in n:evidence[TAG+'/evidence/stages/'+n]=EXPERIMENT/'stages'/n
    for path in ctx['bindings']:
        f=Path(path)
        if f.parent==RESEARCH:evidence[TAG+'/evidence/research/'+f.name]=f
    for f in extra:evidence[TAG+'/evidence/research/'+f.name]=f
    evidence[TAG+'/evidence/root-create-admission.json']=Path(review_path)
    for f in BASE.iterdir():
        if f.is_file():evidence[TAG+'/evidence/packager/'+f.name]=f
    for f in OUTPUT.iterdir():
        if f.is_file():evidence[TAG+'/evidence/preservation/'+f.name]=f
    for n,f in evidence.items():
        if f.suffix.lower()in('.json','.md','.tcl','.log','.py','.ps1','.txt','.xml'):require(not p.SECRET.search(f.read_bytes()),'Credential marker in selected evidence: '+n)
    groups['source-and-evidence']=evidence
    for group,entries in groups.items():
        for i,part in enumerate(p.partition(entries),1):
            name=f'{TAG}-DRAFT-{group}-{i:02}.zip';packages[name]=dict(group=group,**p.write_zip(OUTPUT/name,part))
    require(len(packages)==7,'Package count differs from reviewed7ZIP layout; stop incomplete draft')
    allmembers={}
    for pkg in packages.values():
        for n,row in pkg['members'].items():require(n not in allmembers,'Duplicate cross-package member');allmembers[n]=row
    require({n[len(fullprefix):]:v for n,v in allmembers.items()if n.startswith(fullprefix)}==full,'Exact full checkpoint archive coverage failed')
    reportprefix=TAG+'/evidence/stages/sta/reports/'
    require({n[len(reportprefix):]:v for n,v in allmembers.items()if n.startswith(reportprefix)}==ctx['reports'],'117-report archive coverage differs')
    require(p.snapshot(EXPERIMENT/'stages')==before,'Original native stage changed during packaging')
    for path,h in {**ctx['bindings'],**{str(k):v for k,v in extra.items()},str(Path(review_path)):review_sha}.items():require(sha(path)==h,'Bound evidence changed during packaging')
    p.save(OUTPUT/'MEMBER-HASHES.json',dict(source_commit=SOURCE,packages=packages))
    p.save(OUTPUT/'ORIGINAL-PRESERVATION-CHECK.json',dict(all2245_local_members_unchanged=True,full_checkpoint_member_union_exact=True,all117_reports_archived=True,
        omitted_derived_STA_cache_files=19,omitted_derived_STA_cache_bytes=sum(v['bytes']for v in ctx['delta'].values()),remote_upload=False))
    p.save(OUTPUT/'PACKAGE-INDEX.json',dict(state='LOCAL_DRAFT_PENDING_ROOT_PACKAGE_REVIEW',source_commit=SOURCE,seed=4,packager_sha256=sha(__file__),
        packages={n:{k:v for k,v in row.items()if k!='members'}for n,row in packages.items()},package_count=7,
        full_checkpoint_files=1051,STA_reports=117,all2245_native_stage_files_remote_restorable=False,
        sidecars={f.name:p.info(f)for f in OUTPUT.iterdir()if f.is_file()and f.suffix!='.zip'},remote_uploaded=False,
        timing_acceptance=False,hardware_acceptance=False,bit_identical_rebuild_demonstrated=False))
    return dict(output=str(OUTPUT),package_index_sha256=sha(OUTPUT/'PACKAGE-INDEX.json'),packages=7)
def verify(package_dir,index_sha):
    p=primitives();folder=Path(package_dir).resolve();require(sha(folder/'PACKAGE-INDEX.json')==index_sha,'Root-reviewed package index hash required')
    index=load(folder/'PACKAGE-INDEX.json');require(index['source_commit']==SOURCE and index['package_count']==7 and index['full_checkpoint_files']==1051,'Wrong package source/scope')
    for n,row in index['sidecars'].items():p.relative(n);p.no_link(folder/n);require(p.info(folder/n)==row,'Sidecar differs')
    records=load(folder/'MEMBER-HASHES.json')['packages'];require(set(records)==set(index['packages']),'ZIP inventory differs')
    union={};locations={}
    for name,pkg in records.items():
        p.relative(name);path=folder/name;p.no_link(path);require(p.info(path)=={k:pkg[k]for k in ('bytes','sha256')},'ZIP hash/size differs')
        require({k:v for k,v in pkg.items()if k!='members'}==index['packages'][name],'ZIP index metadata differs')
        with zipfile.ZipFile(path)as z:
            require(z.testzip()is None and z.namelist()==list(pkg['members']),'ZIP CRC/member list differs')
            for n,row in pkg['members'].items():
                p.relative(n);require(n not in union,'Duplicate cross-ZIP member');raw=z.read(n)
                require(dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())==row,'Archived member hash differs')
                union[n]=row;locations[n]=name
    prefix=TAG+'/checkpoint/tree/';full=load(folder/'FULL-SNAPSHOT.json')['files']
    require(len(full)==1051 and {n[len(prefix):]:v for n,v in union.items()if n.startswith(prefix)}==full,'Full checkpoint archive union differs')
    require(len({n for n in union if n.startswith(TAG+'/evidence/stages/sta/reports/')})==117,'STA report count differs')
    return p,folder,full,locations
def restore(package_dir,index_sha,target):
    p,folder,full,locations=verify(package_dir,index_sha);target=Path(target).resolve()
    require(target.parent==RESEARCH and target.name.startswith('row-predecessor-native-restore-')and not target.exists(),'Require exclusive new direct research restore directory')
    p.no_link(RESEARCH);require(len({n.casefold()for n in full})==1051,'Case-colliding restore paths')
    target.mkdir()
    for n,row in full.items():
        p.relative(n);member=TAG+'/checkpoint/tree/'+n;dst=target/n;require(dst.resolve().is_relative_to(target),'Restore path escaped target');dst.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(folder/locations[member])as z:raw=z.read(member)
        with dst.open('xb')as f:f.write(raw)
        require(p.info(dst)==row,'Restored file differs')
    require(p.snapshot(target)==full,'Exact restored1051-file tree differs')
    require(sha(target/'output_files/STV_DS.rbf')==RBF and sha(target/'output_files/STV_DS.sof')==SOF,'Restored programming differs')
    return dict(state='EXACT1051_FILE_RESTORE_VERIFIED_NO_NATIVE_BUILD',target=str(target),files=1051,RBF_sha256=RBF,SOF_sha256=SOF,bit_identical_rebuild_demonstrated=False)
def main():
    a=argparse.ArgumentParser(description=__doc__);g=a.add_mutually_exclusive_group();g.add_argument('--plan',action='store_true');g.add_argument('--create',action='store_true');g.add_argument('--verify',type=Path);g.add_argument('--restore',type=Path)
    a.add_argument('--review',type=Path);a.add_argument('--review-sha256');a.add_argument('--index-sha256');a.add_argument('--target',type=Path);args=a.parse_args()
    if args.restore:out=restore(args.restore,args.index_sha256,args.target)
    elif args.verify:
        _,_,full,_=verify(args.verify,args.index_sha256);out=dict(state='ARCHIVE_HASH_CRC_AND_MEMBER_UNION_VERIFIED',full_checkpoint_files=len(full))
    else:
        ctx=metadata();out=create(ctx,args.review,args.review_sha256)if args.create else plan(ctx)
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
