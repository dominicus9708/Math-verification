# MATH-094 — resolution-indexed danger kernel

Date: 2026-09-12

Status: `EXACT STRUCTURAL REDUCTION / DANGER-KERNEL GENERATOR ADDED / NUMERICAL KERNEL SUMMARY NOT YET FROZEN`

## 1. Why macro depth can be removed

MATH-093 replaces each exact family by the safe dyadic envelope

\[
0\le s<2^R.
\]

Every multi-edge of resolution `h<=R` then updates

\[
\boxed{R'=R-h}
\]

exactly and contributes reduced cost exactly equal to its positive penalty.
Therefore all possible negative reduced cost is localized to the final edge.

The first one-paid macro has resolution at least 3, and the first-cell source window has width below `2^72`.  Hence the first unresolved envelope after one macro satisfies

\[
\boxed{R\le69.}
\]

Thus the remaining search lives on a finite resolution DAG `R=0,...,69`.

## 2. Danger kernel

Let

\[
D_R\subset(1/2,1)
\]

be the set of current phases from which the address-forgotten dyadic envelope can reach a locally negative terminal edge.

For one exact phase edge `e` with

\[
(h,I_e,\rho_e,c_e),
\]

where

\[
\Omega_{out}=\rho_e\Omega,
\qquad
p_e=c_e\Omega_{out},
\]

the safe over-approximation obeys

\[
\boxed{
D_R=
\bigcup_{h\le R}
\left(I_e\cap\rho_e^{-1}D_{R-h}\right)
\cup
\bigcup_{h>R}
\left\{
\Omega\in I_e:
 c_e\rho_e\Omega<\lambda(h-R)
\right\}.
}
\]

The first term propagates danger through a multi-edge.  The second term is the local terminal phase-address wedge with address temporarily forgotten.

## 3. Acyclicity

Every canonical one-paid edge satisfies

\[
h\ge3.
\]

Therefore every recursive reference uses

\[
R-h<R.
\]

The kernel is computed bottom-up with no cycle and no macro-depth state.

## 4. Safety direction

The kernel deliberately forgets exact dyadic address compatibility and all positive penalties accumulated before the terminal edge.
Both omissions enlarge the danger language.

Hence

\[
\boxed{
\text{actual dangerous phase at resolution }R
\subseteq D_R.
}
\]

A phase outside `D_R` is therefore Bellman-safe for every actual same-integer address state with that resolution.
A phase inside `D_R` is only a candidate and must still pass the MATH-090 carry/address test.

## 5. Consequence for the old frontier

The previous unresolved macro-depth band

\[
7\le t\le16
\]

is now better represented as

\[
\boxed{
R\in\{0,1,\ldots,69\}
\quad+\quad
\Omega\in D_R
\quad+\quad
\text{exact carry/address state}.
}
\]

This is a stronger structural reduction because the same `D_R` kernel covers every macro depth simultaneously.

## 6. Next calculation

The next high-value step is:

1. execute and freeze the exact interval unions for all `D_R`;
2. intersect each actual first-macro envelope with `D_R`;
3. propagate only those surviving danger cells through the MATH-092 normalized 2-adic transducer;
4. apply MATH-090 low-residue/carry valuation at terminal edges.

If this closes, the whole one-paid Bellman language is closed without separately certifying depths 7 through 16.

Generator:

`collatz/src/2026_09_12_math094_resolution_indexed_danger_kernel.py`
