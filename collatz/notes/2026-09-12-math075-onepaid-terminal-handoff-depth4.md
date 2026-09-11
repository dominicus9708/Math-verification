# MATH-075 — exact one-paid terminal handoff audit through macro depth 4

Date: 2026-09-12

Status: `FINITE EXACT / DEPTH-4 TERMINAL HANDOFFS CLOSED / DEEPER SYMBOLIC QUOTIENT OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note extends MATH-061's exact one-paid composition catalogue to macro depth 4.
- MATH-074 is used conceptually: multi-source symbolic edges are not the Bellman bottleneck; singleton-producing terminal handoffs are audited directly.

## 1. Initial one-paid catalogue

MATH-061 supplies exactly

\[
910
\]

one-paid macro cylinders.

Of these, 53 are already singleton source cylinders. The remaining

\[
\boxed{857}
\]

are symbolic multi-source states with accumulated resolution below the 73-bit handoff.

## 2. Exact recursive composition

The unchanged MATH-061 composition law is used.

At each depth:

1. intersect the exact current endpoint phase interval with the next macro source phase interval;
2. solve the exact dyadic congruence for the next parameter residue;
3. update source and target affine anchors;
4. retain the child symbolically only if source multiplicity remains greater than one;
5. if multiplicity becomes one, continue the resulting ordinary target integer directly under the shortcut Collatz map.

No density, random-parity, or average-drift assumption is used.

## 3. Exact counts

The new terminal and surviving symbolic counts are

| macro depth | new singleton handoffs | multi-source survivors |
|---:|---:|---:|
| 2 | 1,137 | 11,389 |
| 3 | 11,511 | 85,803 |
| 4 | 76,585 | 442,957 |

The depth-2 value is consistent with MATH-061's 1,141 singleton ordered pairs after removing cases whose first macro was already singleton and therefore should have been handed off earlier in the resolution-first recursion.

## 4. Same-integer terminal audit

After deduplicating identical ordinary target integers, the terminal sets are

| macro depth | singleton occurrences | unique ordinary targets | maximum additional shortcut descent |
|---:|---:|---:|---:|
| 2 | 1,137 | 576 | 71 |
| 3 | 11,511 | 6,562 | 202 |
| 4 | 76,585 | 46,845 | 185 |

Every audited unique target reaches

\[
\le2^{71}.
\]

There are zero terminal failures in these finite sets.

## 5. Why brute composition stops here

The number of exact symbolic multi-source representations grows

\[
857\to11,389\to85,803\to442,957.
\]

A naive fifth composition therefore repeats the representation-growth problem already seen in MATH-070.

This is not evidence of a mathematical obstruction. It is evidence that the state description must be compressed before deeper composition.

The relevant state has already been factored by MATH-072--074 into

\[
\boxed{
\text{analytic phase/penalty}
\times
\text{dyadic compatibility}
\times
\text{Hensel dominance}
\times
\text{resolution height}.
}
\]

For the one-paid catalogue, exact future compatibility requires the dyadic endpoint address information; MATH-051 bounded-carry states may assist Hensel-dominance pruning but do not replace that address coordinate.

## 6. Updated next target

Do not continue depth 5 by raw Cartesian composition.

Instead:

1. quotient states by identical future dyadic compatibility data;
2. union exact overlapping phase intervals inside each compatibility class;
3. retain sufficient affine information to reconstruct a terminal singleton target exactly;
4. use MATH-074 to ignore local reduced-cost negativity while a state remains multi-source;
5. immediately audit every generated singleton handoff by same-integer descent;
6. attach bounded-carry dominance only where it provably removes future-equivalent address states.

The symbolic one-paid horizon is finite because each macro has shortcut length at least 3 and the source resolution handoff occurs by 73 accumulated bits. Hence no more than 24 one-paid macros can remain symbolic before singleton resolution. This finite-horizon statement does not imply those terminal singletons all descend; terminal closure still requires exact audit.

## Reproducibility

`collatz/src/2026_09_12_math075_onepaid_terminal_handoff_depth4.py`
