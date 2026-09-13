# MATH-128 — r=11 piecewise hybrid q-gate certificate selection

Status: `EXACT FINITE AUDIT / SUPERSEDED AS FRONTIER SAFE-MASS BOUND BY MATH-129 / r=11 OPEN`

Date: 2026-09-14

## Purpose

Two exact but different one-sided certificates were available for each prepared r=11 AP piece:

1. an adaptive complete-block MATH-125 certificate using the best depth `1<=d<=34` for that piece, but assigning zero credit to incomplete blocks;
2. the MATH-127 exact remainder-aware common-depth `d=22` certificate.

The safe subsets from these two methods need not be nested, so their masses must not be added. MATH-128 instead chooses, independently for each AP piece, the certificate that proves the larger safe subset count.

## Exact result

```text
prepared pieces:                    605,977
total occurrence mass:        3,419,719,061,560
adaptive complete-block safe: 2,971,304,357,696
exact d=22 safe:              2,904,383,883,175
piecewise-max safe:           2,987,225,373,882
piecewise tail:                 432,493,687,678
safe fraction:                    87.352946838834583%
```

Certificate selection by AP piece:

```text
adaptive wins:   7,512 pieces
d=22 wins:     585,683 pieces
ties:           12,782 pieces
```

Because exactly one certificate is selected for each AP piece, this is a legitimate exact lower bound and contains no cross-method double counting.

## Supersession

MATH-129 constructs the exact union of MATH-125 prefix gates for all `1<=d<=22` at the source-residue level and yields a strictly stronger safe-mass bound. Therefore MATH-128 remains a valid audit record but is not the current frontier pruning bound.

## Claim boundary

The percentage is source occurrence mass in the exact MATH-116 representation. It is not natural density, not necessarily a unique-integer percentage, and cannot close r=11 while the exact tail is nonempty.
