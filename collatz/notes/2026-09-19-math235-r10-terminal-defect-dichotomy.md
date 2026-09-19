# MATH-235 — terminal-defect dichotomy for the frozen r=10 full factors

Date: 2026-09-19

Status: EXACT FACTOR-LEVEL CLOSURE / CONTRACTING-COEFFICIENT BRANCH CLOSED / r=10 OPEN

## 1. Synchronized factor

For every MATH-206 frozen negative-candidate full factor

N(s)=A+2^H s,
Y(s)=B+3^Q s,
0<=s<M,

define

C=2^H B-3^Q A

and

J(s)=C-N(s)(2^H-3^Q)=2^H(Y(s)-N(s)).

Thus J<0 is exact strict self-descent of the same ordinary source.

## 2. Exact threshold audit

The 278,725 frozen r=10 factor records split by coefficient sign as

- 2^H>3^Q: 183,189 records;
- 2^H=3^Q: 0 records;
- 2^H<3^Q: 95,536 records.

For every one of the 183,189 coefficient-contracting records, the minimum source already satisfies J<0.

Since J(s) strictly decreases in s when 2^H>3^Q, every source in every such cylinder self-descends.

Hence

boxed: 183,189 / 183,189 contracting-coefficient r=10 factors are CLOSED by J.

There are no partially surviving contracting cylinders.

Conversely, every coefficient-expanding record is unchanged by this self-descent cut.

Thus the frozen r=10 factor language has an exact all-or-nothing terminal-defect dichotomy at this stage.

## 3. Mass reduction

Original represented occurrence mass:

27,557,263,803,397.

Removed exactly by J<0:

21,000,159,682,978.

Remaining coefficient-expanding mass:

6,557,104,120,419.

The maximum surviving multiplicity is

166,975,641,136,

so the maximum surviving source-resolution height is

boxed: R_max=38.

This improves the pre-J r=10 ceiling R<=40.

## 4. Structural meaning

By the complete-boundary telescope

3^Q/2^H = omega/omega'.

Therefore the closed branch 2^H>3^Q is exactly the branch with coefficient ratio <1, equivalently omega<omega'.

The only frozen r=10 factors that still require future continuation are coefficient-expanding:

boxed: 3^Q/2^H>1.

This is a phase/coefficient restriction, not an AP-shard label.

## 5. Relation to MATH-182/183

MATH-182/183 predicted that when rho=2^H/3^Q>1, the non-descending members form one initial source prefix and can be cut by one exact threshold.

For the frozen r=10 factors the result is stronger:

that bad prefix is empty for every rho>1 record.

So no repeated midpoint contraction is needed on the coefficient-contracting half of the factor language.

## Claim boundary

Established:
- exact J-threshold audit of every frozen r=10 full factor;
- complete closure of all coefficient-contracting frozen r=10 factors;
- survivor mass 6,557,104,120,419;
- survivor resolution ceiling R<=38.

Not established:
- a symbolic theorem that every regenerated coefficient-contracting r=10 factor also has empty bad prefix;
- closure of the coefficient-expanding continuation;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.