# Rational Denjoy–Koksma certificate at the next unresolved resonance

Date: 2026-08-09

Status: **DERIVED EXACT RATIONAL CERTIFICATE + INDEPENDENT WOLFRAM CHECK**

This note replaces the previous high-precision decimal check at the next unresolved convergent resonance by an explicit rational certificate. It does not prove Collatz/CST; it only certifies the finite magnitude and recursive-core reductions used by the project.

## 1. Resonance and DK correction bound

Use

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617.
\]

At this convergent denominator, Denjoy–Koksma gives

\[
S^*(q)\le \frac{q}{6\ln2}+\frac13.
\]

Write

\[
\Lambda=\sigma\ln2-q\ln3>0,
\qquad
\delta=e^\Lambda-1.
\]

A paradoxical first crossing satisfies

\[
x\le \frac{S^*(q)}{\delta}.
\]

## 2. Exact rational logarithm intervals

For `0<x<1`,

\[
\log\frac{1+x}{1-x}
=2\sum_{k=0}^{\infty}\frac{x^{2k+1}}{2k+1}.
\]

Let

\[
L_N(x)=2\sum_{k=0}^{N}\frac{x^{2k+1}}{2k+1}.
\]

Because every omitted denominator is at least `2N+3`, the positive tail obeys

\[
0<
\log\frac{1+x}{1-x}-L_N(x)
\le
\frac{2x^{2N+3}}{(2N+3)(1-x^2)}.
\]

Take `N=40`.

- `x=1/3` gives an exact lower/upper rational interval for `ln 2`;
- `x=1/2` gives an exact lower/upper rational interval for `ln 3`.

Denote the lower bound for `ln 2` by `l2` and the upper bound for `ln 3` by `u3`. Then the exact rational number

\[
\Lambda_-:=\sigma l2-q u3
\]

is strictly positive.

Also

\[
S^*(q)
\le
U_S:=\frac{q}{6l2}+\frac13,
\]

and

\[
\delta=e^\Lambda-1\ge \Lambda\ge\Lambda_-.
\]

Hence

\[
\boxed{
x\le \frac{U_S}{\Lambda_-}.}
\]

Exact rational comparison gives

\[
\boxed{
\frac{U_S}{\Lambda_-}
<36,797,925,187,243,805,015,225
<2^{75}.
}
\]

Therefore every paradoxical candidate at this resonance satisfies the fully certified integer bound

\[
\boxed{
x<36,797,925,187,243,805,015,225.}
\]

The margin below `2^75` is

\[
\boxed{
981,006,675,713,356,694,343.
}
\]

No decimal logarithm or floating-point exponential is used in this certificate.

## 3. Exact m=46 ternary-prefix restriction

In the recursive-sufficiency `m=46` layer write

\[
x=4(3^{46}+S)+3,
\qquad
S=\sum_{i=0}^{43}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

The certified integer bound implies

\[
S\le
\boxed{336,543,177,158,450,157,876}.
\]

Now compare the four highest free ternary digits `a_43,a_42,a_41,a_40`.

If `a_43=0`, even the largest possible lower tail is

\[
\frac{3^{43}-1}{2}
=164,128,483,697,268,538,813,
\]

which is below the allowed `S` bound. Hence every prefix `0***` is allowed.

If `a_43=1` and any of `a_42,a_41,a_40` equals 1, the smallest such contribution is already

\[
3^{43}+3^{40}
=340,414,632,853,594,006,428,
\]

which exceeds the allowed `S` bound.

On the other hand, with prefix `1000`, even the maximal remaining tail is

\[
3^{43}+\frac{3^{40}-1}{2}
=334,335,800,124,065,542,027,
\]

which is allowed.

Therefore the high four free trits are restricted exactly to

\[
\boxed{
0000,0001,0010,0011,
0100,0101,0110,0111,
1000.
}
\]

Equivalently,

\[
\boxed{
a_{43}=1\Longrightarrow a_{42}=a_{41}=a_{40}=0.}
\]

Thus the `m=46` block contains at most

\[
\boxed{9\cdot2^{40}=9,895,604,649,984}
\]

candidates rather than `2^44`.

The other three 44-digit affine blocks lie wholly below the certified upper endpoint. Hence the complete recursively sufficient candidate count in the current lower/upper window is exactly

\[
\boxed{
3\cdot2^{44}+9\cdot2^{40}
=62,672,162,783,232.
}
\]

This upgrades the earlier high-precision digit-DP count to an exact rationally certified count.

## 4. Rational defect-density consequence

Let

\[
X_{46}=4\cdot3^{46}+3.
\]

Using the same rational bounds,

\[
\Delta S
\le
A_+:=U_S-\Lambda_-X_{46}.
\]

Together with

\[
N_{\ge s}\le\frac{6\Delta S}{1-2^{-s}},
\]

exact integer arithmetic gives the safe bounds

\[
\boxed{N_{>0}\le14,516,878,922,}
\]

\[
\boxed{N_{\ge2}\le9,677,919,281,}
\]

\[
\boxed{N_{\ge3}\le8,295,359,384.}
\]

Thus every paradoxical `m=46` candidate must have at least

\[
\boxed{89.4444\%}
\]

of its odd positions exactly on the mechanical cap. This is slightly weaker than the earlier high-precision decimal percentage, but it is now fully rationally certified.

## 5. Verification

`collatz/src/rational_dk_next_resonance.py` constructs all logarithm bounds with `fractions.Fraction` and checks the integer comparisons by cross multiplication.

An independent Wolfram exact-rational implementation reproduced:

- positivity of `Lambda_-`;
- the certified integer upper endpoint;
- the nine allowed four-trit prefixes;
- total core count `62,672,162,783,232`;
- the three integer defect-count bounds above.

## 6. Scope

This is a finite rigorous sharpening only. It does not solve the remaining cross-base problem: one must still exclude every candidate whose 44-digit ternary core is compatible with a very long coefficient-surviving Collatz parity word and the certified high-correction constraint.