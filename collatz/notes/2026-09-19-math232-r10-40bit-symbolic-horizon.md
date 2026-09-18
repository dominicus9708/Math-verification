# MATH-232 — 40-bit symbolic horizon before r=10 output singletonization

Date: 2026-09-19

Status: EXACT WELL-FOUNDED SYMBOLIC HORIZON / MULTI-SOURCE SAFE PREFIX <=40 BITS / r=10 OPEN

## 1. Starting resolution

MATH-225 proves every frozen r=10 output family has

R_0 = ceil(log2 M_0) <= 40.

## 2. Exact factor composition

Append any exact future factor of dyadic source depth h.

If the compatible child remains multi-source, MATH-074/MATH-228 give

h <= R

and

R' <= R-h.

Therefore every future factor that preserves symbolic multiplicity consumes at least its entire dyadic depth from the remaining resolution budget.

## 3. Total multi-source horizon

For a sequence of future factors that all leave M>=2,

h_1 + h_2 + ... + h_n
<= R_0 - R_n
<= R_0
<= 40.

Hence

boxed: after a frozen r=10 output, no nonempty continuation can remain multi-source for more than 40 additional dyadic shortcut bits.

The first factor with h>R is an overshoot handoff and has at most one compatible ordinary source.

## 4. Relation to Bellman danger

Every factor with h<=R is automatically Bellman-safe under the resolution potential, independently of its local paid penalty.

Therefore the symbolic multi-source part of the r=10 continuation is both:

- Bellman-safe, and
- well-founded with a <=40-bit address horizon.

Any first locally negative transfer is necessarily an overshoot and therefore enters the singleton regime immediately.

## 5. State-size consequence

MATH-228 shows that this entire multi-source horizon needs at most 129 bits of normalized address precision.

MATH-229 shows that when the first negative low-paid edge is reached, each contracted state has at most 54 raw mechanical selector candidates.

Thus the remaining executor has the exact form

boxed:
<=40 symbolic address bits
 -> singleton handoff
 -> deterministic same-integer tail / terminal test.

This is a finite-horizon symbolic problem, not an unbounded AP-depth problem.

## Claim boundary

Established:
- <=40 total future dyadic bits while the r=10 output remains multi-source;
- all such multi-source refinements are Bellman-safe;
- first negative transfer singletonizes;
- finite 129-bit address sufficiency throughout.

Not established:
- a small bound on the number of distinct <=40-bit symbolic states;
- closure of every singleton tail after handoff;
- full r=10 closure;
- the Collatz conjecture.