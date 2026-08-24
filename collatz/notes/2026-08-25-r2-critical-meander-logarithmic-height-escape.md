# R2 critical meander: density-one logarithmic height escape

Date: 2026-08-25

Status: **audit-corrected consequence of the harmonic area-deficit theorem plus the known parity-density necessity for a rational non-cyclic 2-adic Collatz orbit.**  The previous first version derived the weaker constant `7/9` indirectly through state escape.  The already proved harmonic moving-strip theorem gives the sharp constant available in this proof architecture, `8/9`.  This narrows the eventual coefficient-survival branch but does not exclude it.

## 1. Post-formation odd-event coordinates

For a fixed positive integer `N` whose nonperiodic odd-event orbit never descends below `N`, write

\[
A_i=\sum_{j<i}v_j,
\qquad
\lambda_i:=\frac{2^{A_i}}{3^i},
\qquad
D_i:=A_i-i\gamma,
\qquad
\gamma:=\log_2 3.
\]

Thus

\[
\boxed{\lambda_i=2^{D_i}.}
\]

Equivalently, with the positive coefficient-surplus coordinate

\[
e_i:=i\gamma-A_i=-D_i,
\]

one has

\[
\boxed{\lambda_i=2^{-e_i}.}
\]

The harmonic-correction theorem gives, for some constant `C_N>0`,

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i\le C_Nq^{1/9}
}
\]

for all sufficiently large `q`.

## 2. Moving low-height sparsity

For any threshold `E>=0`, if `e_i<=E`, then

\[
\lambda_i=2^{-e_i}\ge2^{-E}.
\]

Therefore

\[
2^{-E}\#\{i<q:e_i\le E\}
\le\sum_{i<q}\lambda_i
\le C_Nq^{1/9},
\]

and hence

\[
\boxed{
\#\{i<q:e_i\le E\}
\le C_N2^E q^{1/9}.
}
\]

Taking

\[
E=\delta\log_2q,
\qquad0<\delta<8/9,
\]

gives

\[
\boxed{
\#\{i<q:e_i\le\delta\log_2q\}
=O_N(q^{1/9+\delta})=o(q).
}
\]

Thus for every `epsilon>0`, on a density-one set of odd-event indices,

\[
\boxed{
e_i\ge(8/9-\varepsilon)\log_2 i}
\]

up to an absorbable fixed additive constant.  In the integer skew coordinate

\[
s_i=\lfloor i\gamma\rfloor-A_i=e_i-\{i\gamma\},
\]

the same asymptotic statement holds:

\[
\boxed{
s_i\ge(8/9-\varepsilon)\log_2 i}
\]

on a density-one set for all sufficiently large `i`.

This is exactly the moving critical-strip sparsity already implicit in the harmonic area-deficit theorem; the present note records it in the R2 coordinate system.

## 3. Rational non-cyclic density constraint

López and Stoll, *The 3x+1 Periodicity Conjeture in R* (arXiv:2101.12747), prove the necessary condition that if a rational 2-adic integer has a non-cyclic Collatz trajectory, then the lower limiting parity density is

\[
\frac{\ln2}{\ln3}.
\]

For an ordinary positive integer this implies, in the present coefficient coordinates,

\[
\boxed{
\liminf_{i\to\infty}\frac{s_i}{i}=0
}
\]

(up to the bounded fractional part separated above).

## 4. Exact shape of the remaining R2 branch

Combining Sections 2 and 3, an eventual coefficient-survival counterexample candidate must satisfy both

\[
\boxed{
 s_i\ge(8/9-o(1))\log_2 i
\quad\text{for density-one many }i,
}
\]

and

\[
\boxed{
\liminf s_i/i=0.
}
\]

Thus the R2 hard core is an **unbounded but sublinear critical meander**.  It cannot remain in any fixed finite skew strip, and in fact it spends density one of its odd-event time above every moving logarithmic strip of slope strictly below `8/9`.

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

Therefore an eventually periodic positive cycle belongs to the coefficient-contracting side in average density and is separate from the non-cyclic R2 critical-meander analysis above.  This does not exclude all nontrivial positive cycles.

## 6. Proof-program consequence

A fixed-height finite-state quotient cannot model R2.  Any genuine R2 counterexample must occupy logarithmically growing skew levels on a density-one set while still returning arbitrarily close to the critical density on a sublinear scale.

The correct split remains

\[
\boxed{
\begin{array}{ll}
\text{neutral-return branch:}&\text{root-translation ultrametric locking},\\[1mm]
\text{R2/open-positive branch:}&\text{unbounded sublinear height/potential analysis}.
\end{array}}
\]
