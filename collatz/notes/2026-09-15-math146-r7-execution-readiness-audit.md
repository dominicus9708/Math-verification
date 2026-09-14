# MATH-146 — `r=7` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=7 CLOSURE CLAIM`

## Frozen exact workload

The unchanged MATH-115 exporter freezes the MATH-113 `r=7` workload:

```text
classification                963 = 42 safe + 291 singleton + 630 critical
branch-and-bound nodes        201,298
AP source cylinders           29,342
represented occurrence mass  8,499,072,326,407,060
maximum multiplicity          807,229,562,860,607
```

## Exact 128-way mass-balanced representation

Applying the unchanged MATH-114 splitting/scheduling semantics gives:

```text
source records                29,342
split pieces                  29,397
only additional pieces        55
128-shard cap                 66,399,002,550,056
minimum shard mass            66,399,002,550,054
maximum shard mass            66,399,002,550,056
maximum pieces per shard      407
```

Every shard-local mass and every split-piece multiplicity fits `uint64_t`, so the unchanged MATH-108 generalized exact AP-union engine remains representation-safe.

## Resource interpretation

Relative to `r=8`, source-record, split-piece, and maximum-pieces-per-shard counts all decrease substantially, while represented occurrence mass and balanced shard mass increase. Since MATH-108 advances exact AP/state records rather than enumerating every represented ordinary integer, the larger mass is not by itself a runtime multiplier or theorem obstruction.

For a single AP at the shard-mass cap, at most 26 exact half-interval bisections are sufficient to bring the source mass below `STATE_CAP=1,000,000`, since `ceil(66,399,002,550,056 / 2^26) < 1,000,000`. This controls only the state-cap resource obstruction and does not prove closure within `MAX_DEPTH=1000`.

## Exactness argument

MATH-114 uses consecutive exact AP parameter splits:

`AP(a,b,m) = disjoint union_j AP(a+b*offset_j,b,m_j)`.

This changes only execution scheduling. Ordinary-integer membership, AP step, and exact source semantics are preserved.

## Claim boundary

This audit proves only that `r=7` has an exact source and an exact `u64`-safe 128-shard representation compatible with MATH-108.

It does **not** prove `r=7 CLOSED`, closure within current resource/depth gates, paid-layer coverage, first-cell emptiness, or the Collatz conjecture.

## Execution policy

Keep the closure workflow manual-only. Do not launch while MATH-117 `r=10` is running, and do not overtake the prepared `r=9` and `r=8` gates without an explicit scheduling reason.
