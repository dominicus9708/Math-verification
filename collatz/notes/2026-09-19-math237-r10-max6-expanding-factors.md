# MATH-237 — at most six consecutive coefficient-expanding complete factors before singletonization

Date: 2026-09-19

Status: EXACT FINITE PHASE-CLOCK BOUND / POST-J r=10 SURVIVOR / r=10 OPEN

## 1. Starting point

MATH-235 leaves only coefficient-expanding frozen r=10 factors.

MATH-236 proves that while the post-r10 continuation remains multi-source, its cumulative future odd count satisfies

Q_fut <= 24.

Every complete boundary factor has positive odd count q>=1 and exact coefficient ratio

c_q = 3^q / 2^h

with 1/2 < c_q < 2.

## 2. Minimum expansion at fixed odd count

If one complete factor is coefficient-expanding, c_q>1.

For fixed q, the smallest possible expanding ratio is obtained at

h=floor(log2(3^q)),

so

e_q = 3^q / 2^floor(log2(3^q)).

Every expanding factor with odd count q has coefficient ratio at least e_q.

## 3. Phase telescope constraint

For any consecutive complete-boundary subchain, MATH-207 gives

product c_i = omega_start / omega_end.

Since both boundary phases lie in (1/2,1],

boxed: product c_i < 2.

Thus a run of expanding factors must have a product strictly below 2.

## 4. Exact finite optimization under Q_fut<=24

Minimize the product of expanding ratios for n factors subject to

q_1+...+q_n <=24,  q_i>=1.

Exact rational dynamic programming gives:

- n=5 minimum: 3^20 / 2^31 = 3486784401/2147483648 <2;
- n=6 minimum: 3^22 / 2^34 = 31381059609/17179869184 <2;
- n=7 minimum: 3^24 / 2^37 = 282429536481/137438953472 >2.

A minimizing 7-factor odd-count pattern is

(2,2,2,2,2,2,12).

Therefore seven consecutive coefficient-expanding complete factors are impossible while the continuation remains multi-source.

boxed: at most six consecutive expanding complete factors.

## 5. Consequence

Starting from a MATH-235 coefficient-expanding r=10 survivor, before the seventh future complete factor one of the following must happen:

1. source resolution is exhausted and the path becomes singleton; or
2. a coefficient-contracting complete factor occurs.

This conclusion allows arbitrary mixtures of paid tags. It depends only on total odd count and complete-boundary phase telescoping.

## 6. Role in the executor

MATH-234 now applies the exact J/master-defect threshold after every synchronized parity refinement.

A coefficient-contracting composed prefix is therefore immediately eligible for a monotone J suffix cut.

MATH-237 guarantees that the multi-source executor cannot avoid such a contracting opportunity for more than six complete factors unless it singletonizes first.

## Claim boundary

Established:
- exact 6-factor maximum for consecutive coefficient expansion under Q_fut<=24;
- by factor 7, contraction or singletonization is forced.

Not established:
- every contracting future factor closes its entire cylinder;
- every singleton tail closes;
- full r=10 closure;
- the Collatz conjecture.