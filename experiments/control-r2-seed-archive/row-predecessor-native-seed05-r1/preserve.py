"""DRAFT fixed6eb/seed5 preservation. --plan never opens the running trial or its metadata.
Creation is root-gated after whole-trial terminal/cleanup. No Git, compiler or device action.
"""
import argparse,hashlib,importlib.util,json,math,os,re,sys,zipfile
from pathlib import Path
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent
RESEARCH=BASE.parent
TRIAL=RESEARCH/'row-predecessor-seed05-fit-sta-r1'
OUTPUT=RESEARCH/'row-predecessor-seed05-preservation-r1'
PROVIDER=BASE/'archive_primitives.py'
PROVIDER_SHA='1f4def931bdef7ccf1ed7c52de6418582b2e2e1b1bcdd729867da077816d52b3'
SOURCE='6eb9367e2d64c18b0b109d221a0bc07d35d493b4'
VARIANT='73ca65c64ef89e037e3995ca1faa56e3f7b8a1480b1a2f20190fb3d17b41ef57'
FROZEN='d398a7fec12cb60c64b9906ac33523cd9e11af766dd6fb0c0134a8acc8fc560b'
GUARD='5d287472358720e99822c57a5b576508af60ef5c41db5131ffe2ea5b78ec04c9'
TASK='CoreLab-Shienryu-RowPredecessor-Seed05-FitASMSTA-Q251-R1'
TAG='rowpred6eb-seed05'
STAGES=('fit','asm','sta')
SOURCE_CONTROL={
    'ROOT-ROW-PREDECESSOR-COMMITTED-SOURCE-R1.json':'bd2f054ac4b2bd5a1b786dc61c3c7e6927b5d19167aa1c3a0852d0378544ff2e',
    'ROOT-ROW-PREDECESSOR-SOURCE-REMOTE-VERIFICATION-R1.json':'78195e560d4f31c5f7e47f8e64c627ea30e10d8ceea49c6355ffd89816eb7078',
    'ROW-PREDECESSOR-ONE-SEED-HYPOTHESIS.json':'5eaa9cbd5521522ef191979b8d4f863fe9f5561ba7c4966e53ebefadc2fd6df3',
    'INDEPENDENT-ROW-PREDECESSOR-SEED05-ADAPTER-REVIEW.json':'ad5921021bc71297f1f2fa024d71c31a58657071617671201ef0e61d0b91c250'}
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
    s=importlib.util.spec_from_file_location('same_reviewed_archive_primitives',PROVIDER);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def native_matrix_check(matrix):
    # The frozen provider checks displayed slack. Retain its structural checks on
    # a display-only copy; actual pass/status also require native violation counts.
    p=primitives();require(isinstance(matrix,list),'Timing matrix must be a list')
    display=[]
    for row in matrix:
        require(type(row['temperature_C'])in(int,float),'Invalid condition temperature')
        require(set(row['checks'])==set(p.CHECKS),'Missing timing check')
        copied=dict(row);copied['checks']={}
        for kind,item in row['checks'].items():
            slack=item['slack_ns'];count=item['native_report_violated_paths']
            require(type(slack)in(int,float)and math.isfinite(slack),'Nonfinite/invalid native slack')
            require(type(count)is int and count>=0,'Native violation count must be a nonnegative integer')
            require(type(item['pass'])is bool and item['pass']==(slack>=0 and count==0),'Native pass/count mismatch')
            copied['checks'][kind]=dict(item,**{'pass':slack>=0})
        pw=row['minimum_pulse_width']
        require(type(pw['slack_ns'])in(int,float)and math.isfinite(pw['slack_ns']),'Invalid MPW slack')
        require(type(pw['violated'])is int and pw['violated']>=0 and type(pw['reported_paths'])is int and pw['reported_paths']>0,'Invalid MPW counts')
        passed=all(v['pass']for v in row['checks'].values())and pw['slack_ns']>=0 and pw['violated']==0
        require(row['status']==('PASS'if passed else'FAIL'),'Native row status mismatch')
        display.append(copied)
    p.matrix_check(display)
