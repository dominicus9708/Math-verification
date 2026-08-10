# Unresolved-set channel escape formulation for Collatz

Date: 2026-08-11

Status: **exact set-theoretic reformulation + proved channel-rank lemmas + revised global target**. This note supersedes the earlier use of Terras's coefficient-stopping-time conjecture as a required main proposition. It does not claim a proof of the Collatz conjecture.

## 1. Actual unresolved sets

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

define, for each depth \(k\ge0\),

\[
\boxed{
U_k
:=
\{n\in\mathbb N:n\ge2,\ T^j(n)\ge n\text{ for every }1\le j\le k\}.
}
\]

Thus \(U_k\) is the set of positive integers whose orbit has not yet fallen below its own starting value by time \(k\).

The sets are nested:

\[
\boxed{U_{k+1}\subseteq U_k.}
\]

Moreover,

\[
\boxed{
\bigcap_{k\ge0}U_k
=
\{n\ge2:\tau(n)=\infty\},
}
\]

where

\[
\tau(n)=\min\{j\ge1:T^j(n)<n\}.
\]

Since finite first descent for every \(n>1\) is equivalent to the Collatz conjecture by strong induction,

\[
\boxed{
\text{Collatz}
\Longleftrightarrow
\bigcap_{k\ge0}U_k=\varnothing.
}
\]

This is the master set statement. It makes no coefficient-stopping-time assumption.

---

## 2. Exact finite channel decomposition at fixed time

At depth \(k\), partition the positive integers by residue modulo \(2^k\):

\[
n=r+2^k m.
\]

For a fixed realizable residue channel, the exact prefix identity gives, for every \(j\le k\),

\[
T^j(r+2^k m)-(r+2^k m)
=A_{j,k}(r)+B_{j,k}(r)m,
\]

with

\[
A_{j,k}(r)=T^j(r)-r,
\]

\[
B_{j,k}(r)=2^{k-j}(3^{q_j(r)}-2^j).
\]

Therefore the unresolved parameter set in one residue channel is a finite intersection of affine half-lines and hence an integer interval:

\[
\boxed{
I_k(r)=[L_k(r),U_k(r)]\cap\mathbb Z,
}
\]

where \(U_k(r)\) may be \(+\infty\).

For a nonempty channel \(\mathfrak s\), define the represented set

\[
\mathcal N(\mathfrak s)
=
\{r+2^k m:m\in I_k(r)\}.
\]

Then

\[
\boxed{
U_k
=
\bigsqcup_{\mathfrak s\in\mathscr C_k}\mathcal N(\mathfrak s),
}
\]

where \(\mathscr C_k\) is a finite collection of nonempty unresolved channels.

Thus an infinite set of integers is represented exactly by finitely many arithmetic-interval channels on every fixed time slice.

---

## 3. Exact channel dynamics and complement removal

A channel at depth \(k\) splits according to the next binary lift bit \(c\in\{0,1\}\). Writing

\[
m=c+2m',
\]

the child channel represents only integers already represented by the parent. After applying the exact Collatz attribute update and intersecting with the new no-descent half-line, an empty child is removed.

