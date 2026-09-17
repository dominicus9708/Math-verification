# MATH-196 — scalar first-crossing gate recovers the first universal Farey frontier

Date: 2026-09-18

Status: `EXACT STRUCTURAL THEOREM / FIRST SCALAR-HARD CROSSING IDENTIFIED / FIRST-CELL EMPTINESS OPEN`

## 1. Purpose

MATH-194/195 showed that many first coefficient crossings descend from a source-independent scalar defect bound. The older verified-floor branch independently defined the first universal crossing through a Farey strip and found

\[
(A_0,q_0)=(114208327604,72057431991).
\]

This note proves that these are not two unrelated frontiers. The new scalar gate fails for the first time at exactly the old first universal Farey cell.

This identifies where same-integer address/Hensel structure first becomes necessary; it does **not** prove first-cell emptiness.

## 2. First-crossing coordinates

Let

\[
B_0=2^{71}.
\]

At the first coefficient failure, let `A` be the shortcut depth after the failing even step and `q` the odd count. Immediately before that even step the coefficient survives, so

\[
2^{A-1}\le3^q<2^A.
\]

Thus

\[
\boxed{A=\lceil q\log_2 3\rceil}
\]

and

\[
\boxed{
\rho-1=\frac{2^A}{3^q}-1>0.
}
\]

MATH-053 gives the source-independent correction envelope

\[
\boxed{
S\le S_\partial(q):=rac13\sum_{n=0}^{q-1}\Omega_n<\frac q3.
}
\]

Therefore every source `N>=B0` descends at that first crossing whenever

\[
\boxed{
\Gamma(q):=B_0\left(\frac{2^A}{3^q}-1\right)-S_\partial(q)>0.
}
\]

Call a first-crossing coordinate **scalar-hard** when `Gamma(q)<=0`, i.e. this source-independent test does not certify all starts simultaneously.

## 3. Scalar-hard implies the old Farey strip

Suppose `Gamma(q)<=0`. Then

\[
0<\frac{2^A}{3^q}-1
\le\frac{S_\partial(q)}{B_0}
<\frac{q}{3B_0}.
\]

Put

\[
x=\frac1{3B_0}>0.
\]

Then

\[
\frac{2^A}{3^q}<1+qx.
\]

Taking `q`-th roots and using Bernoulli's inequality

\[
1+qx\le(1+x)^q
\]

gives

\[
2^{A/q}<3(1+x)=3+\frac1{B_0}.
\]

Since first failure also gives `2^(A/q)>3`,

\[
\boxed{
3<2^{A/q}<3+B_0^{-1}.
}
\]

Taking logarithms and reciprocals,

\[
\boxed{
\frac{\ln2}{\ln(3+B_0^{-1})}
<\frac qA
<\frac{\ln2}{\ln3}.
}
\]

Define

\[
\beta:=\frac{\ln2}{\ln(3+B_0^{-1})},
\qquad
\alpha:=\frac{\ln2}{\ln3}.
\]

Then every scalar-hard first crossing lies in exactly the old verified-floor Farey strip

\[
\boxed{\beta<q/A<\alpha.}
\]

Thus the new DSD scalar gate and the old Farey construction are looking at the same Diophantine obstruction.

## 4. Canonical Farey neighbors

The canonical verified-floor certificate uses

\[
\frac{P_L}{Q_L}
=\frac{6586818670}{10439860591},
\qquad
\frac{P_U}{Q_U}
=\frac{65470613321}{103768467013},
\]

with

\[
\frac{P_L}{Q_L}<\beta<\alpha<\frac{P_U}{Q_U}
\]

and the unimodular relation

\[
\boxed{P_UQ_L-P_LQ_U=1.}
\]

Their mediant is

\[
\frac{P_L+P_U}{Q_L+Q_U}
=\frac{q_0}{A_0},
\]

where

\[
\boxed{
(A_0,q_0)
=(114208327604,72057431991).
}
\]

The standard Farey-neighbor theorem says that every reduced rational strictly between the two neighbors has denominator at least

\[
Q_L+Q_U=A_0.
\]

A scalar-hard first crossing has `q/A` inside the smaller open strip `(beta,alpha)`, hence between those neighbors. Reducing `q/A` if necessary therefore gives

\[
\boxed{A\ge A_0.}
\]

Consequently **every first coefficient failure with `A<A0` is scalar-safe**; no address/Hensel analysis is needed there.

