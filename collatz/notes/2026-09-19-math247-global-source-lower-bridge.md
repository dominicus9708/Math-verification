# MATH-247 — global-source lower bridge for local r=10 boundary factors

Date: 2026-09-19

Status: EXACT ORIGINAL-SOURCE TERMINAL BRIDGE / REPLACEMENT FOR LOCAL-J CLOSURE / r=10 OPEN

## 1. Original source and local boundary anchor

Let N be the original first-cell ordinary start and let Y=T^k(N) be a coefficient-valid u=0 boundary anchor.

MATH-053/057 give at such an anchor

N = Omega Y - S,

with

0 <= S < q/3 <= q0/3,

where q0=72,057,431,991 is the first-cell odd-count ceiling and Omega is the exact boundary phase.

Suppose the source phase lies in an exact cell

Omega in [omega_lo,omega_hi].

Then

boxed: N > omega_lo Y - q0/3.

## 2. Safe terminal criterion for an imported local factor

Let one MATH-206 local boundary factor be

Y(s)=A+2^H s,
Y'(s)=B+3^Q s,
0<=s<M.

If

boxed: Y'(s) < omega_lo Y(s) - q0/3,

then Y'(s)<N.

For a hypothetical minimal counterexample N, reaching a smaller positive integer closes that source by minimality.

This comparison is referenced to the original source N and therefore does not make the local-origin mistake identified in MATH-246.

## 3. Exact affine threshold

Define

D(s)=omega_lo(A+2^H s) - (B+3^Q s) - q0/3.

Then

D(s)=D0+s Delta,

where

D0=omega_lo A-B-q0/3,

Delta=omega_lo 2^H-3^Q.

All quantities are exact rationals.

The globally safe original-source closure set inside a local cylinder is exactly the integer interval subset

{s in [0,M): D(s)>0}.

Because D is affine, this set is one prefix, one suffix, all, or empty. No ordinary-source enumeration is needed.

## 4. Frozen-floor closure combines independently

Also, any target

Y'(s)<=2^71

is closed by the frozen verified floor.

Since Y'(s) is increasing in s, the floor-closed set is an initial interval.

The union of the floor interval and the MATH-247 original-source-descent interval is therefore computable exactly by interval arithmetic for every frozen r=10 factor.

## 5. Why this is stronger than merely reverting MATH-235

MATH-235 used only the local comparison Y'<Y, which is not globally sufficient.

MATH-247 replaces it with the phase-aware lower bound on the true original source N.

It can therefore safely recover any local-factor pruning that is strong enough to cross not just below Y but below the original-source lower envelope.

## Claim boundary

Established analytically:
- exact original-source lower envelope N>omega_lo Y-q0/3;
- exact affine whole/partial-cylinder closure test D(s)>0;
- compatibility with direct frozen-floor closure.

The amount of the frozen r=10 workload removed by this criterion is a finite exact certificate result and must be reported separately after execution.

r=10 remains OPEN.
First-cell emptiness remains OPEN.
The Collatz conjecture remains OPEN.