def plan():
    primitives()  # Local copied code only; never inspect TRIAL in this branch.
    return dict(state='DRAFT_PLAN_ONLY_NO_TRIAL_METADATA_TREE_REPORTS_COPY_FREEZE_PACKAGES_OR_ACTIONS',source_commit=SOURCE,seed=5,BUILD_DATE='261025',
        expected_frozen_adapter=FROZEN,output=str(OUTPUT),fit_files=None,assembled_files=None,STA_files=None,report_count=None,RBF=None,SOF=None,
        counts_and_hashes='PENDING; derive only from the future terminal native preservation-index and actual qualifications',
        layout='Fit checkpoint db/incremental/project parts + exact ASM changed/added overlay + source/programming/evidence; actual part count dynamic85MB raw/100MB ZIP',
        preservation='Exact fit and ASM tree restoration; genuine programming only if fresh ASM qualifies. Every actual STA report plus STA hash inventory. Redundant STA derived caches remain local.',
        outcomes='Preserve actual success/timing-failure/resource/infrastructure labels; partial artifacts remain unqualified. No timing/hardware or identical-rebuild claim.')
def review(path,digest):
    require(path is not None and Path(path).is_absolute() and re.fullmatch('[0-9a-f]{64}',digest or '') and sha(path)==digest,'Actual absolute root create review/hash required')
    r=load(path);require(r['reviewer']=='root' and r['decision']=='ACCEPTED_6EB_SEED05_PRESERVATION_PACKAGER','Wrong root create review')
    require(r['script_sha256']==sha(__file__) and r['provider_sha256']==PROVIDER_SHA and r['source_commit']==SOURCE and r['seed']==5,'Review bindings differ')
    require(r['derived_STA_caches_excluded'] is True and r['all_native_stage_files_remote_restorable'] is False,'Explicit archive scope required')
    required={'experiment-result.json','preservation-index.json','trial-manifest.json','frozen-pins.json','terminal-task-cleanup.json','scheduler-action-exit.json'}
    require(set(r['closed_trial_evidence'])==required,'Actual whole-trial terminal evidence required')
    bindings={}
    for name,h in r['closed_trial_evidence'].items():
        require(sha(TRIAL/name)==h,'Terminal control evidence changed: '+name);bindings[TRIAL/name]=h
    for item in r['actual_review_files']:
        p=Path(item['path']);require(p.is_absolute() and p.parent==RESEARCH and sha(p)==item['sha256'],'Actual external review absent/changed');bindings[p]=item['sha256']
    return r,bindings
