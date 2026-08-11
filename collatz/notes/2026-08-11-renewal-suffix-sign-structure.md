# Renewal suffix-sign structure

Date: 2026-08-11

Status: **exact structural theorem for renewal-floor segments at maximal-block resolution**.

## 1. Setup

Let

\[
X_0=N<X_m=N'
\]

be consecutive renewal floors, with

\[
X_r>N'
\qquad(0<r<m).
\]

Let block `r` have parameters `(h_r,d_r)` and define

\[
\alpha:=\log_2(3/2),
\qquad
\delta_r:=d_r-\alpha h_r.
\]

The block multiplier is

\[
M_r=2^{\delta_r}.
\]

## 2. First block is subcritical

The first block satisfies

\[
X_1>N'>N=X_0.
\]

By the macroblock sign theorem, every nonperiodic increasing maximal block is subcritical. Hence

\[
\boxed{\delta_0<0.}
\]

## 3. Every proper suffix is aggregate-supercritical

Fix `r` with `1<=r<m`. The suffix from `X_r` to `N'` is an exact positive affine Collatz map

\[
N'=a_r X_r+b_r,
\qquad b_r>0.
\]

Because

\[
N'<X_r,
\]

one must have

\[
a_r<1.
\]

Otherwise `a_r>=1` together with `b_r>0` would imply `N'>X_r`.

The corresponding multiplier convention is the reciprocal linear coefficient, so the suffix multiplier is strictly larger than `1`. Equivalently,

\[
\boxed{
\prod_{k=r}^{m-1}M_k>1.
}
\]

Taking base-2 logarithms,

\[
\boxed{
\sum_{k=r}^{m-1}\delta_k>0
\qquad(1\le r<m).
}
\]

In particular, for `m>1`,

\[
\boxed{\delta_{m-1}>0,}
\]

so the last maximal block is supercritical.

## 4. Reverse-ballot form

Reading discrepancies backward from the renewal endpoint, every proper partial sum is strictly positive:

\[
\delta_{m-1}>0,
\]

\[
\delta_{m-2}+\delta_{m-1}>0,
\]

and so on.

Thus a renewal segment is a strict reverse-ballot word in the irrational block weights `d-alpha h`, with a subcritical first block and strictly supercritical every proper suffix.

The full aggregate discrepancy

\[
\Delta:=\sum_{k=0}^{m-1}\delta_k
\]

may be either negative or positive. Hence renewal segments split only at the total level:

- `Delta<0`: aggregate-subcritical renewal;
- `Delta>0`: aggregate-supercritical renewal.

The internal suffix-sign constraints are common to both.

## 5. Role

This theorem is stronger than merely saying that a renewal segment begins with an increase and ends with a decrease. It constrains every suffix aggregate coefficient.

For an aggregate-supercritical renewal, all reverse partial discrepancy sums, including the total, are positive. This identifies the finite word as the canonical minimum rotation of its positive rational cycle shadow.

For an aggregate-subcritical renewal, every proper suffix is still supercritical, but the first subcritical block is strong enough to push the total discrepancy below zero.

This reverse-ballot structure is a natural candidate for future continued-fraction/Christoffel or discrete-budget analysis of renewal words.
