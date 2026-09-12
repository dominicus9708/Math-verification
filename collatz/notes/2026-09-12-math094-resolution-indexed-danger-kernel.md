# MATH-094 — resolution-indexed danger kernel

Date: 2026-09-12

Status: `EXACT NEGATIVE RESULT / PHASE-ONLY RESOLUTION KERNEL SATURATES`

## 1. Construction

MATH-093 replaces the exact source family by the safe dyadic envelope

\[
0\le s<2^R,
\]

so every multi-edge of resolution `h<=R` updates

\[
R'=R-h
\]

exactly and contributes only positive penalty.
The initial unresolved envelope satisfies `R<=69`.

Define `D_R` as the current phases from which the address-forgotten envelope can reach a locally negative terminal edge.  With a merged phase edge

\[
(h,I_e,\rho_e,c_e),
\]

the exact over-approximation is

\[
D_R=
\bigcup_{h\le R}
\left(I_e\cap\rho_e^{-1}D_{R-h}\right)
\cup
\bigcup_{h>R}
\left\{\Omega\in I_e:c_e\rho_e\Omega<\lambda(h-R)\right\}.
\]

The recursion is acyclic because every one-paid edge has `h>=3`.

## 2. Exact numerical result

Using the canonical 126 merged phase-edge components from MATH-086 and exact `Fraction` arithmetic gives

\[
\boxed{
D_R=(1/2,1)
\qquad
\text{for every }R=0,1,\ldots,69.
}
\]

Thus the phase-only resolution kernel is completely saturated.

## 3. Interpretation

This is a useful negative result.
It shows that the abstraction

\[
(R,\Omega)
\]

alone is too coarse once both of the following are discarded:

1. accumulated positive penalty from earlier multi-edges;
2. exact dyadic carry/address compatibility.

Every phase remains connected, in the enlarged language, to some locally dangerous terminal.
Therefore a successful depth-free quotient must preserve at least one additional proof-facing channel.

## 4. What is *not* implied

The saturation

\[
D_R=(1/2,1)
\]

does not mean every actual source state is dangerous.
The kernel deliberately forgets same-integer address information and earlier paid penalty, so it contains many fictitious paths.  MATH-088 already gives a concrete example where every phase-danger path at depth 17 is killed by exact dyadic address incompatibility.

## 5. Revised next target

Do **not** continue with the bare `(R,Omega)` kernel.
The next quotient must retain one of:

- accumulated penalty coefficient/current-phase Bellman credit;
- MATH-090 carry valuation / MATH-092 normalized 2-adic address;
- or a controlled combination of both.

The strongest current candidate is a product state of

\[
\boxed{(R,\Omega,\text{carry/address credit})}
\]

with the terminal MATH-089 phase-address wedge.

Reproducibility:

`collatz/src/2026_09_12_math094_resolution_indexed_danger_kernel.py`
