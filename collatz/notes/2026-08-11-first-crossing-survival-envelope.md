# First-crossing survival envelope and extremal correction bound

Date: 2026-08-11

Status: **derived extremal bound using coefficient-survival prefix constraints and parity-word majorization**. This note gives a sufficient boundary criterion for first-crossing descent. It does not prove Terras's coefficient-stopping-time conjecture or the Collatz conjecture.

## 1. Crossing layers indexed by odd-count q

Let

\[
\beta:=\log_2 3,
\qquad
\alpha:=\log_3 2=\beta^{-1},
\]

and define

\[
\boxed{\kappa(q):=\lfloor q\beta\rfloor.}
\]

Then

\[
2^{\kappa(q)}<3^q<2^{\kappa(q)+1}.
\]

Hence a first coefficient crossing with exactly \(q\) odd steps occurs, if realizable, on the even step from predecessor depth

\[
\boxed{j=\kappa(q)}
\]

to child depth \(j+1\).

At the predecessor depth the coefficient is greater than one,

\[
\frac{3^q}{2^j}>1,
\]

while after the forced even step it is less than one,

\[
\frac{3^q}{2^{j+1}}<1.
\]

---

## 2. Prefix-survival lower envelope

Let a parity word of predecessor length \(j\) have cumulative odd-counts

\[
Q_t=\sum_{i=0}^{t-1}p_i,
\qquad 1\le t\le j.
\]

Coefficient survival through the predecessor depth requires

\[
3^{Q_t}>2^t
\]

for every \(t\le j\). Since \(\alpha\) is irrational, this is exactly

\[
\boxed{Q_t\ge\lceil \alpha t\rceil.}
\]

For a crossing layer with total odd-count \(q\), the total is the minimal allowed value

\[
Q_j=q=\lceil\alpha j\rceil.
\]

Define the boundary word \(W_q^*\) by

\[
Q_t^*=\lceil\alpha t\rceil.
\]

Its bits are

\[
p_{t-1}^*
=
\lceil\alpha t\rceil-
\lceil\alpha(t-1)\rceil.
\]

Equivalently, the positions of its \(q\) odd entries are

\[
\boxed{
a_i^*=\kappa(i)=\lfloor i\log_2 3\rfloor,
\qquad i=0,1,\ldots,q-1.
}
\]

Thus \(W_q^*\) delays every odd entry as far to the right as coefficient survival permits.

---

## 3. Extremal remainder under the survival constraint

Rozier and Terracol order parity vectors of equal length and equal odd-count by the prefix-sum / unordered-majorization order. In their orientation, moving a 1 to the left decreases the remainder; equivalently, a word with smaller prefix odd-counts has the larger remainder.

Every coefficient-surviving crossing predecessor word \(W\) satisfies

\[
Q_t^*\le Q_t
\]

for all proper prefixes and has the same total \(q\). Hence

\[
W_q^*\preceq W.
\]

Therefore the boundary word maximizes the correction/remainder over the entire coefficient-surviving crossing layer.

For odd positions

\[
0\le a_0<a_1<\cdots<a_{q-1}<j,
\]

the correction numerator is

\[
R
=
\sum_{i=0}^{q-1}
3^{q-1-i}2^{a_i}.
\]

Consequently,

\[
\boxed{
R\le R_q^*
:=
\sum_{i=0}^{q-1}
3^{q-1-i}2^{\kappa(i)}.
}
\]

This is an exact extremal bound for the coefficient-surviving first-crossing predecessor family.

A coarse consequence follows from

\[
2^{\kappa(i)}<3^i:
\]

\[
\boxed{R_q^*<q\,3^{q-1}.}
\]

---

## 4. Crossing gap and descent criterion

Let

\[
j=\kappa(q),
\qquad
D_q:=2^{j+1}-3^q>0.
\]

The crossing step is even, so the correction numerator does not change. Thus every first-crossing candidate satisfies

\[
T^{j+1}(n)
=
\frac{3^q n+R}{2^{j+1}}.
\]

Actual descent at the crossing is equivalent to

\[
\boxed{D_q n>R.}
\]

Since \(R\le R_q^*\), the entire \(q\)-crossing layer descends whenever

\[
\boxed{
n>
H_q
:=
\frac{R_q^*}{D_q}.
}
\]

Therefore \(H_q\) is an explicit structural danger threshold: any counterexample to first-crossing descent with odd-count \(q\) must start at or below \(H_q\).

---

## 5. Crossing frontier

Define the realizable crossing frontier

\[
\chi(q)
:=
\min\{n>1:
\text{n reaches its first coefficient crossing with q odd steps}\},
\]

with \(\chi(q)=+\infty\) if the crossing layer is unrealized.

Then the sufficient layer criterion is

\[
\boxed{
\chi(q)>H_q
\Longrightarrow
\text{every realizable first crossing in the q-layer is an actual descent}.
}
\]

This criterion deliberately separates two tasks:

1. \(R_q^*\) and \(H_q\) are explicit functions of the boundary parity word;
2. \(\chi(q)\) is a set-frontier quantity of the exact realizable channel system.

It is stronger than necessary because the word achieving \(R_q^*\) need not be the word achieving \(\chi(q)\), but it replaces enumeration of every crossing word by one extremal correction bound plus one frontier estimate.

---

## 6. Relation to the unresolved-set master proposition

Terras's coefficient-stopping-time conjecture would require first-crossing descent for every \(q\)-layer. The unresolved-set channel-escape formulation does not require this conjecture: bounded post-crossing channels may be retained and handled dynamically.

Nevertheless, the survival-envelope bound is useful in two ways:

- any layer satisfying \(\chi(q)>H_q\) can be removed from the bounded-sector analysis entirely;
- the explicit threshold identifies which Diophantine crossing layers can even be dangerous before any Collatz trajectory is enumerated.

Thus this note is an auxiliary boundary-reduction tool for the master rank-escape problem, not a replacement for it.

## 7. Literature alignment

The parity-word partial order and monotonicity of the remainder used in Section 3 are taken from Olivier Rozier and Claude Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167; arXiv:2502.00948. The present use adds the coefficient-survival lower-envelope constraint before applying that order.
