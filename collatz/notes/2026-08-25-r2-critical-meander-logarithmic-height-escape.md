# R2 critical meander: density-one logarithmic height escape

Date: 2026-08-25

Status: **exact consequence of previously proved harmonic/state-escape bounds, combined with the known parity-density necessity for a rational non-cyclic 2-adic Collatz orbit.**  This narrows the eventual coefficient-survival branch but does not exclude it.

## 1. Post-formation odd-event coordinates

For a fixed positive integer `N` whose orbit never descends below `N`, write

\[
x_q=(N+c_q)2^{s_q+\theta_q},
\]

where

\[
s_q=\lfloor q\gamma\rfloor-A_q,
\qquad
\theta_q=\{q\gamma\},
\qquad
\gamma=\log_2 3.
\]

The harmonic-correction theorem gives

\[
\boxed{c_q=O_N(q^{1/9}).}
\]

Thus, for sufficiently large `q`,

\[
\log_2(N+c_q)
\le
\frac19\log_2q+O_N(1).
\]

## 2. State escape input

The exact state-escape theorem for a nonperiodic no-first-descent odd-event orbit says that for every

\[
0<\vartheta<\frac89,
\]

one has

\[
\boxed{
x_q>q^\vartheta}
\]

on a set of odd-event indices of natural density one.

Taking logarithms in the exact state identity gives on this density-one set

\[
s_q+\theta_q
>
\vartheta\log_2q-rac19\log_2q-O_N(1).
\]

Since `0<theta_q<1`,

\[
s_q
>
\left(\vartheta-\frac19\right)\log_2q-O_N(1).
\]

Let `epsilon>0` and choose `vartheta<8/9` sufficiently close to `8/9`.  Absorbing the fixed `O_N(1)` term into `epsilon log q` for all sufficiently large `q` yields

\[
\boxed{
s_q\ge
\left(\frac79-\varepsilon\right)\log_2q}
\]

on a density-one set.

In particular, an eventual coefficient-survival branch cannot remain in any fixed finite skew strip.

## 3. Rational non-cyclic density constraint

López and Stoll, *The 3x+1 Periodicity Conjeture in R* (arXiv:2101.12747), prove the following necessary condition: if a rational 2-adic integer has a non-cyclic Collatz trajectory, then the lower limiting parity density is exactly

\[
\frac{\ln2}{\ln3}.
\]

For an ordinary positive integer this applies because it is a rational 2-adic integer.

In the present coefficient coordinates this implies, for the non-cyclic R2 branch,

\[
\boxed{
\liminf_{q\to\infty}\frac{s_q}{q}=0
}
\]

(up to the bounded fractional part already separated as `theta_q`).

## 4. Exact shape of the remaining R2 branch

Combining Sections 2 and 3, the eventual coefficient-survival hard core must satisfy both

\[
\boxed{
 s_q\ge(7/9-o(1))\log_2q
\quad\text{for density-one many }q,
}
\]

and

\[
\boxed{
\liminf s_q/q=0.
}
\]

Thus the R2 hard core is not a bounded critical strip.  It is an **unbounded but sublinear critical meander**: its coefficient skew must escape at least logarithmically during almost all odd-event times, while never acquiring a uniform positive linear slope.

## 5. Periodic branch

If a positive integer enters a cycle of parity length `L` with `q` odd symbols, the cycle affine identity is

\[
(2^L-3^q)x=R,
\qquad R>0.
\]

Hence

\[
2^L>3^q,
\qquad
\frac qL<\frac{\ln2}{\ln3}.
\]

Therefore an eventually periodic positive cycle belongs to the coefficient-contracting side in average density and is separate from the non-cyclic R2 critical-meander analysis above.

This observation does not exclude all nontrivial positive cycles; it only records their density side correctly.

## 6. Proof-program consequence

A finite-state quotient that simply truncates the accumulated height at a fixed constant cannot be a complete model of R2: any genuine R2 counterexample must visit arbitrarily high skew levels and in fact occupy logarithmically growing levels on a density-one set.

The remaining global proof architecture should therefore keep the branches distinct:

\[
\boxed{
\begin{array}{ll}
\text{neutral-return branch:}&
\text{root-translation ultrametric locking;}\\[1mm]
\text{R2 open-positive branch:}&
\text{unbounded sublinear height/potential analysis.}
\end{array}}
\]

This prevents a false finite-height SCC closure while preserving the exact same-integer finite-state reduction on the neutral-return side.