def metadata(r,bindings):
    p=primitives();result=load(TRIAL/'experiment-result.json');seal=load(TRIAL/'preservation-index.json');m=load(TRIAL/'trial-manifest.json')
    for name,h in SOURCE_CONTROL.items():require(sha(RESEARCH/name)==h,'Fixed actual source/control evidence changed');bindings[RESEARCH/name]=h
    require(result['source_commit']==seal['source_commit']==m['source_commit']==SOURCE and result['seed']==seal['seed']==m['seed']==5,'Wrong trial source/seed')
    require(result['variant_exact_sha256']==m['variant_exact_sha256']==VARIANT and result['BUILD_DATE']==m['BUILD_DATE']=='261025','Wrong variant/date')
    require(sha(TRIAL/'frozen-pins.json')==FROZEN and result['preservation_index_sha256']==sha(TRIAL/'preservation-index.json'),'Wrong frozen adapter/native seal')
    require(m['limits']==seal['limits']==LIMITS and m['tool_bindings']==seal['tool_bindings'],'Guard/tool provenance changed')
    for name,h in load(TRIAL/'frozen-pins.json').items():p.relative(name);require(sha(TRIAL/name)==h,'Frozen trial input changed');bindings[TRIAL/name]=h
    cleanup=load(TRIAL/'terminal-task-cleanup.json')
    require(cleanup['task_name']==TASK and cleanup['exact_registered_action_verified'] and cleanup['exact_task_unregistered'],'Exact new task cleanup absent')
    require(cleanup['all_job_processes_terminal'] and cleanup['all_handles_closed'] and cleanup['errors']==[] and cleanup['remaining_owned_or_quartus_processes']==[],'Cleanup incomplete')
    require(cleanup['last_task_result']==load(TRIAL/'scheduler-action-exit.json')['exit_code']==result['exit_code'],'Scheduler/trial exit differs')
    members=seal['members'];trees={s:{n[len(s+'/tree/'):]:v for n,v in members.items()if n.startswith(s+'/tree/')}for s in STAGES}
    quals={};native={}
    for name in members:p.relative(name)
    for stage in STAGES:
        prefix=stage+'/'
        if prefix+'result.json' in members:
            q=load(TRIAL/'stages'/stage/'result.json');native[stage]=q
            if q.get('state')=='deferred-before-launch' and q.get('no_child_launched') is True:continue
            require(q['state']=='terminal' and q['all_job_processes_terminal'] and q['all_handles_closed'] and q['final_job_active_processes']==0,'Native stage not terminal/closed')
            require(q['baseline_commit']==SOURCE and q['launcher_sha256']==GUARD and q['limits']==LIMITS,'Native source/guard changed')
        if prefix+'qualification.json' in members:quals[stage]=load(TRIAL/'stages'/stage/'qualification.json')
    complete=seal['completed_native_sequence'];require(complete==(result['exit_code']==0),'Trial completion label differs')
    if not complete:require(r['allow_closed_partial_failure_backup'] is True,'Root must explicitly authorize unqualified partial backup')
    fq=quals.get('fit',{});aq=quals.get('asm',{});sq=quals.get('sta',{})
    fit_qualified=fq.get('passed') is True
    asm_qualified=aq.get('passed') is True and aq.get('fresh_RBF_and_SOF') is True
    if complete:
        require(set(native)==set(STAGES) and all(q['flow_exit_code']==0 and not q['errors'] for q in native.values()),'Complete sequence lacks native0 proof')
        require(fit_qualified and fq['actual_placement_seed']==5 and fq['no_post_fit_input'] and fq['zero_requested_and_achieved_placement_and_routing'],'Native fitter mechanism differs')
        require(asm_qualified and aq['assembler_successful'],'Fresh genuine ASM qualification missing')
        require(trees['fit']==load(TRIAL/'stages/fit/checkpoint.json') and trees['asm']==load(TRIAL/'stages/asm/checkpoint.json'),'Qualified snapshots differ from seal')
        require(all(trees[s]['sys/ascal.vhd']['sha256']==VARIANT and trees[s]['STV_DS.qsf']['sha256']==m['seed_start_QSF_sha256']for s in STAGES),'Actual RTL/QSF differs from fixed source/seed recipe')
        native_matrix_check(sq['timing_condition_matrix']);require(sq['timing_condition_matrix']==result['timing_condition_matrix'],'Actual timing matrix differs')
        for stage in STAGES:
            for name,h in native[stage]['input_hashes_after'].items():
                if not Path(name).is_absolute():p.relative(name);require(trees[stage][name]['sha256']==h,'Final protected native input differs')
        protected=set().union(*(set(m['roles'][k])for k in ('source_names','generated_names','map_database_names')))
        require(all(trees['fit'][n]==trees['asm'][n]==trees['sta'][n]for n in protected|{'db/STV_DS.cmp.cdb'}),'Source/date/map/primary fit changed across qualified copies')
    outputs={}
    if asm_qualified:
        for name,entry in aq['outputs'].items():
            p.relative(name);row={k:entry[k]for k in ('bytes','sha256')};require(trees['asm'][name]==row,'Genuine ASM output differs');outputs[name]=row
    reports={n[len('sta/reports/'):]:v for n,v in members.items()if n.startswith('sta/reports/')}
    if complete:require(reports and all(n in reports for n in ('corner-inventory.tsv','clock-check-coverage.tsv','global-check-coverage.tsv','old-mode-check-coverage.tsv','row-predecessor-check-coverage.tsv')),'Completed STA coverage evidence absent')
    changed={n:v for n,v in trees['asm'].items()if trees['fit'].get(n)!=v};deleted=sorted(set(trees['fit'])-set(trees['asm']))if trees['asm']else[]
    return dict(p=p,bindings=bindings,result=result,seal=seal,members=members,manifest=m,trees=trees,quals=quals,complete=complete,
        fit_qualified=fit_qualified,asm_qualified=asm_qualified,outputs=outputs,reports=reports,changed=changed,deleted=deleted)
