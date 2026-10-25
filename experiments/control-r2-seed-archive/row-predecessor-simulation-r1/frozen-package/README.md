# Row-predecessor closed simulation evidence (local draft)

This package preserves both completed isolated attempts in full: R1 including its failed reference reset run, and R2 focused bob/CE-gap and weave passes. It also contains the finite-math receipt, path proposal, both root reviews and the independent semantic review.

The exact reference is c958d749... and the isolated 4+/1- variant is 73ca65c6..., based on 7e987bb9.... Current worktree and active native batch files are excluded. Stored manifests/logs retain historical absolute path references; those references do not mean external files are bundled.

The package is evidence, not feature/timing/hardware acceptance. Arbitrary midrun reset remains unverified after an inherited reference underflow at480.385us. Both runtime flavors share the inherited SIM-only zero-offset shift-wrap. Exact FPGA source was analyzed/elaborated, while runtime used that shared shim. Focused tests are golden-reference equivalence; progressive tests additionally have an independent pixel oracle.

PACKAGE-CONTEXT.json records scope, qualifications and input provenance. MEMBER-HASHES.json gives every archive member's exact SHA256/bytes and owning ZIP. PACKAGE-INDEX.json binds ZIP/member-index hashes and verification. ZIP entries use sorted paths, fixed1980 timestamps, fixed regular-file mode and DEFLATE9; a second independent archive construction is byte-compared in memory. Determinism is within the recorded Python/zlib implementation.

Nothing was extracted or built. Original folders are rehashed after packaging and remain unchanged. Root will independently QC and decide whether to publish on the authorized evidence branch. No Git, device, compiler or active native DB action occurs here.
