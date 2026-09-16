# Cyclic-successor dominance for finite-horizon Collatz states

Date: 2026-08-09

Status: **DERIVED LEMMA + EXACT SPLIT FORMULATION + COMPUTATIONAL CHECK**

This note strengthens the finite-horizon min-plus formulation without claiming a global Collatz proof.

## 1. Split state

Fix a target depth `K` and a split depth `k`, with

\[
m=K-k.
\]

For a coefficient-surviving prefix at depth `k`, write the exact canonical state as

\[
(r,q,y),
\]

where `r` is the canonical start modulo `2^k`, `q` is the odd-count, and

\[
y=T^k(r).
\]

For any lift integer

\[
0\le C<2^m,
\]

the corresponding depth-`K` start is

\[
\boxed{r_C=r+2^kC.}
\]

The prefix affine identity gives

\[
\boxed{T^k(r+2^kC)=y+3^qC.}
\]

Thus the high `m` binary digits of the final canonical start are exactly the lift integer `C`.

Because `0<=r<2^k`, comparison of two depth-`K` descendants from the same split depth is lexicographic in

\[
\boxed{(C,r)}:
\]

one first minimizes `C`; only a tie in `C` is broken by `r`.

## 2. Future admissible suffix set

Let

\[
A_{k,q,m}\subset\mathbb Z/2^m\mathbb Z
\]

be the canonical residues whose length-`m` parity suffix keeps the total odd-count above the coefficient barrier when started with the already accumulated count `q` at depth `k`.

Equivalently, if a suffix residue `rho` has suffix odd-counts `u_j(rho)` through its first `j` steps, then

\[
\rho\in A_{k,q,m}
\]

iff

\[
3^{q+u_j(\rho)}\ge2^{k+j}
\qquad(1\le j\le m).
\]

This set depends on `(k,q,m)` but not on the endpoint residue `y`.

## 3. Exact lift formula

A lift `C` realizes a suffix whose canonical residue is `rho` iff

\[
y+3^qC\equiv\rho\pmod{2^m}.
\]

Since `3^q` is odd, it is invertible modulo `2^m`, hence the unique lift is

\[
\boxed{
C\equiv3^{-q}(\rho-y)\pmod{2^m}.
}
\]

Taking the least nonnegative representative gives the exact future cost

\[
\boxed{
J_{k,q,m}(y)
=
\min_{\rho\in A_{k,q,m}}
\left[3^{-q}(\rho-y)\right]_{2^m}.
}
\]

Therefore the smallest depth-`K` descendant of the split state is

\[
\boxed{
V_K(r,q,y)
=r+2^kJ_{k,q,m}(y).
}
\]

The global minimal survivor satisfies the exact split identity

\[
\boxed{
\mu(K)=
\min_{(r,q,y)\in P_k}
\left(r+2^kJ_{k,q,K-k}(y)\right),
}
\]

where `P_k` is the coefficient-surviving prefix set at depth `k`.

## 4. Cyclic successor form

Put

\[
M=2^m,
\qquad
S_{k,q,m}=3^{-q}A_{k,q,m}\pmod M,
\]

and

\[
\xi=3^{-q}y\pmod M.
\]

Then

\[
\boxed{
J_{k,q,m}(y)
=
\min_{s\in S_{k,q,m}}[s-\xi]_M.
}
\]

Thus `J` is exactly the clockwise distance from `xi` to the next point of the finite cyclic set `S`.

If the sorted cyclic points are

\[
s_0<s_1<\cdots<s_{N-1},
\]

then `J` is a sawtooth successor-distance function.  No probability or heuristic assumption enters this representation.

## 5. Certified gap dominance

Fix one odd-count layer `q`.  Suppose two transformed endpoint states lie in the same cyclic gap and therefore have the same optimal successor point `s` after a consistent unwrapping of the circle.

For a state `(r,xi)` in that gap,

\[
V_K=r+2^k(s-\xi)
=2^ks+\left(r-2^k\xi\right).
\]

Hence, among all split states in the same `(q, successor-gap)` cell, only a state minimizing

\[
\boxed{r-2^k\xi}
\]

can attain the minimum at depth `K`.

All other states in that cell are **certifiably dominated** and may be removed.

This is different from the failed endpoint-only rule: the future admissible set is first computed, the common optimal future channel is certified, and only then is dominance applied.

## 6. Exact meet-in-the-middle algorithm

For each `q` at the split:

1. enumerate the surviving prefix states `(r,q,y)` at depth `k`;
2. construct the admissible future residue set `A_{k,q,m}`;
3. multiply it by `3^{-q}` modulo `2^m` and sort the resulting `S_{k,q,m}`;
4. for every prefix state compute `xi=3^{-q}y mod 2^m`;
5. find the cyclic successor of `xi` in `S` by binary search;
6. evaluate `V_K=r+2^kJ`;
7. optionally apply same-gap dominance before the final minimum.

This avoids the Cartesian product between all surviving prefixes and all admissible suffixes.

If the prefix and suffix sets are explicitly materialized, the work is roughly linearithmic in their separate sizes rather than proportional to their product.  This is an exact finite computation, not an asymptotic convergence theorem.

## 7. Independent checks

The formula reproduces the earlier counterexample to endpoint-only dominance:

- `(k,q,r,y)=(10,8,127,820)`, `m=5` gives `J=2` and final start `2175`;
- `(k,q,r,y)=(10,7,383,820)`, `m=5` gives `J=1` and final start `1407`.

An independent Wolfram exhaustive check at `(K,k,m)=(12,6,6)` compared the cyclic-successor formula with direct enumeration of every lift `0<=C<2^6` for every coefficient-surviving split state and found no discrepancy.

Small exact split profiles also reproduce the known minimum `mu(K)=27` for `K=20,24,28,30`.

Observed same-successor contractions at balanced splits are modest but nonzero:

| K | split k | surviving prefix states | distinct `(q, optimal-successor)` cells |
|---:|---:|---:|---:|
| 20 | 10 | 64 | 63 |
| 24 | 12 | 226 | 211 |
| 28 | 14 | 734 | 686 |
| 30 | 15 | 1295 | 1193 |

These counts are computational diagnostics only.

## 8. Relation to the E/O channel picture

The resulting hierarchy is

\[
\boxed{
(k,q)
\;\longrightarrow\;
A_{k,q,m}
\;\longrightarrow\;
S_{k,q,m}
\;\longrightarrow\;
\xi
\;\longrightarrow\;
J
\;\longrightarrow\;
V_K.
}
\]

The E/O plane fixes the coefficient channel `q`; the future suffix language supplies the admissible target channel; multiplication by `3^{-q}` converts the affine realization constraint into a cyclic translation; and the min-plus objective becomes a successor-distance problem.

This is the current safe form of **certified dominance compression**.

## 9. Next target

The unresolved step is to describe or bound the cyclic gaps of `S_{k,q,m}` without explicitly enumerating every admissible suffix residue.

A useful theorem would be a block/automaton representation that supports exact or certified successor queries while using subexponentially fewer states than the explicit suffix set.

Any such theorem would directly improve the min-plus computation and could also connect the existing Fourier transfer to the actual small-residue obstruction, because the latter is precisely a statement about gaps / successor distances in these transformed residue sets.
