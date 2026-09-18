# MATH-229 — exact safe-prefix contraction and first-danger normal form

Date: 2026-09-19

Status: EXACT FUTURE-COMPLETE TRANSDUCER LEMMA / SAFE*·DANGER NORMAL FORM / r=10 OPEN

## 1. Composed cylinder state

Use one exact composed boundary cylinder

Y0 = A + 2^H s,
Y  = B + 3^Q s,
0 <= s < M.

Let the original source phase Omega0 lie in an exact rational interval I.

Carry two exact scalar transport coefficients:

Omega_current = g Omega0,
P_total = beta Omega0.

Let

R=ceil(log2 M), with R=0 for M=1.

The address channel is the MATH-228 finite state

(X,G) mod 2^(89+R).

## 2. Exact composition of one next factor

Let the next legal low-paid factor be

A_e + 2^h t -> B_e + 3^q t,

with source phase interval I_e, phase multiplier g_e, and local penalty

P_e = beta_e Omega_current.

Exact source compatibility selects

r = (A_e-B) (3^Q)^(-1) mod 2^h.

If r>=M, the edge is empty.

Otherwise write s=r+2^h u.

Then

A' = A + 2^H r,
H' = H+h,
Q' = Q+q,
M' = 1 + floor((M-1-r)/2^h),

u0 = (B + 3^Q r - A_e)/2^h,
B' = B_e + 3^q u0.

Hence

Y0 = A' + 2^(H+h) u,
Y' = B' + 3^(Q+q) u.

The representation is closed under arbitrary low-paid composition.

Phase compatibility pulls back to

I' = I intersect g^(-1) I_e.

If I' is empty, the edge is empty.

Otherwise

g' = g g_e,
beta' = beta + g beta_e.

These are exactly the MATH-061 composition laws, now stated for every remaining low-paid factor rather than only one-paid factors.

## 3. Adjusted Bellman reserve

Let lambda=19/503 and define the exact phase-dependent reserve

boxed: V(Omega0) = beta Omega0 - lambda(H-89) - lambda R.

The constant 89 is the MATH-060 first-cell overhead.

After one factor,

V'(Omega0)-V(Omega0)
= g beta_e Omega0 - lambda h + lambda(R-R').

This is the exact macro form of the MATH-197 resolution-adjusted Bellman increment.

Call an edge SAFE on its exact phase cell when the infimum of this expression over I' is nonnegative.

Because all penalty coefficients are nonnegative and I' has rational endpoints, this infimum is an exact rational endpoint calculation.

## 4. Safe-prefix contraction

Consider any finite path whose first n factors are SAFE.

Repeated exact composition gives one cylinder state of the same form, and the reserve satisfies

inf V_n >= inf V_0.

Therefore the internal SAFE history is irrelevant to the proof-facing Bellman debt once the composed state

(A,B,H,Q,M,I,g,beta,X,G)

is retained.

In symbols:

SAFE · SAFE · ... · SAFE

contracts to one future-complete composed state without losing address, phase, multiplicity, penalty, or synchronized correction information.

## 5. First-danger normal form

Every path not already closed can therefore be cut at its first non-SAFE low-paid factor:

boxed: SAFE* · DANGER.

All preceding history is represented by the single contracted state immediately before DANGER.

Suppose DANGER emits paid count r in {2,...,10}.

MATH-202 gives the necessary overshoot

z >= z_min(r).

If the current source resolution is R, the zero-cost prefix of the dangerous factor has length

L = R+z >= R+z_min(r).

Let

L_star = R+z_min(r).

Every dangerous factor therefore begins with a length-L_star zero-cost mechanical prefix.

## 6. Uniform first-danger selector bound

At length L_star, the exact mechanical language is constant on at most L_star+1 phase cells.

Each compatible mechanical word fixes one canonical source residue modulo 2^L_star.

Since

M <= 2^R < 2^(R+z_min(r)) = 2^L_star,

each word selects at most one ordinary source parameter s.

After the frozen r=10 layer, MATH-225 gives R<=40, while

max_{2<=r<=10} z_min(r)=13.

Hence

L_star <= 53

and

boxed: every contracted state has at most 54 ordinary candidates for its first dangerous low-paid successor.

This bound is independent of the represented AP mass.

For a singleton contracted state R=0, the raw bound is at most z_min(r)+1<=14 phase cells; r=10 sharpens further to the nine MATH-220 address cells.

## 7. Correction/Hensel information is not lost

The composed affine cylinder determines its exact correction numerator by

C = 2^H B - 3^Q A.

Therefore Sigma, normalized correction, Hensel class, and terminal defect coordinates remain derivable from the contracted state, by MATH-189/197.

No separate raw parity history is required.

## 8. Consequence

The logical gap left after MATH-226 is no longer 'how to represent arbitrary safe prefixes'.

That representation is now exact and future-complete.

The remaining quantitative problem is only:

how many distinct reachable contracted SAFE states survive, and do any of their <=54 first-danger singleton candidates evade terminal descent / Bellman reserve closure?

## Claim boundary

Established:
- exact variable-r cylinder composition;
- exact phase and penalty composition;
- exact adjusted Bellman reserve;
- arbitrary SAFE-prefix contraction;
- SAFE*·DANGER normal form;
- <=54 first-danger ordinary candidates per contracted state after r=10.

Not established:
- a small bound on the number of reachable contracted SAFE states;
- closure of every first-danger candidate from every reachable contracted state;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.