# Four-block recursive-core reduction at the next unresolved resonance

Date: 2026-08-09

Status: **EXACT FINITE SET REDUCTION USING CURRENT LOWER/UPPER WINDOWS**

This note combines the current recursive-sufficiency verified lower interval with the Denjoy–Koksma binary magnitude bound for the next unresolved upper convergent. It is a finite reduction, not a Collatz/CST proof.

## 1. Numerical window

The next unresolved convergent resonance is

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617.
\]

The recursive-sufficiency verification floor used by the project is

\[
L=4\cdot3^{44}+2.
\]

The Denjoy–Koksma resonance refinement gives the high-precision finite bound

\[
x<3.6797780659000120\times10^{22}<2^{75}.
\]

For the exact combinatorial reduction below, only the clean integer window

\[
\boxed{L<x<2^{75}}
\]

is used.

## 2. Recursive-sufficiency core

A hypothetical minimal counterexample in the recursively sufficient core has

\[
x=4Y+3,
\qquad
Y=3^m+\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

The window `L<x<2^75` permits exactly the leading ternary depths

\[
\boxed{m\in\{44,45,46\}.}
\]

The depth ranges are:

\[
4\cdot3^{44}+3\le x\le 4\left(\frac{3^{45}-1}{2}\right)+3,
\]

\[
4\cdot3^{45}+3\le x\le 4\left(\frac{3^{46}-1}{2}\right)+3,
\]

and the lower part of the `m=46` layer.

## 3. Exact restriction in the m=46 layer

The inequality `x<2^75` is equivalent to

\[
Y<2^{73}.
\]

For `m=46`, write

\[
Y=3^{46}+a_{45}3^{45}+a_{44}3^{44}
+\sum_{i=0}^{43}a_i3^i.
\]

Since

\[
2^{73}-1-3^{46}<3^{44},
\]

both high optional digits are forced to vanish:

\[
\boxed{a_{45}=a_{44}=0.}
\]

Conversely,

\[
\sum_{i=0}^{43}3^i=\frac{3^{44}-1}{2}
<2^{73}-1-3^{46},
\]

so every choice of the lower 44 digits is allowed.

Thus the m=46 layer contributes exactly

\[
\boxed{2^{44}}
\]

candidates to the clean window.

## 4. Four identical 44-digit blocks

Put

\[
S=\sum_{i=0}^{43}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

All recursively sufficient candidates in `L<x<2^75` are exactly

\[
\boxed{x=4(S+C_j)+3}
\]

with

\[
\boxed{
C_j\in
\{3^{44},\ 3^{45},\ 3^{45}+3^{44},\ 3^{46}\}.
}
\]

The four blocks correspond respectively to

1. depth 44;
2. depth 45 with `a_44=0`;
3. depth 45 with `a_44=1`;
4. depth 46 with `a_45=a_44=0`.

Each block contains exactly `2^44` values, so the complete clean-window core has

\[
oxed{4\cdot2^{44}=2^{46}=70,368,744,177,664}
\]

candidates.

This is an exact parameter-count identity. It does not mean flat enumeration is practical.

## 5. Common two-step Collatz form

Every candidate is `3 mod 4`, hence its first two accelerated steps are odd. For

\[
x=4Y+3
\]

one has

\[
T(x)=6Y+5,
\qquad
\boxed{T^2(x)=9Y+8.}
\]

Therefore all four blocks share the same 44-digit variable contribution after the compulsory `OO` prefix:

\[
\boxed{
T^2(x)=9S+(9C_j+8).
}
\]

The remaining cross-base problem is thus four affine translates of one common 44-digit ternary subset-sum family, not three unrelated ternary depths.

## 6. Record interpretation

Any candidate in this window realizing the specified first coefficient crossing would satisfy

\[
\tau_c(x)=217,976,794,617.
\]

Hence it would force an enormous coefficient-stopping record at bit length at most 75:

\[
\boxed{M(75)\ge217,976,794,617.}
\]

Equivalently, in the recursively sufficient parameterization, one of the four 44-digit affine blocks would have to contain an element with that coefficient stopping time.

This is a finite restatement, not an upper bound on `M(75)`.

## 7. Next use

The four-block representation is intended for exact cross-base methods:

- meet-in-the-middle on the common 44-digit subset sum;
- parity/carry interval certificates on each affine translate;
- deterministic endpoint merging;
- or a proof-level exclusion theorem coupling ternary digits to late-lift forcing.

No independence or random-distribution assumption is used.