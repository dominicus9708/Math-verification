# Two-channel successor Bellman recurrence

Date: 2026-08-09

Status: **DERIVED EXACT RECURRENCE + INDEPENDENT SMALL-DEPTH CHECK**

This note gives a dual / backward form of the finite-horizon min-plus transfer.  It is an exact reformulation of the coefficient-survivor problem, not a proof of the Collatz conjecture.

## 1. Transformed future set

For target depth `K`, split depth `k`, remaining horizon `m=K-k`, and current odd-count `q`, let

\[
A_{k,q,m}\subset\mathbb Z/2^m\mathbb Z
\]

be the future suffix residues that preserve the coefficient barrier.

Define

\[
\boxed{
S_{k,q,m}=3^{-q}A_{k,q,m}\pmod{2^m}.
}
\]

For a transformed endpoint query

\[
\xi=3^{-q}y\pmod{2^m},
\]

define the cyclic successor value

\[
\boxed{
J_{k,q,m}(\xi)
=
\min_{s\in S_{k,q,m}}[s-\xi]_{2^m}.
}
\]

By the cyclic-successor lemma, `J` is exactly the minimum future lift integer.

## 2. Exact E/O set recursion

At `m=0`,

\[
\boxed{S_{k,q,0}=\{0\}.}
\]

Let `m>=1` and `M=2^m`.

An even first suffix step is admissible iff

\[
3^q\ge2^{k+1}.
\]

Its transformed image is

\[
\boxed{
S_E=2S_{k+1,q,m-1}\pmod M.
}
\]

An odd first suffix step is admissible iff

\[
3^{q+1}\ge2^{k+1}.
\]

Put

\[
g_{q,m}=[3^{-(q+1)}]_M.
\]

Solving the odd inverse step gives the transformed image

\[
\boxed{
S_O=
2S_{k+1,q+1,m-1}-g_{q,m}
\pmod M.
}
\]

Therefore

\[
\boxed{
S_{k,q,m}=S_E\cup S_O,
}
\]

with only the barrier-admissible branches included.

The E image consists of even residues and the O image of odd residues, so the two channel images are disjoint at each node.

This recursion was independently checked in Wolfram against direct enumeration for all barrier-admissible states with `0<=k<=5` and `0<=m<=6`; no discrepancy was found.

## 3. Successor transform through an even affine image

Let `M=2^m`, `M'=2^(m-1)`, and consider a subset

\[
2U\subset\mathbb Z/M\mathbb Z.
\]

For a query `x`, put

