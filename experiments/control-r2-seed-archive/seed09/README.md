# Preserved Shienryu control R2 seed 9

Seed 9 completed with source commit `7e987bb9ef0361356be22be13551e4626902f3a7`, Quartus 25.1 Lite and build date 261025. It uses the same synthesis/map checkpoint as the other control R2 seeds, with the placement seed changed. Hold fails at all eight conditions and setup fails at all four Slow conditions. Seed 4 remains the preferred experimental candidate.

All results below are at 1.1 V. Positive slack is margin and negative slack is failure. Recovery, removal and minimum pulse width pass at every condition.

| Model | °C | Setup ns | Hold ns | Result |
| --- | ---: | ---: | ---: | --- |
| Slow | -40 | -0.305 | -0.530 | Fail setup and hold |
| Slow | 0 | -0.261 | -0.550 | Fail setup and hold |
| Slow | 85 | -0.341 | -0.568 | Fail setup and hold |
| Slow | 100 | -0.317 | -0.586 | Fail setup and hold |
| Fast | -40 | +3.491 | -0.308 | Fail hold |
| Fast | 0 | +3.394 | -0.310 | Fail hold |
| Fast | 85 | +2.998 | -0.307 | Fail hold |
| Fast | 100 | +3.035 | -0.307 | Fail hold |

Exact RBF: 4,368,808 bytes, SHA256 `2d5c96d5c306b38ea2ab599c38c984ef9309ec5878e10d96f0e7557b44543347`. Extract `seed09/programming/STV_DS.rbf` from `frozen-package/control-r2-seed09-DRAFT-source-programming-and-evidence-01.zip`. The seven parts preserve the full fitted/map checkpoint, assembler overlay, exact source/settings/generated date/tool provenance, all 116 STA reports and member hashes. Frozen DRAFT metadata records packaging history, not a release claim.

Download this entire directory and use Python 3.11 or newer to run:

```text
python restore_seed.py --seed 9 --out C:/new-empty-path/seed9
```

The destination must not exist. The helper verifies and restores all 1,051 exact checkpoint files without invoking Quartus. Root actually ran it; `ROOT-RESTORE-VALIDATION.json` records that proof. Exact recovery is demonstrated; identical recompilation is not.

The two supporting clock-comparison JSON files preserve a separate read-only study of completed seeds 1–8. They support a future isolated scaler experiment and are not seed9 or new-variant timing results. Their full condition arrays and zero-margin qualification are retained. The original published/installed experimental core stays preserved.
