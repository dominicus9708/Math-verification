# Reverse contracting-ancestor sieve inside the ternary recursive core

Date: 2026-08-12

Status: **new exact recursively-sufficient sieve independent of Ansari's nested `F_n` chain + finite depth-18 intersection certificate**. It removes additional ternary `0/1` cylinders from the minimal-counterexample core. This does not prove Collatz.

## 1. Motivation

Ansari's intersection sieve leaves the finite ternary Cantor core

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

Applying deeper members of the same nested chain cannot shrink this intersection further.

However, recursive sufficiency is stable under intersection. Therefore any independent family of integers that can be proved to merge with a smaller positive integer can be removed from `F`, producing a strictly finer minimal-counterexample sieve.

The natural dual construction is to search backward from a candidate endpoint for a smaller Collatz ancestor.

## 2. Contracting reverse words

Use the accelerated map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

A specified forward parity word `w` of total length `k`, with `q` odd symbols, has affine form

\[
\boxed{
T^k(m)=\frac{3^q m+R_w}{2^k},
}
\]

where `R_w>0`.

If its endpoint is `n`, then

\[
\boxed{
m=\frac{2^k n-R_w}{3^q}.}
\]

The endpoint integrality condition is one exact 3-adic residue class

\[
\boxed{
n\equiv R_w2^{-k}\pmod{3^q}.}
\]

Whenever

\[
\boxed{2^k<3^q,}
\]

the reverse multiplicative factor is less than one. Since `R_w>0`, every positive realization satisfies

\[
\boxed{0<m<n.}
\]

Thus every endpoint in this residue class is recursive in Ansari's sense and cannot be a minimal counterexample.

For `q=1,k=1`, the word is a single odd step and the endpoint class is

\[
n\equiv2\pmod3.
\]

This is exactly the first ternary digit-`2` class removed in Ansari's construction. The present sieve is therefore a strict higher-depth generalization of that elementary reverse merge.

## 3. Reverse-cycle formulation

Starting at an endpoint state `y`, an inverse-even step sends

\[
y\mapsto2y.
\]

An inverse-odd step exists precisely when the current state is `2 mod 3`, and then

\[
y\mapsto\frac{2y-1}{3}.
\]

Group `e>=0` inverse-even steps immediately before one inverse-odd step. One reverse cycle is

\[
\boxed{
y\mapsto\frac{2^{e+1}y-1}{3}.}
\]

After `q` inverse-odd cycles, let

\[
E=e_1+\cdots+e_q.
\]

The net reverse multiplicative factor is

\[
\boxed{
\frac{2^{q+E}}{3^q}.
}
\]

Hence a contracted ancestor exists as soon as

\[
\boxed{2^{q+E}<3^q.}
\]

Define the exact contraction budget

\[
\boxed{
B_q:=\max\{E\in\mathbb Z_{\ge0}:2^{q+E}<3^q\}.
}
\]

The first values are

\[
0,1,1,2,2,3,4,4,5,5,6,7,7,8,8,9,9,10,\ldots
\]

No logarithmic approximation is needed to compute `B_q`.

## 4. Finite 3-adic dynamic program

Suppose the endpoint is known modulo `3^Q`.

After one inverse-odd division only its residue modulo `3^{Q-1}` is needed; after `j` inverse-odd steps, only the residue modulo `3^{Q-j}` remains relevant.

For a current residue `y`:

- if `y=0 mod 3`, no power of two can make an inverse-odd step available;
- if `y=2 mod 3`, the admissible `e` are even;
- if `y=1 mod 3`, the admissible `e` are odd.

For each remaining residue, keeping only the smallest accumulated `E` is exact: future admissibility depends only on that residue, and a smaller accumulated cost weakly dominates every larger one.

This gives a finite exact DP for the question:

> Does a given endpoint cylinder modulo `3^Q` admit any contracted positive ancestor using at most `Q` inverse-odd steps?

## 5. Intersection with the ternary 0/1 core

For a depth-`Q` ternary core cylinder write

