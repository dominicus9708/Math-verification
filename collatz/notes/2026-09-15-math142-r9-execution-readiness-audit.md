# MATH-142 — `r=9` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=9 CLOSURE CLAIM`

## Frozen exact workload

The unchanged MATH-115 exporter freezes the MATH-113 `r=9` workload:

```text
classification                977 = 72 safe + 349 singleton + 556 critical
branch-and-bound nodes        915,218
AP source cylinders           141,002
represented occurrence mass  172,107,496,438,700
maximum multiplicity          3,381,256,733,001
```

## Exact 128-way mass-balanced representation

Applying the unchanged MATH-114 splitting/scheduling semantics gives:

```text
source records                141,002
split pieces                  141,021
only additional pieces        19
128-shard cap                 1,344,589,815,928
minimum shard mass            1,344,589,815,927
maximum shard mass            1,344,589,815,928
maximum pieces per shard      1,300
```

Every shard-local mass and every split-piece multiplicity fits `uint64_t`, so the unchanged MATH-108 generalized exact AP-union engine remains representation-safe.

## Resource interpretation

Relative to the currently running `r=10` gate:

- source-record count is about `0.506 × r10`;
- split-piece count is about `0.506 × r10`;
- maximum pieces per shard is about `0.531 × r10`;
- represented occurrence mass and balanced shard mass are about `6.245 × r10`.

The MATH-108 engine advances AP/state records rather than enumerating every represented ordinary integer. Therefore the `6.245×` occurrence-mass increase is **not** a runtime multiplier or a closure theorem. The smaller AP/piece counts are favorable, but intermediate state expansion and closure depth remain empirical until execution.

## Exactness argument

MATH-114 uses the identity

`AP(a,b,m) = disjoint union_j AP(a+b*offset_j,b,m_j)`

with consecutive parameter intervals. It changes only resource scheduling. Ordinary-integer membership, AP step, and exact source semantics are unchanged.

## Claim boundary

This audit proves only that `r=9` has an exact source and an exact `u64`-safe 128-shard representation compatible with the already-audited MATH-108 engine.

It does **not** prove:

- `r=9 CLOSED`,
- that every shard will close within the present resource cap,
- paid-layer coverage,
- first-cell emptiness,
- the Collatz conjecture.

## Execution policy

Do not launch the `r=9` closure gate while MATH-117 `r=10` is consuming the Actions queue. Prepare the manual-only workflow, then execute only after the `r=10` gate reaches a stable result.
