# Current Collatz frontier through MATH-162 and MATH-161 final original-shard closures

Date: 2026-09-16

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — original shards 0,1,2,18 exactly CLOSED; 124 original shards unresolved
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid r=8                       OPEN — MATH-145 execution-ready, not launched
Multi-paid r=7                       OPEN — MATH-146 execution-ready, not launched
Multi-paid r=6                       OPEN — MATH-147 execution-ready, not launched
Multi-paid r=5                       OPEN — MATH-149 execution-ready, not launched
Multi-paid r=4                       OPEN — MATH-150 execution-ready, not launched
Multi-paid r=3                       OPEN — MATH-151 execution-ready, not launched
Multi-paid r=2                       OPEN — MATH-152 execution-ready, not launched
```

No original-shard or layer closure is promoted to first-cell emptiness or the Collatz conjecture without the separate coverage and implication-chain audits.

## MATH-116 — final exact `r=11` layer closure

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
AP source cylinders           605,972
prepared split pieces         605,977
represented occurrence mass  3,419,719,061,560
```

Workflow run `34768752143` completed with `success`; all 128 shard jobs required `PASS generalized exact AP-union audit`. Therefore, within the audited multi-paid framework:

```text
r >= 11  CLOSED
```

Authoritative records:

```text
collatz/results/2026-09-15-math116-r11-final-closure.tsv
collatz/notes/2026-09-15-math116-r11-final-closure.md
```

## q-gate/address deepening — support only

MATH-121..139 remain structural/support results. MATH-139 reached:

```text
D=39 exact new safe mass  1,741,505,726
cumulative q-gate safe    3,350,963,514,708
q-gate tail                  68,755,546,852
safe fraction                 97.98943873416796%
```

That finite tail is not an `r=11` survivor family because MATH-116 independently closes the complete exact source.

## MATH-117 attempt 1 — `r=10` resource timeout, no mathematical failure

Frozen exact source:

```text
classification                994 = 91 safe + 396 singleton + 507 critical
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
mass-balanced split pieces    278,739
original shards               128
128-shard cap                 215,291,123,465
```

Workflow run `34881179736` completed source export, exact MATH-114 preparation, partition-certificate audit, and prepared-shard preservation. The original 128 closure jobs then hit the 180-minute resource limit. No `FAIL`, surviving-state certificate, depth-limit exception, or contradictory arithmetic output was observed. This remains a resource/scheduling result, not `r=10` non-closure.

MATH-143 shows original shards `0..13` are each one giant AP; original shards `14..127` are fragmented many-record workloads. Further audit separates the giant group into `3^19` step shards `0..2` and `3^20` step shards `3..13`.

## MATH-153 — original `r=10` shard 0 exactly CLOSED

Original shard 0 was split into 64 disjoint consecutive parameter intervals:

```text
215291123465 = 9 * 3363923805 + 55 * 3363923804.
```

Workflow run `34947502210` completed with overall `success`. All 64 unchanged MATH-108 micro closures succeeded, and `certify-original-shard0` verified every PASS log, every micro occurrence mass, every `closed_occurrence_mass`, complete 64-way coverage, and exact total mass `215291123465`.

```text
ORIGINAL r=10 SHARD 0  CLOSED
```

Authoritative records:

```text
collatz/results/2026-09-15-math153-r10-shard0-microclosure-progress.tsv
collatz/notes/2026-09-15-math153-r10-shard0-final-closure.md
```

## MATH-159 — original `r=10` shard 1 exactly CLOSED

MATH-159 independently applies the generic MATH-156 exact single-AP microsharder to original shard 1. Workflow run `34962500310` completed source preparation, all 64 micro closures, and the dependent `certify-original-shard1` job with `success`.

```text
ORIGINAL r=10 SHARD 1  CLOSED
```

Authoritative records:

```text
collatz/results/2026-09-15-math159-r10-shard1-final-closure.tsv
collatz/notes/2026-09-15-math159-r10-shard1-final-closure.md
```

## MATH-162 — original `r=10` shard 2 exactly CLOSED

Original shard 2 is the final giant boundary shard with step

```text
3^19 = 1,162,261,467.
```

Workflow run `34990484411` completed with `success`. All 64 exact micro closures passed unchanged MATH-108 with explicit `source_chunk=1`. Dependent certificate job `104533295513` verified all micro metadata and logs, `occurrences=mass`, `closed_occurrence_mass=mass`, and exact total source mass:

```text
215,291,123,465.
```

Final output:

```text
PASS MATH-162 original r10 shard2 exact 64-micro closure mass=215291123465
NO r10 LAYER CLOSURE CLAIM
```

Therefore:

```text
ORIGINAL r=10 SHARD 2  CLOSED
```

Authoritative records:

