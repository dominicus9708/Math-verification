# Forced-OO resonance converts the boundary Fourier phase to forward correction

Date: 2026-08-24

Status: **exact modular/Fourier identity.**  This identifies the large odd-frequency resonances of the Beatty boundary transfer with a forward-correction exponential sum and aligns them with the ternary selector clock.  It is not yet a decay theorem and is not a proof of the Collatz conjecture.

## 1. Strip the forced initial `11`

For every coefficient-surviving accelerated Collatz prefix of depth at least two, the first two parity symbols are forced odd.

Write the starting integer as

\[
N=4Y+3.
\]

Two accelerated odd steps give exactly

\[
\boxed{T^2(N)=9Y+8.}
\]

Fix a total binary depth `K>=2`.  Put

\[
L:=K-2.
\]

If the complete word has `Q` odd symbols, its tail after the forced `11` has

\[
q':=Q-2
\]

odd symbols.

Let the tail odd positions, now measured from zero inside the tail, be

\[
0\le d_1<\cdots<d_{q'}\le L-1.
\]

Define the ordinary forward tail correction

\[
\boxed{
R_{\rm tail}
:=
\sum_{\ell=1}^{q'}
3^{q'-\ell}2^{d_\ell}.
}
\]

Then the exact tail affine relation is

\[
\boxed{
2^L Z
=
3^{q'}(9Y+8)+R_{\rm tail},
}
\]

where `Z=T^K(N)`.

## 2. Canonical reduced address

Reducing modulo `2^L` gives

\[
9\,3^{q'}Y+8\,3^{q'}+R_{\rm tail}
\equiv0\pmod{2^L}.
\]

Since 9 is a dyadic unit,

\[
\boxed{
3^{q'}Y
\equiv
-8\,9^{-1}3^{q'}
-9^{-1}R_{\rm tail}
\pmod{2^L}.
}
\]

This is the reduced-coordinate counterpart of the usual Hensel inverse formula.

## 3. Resonant odd-frequency identity

Let

\[
e_L(x):=\exp(2\pi i x/2^L).
\]

For any odd integer `h`, choose the reduced Fourier frequency

\[
\boxed{t=h3^{q'}.}
\]

Then the previous congruence yields

\[
\boxed{
 e_L(tY)
=
 e_L(-8h\,9^{-1}3^{q'})
 \,e_L(-h\,9^{-1}R_{\rm tail}).
}
\]

The first factor is independent of the parity word.  Therefore on every fixed-`q'` boundary family,

\[
\boxed{
\left|
\frac1B\sum_{\rm boundary}e_L(h3^{q'}Y)
\right|
=
\left|
\frac1B\sum_{\rm boundary}
 e_L(-h9^{-1}R_{\rm tail})
\right|.
}
\]

Thus the resonant boundary Fourier coefficient is exactly a **forward-correction exponential sum**.  No inverse powers of three remain.

This explains why frequencies in the `3^{q'}` orbit repeatedly appear among the largest boundary Fourier modes in finite scans.

## 4. Exact triadic-place split with the selector

For a recursively sufficient ternary selector

\[
Y=3^m+\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

the normalized selector Fourier transform at the same resonant frequency is, up to the fixed leading-digit phase,

\[
\boxed{
\widehat\mu_{m,L}(h3^{q'})
=
\prod_{i=0}^{m-1}
\frac{1+e_L(h3^{q'+i})}{2}.
}
\]

The forward tail correction, on the other hand, uses ternary exponents

\[
q'-\ell\in\{0,1,\ldots,q'-1\}.
\]

Hence the two pieces occupy adjacent triadic exponent ranges:

\[
\boxed{
\begin{array}{ll}
\text{dynamical forward correction:}&3^0,3^1,\ldots,3^{q'-1},\\[1mm]
\text{selector digits at resonance:}&3^{q'},3^{q'+1},\ldots,3^{q'+m-1}.
\end{array}}
\]

This is an exact split at the same `q'` boundary.  The remaining resonance problem is therefore a mixed-coefficient carry/oscillation problem on one contiguous ternary clock rather than two unrelated Fourier systems.

## 5. Relation to the tri-place program

The earlier Christoffel tri-place coordinate showed that one normalized correction defect simultaneously controls real, 2-adic and modular-gap locations.  The present identity is complementary:

- the forced-OO reduction removes the two universal initial odd events;
- the resonant frequency `3^{q'}` removes the remaining Hensel inverse;
- the boundary phase is expressed in ordinary forward correction coordinates;
- the selector occupies the immediately higher ternary places.

Thus a useful next theorem can be stated without generic frequency language:

> **Resonant triadic carry cancellation target.**  Bound the joint selector/boundary contribution when the lower ternary places carry dyadic coefficients `2^{d_ell}` from an admissible Beatty excursion and the higher places carry selector digits `0/1`.

Off-resonant frequencies remain governed by the valuation boundary-projection and selector Riesz attenuation framework.
