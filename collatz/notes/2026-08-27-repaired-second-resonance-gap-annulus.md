# Repaired second-resonance gap annulus

Date: 2026-08-27

Status: **SAFE LEMMA + exact rational certificate, conditional only on entering the exact second-resonance branch isolated by the repaired phase-renewal bridge.** No ternary Cantor-core assumption and no repeated-local pullback is used. This is not a proof of the Collatz conjecture.

## 1. Repaired two-block setup

Let a hypothetical minimal counterexample `N` satisfy the already-certified first-resonance state

\[
(A_0,Q_0)
=(114208327604,72057431991),
\]

\[
y=T^{A_0}(N)=N+g,
\qquad
0<g<2^{33},
\qquad
g\equiv0\pmod4,
\]

with

\[
N>2^{71}.
\]

The endpoint near-survival theorem gives coefficient survival of `y` through every proper prefix before `A_0`.

The phase-renewal bridge then isolates

\[
(K_1,P_1)
=(103768467013,65470613321).
\]

We now take only the exact second-resonance branch

\[
q_{K_1}(y)=P_1.
\]

Put

\[
z=T^{K_1}(y),
\qquad
h=z-N.
\]

The goal is to bound `h` without any ternary recursive-sufficiency input.

## 2. First-resonance correction also bounds the root magnitude

Write

\[
P_0=\frac{2^{A_0}}{3^{Q_0}}>1.
\]

In normalized correction form,

\[
y=\frac{N+S_w}{P_0},
\]

hence

\[
g
=\frac{S_w-(P_0-1)N}{P_0}>0.
\]

Therefore

\[
(P_0-1)N<S_w.
\]

The mechanical first-crossing correction ceiling gives

\[
S_w\le
\frac{Q_0}{6\ln2}+\frac13.
\]

Also

\[
P_0-1
>\ln P_0
=A_0\ln2-Q_0\ln3.
\]

The exact rational logarithm certificate therefore proves

\[
\boxed{
N<\frac43\,2^{71}.
}
\]

Numerically the certified intermediate ratio is about

\[
N/2^{71}<1.331529,
\]

so the rational `4/3` bound has positive margin.

Consequently

\[
\boxed{
y<N+2^{33}<\frac43\,2^{71}+2^{33}.}
\]

This root-magnitude ceiling is unconditional inside the repaired first-resonance branch and does not use the old conditional Cantor-core lower bound.

## 3. The second block is slightly supercritical

Define

\[
x_1:=P_1\ln3-K_1\ln2>0
\]

and

\[
B_1:=\frac{3^{P_1}}{2^{K_1}}=e^{x_1}>1.
\]

Exact rational log bounds certify

\[
\boxed{
2^{-38}<x_1<2^{-37}.
}
\]

Numerically,

\[
x_1\approx4.6122352249\times10^{-12}.
\]

Because the affine correction is positive,

\[
z-y>(B_1-1)y.
\]

Using

\[
B_1-1=e^{x_1}-1>x_1
\]

and

\[
y>N>2^{71},
\]

we get

\[
z-y
>x_1 2^{71}
>2^{-38}2^{71}
=2^{33}.
\]

Thus

\[
\boxed{z-y>2^{33}.}
\]

Since `g>0`, this already implies

\[
\boxed{h=z-N>2^{33}.}
\]

So the second resonance cannot return inside the first near-return window.

## 4. Proper-prefix survival bounds the second correction

Write the exact second-block affine formula as

\[
z=\frac{3^{P_1}y+R_1}{2^{K_1}}.
\]

Because `y` coefficient-survives every proper prefix of this block, the standard whole-prefix correction bound applies:

\[
R_1\le P_1 3^{P_1-1}.
\]

Therefore

\[
z-y
\le
(B_1-1)y+B_1\frac{P_1}{3}.
\]

Put

\[
U:=2^{-37}.
\]

Since `0<x_1<U<1`, the elementary inequality

\[
e^{x_1}\le\frac1{1-U}
\]

gives

\[
B_1\le\frac1{1-U},
\qquad
B_1-1\le\frac{U}{1-U}.
\]

Using the root/endpoint ceiling from Section 2,

\[
y<\frac43\,2^{71}+2^{33},
\]

we obtain the exact rational upper bound

\[
z-y
<
\frac{
U\left(\frac43 2^{71}+2^{33}\right)+P_1/3
}{1-U}.
\]

Adding

\[
g<2^{33}
\]

and evaluating only rational inequalities yields

\[
\boxed{
h<7\cdot2^{33}.}
\]

The actual certified coarse ratio is about

\[
h/2^{33}<6.207261.
\]

Hence the deliberately simple integer constant `7` is safe.

## 5. Minimality forces the second endpoint to be 3 mod 4

We have

\[
z=N+h,
\qquad
h<7\cdot2^{33}.
\]

Since

\[
7\cdot2^{33}<2^{71}<N,
\]

if `z` were even then

\[
T(z)=z/2<N,
\]

contradicting minimal-counterexample no-descent.

If

\[
z\equiv1\pmod4,
\]

then

\[
T^2(z)=\frac{3z+1}{4}.
\]

But the rational certificate also verifies

\[
3\cdot7\cdot2^{33}+1<2^{71}<N,
\]

so

\[
3h+1<N
\]

and consequently

\[
T^2(z)<N,
\]

again impossible.

Therefore

\[
\boxed{z\equiv3\pmod4.}
\]

The minimal root already satisfies

\[
N\equiv3\pmod4,
\]

hence

\[
\boxed{h=z-N\equiv0\pmod4.}
\]

## 6. Second-resonance annulus theorem

Combining the preceding sections gives the repaired branch theorem

\[
\boxed{
h\in4\mathbb Z_{>0},
\qquad
2^{33}<h<7\cdot2^{33}.}
\]

Equivalently, if the first near-return endpoint takes the exact upper-convergent block and the original trajectory reaches the next lower resonance, then its second endpoint must lie in the thin arithmetic annulus

\[
\boxed{
N+2^{33}<T^{A_2}(N)<N+7\cdot2^{33},
\qquad
T^{A_2}(N)\equiv N\equiv3\pmod4.
}
\]

Here

\[
(A_2,Q_2)
=(217976794617,137528045312).
\]

## 7. DSD significance

The repaired two-boundary chain is now

\[
N
\xrightarrow[A_0]{Q_0}
N+g
\xrightarrow[K_1]{P_1}
N+h,
\]

with the two displacements living in disjoint certified scales:

\[
\boxed{
0<g<2^{33}
< h <7\cdot2^{33}.
}
\]

Thus the second exact resonance does not reproduce the first tiny return. It necessarily jumps out of the first return cell, but remains within a fixed additive `O(2^33)` neighborhood of the same minimal root despite more than `2.17e11` accelerated steps.

This is a stronger two-boundary arithmetic target than the old standalone second-resonance/Cantor-core calculation, and it is independent of the currently unproved Ansari recursive-sufficiency entry theorem.

## 8. Audit classification

- **SAFE:** phase-renewal bridge and exact branch split.
- **SAFE:** first-resonance normalized correction ceiling and resulting `N<(4/3)2^71`.
- **SAFE:** second-block proper-prefix correction bound.
- **SAFE:** exact rational logarithm inequalities and mod-4 minimality argument.
- **NOT USED:** ternary selector/Cantor-core entry.
- **NOT USED:** repeated local residue-maximality pullback.
- **OPEN:** exclude all arithmetic words realizing this second-return annulus, or prove that the endpoint block must instead gain one surplus odd event before `K_1`.

Companion certificate:

`collatz/src/second_resonance_gap_annulus_certificate.py`
