# Next resonance and cross-base rank diagnostic

Date: 2026-08-09

Status: computational/structural diagnostics. No global Collatz or CST claim.

## 1. Next upper resonance after the eliminated 72-bit candidate

The next upper continued-fraction convergent considered is

\[
q=137,528,045,312,\qquad
\sigma=217,976,794,617.
\]

With
\[
\delta=2^\sigma/3^q-1,
\]
high-precision evaluation gives
\[
\delta\approx 8.98654870862196\times10^{-13}.
\]

The elementary mechanical-pair correction bound
\[
S^*(q)\le (7q+1)/24
\]
gives the paradoxical-start upper bound
\[
\boxed{x<4.4635986350\times10^{22}}.
\]
This requires at most 76 binary bits and corresponds to ternary Cantor depth at most 46 for Ansari's recursively sufficient core.

The current recursive-sufficiency verified lower bound
\[
L=4\cdot3^{44}+2\approx3.93908\times10^{21}
\]
does not eliminate this resonance: the crude upper/lower ratio is about 11.33.

## 2. Exact number of Ansari-core integers in this window

For a minimal counterexample in Ansari's core, write
\[
x=4y+3,
\]
where the ternary digits of y are all in {0,1} and the leading digit is 1.

A ternary digit-DP count in the interval
\[
L<x<4.4635986350\times10^{22}
\]
gives exactly
\[
\boxed{87,960,930,222,080=5\cdot2^{44}}
\]
core integers before any first-crossing parity constraints are imposed.

This is still too large for direct enumeration but is finite and represented by only about 47 ternary binary-choice coordinates.

## 3. Exact parity-prefix / subset-sum bridge

For a length-k parity prefix, the accelerated Collatz parity-vector theorem fixes one residue
\[
x\equiv r\pmod{2^k}.
\]
Since x=4y+3,
\[
y\equiv (r-3)/4\pmod{2^{k-2}}.
\]
For the Ansari core,
\[
y=3^m+\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\}.
\]
Hence the cross-base realization problem is the structured subset-sum congruence
\[
\boxed{
3^m+\sum_i a_i3^i
\equiv c\pmod{2^{k-2}}.
}
\]
Its group-algebra generating function is
\[
G_m(z)=z^{3^m}\prod_{i=0}^{m-1}(1+z^{3^i})
\quad\text{in }\mathbb Z[z]/(z^{2^{k-2}}-1).
\]

## 4. Naive tensor-network rank probe

To test whether the ternary-to-binary carry bridge has a low bond dimension, the Boolean indicator

`coefficient barrier survives through B=ceil(m log_2 3+2)`

was evaluated on all 2^m ternary digit strings, reshaped across a half-digit bipartition, and its exact matrix rank was computed in Wolfram.

Results:

| m | B | survivors | exact rank | maximal possible rank |
|---:|---:|---:|---:|---:|
| 4 | 9 | 4 | 4 | 4 |
| 5 | 10 | 7 | 4 | 4 |
| 6 | 12 | 15 | 7 | 8 |
| 7 | 14 | 24 | 8 | 8 |
| 8 | 15 | 38 | 14 | 16 |
| 9 | 17 | 70 | 16 | 16 |
| 10 | 18 | 114 | 32 | 32 |
| 11 | 20 | 209 | 32 | 32 |
| 12 | 22 | 362 | 64 | 64 |
| 13 | 23 | 664 | 64 | 64 |

Thus the most naive matrix-product-state factorization across the ternary digit order becomes essentially full rank. A constant or very small bond dimension should not be expected from this digit ordering.

This does not destroy polynomial reducibility in the nominal first-crossing length because m itself is O(log sigma). Full rank in m is still polynomial in sigma. It does show that the cross-base carry bridge is a genuine source of complexity and should not be treated as a low-rank perturbation without further structure.

## 5. Small-depth coefficient-stopping behavior inside F

Exhaustive Wolfram calculations for all 2^m elements at fixed ternary depth show that the mean coefficient-stopping time stays close to 10 through m=18, while the observed maxima fluctuate rather than growing monotonically. Selected maxima:

m=13: 197
m=14: 170
m=15: 251
m=16: 192
m=17: 243
m=18: 195

This is empirical only. It is not evidence for a proven O(m) maximum bound, and the irregular spikes make such a claim premature.

## 6. Relation to known Cantor-set dynamics

Ansari's recursively sufficient core is an affine image of the ternary Cantor set (digits 0/1). Lagarias and later Abram--Lagarias studied intersections of multiplicative translates of the 3-adic Cantor set under powers of 2 and showed that these intersections admit finite-automaton presentations and nontrivial Hausdorff-dimension bounds. These results are structurally relevant to the cross-base problem but do not by themselves provide the uniform deterministic exclusion required for Collatz.
