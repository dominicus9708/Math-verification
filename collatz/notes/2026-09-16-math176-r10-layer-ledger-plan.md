# MATH-176 — r=10 original-shard ledger and layer aggregation plan

Date: 2026-09-16

Status: SUPPORT / REPRODUCIBILITY INFRASTRUCTURE / NO r=10 LAYER CLOSURE CLAIM

## Purpose

The MATH-117 r=10 source is already frozen and exactly partitioned by MATH-114 into 128 original shards. Long-running retry workflows now use different exact scheduling geometries for giant and fragmented original shards. MATH-176 fixes the bookkeeping rule needed to prevent omission, duplication, or loss of final certificates while these retries proceed.

This is not a new mathematical filter and does not strengthen any closure theorem. It records exact execution state and specifies the final layer-level aggregation audit.

## Frozen r=10 layer

```text
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
original shards               128
```

## Live original-shard state at this snapshot

```text
shard 0       CLOSED — MATH-153 final original-shard certificate
shard 1       CLOSED — MATH-159 final original-shard certificate
shard 2       OPEN — MATH-162 giant boundary-family pilot; micro 0..39 observed exact PASS
shards 3..13  OPEN — MATH-168 generic giant family prepared
shards 14..127
              OPEN — MATH-166 fragmented generic family prepared
shard 18      OPEN — MATH-161 fragmented pilot; subshard 0..50 observed exact PASS
r=10 layer    OPEN
```

The shard-2 source is a distinct giant family with step `3^19`. Generic giant shards `3..13` use step `3^20`, so shard 2 is not redundant with MATH-168.

For shard 18, the first 47 single-AP subshards `0..46` and composite subshards `47..50` have been observed exact PASS under the unchanged MATH-108 closure criterion. This is partial subshard progress only. Original shard 18 remains OPEN until all 64 exact subshards PASS and the dependent original-shard mass certificate succeeds.

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
original shards closed  2 / 128
original shards open    126 / 128
r=10 layer              OPEN
```

MATH-161 and MATH-162 are active representative pilots. Their partial PASS frontiers are preserved as execution progress, not theorem-level closure.