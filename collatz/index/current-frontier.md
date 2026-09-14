# Current Collatz frontier through MATH-148 lower-layer preflights

Date: 2026-09-15

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — MATH-117 exact gate running
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid r=8                       OPEN — MATH-145 execution-ready, not launched
Multi-paid r=7                       OPEN — MATH-146 execution-ready, not launched
Multi-paid r=6                       OPEN — MATH-147 execution-ready, not launched
Multi-paid 2<=r<=5                   OPEN
```

No layer closure is promoted to first-cell emptiness or the Collatz conjecture without the separate coverage and implication-chain audits.

## MATH-116 — final exact `r=11` layer closure

Frozen exact source:

```text
classification                1013 = 119 safe + 414 singleton + 480 critical
AP source cylinders           605,972
prepared split pieces         605,977
represented occurrence mass  3,419,719,061,560
```

The exact mass-balanced partition certificate uses 128 shards:

```text
TOTAL_SOURCE_RECORDS  605,972
TOTAL_PIECES          605,977
TOTAL_MASS            3,419,719,061,560
CAP                    26,716,555,169
MIN_SHARD_MASS         26,716,555,168
MAX_SHARD_MASS         26,716,555,169
PASS                    exact_mass_balanced_partition
```

Workflow run `34768752143` at head SHA `ac2cd3d59ce5878632d88c1bf4f724223a285a80` completed with conclusion `success`. Its 128 matrix shards all completed successfully and each required `PASS generalized exact AP-union audit` from the unchanged MATH-108 engine. Therefore, within the audited multi-paid framework,

```text
r >= 11  CLOSED
```

Authoritative final records:

```text
collatz/results/2026-09-15-math116-r11-final-closure.tsv
collatz/notes/2026-09-15-math116-r11-final-closure.md
```

## q-gate/address deepening — retained as support

MATH-121..139 remain valid structural/support results. MATH-139 reached:

```text
D=39 exact new safe mass  1,741,505,726
cumulative q-gate safe    3,350,963,514,708
q-gate tail                  68,755,546,852
safe fraction                 97.98943873416796%
```

That finite tail is not an `r=11` survivor family: MATH-116 independently closes the complete exact source.

## MATH-117 — `r=10` exact gate running

Frozen exact source/preflight:

```text
classification                994 = 91 safe + 396 singleton + 507 critical
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
max unsplit multiplicity      830,483,089,363
mass-balanced split pieces    278,739
128-shard cap                 215,291,123,465
shard mass range              215,291,123,463 .. 215,291,123,465
```

Launch commit `e4a5cd1704122d2901437d4cc98fbbc8c8c97040`, workflow run `34881179736`.

Latest audited job state:

- prepare/source/partition certificate: `success`
- exactly 16 first-wave shard jobs are in `Run exact shard closure`
- later shards are queued by `max-parallel: 16`
- observed shard failures: `0`
- no shard closure artifact has completed yet at the latest inspection

Therefore `r=10` remains `OPEN`.

MATH-143/144 explain the resource geometry of the giant first-wave APs. For the largest split AP mass `215,291,123,465`, at most 18 exact parameter halvings reduce descendant mass below `STATE_CAP = 1,000,000`; this is a resource bound, not a closure theorem.

## Prepared lower-layer gates

### MATH-142 — `r=9`

```text
classification                977 = 72 safe + 349 singleton + 556 critical
AP source cylinders           141,002
occurrence mass               172,107,496,438,700
split pieces                  141,021
128-shard cap                 1,344,589,815,928
max pieces per shard          1,300
```

### MATH-145 — `r=8`

```text
classification                977 = 60 safe + 330 singleton + 587 critical
AP source cylinders           65,811
occurrence mass               1,281,026,785,265,013
split pieces                  65,844
128-shard cap                 10,008,021,759,883
max pieces per shard          696
```

### MATH-146 — `r=7`

```text
classification                963 = 42 safe + 291 singleton + 630 critical
AP source cylinders           29,342
occurrence mass               8,499,072,326,407,060
split pieces                  29,397
128-shard cap                 66,399,002,550,056
max pieces per shard          407
```

### MATH-147 — `r=6`

```text
classification                963 = 34 safe + 250 singleton + 679 critical
AP source cylinders           15,133
occurrence mass               53,251,059,016,858,758
split pieces                  15,183
128-shard cap                 416,023,898,569,210
max pieces per shard          197
```

All four gates are representation-safe shard-locally and use manual-only workflows. None has been launched while MATH-117 occupies the Actions queue.

## MATH-148 — finite `STATE_CAP` recursion bound

For every MATH-114 split piece in `r=2..12`, pure state-count overflow is finitely removable by exact AP parameter bisection after the AP is isolated. The least worst-case half-bisection depths are:

```text
r12 13   r11 15   r10 18   r9 21   r8 24   r7 26
r6  29   r5  32   r4  34   r3 37   r2 40
```

Each listed depth makes the worst descendant source mass at most `1,000,000`. This controls only `STATE_CAP`; exact closure before `MAX_DEPTH = 1000` remains an execution obligation.

Records:

```text
collatz/results/2026-09-15-math148-state-cap-bisection-depth.tsv
collatz/notes/2026-09-15-math148-finite-state-cap-recursion-bound.md
```

## Remaining proof obligations after layer closures

1. Finish `r=10`, then close `r=9,...,2`.
2. Audit one-paid/multi-paid coverage, including `r=0/1` semantics.
3. Audit the entire first universal cell implication chain.
4. Separately prove or re-audit the universal reduction from the frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite safe subsets, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.
