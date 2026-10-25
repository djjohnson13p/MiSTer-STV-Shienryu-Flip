# Preserved Shienryu control R2 seed 4

Source7e987bb (olderbase, Shienryu-only/HDMI-only profile), Quartus25.1Lite, date261025. Leading provisional indoor-use candidate. Six measured conditions pass; onlySlow-40/0Csetup remainnegative. Full-range timing/hardware acceptance is not claimed. Original release remains unchanged.

Authoritative RBF:4,376,812bytes, SHA256 `99654dbf7a472b610f840f9dbbb0087bc6f508ce3dfdfe2ffbd48e6df5396d11`, inside `frozen-package/control-r2-seed04-DRAFT-source-programming-and-evidence-01.zip` under `seed04/programming/`. Copied fitter-only programming files are inherited earlier artifacts; use this separately generated binary.

To restore the complete assembled checkpoint, download every file in this directory including all seven ZIPs. Python3.11+: `python restore_seed.py --seed 4 --out C:/new-empty-path/seed4`. Output must not exist. The helper verifies package/member hashes, applies the explicit assembler overlay in a new folder and verifies all1051restored files. Compatible Quartus tools/device support remain needed for analysis; bit-identical recompilation is unproven.

ROOT-PACKAGE-REVIEW.json records independent package checks. Frozen packaging metadata retains original pre-upload DRAFT/status fields. All96 actual STA report files are included; fewer negative-clock detail files reflect fewer failing conditions. Earlier seeds remain intact. The parent's batch may continue later seeds; seed4's own Jobs are terminal/closed.

All analyzed1.1Vconditions:

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.101 | +0.174 | +3.437 | +0.932 | +1.091 | Fail setup |
| Slow | 0 | -0.038 | +0.172 | +3.451 | +0.928 | +1.091 | Fail setup |
| Slow | 85 | +0.070 | +0.242 | +3.334 | +0.999 | +1.091 | Pass |
| Slow | 100 | +0.014 | +0.235 | +3.292 | +1.006 | +1.091 | Pass |
| Fast | -40 | +3.441 | +0.052 | +5.034 | +0.411 | +1.091 | Pass |
| Fast | 0 | +3.350 | +0.054 | +4.977 | +0.426 | +1.091 | Pass |
| Fast | 85 | +2.972 | +0.089 | +4.761 | +0.474 | +1.091 | Pass |
| Fast | 100 | +2.923 | +0.093 | +4.697 | +0.487 | +1.091 | Pass |
