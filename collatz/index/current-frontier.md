# Current Collatz frontier through MATH-176 ledger audit and MATH-168 shard 6 launch

Date: 2026-09-16

This file is the compact restart point. Detailed calculations remain in `collatz/notes/`, `collatz/results/`, and `collatz/src/`.

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — original shards {0,1,2,3,4,5,18} CLOSED; 121 unresolved
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid r=8                       OPEN — MATH-145 execution-ready, not launched
Multi-paid r=7                       OPEN — MATH-146 execution-ready, not launched
Multi-paid r=6                       OPEN — MATH-147 execution-ready, not launched
Multi-paid r=5                       OPEN — MATH-149 execution-ready, not launched
Multi-paid r=4                       OPEN — MATH-150 execution-ready, not launched
Multi-paid r=3                       OPEN — MATH-151 execution-ready, not launched
Multi-paid r=2                       OPEN — MATH-152 execution-ready, not launched
```

No finite layer or original-shard result is promoted to first-cell emptiness or the Collatz conjecture without separate coverage and implication-chain audits.

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
shards 0..2              giant step 3^19 = 1,162,261,467
shards 3..13             giant step 3^20 = 3,486,784,401
```

## Permanently CLOSED original r=10 shards

```text
shard 0   MATH-153   run 34947502210   mass 215,291,123,465
shard 1   MATH-159   run 34962500310   mass 215,291,123,465
shard 2   MATH-162   run 34990484411   mass 215,291,123,465
shard 3   MATH-164   run 35015125184   mass 215,291,123,465
shard 4   MATH-168   run 35041888071   mass 215,291,123,465
shard 5   MATH-168   run 35047509321   mass 215,291,123,465
shard 18  MATH-161   run 34990207168   mass 215,291,123,464
```

```text
permanent CLOSED set     {0,1,2,3,4,5,18}
closed count             7 / 128
unresolved count         121 / 128
certified closed mass    1,507,037,864,254
```

The `r=10` layer remains OPEN.

### MATH-168 shard 5 final closure

Workflow run `35047509321` regenerated the frozen source and selected original shard 5 with step `3^20` and mass `215,291,123,465`. MATH-156 split it into 64 exact consecutive parameter intervals. All 64 unchanged MATH-108 micro jobs completed `success`, and final certificate job `104655154075` completed `success` after auditing complete coverage and PASS logs.

Permanent records:

```text
collatz/notes/2026-09-16-math168-r10-shard5-final-closure.md
collatz/results/2026-09-16-math168-r10-shard5-final-closure.tsv
```

## Active giant-family gate — original shard 6

MATH-168 workflow run `35090872254` is active for original shard 6 after launch-target commit `fbce6659918082f0aa93509482ad581816be29a7`.

Shard 6 remains OPEN until its 64 exact micro jobs and dependent final original-shard certificate all succeed. Shards `7..13` remain independently OPEN and require their own certificates.

## Fragmented-family scheduling

Original shards `14..127` are fragmented exact AP unions. MATH-161 independently CLOSED shard 18 after recursive 64-way exact repartitioning and complete final certification.

MATH-166 remains the generic fragmented 64-way executor. MATH-171 is the selective exact 256-way fallback for resource timeout. MATH-173/174 audit fallback geometry and `source_chunk=1` independence. No fragmented shard other than 18 is closed by those support results.

Exact retry rule from MATH-160: retries may refine only exact representation or scheduling. They may not delete candidates, relax conditions, change the frozen source, or reinterpret timeout as mathematical evidence.

MATH-178 is a `SUPPORT / RESOURCE-SCHEDULING BARRIER`: current exact finite telemetry rejects occurrence-mass-only workload prediction and direct reuse of a previous giant shard's micro-index runtime ranking. It does not alter any proof condition.

## MATH-176 — permanent original-shard ledger

Authoritative files:

```text
collatz/results/2026-09-16-math176-r10-original-shard-ledger.tsv
collatz/src/2026_09_16_math176_r10_original_shard_ledger_validator.py
.github/workflows/collatz-math176-r10-original-shard-ledger-audit.yml
collatz/notes/2026-09-16-math176-r10-layer-ledger-plan.md
```

The validator regenerates the canonical MATH-115 `r=10` source and exact MATH-114 128-way partition. Every CLOSED ledger row is checked for ID uniqueness/range, `CLOSED` status, frozen shard mass, permanent certificate path, certificate MATH ID, workflow run, shard number, certified mass, and CLOSED marker.

After adding shard 5, ledger audit run `35090861508`, job `104776561220`, completed `success`.

```text
closed IDs               {0,1,2,3,4,5,18}
closed original shards   7 / 128
certified closed mass    1,507,037,864,254
r10 layer closure claim  NO
```

Final `--require-complete` aggregation requires all 128 IDs exactly once and total certified mass `27,557,263,803,397`. Only then may `r=10` be promoted to CLOSED within the audited multi-paid framework.

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

MATH-148 finite STATE_CAP half-bisection depths remain:

```text
r12 13   r11 15   r10 18   r9 21   r8 24   r7 26
r6  29   r5  32   r4  34   r3 37   r2 40
```

This controls only `STATE_CAP <= 1,000,000`; closure before `MAX_DEPTH=1000` remains an execution obligation.

## Remaining proof obligations

1. Finish all remaining original `r=10` shards with complete exact certificates and pass MATH-176 complete aggregation.
2. Execute `r=9,...,2` in frontier order with exact scheduling adapted to each source geometry.
3. Audit one-paid/multi-paid coverage, including `r=0/1` semantics and any omitted ordinary-integer address families.
4. Audit the complete first universal Farey-cell implication chain.
5. Separately prove or re-audit the universal reduction from the frozen published baseline plus first-cell closure to every positive integer.

## Claim boundary

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

No lower item is promoted to a higher one without its separate audit.
