# Current Collatz frontier through MATH-176 ledger automation and MATH-168 shard 4 execution

Date: 2026-09-16

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — original shards {0,1,2,3,18} CLOSED; 123 unresolved
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid r=8                       OPEN — MATH-145 execution-ready, not launched
Multi-paid r=7                       OPEN — MATH-146 execution-ready, not launched
Multi-paid r=6                       OPEN — MATH-147 execution-ready, not launched
Multi-paid r=5                       OPEN — MATH-149 execution-ready, not launched
Multi-paid r=4                       OPEN — MATH-150 execution-ready, not launched
Multi-paid r=3                       OPEN — MATH-151 execution-ready, not launched
Multi-paid r=2                       OPEN — MATH-152 execution-ready, not launched
```

No finite layer or original-shard result is promoted to first-cell emptiness or the Collatz conjecture without the separate coverage and implication-chain audits.

## Frozen r=10 source

```text
classification                994 = 91 safe + 396 singleton + 507 critical
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
MATH-114 original shards      128
```

MATH-143 geometry:

```text
original shards 0..13    one giant AP each
original shards 14..127  fragmented exact AP unions
```

Giant-family split:

```text
shards 0..2   step 3^19 = 1,162,261,467
shards 3..13  step 3^20 = 3,486,784,401
```

MATH-117 attempt 1 completed exact source export and exact MATH-114 preparation but its original closure wave hit the 180-minute resource limit. No mathematical FAIL, surviving-state certificate, or depth-limit contradiction was produced. Timeout remains a resource result only.

## Permanently CLOSED original r=10 shards

```text
shard 0   MATH-153   run 34947502210   mass 215,291,123,465
shard 1   MATH-159   run 34962500310   mass 215,291,123,465
shard 2   MATH-162   run 34990484411   mass 215,291,123,465
shard 3   MATH-164   run 35015125184   mass 215,291,123,465
shard 18  MATH-161   run 34990207168   mass 215,291,123,464
```

Each row above has an independent final original-shard certificate after complete exact retry coverage and unchanged MATH-108 PASS results.

Permanent CLOSED set:

```text
{0,1,2,3,18}
count = 5 / 128
certified closed mass = 1,076,455,617,324
```

The r=10 layer remains OPEN.

## MATH-168 — active giant 3^20 family gate

Original shard 4 is currently active under MATH-168 workflow run `35041888071`.

Preparation has already certified:

```text
original shard       4
source step           3^20 = 3,486,784,401
source mass           215,291,123,465
exact micro parts     64
```

The exact MATH-156 partition is

```text
215,291,123,465
= 9 * 3,363,923,805 + 55 * 3,363,923,804.
```

The 64 micros preserve the same AP step and form consecutive, disjoint parameter intervals covering the original giant AP exactly.

Preserved logs currently certify contiguous micro PASS through at least `0..8`. This is execution progress only. Original shard 4 remains OPEN until all 64 micros PASS and the dependent `certify-original-shard4` job succeeds.

Shards `5..13` remain independently OPEN and require their own complete certificates; shard-3 or shard-4 success is not transferred by analogy.

## Fragmented scheduling — MATH-161 / 166 / 171 / 173 / 174

MATH-161 established exact recursive 64-way MATH-114 repartitioning for fragmented original shards. Across original shards `14..127`:

```text
source records/shard          2427 .. 2448
recursive64 exact pieces      2481 .. 2494
64-way exact cap              3,363,923,805
subshard mass spread          3 .. 6
max pieces/subshard           244
```

Original shard 18 independently passed all 64 recursive subshards and its final original-shard certificate, so shard 18 is CLOSED. No other fragmented shard is closed by that result.

MATH-166 is the generic fragmented 64-way gate and remains the primary fragmented executor.

MATH-171 is a selective exact 256-way fallback for an original fragmented shard that suffers a resource timeout under 64-way scheduling. MATH-173 audited all 114 fragmented originals under this fallback:

```text
256-way cap                   840,980,952
recursive256 pieces/shard     2657 .. 2669
subshard mass spread          7 .. 10
max pieces/subshard           68 .. 95
```

MATH-174 confirms that with `source_chunk=1`, different AP rows are independently/sequentially audited by unchanged MATH-108. Runtime scheduling may change, but proof conditions do not.

Exact retry rule from MATH-160: retries may refine only exact representation or scheduling. They may not delete candidates, relax conditions, change the frozen source, or reinterpret timeout as mathematical evidence.

## MATH-176 — permanent original-shard ledger

Authoritative files:

```text
collatz/results/2026-09-16-math176-r10-original-shard-ledger.tsv
collatz/src/2026_09_16_math176_r10_original_shard_ledger_validator.py
.github/workflows/collatz-math176-r10-original-shard-ledger-audit.yml
collatz/notes/2026-09-16-math176-r10-layer-ledger-plan.md
```

The validator regenerates the canonical MATH-115 r=10 source and MATH-114 128-way partition, then verifies every CLOSED ledger row against the frozen original-shard mass and a permanent certificate record.

First live partial-ledger audit:

```text
run                     35042686972
job                     104625729723
result                   success
closed original shards  5 / 128
certified closed mass    1,076,455,617,324
```

Partial ledger PASS makes no layer-closure claim.

Final `--require-complete` aggregation requires all of:

```text
closed original-shard count = 128
closed IDs exactly           = {0,1,...,127}
no duplicate/missing ID
sum certified mass           = 27,557,263,803,397
```

Only after that aggregation may `r=10` be promoted to CLOSED within the audited multi-paid framework.

## Prepared lower-layer gates

```text
ID        layer  AP records  split pieces  shard cap                    max pieces/shard
MATH-142  r9       141,002       141,021       1,344,589,815,928        1,300
MATH-145  r8        65,811        65,844      10,008,021,759,883          696
MATH-146  r7        29,342        29,397      66,399,002,550,056          407
MATH-147  r6        15,133        15,183     416,023,898,569,210          197
MATH-149  r5         6,525         6,598   3,183,370,901,768,032          122
MATH-150  r4         3,675         3,761  14,416,641,320,007,807           93
MATH-151  r3         1,873         1,972 102,294,036,332,826,744           72
MATH-152  r2         1,116         1,235 580,341,421,448,851,123          128
```

For r=2, global accounting remains in Python arbitrary precision and exact splitting occurs before C++ ingestion so every emitted piece and shard-local mass is uint64-safe.

## MATH-148 — finite STATE_CAP recursion bound

Pure state-count overflow after exact isolation is finitely removable with sufficient half-bisection depth:

```text
r12 13   r11 15   r10 18   r9 21   r8 24   r7 26
r6  29   r5  32   r4  34   r3 37   r2 40
```

This controls only `STATE_CAP <= 1,000,000`; closure before `MAX_DEPTH=1000` remains an execution obligation.

## Remaining proof obligations

1. Finish all remaining original r=10 shards with complete exact certificates and pass MATH-176 complete aggregation.
2. Execute r=9,...,2 in frontier order with exact scheduling adapted to each source geometry.
3. Audit one-paid/multi-paid coverage, including r=0/1 semantics and any omitted ordinary-integer address families.
4. Audit the complete first universal Farey-cell implication chain.
5. Separately prove or re-audit the universal reduction from the frozen published baseline plus first-cell closure to every positive integer.

## Claim boundary

The project distinguishes:

```text
exact finite workload
exact finite safe subset
exact retry-piece closure
exact original-shard closure
exact finite layer closure
coverage of a proof partition
first-cell emptiness
universal reduction
full Collatz proof
```

No lower item in this list is promoted to a higher one without its separate audit.
