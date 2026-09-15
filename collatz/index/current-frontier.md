# Current Collatz frontier through MATH-158 r10 scheduling audit

Date: 2026-09-15

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — original shard 0 exactly CLOSED by MATH-153; remaining 127 original shards unresolved
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid r=8                       OPEN — MATH-145 execution-ready, not launched
Multi-paid r=7                       OPEN — MATH-146 execution-ready, not launched
Multi-paid r=6                       OPEN — MATH-147 execution-ready, not launched
Multi-paid r=5                       OPEN — MATH-149 execution-ready, not launched
Multi-paid r=4                       OPEN — MATH-150 execution-ready, not launched
Multi-paid r=3                       OPEN — MATH-151 execution-ready, not launched
Multi-paid r=2                       OPEN — MATH-152 execution-ready, not launched
```

No layer closure is promoted to first-cell emptiness or the Collatz conjecture without the separate coverage and implication-chain audits.

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

MATH-121..139 remain valid structural/support results. MATH-139 reached:

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
128-shard cap                 215,291,123,465
```

Workflow run `34881179736` successfully completed source export, exact MATH-114 preparation, partition-certificate audit, and prepared-shard preservation.

The first shard wave then ran the unchanged MATH-108 exact closure. The running shard jobs were cancelled at approximately 180 minutes, matching `timeout-minutes: 180`. No `FAIL`, surviving-state certificate, depth-limit exception, or contradictory arithmetic output was observed. Attempt 1 is classified as a job-timeout/resource-scheduling result, not `r=10` non-closure.

MATH-143 shows original shards `0..13` are each one giant AP of mass `215,291,123,465`; the other shards are fragmented many-record workloads. Thus occurrence-mass balance and runtime geometry are distinct.

## MATH-153 — original `r=10` shard 0 exactly CLOSED

Original shard 0 was split externally into 64 disjoint consecutive parameter intervals:

```text
215291123465 = 9 * 3363923805 + 55 * 3363923804.
```

Historical workflow run `34947502210` completed with overall conclusion `success`. All 64 unchanged MATH-108 micro-closure jobs succeeded.

The dependent final certificate job `certify-original-shard0` (`104336460767`) then verified every micro log, each micro occurrence mass, each `closed_occurrence_mass`, complete 64-way coverage, and the exact total mass

```text
215291123465.
```

Therefore:

```text
ORIGINAL r=10 SHARD 0  CLOSED
r=10 LAYER              OPEN
```

Authoritative records:

```text
collatz/results/2026-09-15-math153-r10-shard0-microclosure-progress.tsv
collatz/notes/2026-09-15-math153-r10-shard0-final-closure.md
```

The historical run retains the temporary workflow label `MATH-148` because it was launched before the project-ID collision was corrected; MATH-153 is the authoritative project ID for this computation.

## MATH-154 / MATH-157 / MATH-158 — next exact `r=10` scheduling regime

MATH-157 fixes a bimodal exact scheduler for the prepared `r=10` geometry:

```text
single giant AP shards  -> exact external AP-parameter microsharding
fragmented shards       -> smaller exact source-record chunks
```

MATH-158 audits the unchanged MATH-108 engine and confirms that `source_chunk` changes scheduling only. Every source record is assigned to exactly one initial chunk; any `TooBig` branch is split by exact source-list or AP-parameter set identities; final PASS requires `closed_occurrence_mass == total_occurrences`.

The immediate fragmented-shard pilot is MATH-154 on original shard 18:

```text
AP records                 2,444
occurrence mass            215,291,123,464
maximum AP multiplicity    116,786,684,442
source_chunk               128
initial exact chunks       20 = 19*128 + 12
```

A successful MATH-154 run closes original shard 18 only and validates the fragmented-shard schedule. It does not close `r=10`.

## Prepared lower-layer gates

All remaining layers `r=9..2` have exact frozen sources, exact MATH-114 128-way partitions, manual-only workflows, and no closure claim.

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

For `r=2`, the global total occurrence mass and largest unsplit multiplicity exceed `uint64_t`. MATH-152 therefore keeps global accounting in Python arbitrary precision and performs exact splitting before C++ ingestion. Every resulting split-piece multiplicity and shard-local mass is `uint64_t` safe.

None of these lower-layer workflows is promoted while the `r=10` exact resource architecture remains the active frontier.

## MATH-148 — finite `STATE_CAP` recursion bound

For every MATH-114 split piece in `r=2..12`, pure state-count overflow is finitely removable by exact AP parameter bisection after the AP is isolated:

```text
r12 13   r11 15   r10 18   r9 21   r8 24   r7 26
r6  29   r5  32   r4  34   r3 37   r2 40
```

Each listed depth makes the worst descendant source mass at most `1,000,000`. This controls only `STATE_CAP`; exact closure before `MAX_DEPTH = 1000` remains an execution obligation.

## Remaining proof obligations after layer closures

1. Resolve all remaining original `r=10` shards under exact schedules; immediate next gate: MATH-154 shard-18 fragmented pilot.
2. Then execute `r=9,...,2` in frontier order, adapting exact scheduling to each observed geometry rather than assuming `r=10` runtime behavior.
3. Audit one-paid/multi-paid coverage, including `r=0/1` semantics.
4. Audit the entire first universal cell implication chain.
5. Separately prove or re-audit the universal reduction from the frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project distinguishes exact finite workload, exact finite safe subsets, exact original-shard closure, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.
