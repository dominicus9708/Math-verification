# MATH-154 — `r=10` fragmented-shard source-chunk pilot

Date: 2026-09-15

## Status

`SUPPORT / EXACT RESOURCE-SCHEDULING PILOT / NOT LAUNCHED / NO r=10 CLOSURE CLAIM`

## Motivation

MATH-117 attempt 1 timed out after 180 minutes not only on the single-giant-AP shards but also on fragmented shards. The unchanged MATH-108 engine was invoked with

```text
source_chunk = 2000.
```

When an exact state becomes too large, `audit` recursively splits the original source-record list and restarts the child audit from depth 0. A large initial source chunk can therefore cause repeated shared-prefix work before the source-record partition is sufficiently small.

## Exact shard-18 geometry

The preserved MATH-117 prepared artifact gives original shard 18:

```text
AP records                 2,444
occurrence mass            215,291,123,464
maximum AP multiplicity    116,786,684,442
odd-step exponent range    21..49
```

The most common odd-step exponents by record count begin:

```text
3^43  182 records
3^42  177 records
3^44  176 records
3^41  170 records
3^40  164 records
```

## Pilot scheduling change

Keep the exact shard input unchanged, but call the unchanged MATH-108 engine with

```text
source_chunk = 128
```

rather than 2000.

For 2,444 source records this starts from exactly 20 disjoint input chunks:

```text
19 chunks of 128 records
1 chunk of 12 records.
```

This is not pruning. MATH-108 already treats initial chunks independently and adds closed occurrence mass. The union of the 20 source-record chunks is exactly the original shard-18 source list.

A smaller `source_chunk` may reduce resource-split prefix recomputation, at the possible cost of losing cross-chunk AP merging. The effect on runtime is therefore empirical and must be benchmarked.

## Pilot gate

1. Regenerate the exact MATH-117 prepared `r=10` 128-shard artifact.
2. Assert shard 18 has 2,444 AP records and occurrence mass `215291123464`.
3. Run the unchanged MATH-108 engine on the unchanged shard-18 file with arguments:

```text
expected_cylinders = 2444
expected_occurrences = 215291123464
source_chunk = 128
```

4. Require `PASS generalized exact AP-union audit` and exact closed mass equality.

If the pilot passes within the workflow timeout, shard 18 is closed exactly and `source_chunk=128` becomes a candidate schedule for the fragmented-shard regime. If it times out, no mathematical failure is inferred.

## Claim boundary

This pilot changes only source-record scheduling. It does not change AP membership, transition arithmetic, `STATE_CAP`, `MAX_DEPTH`, or the frozen floor. It does not prove `r=10 CLOSED`.
