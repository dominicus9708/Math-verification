# Recursive-sieve intersection limit at the current R1 core

Date: 2026-08-12

Status: **scope clarification from Ansari's recursive-sufficiency construction**. The nested sieves do not automatically remove the three lower ternary affine blocks left after the `m=46` exclusion. This is a negative structural result, not a Collatz theorem.

## 1. Ansari's nested recursively sufficient sets

Ansari (2025) defines

\[
F_0=4\mathbb N_0+3
\]

and, for `n>=1`,

\[
F_n
=
\bigcup_{a_0,\ldots,a_{n-1}\in\{0,1\}}
\left(
4\cdot3^n\mathbb N_0
+4\sum_{i=0}^{n-1}a_i3^i
+3
\right).
\]

The paper proves

\[
F_0\supseteq F_1\supseteq F_2\supseteq\cdots
\]

and that every `F_n` is recursively sufficient.

For a hypothetical *minimal* Collatz counterexample `N`, recursive sufficiency implies

\[
N\in F_n
\qquad\text{for every }n.
\]

Otherwise `N notin F_n` would merge with a smaller positive integer, contradicting minimality.

## 2. What the intersection means for finite ordinary integers

For a fixed finite integer `N`, once `n` exceeds its ternary digit length, the term

\[
4\cdot3^n k
\]

must have `k=0` in any representation of `N` inside `F_n`.

Therefore membership in every sufficiently deep `F_n` is exactly the condition

\[
\boxed{
N=4\left(\sum_{i\ge0}a_i3^i\right)+3,
\qquad
a_i\in\{0,1\},
}
\]

with only finitely many nonzero `a_i`.

Thus the project’s ternary `0/1` recursive core is not a temporary `F_44` approximation. It is the finite-integer part of the nested-sieve intersection.

## 3. Consequence after the m=46 exclusion

At the current upper-CF first-crossing resonance, the transition-conditioned overlapping-window theorem eliminates the entire leading `m=46` affine layer.

The remaining recursive-core candidates lie in the three lower 44-free-trit blocks

\[
\boxed{
N=4\left(C+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad
a_i\in\{0,1\},
}
\]

with

\[
\boxed{
C\in\{3^{44},\ 3^{45},\ 3^{45}+3^{44}\}.
}
\]

Passing from `F_44` to `F_45,F_46,...` does not remove these integers: in the deeper formula they are represented by setting the newly introduced higher ternary coefficients to zero.

Hence there is no further automatic recursive-sieve descent available from this particular nested family.

## 4. Correct next target

The residual R1 problem is therefore a genuine intersection problem between

1. the ternary Cantor core
   \[
   4\sum a_i3^i+3,
   \]
2. the dyadic first-crossing / high-resolution formation cylinder,
3. the exact ordinary renewal-gap condition,
4. and the terminal 3-adic endpoint cylinder.

Further progress requires a new cross-base obstruction or an additional independent recursively sufficient sieve, not merely another application of the same `F_n` chain.

## Reference

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025), especially the definition of `F_n`, Lemma 3.1, and Proposition 3.1.
