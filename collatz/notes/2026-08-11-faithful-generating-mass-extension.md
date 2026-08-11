# Faithful generating-mass extension for Collatz survivor sets

Date: 2026-08-11

Status: **exact parameterized aggregation theorem**. This note extends the dyadic mass construction; it does not claim a proof of Collatz.

## 1. Full-support geometric family

For any fixed

\[
0<z<1,
\]

define

\[
\boxed{
w_n(z):=(1-z)z^{n-2},\qquad n\ge2.
}
\]

Then

\[
\sum_{n=2}^{\infty}w_n(z)=1
\]

and every singleton has strictly positive mass.

For \(A\subseteq\mathbb N_{\ge2}\), define

\[
\mu_z(A):=\sum_{n\in A}w_n(z).
\]

Thus

\[
\mu_z(A)=0\iff A=\varnothing.
\]

For the unresolved sets

\[
U_k=\{n\ge2:T^j(n)\ge n\text{ for }1\le j\le k\},
\]

define

\[
\boxed{M_k(z):=\mu_z(U_k).}
\]

Because \(U_k\) decreases and \(\mu_z(U_0)=1\), continuity from above gives

\[
\boxed{
\text{Collatz}
\iff
M_k(z)\to0
}
\]

for every fixed \(z\in(0,1)\). In fact proving the limit for any single such \(z\) is sufficient.

---

## 2. Faithfulness to the frontier

Let

\[
\nu(k)=\min U_k
\]

when \(U_k\neq\varnothing\). Then

\[
\boxed{
(1-z)z^{\nu(k)-2}
\le
M_k(z)
\le
z^{\nu(k)-2}.
}
\]

The lower bound is the weight of the frontier element itself; the upper bound is the full geometric tail beginning at the frontier.

Thus \(M_k(z)\to0\) iff \(\nu(k)\to\infty\). The aggregation cannot hide a finite or sparse survivor set.

For \(z=1/2\), this reduces to

\[
2^{1-\nu(k)}\le M_k\le2^{2-\nu(k)}.
\]

---

## 3. Exact channel generating mass

For a channel

\[
\llbracket s\rrbracket
=\{r+2^k m:L\le m\le U\},
\]

if \(U<\infty\),

\[
\boxed{
\mu_z(s)
=
(1-z)z^{r+2^kL-2}
\frac{1-z^{2^k(U-L+1)}}{1-z^{2^k}}.
}
\]

If \(U=+\infty\),

\[
\boxed{
\mu_z(s)
=
\frac{(1-z)z^{r+2^kL-2}}{1-z^{2^k}}.
}
\]

Thus every finite or infinite interval channel has an exact rational generating-mass expression in \(z\).

Equivalently, without normalization one may use the survivor generating function

\[
G_k(z):=\sum_{n\in U_k}z^n,
\]

for which each channel contributes a geometric rational term.

---

## 4. Parameterized hazards

For an exact survivor channel \(s\), define the \(z\)-mass of its surviving children by

\[
\mu_z^+(s)
:=
\sum_{s'\in\mathrm{Ch}(s)}\mu_z(s').
\]

The local \(z\)-hazard is

\[
\boxed{
\eta_z(s)
:=1-\frac{\mu_z^+(s)}{\mu_z(s)}.
}
\]

The global hazard is

\[
\bar\eta_k(z)
=
\sum_{s\in K_k}
\frac{\mu_z(s)}{M_k(z)}\eta_z(s),
\]

and exactly

\[
\boxed{
M_{k+1}(z)
=
\bigl(1-\bar\eta_k(z)\bigr)M_k(z).
}
\]

Therefore the choice of \(z\) is a free analytic parameter that may be optimized to make a symbolic transfer or Lyapunov inequality contractive.

---

## 5. Transfer-operator target

Given a dynamically closed attribute map \(\Phi(s)=a\), define the attribute-mass vector

\[
m_k(a;z)
:=
\sum_{\Phi(s)=a}\mu_z(s).
\]

A universal proof may seek a nonnegative symbolic transfer majorant

\[
\mathbf m_{k+1}(z)
\le
P(z)\mathbf m_k(z)
\]

whose entries are proved for entire attribute classes.

If for some \(z\in(0,1)\) there exist \(v>0\) and \(\lambda<1\) such that

\[
v^\top P(z)\le\lambda v^\top,
\]

then \(M_k(z)\to0\), hence Collatz.

The parameter \(z\) is not a numerical cutoff. It is a fixed transform parameter in a full-support measure over all natural numbers.

---

## 6. Interpretation

This family formalizes the integral/generating-function intuition:

\[
\text{infinitely many starting integers}
\longrightarrow
\text{one exact analytic aggregate }M_k(z),
\]

while preserving the logical fact that even a single fixed survivor has positive mass. The unresolved mathematical task is not summation; it is to construct a finite or otherwise controlled attribute transfer whose universal symbolic bounds force the aggregate to vanish.
