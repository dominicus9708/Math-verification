# Primitive continued-fraction renewal words are first coefficient crossings

Date: 2026-08-11

Status: **exact consequence of the renewal rational-shadow minimum and the best-approximation property of continued-fraction convergents**. This is a strong restriction on the primitive upper-CF residual branch, but it is not a proof of its exclusion and must not be confused with a proof of the Coefficient Stopping Time conjecture.

## 1. Setup

Put

\[
\gamma:=\log_2 3.
\]

Let an aggregate-supercritical renewal word have accelerated length `A` and odd count `H`, with

\[
\boxed{\frac AH>\gamma.}
\]

Assume `(A,H)` is primitive,

\[
\gcd(A,H)=1,
\]

and `A/H` is an upper continued-fraction convergent of `gamma`.

Define the total positive coefficient discrepancy

\[
\boxed{\delta:=A-\gamma H>0.}
\]

Let `C` be the positive rational periodic shadow minimum of the renewal word.

## 2. Every proper suffix is coefficient-contracting

Take any proper parity boundary inside the word. Let the corresponding rational shadow state be `C_r` and let the suffix from this boundary to the end have accelerated length `A_s` and odd count `H_s`.

The renewal shadow has `C` as its strict global minimum over the parity rotations, so

\[
\boxed{C_r>C.}
\]

The suffix affine map has positive additive correction and sends `C_r` to `C`.

An affine map

\[
y\mapsto a_s y+b_s,
\qquad b_s>0,
\]

cannot map a positive `y` to a smaller value if `a_s>=1`. Therefore

\[
\boxed{a_s<1.}
\]

For the accelerated Collatz suffix,

\[
a_s=\frac{3^{H_s}}{2^{A_s}},
\]

so

\[
\boxed{
\delta_s:=A_s-\gamma H_s>0.
}
\]

This holds for every proper suffix, not merely for maximal-block boundaries.

## 3. Best-approximation lower bound on every proper suffix discrepancy

Because `A/H` is a continued-fraction convergent of `gamma`, it is a best approximation of the second kind. Hence for every integer pair `(A_s,H_s)` with

\[
0<H_s<H,
\]

we have

\[
\boxed{
|A_s-\gamma H_s|
>
|A-\gamma H|
=\delta,
}
\]

apart from the irrelevant equality/base degeneracies.

Since every proper suffix discrepancy is positive,

\[
\boxed{\delta_s>\delta.}
\]

## 4. Every proper prefix remains below the coefficient crossing

Let the complementary proper prefix have counts `(A_p,H_p)`. Then

\[
A=A_p+A_s,
\qquad
H=H_p+H_s,
\]

so

\[
\delta
=
(A_p-\gamma H_p)
+
(A_s-\gamma H_s).
\]

Therefore

\[
\delta_p:=A_p-\gamma H_p
=
\delta-\delta_s<0.
\]

Thus every proper prefix satisfies

\[
\boxed{
A_p-\gamma H_p<0,
}
\]

or equivalently

\[
\boxed{
2^{A_p}<3^{H_p}.
}
\]

At the full endpoint,

\[
\boxed{2^A>3^H.}
\]

Hence the full word is exactly a **first coefficient-crossing word**:

\[
\boxed{
2^{A_p}<3^{H_p}
\quad\text{for every proper prefix},
\qquad
2^A>3^H.
}
\]

## 5. Nearest upper layer

The convergent estimate gives

\[
0<\frac AH-\gamma<\frac1{H^2},
\]

so

\[
0< A-\gamma H<\frac1H<1
\]

for `H>1`. Consequently

\[
\boxed{A=\lceil\gamma H\rceil.}
\]

Thus the primitive upper-CF branch lies automatically on the minimal supercritical integer layer.

## 6. Relation to the coefficient-stopping problem

This theorem must be used with care.

The statement that an integer cannot remain above its start at its first coefficient crossing would essentially assert the Coefficient Stopping Time conjecture, which is not proved here.

The present result is narrower: it says that any primitive upper-CF **renewal** candidate necessarily lies inside that hard first-crossing sector while also satisfying all of the additional renewal constraints already derived:

- the renewal gap is a positive multiple of `4`;
- `0<g<H/3`;
- the exact gap congruence `g congruent g_w mod (2^A-3^H)`;
- all interior block starts lie above the next renewal floor;
- the fixed-word shadow/gap window;
- the near-Christoffel defect budget.

The next proof step should exploit these extra conditions rather than replace them by the stronger unproved global CST claim.
