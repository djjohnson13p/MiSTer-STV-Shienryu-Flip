# Credits and license notices

- **srg320** and the Saturn/ST-V contributors: the underlying FPGA core.
- **MiSTer-devel**, **Alexey Melnikov**, and MiSTer framework contributors: the MiSTer platform and hardware abstraction.
- **TEMLIB**: the Avalon scaler in `sys/ascal.vhd`.
- **Dale / djjohnson13p**: the earlier Shienryu 180 Flip contribution and physical testing, retained from [original PR #516](https://github.com/MiSTer-devel/Saturn_MiSTer/pull/516).

The source retains its existing per-file license and copyright notices. In particular, `Saturn.sv` and `sys/sys_top.v` declare **GNU GPL version 2 or later**. A copy of GPL version 2 is included at [LICENSES/GPL-2.0.txt](LICENSES/GPL-2.0.txt).

`sys/ascal.vhd` retains TEMLIB’s notice permitting distribution and use for any purpose, with its request to report bugs or suggestions to TEMLIB. Preserve that notice when redistributing the scaler source.

Other upstream files retain their own applicable notices and terms. This document adds attribution and does not replace those licenses. The [source branch](https://github.com/djjohnson13p/MiSTer-STV-Shienryu-Flip/tree/stv-flip-v1.1) contains the project sources and build files; [source provenance](docs/SOURCE-AND-TEST-STATUS.md) identifies the exact retained commit.

No game ROMs, BIOS files, personal settings, save files or account credentials are included in the install package.
