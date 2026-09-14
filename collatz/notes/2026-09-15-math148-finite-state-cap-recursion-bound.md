# MATH-148 — finite `STATE_CAP` recursion bound for remaining paid layers

Date: 2026-09-15

## Status

`SUPPORT / EXACT ENGINE-RESOURCE LEMMA / NO NEW LAYER CLOSURE CLAIM`

## Setup

MATH-108 uses `STATE_CAP = 1,000,000`. MATH-114 splits each layer into exact consecutive AP parameter intervals, and every split-piece multiplicity is at most that layer's mass-balanced cap.

MATH-144 established that for an isolated AP source partition of occurrence mass `M`, the current exact lineage-record count cannot exceed `M`: each source occurrence has at most one current deterministic image at a shortcut depth, while merging and singleton deduplication only reduce the record count.

When `TooBig` occurs on a single AP, MATH-108 exactly halves the AP parameter interval and recursively audits the two halves. After `k` such exact halvings, every descendant source piece has mass at most

```text
ceil(M / 2^k).
```

Therefore it is sufficient to choose the least `k` such that

```text
ceil(cap_r / 2^k) <= 1,000,000.
```

## Exact bounds

```text
layer  cap_r                k   max descendant mass
r12          4,534,939,598  13        553,582
r11         26,716,555,169  15        815,325
r10        215,291,123,465  18        821,271
r9       1,344,589,815,928  21        641,151
r8      10,008,021,759,883  24        596,525
r7      66,399,002,550,056  26        989,423
r6     416,023,898,569,210  29        774,905
r5   3,183,370,901,768,032  32        741,187
r4  14,416,641,320,007,807  34        839,159
r3 102,294,036,332,826,744  37        744,288
r2 580,341,421,448,851,123  40        527,818
```

Result table:

`collatz/results/2026-09-15-math148-state-cap-bisection-depth.tsv`

## Interpretation

For every audited remaining layer `r=2..12`, a pure `STATE_CAP` obstruction on an isolated split AP is finitely eliminable by exact parameter bisection. Even the largest `r=2` split piece requires at most 40 exact half-interval bisections before its descendant mass is below `STATE_CAP`.

For a shard containing multiple source records, MATH-108 can first recursively split the source-record list. Since each shard has finitely many source pieces, repeated source-list splitting eventually isolates source AP pieces; the bound above then applies to each isolated AP.

Thus a long-running shard must not be interpreted as evidence of an infinite state-count obstruction merely because of the raw represented occurrence mass.

## Claim boundary

This result does **not** prove that a layer closes. In particular it does not prove that an exact trajectory empties before `MAX_DEPTH = 1000`.

The remaining theorem-facing possibilities are cleanly separated:

1. finite source/state scheduling — controlled by MATH-108/MATH-114/MATH-148;
2. exact dynamical closure within the audited depth gate — still requires the actual AP-union execution;
3. paid-layer coverage and first-cell/universal implication — separate later obligations.
