# MATH-228 — finite 129-bit future address for the remaining low-paid transducer

Date: 2026-09-19

Status: EXACT VARIABLE-r FINITE-PRECISION THEOREM / r=2..10 / r=10 OPEN

## 1. Remaining low-paid edge depth

For every remaining paid tag 2<=r<=10, MATH-058 gives zero-cost prefix length L<=72.

MATH-179 gives paid first-return cluster length

h_r = r+1+m(r)+I,  I in {0,1},  m(r)=floor(r log2(3/2)).

For r<=10, h_r<=17, with the maximum attained at r=10.

Therefore every complete remaining low-paid boundary factor has dyadic source depth

boxed: h_edge <= 72+17 = 89.

## 2. Normalized address

For a current exact family

Y = B + 3^Q s,   0<=s<M,

define

G = 3^(-Q) in Z_2,
X = G B in Z_2,
R = ceil(log2 M), with R=0 for M=1.

For a canonical next factor

A_e + 2^h t -> B_e + 3^q_e t,

define

eta = G A_e,
beta = 3^(-(Q+q_e)) B_e.

Compatibility selects

rsel = (eta-X) mod 2^h.

If rsel>=M the edge is empty.

If rsel<M, write s=rsel+2^h u. Then

M' = 1 + floor((M-1-rsel)/2^h),

and the exact normalized child intercept is

X' = (X+rsel-eta)/2^h + beta.

Also

G' = G * 3^(-q_e).

This is exactly the MATH-092 radix-2 shift-add transition, now used for arbitrary remaining low-paid factors.

## 3. Resolution-indexed precision

Define

boxed: P_10(R)=89+R.

Assume the child remains multi-source, M'>=2.

Then necessarily h<=R; otherwise one residue class modulo 2^h contains at most one member of a family of size <=2^R.

Moreover

M' <= ceil(M/2^h),

so

R' <= R-h.

MATH-092 consumes exactly h low dyadic bits. Starting with P=89+R bits leaves

P-h = 89+R-h >= 89+R' = P_10(R').

Thus the child still has every bit required for all future r=2..10 address decisions.

If M'=1, the ordinary source is exact and no symbolic source-address precision theorem is needed.

Therefore

boxed: (X mod 2^(89+R), G mod 2^(89+R))

is future-complete for the entire remaining low-paid address channel.

## 4. r=10 output bound

MATH-225 proves every frozen r=10 child family has R<=40.

Hence throughout its symbolic multi-source continuation

P_10(R) <= 89+40 = 129.

So the address part of the safe-prefix transducer never needs more than 129 dyadic bits.

## 5. DSD consequence

The remaining address state is finite and decreases in precision as source resolution is consumed.

Raw AP member lists, arbitrary 2-adic tails, and unbounded ordinary carry values are not required as independent proof-state axes.

## Claim boundary

Established:
- full low-paid factor depth <=89 for r=2..10;
- exact normalized shift-add transition for those factors;
- future-complete precision P_10(R)=89+R;
- maximum symbolic precision 129 bits after the frozen r=10 layer.

Not established:
- a small bound on the number of reachable 129-bit states;
- safe-prefix transducer emptiness;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.