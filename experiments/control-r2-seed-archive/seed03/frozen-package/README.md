# Shienryu control R2 seed 3 — experimental preservation

Local draft awaiting root package review. Source `7e987bb9ef0361356be22be13551e4626902f3a7`; Quartus25.1 Lite/STV_DS, stored seed3, fixed generated build date `261025`. No complete-fix or hardware acceptance is claimed. No Git commit/upload or device action occurred.

The six checkpoint ZIPs contain every fit tree file (1050 files) and an11-file/zero-deletion assembler overlay reconstructing the exact1051-file assembled tree. Extract all fit-checkpoint parts together into a NEW empty directory, then apply the assembler overlay; its explicit deleted list is empty. `ASM-OVERLAY.json` binds both snapshots. Never overwrite previous seeds. The separate `programming/STV_DS.rbf` and `.sof` are genuine seed3 assembler outputs; copied fitter-only programming/STA files remain inherited seed1 artifacts.

Exact RBF/SOF restoration is supported by member hashes; bit-identical recompilation has not been demonstrated. Compatible Quartus/device support is required. Source/QSF/SDC/PLL/build date, full map/fitted/incremental DB, all100 raw all-corner reports, Tcls, guards, qualifications and root reviews are preserved. Redundant analysis-local timing DB caches are omitted. All3288 sealed original seed3 members were rehashed before and after packaging.

Each ZIP is below100,000,000 bytes. Sorted POSIX members use fixed1980 timestamps, Unix0644 attributes and DEFLATE6; each ZIP was generated twice identically and allmember hashes/CRCs verified. Keep allZIPs and `MEMBER-HASHES.json`/`PACKAGE-INDEX.json` together.

Per-stage fit/ASM/STA owned Jobs are terminal and handles closed; the parent batch task is still active for a separate seed4. Whole-batch task cleanup is pending and is NOT claimed by this seed archive. No seed4 tree/data was accessed. The index snapshot records pre-upload status. The frozen adapter bundle retains original paths and needs reviewed path/tool adaptation before reuse.

Safety: no externally sourced game/BIOS/runtime archives, device configurations or credentials added. Exact inherited tracked source MIF/microcode and metadata-only MRA files are retained; no content-level copyright clearance is asserted.

All eight conditions at1.1V are below. Recovery, removal and minimum pulse width pass throughout. Existing board-I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain in the root review.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.441 | +0.145 | +3.697 | +0.960 | +1.091 | Fail setup |
| Slow | 0 | -0.388 | +0.150 | +3.737 | +0.953 | +1.091 | Fail setup |
| Slow | 85 | -0.358 | +0.181 | +3.432 | +1.029 | +1.091 | Fail setup |
| Slow | 100 | -0.328 | +0.172 | +3.342 | +1.039 | +1.091 | Fail setup |
| Fast | -40 | +3.347 | +0.054 | +5.228 | +0.406 | +1.091 | Pass |
| Fast | 0 | +3.255 | +0.066 | +5.173 | +0.416 | +1.091 | Pass |
| Fast | 85 | +2.983 | +0.091 | +4.985 | +0.490 | +1.091 | Pass |
| Fast | 100 | +2.896 | +0.102 | +4.923 | +0.501 | +1.091 | Pass |
