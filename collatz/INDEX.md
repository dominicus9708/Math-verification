# Collatz classified index

The historical `collatz/README.md` and all existing notes/certificates remain untouched.

Use the current classification layer here:

- [`index/README.md`](index/README.md) — current status and classification policy
- [`index/current-frontier.md`](index/current-frontier.md) — authoritative compact frontier
- [`index/proof-tree.md`](index/proof-tree.md) — dated mainline proof tree
- [`index/side-branches.md`](index/side-branches.md) — side/support/historical branches
- [`index/retired-and-superseded.md`](index/retired-and-superseded.md) — retired, saturated, redundant, insufficient, and superseded routes
- [`index/reproducibility-index.md`](index/reproducibility-index.md) — certificate/source/result map
- [`index/2026-09-14-math121-129-r11-closeout.md`](index/2026-09-14-math121-129-r11-closeout.md) — MATH-121..129 structural closeout snapshot

## Current exact frontier

```text
one-paid detailed band t=7..16   CLOSED on audited exact Bellman/address criterion
multi-paid r>=12                 CLOSED
multi-paid r=11                  OPEN — MATH-116 exact closure incomplete
multi-paid r=10                  OPEN — MATH-117 execution-ready, not launched
multi-paid 2<=r<=9               OPEN
first universal Farey cell       OPEN
Collatz conjecture                OPEN
```

MATH-111 closed `r=12` with 128 successful exact AP-union shard jobs.

MATH-116 is the current full exact `r=11` closure gate. Its preparation certificate succeeds and multiple shards have completed successfully, but later shards remain runner-queued, so `r=11` is not promoted.

MATH-121..125 isolate layer-independent structure for the lower frontier:

- MATH-121: scalar normalized margin alone is not a sufficient well-founded rank;
- MATH-122/123: exact non-singleton AP resolution ranks, strengthened to lexicographic `(W,m)` with `W=(N+1)m`;
- MATH-124: direct parity-word to AP source-parameter residue theorem;
- MATH-125: sharp correction envelope and exact odd-count floor-safe gate.

MATH-129 is the current strongest theorem-facing `r=11` pruning certificate. On the exact MATH-116 prepared source it certifies

```text
safe source occurrence mass   3,209,065,424,947
uncertified tail mass            210,653,636,613
safe fraction                         93.840030925905822%
```

through the exact logical union of all MATH-125 prefix gates for depths `1..22`.

This is an exact finite safe subset, not a density argument and not an `r=11 CLOSED` claim.

Authoritative MATH-129 artifacts:

```text
collatz/src/2026_09_14_math129_r11_multidepth_qgate_audit.cpp
collatz/results/2026-09-14-math129-r11-multidepth-qgate.tsv
collatz/notes/2026-09-14-math129-r11-exact-multidepth-qgate.md
```

The next mathematical target is the exact `210,653,636,613`-occurrence `r=11` tail, or completion of MATH-116. After the remaining multi-paid layers close, separate paid-layer coverage, first-cell implication-chain, and universal-reduction audits remain mandatory.