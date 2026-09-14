# MATH-147 — `r=6` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=6 CLOSURE CLAIM`

## Frozen exact workload

The unchanged MATH-115 exporter freezes the MATH-113 `r=6` workload:

```text
classification                963 = 34 safe + 250 singleton + 679 critical
branch-and-bound nodes        95,577
AP source cylinders           15,133
represented occurrence mass  53,251,059,016,858,758
maximum multiplicity          3,228,918,251,442,427
```

## Exact 128-way mass-balanced representation

Applying unchanged MATH-114 splitting/scheduling semantics gives:

```text
source records                15,133
split pieces                  15,183
only additional pieces        50
128-shard cap                 416,023,898,569,210
minimum shard mass            416,023,898,569,208
maximum shard mass            416,023,898,569,210
maximum pieces per shard      197
```

Every split-piece multiplicity and every shard-local occurrence mass fits `uint64_t`, so the unchanged MATH-108 generalized exact AP-union engine remains representation-safe.

## Resource interpretation

The represented ordinary-integer mass is much larger than in the upper layers, while the compressed AP/state input is much smaller. MATH-108 advances exact AP/state records and recursively bisects source records / AP parameter intervals when needed; it does not enumerate represented ordinary integers one by one.

Therefore raw occurrence mass is not a runtime multiplier and is not a closure claim. Intermediate AP/state expansion and closure depth remain empirical until execution.

Using the MATH-144 single-AP state-record bound, a split AP with multiplicity at most the MATH-114 cap satisfies

```text
ceil(416023898569210 / 2^29) = 774905 < 1000000 = STATE_CAP.
```

Thus at most 29 exact parameter-half bisections after an AP is isolated are sufficient to remove a pure `STATE_CAP` obstruction. This does not address the separate `MAX_DEPTH = 1000` theorem-facing gate.

## Exactness argument

MATH-114 uses consecutive parameter-interval splitting:

`AP(a,b,m) = disjoint union_j AP(a+b*offset_j,b,m_j)`.

It changes only resource scheduling. Ordinary-integer membership, AP step, and exact source semantics are unchanged.

## Claim boundary

This audit proves only that `r=6` has an exact source and an exact 128-shard representation compatible with the audited MATH-108 engine.

It does **not** prove:

- `r=6 CLOSED`,
- that every shard closes within `MAX_DEPTH = 1000`,
- paid-layer coverage,
- first-cell emptiness,
- the Collatz conjecture.

## Execution policy

Keep the workflow manual-only. Do not launch it while MATH-117 `r=10` is occupying the Actions queue. Execute remaining layers in frontier order unless a separately audited scheduling reason justifies otherwise.
