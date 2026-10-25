# Preserved Shienryu control R2 seed 3

Exact source `7e987bb9ef0361356be22be13551e4626902f3a7`, Quartus 25.1 Lite, fixed date261025. Experimental: no completed timing/hardware acceptance or replacement of the original core.

Actual programming RBF:4,390,248 bytes, SHA256 `26424d1d5011076796be6cd10c356af8405654875e607dce847a68a03e0d7a83`. It is in `frozen-package/control-r2-seed03-DRAFT-source-programming-and-evidence-01.zip`, under `seed03/programming/`. The fitter-only checkpoint contains inherited earlier programming files; this separately generated RBF is authoritative.

For a complete assembled checkpoint, download this directory including all seven ZIP parts. With Python3.11 or newer: `python restore_seed.py --seed 3 --out C:/new-empty-path/seed3`. The output must not exist. The helper verifies package/member hashes and reconstructs/validates every original assembled checkpoint byte. Compatible recorded Quartus tools/device support remain needed for analysis. Bit-identical recompilation has not been demonstrated.

`ROOT-PACKAGE-REVIEW.json` records independent full checkpoint/overlay and all100report checks. Frozen packaging records retain original pre-upload DRAFT/status fields. Only seed3's Jobs are closed; the parent batch may continue later seeds. Exact earlier seeds remain preserved.

Full timing conditions at1.1V follow; recovery/removal/pulse-width pass throughout.

| Model | C | Setup ns | Hold ns | Recovery ns | Removal ns | MPW ns | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Slow | -40 | -0.441 | +0.145 | +3.697 | +0.960 | +1.091 | Fail setup |
| Slow | 0 | -0.388 | +0.150 | +3.737 | +0.953 | +1.091 | Fail setup |
| Slow | 85 | -0.358 | +0.181 | +3.432 | +1.029 | +1.091 | Fail setup |
| Slow | 100 | -0.328 | +0.172 | +3.342 | +1.039 | +1.091 | Fail setup |
| Fast | -40 | +3.347 | +0.054 | +5.228 | +0.406 | +1.091 | Pass |
| Fast | 0 | +3.255 | +0.066 | +5.173 | +0.416 | +1.091 | Pass |
| Fast | 85 | +2.983 | +0.091 | +4.985 | +0.490 | +1.091 | Pass |
| Fast | 100 | +2.896 | +0.102 | +4.923 | +0.501 | +1.091 | Pass |
