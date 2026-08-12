# Renewal record quantization and rotation-mean correction bound

Date: 2026-08-12

Status: **exact renewal record-gap quantization + asymptotic irrational-rotation correction bound + exact Denjoy--Koksma corollary at convergent denominators**. This strengthens the adjacent upper-layer cost and the primitive upper-CF first-crossing ceiling. It does not prove Collatz.

## 1. Setup

Work after formation has stabilized at one fixed positive odd integer orbit. For one renewal segment

\[
N=x_0 < N'=x_H=N+g,
\qquad g>0,
\]

write the odd-only Syracuse dynamics as

\[
x_{k+1}=\frac{3x_k+1}{2^{v_k}},
\qquad v_k=v_2(3x_k+1),
\]

and put

\[
A_k:=\sum_{i<k}v_i,
\qquad
\gamma:=\log_2 3,
\qquad
\alpha:=\gamma-1=\log_2(3/2).
\]

Define

\[
e_k:=k\gamma-A_k.
\]

Since every `v_i>=1`, write

\[
W_k:=A_k-k=\sum_{i<k}(v_i-1)\in\mathbb Z_{\ge0}.
\]

Then

\[
\boxed{e_k=k\alpha-W_k.}
\]

The exact affine correction is

\[
c_H:=\sum_{k=0}^{H-1}\frac{2^{A_k}}{3^{k+1}}
=\frac13\sum_{k=0}^{H-1}2^{-e_k}.
\]

The renewal endpoint identity is

\[
\boxed{N+c_H=P(N+g),}
\qquad
P:=\frac{2^{A_H}}{3^H}=2^{-e_H}.
\]

For every genuine renewal endpoint, the previously proved pure-coefficient record theorem gives

\[
\boxed{e_k>e_H\qquad(0<k<H).}
\]

## 2. Quantized record-gap lemma

For `1<=j<=H-1`, compare the endpoint with the prefix `H-j`:

\[
e_{H-j}-e_H
=-j\alpha+\left(W_H-W_{H-j}\right).
\]

The second term is an integer. Because the renewal endpoint is a strict coefficient record, the left side is positive.

Define

\[
\boxed{\delta_j:=\lceil j\alpha\rceil-j\alpha=1-\{j\alpha\}\in(0,1).}
\]

Among positive real numbers congruent to `-j alpha (mod 1)`, the smallest is exactly `delta_j`. Therefore

\[
\boxed{
e_{H-j}-e_H\ge\delta_j,
\qquad 1\le j\le H-1.
}
\]

This is strictly stronger than the qualitative record inequality `e_{H-j}>e_H`: the available record gaps lie on an irrationally shifted integer lattice and cannot approach zero arbitrarily for a fixed lag `j`.

## 3. Adjacent upper layer `sigma=-1`

On the nearest upper critical layer,

\[
A_H=\lceil H\gamma\rceil,
\]

so

\[
e_H
=H\gamma-\lceil H\gamma\rceil
=-\delta_H,
\]

and hence

\[
\boxed{P=2^{\delta_H}\in(1,2).}
\]

For `k=H-j`, the quantized record-gap lemma gives

\[
e_k\ge-\delta_H+\delta_j.
\]

The `k=0` term corresponds exactly to `j=H`, because `e_0=0=-delta_H+delta_H`. Thus every correction term obeys the unified bound

\[
2^{-e_{H-j}}
\le
2^{\delta_H}2^{-\delta_j}
=P\,2^{-\delta_j},
\qquad 1\le j\le H.
\]

Therefore

\[
\boxed{
c_H
\le
\frac P3
\sum_{j=1}^{H}2^{-\delta_j}.
}
\]

Since

\[
2^{-\delta_j}=2^{\{j\alpha\}-1},
\]

define the fixed irrational-rotation sum

\[
\boxed{
S_H(\alpha):=
\sum_{j=1}^{H}2^{\{j\alpha\}-1}.
}
\]

The exact upper-layer renewal budget becomes

\[
(P-1)N+Pg=c_H
\le\frac P3S_H(\alpha).
\]

After division by `P`,

\[
\boxed{
g+\left(1-\frac1P\right)N
\le
\frac13S_H(\alpha).
}
\]

This bound uses only the actual renewal coefficient-record property and the adjacent upper layer; it does not require a first-coefficient-crossing hypothesis.

## 4. Irrational-rotation mean

The function

\[
f(u):=2^{u-1},\qquad 0\le u<1,
\]

is Riemann integrable and

\[
\int_0^1f(u)\,du
=\frac1{2\ln2}.
\]

Because `alpha=log_2(3/2)` is irrational, the Kronecker sequence `{j alpha}` is uniformly distributed modulo one. Hence

\[
\boxed{
\frac{S_H(\alpha)}H
\longrightarrow
\frac1{2\ln2}.
}
\]

Consequently every sufficiently long adjacent-upper-layer renewal satisfies

\[
\boxed{
g+\left(1-\frac1P\right)N
\le
\left(\frac1{6\ln2}+o(1)\right)H.
}
\]

Numerically,

\[
\frac1{6\ln2}=0.240449173\ldots,
\qquad
6\ln2=4.158883083\ldots.
\]

