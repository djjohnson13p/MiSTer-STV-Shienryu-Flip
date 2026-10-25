# Preserved Shienryu control R2 seed 8

Seed 8 completed with source commit `7e987bb9ef0361356be22be13551e4626902f3a7`, Quartus 25.1 Lite and build date 261025. It uses the same synthesized source checkpoint as the other control R2 seeds, with only the placement seed changed. It passes hold throughout but fails setup at all four Slow conditions, including 85°C and 100°C. Seed 4 remains the preferred experimental candidate.

All results below are at 1.1 V. Positive slack is margin, negative slack is failure. Recovery, removal and minimum pulse width pass at all eight conditions.

| Model | °C | Setup ns | Hold ns | Result |
| --- | ---: | ---: | ---: | --- |
| Slow | -40 | -0.512 | +0.136 | Fail setup |
| Slow | 0 | -0.471 | +0.142 | Fail setup |
| Slow | 85 | -0.558 | +0.157 | Fail setup |
| Slow | 100 | -0.553 | +0.135 | Fail setup |
| Fast | -40 | +3.429 | +0.042 | Pass |
| Fast | 0 | +3.338 | +0.058 | Pass |
| Fast | 85 | +3.065 | +0.088 | Pass |
| Fast | 100 | +2.958 | +0.092 | Pass |

The exact RBF is 4,356,792 bytes, SHA256 `adf4ddea8584f666c5fdd773c68772370741d2c82b57231c382139485c7c3ced`. Extract it from `frozen-package/control-r2-seed08-DRAFT-source-programming-and-evidence-01.zip` under `seed08/programming/`. The original installed and published experimental core remains unchanged.

The seven ZIP parts preserve the full fitter/map checkpoint, assembler overlay, exact programming files, source/QSF/SDC/PLL/generated date, tool/settings records, all timing reports and per-member hashes. Frozen metadata retains its original DRAFT fields as provenance. This is a failed timing trial preserved for recovery, not a stable release.

To restore the exact assembled checkpoint, download this entire directory and run:

```text
python restore_seed.py --seed 8 --out C:/new-empty-path/seed8
```

Use Python 3.11 or newer. The destination must not exist. The helper verifies package and restored-file hashes, applies the preserved assembler overlay and never invokes Quartus. Root actually restored and verified all 1,051 files; see `ROOT-RESTORE-VALIDATION.json`. This proves exact checkpoint/binary recovery, not that a fresh compilation will reproduce identical bytes. Root and independent package/timing reviews retain their exact scope and qualifications.