def create(ctx,review_path,review_sha):
    p=ctx['p'];require(not OUTPUT.exists(),'Occupied output: never overwrite/resume')
    before=p.snapshot(TRIAL/'stages')if(TRIAL/'stages').exists()else{};require(before==ctx['members'],'Original local stage bytes/membership changed')
    if ctx['complete']:require((TRIAL/'stages/asm/tree/build_id.v').read_bytes()==b'`define BUILD_DATE "261025"','Date bytes changed')
    OUTPUT.mkdir();fit=ctx['trees']['fit'];asm=ctx['trees']['asm'];packages={};baseprefix=TAG+'/fit-checkpoint/tree/';overlayprefix=TAG+'/assembled-checkpoint-overlay/tree/'
    p.save(OUTPUT/'FIT-SNAPSHOT.json',dict(files=fit,file_count=len(fit),qualified_fitter_checkpoint=ctx['fit_qualified']))
    p.save(OUTPUT/'ASM-SNAPSHOT.json',dict(files=asm,file_count=len(asm),qualified_fresh_assembly=ctx['asm_qualified']))
    p.save(OUTPUT/'ASM-OVERLAY.json',dict(changed_or_added=ctx['changed'],deleted=ctx['deleted'],base_prefix=baseprefix,overlay_prefix=overlayprefix))
    p.save(OUTPUT/'STA-HASH-SNAPSHOT.json',dict(files=ctx['trees']['sta'],file_count=len(ctx['trees']['sta']),STA_working_DB_archived=False))
    p.save(OUTPUT/'REPORT-HASHES.json',ctx['reports']);p.save(OUTPUT/'SEALED-LOCAL-STAGE-INDEX.json',ctx['seal'])
    actual_state=ctx['result']['state'];manifest=dict(state='LOCAL_DRAFT_PENDING_ROOT_PACKAGE_REVIEW',source_commit=SOURCE,variant_exact_sha256=VARIANT,seed=5,BUILD_DATE='261025',
        actual_trial_state=actual_state,actual_trial_exit_code=ctx['result']['exit_code'],completed_native_sequence=ctx['complete'],
        fit_checkpoint_files=len(fit),assembled_files=len(asm),STA_hash_files=len(ctx['trees']['sta']),actual_STA_reports=len(ctx['reports']),
        fit_qualified=ctx['fit_qualified'],genuine_ASM_programming_qualified=ctx['asm_qualified'],genuine_ASM_outputs=ctx['outputs'],
        native_matrix=ctx['result'].get('timing_condition_matrix'),native_qualified_clean_candidate=ctx['result'].get('qualified_clean_candidate'),
        raw_native_labels_preserved=True,root_create_admission_sha256=review_sha,derived_STA_caches_remain_local=True,all_native_stage_files_remote_restorable=False,
        timing_acceptance=False,hardware_acceptance=False,bit_identical_rebuild_demonstrated=False,remote_uploaded=False)
    p.save(OUTPUT/'PRESERVATION-MANIFEST.json',manifest)
    lines=['#6eb seed5 — preserved actual trial, not acceptance','',f'Actual state: {actual_state}; native sequence complete: {ctx["complete"]}.',
        f'Fit tree {len(fit)} files (qualified={ctx["fit_qualified"]}); assembled tree {len(asm)} files (fresh ASM qualified={ctx["asm_qualified"]}).',
        f'All {len(ctx["reports"])} actual STA reports plus full {len(ctx["trees"]["sta"])}-file STA hash inventory retained; redundant derived STA caches remain LOCAL.',
        'Fit-tree programming files may be inherited; only programming/ contains qualified genuine ASM outputs, when available.',
        'Restore fit or assembled tree into a new empty directory; assembled mapping applies the explicit overlay/deletion inventory in memory, never deletes or overwrites originals.',
        'Snapshot/report/package counts and programming hashes come from the actual terminal seal; no inherited count assumption.',
        'Exact existing bytes can be restored; no bit-identical rebuild, timing/hardware acceptance or full native-stage remote restoration is claimed.',
        'Retain every ZIP and indexed sidecar. Missing final PACKAGE-INDEX.json means incomplete output. No upload is performed.','']
    if manifest['native_matrix']:
        lines+=['|Model|C|Setup|Hold|Recovery|Removal|MPW|Recorded result|','|---|---:|---:|---:|---:|---:|---:|---|']
        for row in manifest['native_matrix']:
            checks=row['checks'];pw=row['minimum_pulse_width'];lines.append('|'+ '|'.join([row['model'],str(row['temperature_C']),*[f"{checks[k]['slack_ns']:+.3f}"for k in p.CHECKS],f"{pw['slack_ns']:+.3f}",row['status']])+'|')
    with(OUTPUT/'README.md').open('x',encoding='utf-8')as f:f.write('\n'.join(lines)+'\n')
    groups={}
    for n in fit:
        group='checkpoint-db'if n.startswith('db/')else'checkpoint-incremental-db'if n.startswith('incremental_db/')else'checkpoint-project-and-outputs'
        groups.setdefault(group,{})[baseprefix+n]=TRIAL/'stages/fit/tree'/n
    if ctx['changed']:groups['assembled-checkpoint-overlay']={overlayprefix+n:TRIAL/'stages/asm/tree'/n for n in ctx['changed']}
    evidence={}
    for root,dirs,files in os.walk(TRIAL,followlinks=False):
        if Path(root)==TRIAL:dirs[:]=[d for d in dirs if d!='stages']
        for name in files:
            f=Path(root)/name;p.no_link(f);evidence[TAG+'/evidence/trial/'+f.relative_to(TRIAL).as_posix()]=f
    for n in ctx['members']:
        if '/tree/'not in n:evidence[TAG+'/evidence/stages/'+n]=TRIAL/'stages'/n
    for f in ctx['bindings']:
        if f.parent==RESEARCH:evidence[TAG+'/evidence/research/'+f.name]=f
    evidence[TAG+'/evidence/root-create-admission.json']=Path(review_path)
    for f in BASE.iterdir():
        if f.is_file():evidence[TAG+'/evidence/packager/'+f.name]=f
    for f in OUTPUT.iterdir():
        if f.is_file():evidence[TAG+'/evidence/preservation/'+f.name]=f
    for n in ctx['outputs']:evidence[TAG+'/programming/'+Path(n).name]=TRIAL/'stages/asm/tree'/n
    for n,f in evidence.items():
        if f.suffix.lower()in('.json','.md','.tcl','.log','.py','.ps1','.txt','.xml'):require(not p.SECRET.search(f.read_bytes()),'Credential marker in selected evidence: '+n)
    groups['source-programming-and-evidence']=evidence
    for group,entries in groups.items():
        for i,part in enumerate(p.partition(entries),1):
            name=f'{TAG}-DRAFT-{group}-{i:02}.zip';packages[name]=dict(group=group,**p.write_zip(OUTPUT/name,part))
    union={}
    for pkg in packages.values():
        for n,row in pkg['members'].items():require(n not in union,'Duplicate ZIP member');union[n]=row
    require({n[len(baseprefix):]:v for n,v in union.items()if n.startswith(baseprefix)}==fit,'Fit archive mapping differs')
    rebuilt=dict(fit)
    for n in ctx['deleted']:rebuilt.pop(n)
    rebuilt.update({n[len(overlayprefix):]:v for n,v in union.items()if n.startswith(overlayprefix)})
    if asm:require(rebuilt==asm,'Assembled archive mapping differs')
    reportprefix=TAG+'/evidence/stages/sta/reports/';require({n[len(reportprefix):]:v for n,v in union.items()if n.startswith(reportprefix)}==ctx['reports'],'Actual report mapping differs')
    require((p.snapshot(TRIAL/'stages')if(TRIAL/'stages').exists()else{})==before,'Original local trial stages changed')
    for f,h in ctx['bindings'].items():require(sha(f)==h,'Bound terminal/frozen/review evidence changed')
    require(sha(review_path)==review_sha,'Root create admission changed')
    p.save(OUTPUT/'MEMBER-HASHES.json',dict(source_commit=SOURCE,seed=5,packages=packages))
    p.save(OUTPUT/'ORIGINAL-PRESERVATION-CHECK.json',dict(all_actual_local_stage_members_unchanged=True,local_stage_members=len(before),
        exact_fit_mapping=True,exact_assembled_mapping=bool(asm),actual_reports_archived=len(ctx['reports']),all_native_stage_files_remote_restorable=False))
    p.save(OUTPUT/'PACKAGE-INDEX.json',dict(state='LOCAL_DRAFT_PENDING_ROOT_PACKAGE_REVIEW',source_commit=SOURCE,seed=5,packager_sha256=sha(__file__),
        packages={n:{k:v for k,v in row.items()if k!='members'}for n,row in packages.items()},package_count=len(packages),
        fit_checkpoint_files=len(fit),assembled_files=len(asm),actual_STA_reports=len(ctx['reports']),all_native_stage_files_remote_restorable=False,
        sidecars={f.name:p.info(f)for f in OUTPUT.iterdir()if f.is_file()and f.suffix!='.zip'},remote_uploaded=False,timing_acceptance=False,hardware_acceptance=False,bit_identical_rebuild_demonstrated=False))
    return dict(output=str(OUTPUT),package_index_sha256=sha(OUTPUT/'PACKAGE-INDEX.json'),packages=len(packages),actual_trial_state=actual_state)
