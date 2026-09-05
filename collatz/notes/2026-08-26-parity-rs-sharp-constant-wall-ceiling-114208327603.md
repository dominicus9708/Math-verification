# Sharp constant-wall parity-RS coefficient gate through depth 114,208,327,603

Date: 2026-08-26

Status: exact finite theorem after taking Barina's published verification below \(2^{71}\) as an external finite input. This supersedes the earlier 17,087,914-step rational-wall gate. It is not a proof of the Collatz conjecture.

## 1. Two critical slopes

Let

\[
B=2^{71},
\qquad
A=3+\frac1B.
\]

Define

\[
\beta:=\log_A2,
\qquad
\alpha:=\log_3 2.
\]

Since \(A>3\),

\[
\beta<\alpha.
\]

A constant parity-RS wall

\[
dQ_j>pj
\]

is valid from the finite base \(B\) whenever

\[
A^p<2^d,
\]
that is,

\[
\frac pd<\beta.
\]

To force coefficient survival at depth \(j\), the same wall must imply

\[
Q_j\ge\lceil\alpha j\rceil.
\]

Thus the exact problem is to understand the rational gap between \(\beta\) and \(\alpha\).

## 2. A much closer valid lower wall

Take

\[
\boxed{
\frac pd
=
\frac{6,586,818,670}{10,439,860,591}.
}
\]

The companion certificate uses the positive expansion

\[
\log x
=
2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad
z=\frac{x-1}{x+1},
\]

with an explicit geometric tail upper bound. Using only exact `Fraction` arithmetic and 35 terms, it proves

\[
p\log A<d\log2.
\]

Therefore

\[
\boxed{p/d<\beta},
\]
so the ballot sets

\[
V_m=
\{n:dQ_j(n)>pj\ \forall j\le m\}
\]

are recursively sufficient for every finite \(m\), conditional only on the published finite verification below \(2^{71}\).

## 3. Farey neighbour above the exact coefficient slope

Take

\[
\boxed{
\frac uv
=
\frac{65,470,613,321}{103,768,467,013}.
}
\]

The same rigorous logarithm bounds prove

\[
\alpha<\frac uv.
\]

Moreover

\[
\boxed{ud-pv=1}.
\]

Hence \(p/d\) and \(u/v\) are Farey neighbours.

Their mediant is

\[
\frac{P}{Q}
=
\frac{p+u}{d+v}
=
\boxed{
\frac{72,057,431,991}{114,208,327,604}
}.
\]

Exact rational logarithm bounds prove the stronger placement

\[
\boxed{
\beta<\frac PQ<\alpha.
}
\]

Thus \(P/Q\) is an actual rational lying in the narrow adjusted-vs-exact critical strip.

## 4. Exact coefficient gate

Because \(p/d\) and \(u/v\) are Farey neighbours, every rational strictly between them has denominator at least

\[
d+v=Q=114,208,327,604.
\]

For every integer

\[
1\le j<Q,
\]
there can therefore be no rational \(n/j\) satisfying

\[
\frac pd<\frac nj<\alpha.
\]

Hence

\[
\boxed{
\left\lfloor\frac{pj}{d}\right\rfloor
=
\lfloor\alpha j\rfloor
\qquad(1\le j\le Q-1).
}
\]

The valid RS wall

\[
dQ_j>pj
\]
therefore yields

\[
Q_j\ge
\left\lfloor\frac{pj}{d}\right\rfloor+1
=
\lfloor\alpha j\rfloor+1
=
\lceil\alpha j\rceil.
\]

Thus every hypothetical minimal counterexample satisfies

\[
\boxed{
3^{Q_j}\ge2^j
\qquad
1\le j\le114,208,327,603.
}
\]

This extends the previous 17,087,914-step theorem by a factor of about \(6684\), and the original 301,993-step gate by more than five orders of magnitude.

## 5. Sharpness for every single constant RS wall at base \(2^{71}\)

This is stronger than sharpness of one chosen rational.

At

\[
Q=114,208,327,604,
\]
the mediant satisfies

\[
\beta<\frac PQ<\alpha.
\]

Therefore every valid constant parity-RS slope \(r<\beta\) obeys

\[
rQ<P<\alpha Q.
\]

So the RS lower bound at this depth cannot force the coefficient threshold \(\lceil\alpha Q\rceil\).

Consequently

\[
\boxed{
114,208,327,603
}
\]
is the **maximum possible coefficient-survival horizon obtainable from the finite base \(B=2^{71}\) using only one constant linear parity-RS wall**.

This is a methodological ceiling, not a Collatz obstruction. It says that to go farther one must add information beyond a single adjusted-average odd-density inequality.

## 6. Survivor-Hensel maximality remains valid throughout the full gate

The survivor-Hensel credit theorem gives, for two coefficient-surviving same-\(Q_H\) Hensel siblings,

\[
0<d_{\rm root}<\frac{Q_H}{3}\le\frac H3.
\]

For

\[
H\le114,208,327,603
\]
we have

\[
\frac H3<4\times10^{10}\ll2^{71}<N
\]
for every hypothetical minimal counterexample \(N\).

Hence every positive survivor-sibling credit produces a genuine smaller positive root. Therefore throughout the entire sharp constant-wall horizon a minimal counterexample must use the maximum-correction representative in its same-\(Q_H\), same-Hensel survivor class.

The fixed-endpoint multiplicity consequently remains only

\[
O(H),
\]
with information cost

\[
O(\log H)=o(H).
\]

## 7. DSD audit and next branch

The proof-valid global binary chain is now

\[
\boxed{
2^{71}\text{ finite base}
\to
\text{parity RS}
\to
\text{coefficient survival through }114,208,327,603
\to
\text{survivor-Hensel maximality}
\to
O(H)\text{ endpoint fibre}.
}
\]

No ternary selector family and no repeated local L7/L14 pullback occurs.

The constant-wall parity-RS route is now exhausted sharply at this finite base. The next proof-level route must use at least one of:

1. the exact affine remainder at a first coefficient crossing;
2. a state-dependent or multi-wall RS condition rather than a single constant slope;
3. survivor-Hensel/endpoint structure strong enough to force merge or descent before the sharp horizon;
4. a larger independently verified finite base.

The immediate next target is the first option because the mechanical first-crossing envelope is already an unconditional parity-domain theorem.

Certificate:

`collatz/src/parity_rs_farey_sharp_ceiling_114208327603_certificate.py`.
