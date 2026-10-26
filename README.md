# MiSTer Shienryu: HDMI 180° Flip — seed 4

Experimental **Shienryu-only, HDMI-only, dual-SDRAM** build. This is the preferred tested seed 4 from source `7e987bb9ef0361356be22be13551e4626902f3a7`. The user confirmed that audio, video and flip work as intended on a first-generation MiSTer Pi with dual SDRAM. This build has **not achieved full-range timing closure**: Slow −40°C setup is−0.101 ns and Slow 0°C setup is−0.038 ns. Hold passes at every analyzed condition.

## Install

1. Download `packages/MiSTer-STV-Shienryu-Flip-seed04-20261025.zip` from this repository and extract it on your computer.
2. Back up your existing Shienryu core, MRA and settings. Copy the **contents of `install/`** to the MiSTer SD-card root, merging `_Arcade/`. The exact tested files are:

   ```text
   _Arcade/cores/SHYF0004.rbf
   _Arcade/SHYF0004.mra
   ```

3. Supply your compatible `shienryu.zip` and `stvbios.zip` under `games/mame/`. The MRA lists the required members and CRCs. Game ROMs and BIOS files are not included.
4. Open the supplied Shienryu entry. Its retained tested description is `CoreLab Shienryu HDMI-only flip candidate SHYF0004`.
5. Press **F12**, enter **Audio & Video**, and set **Shienryu180 Flip** to **On** or **Off**. The option defaults to Off with fresh settings. Use ordinary **Save settings** to retain your choice; existing settings may already retain On.

Keep the RBF and MRA names together. `SHYF0004` is also the separate settings/save namespace; do not overwrite an older variant's save files. Standard MiSTer input mapping applies. This feature rotates the active game picture 180° through the HDMI scaler; OSD orientation is separate. This profile supports Shienryu only. It adds no 90° rotation or analog/direct-video support.

## Validation and timing

Remote boot/menu/gameplay checks and the user's physical audio/video/flip confirmation belong to this exact RBF/MRA pair. Pre-scaler screenshots alone do not prove physical HDMI rotation. Reset/EEPROM retention and every custom display geometry have not been fully verified. No 25°C static measurement or universal hardware compatibility is inferred from the results below.

All measured conditions are at 1.1 V. Recovery, removal and minimum pulse width pass throughout. These are design timing results with inherited coverage qualifications, not complete board/industrial signoff.

| Model | °C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.101 | +0.174 | +3.437 | +0.932 | +1.091 | Fail setup |
| Slow | 0 | -0.038 | +0.172 | +3.451 | +0.928 | +1.091 | Fail setup |
| Slow | 85 | +0.070 | +0.242 | +3.334 | +0.999 | +1.091 | Pass |
| Slow | 100 | +0.014 | +0.235 | +3.292 | +1.006 | +1.091 | Pass |
| Fast | -40 | +3.441 | +0.052 | +5.034 | +0.411 | +1.091 | Pass |
| Fast | 0 | +3.350 | +0.054 | +4.977 | +0.426 | +1.091 | Pass |
| Fast | 85 | +2.972 | +0.089 | +4.761 | +0.474 | +1.091 | Pass |
| Fast | 100 | +2.923 | +0.093 | +4.697 | +0.487 | +1.091 | Pass |

## Source, recovery and earlier release

The exact RBF SHA256 is `99654dbf7a472b610f840f9dbbb0087bc6f508ce3dfdfe2ffbd48e6df5396d11` (4,376,812 bytes). The exact tested MRA SHA256 is `2de3e62a46fa823dfd392029410e747bb27c2a97f3e4c205bb2d8e51df37a4d3`.

See [build and preservation details](docs/SEED04-BUILD-AND-TEST.md) and [compiled source manifest](source/COMPILED-SOURCE-MANIFEST.json). `source/Shienryu-seed04-compiled-source.zip` contains the 203 source inputs plus the fixed generated build-date file. The complete map/fitted checkpoint, genuine RBF/SOF and all 96 actual STA report files remain in the [verified recovery archive](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/tree/9a6527f159567c6cd3ffa55f971e147f4b6396b9/experiments/control-r2-seed-archive/seed04). Exact checkpoint/binary restoration has been verified; an identical fresh recompilation has not.

The [original v1.1 release](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/releases/tag/v1.1-share-20261022) and its source/tag remain preserved. This seed 4 publication supersedes its install payload; it does not erase that historical release. See [credits and licenses](NOTICE.md).
