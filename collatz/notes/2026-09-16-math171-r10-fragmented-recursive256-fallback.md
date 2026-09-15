# MATH-171 — r=10 fragmented original-shard recursive256 exact fallback

Date: 2026-09-16

## Status

`PREPARED / MANUAL-ONLY / NOT EXECUTED`

This gate is a proof-preserving resource fallback for an `r=10` fragmented original shard if the 64-way recursive gate (MATH-161/MATH-166 geometry) proves too coarse for the 180-minute per-job limit.

It makes no new Collatz closure claim until a selected workflow run completes its dependent final certificate successfully.

## Frozen source

The gate regenerates the exact MATH-115 `r=10` source and the exact original 128-way MATH-114 partition, then requires the selected original shard to satisfy:

```text
original shard index       14..127
source-record count        > 1
source occurrence mass     215291123463 or 215291123464
```

Thus it does not import a MATH-161 partial result or infer closure from another original shard.

## Recursive256 refinement

The complete selected original-shard AP source is repartitioned by unchanged MATH-114 semantics into 256 exact subshards.

For either allowed original-shard mass,

```text
ceil(source_mass / 256) = 840980952.
```

Therefore every emitted subshard is required to have occurrence mass at most `840,980,952`, about one quarter of the MATH-161/MATH-166 64-way cap `3,363,923,805`.

The exact identity remains

```text
AP(a,b,m) = disjoint union of consecutive AP parameter intervals,
```

so only scheduling granularity changes.

## Exact closure condition

Each of the 256 matrix jobs runs the unchanged MATH-108 engine with `source_chunk=1` and must emit

```text
PASS generalized exact AP-union audit
```

with exact equality of

```text
reported cylinders       = certified pieces
reported occurrences     = certified subshard mass
closed_occurrence_mass   = certified subshard mass.
```

The dependent `certify-original-shard` job then independently checks all 256 logs and requires their certified masses to sum exactly to the selected original source mass.

Only that final certificate may promote the selected original shard to `CLOSED`.

## Runtime telemetry

Proof-neutral telemetry is retained separately:

```text
wall_seconds
closure_leaves
resource_splits
max_depth
max_state
distinct_steps
max_piece_mass
source_sha256
```

These fields may guide future scheduling but are not substituted for any mathematical closure condition.

## Execution rule

MATH-171 should not be launched while a valid 64-way run is progressing normally. It is intended for one of the following observed resource conditions:

```text
1. a 64-way fragmented subshard reaches the job timeout without a mathematical FAIL certificate;
2. composite-tail wall time becomes incompatible with the existing resource gate;
3. an independent full-original retry is preferable to cross-run artifact stitching.
```

A timeout remains a scheduling result only; it is not evidence of a surviving Collatz family.

## Authoritative workflow

```text
.github/workflows/collatz-math171-r10-fragmented-recursive256-fallback.yml
```

## Claim boundary

MATH-171 changes resource layout only. It does not close the `r=10` layer, the first universal cell, or the Collatz conjecture by itself.
