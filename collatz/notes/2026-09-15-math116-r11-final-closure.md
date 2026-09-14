# MATH-116 — final exact `r=11` closure

Date: 2026-09-15

## Status

`MAINLINE LAYER CLOSURE / r=11 CLOSED / NO FIRST-CELL OR COLLATZ CLAIM`

## Exact source

The unchanged MATH-115 exporter produced the frozen `r=11` source:

- AP source records: `605,972`
- prepared split pieces: `605,977`
- represented occurrence mass: `3,419,719,061,560`
- maximum unsplit multiplicity: `51,905,193,085`

The MATH-114/MATH-115 exact mass-balanced partition certificate uses 128 shards and proves:

- `TOTAL_SOURCE_RECORDS = 605972`
- `TOTAL_PIECES = 605977`
- `TOTAL_MASS = 3419719061560`
- `CAP = 26716555169`
- `MIN_SHARD_MASS = 26716555168`
- `MAX_SHARD_MASS = 26716555169`
- all shard-local counts are `u64_safe=1`
- `PASS exact_mass_balanced_partition`

## Closure gate

Workflow:

`.github/workflows/collatz-math116-r11-mass-balanced-sharded-closure.yml`

Run:

`34768752143`

Head SHA:

`ac2cd3d59ce5878632d88c1bf4f724223a285a80`

The workflow definition requires matrix shards `0..127` exactly. Every shard compiles the unchanged MATH-108 generalized exact AP-union engine, audits its shard metadata, runs the exact shard closure, and requires the log token:

`PASS generalized exact AP-union audit`

The GitHub Actions run is now:

- `status = completed`
- `conclusion = success`

There is no `continue-on-error` on the shard matrix. Therefore the successful workflow run certifies successful completion of all required shard jobs after the successful preparation/partition gate.

## Conclusion

Within the audited multi-paid framework,

```text
r >= 11  CLOSED
```

The earlier MATH-129..MATH-140 q-gate calculations remain valid exact finite safe-subset/support results, but their residual tails are no longer an obstruction to the `r=11` layer: MATH-116 closes the complete exact source by the independent AP-union route.

## Claim boundary

This does **not** yet imply:

- complete paid-layer coverage,
- first universal Farey cell emptiness,
- universal Collatz reduction,
- the Collatz conjecture.

The next multi-paid layer is `r=10`, for which MATH-117 is execution-ready.
