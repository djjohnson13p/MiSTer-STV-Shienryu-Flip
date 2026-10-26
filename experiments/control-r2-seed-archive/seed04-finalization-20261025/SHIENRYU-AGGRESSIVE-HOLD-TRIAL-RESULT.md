# Shienryu aggressive-hold trial: no improvement

The one authorized trial completed fitting, fresh assembly and all-eight timing analysis. Native input readback was ON, with no explicit setting rejection observed. The generated RBF is byte-for-byte identical to the original source6eb/seed5 RBF, and all eight numeric timing results are unchanged. This demonstrates no improvement for this build; it does not prove whether the backend consulted the option. The SOF hash differs; no explanation of that difference is assumed.

Recommendation: stop this approach, retain the user-verified source7e9/seed4 candidate and preserve the original release. No additional seed, setting, RTL change or hardware deployment is selected. Full industrial-range timing closure remains unachieved.

All values in ns at1.1V. Negative slack fails; every aggressive-hold row fails hold. Recovery/removal/minimum pulse width pass all8.

| Model | C | Aggressive5 setup | Aggressive5 hold | Result | Preferred4 setup | Preferred4 hold |
|---|---:|---:|---:|---|---:|---:|
| slow | -40 | -0.017 | -0.647 | FAIL | -0.101 | +0.174 |
| slow | 0 | +0.048 | -0.673 | FAIL | -0.038 | +0.172 |
| slow | 85 | +0.158 | -0.704 | FAIL | +0.070 | +0.242 |
| slow | 100 | +0.108 | -0.723 | FAIL | +0.014 | +0.235 |
| fast | -40 | +3.636 | -0.377 | FAIL | +3.441 | +0.052 |
| fast | 0 | +3.550 | -0.380 | FAIL | +3.350 | +0.054 |
| fast | 85 | +3.231 | -0.380 | FAIL | +2.972 | +0.089 |
| fast | 100 | +3.132 | -0.379 | FAIL | +2.923 | +0.093 |

The trial retained source6eb, mapped design, date261025, intended clocks/constraints, seed5 and all other settings. Only TDC_AGGRESSIVE_HOLD_CLOSURE_EFFORT ON was appended. The same13clocks/416clock rows/192qualified NAs/159normalized constraints and32mode/16predecessor queries remain covered. Native violated-path counts prevent rounded0.000 from being misreported as a pass.

Every actual source/map/fit/ASM/report member is retained locally and will be preserved in the separate user-lab recovery archive. Exact fit/ASM restoration and remote raw-byte verification are required before claiming that backup complete. No new bitstream was deployed to MiSTer, and no default branch, original release, PR or author contact was changed.
