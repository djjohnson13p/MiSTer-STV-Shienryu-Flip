# Shienryu control R2 seed preservation — local drafts

Source: `7e987bb9ef0361356be22be13551e4626902f3a7`; Quartus 25.1 Lite; STV_DS; fixed build date `261025`. Each seed is separate. These ZIPs are local drafts awaiting root package review; compiled artifacts have not been uploaded. Original and installed releases are unchanged.

Exact RBF/SOF restoration is supported by member SHA256 hashes. A bit-identical rebuild has **not** been demonstrated. Keep the complete checkpoint, source/settings, generated date, tool identities and all ZIP parts together. Compatible installed Quartus tools/device support remain necessary for further analysis.

Seed 1: extract all checkpoint parts together into a new empty directory. Seed 2: extract all fit-checkpoint parts, then the assembler overlay; apply its explicit deletion list (currently 0). `ASM-OVERLAY.json` binds both complete snapshots. Do not overwrite an original build. The separate `programming/` files are authoritative outputs; seed 2 fitter-only copied RBF/STA files are inherited seed 1 artifacts. Use all-corner reports under evidence, not copied single-corner reports, for timing assessment.

Full original map/fitted/incremental databases are included without filtering: seed 1 1051 files; seed 2 fit 1050 files plus exact assembler overlay reconstructing 1051 files. Redundant STA working-tree caches are omitted; every raw all-corner report, Tcl, manifest, guard record, task cleanup and final root timing review is included. Original full checkpoints were rehashed before and after packaging and matched.

Each ZIP is below 100,000,000 bytes, sorted with fixed timestamps/attributes, and was serialized twice identically. Every member SHA256 and ZIP CRC was verified. Per-seed `MEMBER-HASHES.json` plus root `PACKAGE-INDEX.json` bind files; the final root review remains pending.

Safety: no externally sourced game/BIOS/runtime archives, hardware configuration files or credentials were added. Exact inherited tracked source MIF/microcode members are retained and listed in `SAFETY-AUDIT.json`; this is not content-level copyright clearance. MRA members contain metadata. No device access, native compilation, Git commit or push occurred.

Both seeds remain **EXPERIMENTAL**, not timing-clean or hardware-accepted. At 1.1V, all eight analyzed conditions are listed below. Recovery/removal/minimum-pulse-width are positive in both seeds (seed 1 reported MPW minimum +1.091ns; seed 2 each corner +1.091ns). Inherited I/O/audio-reset/runtime-PLL qualifications and simulation/custom-geometry limits remain in final root reviews.

| Model | C | Seed 1 setup ns | Seed 1 hold ns | Seed 1 result | Seed 2 setup ns | Seed 2 hold ns | Seed 2 result |
| --- | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Slow | -40 | -0.489 | +0.063 | Fail setup | +0.009 | -0.661 | Fail hold |
| Slow | 0 | -0.406 | +0.069 | Fail setup | +0.092 | -0.692 | Fail hold |
| Slow | 85 | -0.156 | +0.142 | Fail setup | +0.237 | -0.711 | Fail hold |
| Slow | 100 | -0.237 | +0.132 | Fail setup | +0.204 | -0.733 | Fail hold |
| Fast | -40 | +3.554 | +0.003 | Pass | +3.656 | -0.390 | Fail hold |
| Fast | 0 | +3.466 | +0.010 | Pass | +3.571 | -0.392 | Fail hold |
| Fast | 85 | +3.227 | +0.041 | Pass | +3.322 | -0.394 | Fail hold |
| Fast | 100 | +3.103 | +0.053 | Pass | +3.241 | -0.392 | Fail hold |
