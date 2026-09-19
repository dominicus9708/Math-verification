# MATH-239 — universal coefficient-sign descent theorem through shortcut depth 183

Date: 2026-09-19

Status: EXACT GENERAL THEOREM / CORRECTION-FREE TERMINAL SIGN THROUGH DEPTH 183 / r=10 OPEN

## 1. General shortcut prefix

Let a shortcut Collatz parity prefix have total length H and Q odd steps at positions

0 <= p_0 < ... < p_(Q-1) <= H-1.

Then

T^H(N) = (3^Q N + C)/2^H

with exact correction

C = sum_{j=0}^{Q-1} 3^(Q-1-j) 2^(p_j).

Define

rho = 2^H/3^Q,
S = C/3^Q.

Then

T^H(N)-N = [S-N(rho-1)]/rho.

## 2. Universal correction bound

Because Q-1-j odd positions must still occur after p_j,

p_j <= H-Q+j.

Therefore

S = sum 2^(p_j)/3^(j+1)
  <= 2^(H-Q) sum_{j=0}^{Q-1} 2^j/3^(j+1)
  = 2^(H-Q)(1-(2/3)^Q)
  < 2^(H-Q)

for Q>=1.

For Q=0, S=0.

Thus universally

boxed: 0 <= S < 2^(H-Q).

No mechanical-word, paid-count, or first-return assumption is used.

## 3. Coefficient-expanding prefixes

If

3^Q > 2^H,

then

(3^Q-2^H)N + C > 0

for every positive N.

Hence

boxed: 3^Q>2^H => T^H(N)>N.

This direction is universal at every depth.

## 4. Coefficient-contracting prefixes

Suppose

2^H > 3^Q.

Strict descent follows if

N(rho-1)>S.

Using the universal correction bound, it is sufficient that

N > [2^(H-Q) 3^Q]/[2^H-3^Q].

Define the exact threshold

B(H,Q) = 2^(H-Q) 3^Q / (2^H-3^Q).

## 5. Exact finite maximum through H=183

An exact rational audit over

1<=H<=183, 0<=Q<=H, 3^Q<2^H

gives

max B(H,Q) = B(176,111)

= 3368286247049896651946194200900164104960084569150131912588856928820527104
  / 4483389639004442388280709442303812380810953936563989

approximately 7.5128e20.

This is strictly below

2^71 = 2361183241434822606848.

Therefore every N>2^71 satisfies the descent inequality for every coefficient-contracting prefix of length at most 183.

## 6. The sign theorem

Combining Sections 3 and 5, and noting 2^H=3^Q has no positive nontrivial integer solution,

boxed:
For N>2^71 and 1<=H<=183,
sgn(T^H(N)-N) = sgn(3^Q-2^H).

Equivalently, throughout this range the correction term can never reverse the sign implied by the multiplicative coefficient.

## 7. Sharpness of the audited depth range

At H=184, Q=116,

B(184,116) is approximately 2.8047e21,

which exceeds 2^71.

So the same universal floor-only argument is no longer sufficient beginning at depth 184.

This does not prove a counterexample at depth 184; it only marks the end of this particular universal bound.

## 8. r=10 consequence

A frozen r=10 complete factor has H<=89.

After MATH-235 the surviving multi-source continuation has at most 38 additional dyadic bits.

Hence every synchronized prefix before singletonization has global depth

H_global <= 89+38 = 127 < 183.

Therefore throughout the entire post-r10 multi-source symbolic horizon:

- cumulative coefficient contraction 3^Q<2^H => exact self-descent below the original source;
- cumulative coefficient expansion 3^Q>2^H => exact non-descent;
- no partial J-threshold cylinder exists.

This removes the master correction C from the terminal SIGN decision during the whole multi-source r=10 horizon, although C remains needed for exact address/synchronized composition.

## 9. Relation to MATH-235/238

MATH-235's all-or-none split for r=10 and MATH-238's orientation coherence for every frozen r=2..12 factor are direct finite manifestations of this general theorem, because all those full factors lie far below depth 183.

## Claim boundary

Established:
- universal correction bound S<2^(H-Q);
- exact coefficient-sign theorem for every N>2^71 through H=183;
- complete applicability to the post-r10 multi-source horizon H<=127.

Not established:
- coefficient-sign control after depth 183;
- closure of coefficient-expanding singleton tails;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.