\[
S_Q=\sum_{i=0}^{Q-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

and

\[
\boxed{
n\equiv4S_Q+3\pmod{3^Q}.}
\]

The map from the `Q` binary choices `(a_0,...,a_{Q-1})` to this residue is injective. Therefore every forbidden endpoint residue modulo `3^q` removes at most one length-`q` ternary `0/1` cylinder.

Running the exact reverse DP through depth `18` gives new **minimal** forbidden cylinders at the following depths:

\[
\boxed{
\begin{array}{c|r}
q&\text{new minimal forbidden cylinders}\\\hline
7&1\\
9&1\\
11&1\\
12&8\\
14&14\\
16&37\\
18&93
\end{array}
}
\]

No new minimal cylinder occurs at the intervening depths through `18`.

Because these are prefix-minimal cylinders, they are disjoint in the ternary symbolic measure. Their exact removed fraction of the ternary `0/1` core is

\[
\boxed{
\frac1{2^7}
+\frac1{2^9}
+\frac1{2^{11}}
+\frac8{2^{12}}
+\frac{14}{2^{14}}
+\frac{37}{2^{16}}
+\frac{93}{2^{18}}
=
\frac{3665}{262144}.
}
\]

Numerically,

\[
\boxed{
\frac{3665}{262144}
\approx0.01398086548.
}
\]

Thus the independent reverse sieve removes about `1.3981%` of Ansari's Cantor core already at inverse-odd depth `18`.

This percentage is not used probabilistically; it is simply the exact fraction of depth-18 symbolic cylinders certified recursive by this finite sieve.

## 6. Explicit first new cylinder

The first genuinely new core cylinder appears at

\[
q=7.
\]

Its low-to-high ternary choices are

\[
\boxed{(a_0,\ldots,a_6)=(1,1,0,0,0,1,0),}
\]

or high-to-low

\[
\boxed{(a_6,\ldots,a_0)=(0,1,0,0,0,1,1).}
\]

For every integer in this cylinder,

\[
\boxed{n\equiv991\pmod{3^7}.}
\]

The forward parity word

\[
\boxed{11111011000}
\]

has `k=11`, `q=7`, and exact affine map

\[
\boxed{
T^{11}(m)=\frac{3^7m+2219}{2^{11}}.
}
\]

Since

\[
2^{11}=2048<2187=3^7,
\]

the inverse is

\[
\boxed{
m=\frac{2^{11}n-2219}{3^7}<n.}
\]

The endpoint congruence is exactly `n=991 mod 3^7`, so the entire ternary cylinder is recursive and is removed from the minimal-counterexample core.

## 7. A second recursively sufficient sieve

Let `R_Q` be the union of all residue cylinders certified by a contracted reverse word of inverse-odd depth at most `Q`.

Every `n>1` in `R_Q` merges with a smaller positive integer. Hence `R_Q` is a recursive set, and its complement

\[
\boxed{G_Q:=\mathbb N\setminus R_Q}
\]

is recursively sufficient.

Since Ansari's `F` is recursively sufficient and intersections of recursively sufficient sets remain recursively sufficient,

\[
\boxed{F\cap G_Q}
\]

is a strictly finer recursively sufficient sieve.

At `Q=18`, this intersection removes the 155 prefix-minimal ternary cylinders listed above (counted across their varying depths) and has the exact depth-18 removal fraction `3665/262144` relative to `F`.

## 8. Why this route is different from the first-crossing defect analysis

The reverse contracting-ancestor sieve makes no assumption about the huge first-crossing resonance `(A,H)` and does not use the Christoffel defect coordinate.

It is instead a **minimal-counterexample sieve**:

\[
\text{short backward word}
\Rightarrow
\text{smaller positive ancestor}
\Rightarrow
\text{recursive endpoint class}
\Rightarrow
\text{remove that ternary cylinder globally}.
\]

Therefore every cylinder removed here disappears simultaneously from R1, R2, and the periodic minimal-counterexample search.

This makes the sieve especially useful for the remaining `m=44` bootstrap target, where a global convergence/minimality argument is more valuable than excluding only one first-crossing resonance.

## 9. Current limitation

Depth `18` removes only about `1.4%` of the ternary Cantor core, so this alone is far from eliminating the entire `m=44` block.

The important result is structural:

> Ansari's ternary intersection is not terminal. There exist explicit, independently generated recursive subcylinders *inside* it, and they can be found by a finite 3-adic reverse-cost automaton.

The next question is whether the sequence of reverse contracting-ancestor sieves has a substantially smaller limiting symbolic entropy than the full ternary `0/1` core.

That is now a concrete finite-state / subshift problem rather than an unrestricted Collatz trajectory problem.

## 10. Reproducibility

The exact verifier is

`collatz/src/reverse_contracting_ancestor_sieve.py`.

It uses only Python integer arithmetic and checks:

- the contraction budgets `B_q`;
- exact inverse-step divisibility;
- minimum accumulated reverse-doubling cost by residue;
- the depth-18 cylinder classification;
- the exact removed fraction `3665/262144`;
- and the explicit depth-7 witness `n=991 mod 3^7` / `11111011000`.
