# MATH-256 — conditional aggregation theorem for closing the r=10 paid layer

Date: 2026-09-19

Status: EXACT CONDITIONAL AGGREGATION / AWAITS L=13..44 SUPPORT CERTIFICATES

## 1. Bellman dichotomy

For a complete multi-paid boundary transfer with emitted r=10, MATH-186 gives

Delta B = epsilon_10 - lambda L + lambda(R-R')

and

Delta B <= 0 => R'=0.

Thus every transfer is either:

- Bellman-positive; or
- a singleton overshoot obligation.

## 2. Length range of every negative-capable r=10 transfer

MATH-202 gives for r=10

z=L-R >=13

whenever the transfer can be Bellman-dangerous.

Since R>=0,

L>=13.

MATH-058 proves every zero-cost prefix immediately preceding a paid cluster in the current first-cell scope satisfies

L<=72.

Therefore every negative-capable r=10 transfer begins from a paid-exit source anchor with

boxed: 13<=L<=72.

## 3. Paid-exit support is a conservative terminal superset

MATH-058R paid_exit_sources(L) enumerates every first-cell phase/address source anchor for which:

- the length-L zero-cost mechanical prefix is legal;
- the next actual shortcut parity is odd, so a paid cluster opens.

An r=10 dangerous transfer is a subset of these paid exits because it additionally requires a specific ten-paid first-return completion and a negative Bellman balance.

Therefore closing the entire paid-exit support at a given L is stronger than closing only the r=10-danger subset.

## 4. Forward-orbit terminal certificate

MATH-249 maps every paid-exit source anchor through its actual length-L mechanical prefix and opening paid odd step to an exact odd-step AP

Z=Z0+3^(q+1)j.

This is an actual forward segment of the same Collatz trajectory.

If every represented Z in that exact AP union reaches <=2^71, then every corresponding source anchor reaches the frozen floor as well.

Hence no such anchor can lie on a hypothetical minimal counterexample trajectory above the verified floor.

## 5. Aggregation theorem

Suppose exact terminal certificates establish, for every integer L with 13<=L<=72,

every MATH-058R paid-exit source anchor at length L reaches <=2^71.

Then every emitted-r=10 boundary transfer satisfies one of:

1. Delta B>0, so it is Bellman-safe; or
2. Delta B<=0, hence it is a singleton overshoot with 13<=L<=72, whose source anchor is terminally closed by the paid-exit support certificate.

Therefore, in the current first-universal-cell Bellman decomposition,

boxed: complete paid-exit shell closure for L=13..72 => the r=10 paid layer is CLOSED.

## 6. Current certified support

MATH-224 certifies L=54..72.
MATH-249 certifies L=53.
MATH-250 certifies L=45..52.

Hence the conditional theorem is currently missing only L=13..44.

MATH-251/253/254/255 are the exact support gates for those remaining lengths.

## 7. Architectural note

The theorem-facing argument is not an L-by-L proof architecture.

The structural theorem is the single safe-or-singleton dichotomy plus the bounded shell 13<=L<=72.

The per-L MATH-108 runs are finite terminal certificates for the bounded singleton shell, analogous to checking a finite list of terminal states after the common recurrence has reduced the problem to that list.

## Claim boundary

Do NOT mark r=10 CLOSED until every remaining L=13..44 terminal gate has a successful exact certificate and a dependency/coverage audit confirms no missing paid-exit source class.

First-cell emptiness and the Collatz conjecture remain OPEN.