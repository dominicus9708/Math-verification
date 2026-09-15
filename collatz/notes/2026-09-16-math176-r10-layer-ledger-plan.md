# MATH-176 — r=10 original-shard ledger and layer aggregation plan

Date: 2026-09-16

Status: SUPPORT / REPRODUCIBILITY INFRASTRUCTURE / NO r=10 LAYER CLOSURE CLAIM

## Purpose

The MATH-117 r=10 source is frozen and exactly partitioned by MATH-114 into 128 original shards. Long-running retry workflows use different exact scheduling geometries for giant and fragmented original shards. MATH-176 fixes the bookkeeping rule needed to prevent omission, duplication, or loss of final certificates while these retries proceed.

This is not a new mathematical filter and does not strengthen any closure theorem. It records exact execution state and specifies the final layer-level aggregation audit.

## Frozen r=10 layer

```text
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
original shards               128
```

## Current original-shard ledger

```text
shard 0       CLOSED — MATH-153 final original-shard certificate
shard 1       CLOSED — MATH-159 final original-shard certificate
shard 2       CLOSED — MATH-162 final original-shard certificate
shards 3..13  OPEN — MATH-168 generic 3^20 giant family prepared
shards 14..127
              OPEN — MATH-166 fragmented generic family prepared, except shard 18
shard 18      CLOSED — MATH-161 final original-shard certificate
r=10 layer    OPEN
```

Closed original-shard set at this snapshot:

```text
{0, 1, 2, 18}
```

The independently certified giant boundary shards `0..2` all belong to the `3^19` step family. Generic giant shards `3..13` use step `3^20`; they therefore remain OPEN until they receive their own exact original-shard certificates.

MATH-161 run `34990207168` closed original shard 18 only after all 64 recursive exact subshards passed unchanged MATH-108 and dependent certificate job `104526872083` verified exact total mass `215291123464`.

MATH-162 run `34990484411` closed original shard 2 only after all 64 exact giant-AP micros passed unchanged MATH-108 and dependent certificate job `104533295513` verified exact total mass `215291123465`.

## Permanent ledger rule

A row may be promoted from `OPEN` to `CLOSED` only after an original-shard certificate verifies all of the following:

1. the source is exactly the corresponding frozen MATH-114 original shard;
2. any retry partition is an exact disjoint AP-parameter partition of that source;
3. every retry piece has an unchanged MATH-108 `PASS` closure result;
4. certified closed occurrence mass equals each retry-piece source mass;
5. the retry-piece masses sum exactly to the original-shard mass.

Partial micro/subshard PASS counts are progress metadata only and are never substituted for an original-shard closure certificate.

## Final 128-way layer aggregation obligation

Only after all 128 original shards are individually `CLOSED` may a layer-level audit test:

```text
closed original-shard count = 128
sum(original-shard certified mass) = 27,557,263,803,397
```

The aggregator must also verify that the closed shard identities are exactly the frozen MATH-114 shard IDs `0..127`, with no duplicate ID and no missing ID.

Only that successful aggregation may promote

```text
r=10 layer  CLOSED
```

within the audited multi-paid framework. It still does not by itself establish first-cell emptiness or the Collatz conjecture.

## Current claim boundary

At this snapshot:

```text
original shards closed  4 / 128
original shards open    124 / 128
r=10 layer              OPEN
```

The next structurally independent giant target is original shard 3, the first `3^20` giant-AP shard. Fragmented originals other than shard 18 remain independently OPEN.
