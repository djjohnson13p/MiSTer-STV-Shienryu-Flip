# Shienryu HDMI 180 Flip — single-SDRAM experimental build

A standalone **Shienryu-only, single-SDRAM-interface** ST-V build with **Shienryu 180 Flip**. It rotates the HDMI game picture by 180° while keeping the MiSTer menu independently oriented. This is experimental: cold-corner setup failures and timing-coverage caveats remain documented in [the full build and test record](BUILD-AND-TEST.md).

## Fresh single-RAM installation

**This package works independently. You do not need to install the dual-RAM branch, core or files first.** Start with a normally configured MiSTer, its SDRAM module and HDMI output.

1. Download [MiSTer-STV-Shienryu-Flip-single-ram-hdmi-20261027.zip](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/download/single-ram-v1.0-experimental-20261027/MiSTer-STV-Shienryu-Flip-single-ram-hdmi-20261027.zip) and extract it on your computer. This is the installation download; the source, saved-fit and timing archives are optional development records.
2. Open the extracted `install` folder and copy the `_Arcade` folder inside it to the MiSTer SD-card root, merging directories. Do **not** copy the enclosing `install` folder itself to the card. Create directories if they do not exist.
3. Put your compatible `shienryu.zip` game set and `stvbios.zip` ST-V BIOS set in `games/mame/`. Leave both ZIPs compressed. These are supplied separately; the MRA lists their exact members and CRCs.

The finished SD-card layout is:

```text
_Arcade/cores/SHYSHD01.rbf
_Arcade/_SingleRAM_Flip/SHYSHD01.mra
games/mame/shienryu.zip
games/mame/stvbios.zip
```

4. On MiSTer, open **Arcade → _SingleRAM_Flip → SHYSHD01** to start Shienryu.
5. Open the core menu with **F12**, then choose **Audio & Video → Shienryu 180 Flip → On**. Fresh settings default to **Off**. On rotates the game picture 180°; Off restores it. Use **Save settings** if you want to retain your choice. This adds no 90° rotation and makes no direct-analog-video promise.

The installation package supplies the RBF core and MRA launcher. Your game and system-BIOS ZIPs are the only additional content files required; no earlier Shienryu release or project-specific controller/settings files are needed.

### Optional: if you already have the dual-RAM version

You can keep it installed. The dual-RAM version uses `SHYF0004`; this single-RAM version uses `SHYSHD01` in its own menu folder. Its installation does not replace the dual-RAM core, launcher, settings or saves. If you have never installed the dual-RAM version, skip this note.

## Exact build and hardware scope

The exact supplied binary booted and passed P1/P2 movement, firing and bomb tests. Main saved Flip Off → On → Off with every other configuration bit unchanged. The owner independently tested the new single-RAM build and reported that HDMI rotation, menu orientation and sound worked as intended. Prepared automated physical-demo helpers were **not run**; the physical result is a human report, separate from the remote gameplay/configuration evidence.

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

The [separate dual-RAM seed 4 release](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/tag/v1.2-seed04-20261025) remains available and unchanged. The repository default branch still shows that version; this branch and the installation download linked above contain the single-RAM version.
