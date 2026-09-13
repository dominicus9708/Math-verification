# MATH-111 final — r=12 exact 128-shard closure

Status: `MAINLINE EXACT FINITE CLOSURE / r=12 CLOSED`

Date finalized: 2026-09-14

## Source workload

MATH-110 froze the unchanged MATH-065 exact `r=12` source:

```text
classification:             1013 total
safe:                        126
singleton:                   457
critical:                    430
branch-and-bound nodes:  8,278,602
AP cylinders:          1,053,555
represented occurrence mass: 580,472,268,528
max multiplicity:        12,976,298,271
```

## Exact partition certificate

MATH-111 independently partitioned source records by index modulo 128.

The partition certificate proved exact disjoint/exhaustive source-record coverage with global totals:

```text
AP cylinders:          1,053,555
occurrence mass:     580,472,268,528
shards:                         128
```

No source record is omitted or duplicated by the partition rule.

## Closure execution

Workflow:

```text
.github/workflows/collatz-math111-r12-sharded-closure.yml
```

Run:

```text
34764316089
```

Each shard:

1. checked out the frozen source/engine revision;
2. compiled the unchanged generalized exact MATH-108 AP-union engine;
3. regenerated the exact MATH-110 `r=12` source stream;
4. selected its exact source-record shard;
5. ran exact AP-union propagation to the frozen floor `2^71`;
6. required `PASS generalized exact AP-union audit`;
7. preserved its audit log.

Final audit on 2026-09-14 checked both GitHub job pages covering all 128 jobs. Across the complete job set:

```text
total jobs: 128
queued:       0
failure:      0
all jobs:     completed / success
```

The later page includes shards 100 onward completed successfully; the first 100-job page likewise contains no queued or failed job.

Therefore every exact source shard closes under the audited MATH-108 AP dynamics.

## Conclusion

By the exact source partition certificate plus successful closure of every shard:

```text
r=12 CLOSED
```

within the current audited multi-paid first-cell framework.

The certified multi-paid frontier becomes:

```text
r >= 12 CLOSED
2 <= r <= 11 OPEN
```

## Claim boundary

This is an exact finite paid-layer closure. It does **not** by itself prove:

- paid-layer coverage completeness;
- first universal Farey-cell emptiness;
- the universal reduction from the frozen baseline;
- the Collatz conjecture.

Those remain separate obligations.