def verify(folder,index_sha):
    p=primitives();folder=Path(folder).resolve();p.no_link(folder);require(sha(folder/'PACKAGE-INDEX.json')==index_sha,'Root-reviewed PACKAGE-INDEX hash required')
    index=load(folder/'PACKAGE-INDEX.json');require(index['source_commit']==SOURCE and index['seed']==5,'Wrong package identity')
    for n,row in index['sidecars'].items():p.relative(n);p.no_link(folder/n);require(p.info(folder/n)==row,'Sidecar differs')
    records=load(folder/'MEMBER-HASHES.json')['packages'];require(set(records)==set(index['packages'])and len(records)==index['package_count'],'ZIP inventory differs')
    union={};locations={}
    for name,pkg in records.items():
        p.relative(name);path=folder/name;p.no_link(path);require(p.info(path)=={k:pkg[k]for k in ('bytes','sha256')},'ZIP hash/size differs')
        require({k:v for k,v in pkg.items()if k!='members'}==index['packages'][name],'ZIP metadata differs')
        with zipfile.ZipFile(path)as z:
            require(z.testzip()is None and z.namelist()==list(pkg['members']),'CRC/member inventory differs')
            for n,row in pkg['members'].items():
                p.relative(n);require(n not in union,'Duplicate ZIP member');raw=z.read(n)
                require(dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())==row,'Archived member differs');union[n]=row;locations[n]=name
    fit=load(folder/'FIT-SNAPSHOT.json')['files'];asm=load(folder/'ASM-SNAPSHOT.json')['files'];overlay=load(folder/'ASM-OVERLAY.json')
    base=TAG+'/fit-checkpoint/tree/';over=TAG+'/assembled-checkpoint-overlay/tree/'
    require({n[len(base):]:v for n,v in union.items()if n.startswith(base)}==fit,'Fit member union differs')
    changed={n[len(over):]:v for n,v in union.items()if n.startswith(over)};require(changed==overlay['changed_or_added'],'ASM overlay union differs')
    rebuilt=dict(fit)
    for n in overlay['deleted']:p.relative(n);require(n in rebuilt,'Invalid ASM deletion inventory');rebuilt.pop(n)
    rebuilt.update(changed)
    if asm:require(rebuilt==asm,'Assembled member union differs')
    reports=load(folder/'REPORT-HASHES.json');prefix=TAG+'/evidence/stages/sta/reports/'
    require({n[len(prefix):]:v for n,v in union.items()if n.startswith(prefix)}==reports,'Actual report union differs')
    require(len(fit)==index['fit_checkpoint_files']and len(asm)==index['assembled_files']and len(reports)==index['actual_STA_reports'],'Dynamic counts differ')
    return p,folder,fit,asm,changed,locations
