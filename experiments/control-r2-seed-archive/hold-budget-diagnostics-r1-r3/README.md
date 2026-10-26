# Shienryu: measured hold-repair feasibility

The saved source6eb/seed5 layout has enough measured setup headroom to justify one targeted hold-repair experiment. No new synthesis, fit, assembly, seed, source, clock, constraint or bitstream was created by this diagnostic. Baseline7e9/seed4 remains the preferred installed core, with the user’s physical audio/video/flip confirmation.

The five failing paths need at most0.723ns additional minimum delay. Across all valid launches into the four affected destination registers, the smallest setup margin is2.793ns. The failing source-to-destination pairs themselves have at least6.367ns setup margin. All72 hold-query rows fit within the corresponding scalar destination setup headroom. These are useful feasibility bounds, not guaranteed inserted-route budgets: minimum/maximum delay models, clock skew, shared fanout and placement can change together.

## Every analyzed condition

All1.1V; slack in ns. These global timing results exactly match the existing seed5 fit, not a new improved core. Recovery, removal and minimum pulse width pass all8; every condition still fails hold.

| Model | C | Global setup | Setup | Global hold | Hold | Least setup margin into affected destinations | Largest required hold delay |
|---|---:|---:|---|---:|---|---:|---:|
| slow | -40 | -0.017 | FAIL | -0.647 | FAIL | 3.083 | 0.647 |
| slow | 0 | +0.048 | Pass | -0.673 | FAIL | 3.090 | 0.673 |
| slow | 85 | +0.158 | Pass | -0.704 | FAIL | 2.870 | 0.704 |
| slow | 100 | +0.108 | Pass | -0.723 | FAIL | 2.793 | 0.723 |
| fast | -40 | +3.636 | Pass | -0.377 | FAIL | 5.714 | 0.377 |
| fast | 0 | +3.550 | Pass | -0.380 | FAIL | 5.596 | 0.380 |
| fast | 85 | +3.231 | Pass | -0.380 | FAIL | 5.237 | 0.380 |
| fast | 100 | +3.132 | Pass | -0.379 | FAIL | 5.121 | 0.379 |

## Affected destinations across all8

| Destination | Smallest setup margin, all launches | Largest hold delay needed |
|---|---:|---:|
| emu:emu|sdram1:sdram1|raddr23[1][15] | 2.891ns | 0.723ns |
| emu:emu|sdram1:sdram1|raddr23[1][14] | 3.694ns | 0.586ns |
| emu:emu|ddram:ddram|cart_rcache_addr[24] | 2.793ns | 0.534ns |
| emu:emu|sdram1:sdram1|raddr23[1][8] | 2.895ns | 0.359ns |

## Proposed next decision

Recommend one controlled hold-repair trial using the same source and seed5, enabling TDC_AGGRESSIVE_HOLD_CLOSURE_EFFORT ON. Ordinary AllPaths hold repair, multi-corner optimization and MAXIMUM routing effort are already enabled. The installed25.1 Standard/Lite metadata recognizes this additional option; actual CycloneV fitter use/effect has not been demonstrated. Verify native acceptance/use before attributing any improvement to it. If ignored/unsupported or hold does not improve without unacceptable setup regressions, stop this approach and keep accepted baseline4. Do not resume a seed sweep.

Full eight-condition closure also requires resolving the separate -0.017ns Slow-40C ascal vertical-counter feedback setup path. That is not one of these five hold paths and this analysis does not prove it repaired. The user excludes freezing conditions from intended operation; disclose the residual and judge any improved candidate honestly as experimental.

No later fitter/RTL/seed action is authorized by selecting this diagnostic. Present this concrete proposal for the joint next-step decision first. Preserve the original and baseline4 unchanged. No Shienryu PR, release or author contact is authorized.

## Evidence and qualifications

R3 completed native0 in391.062s; all144 target reports have unique literal endpoint matches, finite paths and native arrival/required/slack arithmetic checks. Root rehashed all1335 actual stage members (598323147B), verified the immutable1051-file parent and unchanged global all8 numeric values. Exact task removed after Ready/exit0/native handles closed.

R1 andR2 are preserved inconclusive reporting attempts: R1 used a node ID as a collection; R2 tried to change escaping mode after loading a netlist. Neither established a target budget. R3 uses a genuine collection under unchanged default natural bus naming and verifies exact original node ID/name.

Raw144 reports, coverage TSV and complete stage-member hashes accompany the archive. The copied source/map/fit/programming parent is already recoverable from lab archive commit269b33b22ff31de4e54421130bf6dac278e5de7d. Redundant per-analysis working timing caches remain local, explicitly excluded from this small analysis ZIP. No bit-identical fresh recompilation or relocated native DB usability claim is made.
