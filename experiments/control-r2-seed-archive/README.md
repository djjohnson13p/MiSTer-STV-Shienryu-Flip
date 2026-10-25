# Preserved Shienryu control R2 seeds 1 and 2

These are separate experimental Quartus 25.1 Lite results from source `7e987bb9ef0361356be22be13551e4626902f3a7`, fixed build date `261025`. Neither passes complete timing or has final hardware acceptance. The original published/installed experimental core is unchanged.

Every seed retains its exact RBF/SOF, complete fitted/map/incremental databases, compiled source/settings/clocks/constraints, generated date, tool identities and all eight temperature reports. The binaries can be restored exactly without rebuilding. A bit-identical rebuild has not been demonstrated.

| Seed | Actual RBF SHA256 | Programming ZIP |
| --- | --- | --- |
| 1 | `63fcb6892c69dddb4a88664555f6ddad46a10b6ce0fc437b9d43d27bb468592a` | `frozen-package/seed01/control-r2-seed01-DRAFT-source-programming-and-evidence-01.zip` |
| 2 | `69bc89fe8e96f678ebcc1b698af3ab25661720a82bcebbaca6ddfff4c395895c` | `frozen-package/seed02/control-r2-seed02-DRAFT-source-programming-and-evidence-01.zip` |

For just the core binary, extract the selected programming ZIP and use its `seed01/programming/` or `seed02/programming/` RBF. The seed 2 fitter checkpoint still contains inherited seed 1 programming outputs; its separately generated programming RBF above is authoritative.

To restore a complete assembled checkpoint, download all files in this archive directory, including every ZIP part. With Python 3.11 or newer installed, run `python restore_seed.py --seed 1 --out C:/new-empty-path/seed1` (or `--seed 2`). The output directory must not exist. The helper verifies package/member hashes, reconstructs seed 2's explicit assembler overlay, and verifies every restored byte against the original assembled snapshot. It never writes an existing build directory. Further Quartus analysis needs the recorded compatible tools/device support.

`ROOT-PACKAGE-REVIEW.json` records independent package acceptance and exact checkpoint reconstruction checks. `frozen-package/PACKAGE-INDEX.json` and each seed's `MEMBER-HASHES.json` bind every file. Frozen packaging records retain their original pre-upload DRAFT/status fields as provenance. They are not timing-clean release claims.

The full temperature comparison and inherited timing qualifications are in `frozen-package/README.md`. Seed 1 passes hold throughout but fails setup at four slow conditions; seed 2 passes setup throughout but fails hold throughout. Both are retained because later experiments must not erase an earlier result.

| Model | C | Seed 1 setup ns | Seed 1 hold ns | Seed 1 result | Seed 2 setup ns | Seed 2 hold ns | Seed 2 result |
| --- | ---: | ---: | ---: | --- | ---: | ---: | --- |
| Slow | -40 | -0.489 | +0.063 | Fail setup | +0.009 | -0.661 | Fail hold |
| Slow | 0 | -0.406 | +0.069 | Fail setup | +0.092 | -0.692 | Fail hold |
| Slow | 85 | -0.156 | +0.142 | Fail setup | +0.237 | -0.711 | Fail hold |
| Slow | 100 | -0.237 | +0.132 | Fail setup | +0.204 | -0.733 | Fail hold |
| Fast | -40 | +3.554 | +0.003 | Pass | +3.656 | -0.390 | Fail hold |
| Fast | 0 | +3.466 | +0.010 | Pass | +3.571 | -0.392 | Fail hold |
| Fast | 85 | +3.227 | +0.041 | Pass | +3.322 | -0.394 | Fail hold |
| Fast | 100 | +3.103 | +0.053 | Pass | +3.241 | -0.392 | Fail hold |

Additional preserved trial: [Seed 3](seed03/README.md), including its separate complete checkpoint, exact programming files, restore validation and full temperature matrix.