```text
collatz/results/2026-09-16-math162-r10-shard2-final-closure.tsv
collatz/notes/2026-09-16-math162-r10-shard2-final-closure.md
```

The independently certified `3^19` giant boundary family `0..2` is now complete at original-shard level. This does not close the distinct `3^20` giant family `3..13` by analogy.

## MATH-154 — fragmented shard 18 record-chunk pilot: resource timeout

MATH-154 tested original fragmented shard 18:

```text
AP records                 2,444
occurrence mass            215,291,123,464
maximum AP multiplicity    116,786,684,442
source_chunk               128
```

Workflow run `34962372512` passed exact source regeneration and the shard-18 geometry audit. The unchanged MATH-108 closure step then ran until the 180-minute job limit and was cancelled. No mathematical FAIL certificate was observed. MATH-154 is classified as a resource timeout, not a shard-18 non-closure result.

## MATH-160 — exact timeout retry rule

Resource retries may refine only exact representation or scheduling. They may not delete candidates, relax conditions, change the frozen source, or reinterpret timeout as mathematical evidence. Every promoted closure still requires a complete exact coverage certificate.

## MATH-161 — original `r=10` shard 18 exactly CLOSED by recursive64

MATH-161 first audited all 114 fragmented original shards `14..127` under a second exact MATH-114 partition with 64 subshards per original shard.

Across all fragmented originals:

```text
original source records/shard     2427 .. 2448
original occurrence mass          215291123463 .. 215291123464
recursive exact pieces            2481 .. 2494
64-way exact cap                  3363923805
subshard mass spread              3 .. 6
maximum pieces/subshard           244
```

For shard 18:

```text
source records                    2444
source mass                       215291123464
recursive exact pieces            2491
recursive subshards               64
subshard mass range               3363923801 .. 3363923805
workflow run                      34990207168
final certificate job             104526872083
```

All 64 recursive exact subshards passed unchanged MATH-108 with `source_chunk=1`. The dependent certificate rechecked exact metadata, `PASS generalized exact AP-union audit`, `occurrences=mass`, `closed_occurrence_mass=mass`, and exact total mass `215291123464`.

Final output:

```text
PASS MATH-161 original r10 shard18 recursive64 exact closure mass=215291123464
NO r10 LAYER CLOSURE CLAIM
```

Therefore:

```text
ORIGINAL r=10 SHARD 18  CLOSED
```

Authoritative records:

```text
collatz/results/2026-09-16-math161-r10-shard18-final-closure.tsv
collatz/notes/2026-09-16-math161-r10-shard18-final-closure.md
```

This validates the recursive64 fragmented-shard scheduler on one complete original fragmented shard. Other fragmented originals remain independently OPEN.

## Current `r=10` original-shard ledger

```text
CLOSED original shards       {0,1,2,18}
closed count                 4 / 128
unresolved count             124 / 128
shards 3..13                 OPEN — distinct 3^20 giant family; MATH-168 gate prepared
shards 14..127 except 18     OPEN — fragmented family; MATH-166 gate prepared
r=10 layer                   OPEN
```

MATH-176 fixes the permanent ledger rule: an original shard is CLOSED only after its own dependent complete coverage certificate succeeds. The `r=10` layer may be promoted only after all original IDs `0..127` are present exactly once and their certified masses sum exactly to `27,557,263,803,397`.

The next structurally independent giant target is original shard 3, the first `3^20` giant-AP shard.

## Prepared lower-layer gates

All remaining layers `r=9..2` have exact frozen sources, exact MATH-114 128-way partitions, manual workflows, and no closure claim.

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

For `r=2`, global accounting remains in Python arbitrary precision and exact splitting occurs before C++ ingestion so every emitted piece and shard-local mass is `uint64_t` safe.

## MATH-148 — finite `STATE_CAP` recursion bound

For every MATH-114 split piece in `r=2..12`, pure state-count overflow is finitely removable by exact AP parameter bisection after isolation:

```text
r12 13   r11 15   r10 18   r9 21   r8 24   r7 26
r6  29   r5  32   r4  34   r3 37   r2 40
```

This controls only `STATE_CAP`; exact closure before `MAX_DEPTH = 1000` remains an execution obligation.

## Remaining proof obligations after layer closures

1. Resolve all remaining original `r=10` shards with complete exact certificates. Giant AP shards use exact parameter microsharding; fragmented shards use recursive exact mass balancing when record chunking is insufficient.
2. Execute `r=9,...,2` in frontier order with scheduling adapted to each exact geometry.
3. Audit one-paid/multi-paid coverage, including `r=0/1` semantics.
4. Audit the entire first universal cell implication chain.
5. Separately prove or re-audit the universal reduction from the frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project distinguishes exact finite workload, exact finite safe subsets, exact original-shard closure, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.
