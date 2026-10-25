# Preserved Shienryu control R2 seed 10

The final fixed-source seed completed with commit7e987bb9, Quartus25.1 Lite and date261025. It fails setup at all four Slow conditions and hold at Fast−40/0. Seed4 remains preferred. All results are at1.1V, slack in nanoseconds; recovery/removal/minimum pulse width pass throughout.

| Model | °C | Setup ns | Hold ns | Result |
| --- | ---: | ---: | ---: | --- |
| Slow | -40 | -0.374 | +0.140 | Fail setup |
| Slow | 0 | -0.335 | +0.140 | Fail setup |
| Slow | 85 | -0.432 | +0.150 | Fail setup |
| Slow | 100 | -0.403 | +0.149 | Fail setup |
| Fast | -40 | +3.599 | -0.017 | Fail hold |
| Fast | 0 | +3.535 | -0.011 | Fail hold |
| Fast | 85 | +3.288 | +0.012 | Pass |
| Fast | 100 | +3.202 | +0.020 | Pass |

Exact RBF: 4,350,644 bytes, SHA256 `640e40fb2a675e77581d564a9cfac721a8a0313129f35e6bee7812846dbd5cca`. Extract `seed10/programming/STV_DS.rbf` from `frozen-package/control-r2-seed10-DRAFT-source-programming-and-evidence-01.zip`.

Download this entire directory and run with Python3.11 or newer:

```text
python restore_seed.py --seed 10 --out C:/new-empty-path/seed10
```

The destination must not exist. The helper verifies/restores the full1,051-file assembled checkpoint without invoking Quartus. Root actually ran it; see `ROOT-RESTORE-VALIDATION.json`. Seven ZIPs retain the full fitter/map checkpoint, assembler overlay, exact source/settings/date/tools and all99 STA reports with member hashes. Identical recompilation is unproven; exact binary/checkpoint recovery is verified.

The batch terminal and exact scheduled-task cleanup receipts are retained here. It exhausted seeds3–10 without a clean candidate; seeds1–2 were separate earlier trials. Native jobs completed normally and their owned handles closed. The original release and all earlier seeds remain preserved. This archive is recovery evidence, not a stable release.
