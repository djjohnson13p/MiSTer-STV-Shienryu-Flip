# Build and test record

## Exact tested output

- Source commit: `069ac39e319503557fb344d600d8b4ffbaa7f587`, parent `7e987bb9ef0361356be22be13551e4626902f3a7`.
- Quartus Prime Lite 25.1; project/revision `STV`; seed 1; fixed `BUILD_DATE "261025"`.
- RBF: 4,469,432 bytes, SHA256 `cda57070c2aefe4a21dcd7295ec448fbb9d5ada7051f020d3179caf8bc337d6b`.
- MRA: 1,432 bytes, SHA256 `363429d08b7b46ab0991c71e8bda3892cefceb4db4a9adf8cc0ec2dbe991e449`.
- SOF: 6,705,008 bytes, SHA256 `0a99e7dfaaf6208028dcb8dbc419fe598a11edcc8d83a8b0f08656a2c5d7bfca`.

The launcher was tested under `_Arcade/_CoreLab/`; the install archive places those **same MRA bytes** under `_Arcade/_SingleRAM_Flip/`. Both select the separate `SHYSHD01` core alias. Existing dual-RAM `SHYF0004` files remain separate.

## Source and build provenance

This derives from the earlier Shienryu-flip source, not a newly rebased upstream stock core. An unchanged single-RAM `STV` baseline at parent 7e987… was compiled, timed and exercised before this profile. Two source files changed, adding 11 lines: `STV.qsf` enables existing `SHIENRYU_ONLY` and `MISTER_DISABLE_YC` definitions; `sys/sys_top.v` conditionally holds `av_dis=1`/`LED_USER=Z`. Existing flip/scaler logic, shared scanlines, HDMI OSD/audio and game controls remain. All clock/SDC inputs are unchanged.

`MISTER_DUAL_SDRAM` is **undefined**. Defining it as0 still activates Verilog `ifdef` branches and is not the intended configuration. Pin/netlist review found no SDRAM2 interface; primary SDRAM and DDR-backed high work RAM remain. The standard `sys_analog` pin profile is retained and some analog-related logic remains, despite the HDMI-focused feature scope.

The actual flow used the archived `map_fit_asm.tcl` through `quartus_sh -t`, followed by a separate saved-fit timing collection. Fit completed in 3131.547 s and STA in 324.531 s, both native/guard exit 0 with owned processes/handles closed. No wall-clock cutoff was applied. The before/after/current input sets match: 239 fit bindings and 2163 STA bindings.

Retain the exact prepared input archive, fixed-date file, native driver/tool manifest, reports and full saved-fit checkpoint when reproducing or continuing this build. The checkpoint inventory covers 1068 files/278,810,761 bytes; its manifest SHA256 is `e639a75c17f667c32d138991afa5011e483c55f7f3cf8f72b09fbe6e87fe9eb2`. The input manifest SHA256 is `87f54f1e02ac3f8de53f5407e88f112fa56dc78f8152e8b93d0419beef994b42`. These preserve the tested bytes and provenance; **no fresh-recompile bit-identity guarantee is made**.

Saved-fit STA preserved all original 1068 fit members and 1062 strict copied files. Six identified working-database paths were audited separately, with 15 new working files. No semantic-equivalence claim is made for copied RDB databases.

## Resources

|Resource|Unchanged single-RAM baseline|This HDMI profile|
|---|---:|---:|
|Nominal ALMs needed|41,119|36,579 /41,910|
|Physically placed ALMs|41,122|39,273 /41,910|
|LABs|4,184|4,141 /4,191|
|Registers|41,802|38,483|
|M10Ks|553|479 /553|
|RAM bits|4,159,424|3,494,604|
|DSPs|65|62 /112|
|PLLs|3|3 /6|
|Pins|145|145 /314|

The physical reduction is **1,849 placed ALMs, 43 LABs and 74 M10Ks**. The 4,540 decrease in nominal ALMs is a different metric. LAB occupancy remains close to the device limit. Existing effective all-path hold optimization and maximum router timing effort were already active in the baseline; this is not a seed sweep.

## Complete measured timing

All values are worst reported slack in **ns**, at **1.1V**. The temperatures are timing-model junction temperatures, not observed room temperatures. No 25°C result or interpolation is claimed.

