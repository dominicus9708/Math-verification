# MATH-166 — generic fragmented `r=10` recursive64 exact closure gate

Date: 2026-09-16

## Status

`MAINLINE INFRASTRUCTURE / EXECUTION-READY / NO NEW CLOSURE CLAIM`

## Purpose

MATH-161 tests recursive exact mass balancing on original fragmented shard 18. MATH-166 packages the same audited architecture into a manual generic workflow for any original prepared `r=10` shard in the fragmented range `14..127`.

Workflow:

```text
.github/workflows/collatz-math166-r10-fragmented-recursive64-generic.yml
```

It is `workflow_dispatch` only and requires one input:

```text
original_shard = integer in 14..127
```

## Frozen-source guards

For the selected original shard the gate regenerates the unchanged exact `r=10` source and the unchanged MATH-114 128-way prepared partition, then requires:

```text
14 <= original_shard <= 127
source row count > 1
source mass in {215291123463, 215291123464}
```

Thus the generic gate cannot silently accept a giant-AP shard `0..13` or an unrelated workload.

## Recursive exact normalization

The selected original source is passed unchanged to the MATH-115 wrapper around MATH-114 with

```text
subshards = 64.
```

The gate requires:

```text
64 certified subshards
sum(subshard mass) = original source mass
max(subshard mass) <= 3363923805
within-original mass spread <= 6
all emitted masses uint64-safe
```

These bounds are not assumed from MATH-161 alone; the selected source is re-audited at runtime.

## Exact closure execution

Every certified subshard is run through unchanged MATH-108 with explicit

```text
source_chunk = 1.
```

The final dependent certificate requires every subshard log to contain:

```text
PASS generalized exact AP-union audit
cylinders = certified piece count
occurrences = certified subshard mass
closed_occurrence_mass = certified subshard mass
source_chunk = 1
```

and requires all 64 certified masses to reconstruct the selected original source mass exactly.

## Relationship to MATH-160 and MATH-161

MATH-160 permits exact scheduling refinement after a resource timeout but forbids candidate deletion or condition relaxation. MATH-166 implements that rule generically for the fragmented `r=10` population using the resource geometry established by MATH-161.

MATH-161 remains the first live pilot of this recursive64 architecture. MATH-166 is not launched automatically while MATH-161 and MATH-162 consume runner capacity.

## Claim boundary

A successful MATH-166 invocation closes only the specific original shard supplied to that invocation. Different original shard indices require independent complete executions and final certificates. No successful invocation by itself closes the `r=10` layer, first universal cell, or Collatz conjecture.
