# `A_28` hybrid bootstrap: class propositions before trajectories

Date: 2026-08-12

Status: **exact hybrid finite certificate**. A static dyadic residue sieve first proves `88.5650%` of the `A_28` representative family recursive by class-uniform affine descent; deterministic trajectory evaluation is then required for only the remaining `11.4350%`. The resulting bootstrap reaches the same `V_28` floor as the full representative scan. This does not prove Collatz globally.

## 1. Target representative family

Use

\[
A_{28}=
\left\{
4\left(3^{44}+\sum_{i=0}^{27}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

with

\[
|A_{28}|=2^{28}=268,435,456.
\]

The ordinary interval inferred after all of `A_28` is proved recursive has width

\[
4\cdot3^{28}=91,507,169,819,844.
\]

## 2. Dyadic class proposition

Fix

\[
B_{\max}=18.
\]

A residue

\[
r=N\pmod{2^{19}}
\]

fixes every accelerated parity prefix through depth 18.

At depth `B<=18`, write the class affine map as

\[
T^B(N)=\frac{3^{q(r,B)}N+R(r,B)}{2^B}.
\]

If

\[
3^{q(r,B)}<2^B
\]

and

\[
\boxed{
R(r,B)
<
\left(2^B-3^{q(r,B)}\right)N_{\min},
}
\]

where

\[
N_{\min}=4\cdot3^{44}+3,
\]

then for every member of `A_28` in that residue class,

\[
T^B(N)<N.
\]

Thus the entire class is recursive and no trajectory extension beyond depth `B` is needed.

## 3. Static aggregation modulo `2^19`

The exact multiplicity of each dyadic residue in `A_28` is obtained from

\[
\boxed{
G_{28}(X)
=
\prod_{i=0}^{27}
\left(1+X^{4\cdot3^i}\right)
\quad\text{in}\quad
\mathbb Z[X]/(X^{2^{19}}-1),
}
\]

followed by the fixed translation `4*3^44+3`.

Therefore the class layer counts eliminated representative assignments directly from group-algebra coefficients. It does not need to reconstruct the representatives one by one.

Exact aggregation gives

\[
\boxed{
N_{\rm class}=237,739,913,
}
\]

so

\[
\boxed{
\frac{N_{\rm class}}{2^{28}}
\approx0.8856501914560795.
}
\]

Thus more than `88.565%` of the complete representative family is certified recursive by depth-18 **class propositions alone**.

The exact first-kill distribution is

\[
\begin{array}{c|r}
B&\text{representatives first eliminated}\\\hline
4&67,108,864\\
5&67,113,024\\
7&25,165,809\\
8&29,359,599\\
10&12,582,539\\
12&7,864,261\\
13&11,140,088\\
15&5,669,454\\
16&7,798,372\\
18&3,937,903
\end{array}
\]

Their sum is exactly `237,739,913`.

## 4. Surviving representative fringe

The class complement has cardinality

\[
\boxed{
N_{\rm fringe}
=268,435,456-237,739,913
=30,695,543.
}
\]

Hence only

\[
\boxed{11.434980854392052\%}
\]

of `A_28` needs any deeper deterministic trajectory evaluation.

The hybrid verifier follows trajectories only for this fringe and obtains

\[
\boxed{
\max\tau_<=425,
}
\]

with the same extremal selector mask and start as the independent full `A_28` scan:

\[
\text{mask}=140,506,676,
\]

\[
N_*=3,939,083,639,383,279,069,695.
\]

No retained representative fails to descend and no 128-bit overflow is encountered.

## 5. Effective compression

The ordinary interval width certified by the full hybrid is

\[
91,507,169,819,844.
\]

The number of starts that require actual trajectory continuation after the proposition layer is only

\[
30,695,543.
\]

Therefore the ordinary-width / tracked-start ratio is

\[
\boxed{
\frac{91,507,169,819,844}{30,695,543}
\approx2,981,122.37.
}
\]

In this concrete bootstrap stage, one explicitly tracked surviving representative accounts on average for almost three million ordinary integers in the final interval inference.

## 6. Methodological consequence

The proof architecture is now genuinely layered:

\[
\boxed{
\text{static residue aggregation}
\to
\text{class-uniform proposition deletion}
\to
\text{small surviving representative fringe}
\to
\text{finite deterministic recursion check}
\to
\text{whole-interval inference}.}
\]

This is closer to the intended proposition/set/channel program than either raw ordinary-integer enumeration or raw enumeration of all ternary representatives.

The next target is to replace more of the final `11.435%` trajectory fringe by cross-place `3`-adic predecessor propositions and by recursive survivor-cylinder structure, so that the explicit trajectory layer continues shrinking as `d` grows.

## 7. Reproducibility

Hybrid verifier:

`collatz/src/m44_low28_hybrid_class_bootstrap.cpp`

The independent full representative verifier remains

`collatz/src/m44_low28_recursive_bootstrap.cpp`.

Agreement of the hybrid extremal witness with the independent full scan is an implementation cross-check.
