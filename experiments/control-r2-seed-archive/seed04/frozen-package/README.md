# Shienryu control R2 seed 4 — experimental preservation

Local draft awaiting root package review. Source `7e987bb9ef0361356be22be13551e4626902f3a7`; Quartus25.1 Lite/STV_DS, stored seed4, fixed generated build date `261025`. No complete-fix or hardware acceptance is claimed. No Git commit/upload or device action occurred.

The six checkpoint ZIPs contain every fit tree file (1050 files) and an11-file/zero-deletion assembler overlay reconstructing the exact1051-file assembled tree. Extract all fit-checkpoint parts together into a NEW empty directory, then apply the assembler overlay; its explicit deleted list is empty. `ASM-OVERLAY.json` binds both snapshots. Never overwrite previous seeds. Separate `programming/STV_DS.rbf` and `.sof` are genuine seed4 assembler outputs; copied fitter-only programming/STA files remain inherited seed1 artifacts.

Exact RBF/SOF restoration is supported by member hashes; bit-identical recompilation has not been demonstrated. Compatible Quartus/device support is required. Source/QSF/SDC/PLL/build date, full map/fitted/incremental DB, every96 actual all-corner report files, Tcls, guards, qualifications and root reviews are preserved. Negative-clock detailed reports are dynamic, so fewer failing conditions yield96 actual files versus seed3 count100; none are invented or omitted. Redundant analysis-local timing DB caches are omitted. All3284 sealed original seed4 members were rehashed before and after packaging.

Each ZIP is below100,000,000 bytes. Sorted POSIX members use fixed1980 timestamps, Unix0644 attributes and DEFLATE6; each ZIP was generated twice identically and allmember hashes/CRCs verified. Keep allZIPs and `MEMBER-HASHES.json`/`PACKAGE-INDEX.json` together.

Per-stage fit/ASM/STA owned Jobs are terminal and handles closed; the parent batch task is still active for separate seed5. Whole-batch task cleanup is pending and is NOT claimed by this seed archive. No seed5 tree/data was accessed. The index snapshot records pre-upload status. The frozen adapter bundle retains original paths and needs reviewed path/tool adaptation before reuse.

Safety: no externally sourced game/BIOS/runtime archives, device configurations or credentials added. Exact inherited tracked source MIF/microcode and metadata-only MRA files are retained; no content-level copyright clearance is asserted.

All eight conditions at1.1V are below. Recovery, removal and minimum pulse width pass throughout. Existing board-I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain in the root review.

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
