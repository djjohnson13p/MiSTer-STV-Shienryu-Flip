# Credits and license notices

- **srg320** and Saturn/ST-V contributors: the underlying FPGA core.
- **MiSTer-devel**, **Alexey Melnikov / Sorgelig** and MiSTer framework contributors: platform and hardware abstraction.
- **Ludvig Strigeus** and **Sorgelig**: retained HQ2x implementation, as credited in `sys/hq2x.sv`.
- **Till Harbaum** and **Alexey Melnikov**: retained scandoubler implementation, as credited in `sys/scandoubler.v`.
- **TEMLIB**: Avalon scaler in `sys/ascal.vhd`.
- **Dale / djjohnson13p**: earlier Shienryu 180 Flip contribution, project direction and physical testing; earlier work is recorded in [original PR #516](https://github.com/MiSTer-devel/Saturn_MiSTer/pull/516).

The Shienryu HQ2x integration, scaler changes, validation and packaging used Codex assistance. Human picture/sound observations are distinguished from automated and screenshot evidence. This is a derivative experimental release; no upstream endorsement or author review is claimed.

Retain every per-file copyright and license notice and the accompanying license texts. `Saturn.sv` and `sys/sys_top.v` declare **GNU GPL version 2 or later**; `sys/scandoubler.v` declares **GNU GPL version 3 or later**. `sys/hq2x.sv` retains its GPL notice and copyright credits. The publication source provides the full texts at `LICENSES/GPL-2.0.txt` and `LICENSES/GPL-3.0.txt`. Added license/provenance files are separate from the unchanged exact205 compiled-input archive. These notices do not replace or relicense individual files.

`sys/ascal.vhd` retains TEMLIB's permission to distribute and use it for any purpose and its request to report bugs or suggestions to TEMLIB. Preserve that notice with the scaler source. This publication does not itself contact contributors or create an upstream pull request.

The installation package includes no game ROM, system BIOS, invincibility ROM, personal settings, controller maps, save data or credentials. Compatible game and BIOS sets are supplied separately. Source/development archives retain disclosed source-tracked initialization tables and original notices. Existing dual-RAM flip and single-RAM releases remain separate.
