# Shienryu control R2 seed 9 — experimental DRAFT

Local package awaiting root review; no upload, root/package/hardware acceptance or bit-identical rebuild is granted.
Fixed source 7e987bb9ef0361356be22be13551e4626902f3a7, Quartus25.1 Lite/STV_DS, stored seed9, generated date261025.
The archived root measurement decision is: REVIEWED_SEED09_MEASUREMENT_NOT_HARDWARE_ACCEPTANCE

All 1050 fit/map/incremental files plus the exact 11-file ASM overlay reconstruct 1051 assembled files.
Extract every fit-checkpoint part into a NEW empty directory, apply the assembler overlay, and remove only its explicit deleted list. Never overwrite an original.
Programming/ contains the genuine ASM RBF/SOF; fitter-only copied outputs remain inherited seed1 files.
All 116 actual reports, native Jobs/qualification, source/QSF/SDC/PLL/date/tools/admissions/reviews are retained.
Only per-stage terminal/handle proofs are recorded; whole-batch scheduled-task cleanup is not implied.
Exact existing binary/checkpoint restoration is supported by hashes; bit-identical recompilation is unproven. Further analysis needs compatible tools/device support and reviewed path adaptation.
Each ZIP is below100,000,000 bytes, fixed1980/Unix0644/DEFLATE6, serialized twice identically, and every member hash/CRC verified.
Retain all parts and sidecars. An output lacking final PACKAGE-INDEX.json is incomplete and must not publish.
No externally sourced game/BIOS/runtime archives or credentials added. Exact inherited tracked MIF/microcode is retained without asserting content-level copyright clearance.

All eight conditions at1.1V follow. A reported0.000ns is zero visible margin, not positive margin. Inherited I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.305 | -0.530 | +3.785 | +0.648 | +1.091 | Fail setup,hold |
| Slow | 0 | -0.261 | -0.550 | +3.800 | +0.637 | +1.091 | Fail setup,hold |
| Slow | 85 | -0.341 | -0.568 | +3.674 | +0.689 | +1.091 | Fail setup,hold |
| Slow | 100 | -0.317 | -0.586 | +3.630 | +0.698 | +1.091 | Fail setup,hold |
| Fast | -40 | +3.491 | -0.308 | +5.208 | +0.260 | +1.091 | Fail hold |
| Fast | 0 | +3.394 | -0.310 | +5.156 | +0.267 | +1.091 | Fail hold |
| Fast | 85 | +2.998 | -0.307 | +4.967 | +0.296 | +1.091 | Fail hold |
| Fast | 100 | +3.035 | -0.307 | +4.905 | +0.302 | +1.091 | Fail hold |