Thus, in asymptotic cost form,

\[
H
\gtrsim
6\ln2\left[
g+\left(1-\frac1P\right)N\right].
\]

The earlier general supercritical bound was

\[
H>3g+3N\ln P.
\]

For `1<P<2`,

\[
6\ln2>3
\]

and

\[
6\ln2\left(1-\frac1P\right)
\ge
3\ln P,
\]

with equality in the second comparison only at the endpoints `P=1` and `P=2`. Therefore the rotation-mean record bound is asymptotically stronger throughout the interior upper critical layer.

## 5. First-coefficient-crossing refinement

Suppose additionally that the full segment is the first coefficient crossing. Then every proper odd-event prefix is coefficient-expanding:

\[
e_k>0,
\qquad 1\le k<H.
\]

But

\[
e_k=k\alpha-W_k
\]

with integer `W_k`. Therefore positivity quantizes each proper prefix directly:

\[
\boxed{
e_k\ge\{k\alpha\}.}
\]

Hence

\[
\boxed{
c_H
\le
\frac13
\sum_{k=0}^{H-1}2^{-\{k\alpha\}}.
}
\]

This removes the extra factor `P` that appears in the record-only upper-layer estimate.

## 6. Exact Denjoy--Koksma bound at convergent denominators

Let `H=q_n` be a continued-fraction convergent denominator of `alpha`. The periodic function

\[
f_-(u):=2^{-u}
\]

has total variation `1` on the circle and mean

\[
\int_0^1 2^{-u}\,du
=\frac1{2\ln2}.
\]

The classical Denjoy--Koksma inequality gives

\[
\left|
\sum_{k=0}^{H-1}2^{-\{k\alpha\}}
-
\frac{H}{2\ln2}
\right|
\le1.
\]

Therefore a primitive upper-CF first-crossing renewal obeys the exact finite bound

\[
\boxed{
c_H
\le
\frac{H}{6\ln2}+\frac13.
}
\]

Using

\[
c_H=(P-1)N+Pg
\]

and the exact renewal-floor congruence `g in 4 Z_{>0}`, hence `g>=4`, gives

\[
\boxed{
N
\le
\frac{
H/(6\ln2)+1/3-4P
}{P-1}.
}
\]

This improves the previous first-crossing ceiling

\[
N<\frac{H}{3(P-1)}
\]

by the asymptotic factor

\[
\boxed{
\frac1{2\ln2}
=0.7213475204\ldots
}
\]

near the critical line.

## 7. Numerical effect on the current upper-CF frontier

For the previously first unresolved upper convergent

\[
(A,H)
=(10{,}439{,}860{,}591,\ 6{,}586{,}818{,}670),
\]

one has

\[
P-1\approx1.0123125321\times10^{-11}.
\]

The old first-crossing ceiling was approximately

\[
2.1689015534\times10^{20}.
\]

The new Denjoy--Koksma ceiling is approximately

\[
\boxed{
1.5645317540\times10^{20}.
}
\]

Thus this step gives a real but not terminal improvement: the first unresolved finite frontier is tightened by about `27.9%`, but the branch is not eliminated.

## 8. Defect-weighted exact form

For a first-crossing prefix define the nonnegative integer skew height

\[
\boxed{
h_k:=\lfloor k\alpha\rfloor-W_k\ge0.}
\]

Then

\[
e_k=\{k\alpha\}+h_k,
\]

and the correction has the exact weighted form

\[
\boxed{
c_H
=\frac13
\sum_{k=0}^{H-1}
2^{-\{k\alpha\}}2^{-h_k}.
}
\]

The Denjoy--Koksma estimate corresponds to discarding the defect damping factor `2^{-h_k}`.

Equivalently, define the weighted defect mass

\[
\boxed{
\mathfrak D_H
:=
\sum_{k=0}^{H-1}
2^{-\{k\alpha\}}
\left(1-2^{-h_k}\right).
}
\]

Then exactly

\[
\boxed{
c_H
=\frac13
\left[
\sum_{k=0}^{H-1}2^{-\{k\alpha\}}
-\mathfrak D_H
\right].
}
\]

This identifies the next quantitative target. The rotation mean fixes the maximal critical correction mass, while every positive skew defect removes a precisely weighted amount from that budget.

## 9. Next hard lemma

A terminal improvement now has a clean form:

> Prove that an exact ordinary-integer first-crossing renewal word that survives the formation/gap constraints cannot have `mathfrak D_H=o(H)` along an infinite upper-critical sequence.

Any positive linear lower bound

\[
\mathfrak D_H\ge\eta H
\qquad(\eta>0)
\]

would replace the coefficient `1/(6 ln 2)` by a strictly smaller constant and immediately strengthen the ordinary-start ceiling.

The already established exact-Christoffel equality branch is eventually finite, so the residual infinite problem is precisely whether near-Christoffel nonzero defects can remain too sparse to produce a linear correction loss while still satisfying the exact dyadic formation and tiny gap residue conditions.

This is the next bridge to attack: **weighted skew-defect mass versus exact formation/gap arithmetic**.
