"""Root actual-member and native-report audit after the entire trial is closed."""
import importlib.util,json
from pathlib import Path
B=Path(__file__).resolve().parent
D=B/'row-predecessor-seed05-aggressive-hold-fit-sta-r1'
OLD=B/'row-predecessor-seed05-fit-sta-r1'
spec=importlib.util.spec_from_file_location('root_aggressive_hold_audit',D/'trial.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.validate();m.no_overlap()
r=m.load(D/'experiment-result.json');seal=m.load(D/'preservation-index.json')
assert r['state']=='COMPLETED_MEASUREMENT_REQUIRES_ROOT_REVIEW' and r['exit_code']==0
assert m.sha(D/'preservation-index.json')==r['preservation_index_sha256']
actual=m.snapshot(D/'stages');assert actual==seal['members']
m.check_snapshot(m.PARENT/'stages/full/tree',m.load(D/'parent-files.json'))
cleanup=m.load(D/'terminal-task-cleanup.json');assert cleanup['exact_task_unregistered'] and cleanup['errors']==[]
native={s:m.terminal(D/'stages'/s) for s in ('fit','asm','sta')}
start=m.load(D/'stages/fit/seed-start-files.json');roles=m.load(D/'trial-manifest.json')['roles']
protected=set().union(*(set(roles[k]) for k in ('source_names','generated_names','map_database_names')))
for stage in native:
 for name in protected:assert actual[stage+'/tree/'+name]==start[name]
 assert m.sha(D/'stages'/stage/'tree/STV_DS.qsf')=='ff61eae923d26ed3097ae2f61d8c1e527c1fa30243aca3ff0b43d42b1335fd19'
fq=m.load(D/'stages/fit/qualification.json');aq=m.load(D/'stages/asm/qualification.json')
assert fq['passed'] and fq['actual_placement_seed']==5 and fq['no_post_fit_input'] and fq['zero_requested_and_achieved_placement_and_routing']
setting=m.setting_acceptance(D/'stages/fit');assert setting==fq['experimental_setting_acceptance']
assert setting['accepted_input_no_rejection_observed'] and not setting['explicit_setting_rejections']
assert aq['passed'] and aq['fresh_RBF_and_SOF'] and aq['assembler_successful']
for name,row in aq['outputs'].items():
 assert actual['asm/tree/'+name]=={'bytes':row['bytes'],'sha256':row['sha256']}
sq=m.timing_and_targets(D/'stages/sta');assert sq['timing_condition_matrix']==r['timing_condition_matrix']
old=m.load(OLD/'experiment-result.json')
def values(rows):
 return [(x['model'],x['temperature_C'],x['status'],x['checks'],{k:v for k,v in x['minimum_pulse_width'].items() if k!='sha256'}) for x in rows]
assert values(r['timing_condition_matrix'])==values(old['timing_condition_matrix'])
rbf=D/'stages/asm/tree/output_files/STV_DS.rbf'
assert rbf.read_bytes()==(OLD/'stages/asm/tree/output_files/STV_DS.rbf').read_bytes()
receipt=dict(reviewer='root',utc=m.stamp(),decision='NO_MEASURED_IMPROVEMENT_RETAIN_BASELINE4_STOP_THIS_APPROACH',
 actual_all_stage_members_rehashed=len(actual),actual_all_stage_bytes=sum(x['bytes'] for x in actual.values()),
 source_copy_checks=len(roles['source_names'])*3,all_protected_source_map_date_inputs_unchanged=True,
 actual_parent1051_immutable_verified=True,frozen_external_tools_verified=True,
 native_stages={s:{k:v.get(k) for k in ('flow_exit_code','elapsed_seconds','peak_job_private_bytes','all_job_processes_terminal','all_handles_closed','errors')} for s,v in native.items()},
 setting_acceptance=setting,all8_numeric_matrix_identical_to_original5=True,
 all8=r['timing_condition_matrix'],RBF=r['RBF'],SOF=r['SOF'],RBF_actual_bytes_identical_to_original5=True,
 qualified_clean_candidate=False,no_new_hardware_test_or_deployment_warranted=True,
 result_sha256=m.sha(D/'experiment-result.json'),seal_sha256=m.sha(D/'preservation-index.json'),
 cleanup_sha256=m.sha(D/'terminal-task-cleanup.json'),no_further_trial_selected=True)
out=B/'ROOT-SEED05-AGGRESSIVE-HOLD-NATIVE-REVIEW-R1.json';m.save(out,receipt)
baseline=m.load(B/'ROOT-SEED04-TIMING-RESULT.json')['matrix']
by={(x['model'],x['temperature_C']):x for x in baseline}
lines=['# Shienryu aggressive-hold trial: no improvement','',
'The one authorized trial completed fitting, fresh assembly and all-eight timing analysis. Native input readback was ON, with no explicit setting rejection observed. The generated RBF is byte-for-byte identical to the original source6eb/seed5 RBF, and all eight numeric timing results are unchanged. This demonstrates no improvement for this build; it does not prove whether the backend consulted the option. The SOF hash differs; no explanation of that difference is assumed.','',
'Recommendation: stop this approach, retain the user-verified source7e9/seed4 candidate and preserve the original release. No additional seed, setting, RTL change or hardware deployment is selected. Full industrial-range timing closure remains unachieved.','',
'All values in ns at1.1V. Negative slack fails; every aggressive-hold row fails hold. Recovery/removal/minimum pulse width pass all8.','',
'| Model | C | Aggressive5 setup | Aggressive5 hold | Result | Preferred4 setup | Preferred4 hold |',
'|---|---:|---:|---:|---|---:|---:|']
for x in r['timing_condition_matrix']:
 y=by[(x['model'],x['temperature_C'])]
 lines.append(f"| {x['model']} | {x['temperature_C']} | {x['checks']['setup']['slack_ns']:+.3f} | {x['checks']['hold']['slack_ns']:+.3f} | {x['status']} | {y['checks']['setup']['slack_ns']:+.3f} | {y['checks']['hold']['slack_ns']:+.3f} |")
assert all(x['checks'][k]['pass'] for x in r['timing_condition_matrix'] for k in ('recovery','removal'))
assert all(x['minimum_pulse_width']['violated']==0 and x['minimum_pulse_width']['slack_ns']>=0 for x in r['timing_condition_matrix'])
lines+=['','The trial retained source6eb, mapped design, date261025, intended clocks/constraints, seed5 and all other settings. Only TDC_AGGRESSIVE_HOLD_CLOSURE_EFFORT ON was appended. The same13clocks/416clock rows/192qualified NAs/159normalized constraints and32mode/16predecessor queries remain covered. Native violated-path counts prevent rounded0.000 from being misreported as a pass.','',
'Every actual source/map/fit/ASM/report member is retained locally and will be preserved in the separate user-lab recovery archive. Exact fit/ASM restoration and remote raw-byte verification are required before claiming that backup complete. No new bitstream was deployed to MiSTer, and no default branch, original release, PR or author contact was changed.','']
p=B/'SHIENRYU-AGGRESSIVE-HOLD-TRIAL-RESULT.md'
with p.open('x',encoding='utf-8') as f:f.write('\n'.join(lines))
print(json.dumps({'review':str(out),'sha256':m.sha(out),'members':len(actual),'report':str(p),'identical_RBF':True,'improvement':False}))
