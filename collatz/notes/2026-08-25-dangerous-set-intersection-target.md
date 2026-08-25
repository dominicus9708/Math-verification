# Dangerous-set intersection target for the ternary core

Date: 2026-08-25

Status: **safe conditional reduction**. This note does not prove the needed cross-base discrepancy estimate. It identifies a quantitatively sufficient estimate and the exact entropy constant it must beat.

## 1. Dangerous dyadic set

For accelerated Collatz coefficient stopping, define

\[
D_j=\{r\bmod 2^j:\tau_c(r)>j\}.
\]

Each length-j parity word corresponds to exactly one residue modulo `2^j`, and membership in `D_j` means that every prefix satisfies

\[
3^{q_t}\ge 2^t,
\qquad 1\le t\le j.
\]

Let

\[
p=\log_3 2\approx0.6309297535714574.
\]

In particular every word in `D_j` has final odd count

\[
q_j\ge pj.
\]

Therefore, ignoring the stronger prefix constraints only enlarges the set and gives

\[
|D_j|
\le
\sum_{q\ge pj}\binom jq.
\]

For `p>1/2`, the standard binomial-entropy/Chernoff bound yields

\[
\boxed{|D_j|\le 2^{H_2(p)j}},
\]

where

\[
H_2(p)
=-p\log_2p-(1-p)\log_2(1-p).
\]

Numerically,

\[
H_2(p)=0.9499555271883305\ldots
\]

and hence

\[
\boxed{1-H_2(p)=0.05004447281166946\ldots}.
\]

Thus the ambient dangerous-set density has the rigorous upper bound

\[
\boxed{
\frac{|D_j|}{2^j}
\le
2^{-(1-H_2(p))j}.
}
\]

## 2. Ternary selector measure

Let `mu_m` be the uniform probability measure on the `2^m` points of `F_m`, reduced modulo `2^j`.

The number of depth-m selector starts surviving coefficient contraction through j steps is

\[
A(m,j)
=2^m\mu_m(D_j).
\]

The exact atom floor is

\[
A(m,j)\ge1
\iff
\mu_m(D_j)\ge2^{-m}.
\]

Therefore proving

\[
\mu_m(D_j)<2^{-m}
\]

forces

\[
A(m,j)=0.
\]

## 3. Sufficient structured-discrepancy theorem

Full dyadic equidistribution of the selector measure is unnecessary.

It is enough to prove, along a linear scale `j=Cm`, a dangerous-set-specific estimate

\[
\boxed{
\mu_m(D_j)
\le
2^{\varepsilon m}
\frac{|D_j|}{2^j}
}
\]

for some fixed `epsilon>=0` (or more generally a subexponential loss `2^{o(m)}`).

Combining with the entropy bound gives

\[
A(m,j)
\le
2^{m+\varepsilon m-(1-H_2(p))j}.
\]

Set

\[
j=Cm.
\]

Then

\[
A(m,Cm)
\le
2^{\left(1+\varepsilon-C(1-H_2(p))\right)m}.
\]

Hence if

\[
\boxed{
C>
\frac{1+\varepsilon}{1-H_2(\log_3 2)},
}
\]

the exponent is negative and for all sufficiently large m the integer count satisfies

\[
A(m,Cm)<1,
\]

so in fact

\[
\boxed{A(m,Cm)=0.}
\]

This gives the linear stopping bound

\[
\boxed{L_F(m)<Cm}
\]

eventually, and therefore

\[
\boxed{M_F(m)=O(m)}.
\]

## 4. Exact threshold constant

With zero exponential loss (`epsilon=0`),

\[
\boxed{
C_*=
\frac1{1-H_2(\log_3 2)}
=19.98222668391899\ldots
}
\]

So any dangerous-set discrepancy theorem with only subexponential loss would imply

\[
L_F(m)\le(19.9822267+o(1))m
\]

at the entropy scale.

For comparison, an exponential discrepancy loss `2^{epsilon m}` changes the sufficient slope to

| epsilon | sufficient C |
|---:|---:|
| 0 | 19.98222668 |
| 0.01 | 20.18204895 |
| 0.02 | 20.38187122 |
| 0.05 | 20.98133802 |
| 0.10 | 21.98044935 |

## 5. Why this is narrower than full mixing

The earlier support-size barrier proves that a `2^m`-point selector measure cannot have small global Fourier energy on a much larger dyadic space when `j>>m`.

That obstruction does **not** rule out the estimate above, because the estimate asks only for correlation with one special structured set `D_j`.

Thus the remaining problem is not

\[
\text{selector is uniformly distributed modulo }2^j,
\]

but rather

\[
\boxed{
\text{selector does not correlate exponentially strongly with }D_j.
}
\]

This is precisely the spectral-complementarity / cross-base intersection problem identified by the previous audits.

## 6. DSD logic chain

The reduction can be written as:

1. ternary selector channel has exactly `2^m` atoms;
2. coefficient-survivor channel occupies at most `2^{H_2(p)j}` dyadic states;
3. atom floor converts sufficiently small probability into exact emptiness;
4. the only missing link is a cross-channel correlation bound;
5. any subexponential correlation loss closes the core at every slope `C>C_*`.

In compact form,

\[
\boxed{
\text{entropy deficit}
+
\text{cross-base nonconcentration}
+
\text{atom floor}
\Longrightarrow
M_F(m)=O(m).
}
\]

## 7. Relation to the current proof target

The target `M_F(m)=O(m)` is much stronger than the previously recorded sufficient asymptotic condition

\[
\limsup_{m\to\infty}
\frac{\log_2 M_F(m)}m
<
\frac{\log_2 3}{8.616}.
\]

Therefore a proof of the dangerous-set intersection estimate above would close the current ternary-core stopping problem with considerable margin.

What remains open is the cross-base estimate itself.
