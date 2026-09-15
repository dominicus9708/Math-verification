# MATH-159 — original `r=10` shard 1 final exact closure

Date: 2026-09-15

## Status

`MAINLINE / ORIGINAL SHARD EXACTLY CLOSED / NO r=10 LAYER CLOSURE CLAIM`

## Frozen source

Original prepared `r=10` shard 1 is one AP with exact occurrence mass

```text
215291123465
```

The source is regenerated from the unchanged MATH-115 `r=10` exporter and unchanged MATH-114 128-way exact prepared partition.

## Exact external partition

MATH-156 splits the single AP into 64 consecutive disjoint parameter intervals. The partition preserves the exact source set and exact total multiplicity mass.

Each micro source contains one AP and is processed by the unchanged MATH-108 exact AP-union engine with

```text
source_chunk = 1.
```

## Execution

Workflow run:

```text
34962500310
```

completed the source-preparation job, all 64 `micro-closure (0..63)` jobs, and the dependent final job

```text
certify-original-shard1
```

with `success`.

The final certificate requires, for every micro interval:

```text
PASS generalized exact AP-union audit
occurrences = certified micro mass
closed_occurrence_mass = certified micro mass
```

and checks that all 64 certified masses sum exactly to

```text
215291123465.
```

Therefore

```text
ORIGINAL r=10 SHARD 1  CLOSED
r=10 LAYER              OPEN
```

## Relationship to MATH-153

MATH-153 established the same exact 64-micro closure architecture for original shard 0. MATH-159 independently applies the generic MATH-156 single-AP microsharder to shard 1 and closes it with a separate complete execution certificate.

This validates the generic giant-AP scheduling architecture on a second original shard, but it does not permit unexecuted shards `2..13` to be closed by analogy.

## Claim boundary

MATH-159 proves exact closure only for original prepared `r=10` shard 1. The remaining original shards must each receive complete exact coverage certificates before the `r=10` layer can be promoted to CLOSED. No first-cell or Collatz claim follows from this result alone.
