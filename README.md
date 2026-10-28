# Shienryu HQ2x + HDMI 180 Flip — dual-SDRAM experimental build

A separate **Shienryu-only, dual-SDRAM** ST-V build with an **HQ2x** filter and **Shienryu 180 Flip** in the OSD. The flip rotates the HDMI game picture 180° while the MiSTer menu keeps its independent orientation. This is an experimental prerelease; the [build and test record](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/blob/dual-ram-hq2x-r1/BUILD-AND-TEST.md) explains the timing results and remaining coverage limits.

## Install

Start with a normally configured MiSTer with **two SDRAM modules** and HDMI output. An earlier Shienryu flip release is not required.

1. Download the [installation ZIP](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/download/dual-ram-hq2x-v1.0-experimental-20261028/MiSTer-STV-Shienryu-DualRAM-HQ2x-Flip-seed8-20261028.zip) and extract it on your computer. The exact-input source archive is for development.
2. Open its `install` folder and copy the enclosed `_Arcade` folder to the SD-card root, merging directories. Copy the folder's contents, not the enclosing `install` directory. Keep the new filenames so existing cores and profiles remain available.
3. Put compatible **standard, unmodified** `shienryu.zip` and `stvbios.zip` sets in `games/mame/`. Leave the ZIPs compressed. The supplied MRA lists the required members and CRCs. Game ROMs and BIOS files are supplied separately.

```text
_Arcade/cores/SHYHQ2X.rbf
_Arcade/_DualRAM_HQ2x_Flip/SHYHQ2X.mra
games/mame/shienryu.zip
games/mame/stvbios.zip
```

4. Open **Arcade → _DualRAM_HQ2x_Flip → SHYHQ2X**.
5. Press **F12**, open **Audio & Video**, and set **HQ2x → On** and **Shienryu 180 Flip → On**. Fresh settings start with both Off. Set either option to Off when desired. Choose **Save settings** to retain your choices.

HQ2x is intended for the game's progressive, low-resolution video; interlaced or high-resolution modes bypass it. The filter request is applied at a frame boundary. Flip adds no 90° portrait rotation, and this release's display qualification covers HDMI.

The public MRA selects core `SHYHQ2X` and uses the separate profile `SHYHQ2X`. It preserves the standard game's ROM layout. The corrected invincibility ROM used for extended development testing is **not required or included**. Personal CFG, controller maps and NVRAM are not installation payloads.

## Tested scope

The same frozen RTL configuration completed both game loops in two-player mode with **HQ2x On / Flip On**, using the **seed6** binary and corrected invincibility ROM. Both players reached `ALL`; the owner reported normal HDMI picture and sound. Seed8 separately booted and was handed to the owner for manual testing. The seed6 full-game result is not a full-game test of the selected seed8/9 binary.

|Supplied build|Identity|
|---|---|
|Selected fitting seed|`8`|
|Compiled source base|`7f88c496fbfbed6678171175f95a9279f737933f`|
|Quartus / project / revision|25.1 / `STV_DS` / `STV_DS`|
|RBF SHA256|`9f41129eb4beed7efbace2a0e7c288913b3bd194b3914089c899db3344a01124`|

Use `SHA256SUMS` and the publication manifest to identify the exact files. The new branch, tag and aliases keep this HQ2x prerelease separate from the existing dual-RAM flip and single-RAM releases. See [credits and licenses](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/blob/dual-ram-hq2x-r1/NOTICE.md).
