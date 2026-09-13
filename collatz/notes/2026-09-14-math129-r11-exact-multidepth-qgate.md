# MATH-129 — r=11 exact multi-depth q-gate union

Status: `MAINLINE FINITE AUDIT / CURRENT STRONGEST q-GATE SAFE-MASS BOUND / r=11 OPEN`

Date: 2026-09-14

## Construction

MATH-125 gives, for every prefix depth `d` and odd count `q`, an exact source-maximum limit

```text
L(d,q) = floor((2^d*LO - c_max(d,q))/3^q),
LO=2^71,
```

such that every source `n<=L(d,q)` with that prefix odd count is at or below the frozen floor by depth `d`.

For one source residue `r mod 2^22`, let `q_d(r)` be the exact number of odd shortcut steps in its first `d` steps. Define

```text
N_*(r) = max_{1<=d<=22} L(d,q_d(r)).
```

Then a prepared AP piece with branch maximum `N` is MATH-125-safe on source residue `r` iff

```text
N <= N_*(r)
```

for at least one prefix depth `d<=22`.

Thus the union of all safe prefix gates through depth 22 is represented by one exact threshold per source residue. No safe subsets from different depths are added independently; their logical union is constructed first and counted once.

## Exact AP counting

For each odd-step AP `P(a,b,m)`, the map

```text
k -> a+bk mod 2^22
```

is an affine permutation over a complete period. MATH-129 counts the exact threshold-satisfying parameters over all complete cycles and the exact cyclic remainder interval.

The `275` distinct threshold values induced by all `(d,q)` pairs through depth 22 are compressed to integer ranks. For each of the 32 observed `b mod 2^22` classes, block suffix histograms answer exact cyclic threshold-count queries for every AP piece.

## Exact result

```text
prepared split pieces:              605,977
total source occurrence mass: 3,419,719,061,560
threshold levels:                       275
exact multi-depth safe mass:  3,209,065,424,947
exact uncertified tail mass:   210,653,636,613
safe source-mass fraction:          93.840030925905822%
```

The earlier adaptive complete-block method using depths through 34 beats this exact `d<=22` union on **zero** AP pieces:

```text
multi-depth exact union wins: 601,534 pieces
adaptive method wins:               0 pieces
ties:                           4,443 pieces
```

Therefore MATH-129 supersedes MATH-128 as the current theorem-facing q-gate pruning bound for r=11.

## Interpretation

The remaining `210,653,636,613` source occurrences are not counterexamples and are not asserted to survive the Collatz dynamics. They are exactly the part of the prepared r=11 representation not discharged by the MATH-125 correction envelope at any prefix depth through 22.

The natural next target is this high-odd-count/address-sensitive tail. It must be handled by deeper exact prefix gates, MATH-124 exact source-address formulas, or the unchanged MATH-108 exact AP-union engine.

## Claim boundary

This is an exact finite source-residue audit, not a density argument. It does not close r=11 while the tail is nonzero. The certified multi-paid frontier remains `r>=12 CLOSED` until MATH-116 or an equivalent complete exact certificate closes r=11.
