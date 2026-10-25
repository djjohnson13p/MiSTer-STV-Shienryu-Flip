# Shienryu control R2 seed 5 — failed timing trial preserved

EXPERIMENTAL local draft awaiting root package review. Source `7e987bb9ef0361356be22be13551e4626902f3a7`; Quartus25.1 Lite/STV_DS, stored seed5, fixed generated build date `261025`. Seed5 is not an improvement over seed4 and is not selected for hardware. No complete-fix, hardware acceptance, Git upload or device action is claimed.

All1050 fit tree files and an11-file/zero-deletion assembler overlay reconstruct the exact1051-file assembled tree. Extract all fit-checkpoint parts together into a NEW empty directory, then apply the exact assembler overlay; its deleted list is empty. `ASM-OVERLAY.json` binds both snapshots. Never overwrite earlier seeds. Separate `programming/STV_DS.rbf` and `.sof` are genuine seed5 assembler outputs; copied fitter-only programming/STA files remain inherited seed1 artifacts.

Exact RBF/SOF restoration is supported by hashes; bit-identical recompilation has not been demonstrated. Compatible Quartus/device support is required. Canonical source, working QSF/SDC/PLL/build date, full map/fitted/incremental DB, all96 actual all-corner report files, Tcls, guards, qualifications and root reviews are preserved. Negative-clock detailed reports are dynamic; actual count96 is verified without assuming earlier counts. Redundant analysis-local timing DB caches are omitted. All3284 sealed seed5 members were rehashed before and after packaging.

Every ZIP is below100,000,000 bytes. Sorted POSIX members have fixed1980 timestamps, Unix0644 attributes and DEFLATE6; every ZIP was generated twice identically and allmember hashes/CRCs verified. Keep allZIPs and `MEMBER-HASHES.json`/`PACKAGE-INDEX.json` together.

Fit/ASM/STA owned Jobs are terminal with handles closed; the parent batch continues with separate seed6. Whole-batch cleanup is pending and is NOT claimed here. No seed6 tree/data was accessed, no original index or sealed file was edited. The root index is a pre-upload snapshot. The frozen adapter retains original paths and needs reviewed path/tool adaptation before reuse.

Safety: no externally sourced game/BIOS/runtime archives, device configurations or credentials added. Exact inherited tracked source MIF/microcode and metadata-only MRA files are retained; no content-level copyright clearance is asserted.

All eight conditions at1.1V follow. A reported0.000ns is zero reported margin; do not describe it as robust positive margin. Root zero-margin qualification: Fast -40C nativehold0.000ns/50paths/0violations passes at reportedprecision; no positive visible margin.. Existing board-I/O/audio-reset/runtime-PLL and simulation/custom-geometry qualifications remain in the root review.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.413 | +0.115 | +3.773 | +0.870 | +1.091 | Fail setup |
| Slow | 0 | -0.350 | +0.133 | +3.770 | +0.858 | +1.091 | Fail setup |
| Slow | 85 | -0.216 | +0.134 | +3.661 | +0.862 | +1.091 | Fail setup |
| Slow | 100 | -0.204 | +0.117 | +3.618 | +0.858 | +1.091 | Fail setup |
| Fast | -40 | +3.365 | +0.000 | +5.186 | +0.359 | +1.091 | Pass |
| Fast | 0 | +3.266 | +0.010 | +5.141 | +0.379 | +1.091 | Pass |
| Fast | 85 | +2.923 | +0.047 | +4.978 | +0.424 | +1.091 | Pass |
| Fast | 100 | +2.819 | +0.058 | +4.928 | +0.434 | +1.091 | Pass |
