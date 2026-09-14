# Current Collatz frontier after MATH-116 final r11 closure

Date: 2026-09-15

## Exact status

```text
Collatz conjecture                    OPEN
First universal Farey cell           OPEN
One-paid detailed band t=7..16       CLOSED on audited Bellman/address criterion
Multi-paid r>=11                     CLOSED
Multi-paid r=10                      OPEN — MATH-117 exact gate running
Multi-paid r=9                       OPEN — MATH-142 execution-ready, not launched
Multi-paid 2<=r<=8                   OPEN
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

The exact mass-balanced partition certificate uses 128 shards and fixes:

```text
TOTAL_SOURCE_RECORDS  605,972
TOTAL_PIECES          605,977
TOTAL_MASS            3,419,719,061,560
CAP                    26,716,555,169
MIN_SHARD_MASS         26,716,555,168
MAX_SHARD_MASS         26,716,555,169
PASS                    exact_mass_balanced_partition
```

Workflow run `34768752143` at head SHA `ac2cd3d59ce5878632d88c1bf4f724223a285a80` completed with conclusion `success`. Its matrix requires shards `0..127` exactly, and every shard requires `PASS generalized exact AP-union audit` from the unchanged MATH-108 engine. Therefore, within the audited multi-paid framework,

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

Launch commit:

`e4a5cd1704122d2901437d4cc98fbbc8c8c97040`

Workflow run:

`34881179736`

Current audited state:

- exact source export: `success`
- exact mass-balanced shard preparation: `success`
- partition certificate audit: `success`
- prepared shard artifact preservation: `success`
- first shard wave: unchanged MATH-108 exact closure running
- observed shard failures: `0` at the latest inspection

Therefore `r=10` remains `OPEN`. It may be promoted only after the complete 128-shard gate succeeds.

## MATH-142 — `r=9` execution-readiness audit

Prepared but deliberately not launched while MATH-117 uses the Actions queue:

```text
classification                977 = 72 safe + 349 singleton + 556 critical
AP source cylinders           141,002
represented occurrence mass  172,107,496,438,700
max multiplicity              3,381,256,733,001
mass-balanced split pieces    141,021
128-shard cap                 1,344,589,815,928
shard mass range              1,344,589,815,927 .. 1,344,589,815,928
max pieces per shard          1,300
```

The unchanged MATH-114 representation is `u64`-safe shard-locally and compatible with the unchanged MATH-108 exact AP-union engine.

Records:

```text
collatz/notes/2026-09-15-math142-r9-execution-readiness-audit.md
.github/workflows/collatz-math142-r9-mass-balanced-sharded-closure.yml
```

This is an execution preflight only; `r=9` remains `OPEN`.

## Remaining proof obligations after layer closures

1. Finish `r=10`, then close `r=9,...,2`.
2. Audit one-paid/multi-paid coverage, including `r=0/1` semantics.
3. Audit the entire first universal cell implication chain.
4. Separately prove or re-audit the universal reduction from the frozen baseline plus first-cell closure to every positive integer.

## Claim boundary

The project continues to distinguish exact finite workload, exact finite safe subsets, exact finite layer closure, coverage of a proof partition, first-cell emptiness, universal reduction, and a full Collatz proof.
