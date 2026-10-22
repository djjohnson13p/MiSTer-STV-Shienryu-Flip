# MiSTer ST-V: Shienryu 180 Flip

An experimental **dual-SDRAM** ST-V build with an optional 180-degree flip for Shienryu’s active game picture on the HDMI/scaler output. The option defaults to **Off**. The OSD keeps its separate orientation; this switch does not add 90-degree portrait rotation or transform direct analog/raw video.

## Download and install

1. Download [MiSTer-STV-Shienryu-Flip-v1.1.zip](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/tag/v1.1-share-20261022) from release **v1.1-share-20261022** and extract it on your computer.
2. Copy the **contents of `install/`** to your MiSTer SD card’s root, merging `_Arcade/`. The resulting files are:

   ```text
   _Arcade/cores/stv_flip_v1.1_rc1.rbf
   _Arcade/Shienryu stv_flip_v1.1_rc1.mra
   ```

3. Supply compatible `shienryu.zip` and `stvbios.zip` in `games/mame/`. The MRA lists the required ROM members and CRCs. **Game ROMs and BIOS files are not included.**
4. On MiSTer, open **Arcade → Shienryu stv_flip_v1.1_rc1**.
5. Open the OSD with **F12**, enter **Audio & Video**, then set **Shienryu 180 Flip → On**. Set it back to **Off** for the normal picture.

This separate core/MRA alias leaves the normal ST-V entry available. Keep both supplied filenames together: the MRA selects the `stv_flip_v1.1_rc1` core name.

## Version and status

The supplied `rc1` binary is **byte-identical to the original v1.1 Final**; its filename is retained for the matching restored launcher. This is a republication of the earlier contribution, with installation documentation, rather than a new core build.

Original testing reported successful Shienryu boot, HDMI flip, controls, coin/start, audio and gameplay. The recorded setup/hold margins are **−0.089 ns / −0.330 ns**, so this remains experimental and has **not achieved formal timing closure**.

See [source and test status](docs/SOURCE-AND-TEST-STATUS.md), [original release notes](docs/ORIGINAL-RELEASE-NOTES.md), and [credits and licenses](NOTICE.md). The [full source branch](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/tree/stv-flip-v1.1) preserves the original project.