\[
b=x\bmod2,
\qquad
h=\left\lceil\frac{x}{2}\right\rceil\pmod{M'}.
\]

Then

\[
\boxed{
\operatorname{dist}_M^+(x,2U)
=2\operatorname{dist}_{M'}^+(h,U)+b.
}
\]

This identity is just the parity decomposition of the clockwise cyclic distance.

## 4. Exact scalar Bellman recurrence

For the E channel put

\[
b_E=\xi\bmod2,
\qquad
h_E=\left\lceil\frac{\xi}{2}\right\rceil\pmod{2^{m-1}}.
\]

If E is admissible, its candidate value is

\[
\boxed{
J_E
=2J_{k+1,q,m-1}(h_E)+b_E.
}
\]

For the O channel put

\[
t=(\xi+g_{q,m})\bmod2^m,
\]

\[
b_O=t\bmod2,
\qquad
h_O=\left\lceil\frac{t}{2}\right\rceil\pmod{2^{m-1}}.
\]

If O is admissible, its candidate value is

\[
\boxed{
J_O
=2J_{k+1,q+1,m-1}(h_O)+b_O.
}
\]

Hence

\[
\boxed{
J_{k,q,m}(\xi)
=
\min\{J_E,J_O\}_{\text{admissible branches}}.
}
\]

This is an exact two-channel Bellman recurrence.  It requires no explicit construction of the suffix set `S`.

## 5. Root identity

At the root,

\[
k=0,\quad q=0,\quad \xi=0,\quad m=K.
\]

Since `S_{0,0,K}` is precisely the transformed coefficient-surviving residue set and the zero residue fails the first coefficient barrier for `K>=1`,

\[
\boxed{
\mu(K)=J_{0,0,K}(0).
}
\]

Thus the minimal-survivor function is the value of one scalar two-channel recurrence.

## 6. Relation to the forward min-plus transfer

Let

\[
D_k(q,\eta)
\]

be the forward min-plus value from `finite-horizon-minplus-transfer.md`: the smallest low-`k` canonical start reaching signature `(q,eta)`.

The backward query uses

\[
\xi=3^{-q}\eta\pmod{2^{K-k}}.
\]

Then for every split `k`,

\[
\boxed{
\mu(K)=
\min_{q,\eta}
\left[
D_k(q,\eta)
+2^kJ_{k,q,K-k}(3^{-q}\eta)
\right].
}
\]

This is an exact forward/backward min-plus pairing:

- `D_k` is the low-bit / prefix term;
- `2^k J` is the high-bit / future-lift term.

It is the precise two-term decomposition of the final canonical start at a chosen split.

## 7. Why this helps the proof program

A candidate smaller than `2^k` must have

\[
J=0.
\]

Therefore any argument that already gives a polynomial upper bound `x<U(K)` may choose

\[
k>\log_2 U(K)
\]

and reduce candidate realization to the zero-lift condition.

This recovers the conceptual content of the buffered-core / core-reconstruction route: once the low-bit core is longer than the candidate itself, the remaining parity tail is no longer an independent lift degree of freedom.

For the infinite coefficient-survival branch there is no known comparable a priori bound, so both terms remain necessary.

The structural target becomes an **anti-alignment lower bound**: prove that a state cannot simultaneously have an exceptionally small forward cost `D_k` and an exceptionally small backward lift `J` for arbitrarily large target `K`.

## 8. Independent finite checks

A memoized Wolfram implementation of the scalar recurrence gives

\[
\begin{array}{c|cccccccc}
K&5&6&7&10&15&20&24&25\\\hline
J_{0,0,K}(0)&7&7&27&27&27&27&27&27
\end{array}
\]

and additionally

\[
J_{0,0,28}(0)=27,
\qquad
J_{0,0,30}(0)=27,
\]

matching the exact minimal-survivor plateau table.

The number of distinct nonterminal memoized Bellman states visited by the same implementation was:

| K | survivor parity words | Bellman states |
|---:|---:|---:|
| 10 | 64 | 45 |
| 15 | 1,295 | 258 |
| 20 | 27,328 | 1,277 |
| 25 | 573,162 | 6,339 |
| 28 | 3,524,586 | 16,764 |
| 30 | 12,771,274 | 32,399 |

These are finite computational diagnostics.  No asymptotic state-count exponent is claimed from them.

## 9. Literature position

The finite parity-vector / residue correspondence and its 2-adic extension are classical; the current recurrence should be viewed as a constrained min-plus use of that structure, not as a new parity conjugacy theorem.

Relevant external foundations are Terras' stopping-time formulation and the Bernstein--Lagarias `3x+1` conjugacy map.  The project-derived part here is the coefficient-barrier restriction, transformed suffix-set recursion, cyclic-successor value, and its two-channel Bellman organization.

## 10. Next target

The recurrence is exact but its memoized state family may still grow exponentially.

The next proof-relevant question is not another exact rewriting.  It is to prove a uniform contraction / anti-alignment statement for the reachable Bellman states, for example one of:

1. a certified lower bound on `J` for every state with very small forward `D`;
2. a block theorem showing that only a controlled subset of transformed queries `xi` can carry near-minimal values;
3. a gap / discrepancy theorem strong enough to control the specific low-cost cyclic successor queries, rather than only average Fourier cancellation.
