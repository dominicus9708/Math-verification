# MATH-200 — future-address overpartition audit and Hensel future-dominance

Date: 2026-09-18

Status: `EXACT STRUCTURAL CORRECTION / FINITE ADDRESS-PRECISION AUDIT / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-197/198 showed that terminal risk at fixed `(k,q)` is ordered by

[
N	ext{ smaller},qquad C	ext{ larger}.
]

MATH-199 then found very small **terminal-only** Pareto record sets.

The next question is whether those records can also be merged in a future-complete executor by the MATH-096 finite address key

[
Xmod 2^{73+R},qquad G=3^{-q}mod 2^{73+R}.
]

This note audits that idea and separates two distinct notions:

1. terminal Pareto dominance;
2. future-complete equal-endpoint/Hensel dominance.

## 2. Singleton future key

For singleton states, `R=0`, so MATH-096 requires at most

[
oxed{Xmod2^{73},qquad Gmod2^{73}.}
]

At fixed `q`, `G` is common. The partition is therefore driven by `X mod 2^73`.

For a terminal singleton with ordinary start `N`, correction `C`, depth `k`, and odd count `q`,

[
Y=T^k(N)=rac{3^qN+C}{2^k},
]

and

[
oxed{Xequiv 3^{-q}Ypmod{2^{73}}.}
]

## 3. Exact finite audit of the MATH-199 records

For the exact terminal Pareto records from MATH-199:

| depth | Pareto records | distinct `X mod 2^73` classes |
|---:|---:|---:|
| 28 | 120 | 120 |
| 29 | 122 | 122 |
| 30 | 141 | 141 |

Thus the full sufficient MATH-096 future key merges **none** of the terminal Pareto records in these levels.

This is a useful negative result:

[
oxed{	ext{terminal Pareto compression }
otRightarrow	ext{ future-key compression}.}
]

## 4. Low-bit precision audit

The separation occurs much earlier than 73 bits.

The minimum number of low `X` bits that already distinguishes every terminal Pareto record inside each fixed-`q` slice is

| depth | minimum distinguishing bits |
|---:|---:|
| 28 | 13 |
| 29 | 12 |
| 30 | 11 |

For `k=30`, the total number of classes as the retained precision increases is

| bits | classes |
|---:|---:|
| 1 | 23 |
| 2 | 42 |
| 3 | 73 |
| 4 | 97 |
| 5 | 116 |
| 6 | 125 |
| 7 | 132 |
| 8 | 137 |
| 9 | 139 |
| 10 | 140 |
| 11 | 141 |

Therefore the absence of compression is not merely an artifact of storing all 73 sufficient bits.

## 5. Correct role of ordinary Pareto dominance

MATH-198 proves that the risk order is preserved on a **common next branch**.

That is not enough to delete a state for all future time when two states later take different parity/address branches.

Therefore ordinary Pareto dominance is safe for

- terminal extremal tests;
- branch-local pruning when future equivalence is separately certified;

but it is not by itself a future-complete quotient.

This is the DSD correction required by the present audit.

## 6. Equal endpoint gives true future equivalence

Suppose two same-depth states have the same ordinary endpoint `Y`:

[
3^qN_1+C_1
=
3^qN_2+C_2
=
2^kY.
]

Then after depth `k` they are literally at the same integer.

Hence their complete future shortcut trajectory, parity sequence, phase decisions, and every later address decision are identical.

Thus equal endpoint is an exact future-equivalence relation.

## 7. Positive Hensel credit is future-complete dominance

MATH-189 gives positive Hensel translation credit `t>0` as

[
C_*=C+t3^q,
qquad
N_*=N-t.
]

Then

[
3^qN_*+C_*=3^qN+C,
]

so the endpoint is exactly unchanged.

Therefore

[
oxed{	ext{positive Hensel credit }Rightarrow	ext{ equal endpoint + smaller ordinary start}.}
]

The smaller start is the harder representative for minimal-counterexample descent: if the common future ever falls below the smaller start, it also falls below every larger start in that endpoint fiber.

Hence Hensel domination is a genuine **future-complete dominance**, not merely a terminal ordering.

## 8. Revised compression hierarchy

The safe executor order is therefore

[
oxed{
	ext{exact endpoint/future-equivalence}
	o
	ext{Hensel dominance}
	o
	ext{future-equivalent merge}
	o
	ext{terminal Pareto extremum when needed}.
}
]

Do not use terminal Pareto records as a future quotient unless equal-future information is separately present.

## 9. Consequence for the mainline

The MATH-199 terminal record collapse remains useful for terminal first-crossing extremal calculations.

However, the future-complete transfer program should now use **equal-endpoint Hensel fibers** as its primary exact quotient.

This reconnects the modern correction-coordinate program to the older verified endpoint-merge dominance lemma.

The remaining quantitative problem is how many endpoint-minimal/Hensel-maximal fibers remain after the exact address and first-cell constraints are imposed.

## 10. Claim boundary

Established:

- exact singleton MATH-096 future-key audit at depths 28--30;
- no full-key collisions among MATH-199 terminal Pareto records in those depths;
- exact low-bit separation counts;
- terminal Pareto dominance is not promoted to unrestricted future dominance;
- equal endpoint is exact future equivalence;
- positive Hensel credit is exact future-complete dominance toward the smaller start.

Not established:

- a small global endpoint quotient;
- a depth-41 or arbitrary-depth future-complete frontier bound;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
