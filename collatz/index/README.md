# Collatz proof-tree index

This directory is the classification layer for the existing `collatz/` archive.

It does **not** move, delete, or rewrite historical `notes/`, `src/`, `results/`, or `wolfram/` files. The original files remain the reproducibility record; this index records their current role in the proof program.

## Current status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Proof architecture: `PARTIALLY_CONFIRMED`
- Published finite-verification baseline: `B_pub = 2^71`
- Current detailed one-paid frontier: `7 <= t <= 9`
- Natural next order: `t=9 -> t=8 -> t=7`

Current first universal-cell window:

```text
(A0,q0) = (114208327604, 72057431991)
2^71 < N < 1364*2^61
address labels a = 1024,...,1363 (340 blocks)
```

## Classification files

- [`proof-tree.md`](proof-tree.md) — dated mainline and exact barrier/pivot nodes.
- [`side-branches.md`](side-branches.md) — supporting, historical, alternate, and acceleration branches.
- [`retired-and-superseded.md`](retired-and-superseded.md) — strategies/quotients/independent filters that are no longer used, with reasons.
- [`reproducibility-index.md`](reproducibility-index.md) — proof-facing claims mapped to notes, certificates, and result files.

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

No finite certificate in this directory is promoted to a universal Collatz proof. In particular, closing all currently open one-paid macro depths would still require separate treatment of the remaining paid-count layers and the full first-cell implication chain.
