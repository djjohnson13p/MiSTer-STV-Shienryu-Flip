# Shienryu HDMI 180 Flip — single-SDRAM experimental build

An isolated **Shienryu-only, single-SDRAM-interface** ST-V build with the existing **Shienryu 180 Flip** option. It rotates the HDMI game picture by 180° while keeping the MiSTer menu independently oriented. This is an experimental prerelease: the fitted design still has cold-corner setup failures and recorded timing-coverage caveats. See [the full build and test record](BUILD-AND-TEST.md).

The exact supplied binary booted and passed P1/P2 movement, firing and bomb tests. Main saved Flip Off → On → Off with every other configuration bit unchanged. The owner independently tested the new single-RAM build and reported that HDMI rotation, menu orientation and sound worked as intended. Prepared automated physical-demo helpers were **not run**; the physical result is a human report, separate from the remote gameplay/configuration evidence.

## Install alongside the dual-RAM version

Copy the supplied `install/` contents to the MiSTer SD-card root, merging directories:

```text
_Arcade/cores/SHYSHD01.rbf
_Arcade/_SingleRAM_Flip/SHYSHD01.mra
```

Supply compatible `shienryu.zip` and `stvbios.zip` in `games/mame/`; the MRA lists the exact members and CRCs. Open the new entry in **Arcade → _SingleRAM_Flip**, then **Audio & Video → Shienryu 180 Flip**. The default is **Off**; **On** rotates the game picture 180° and **Off** restores it. This adds no 90° rotation and makes no direct-analog-video promise.

**Keep the existing dual-RAM `SHYF0004` core, launcher, settings and saves.** This uses a different alias and directory; it is an additional option. Install only the two supplied new files. The install payload includes no personal input maps, settings, saves, game ROMs, ST-V system BIOS or credentials. Game and system-BIOS data are supplied separately.

## Exact build and hardware scope

|Item|Identity|
|---|---|
|Compiled source|`069ac39e319503557fb344d600d8b4ffbaa7f587`|
|Quartus/project/revision|25.1 / `STV` / `STV`|
|Seed / fixed BUILD_DATE|`1` / `261025`|
|RBF SHA256|`cda57070c2aefe4a21dcd7295ec448fbb9d5ada7051f020d3179caf8bc337d6b`|
|MRA SHA256|`363429d08b7b46ab0991c71e8bda3892cefceb4db4a9adf8cc0ec2dbe991e449`|

Testing used a **first-generation MiSTer Pi fitted with two SDRAM modules**, running a netlist that exposes only the primary SDRAM interface. A board physically fitted with only one module was **not tested**. This profile retains some analog-related hierarchy; it does not claim complete analog removal or support for other ST-V games.

The archived exact inputs and saved fit preserve the tested output. A fresh recompile is not claimed to reproduce identical RBF bytes. See [machine-readable validation](VALIDATION.json) and [credits/licenses](NOTICE.md).

## Downloads and preserved provenance

[Single-RAM release assets](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/tag/single-ram-v1.0-experimental-20261027) include the install ZIP, standalone RBF/MRA, exact 208 prepared inputs, full saved fit and original timing reports. `PUBLICATION-MANIFEST.json` and `SHA256SUMS` identify the assets.

Use the install ZIP for the SD card. The exact-input and fit archives preserve inherited historical install/packages files under archival prefixes; those are not current install payloads. Existing source-tracked CD-controller firmware/default initialization tables are retained in source/checkpoint archives. No externally supplied game ROM or Saturn/ST-V system BIOS is bundled. See [archive scope](provenance/ARCHIVE-SCOPE.md).

The [preferred dual-RAM seed 4 release](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/tag/v1.2-seed04-20261025) remains available and unchanged. The repository default branch is unchanged. This branch is the separate single-RAM variant.
