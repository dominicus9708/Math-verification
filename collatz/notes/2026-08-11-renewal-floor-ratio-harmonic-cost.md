# Renewal floor-ratio harmonic cost

Date: 2026-08-11

Status: **exact/safe harmonic necessary condition for an aggregate-supercritical renewal segment**. Unlike a withdrawn event-level estimate, this argument uses only the current renewal floor `N` as a lower bound for all future odd-event states, which is guaranteed by suffix-minimality.

## 1. Renewal setup

Let `N<N'` be consecutive renewal floors in a hypothetical nonperiodic first-descent survivor. Let the renewal segment contain `H` odd events, with odd-event states

\[
x_0=N,x_1,\ldots,x_H=N'.
\]

Because `N` is a suffix minimum,

\[
\boxed{x_i\ge N\qquad(0\le i\le H).}
\]

The orbit is nonperiodic, so these states are distinct. For `i>=1`, each odd-event state is odd and not divisible by `3`.

Let

\[
P=\frac{2^{H+D}}{3^H}
\]

be the aggregate multiplier, and suppose

\[
\boxed{P>1.}
\]

## 2. Reciprocal-sum bound

Among positive integers, the odd integers not divisible by `3` occupy the two residue classes `1,5 mod 6`. Their counting density is `1/3`.

Ordering the distinct states `x_i` and using at most two admissible residues per interval of length six gives the explicit safe bound

\[
\boxed{
\sum_{i=0}^{H-1}\frac1{x_i}
\le
\frac3N+
\frac13\log\left(1+\frac{3H}{N}\right).
}
\]

The constant `3/N` is deliberately coarse so that no residue-alignment edge case is hidden.

## 3. Exact correction product

At odd-event resolution,

\[
\boxed{
P\frac{N'}N
=
\prod_{i=0}^{H-1}
\left(1+\frac1{3x_i}\right).
}
\]

Since `P>1`,

\[
\frac{N'}N
<
\prod_{i=0}^{H-1}
\left(1+\frac1{3x_i}\right).
\]

Using `log(1+t)<=t` and the reciprocal-sum bound,

\[
\log\frac{N'}N
<
\frac1N+
\frac19\log\left(1+\frac{3H}{N}\right).
\]

Therefore

\[
\boxed{
\frac{N'}N
<
e^{1/N}
\left(1+\frac{3H}{N}\right)^{1/9}.
}
\]

## 4. Depth lower bound from a floor ratio

Rearranging gives

\[
\boxed{
H>
\frac N3
\left[
\left(
e^{-1/N}\frac{N'}N
\right)^9-1
\right].
}
\]

Thus an aggregate-supercritical renewal cannot raise the renewal floor by a fixed multiplicative factor at sublinear odd-event cost.

For fixed `rho>1`, if

\[
N'/N\ge\rho,
\]

then for sufficiently large `N`,

\[
\boxed{H\ge c_\rho N}
\]

for an explicit positive constant `c_rho`. More generally the required depth grows like the ninth power of the floor ratio.

## 5. Scope and correction note

This theorem is valid because every future odd-event state is at least the **current** suffix minimum `N`.

It does **not** claim that all internal odd-event states are at least the **next** renewal floor `N'`. That stronger statement is false inside a maximal block and was the source of a previously withdrawn estimate.

The present floor-ratio theorem is therefore safe to combine with the Christoffel renewal-shadow bounds.
