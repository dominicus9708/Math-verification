# Collatz classified index

The historical `collatz/README.md` and all existing notes/certificates remain untouched.

Use the current classification layer here:

- [`index/README.md`](index/README.md) — current status and classification policy
- [`index/proof-tree.md`](index/proof-tree.md) — dated mainline proof tree
- [`index/side-branches.md`](index/side-branches.md) — side/support/historical branches
- [`index/retired-and-superseded.md`](index/retired-and-superseded.md) — retired, saturated, redundant, insufficient, and superseded routes
- [`index/reproducibility-index.md`](index/reproducibility-index.md) — certificate/source/result map

## Current exact frontier

The detailed one-paid band `7 <= t <= 16` is closed on the audited exact Bellman/address criterion by MATH-097--106.

MATH-107 fixed the exact `r=13` multi-paid workload, MATH-108 extracted the region-independent exact source/parameter sharding lemma, and MATH-109 closed `r=13` by a certified disjoint/exhaustive 16-shard AP-union calculation.

Current multi-paid status:

```text
r >= 13  CLOSED
r = 12   OPEN — exact workload fixed, 128-shard partition certified,
                 exact sharded closure gate running
2 <= r <= 11 OPEN
```

MATH-110 fixes the exact `r=12` workload:

- `1013 = 126 cost-safe + 457 singleton-resolution + 430 critical` cells;
- `8,278,602` branch-and-bound nodes;
- `1,053,555` negative AP cylinders;
- `580,472,268,528` represented ordinary occurrences;
- maximum multiplicity `12,976,298,271`;
- `305` occupied contiguous multiplicity-support intervals.

MATH-111's independent partition certificate proves that record-index residue classes modulo 128 partition all `1,053,555` source cylinders without omission or duplication and preserve the full occurrence mass `580,472,268,528`. The 128 exact AP-union closure jobs are the current executable gate. No `r=12 CLOSED` claim is permitted until every shard passes.

Collatz and the first universal Farey cell remain `OPEN`. No finite computation in this index is upgraded to a universal proof.
