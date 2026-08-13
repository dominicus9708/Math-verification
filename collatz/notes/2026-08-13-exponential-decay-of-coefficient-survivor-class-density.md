# Exponential decay of coefficient-survivor dyadic class density

Date: 2026-08-13

Status: **unconditional asymptotic theorem for the symbolic coefficient-survival language**. It combines the exact rise/plateau count recursion with the uniform positive Beatty-boundary fraction obtained from conditioned random-walk local estimates. It proves exponential decay of the *density* of coefficient-surviving dyadic residue classes. It does not prove that a ternary recursively sufficient core avoids those classes.

## 1. Survivor and boundary densities

Let

\[
\alpha:=\log_3 2,
\qquad
b_L:=\lceil\alpha L\rceil.
\]

At reduced binary depth `L`, let

\[
R_L\subseteq\mathbb Z/2^{L-2}\mathbb Z
\]

be the coefficient-surviving residue classes, and let

\[
B_L:=\{r\in R_L:q_L(r)=b_L\}
\]

be the terminal Beatty boundary.

Define

\[
\boxed{
\sigma_L:=
\frac{|R_L|}{2^{L-2}},
\qquad
\beta_L:=
\frac{|B_L|}{2^{L-2}}.
}
\]

The conditioned-walk theorem gives a constant `c_*>0` and a depth `L_0` such that

\[
\boxed{
\frac{\beta_L}{\sigma_L}
\ge c_*
}
\]

for all `L>=L_0`.

## 2. Exact plateau recursion

If

\[
b_{L+1}=b_L,
\]

every surviving parent has two surviving children.

Hence

\[
|R_{L+1}|=2|R_L|.
\]

The ambient residue group also doubles, so

\[
\boxed{
\sigma_{L+1}=\sigma_L.
}
\]

## 3. Exact rise recursion

If

\[
b_{L+1}=b_L+1,
\]

every parent outside `B_L` has two surviving children, while every boundary parent has only one.

Therefore

\[
|R_{L+1}|
=2|R_L|-|B_L|.
\]

After dividing by the child-group size `2^(L-1)`,

\[
\boxed{
\sigma_{L+1}
=
\sigma_L-rac{\beta_L}{2}
=
\sigma_L
\left(
1-rac12\frac{\beta_L}{\sigma_L}
\right).
}
\]

For every sufficiently large rise depth,

\[
\boxed{
\sigma_{L+1}
\le
(1-c_*/2)\sigma_L.
}
\]

## 4. Number of rise steps

The number of Beatty rises through depth `L` is exactly

\[
b_L-b_0
=\lceil\alpha L\rceil
=\alpha L+O(1).
\]

Thus a positive density `alpha` of all binary depths are contraction steps.

Iterating the rise inequality gives

\[
\sigma_L
\le
C(1-c_*/2)^{\alpha L+O(1)}.
\]

Hence there exist constants

\[
C<\infty,
\qquad
\kappa>0
\]

such that

\[
\boxed{
\sigma_L
\le
C e^{-\kappa L}.
}
\]

Equivalently,

\[
\boxed{
\limsup_{L\to\infty}
\frac1L\log\sigma_L<0.
}
\]

## 5. Interpretation

The dangerous coefficient-surviving binary addresses therefore have exponentially vanishing density among all `N=3 mod 4` dyadic addresses.

This is stronger than the earlier large-deviation upper bound in one important sense: it is obtained from the exact prefix-survival language and its boundary renewal, not merely by forgetting intermediate prefix constraints and retaining the final odd-count tail.

It is also structurally compatible with the observed finite survival profile.

## 6. Why density zero is not Collatz

The theorem does **not** imply that a particular integer, or the recursively sufficient ternary Cantor core, eventually avoids the survivor set.

A zero-density set may contain an infinite prescribed arithmetic or fractal subset.

Thus the remaining R2 problem is the cross-base intersection

\[
\boxed{
\text{ternary recursively sufficient core}
\quad\cap\quad
\text{exponentially sparse dyadic survivor hierarchy}.
}
\]

This is exactly why the mass-transport and spectral-complementarity analysis remains necessary.

## 7. Strengthened transport target

Because the **class** boundary fraction is now known to be bounded below by a constant rather than only `O(1/L)`, any cross-base theorem that transfers this boundary proportion to ternary-weighted mass while ensuring

\[
|K_L|=o(D_L)
\]

would give a constant-factor weighted contraction at every sufficiently large Beatty rise:

\[
\boxed{
C_{L+1}
\le
(1-c+o(1))C_L
}
\]

for some `c>0`.

Thus the symbolic/ballot channel is no longer the asymptotic bottleneck. The bottleneck has been isolated to cross-base spectral compatibility.