|Model|Temperature °C|Setup|Hold|Recovery|Removal|Minimum pulse width|
|---|---:|---:|---:|---:|---:|---:|
|Slow|-40|-0.148|+0.138|+3.704|+0.657|+1.091|
|Slow|0|-0.091|+0.144|+3.700|+0.644|+1.091|
|Slow|85|+0.127|+0.247|+3.514|+0.699|+1.091|
|Slow|100|+0.104|+0.232|+3.466|+0.705|+1.091|
|Fast|-40|+3.553|+0.040|+5.061|+0.261|+1.091|
|Fast|0|+3.434|+0.052|+4.988|+0.267|+1.091|
|Fast|85|+3.020|+0.089|+4.754|+0.299|+1.091|
|Fast|100|+2.882|+0.092|+4.681|+0.303|+1.091|

**Full-range timing is not closed.** Slow-model setup fails at −40°C and 0°C. All reported hold, recovery, removal and minimum-pulse-width checks are positive. Remaining reported negative paths are HDMI scaler divider/address paths; the worst is `o_div[0][20] → o_div[1][20]`. Other scaler address paths also occur in the negative top 50; this is not a single-path-only issue.

The sealed timing set contains 61 reports: 59 mandatory and 2 negative-clock reports. Coverage includes 13 clocks across 8 conditions, 32 global rows and 416 per-clock rows. **192 empty query rows are unqualified**, not passing results. Each condition reports 50 minimum-pulse-width results and zero such violations.

Coverage warnings remain: 2,480 no-clock registers, 57 multiple-clock endpoints, 1 virtual-clock issue, 31 missing input-delay and 130 missing output-delay entries. Unconstrained-path reporting lists 0 unconstrained clocks, 21 input ports /325 input paths and 92 output ports /139 output paths. Existing ignored SPI/Hq2x filters and 4 newly unmatched YC filters at unchanged `sys_top.sdc:63` remain recorded. These results do not establish constraint adequacy or full device signoff.

## Hardware and observation scope

The exact RBF was tested on a **first-generation dual-module MiSTer Pi**, using only the netlist's primary SDRAM interface. There was no physical single-module-board test. Installed default Main SHA256 was `ba8746d91ced547845b743b7826d827cfd6c488de0bcf8b27112d8d77f8a7e27`; Main and INI were preserved.

Bounded actual-hardware tests and capture review verified boot, P1 movement/fire/bomb, the independent P2 route and P2 movement/fire/bomb, and restored P1 control/rejoin. Main saved status bit82 **Off → On → Off**; all other 16-byte CFG bits stayed identical and final Off matched initial Off. Protected old profiles, dual-RAM seed4, settings and saves remained exact during those automated phases. Remote PNGs are pre-scaler and do not prove physical HDMI orientation or audio.

The owner subsequently answered this exact question:

> Can you watch and listen at the MiSTer for the new single-RAM test? I’ll drive all controls. Your observation is needed to verify HDMI rotation, menu orientation and sound, which remote screenshots cannot capture.

Owner's exact reply: **“tested and everything works as intended”**. This is recorded as **human-reported independent physical testing** of the named HDMI/menu/sound behavior. Prepared physical reload/demo scripts were **not executed**; no video, audio recording or per-step automated physical demonstration is claimed. Bounded gameplay tests and this report do not establish an exhaustive game-completion or long-duration stress test.

## Using the saved project

Use the exact-input archive to recover all 208 prepared inputs, including generated `build_id.v`; open `STV.qpf`, revision `STV`, for the single-SDRAM profile. The current branch adds publication documentation/install files; compiled RTL, QSF and clock constraints retain the exact compiled-source bytes. `STV_DS` is a different target, not the supplied single-RAM build.

The fit archive contains the original `fitted-project/` tree, SOF/RBF, compiler databases and reports, plus original-lab guarded build recipes. Those recipes contain historical absolute paths and dependencies: review/adapt them before use. They are provenance, not a tested portable launcher. Do not regenerate the fixed build date inadvertently; use the archived map/fit/asm driver as the record of the actual flow. No additional FPGA build was run for publication.
