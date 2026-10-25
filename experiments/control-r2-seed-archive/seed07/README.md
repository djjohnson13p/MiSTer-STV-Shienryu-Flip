# Preserved Shienryu control R2 seed 7

Experimental timing result: hold passes all eight conditions, while setup fails all four Slow conditions. This seed was not promoted for hardware. Root verified the archive and restored all 1,051 assembled files, including the exact RBF/SOF. See ROOT-PACKAGE-REVIEW.json and ROOT-RESTORE-VALIDATION.json. Raw DRAFT labels remain historical packaging records.

Restore with Python 3.11+: `python restore_seed.py --seed 7 --out C:/new-empty-path/seed7`. The destination must not exist. Existing checkpoint restoration is verified; a bit-identical recompilation is unproven.

# Shienryu control R2 seed 7 — experimental DRAFT

Local package awaiting root review; no upload, root/package/hardware acceptance or bit-identical rebuild is granted.
Fixed source 7e987bb9ef0361356be22be13551e4626902f3a7, Quartus25.1 Lite/STV_DS, stored seed7, generated date261025.
The archived root measurement decision is: REVIEWED_SEED07_MEASUREMENT_NOT_HARDWARE_ACCEPTANCE

All 1050 fit/map/incremental files plus the exact 11-file ASM overlay reconstruct 1051 assembled files.
Extract every fit-checkpoint part into a NEW empty directory, apply the assembler overlay, and remove only its explicit deleted list. Never overwrite an original.
Programming/ contains the genuine ASM RBF/SOF; fitter-only copied outputs remain inherited seed1 files.
All 100 actual reports, native Jobs/qualification, source/QSF/SDC/PLL/date/tools/admissions/reviews are retained.
Only per-stage terminal/handle proofs are recorded; whole-batch scheduled-task cleanup is not implied.
Exact existing binary/checkpoint restoration is supported by hashes; bit-identical recompilation is unproven. Further analysis needs compatible tools/device support and reviewed path adaptation.
Each ZIP is below100,000,000 bytes, fixed1980/Unix0644/DEFLATE6, serialized twice identically, and every member hash/CRC verified.
Retain all parts and sidecars. An output lacking final PACKAGE-INDEX.json is incomplete and must not publish.
No externally sourced game/BIOS/runtime archives or credentials added. Exact inherited tracked MIF/microcode is retained without asserting content-level copyright clearance.

All eight conditions at1.1V follow. A reported0.000ns is zero visible margin, not positive margin. Inherited I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.164 | +0.181 | +3.383 | +0.962 | +1.091 | Fail setup |
| Slow | 0 | -0.123 | +0.184 | +3.380 | +0.955 | +1.091 | Fail setup |
| Slow | 85 | -0.121 | +0.208 | +3.218 | +0.973 | +1.091 | Fail setup |
| Slow | 100 | -0.085 | +0.196 | +3.161 | +0.967 | +1.091 | Fail setup |
| Fast | -40 | +3.404 | +0.043 | +4.901 | +0.368 | +1.091 | Pass |
| Fast | 0 | +3.311 | +0.059 | +4.823 | +0.387 | +1.091 | Pass |
| Fast | 85 | +3.046 | +0.095 | +4.568 | +0.435 | +1.091 | Pass |
| Fast | 100 | +2.956 | +0.098 | +4.491 | +0.451 | +1.091 | Pass |
