# Build and test record

## Selected output and exact inputs

|Item|Value|
|---|---|
|Selected seed|`8`|
|RBF bytes / SHA256|`4462056` / `9f41129eb4beed7efbace2a0e7c288913b3bd194b3914089c899db3344a01124`|
|SOF SHA256|`526f5592ea71e1562be087ae84270c39a0822c301fed5776970a2a51fb9762fc`|
|Saved-fit checkpoint manifest SHA256|`58150657e25bd3ed148570d2855cf3da8fc6bc4b91a18826ea8ffed33a07382d`|
|Compiled source base|`7f88c496fbfbed6678171175f95a9279f737933f`|
|Frozen configuration fingerprint|`1be61edec4ee0b164a9daea38542578a42212e0fd5d436cc2fbf5fc21b606627`|
|Tools / target|Quartus Prime Lite 25.1std.0 Build1129; `STV_DS.qpf`, revision `STV_DS`, device `5CSEBA6U23I7`|
|Effective fitter settings|Standard Fit; Advanced Physical Optimization On|
|Fixed build date|`BUILD_DATE "261025"`|

The build uses 205 sealed source inputs: 204 tracked files from the frozen source plus generated `build_id.v`. Against the frozen seed4 configuration, a trial changes only the single anchored placement-SEED assignment in `STV_DS.qsf`; RTL, clock/SDC inputs, effective fitter settings and fixed date stay unchanged. The publication commit adds packaging and documentation and is distinct from the compiled source base. Exact input manifests and output hashes identify the supplied binary; a fresh compile is not guaranteed to reproduce identical bytes.

MAP/FIT/ASM ran through the reviewed Quartus guard, followed by separate timing analysis of a complete copied saved fit. No automatic wall-clock cutoff was applied. The guard retained memory limits, owned-process cleanup, closed-handle checks and before/after input verification. Closed compile reports confirm **Standard Fit** and **Advanced Physical Optimization On** as the effective settings.

## Selection and timing

The owner ended the campaign after seed9. Select seed9 only if its completed, qualified measurements improve on seed8 under the existing ranking; otherwise use seed8. The primary comparison is `min(worst setup slack, worst hold slack)`. This is a comparison of reported constrained margins, not a waiver for negative slack. The campaign was deliberately stopped before seeds10–12; no all-eleven completion is claimed.

**Supplied seed8 timing result:** `TIMING_FAIL_REPORTED`.

Values are worst reported slack in ns at 1100mV. Temperatures are timing-model junction temperatures.

|Model|°C|Setup|Hold|Recovery|Removal|Minimum pulse width|
|---|---:|---:|---:|---:|---:|---:|
|Slow|-40|-0.095|+0.143|+3.446|+0.601|+1.091|
|Slow|0|-0.049|+0.144|+3.449|+0.590|+1.091|
|Slow|85|-0.118|+0.190|+3.274|+0.696|+1.091|
|Slow|100|-0.100|+0.171|+3.225|+0.723|+1.091|
|Fast|-40|+3.619|+0.042|+4.982|+0.291|+1.091|
|Fast|0|+3.555|+0.045|+4.920|+0.307|+1.091|
|Fast|85|+3.206|+0.084|+4.711|+0.377|+1.091|
|Fast|100|+3.073|+0.094|+4.641|+0.392|+1.091|

The closed seed9 measurements are worse on the global ranking used for selection:

|Seed|Worst setup (ns)|Worst hold (ns)|Balanced setup/hold (ns)|Failed corner/check cells|
|---|---:|---:|---:|---:|
|8|-0.118|+0.042|-0.118|4|
|9|-0.558|+0.019|-0.558|4|

Both have four slow-model global setup failures; neither closes full-range timing. Seed8 has the better minimum of worst setup and hold. Seed9 separately improves the worst HDMI-clock setup query from -0.060ns to -0.030ns, but its overall constrained margin is worse. Negative slack receives no waiver. The supplied seed8 also has positive returned HQ/mode margins; no-path queries are not passes.

Coverage includes eight operating conditions, 13 actual clocks, 32 global setup/hold/recovery/removal cells, 416 per-clock cells, 224 HQ/mode cells and 40 native global summaries including minimum pulse width. The 50-path global reports and conditional one-path reports are capped samples; their counts are **not total violating-path counts or TNS**. Report inventory sizes may vary with the actual negative clock queries.

Inherited constraint limits remain: 2,480 no-clock registers, 57 multiple-clock endpoints and one virtual-clock issue; missing input/output delays and unconstrained interface paths are recorded in the timing evidence. Existing ignored SDC and false paths remain limitations. The overridden/invalid RAM-to-scaler multicycle assignments receive no protection credit. Positive HQ queries do not establish end-to-end CDC safety or full constraint adequacy. There is no general timing-signoff claim.

## Hardware and functional evidence

- **Seed6, HQ2x On / Flip On:** corrected invincibility ROM; two players, both eight-stage loops, terminal `ALL` for both. Final scores were P1 **20,999,440** and P2 **11,918,600**. Sampled gameplay, bosses and endings were coherent, and both players showed upgraded power-icon states. Widely spaced screenshots do not establish exact pickup-contact timing or every-frame flawlessness.
- **Physical observation:** the owner reported “Picture and sound look normal” for that seed6 case. Raw backend screenshots are after core HQ/gamma but before the output flip, HDMI OSD and audio; those screenshots do not independently establish physical orientation or sound.
- **Seed8:** the exact binary booted with HQ2x/flip configured On and the corrected test ROM, then was handed to the owner. The recorded boot is separate from any later manual feedback; no completed seed8 full-game run is established by that boot receipt.
- **Selected seed8/9 binary:** no seed6 full-game result is relabeled as its own. The owner waived the other three hardware-mode checks; a waived check is not a passed check. The public launcher uses standard ROM data, while the extended development run used the separate corrected invincibility ROM.

Two PC-side controller/capture interruptions occurred during the seed6 run; the same game continued without a core reload/reset or another start. Final named-file preservation checks passed. This is a bounded test record, not a whole-device audit.

The scaler proof work covers its documented paired-row domain and reduced test configurations. Early startup before row state is known, a fully independent bob-pixel oracle, complete normal-capture coverage and a full 480-line oracle remain unproved. No support for unrelated ST-V games or exhaustive interlaced/high-resolution behavior is inferred from Shienryu testing.

## Public launcher and archive scope

The release MRA must derive from the standard-ROM launcher, preserving ROM parts, CRCs, byte maps, addresses, button definitions, vertical metadata and 65,664-byte NVRAM declaration. Only its core alias, separate setname/profile and description change for this release. Its `<rbf>` basename must match the installed RBF exactly.

Installation payloads contain the new RBF and standard-ROM MRA. Game/BIOS ZIPs, the private invincibility ROM, personal CFG/controller maps, save/NVRAM data and credentials are excluded. The exact-input source archive contains the 205 prepared inputs, with no inherited installation packages, releases or nested source archives. It retains source-tracked CD-controller initialization MIFs and other inherited tables, disclosed source dependencies distinct from separately supplied game sets and system BIOS files. Additional license/provenance files are packaged separately from the unchanged exact-input set. Preserve original notices and the archive manifest when redistributing the source.
