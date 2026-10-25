# Preserved Shienryu control R2 seed 5

EXPERIMENTAL failed timing trial from source `7e987bb9ef0361356be22be13551e4626902f3a7`, Quartus25.1 Lite, STV_DS seed5 and fixed build date `261025`. Seed5 is retained for recovery/comparison and is not selected for hardware. Seed4 has better reported setup and hold slack in every measured condition. No timing-clean, complete-fix or hardware acceptance claim.

Authoritative RBF:4,348,472 bytes, SHA256 `e65748acbb3a33e520bad90620c96c5d030ac9a6e9a3420f2fe3af51606a2cff`; SOF SHA256 `23798fdfa332d11ac07a5a02709395889e70b58fde0a20a1c2b94d6178b45bba`. Extract `seed05/programming/` from `frozen-package/control-r2-seed05-DRAFT-source-programming-and-evidence-01.zip`. Fitter-only copied programming files remain inherited seed1 artifacts.

All19 frozen draft files were copied byte-identically. Seven ZIPs preserve the complete1050-file fit/map/incremental checkpoint plus11-file assembler overlay to1051 exact assembled files, source/QSF/SDC/PLL/date/settings/tools, all96 actual timing reports and final measurement reviews. Frozen DRAFT/pre-upload status remains historical provenance. `frozen-package/PACKAGE-INDEX.json` and `MEMBER-HASHES.json` bind every file.

`INDEPENDENT-AGENT-PACKAGE-REVIEW.json` (SHA256 `c6a1778fba7420c323be58662a5b3af9cf921dc3ea5f49587a434075be21014d`) records the independent agent's actual fresh1051-file restore with exact RBF/SOF. `RESTORE-VALIDATION.json` attributes those facts to `agent:shienryu_constraints_review`; it is not root acceptance. `ROOT-PACKAGE-REVIEW.PROPOSED.json` remains a historical proposal; actual `ROOT-PACKAGE-REVIEW.json` records root acceptance after independent ZIP/member checks. `ROOT-RESTORE-VALIDATION.json` records root's additional actual full1051-file restore through the supplied helper.

To restore, use Python3.11+: `python restore_seed.py --seed 5 --out C:/new-empty-path/seed5`. The destination must not exist. The helper checks package/member hashes and every reconstructed byte, and never overwrites an existing build. It has exactly three seed-specific substitutions from seed4; root actually ran this helper and verified every restored byte and exact RBF/SOF. The independent agent also restored using its separately reviewed method. Exact checkpoint/binary restoration is demonstrated by the agent receipt. Bit-identical recompilation is unproven; further analysis needs the recorded compatible Quartus/device support and reviewed path adaptation.

All eight conditions at1.1V are below. Fast-40C hold0.000ns is zero reported margin, not positive visible margin. Recovery/removal/minimum pulse width pass throughout. Existing board-I/O/audio-reset/runtime-PLL and qualified simulation/custom-geometry limits remain.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Setup / hold |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.413 | +0.115 | +3.773 | +0.870 | +1.091 | FAIL / PASS |
| Slow | 0 | -0.350 | +0.133 | +3.770 | +0.858 | +1.091 | FAIL / PASS |
| Slow | 85 | -0.216 | +0.134 | +3.661 | +0.862 | +1.091 | FAIL / PASS |
| Slow | 100 | -0.204 | +0.117 | +3.618 | +0.858 | +1.091 | FAIL / PASS |
| Fast | -40 | +3.365 | +0.000 | +5.186 | +0.359 | +1.091 | PASS / PASS |
| Fast | 0 | +3.266 | +0.010 | +5.141 | +0.379 | +1.091 | PASS / PASS |
| Fast | 85 | +2.923 | +0.047 | +4.978 | +0.424 | +1.091 | PASS / PASS |
| Fast | 100 | +2.819 | +0.058 | +4.928 | +0.434 | +1.091 | PASS / PASS |

The three seed5 Jobs are terminal/closed; the separate parent batch continues and whole-batch cleanup is not claimed. No active seed6 tree/DB, device, compiler or Git mutation was used for this preparation. Exact inherited tracked source MIF/microcode remains; no externally sourced game/BIOS/runtime archive or credentials were added.
