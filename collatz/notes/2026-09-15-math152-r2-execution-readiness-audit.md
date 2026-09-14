# MATH-152 — `r=2` exact execution-readiness audit

Date: 2026-09-15

## Status

`MAINLINE PREFLIGHT / EXACT REPRESENTATION READY AFTER ARBITRARY-PRECISION GLOBAL SPLIT / EXECUTION NOT LAUNCHED / NO r=2 CLOSURE CLAIM`

## Frozen exact workload

```text
classification                939 = 3 safe + 104 singleton + 832 critical
branch-and-bound nodes        6,218
AP source cylinders           1,116
represented occurrence mass  74,283,701,945,452,943,666
maximum multiplicity          21,350,398,233,904,928,148
```

Both the global occurrence mass and the largest unsplit multiplicity exceed `2^64-1 = 18,446,744,073,709,551,615`. Therefore the unsplit `r=2` source is **not** directly representable in the unchanged C++ AP struct whose multiplicity field is `uint64_t`.

This is the representation-width barrier identified by MATH-113; it is not a mathematical survivor.

## Exact arbitrary-precision split before C++ ingestion

MATH-114 performs the global partition in Python arbitrary-precision arithmetic and splits AP parameter intervals exactly before any shard is passed to MATH-108.

The resulting 128-way representation is:

```text
source records                1,116
split pieces                  1,235
only additional pieces        119
128-shard cap                 580,341,421,448,851,123
minimum shard mass            580,341,421,448,851,114
maximum shard mass            580,341,421,448,851,123
maximum pieces per shard      128
```

Every split-piece multiplicity and every shard-local occurrence mass fits `uint64_t`. Thus the unchanged MATH-108 C++ engine is safe **after** the exact arbitrary-precision global split.

The global total must remain in Python/arbitrary-precision certificate accounting and must not be accumulated into a `uint64_t` total inside the C++ engine.

## Resource bound

By MATH-148,

```text
ceil(580341421448851123 / 2^40) = 527818 < 1000000 = STATE_CAP.
```

Thus even the largest split AP needs at most 40 exact parameter-half bisections after isolation to remove a pure `STATE_CAP` obstruction.

The separate `MAX_DEPTH = 1000` exact closure obligation remains empirical.

## Claim boundary

This audit proves exact execution readiness only after the arbitrary-precision global split. It does not prove `r=2 CLOSED`, paid-layer coverage, first-cell emptiness, or the Collatz conjecture.

## Execution policy

Keep the workflow manual-only and unlaunched while higher frontier layers are running. The prepare job must retain arbitrary-precision total-mass assertions and only pass shard-local `u64`-safe records to MATH-108.
