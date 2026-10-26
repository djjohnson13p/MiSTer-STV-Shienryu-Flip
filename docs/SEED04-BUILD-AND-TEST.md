# Seed4 build and preservation

Source: `7e987bb9ef0361356be22be13551e4626902f3a7`, branch `lab/shienryu-oldbase-hdmi`. This is the original experimental base plus the Shienryu/HDMI profile and synchronized, frame-held flip control. It is not the later row-predecessor experiment.

The compiled revision is `STV_DS`, Quartus Prime25.1std.0 Lite Edition, stored seed 4, placement effort 2.0, fixed generated `BUILD_DATE=261025`. The exact compiled QSF SHA256 is `29cd056b1113fdab5f30de9b378932f2ced2736f25713fea057befdf3fe9543e`; its source/clock/SDC/PLL inputs are retained in the source ZIP and full recovery checkpoint. No aggressive-hold option is added to this build.

The historical seed 4 flow starts from the fixed source 7e9 seed 1 synthesis/map snapshot, changes only the stored seed 1→4, qualifies native source/Post-Synthesis inputs (no Post-Fit) and zero requested/achieved placement/routing reuse, runs fitter-only, then fresh assembler and independent all8 STA. The complete archived fit tree has 1050 files; the exact 11-file assembler overlay reconstructs the 1051-file assembled checkpoint. The genuine SOF SHA256 is `506acff43a34289b123b79b5d8e4ae50af1ab0bb6fc4eae495bc64f43d4ac18f`.

For exact recovery use every indexed sidecar/ZIP and `restore_seed.py` in the verified recovery archive. Restore to a new empty directory and verify full member hashes; never merge into an old checkpoint. The 203-file compiled-source snapshot matches 202 source-commit Git blobs exactly; `STV_DS.qsf` alone contains the recorded compiler version/newline rewrite and stored seed 4. The generated build-date file is supplied separately and in the source ZIP. Historical documentation inside that exact source snapshot is retained for byte provenance; this publication README describes the selected build.

A new compilation from source is an unproven fresh rebuild, not an exact binary restoration. Preserve the provided RBF/SOF and checkpoint if exact existing bytes are required. No new build is needed to install the supplied RBF.

The MRA is the byte-identical hardware-tested SHYF0004 launcher. Header `00 01` preserves Shienryu mode0 and alternate BIOS selection; ROM/BIOS/EEPROM maps, rotation metadata and NVRAM index 4/size 65664 remain unchanged. Only metadata identifying the isolated SHYF0004 launcher differs from the canonical Shienryu MRA. ROM/BIOS data, saved CFG/NVRAM and per-device input maps are not included.

The user's exact confirmation was “audio video and flip work as intended”, bound by a read-only checkpoint to SHYF0004/RBF99654… and the exact supplied MRA. This does not assert reset/EEPROM-retention or full-range timing closure. The complete timing table is in the main README and `SEED04-STATUS.json`.
