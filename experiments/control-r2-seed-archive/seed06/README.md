# Preserved Shienryu control R2 seed 6

Experimental measured failure, retained for recovery/comparison. Seed6 fails hold at all eight conditions and setup at all four Slow conditions; no hardware promotion or complete-fix claim. Native RBF SHA256 `f1415ad5d52066bc381a2f9e132e14a6cd35fdb10177777dee68062fae891134` (4,353,728 bytes).

All frozen package files are unchanged under frozen-package/. The raw DRAFT labels describe packaging-time state. Actual package acceptance belongs in ROOT-PACKAGE-REVIEW.json; actual restoration proof belongs in ROOT-RESTORE-VALIDATION.json. These records are not timing or hardware acceptance.

Root accepted package integrity after code/native/whole-ZIP and independent1218-member checks. Root actually restored all1051 assembled files with this helper and verified exact RBF/SOF; see ROOT-RESTORE-VALIDATION.json. To restore, use Python3.11+: `python restore_seed.py --seed 6 --out C:/new-empty-path/seed6`. Destination must not exist. The helper verifies all package/sidecar/member hashes and the full1051-file assembled checkpoint, without launching Quartus. This is exact existing checkpoint restoration, not a demonstrated bit-identical recompilation.

The complete raw package description and eight-condition results follow:

# Shienryu control R2 seed 6 — experimental DRAFT

Local package awaiting root review; no upload, root/package/hardware acceptance or bit-identical rebuild is granted.
Fixed source 7e987bb9ef0361356be22be13551e4626902f3a7, Quartus25.1 Lite/STV_DS, stored seed6, generated date261025.
The archived root measurement decision is: REVIEWED_SEED06_MEASUREMENT_NOT_HARDWARE_ACCEPTANCE

All 1050 fit/map/incremental files plus the exact 11-file ASM overlay reconstruct 1051 assembled files.
Extract every fit-checkpoint part into a NEW empty directory, apply the assembler overlay, and remove only its explicit deleted list. Never overwrite an original.
Programming/ contains the genuine ASM RBF/SOF; fitter-only copied outputs remain inherited seed1 files.
All 106 actual reports, native Jobs/qualification, source/QSF/SDC/PLL/date/tools/admissions/reviews are retained.
Only per-stage terminal/handle proofs are recorded; whole-batch scheduled-task cleanup is not implied.
Exact existing binary/checkpoint restoration is supported by hashes; bit-identical recompilation is unproven. Further analysis needs compatible tools/device support and reviewed path adaptation.
Each ZIP is below100,000,000 bytes, fixed1980/Unix0644/DEFLATE6, serialized twice identically, and every member hash/CRC verified.
Retain all parts and sidecars. An output lacking final PACKAGE-INDEX.json is incomplete and must not publish.
No externally sourced game/BIOS/runtime archives or credentials added. Exact inherited tracked MIF/microcode is retained without asserting content-level copyright clearance.

All eight conditions at1.1V follow. A reported0.000ns is zero visible margin, not positive margin. Inherited I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.310 | -0.517 | +4.255 | +0.857 | +1.091 | Fail setup,hold |
| Slow | 0 | -0.261 | -0.548 | +4.241 | +0.847 | +1.091 | Fail setup,hold |
| Slow | 85 | -0.347 | -0.586 | +4.094 | +0.919 | +1.091 | Fail setup,hold |
| Slow | 100 | -0.317 | -0.608 | +4.059 | +0.926 | +1.091 | Fail setup,hold |
| Fast | -40 | +3.482 | -0.347 | +5.381 | +0.231 | +1.091 | Fail hold |
| Fast | 0 | +3.405 | -0.346 | +5.329 | +0.242 | +1.091 | Fail hold |
| Fast | 85 | +3.186 | -0.344 | +5.153 | +0.304 | +1.091 | Fail hold |
| Fast | 100 | +3.097 | -0.341 | +5.095 | +0.309 | +1.091 | Fail hold |
