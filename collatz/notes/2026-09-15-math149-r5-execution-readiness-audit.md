# MATH-149 — `r=5` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY / EXECUTION NOT LAUNCHED / NO r=5 CLOSURE CLAIM`

## Frozen exact workload

```text
classification                952 = 20 safe + 226 singleton + 706 critical
branch-and-bound nodes        46,721
AP source cylinders           6,525
represented occurrence mass  407,471,475,426,308,081
maximum multiplicity          51,662,692,023,078,828
```

These values are frozen by the unchanged MATH-115 exporter from the MATH-113 workload audit.

## Exact 128-way mass-balanced representation

Unchanged MATH-114 splitting gives:

```text
source records                6,525
split pieces                  6,598
only additional pieces        73
128-shard cap                 3,183,370,901,768,032
minimum shard mass            3,183,370,901,768,031
maximum shard mass            3,183,370,901,768,032
maximum pieces per shard      122
```

Every split-piece multiplicity and every shard-local mass fits `uint64_t`; the unchanged MATH-108 exact AP-union engine is therefore representation-compatible.

## Resource bound

By MATH-148,

```text
ceil(3183370901768032 / 2^32) = 741187 < 1000000 = STATE_CAP.
```

Thus after an AP is isolated, at most 32 exact parameter-half bisections suffice to remove a pure `STATE_CAP` obstruction.

This says nothing about whether the exact AP dynamics empty before `MAX_DEPTH = 1000`.

## Claim boundary

This audit proves exact source/partition readiness only. It does not prove `r=5 CLOSED`, paid-layer coverage, first-cell emptiness, or the Collatz conjecture.

## Execution policy

Keep the workflow manual-only and unlaunched while MATH-117 `r=10` is running.
