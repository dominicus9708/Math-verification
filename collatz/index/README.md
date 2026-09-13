# Collatz proof-tree index

This directory is the classification layer for the existing `collatz/` archive.

It does **not** move, delete, or rewrite historical `notes/`, `src/`, `results/`, or `wolfram/` files. The original files remain the reproducibility record; this index records their current role in the proof program.

## Current status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Proof architecture: `PARTIALLY_CONFIRMED`
- Published finite-verification baseline: `B_pub = 2^71`
- One-paid detailed band `7 <= t <= 16`: `CLOSED` on the audited exact Bellman/address criterion
- Multi-paid frontier: `r >= 12 CLOSED`; `r=11 OPEN`; `2 <= r <= 10 OPEN`
- MATH-111: exact `r=12` closure from 128 successful exact AP-union shards
- MATH-116: current full exact `r=11` closure workflow; preparation passed, several shards succeeded, later shards remain queued
- MATH-129: current strongest finite theorem-facing `r=11` q-gate pruning bound

Current first universal-cell window:

```text
(A0,q0) = (114208327604, 72057431991)
2^71 < N < 1364*2^61
address labels a = 1024,...,1363 (340 blocks)
```

## Current r=11 structural result

MATH-121..125 separate the current lower-layer mechanism into exact components:

```text
normalized floor-margin barrier
-> non-singleton AP resolution rank
-> direct parity-word/AP address
-> sharp correction envelope
-> exact q-safe prefix gates
```

MATH-129 takes the logical union of all safe MATH-125 prefix gates through depth 22 on the exact MATH-116 prepared source:

```text
prepared pieces                     605,977
total source occurrence mass        3,419,719,061,560
exact safe mass                     3,209,065,424,947
exact uncertified tail              210,653,636,613
safe fraction                       93.840030925905822%
```

This is an exact finite subset certificate. It is not an `almost all => all` argument and does not close `r=11` while the tail is nonzero.

See [`2026-09-14-math121-129-r11-closeout.md`](2026-09-14-math121-129-r11-closeout.md) for the current structural closeout.

## Classification files

- [`proof-tree.md`](proof-tree.md) — dated mainline and exact barrier/pivot nodes.
- [`side-branches.md`](side-branches.md) — supporting, historical, alternate, and acceleration branches.
- [`retired-and-superseded.md`](retired-and-superseded.md) — strategies/quotients/independent filters that are no longer used, with reasons.
- [`reproducibility-index.md`](reproducibility-index.md) — proof-facing claims mapped to notes, certificates, and result files.
- [`current-frontier.md`](current-frontier.md) — authoritative compact frontier and remaining proof obligations.

## Status vocabulary

- `MAINLINE`: current proof route directly depends on the result.
- `SIDE / SUPPORT`: useful support, diagnostic, alternate representation, or acceleration; not a binding dependency of the current end state.
- `BARRIER / NEGATIVE RESULT`: exact result showing that a strategy or quotient is insufficient. These are preserved as proof pivots, not treated as failed mathematics.
- `REDUNDANT`: exact information is already carried by another condition, so it must not be counted as an independent filter.
- `SUPERSEDED`: a stronger later result replaced it as the active input.
- `RETIRED`: a strategy or implementation is no longer used.
- `HISTORICAL`: retained for traceability; no stronger status is assigned without a verified reason.

`RETIRED` or `SUPERSEDED` does not mean that the underlying theorem is false. The object being retired must be identified: theorem, strategy, quotient, state representation, bound, or implementation.

## Source-of-truth policy

GitHub remains authoritative for exact calculations, certificates, outputs, and history. Notion is the narrative/dependency index. A classification change never deletes the raw record.

## Claim boundary

The current finite frontier is

```text
one-paid detailed band t=7..16: closed on audited Bellman/address criterion
multi-paid r>=12: closed
multi-paid r=11: open
multi-paid 2<=r<=10: open
first universal Farey cell: open
Collatz conjecture: open
```

The next obligations are to discharge the exact r=11 tail or complete MATH-116, descend through `r=10..2`, audit paid-layer coverage, and only then audit the complete first-cell implication chain and the separate universal reduction from first-cell closure to the full Collatz statement.