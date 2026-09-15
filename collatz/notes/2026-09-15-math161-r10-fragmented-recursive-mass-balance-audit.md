# MATH-161 — recursive exact mass-balance audit for all fragmented `r=10` shards

Date: 2026-09-15

## Status

`SUPPORT / EXACT RESOURCE-GEOMETRY NORMALIZATION / NO NEW CLOSURE CLAIM`

## Motivation

MATH-154 tests `source_chunk=128` on original fragmented shard 18. Direct inspection of the preserved MATH-117 exact prepared artifact shows that record-count chunking does not balance occurrence mass: the largest 128-record chunk in shard 18 has mass `213429935730`, while the full shard mass is `215291123464`.

Thus a smaller record count does not by itself guarantee a smaller high-multiplicity workload.

MATH-114 already provides a stronger exact transformation: split APs into consecutive parameter intervals capped by occurrence mass, then LPT-assign those exact pieces to mass-balanced shards.

## Source population audited

The preserved MATH-117 artifact contains 114 fragmented original shards, indices `14..127`.

Across these shards:

```text
source records per original shard     2427 .. 2448
source occurrence mass                215291123463 .. 215291123464
```

The source-record geometry is therefore narrow, while individual AP multiplicities remain highly uneven.

## Recursive 64-way MATH-114 transformation

For each original fragmented shard independently, apply the unchanged MATH-114 `build_partition` semantics with

```text
N = 64.
```

Since every source mass is either `215291123463` or `215291123464`, every shard has the same exact cap

```text
ceil(M/64) = 3363923805.
```

MATH-114 uses the exact identity

```text
AP(a,b,m) = disjoint union_j AP(a+b*offset_j,b,m_j)
```

for every split AP and preserves the total occurrence mass exactly.

## Exhaustive geometry result over original shards 14..127

The recursive partition has the following ranges across all 114 fragmented originals:

```text
exact pieces per original shard       2481 .. 2494
subshard minimum mass                 3363923799 .. 3363923802
subshard maximum mass                 3363923805 .. 3363923805
within-original mass spread           3 .. 6
minimum pieces in a subshard          1
maximum pieces in a subshard          131 .. 244
single-piece subshards                45 .. 54 of 64
maximum emitted piece mass            3363923805
```

Thus every fragmented original shard can be converted into 64 exact subshards whose occurrence masses differ by at most six ordinary occurrences.

## Shard-18 example

For original shard 18:

```text
source records             2444
source mass                215291123464
recursive exact pieces     2491
64-way cap                 3363923805
subshard mass range        3363923801 .. 3363923805
mass spread                4
pieces/subshard range      1 .. 146
single-piece subshards     47 of 64
```

This is substantially more balanced than the record-count `source_chunk=128` layout, whose largest initial chunk contains mass `213429935730`.

## Interpretation

Recursive MATH-114 is an exact external resource normalization, not pruning. It changes only where an already exact source is split and scheduled.

It has two useful consequences:

1. every emitted AP piece has multiplicity at most `3,363,923,805`, the same scale already closed repeatedly in the MATH-153 shard-0 microclosure;
2. each exact execution unit has total occurrence mass at most `3,363,923,805`, rather than allowing one record-count chunk to retain almost the full `2.15e11` original-shard mass.

This does not guarantee wall-clock completion or depth closure. State geometry can still depend on the number and arithmetic structure of AP records.

## Scheduling consequence

For fragmented `r=10` shards, the preferred escalation order is now:

```text
MATH-154 source_chunk=128 pilot
    -> if PASS, retain as a validated simple schedule;
    -> if timeout/resource failure without mathematical failure,
       switch to recursive exact 64-way MATH-114 mass balancing.
```

The recursive 64-way strategy may also be used as an independent cross-check even if MATH-154 passes.

## Claim boundary

MATH-161 proves only exact resource-geometry normalization of the frozen prepared sources. It closes no original shard and does not close the `r=10` layer, first universal cell, or Collatz conjecture.
