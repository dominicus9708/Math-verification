# Endpoint rational-grid localization at a finite split

Date: 2026-08-09

Status: **DERIVED UNIFORM BOUND + GRID LOCALIZATION + INDEPENDENT FINITE CHECK**

This note isolates additional arithmetic structure in the backward query of the finite-horizon Bellman formulation.  Although the future modulus is `2^m`, canonical prefix endpoints query only a thin rational grid whose denominator is the prefix odd multiplier `3^q`.

No global Collatz result is claimed.

## 1. Uniform endpoint bound inside a prefix cell

Fix a length-`h` parity prefix with `q` odd entries. Put

\[
M=2^h,\qquad P=3^q.
\]

Let its correction be

\[
R=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i},
\qquad d_i<h,
\]

and let `r` be its canonical start in `[0,M)`. The endpoint is

\[
\boxed{y=\frac{Pr+R}{M}.}
\]

Since every odd position satisfies

\[
2^{d_i}\le M/2,
\]

we have

\[
R
\le
\frac M2\sum_{i=0}^{q-1}3^{q-1-i}
=
\frac{M(P-1)}4.
\]

Also `r<M`, hence

\[
\frac{Pr}{M}<P.
\]

Therefore every canonical endpoint obeys the uniform bound

\[
\boxed{
0\le y<P+\frac{P-1}{4}<\frac54P.
}
\]

This bound uses only the affine prefix form and does not depend on the detailed parity ordering.

## 2. Backward transformed query

Fix a remaining horizon `m` and put

\[
N=2^m.
\]

The backward Bellman / suffix query is

\[
\boxed{\xi=[P^{-1}y]_N.}
\]

Assume

\[
\boxed{N>\frac54P.}
\]

Because `P xi-y` is divisible by `N`, there is an integer `t` satisfying

\[
\boxed{P\xi=y+tN.}
\]

The endpoint bound and `0<=xi<N` imply

\[
0\le t<P.
\]

Reducing the identity modulo `P` gives the unique grid label

\[
\boxed{
t=[-yN^{-1}]_P.}
\]

Consequently

\[
\boxed{
\xi=\frac{tN+y}{P}.
}
\]

## 3. Rational-grid localization

The preceding identity gives

\[
\boxed{
0\le
\xi-\frac{tN}{P}
=\frac yP
<\frac54.
}
\]

Thus every transformed endpoint query lies within a one-sided distance `<5/4` of one of the `P` rational grid points

\[
\boxed{
\frac{tN}{P},
\qquad t=0,1,\ldots,P-1.
}
\]

Since `xi` is integral, for each `t` there are at most two possible query integers in this interval.

Therefore all canonical prefix states in a fixed `(h,q)` layer query a subset of a universal set of cardinality at most

\[
\boxed{2P=2\cdot3^q,}
\]

independent of the exponentially larger future modulus `N=2^m`.

This cardinality bound is not necessarily smaller than the number of prefix states, because coefficient survival implies `P>=M`; its importance is geometric rather than combinatorial: the query positions form a small-denominator rational grid rather than an arbitrary subset of the `2^m`-cycle.

## 4. Dangerous interval extension

For a threshold certificate, a prefix state may require testing not only `J=0` but a short interval

\[
J=0,1,\ldots,L-1.
\]

The corresponding transformed query interval is

\[
I_N(\xi,L).
\]

By the grid localization, this interval is contained in

\[
\left[
\frac{tN}{P},
\frac{tN}{P}+L+\frac54
\right)
\]

on the cyclic group after the appropriate integer rounding.

Thus a whole `(h,q)` layer may be safely over-approximated by at most `P` short intervals centered on the denominator-`P` grid.  If the exact suffix interval-count recursion certifies zero admissible points on all such intervals, the whole layer is eliminated without enumerating its individual prefix states.

This is only a sufficient block certificate; a nonzero grid interval may be caused by a point that is not queried by any actual prefix state.

## 5. Relation to the high-resolution defect coordinate

For two prefix states with the same `(h,q)`, endpoint differences also satisfy

\[
|y_1-y_2|<\frac54P.
\]

The high block `W` of the target-resolution defect translation obeys

\[
P W+(y-y^*)=tN
\]

for an integer grid label `t`. Hence

\[
\left|
W-\frac{tN}{P}
\right|
<\frac54.
\]

Therefore the high block of the defect coordinate and the absolute backward query have the same rational-grid geometry.  This is the arithmetic reason the two-coordinate `(U,V)` description could be collapsed to one target-resolution defect residue.

## 6. Interpretation for the late-lift program

At the intended logarithmic split

\[
h=O(\log K),
\]

we have

\[
P=3^q\le3^h=K^{O(1)},
\]

while the remaining modulus

\[
N=2^{K-h}
\]

is exponentially larger.

Thus the difficult backward small-lift queries lie near a polynomial-denominator grid in an exponentially large cycle.

A useful next theorem would exploit the exact E/O suffix recursion specifically at these rational-grid locations, rather than attempting uniform discrepancy control over all `2^m` possible queries.

## 7. Independent finite check

Wolfram exact enumeration checked all coefficient-admissible prefix cells with

\[
1\le h\le8,
\qquad
1\le m\le12,
\]

whenever

\[
2^m>\frac54 3^q.
\]

Across

\[
\boxed{204}
\]

`(h,q,m)` cases, every canonical prefix state satisfied

\[
P\xi=y+tN,
\qquad
0\le t<P,
\]

and

\[
0\le\xi-tN/P<5/4.
\]

The check used exact integer/modular arithmetic; the displayed rational comparison was exact inside Wolfram.