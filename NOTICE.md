# Credits and license notices

- **srg320** and Saturn/ST-V contributors: underlying FPGA core.
- **MiSTer-devel**, **Alexey Melnikov** and MiSTer framework contributors: platform and hardware abstraction.
- **TEMLIB**: Avalon scaler in `sys/ascal.vhd`.
- **Dale / djjohnson13p**: earlier Shienryu 180 Flip contribution and physical testing, retained from [original PR #516](https://github.com/MiSTer-devel/Saturn_MiSTer/pull/516), and this single-RAM project/testing direction.

The single-RAM HDMI profile and validation work used Codex assistance. The owner's physical testing is recorded separately from automated test evidence. This is a derivative experimental build; no upstream endorsement or author review is claimed.

Preserve all existing per-file copyright and license notices in the accompanying complete source. In particular, `Saturn.sv` and `sys/sys_top.v` declare GNU GPL version 2 or later; the retained GPL v2 text is in `LICENSES/GPL-2.0.txt`. Other files retain their own applicable terms. This notice adds attribution and does not replace those terms.

`sys/ascal.vhd` retains TEMLIB's permission to distribute and use it for any purpose and its request to report bugs or suggestions to TEMLIB. Retain that notice when redistributing the scaler source. This publication does not contact contributors or create an upstream pull request.

The install package contains no game ROMs, BIOS files, personal settings, save data or account credentials. Compatible game/BIOS data must be supplied separately. The existing dual-RAM release and its source/licenses remain separate and preserved.

Exact source/checkpoint archives retain existing source-tracked CD-controller firmware MIFs and other initialization tables. These are disclosed dependencies inherited from the source, distinct from separately supplied game sets and Saturn/ST-V system BIOS files. See provenance/ARCHIVE-SCOPE.md.
