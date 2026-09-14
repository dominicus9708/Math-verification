# MATH-143 — `r=10` exact shard-geometry audit

Date: 2026-09-15

## Status

`SUPPORT / EXACT RESOURCE-GEOMETRY AUDIT / NO r=10 CLOSURE CLAIM`

This audit inspects the exact prepared artifact from MATH-117 run `34881179736` after its successful exporter, mass-balanced preparation, and partition-certificate stages.

## Global invariants

```text
shards                    128
source/split pieces       278,739
represented mass          27,557,263,803,397
minimum shard mass           215,291,123,463
maximum shard mass           215,291,123,465
mass spread                              2
```

Thus MATH-114 achieves essentially perfect occurrence-mass balance.

## Bimodal shard geometry

The source-record geometry is not balanced in the same way as the occurrence mass.

- shards `0..13` each contain exactly one piece;
- each of those 14 pieces has multiplicity exactly equal to the cap `215,291,123,465`;
- the remaining shards are highly fragmented, with piece counts around the mid-2400s;
- global pieces-per-shard range is `1..2448`;
- median pieces per shard is `2445`;
- mean pieces per shard is `2177.6484375`.

Therefore two different computational regimes coexist under the same mass-balanced theorem partition:

1. **single giant AP** shards, which directly stress the MATH-108 exact parameter-bisection mechanism;
2. **many-record** shards, which stress AP-state population/closure propagation.

Neither regime changes theorem membership or ordinary-integer mass.

## Odd-step structure

Across the prepared pieces there are exactly 36 odd-step classes, all powers of three:

```text
3^19 .. 3^54
```

The three most frequent classes by piece count are:

```text
3^43   20,748 pieces
3^42   20,163 pieces
3^44   20,095 pieces
```

## Interpretation

Occurrence mass alone is not a runtime proxy. MATH-117 has near-perfect mass balance but deliberately nonuniform AP-record geometry. A slow shard is therefore not evidence of a mathematical survivor; its log/state-growth behavior must be inspected before any interpretation.

The current exact MATH-117 gate remains the theorem-facing test. This note does not promote `r=10` and makes no first-cell or Collatz claim.
