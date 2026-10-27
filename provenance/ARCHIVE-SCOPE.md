# Local release archive scope

These archives preserve actual recorded measurements and the original fitted project. They are not a new FPGA build, current hardware test journal or portable automatic launcher. No original file was edited.

The fitted-project folder is exactly the original 1,068-member, 278,810,761-byte checkpoint, including inherited historical release docs/packages, unused source files and compiler databases. The current single-RAM HDMI output is fitted-project/output_files/STV.rbf (SHA256 cda57070c2aefe4a21dcd7295ec448fbb9d5ada7051f020d3179caf8bc337d6b); inherited install/packages files are historical and are not the current install payload. The preserved dual-RAM release is separate.

Original source commit: 069ac39e319503557fb344d600d8b4ffbaa7f587. Quartus 25.1, project/revision STV, seed 1, fixed HDL build date 261025. A saved checkpoint preserves actual compiled bytes; a fresh future fit is not promised to reproduce the same layout/output.

Original-lab metadata/recipes contain local absolute paths, local tool hashes, preservation dependencies and historical preacceptance wording/false timing or hardware-acceptance flags. They are included unchanged as provenance. They require review/adaptation to run elsewhere. Tool executables, referenced external preservation assets and private hardware journals are not bundled. Current publication/hardware status is documented separately by the release maintainer.

No downloaded game ROM set or Saturn/ST-V system BIOS, private CFG/INI/save/NVM, hardware credentials or raw hardware journals are included. Existing source-tracked initialization data remain part of the exact checkpoint: five CD-controller firmware MIFs (rtl/Saturn/CD/sh7034.mif, rtl/cdb105.mif, rtl/cdb105m.mif, rtl/cdb106.mif, rtl/cdb106m.mif), FX68K micro/nanorom tables, PLL/Hq2x generated initialization and the source default ST-V EEPROM image. These tracked firmware files are explicitly retained, not claimed to be absent ROM-like data. The historical nested v1.1 ZIP contains docs, license, MRA and RBF only.

Timing archive: exact 61 current HDMI reports and 77 corrected baseline-R2 reports, report/input manifests, qualifications, native logs/results, reviewed STA methods and actual report audits/matrices. Failed baseline-R1 collector is excluded. Original successful fitted databases are in the checkpoint archive; tool-managed timing-working-copy databases are not substituted.

Full-range timing is not closed: current slow -40 C setup -0.148 ns and slow 0 C -0.091 ns remain. All other measured corners/check types are nonnegative, with the documented constraint/UCP/empty-path caveats. See the complete eight-condition matrices; no 25 C measurement is inferred.

ZIP reproducibility: sorted member paths, UTF-8 metadata, fixed ZIP timestamp 2026-10-27 00:00:00, Unix regular-file mode 0644, DEFLATE level 9, no filesystem timestamps/ACLs or ZIP comments. ARCHIVE-MEMBERS.json seals every other member; it intentionally cannot hash itself. Every source-derived member is read back against its original byte count and SHA256, and ZIP CRCs are checked.