Hence for every nonempty child \(\mathfrak s'\) of \(\mathfrak s\),

\[
\boxed{
\mathcal N(\mathfrak s')\subseteq\mathcal N(\mathfrak s).
}
\]

This is the set-theoretic form of

\[
\text{formed state}
\to
\text{static aggregate}
\to
\text{attribute update}
\to
\text{dynamic refinement}
\to
\text{complement removal}.
\]

---

## 4. Minimal representative rank

For a nonempty channel define

\[
\boxed{
\rho(\mathfrak s)
:=
\min\mathcal N(\mathfrak s)
=
r+2^k L_k(r).
}
\]

Because every child represents a subset of its parent,

\[
\boxed{
\mathfrak s\to\mathfrak s'
\Longrightarrow
\rho(\mathfrak s')\ge\rho(\mathfrak s).
}
\]

Thus \(\rho\) is an exact nondecreasing rank along every unresolved channel path.

This rank is not required to increase at every step. Long plateaus are allowed. What matters is whether a path can keep \(\rho\) bounded forever.

---

## 5. Channel Escape Equivalence Theorem

Consider an infinite nested unresolved path

\[
\mathfrak s_0\to\mathfrak s_1\to\mathfrak s_2\to\cdots.
\]

The following statements are equivalent:

1. the Collatz conjecture is true;
2. \(\bigcap_{k\ge0}U_k=\varnothing\);
3. every infinite unresolved channel path satisfies
   \[
   \boxed{\rho(\mathfrak s_k)\to\infty;}
   \]
4. the global unresolved frontier
   \[
   \nu(k):=\min U_k
   =\min_{\mathfrak s\in\mathscr C_k}\rho(\mathfrak s)
   \]
   satisfies
   \[
   \boxed{\nu(k)\to\infty.}
   \]

### Proof of (2) iff (3)

If some integer \(n\) belongs to every \(U_k\), then its unique residue channel at each depth gives an infinite nested path whose represented sets all contain \(n\). Therefore

\[
\rho(\mathfrak s_k)\le n
\]

for all \(k\), so the channel rank does not escape.

Conversely, suppose an infinite unresolved path has bounded \(\rho\). Since \(\rho\) is a nondecreasing integer sequence, it eventually stabilizes at some finite integer \(n\). The represented sets are nested, and once their minimum is \(n\), each contains \(n\). Hence \(n\in U_k\) for every depth, so \(n\) has infinite first-descent time.

### Proof of (2) iff (4)

The sets \(U_k\) are nested. Hence \(\nu(k)\) is nondecreasing whenever \(U_k\) is nonempty. If \(\nu(k)\) failed to diverge, it would remain bounded by some \(M\). The finite nested sets

\[
U_k\cap\{2,3,\ldots,M\}
\]

would then remain nonempty and therefore have nonempty intersection, contradicting (2). The converse is immediate.

Thus the Collatz problem is exactly a channel-rank escape problem, not a requirement to eliminate every abstract infinite 2-adic path.

---

## 6. Unbounded and bounded sectors

For one residue channel, the interval \(I_k(r)\) is unbounded if and only if every coefficient slope encountered so far is positive:

\[
3^{q_j(r)}>2^j
\qquad(1\le j\le k).
\]

Define the coefficient-surviving sector

\[
C_k
:=
\{n\ge2:3^{Q_j(n)}>2^j\text{ for every }1\le j\le k\}.
\]

Since nonnegative correction prevents actual descent while the coefficient is at least one,

\[
\boxed{C_k\subseteq U_k.}
\]

Define the post-crossing unresolved remainder

\[
\boxed{P_k:=U_k\setminus C_k.}
\]

At fixed \(k\), \(P_k\) is finite. Indeed, in every residue channel belonging to \(P_k\), at least one affine no-descent condition has negative slope, which places a finite upper bound on \(m\); there are only finitely many residue channels at depth \(k\).

Thus

\[
\boxed{U_k=C_k\sqcup P_k,}
\]

where \(C_k\) is the unbounded coefficient-surviving tail sector and \(P_k\) is a finite bounded post-crossing sector.

Once a channel becomes bounded, all of its descendants remain bounded because every descendant represents a subset of the finite parent set. Hence the channel-type transition

\[
\text{unbounded}\to\text{bounded}
\]

can occur at most once along a path, and

\[
\text{bounded}\to\text{unbounded}
\]

is impossible.

---

## 7. Relation to the coefficient-stopping-time conjecture

The statement that coefficient stopping always coincides with actual stopping is Terras's coefficient-stopping-time (CST) conjecture.

In the present set language, CST would force the bounded post-crossing sector to be empty:

\[
P_k=\varnothing
\qquad\text{for every }k.
\]

That is stronger than what the Collatz proof requires.

The channel-escape formulation permits bounded post-crossing islands to exist. It only requires that no fixed finite integer can remain in them forever.

Define

\[
\mu(k)=\min C_k
\]

when \(C_k\ne\varnothing\), and

\[
\pi(k)=\min P_k
\]

with \(\pi(k)=+\infty\) when \(P_k=\varnothing\). Then

\[
\boxed{
\nu(k)=\min\{\mu(k),\pi(k)\}.
}
\]

Therefore a sufficient and in fact equivalent sector-wise formulation is

\[
\boxed{
\mu(k)\to\infty
\quad\text{and}\quad
\pi(k)\to\infty.
}
\]

This is strictly weaker than demanding \(P_k=\varnothing\) at all depths.

---

## 8. Revised master proposition

The previous two-proposition architecture based on

\[
\tau=\tau_c
\]

and

\[
\mu(k)\to\infty
\]

is retained as a possible sufficient route, but it is no longer the primary architecture because the first statement is the independent CST conjecture.

The primary target is now one exact proposition.

### Master Proposition — Unresolved Channel Escape

For every infinite path in the exact first-descent interval-channel tree,

\[
\boxed{
\rho(\mathfrak s_k)\to\infty.
}
\]

Equivalently,

\[
\boxed{
\nu(k)=\min U_k\to\infty.
}
\]

The coefficient-surviving tree, bounded post-crossing islands, endpoint quotient, carry/wrap channels, and first-merge dominance are auxiliary structures for proving rank escape; none is individually required to vanish.

---

## 9. What must be found next

The next useful theorem should not be another finite-depth exclusion. It should be a structural mechanism forcing rank escape. Candidate forms include:

1. a channel potential \(\Phi\) on a well-founded ordered set such that every bounded-\(\rho\) path must strictly decrease \(\Phi\) after finitely many transitions;
2. a block theorem showing that a channel whose rank remains below \(R\) can survive for at most an explicit finite function \(F(R)\) of steps;
3. a dominance/quotient theorem showing that every bounded-rank channel is eventually represented by a strictly smaller finite family of canonical states;
4. a sector theorem proving separately that the unbounded frontier \(\mu(k)\) and bounded frontier \(\pi(k)\) both escape.

The computational records accumulated so far should be used to discover or falsify such a structural mechanism, not to extend the depth indefinitely.
