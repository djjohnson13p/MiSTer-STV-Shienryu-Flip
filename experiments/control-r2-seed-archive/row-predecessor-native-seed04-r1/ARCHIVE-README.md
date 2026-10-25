# Shienryu scaler row-predecessor trial, seed 4

This is a preserved experimental result, not a release. It has worse overall timing than control-R2 seed 4 and was not installed on MiSTer. The original release and earlier seeds remain unchanged.

Source: `6eb9367e2d64c18b0b109d221a0bc07d35d493b4`, branch `lab/shienryu-row-predecessor-r1`; Quartus 25.1 Lite; seed 4; fixed build date `261025`. Fresh synthesis, fitting, assembly and separate eight-condition timing analysis completed with native exit 0. Intended clocks and constraints are unchanged.

All seven ZIPs and indexed sidecars preserve the exact 1,051-file source/map/fit/ASM checkpoint, genuine RBF/SOF and all 117 timing reports. The 19 redundant, derived STA cache deltas remain local and are explicitly excluded from this remote recovery package. The full STA inventory is retained as hashes. The package does not claim all 2,245 local stage files are restorable.

Exact restoration of the 1,051-file checkpoint was actually performed and independently rehashed, including both programming files. This proves recovery of the emitted checkpoint and binaries; bit-identical recompilation and relocated-database native usability have not been demonstrated.

To recover, keep this directory intact, use Python 3.11 or newer, and invoke `preserve.py --restore . --index-sha256 25f98d09074811e5aaa5834f08235c7498a690cb55eed9b4a98e30aa4b31350b --target ../row-predecessor-native-restore-recovered`. The target must be a new direct sibling of this directory. The helper only verifies and extracts; it does not execute Quartus or project code.

The package index and manifests describe their historical pre-upload state. Upload success is established only by a separate remote verification receipt in the local project; no archive metadata is rewritten to manufacture that proof.

All conditions are at 1.1 V; slack is in ns. Recovery, removal and minimum pulse width pass all eight conditions.

| Model | Temperature C | Setup | Hold | Result |
|---|---:|---:|---:|---|
| slow | -40 | -0.430 | +0.104 | FAIL |
| slow | 0 | -0.380 | +0.114 | FAIL |
| slow | 85 | -0.477 | +0.139 | FAIL |
| slow | 100 | -0.450 | +0.142 | FAIL |
| fast | -40 | +3.535 | +0.052 | PASS |
| fast | 0 | +3.458 | +0.064 | PASS |
| fast | 85 | +3.230 | +0.085 | PASS |
| fast | 100 | +3.141 | +0.094 | PASS |
