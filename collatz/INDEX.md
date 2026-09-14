# Collatz classified index

The historical `collatz/README.md` and all existing notes/certificates remain untouched.

Use the current classification layer here:

- [`index/README.md`](index/README.md) — current status and classification policy
- [`index/current-frontier.md`](index/current-frontier.md) — authoritative compact frontier
- [`index/proof-tree.md`](index/proof-tree.md) — dated mainline proof tree
- [`index/side-branches.md`](index/side-branches.md) — side/support/historical branches
- [`index/retired-and-superseded.md`](index/retired-and-superseded.md) — retired, saturated, redundant, insufficient, and superseded routes
- [`index/reproducibility-index.md`](index/reproducibility-index.md) — certificate/source/result map
- [`index/2026-09-14-math121-129-r11-closeout.md`](index/2026-09-14-math121-129-r11-closeout.md) — q-gate structural snapshot

## Current exact frontier

```text
one-paid detailed band t=7..16   CLOSED on audited exact Bellman/address criterion
multi-paid r>=11                 CLOSED
multi-paid r=10                  OPEN — MATH-117 execution-ready, not launched
multi-paid 2<=r<=9               OPEN
first universal Farey cell       OPEN
Collatz conjecture                OPEN
```

MATH-111 closed `r=12`; MATH-116 has now closed `r=11`.

## MATH-116 final `r=11` closure

The exact MATH-116 source contains `605,972` AP records, `605,977` prepared split pieces, and occurrence mass `3,419,719,061,560`.

The mass-balanced partition certificate divides it into exactly 128 `u64`-safe shards. Workflow run `34768752143` is `completed / success`. The workflow requires matrix shards `0..127`, and every shard must run the unchanged MATH-108 generalized exact AP-union engine and match `PASS generalized exact AP-union audit`.

Therefore, within the audited multi-paid framework:

```text
r >= 11 CLOSED
```

Authoritative final records:

```text
collatz/results/2026-09-15-math116-r11-final-closure.tsv
collatz/notes/2026-09-15-math116-r11-final-closure.md
```

## q-gate/address work — support status

MATH-121..139 remain valid exact structural/support results. They established AP-resolution ranks, exact parity-word addresses, sharp correction envelopes, and deep exact finite safe subsets. MATH-139 reached:

```text
D=39 exact new safe mass  1,741,505,726
cumulative q-gate safe    3,350,963,514,708
q-gate tail                  68,755,546,852
safe fraction                 97.98943873416796%
```

That tail is not a surviving `r=11` family: MATH-116 independently closes the full exact source. Further q-gate deepening is therefore support/algorithmic work, not a prerequisite for the `r=11` theorem-facing layer closure.

## Next layer

MATH-117 is the complete exact `r=10` gate. Frozen preflight:

```text
classification                994 = 91 safe + 396 singleton + 507 critical
AP source cylinders           278,725
represented occurrence mass  27,557,263,803,397
max unsplit multiplicity      830,483,089,363
mass-balanced pieces          278,739
128-shard cap                 215,291,123,465
```

The workflow is manual-only and remains unlaunched. `r=10` is therefore still `OPEN`.

After the remaining multi-paid layers close, separate paid-layer coverage, first-cell implication-chain, and universal-reduction audits remain mandatory.
