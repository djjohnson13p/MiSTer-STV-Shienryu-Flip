# Shienryu row-predecessor seed5: preserved timing failure

This is a recovery archive, not a release. Source6eb9367e2d64c18b0b109d221a0bc07d35d493b4; Quartus25.1 Lite; seed5; fixed date261025. This fitter/assembler/eight-condition STA sequence completed native0 with closed processes/handles. Setup improves baseline4, but five hold paths fail at all eight conditions. This build was not deployed. The original and baseline4 remain unchanged.

The sevenZIPs preserve the exact1050-file fitted checkpoint and eleven changed/added assembly-overlay files reconstructing the exact1051-file assembled checkpoint. Both restorations were actually performed and independently rehashed. All118 STA reports are archived. The1066-file STA inventory is a hash record;21 redundant derived STA versions remain local, so this package does not claim all3306 local stage files remotely restorable. Bit-identical recompilation and relocated-database native usability are unproved.

Keep this directory intact. With Python3.11 or newer, run preserve.py --restore . --index-sha256 91a36f49ca50e0bac07c9d35fbf7944a6fbb2ffcce7b1e5ccc7597ca0d56c684 --target ../row-predecessor-seed05-restore-recovered-asm --kind asm. Use --kind fit and a different new target for the fitted checkpoint. Targets must be new direct siblings beginning row-predecessor-seed05-restore-. No project/compiler code runs. Only qualified assembly outputs in programming/ are genuine seed5 binaries; fit-tree programming files can be inherited.

The frozen package metadata describes its pre-upload state. Upload success is established only by a separate remote verification receipt. Supporting metadata proves the installed CLI recognizes an aggressive hold setting, not that the CycloneV fitter uses it or achieves closure. Human audio/video/flip confirmation applies to baseline7e9seed4, not this trial. Further FPGA builds are held for joint next-step discussion.

All1.1V; slack ns. Recovery/removal/minimum pulse width pass all8.

| Model | C | Setup | Hold | Result |
|---|---:|---:|---:|---|
| slow | -40 | -0.017 | -0.647 | FAIL |
| slow | 0 | +0.048 | -0.673 | FAIL |
| slow | 85 | +0.158 | -0.704 | FAIL |
| slow | 100 | +0.108 | -0.723 | FAIL |
| fast | -40 | +3.636 | -0.377 | FAIL |
| fast | 0 | +3.550 | -0.380 | FAIL |
| fast | 85 | +3.231 | -0.380 | FAIL |
| fast | 100 | +3.132 | -0.379 | FAIL |
