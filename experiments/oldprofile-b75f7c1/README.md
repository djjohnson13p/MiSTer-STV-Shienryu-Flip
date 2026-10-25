# EXPERIMENTAL — root-reviewed Shienryu b75 milestone

Source `b75f7c175dad7fcc9c685ba776f6aa673e2a4d6e`, Quartus 25.1, seed 1, placement effort 2, build date 261025. This is evidence for a later user-fork lab branch, not a release, PR or verified fix. No commit, push or installation was performed.

Root's final all-corner review is included as `allcorner/ROOT-TIMING-RESULT.json`, SHA-256 `e95d09c9c103d717d735c9b04713b3ea586d911fd524ce87f743b251ecafd931`. The complete agent report review is also included, SHA-256 `48c57b4964b34241a173890357c7cbb0c69a42b283eaab649fc70282f1ecbf98`.

**Setup still fails:** the four slow-condition global slacks are -0.058, -0.300, -0.023 and -0.240 ns. Hold is positive at all eight conditions, worst +0.040 ns; reviewed recovery/removal/minimum-pulse-width results are positive. Native STA completed in 341.343 seconds with processes/handles closed and the task removed. Root independently verified all 1,051 original fit files and 210 immutable analysis inputs. This is timing improvement, not clean closure.

**The incoming flip-control CDC/frame-coherence gap remains unfixed in b75. This RBF has no hardware test.** The original published and installed release remains unchanged. Subsequent synchronization/frame variants are outside this bundle.

Exact RBF: 4,366,552 bytes, SHA-256 `0ef3dc29f3eae6d5b8780563e10b42c015dd73aaba2ebe7a1ba20b8c9a012bc7`. Exact canonical source ZIP: SHA-256 `5d5ef592683a17429f566ef44e5a452e49d5f3ba45e7edf8c89a8988a1d47f8a`. Raw fullflow source-integrity/adapter false and scheduler exit 1 remain preserved with the precise metadata-only audit.

All original evidence/report bytes are retained. Only this README and review-status manifest changed; both final review JSONs were added. No game ROM/BIOS payload, additional ROM/BIOS archive, live MiSTer configuration, credential or database payload is added. The requested canonical source ZIP retains its committed source/IP initialization files unchanged.

`PRESERVATION-MANIFEST.json` inside the ZIP records final review bindings. External `MEMBER-HASHES.json` verifies every ZIP member and the ZIP hash. The earlier draft ZIP remains byte-for-byte unchanged; `MEMBER-HASHES-draft.json` retains its earlier member manifest.
