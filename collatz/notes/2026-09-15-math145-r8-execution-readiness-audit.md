# MATH-145 — `r=8` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=8 CLOSURE CLAIM`

## Frozen exact workload

The unchanged MATH-115 exporter freezes the MATH-113 `r=8` workload:

```text
classification                977 = 60 safe + 330 singleton + 587 critical
branch-and-bound nodes        436,659
AP source cylinders           65,811
represented occurrence mass  1,281,026,785,265,013
maximum multiplicity          67,269,130,238,384
```

## Exact 128-way mass-balanced representation

Applying the unchanged MATH-114 splitting/scheduling semantics gives:

```text
source records                65,811
split pieces                  65,844
only additional pieces        33
128-shard cap                 10,008,021,759,883
minimum shard mass            10,008,021,759,882
maximum shard mass            10,008,021,759,883
maximum pieces per shard      696
```

Every shard-local mass and every split-piece multiplicity fits `uint64_t`, so the unchanged MATH-108 generalized exact AP-union engine remains representation-safe.

## Resource interpretation

Relative to `r=9`:

- source-record count is about `0.467 × r9`;
- split-piece count is about `0.467 × r9`;
- maximum pieces per shard is about `0.535 × r9`;
- represented occurrence mass and balanced shard mass are about `7.443 × r9`.

The MATH-108 engine advances exact AP/state records rather than enumerating every represented ordinary integer. Hence the larger occurrence mass is not itself a runtime multiplier or a closure obstruction. The AP/piece geometry is smaller than at `r=9`; intermediate state expansion and closure depth remain empirical until execution.

For a single AP at the shard-mass cap, repeated exact parameter bisection would reduce its source mass below `STATE_CAP=1,000,000` after at most 24 halvings, since `ceil(10,008,021,759,883 / 2^24) < 1,000,000`. This is only a resource bound, not a closure theorem.

## Exactness argument

MATH-114 uses consecutive exact AP parameter splits:

`AP(a,b,m) = disjoint union_j AP(a+b*offset_j,b,m_j)`.

This changes only execution scheduling. Ordinary-integer membership, AP step, and exact source semantics are preserved.

## Claim boundary

This audit proves only that `r=8` has an exact source and an exact `u64`-safe 128-shard representation compatible with the already-audited MATH-108 engine.

It does **not** prove:

- `r=8 CLOSED`,
- that every shard will close within the current depth/resource gates,
- paid-layer coverage,
- first-cell emptiness,
- the Collatz conjecture.

## Execution policy

Do not launch this workflow while MATH-117 `r=10` is running or before the prepared MATH-142 `r=9` gate has reached an appropriate launch point. Keep it `workflow_dispatch` only.
