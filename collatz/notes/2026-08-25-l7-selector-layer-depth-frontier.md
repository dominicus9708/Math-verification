# Exact L7 selector-layer depth frontier through m=28

Date: 2026-08-25

Status: **finite exact computation inside the Collatz proof program; not an asymptotic theorem and not a proof of the Collatz conjecture.**

## 1. Object

For

\[
\mathcal C_m=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

let \(M_{F,L7}(m)\) be the largest depth attained by a member of \(\mathcal C_m\) while satisfying simultaneously

1. coefficient survival
   \[
   3^{q_k}\ge2^k
   \]
   at every prefix depth \(k\), and
2. every completed aligned seven-step block is the maximum-correction representative of its full-Hensel class, using exactly the L7 convention of `l7_residue_maximal_seven_fiftieths_macro_certificate.py`.

The authoritative finite enumerator is

`collatz/src/l7_small_core_frontier_m0_m28_certificate.cpp`.

It reconstructs the L7 class table from scratch and checks the regression

\[
(c_0,\ldots,c_7)=(1,2,6,15,21,16,7,1).
\]

The correction convention is exactly

\[
R\leftarrow3R+2^i
\]

when bit \(i\) of the seven-step block is odd.

## 2. Exact layer maxima

A clean HMAX=224 re-run gives

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
m&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\\hline
M_{F,L7}(m)&6&6&7&30&20&27&28&27&44&39&60&48&61&69&62
\end{array}
\]

and

\[
\begin{array}{c|rrrrrrrrrrrrrr}
m&15&16&17&18&19&20&21&22&23&24&25&26&27&28\\\hline
M_{F,L7}(m)&91&98&103&97&97&125&111&146&146&153&139&153&167&195.
\end{array}
\]

Thus, in particular,

\[
\boxed{M_{F,L7}(28)=195.}
\]

The m=28 layer has exactly one survivor through depth 192,

\[
\boxed{N=123,557,930,933,407,}
\]

and no survivor through depth 196.  The unique depth-192 survivor loses admissibility before depth 196, and the exact maximum is 195.

## 3. Minimal selector layer required by depth

Define

\[
m_{\min}(H)=
\min\{m:\mathcal C_m\cap\mathcal L_H\ne\varnothing\},
\]

where \(\mathcal L_H\) denotes the coefficient-surviving aligned-L7 language through depth \(H\).

The exact maxima above imply

\[
\begin{array}{c|c}
H\text{ range}&m_{\min}(H)\\\hline
1-6&0\\
7&2\\
8-30&3\\
31-44&8\\
45-60&10\\
61&12\\
62-69&13\\
70-91&15\\
92-98&16\\
99-103&17\\
104-125&20\\
126-146&22\\
147-153&24\\
154-167&27\\
168-195&28.
\end{array}
\]

Therefore

\[
\boxed{m_{\min}(196)\ge29.}
\]

No extrapolation beyond m=28 is made here.

## 4. Relation to the corrected Stage 4 scaling

The joint-scaling audit shows that a hypothetical first-crossing counterexample only needs selector layers

\[
m\le K\log_2H+O(1),
\]

with

\[
K_{\rm all}=\frac{14.3}{\log_2 3}\approx9.02230
\]

for the unconditional all-range magnitude exponent, and a smaller asymptotic constant after its effective threshold is made explicit.

An equivalent global target can be expressed with the layer-depth function:

\[
\boxed{
\limsup_{m\to\infty}
\frac{\log_2 M_{F,L7}(m)}m
<\frac1K.
}
\]

At m=28 the finite value is

\[
\frac{\log_2 195}{28}\approx0.27169,
\]

whereas

\[
\frac1{K_{\rm all}}
=\frac{\log_2 3}{14.3}
\approx0.11084.
\]

So the finite scan does **not** establish the required asymptotic inequality.  Its value is instead structural: the observed hard depth remains only O(10^2) while the selector layer grows, and it identifies the exact quantity that a finite-state/min-plus or symbolic growth theorem must control.

## 5. Audit correction of earlier temporary counts

During development, temporary counts at H=128/144/160 for m=27 and m=28 were quoted from a separate scratch scan.  They do not agree with the clean HMAX=224 authoritative certificate and are withdrawn.

The authoritative re-run gives

m=27:

- H128: 23 survivors,
- H144: 3,
- H160: 1,
- H192: 0,
- maximum depth 167.

m=28:

- H128: 78 survivors,
- H144: 13,
- H160: 4,
- H192: 1,
- H196: 0,
- maximum depth 195.

This correction does not alter the layer maxima or the \(m_{\min}(H)\) frontier, which were independently re-run over all m=0,...,28 with the same current implementation.

## 6. Next target

Do not merely extend brute-force m indefinitely.

The next proof target is to encode the passage from ternary selector digit \(a_m\in\{0,1\}\) to the dyadic Collatz/L7 state by a bounded or renormalizable carry state.  If the selector carry, L7 phase/Hensel state, and the necessary coefficient-height state form a finite graph after a proved truncation/renormalization, then \(M_{F,L7}(m)\) becomes a longest-path or cycle-mean problem.

A polynomial or otherwise subexponential upper bound on \(M_{F,L7}(m)\) would already beat the exponential layer window forced by the first-crossing magnitude bound.