def restore(folder,index_sha,target,kind):
    p,folder,fit,asm,changed,locations=verify(folder,index_sha);target=Path(target).resolve();expected=fit if kind=='fit'else asm
    require(expected,'Requested stage has no archived tree')
    require(target.parent==RESEARCH and target.name.startswith('row-predecessor-seed05-restore-')and not target.exists(),'Require exclusive new restore directory')
    p.no_link(RESEARCH);require(len({n.casefold()for n in expected})==len(expected),'Case-colliding paths');target.mkdir()
    for n,row in expected.items():
        p.relative(n);prefix=TAG+('/assembled-checkpoint-overlay/tree/'if kind=='asm'and n in changed else'/fit-checkpoint/tree/');member=prefix+n
        dst=target/n;require(dst.resolve().is_relative_to(target),'Restore escaped target');dst.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(folder/locations[member])as z:raw=z.read(member)
        with dst.open('xb')as f:f.write(raw)
        require(p.info(dst)==row,'Restored member differs')
    require(p.snapshot(target)==expected,'Exact stage restoration differs')
    manifest=load(folder/'PRESERVATION-MANIFEST.json')
    if kind=='asm'and manifest['genuine_ASM_programming_qualified']:
        for n,row in manifest['genuine_ASM_outputs'].items():require(p.info(target/n)==row,'Restored genuine programming differs')
    return dict(state='EXACT_RECORDED_STAGE_TREE_RESTORED_NO_NATIVE_ACTION',stage=kind,files=len(expected),target=str(target),
        recorded_trial_state=manifest['actual_trial_state'],genuine_ASM_qualified=kind=='asm'and manifest['genuine_ASM_programming_qualified'],bit_identical_rebuild_demonstrated=False)
def main():
    a=argparse.ArgumentParser(description=__doc__);g=a.add_mutually_exclusive_group();g.add_argument('--plan',action='store_true');g.add_argument('--create',action='store_true');g.add_argument('--verify',type=Path);g.add_argument('--restore',type=Path)
    a.add_argument('--review',type=Path);a.add_argument('--review-sha256');a.add_argument('--index-sha256');a.add_argument('--target',type=Path);a.add_argument('--kind',choices=('fit','asm'),default='asm');args=a.parse_args()
    if args.restore:out=restore(args.restore,args.index_sha256,args.target,args.kind)
    elif args.verify:
        _,_,fit,asm,_,_=verify(args.verify,args.index_sha256);out=dict(state='ACTUAL_ARCHIVE_MEMBERS_VERIFIED',fit_files=len(fit),assembled_files=len(asm))
    elif args.create:
        r,bindings=review(args.review,args.review_sha256);out=create(metadata(r,bindings),args.review,args.review_sha256)
    else:out=plan()
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