If `A=A0`, reduction cannot lower the denominator (otherwise it would contradict minimality), and equality in the Farey denominator theorem forces the mediant. Hence the unique possible scalar-hard coordinate at the first depth is

\[
\boxed{(A,q)=(A_0,q_0).}
\]

## 5. The scalar gate really does fail at the mediant

It remains to show that `(A0,q0)` is not merely the first *possible* strip point but actually defeats the exact phase-envelope scalar gate.

The normalized phase map satisfies, for every consecutive pair,

\[
\boxed{\Omega_n+\Omega_{n+1}>\frac76.}
\]

Indeed:

- if `Omega_n>3/4`, then `Omega_(n+1)=2 Omega_n/3` and the sum is `>5/4`;
- if `Omega_n<=3/4`, then `Omega_(n+1)=4 Omega_n/3` and, since `Omega_n>1/2`, the sum is `>7/6`.

The canonical

\[
q_0=72057431991
\]

is odd. Pairing the first `q0-1` phases and using the final phase `>1/2` gives

\[
\sum_{n=0}^{q_0-1}\Omega_n
>
\frac{7(q_0-1)}{12}+\frac12
=
\frac{7q_0-1}{12}.
\]

Therefore

\[
\boxed{
S_\partial(q_0)>\frac{7q_0-1}{36}.
}
\]

A rigorous rational-log interval certificate verifies

\[
\boxed{
B_0\left(\frac{2^{A_0}}{3^{q_0}}-1\right)
<\frac{7q_0-1}{36}.
}
\]

Hence

\[
\boxed{
\Gamma(q_0)<0.
}
\]

So the source-independent exact phase-envelope gate indeed fails at the canonical mediant.

Combining with Section 4:

\[
\boxed{
(A_0,q_0)
\text{ is exactly the first scalar-hard first-crossing coordinate.}
}
\]

## 6. Relation to the old `buffered_B=72` result

The older verified-floor certificate independently found

\[
\operatorname{buffered\_B}(A_0,q_0)=72.
\]

This means the coarser envelope `S<q/3` needs one more source bit than the frozen `B0=2^71` floor to force descent at the first cell.

MATH-196 strengthens the interpretation: even after replacing `q/3` by the sharper phase envelope `S_partial(q)`, the same `(A0,q0)` remains the first unresolved scalar coordinate.

Thus the Farey frontier is not an artifact of the earlier coarse correction bound.

## 7. DSD consequence

The proof architecture now separates cleanly:

\[
\boxed{
A<A_0:
\text{ scalar first-crossing gate closes every source}
}
\]

and

\[
\boxed{
A=A_0,\ q=q_0:
\text{ first genuinely structural cell requiring address/Hensel information.}
}
\]

This explains why the old first-cell branch and the newer MATH-188--193 product-state branch meet at the same point.

The expensive same-integer machinery is not needed to *discover* the first hard coordinate. It is needed only to decide whether the unique first hard cell is actually empty.

## 8. Consequence for r=1..21 / depth 2..41 work

MATH-194 already closes every first coefficient failure occurring inside depth 41. MATH-196 shows the much stronger global reason: the first scalar-hard coefficient crossing cannot occur until depth

\[
A_0=114208327604.
\]

Thus the finite `k=2..41` product system is entirely inside the scalar-safe pre-Farey region as far as *first coefficient failure* is concerned.

Its Hensel/address states remain useful for coefficient-surviving structural compression and for regression against the historical proof tree, but not because a first coefficient failure inside that range could itself be dangerous.

## 9. Claim boundary

Established:

- scalar-hard first crossing implies membership in the canonical verified-floor Farey strip;
- Farey-neighbor minimality forces every scalar-hard crossing to have `A>=A0`;
- the unique possible scalar-hard coordinate at `A=A0` is `(A0,q0)`;
- exact two-phase lower bound plus rigorous logarithm intervals gives `Gamma(q0)<0`;
- therefore `(A0,q0)` is exactly the first failure of the source-independent phase-envelope scalar gate.

Not established:

- that any ordinary source in the first cell actually survives all address/Hensel/defect tests;
- first-cell emptiness;
- arbitrary later Farey-cell closure;
- closure of `r=10` by itself;
- the Collatz conjecture.

## Reproducibility

Companion certificate:

`collatz/src/2026_09_18_math196_scalar_gate_farey_frontier_certificate.py`
