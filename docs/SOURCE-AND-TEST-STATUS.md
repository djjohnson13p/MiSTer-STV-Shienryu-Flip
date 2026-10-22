# Source and test status

## Provenance

This package preserves djjohnson13p’s earlier [ST-V Shienryu 180 Flip contribution, PR #516](https://github.com/MiSTer-devel/Saturn_MiSTer/pull/516), submitted on June 29, 2026. That PR was closed without merging into the upstream core.

The retained source commit is:

```text
5f5271526e73f7dfc7111490c4564a3386b3d124
```

The [full source branch](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/tree/stv-flip-v1.1) starts from that exact project. The original build used **Quartus 25.1 Standard**, project **STV_DS**. No recompilation was performed for this sharing package.

The original `releases/stv_flip_v1.1_final.rbf` and the restored `stv_flip_v1.1_rc1.rbf` have identical contents. The [original release notes](ORIGINAL-RELEASE-NOTES.md) explicitly record that promotion without a binary change. Matching publisher bytes and source provenance are established; a reproducible-build attestation is not claimed.

## Exact install files

| File | Bytes | SHA-256 |
|---|---:|---|
| `stv_flip_v1.1_rc1.rbf` | 4,642,408 | `bf1a726b0e7ac5e41a8262ea1db54bcc613c56355dcb0e4bcce5826820044b31` |
| `Shienryu stv_flip_v1.1_rc1.mra` | 1,373 | `0e9c0a8422fe419a458c8ad8673555acc4500fca7aa19e93985096353efd813e` |

The MRA selects the separate core alias and preserves the Shienryu ROM/BIOS definitions. It contains descriptors, not game or BIOS payloads.

## Behavior and testing limits

The source adds **Audio & Video → Shienryu 180 Flip**, Off/On, using status bit 82. It routes that option into the late HDMI/scaler framebuffer addressing. It flips the active game picture by 180 degrees, leaves OSD orientation separate, and is built for dual SDRAM. Direct analog/raw output is outside this feature’s scope.

Original manual testing reported Shienryu boot, flip Off/On on HDMI, controls, coin/start, audio and gameplay. Physical monitor photos confirmed the flip; core screenshots alone do not establish OSD orientation. These historical results are not a new compatibility test of every MiSTer board or every ST-V game.

The original build reported **setup −0.089 ns** and **hold −0.330 ns**. Those negative margins mean formal timing closure was not achieved. The unchanged binary remains experimental; repackaging it does not turn the recorded manual test into timing qualification.
