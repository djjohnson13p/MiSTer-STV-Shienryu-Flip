# Shienryu scaler row-predecessor prototype evidence

This archive preserves a small proposed timing optimization and its completed simulations, based on synchronized flip control source 7e987bb9. It precomputes the previous row counter value to remove a subtract before the scaler address multiplication, keeping the existing pipeline delay. No FPGA timing improvement is claimed yet.

The frozen ZIP contains both completed simulation attempts in full, the exact reference and prototype RTL, fixtures, checkers, logs, captures and root/independent reviews (212 members). Eight progressive comparisons passed, including an independent pixel oracle. Two focused bob/weave comparisons passed, exercising the changed operand with Flip Off and On. The failed earlier reference hard-reset test is preserved too; arbitrary midrun reset behavior remains unverified. Both runtime flavors use the same documented simulation-only shift-wrap shim.

`ROOT-PACKAGE-REVIEW.json` verifies all archived member hashes/CRC and all 210 source files. `frozen-package/PACKAGE-INDEX.json` and `MEMBER-HASHES.json` identify the exact contents. The archive can be extracted with an ordinary ZIP tool into a new directory. Manifests retain historical absolute paths; rerunning elsewhere requires deliberate path setup and the recorded tool versions. No new FPGA compile, hardware acceptance or bit-identical compilation is implied.

This is recovery evidence on a lab branch. The published experimental core and its original branch/tag are unchanged.
