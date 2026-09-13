# MATH-111 — r=12 exact 128-shard closure

Status: `EXACT FINITE r=12 CLOSURE / MAINLINE / FIRST CELL STILL OPEN`

Date: 2026-09-14

## Frozen source

MATH-110 fixed the exact `r=12` negative-candidate source:

```text
classification                1013 = 126 safe + 457 singleton + 430 critical
branch-and-bound nodes        8,278,602
AP cylinders                  1,053,555
represented occurrence mass  580,472,268,528
max multiplicity              12,976,298,271
```

## Exact partition

The MATH-111 source-record partition is exact, disjoint, and exhaustive over all `1,053,555` AP source records, preserving the full occurrence mass `580,472,268,528`.

Partitioning changes only scheduling. It does not remove or add any ordinary integer represented by the source AP family.

## Closure execution

Workflow:

```text
.github/workflows/collatz-math111-r12-sharded-closure.yml
```

Run:

```text
34764316089
```

Head SHA:

```text
eba8a5b139d295fc12fc132cb93e99957336f097
```

Final GitHub Actions state:

```text
status:     completed
conclusion: success
jobs:       128
```

The full jobs API was audited in two pages (`100 + 28` jobs). No queued job and no failed job remained. Every shard job completed successfully, including the step

```text
Run exact shard closure
```

which requires the unchanged generalized exact AP-union engine to emit

```text
PASS generalized exact AP-union audit
```

before the job may succeed.

## Acceptance gate

The previously frozen MATH-111 acceptance gate is therefore satisfied:

1. exact MATH-110 source totals fixed;
2. source-record partition exact/disjoint/exhaustive;
3. all 128 shard jobs completed;
4. all 128 jobs concluded `success`;
5. every job's exact closure step concluded `success`;
6. no resource/job failure remains to classify.

Therefore, within the audited multi-paid framework,

```text
r=12 CLOSED
```

and the certified frontier becomes

```text
r>=12 CLOSED
2<=r<=11 OPEN
```

## Claim boundary

This result is an exact finite closure of the `r=12` multi-paid layer only.

It does **not** by itself prove:

- `r=11` or any lower paid-count layer;
- paid-layer coverage including the `r=0,1` semantic boundary;
- first universal Farey-cell emptiness;
- the universal reduction from the first cell to every positive integer;
- the Collatz conjecture.
