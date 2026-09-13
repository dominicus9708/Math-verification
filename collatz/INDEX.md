# Collatz classified index

The historical `collatz/README.md` and all existing notes/certificates remain untouched.

Use the current classification layer here:

- [`index/README.md`](index/README.md) — current status and classification policy
- [`index/proof-tree.md`](index/proof-tree.md) — dated mainline proof tree
- [`index/side-branches.md`](index/side-branches.md) — side/support/historical branches
- [`index/retired-and-superseded.md`](index/retired-and-superseded.md) — retired, saturated, redundant, insufficient, and superseded routes
- [`index/reproducibility-index.md`](index/reproducibility-index.md) — certificate/source/result map

The formerly unresolved detailed one-paid frontier `7 <= t <= 9` is closed on the audited exact Bellman/address criterion by MATH-104--106.

MATH-107 now fixes the exact next multi-paid workload at `r=13`:

- `1035 = 157 cost-safe + 483 singleton-resolution + 395 critical` phase/address cells;
- `15,364,524` exact branch-and-bound nodes;
- `1,959,535` negative AP cylinders;
- `76,391,629,325` represented ordinary occurrences;
- maximum multiplicity `687,142,557`;
- `276` occupied contiguous multiplicity-support intervals.

This is a workload/representation audit, not an `r=13` closure. The current next proof-facing task is to build a fragmentation-aware exact AP/address propagation schedule, regression-test it on the already closed `r=14` layer, and only then apply it to `r=13`.

Current multi-paid status: `r>=14 CLOSED`, `2<=r<=13 OPEN` in the present audited first-cell calculation.

Collatz and the first universal Farey cell remain `OPEN`. No finite computation in this index is upgraded to a universal proof.
