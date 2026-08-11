# Uniform harmonic scaling for a first-descent survivor

Date: 2026-08-11

Status: **exactly derived universal-scale bound up to an absolute counting constant**. This is a necessary condition for a hypothetical nonperiodic first-descent survivor.

## 1. Setup

Let `N>=3` be odd and suppose its odd-event orbit

\[
x_0=N,x_1,x_2,\ldots
\]

is nonperiodic and satisfies

\[
x_i\ge N
\]

for all `i`.

For `i>=1`, every `x_i` is odd and not divisible by `3`. All event states are distinct.

Define

\[
\lambda_i:=\frac{2^{A_i}}{3^i},
\qquad
c_q:=\frac13\sum_{i=0}^{q-1}\lambda_i.
\]

The exact product identity is

\[
\boxed{
1+\frac{c_q}{N}
=\prod_{i=0}^{q-1}
\left(1+\frac1{3x_i}\right).
}
\]

## 2. Reciprocal packing above N

Among positive odd integers not divisible by `3`, the asymptotic spacing is `3`. Therefore for any `q` distinct such integers all at least `N`, the reciprocal sum is bounded by the reciprocal sum of the `q` smallest admissible integers above `N`.

Consequently

\[
\boxed{
\sum_{i=0}^{q-1}\frac1{x_i}
\le
\frac13\log\!\left(1+\frac{3q}{N}\right)
+O\!\left(\frac1N\right),
}
\]

where the `O(1/N)` term can be replaced by an explicit absolute residue-class endpoint constant if desired.

## 3. Uniform product bound

Using `log(1+t)<=t`,

\[
\log\!\left(1+\frac{c_q}{N}\right)
\le
\frac13\sum_{i<q}\frac1{x_i}.
\]

Hence

\[
\boxed{
1+\frac{c_q}{N}
\le
\exp\!\left(O\!\left(\frac1N\right)\right)
\left(1+\frac{3q}{N}\right)^{1/9}.
}
\]

In particular, for `q` large compared with `N`,

\[
\boxed{
c_q=O(N^{8/9}q^{1/9}).}
\]

For `q=theta N` with fixed `theta>0`,

\[
\boxed{
\frac{c_q}{N}
\le
(1+o_N(1))(1+3\theta)^{1/9}-1.
}
\]

Thus the correction budget is naturally controlled by the dimensionless event horizon `q/N`.

## 4. Suffix-minimum renormalization

Any infinite sequence of distinct positive integers tends to infinity. Therefore a hypothetical nonperiodic divergent orbit has infinitely many suffix-minimum times `t_j` such that

\[
N_j:=x_{t_j}
< x_i\qquad(i>t_j),
\]

and

\[
N_j\to\infty.
\]

Each `N_j` is itself a strict first-descent survivor for its future suffix. Hence the same uniform harmonic bound applies after resetting the event clock at every `N_j`.

This produces an infinite hierarchy of increasingly large survivor starts governed by the same scale law.

## 5. Current limitation

The scale law does not alone force a contradiction: the time between successive suffix minima may grow arbitrarily fast compared with `N_j`, and the cumulative multiplier can be correspondingly small. Its value is to remove the unspecified dependence hidden in `O_N(q^{1/9})` and provide a scale-invariant input for any later renewal or suffix-minimum argument.
