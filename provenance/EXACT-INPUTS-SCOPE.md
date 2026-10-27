# Exact prepared build inputs — preservation scope

This archive preserves 208 exact prepared inputs for STV/STV seed 1, fixed BUILD_DATE 261025, compiled source commit 069ac39e319503557fb344d600d8b4ffbaa7f587 with Quartus 25.1. There are 207 Git-blob inputs and generated build_id.v. Their original paths and bytes are retained under exact-inputs/. INPUT-MANIFEST.json is the original unmodified manifest.

This is a build-input/preservation archive, not the current install package. Historical exact-inputs/install/ and exact-inputs/packages/ content, and inherited README/release notes, describe older artifacts. They are retained because they were prepared inputs. DO NOT copy those historical install/package files onto your MiSTer as the new single-RAM release. Use the separate new release install archive containing SHYSHD01.rbf and SHYSHD01.mra, and keep the existing dual-RAM SHYF0004 files intact.

Source-tracked controller initialization MIFs are retained byte-for-byte, including rtl/Saturn/CD/sh7034.mif and rtl/cdb105*.mif / rtl/cdb106*.mif, together with PLL and ST-V EEPROM initialization files. Their existing upstream source notices and licensing remain applicable. No externally supplied game ROM archive or ST-V/Saturn system-BIOS package has been added to this archive. No personal settings, saves, account credentials or downloaded game/BIOS payloads are added. The inherited historical package ZIP is also a source-tracked preserved input, not an installation instruction.

All ZIP entries use fixed 1980-01-01 00:00:00 metadata and regular-file mode 0644. This preserves the exact tested inputs; it does not guarantee that a fresh Quartus compilation produces bit-identical output. Original manifest and this scope note are also supplied as separate companion assets.
