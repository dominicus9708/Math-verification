# Plateau-pair two-place defect coordinates

Date: 2026-08-13

Status: **exact local-to-global theorem**. On deterministic Beatty plateau pairs, a single `01 -> 10` move simultaneously has an exact Archimedean remainder cost and an exact dyadic canonical-address shift. Disjoint plateau moves add independently. This refines the earlier global real-shadow/dyadic-address coupling; it is not a proof of Collatz.

## 1. Time-expanded parity notation

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

let a length-`L` parity word be

\[
w=(w_0,\ldots,w_{L-1})\in\{0,1\}^L.
\]

Let

\[
q=\sum_{i=0}^{L-1}w_i
\]

and let `ell` denote the ordinal of a specified one in the word.

The affine iterate is

\[
T^L(n)
=
\frac{3^q n+R(w)}{2^L},
\]

where

\[
\boxed{
R(w)
=
\sum_{j:w_j=1}
2^j3^{q-q_{j+1}(w)}.
}
\]

The real remainder is

\[
E(w)=R(w)/2^L.
\]

The canonical starting residue modulo `2^L` is

\[
\boxed{
r(w)
\equiv
-\sum_{j:w_j=1}
2^j3^{-q_{j+1}(w)}
\pmod{2^L}.}
\]

## 2. One adjacent move

Suppose positions `(j,j+1)` contain exactly one one, and that one is the `ell`-th one in the word.

Let `w_R` contain `01` and `w_L` contain `10`, with all other bits identical.

All later one-ordinals agree because the pair contains one one in both orientations.

For the affine numerator,

\[
R(w_R)-R(w_L)
=
(2^{j+1}-2^j)3^{q-\ell}
=
\boxed{2^j3^{q-\ell}}.
\]

Hence

\[
\boxed{
E(w_R)-E(w_L)
=
2^{j-L}3^{q-\ell}>0.
}
\]

Thus moving the one to the right increases the Archimedean remainder; moving it left decreases the remainder by exactly this amount. This is compatible with the known `01/10` parity-vector remainder order of Rozier--Terracol.

For the canonical dyadic residue,

\[
r(w_R)-r(w_L)
\equiv
-(2^{j+1}-2^j)3^{-\ell}
\pmod{2^L},
\]

so

\[
\boxed{
r(w_L)-r(w_R)
\equiv
2^j3^{-\ell}
\pmod{2^L}.}
\]

The same local coordinate therefore appears in two completions:

\[
\boxed{
2^j3^{-\ell}
}
\]

is the dyadic address shift, while multiplying its formal real counterpart by the global coefficient `3^q/2^L` gives the exact real remainder cost.

## 3. Why deterministic plateau pairs are admissible coordinates

Put

\[
\alpha=\log_3 2,
\qquad
b_t=\lceil\alpha t\rceil.
\]

On the coefficient-survival boundary

\[
q_t\ge b_t,
\qquad
q_L=b_L,
\]

every deterministic plateau start

\[
b_{j+1}=b_j
\]

makes a mixed pair `(j,j+1)` freely swappable. This was proved in

`2026-08-13-deterministic-plateau-pair-cube-decomposition.md`.

Since `alpha>1/2`, those plateau pairs are disjoint.

## 4. Mechanical orientation

The lower mechanical/Beatty word is

\[
m_j=b_{j+1}-b_j.
\]

At a plateau start `j`,

\[
m_j=0.
\]

Because two consecutive plateau increments are impossible, the next mechanical digit is one, so the mechanical pair is

\[
\boxed{01}.
\]

Therefore `10` on a mixed deterministic plateau pair is a local left-shift defect relative to the mechanical remainder maximizer.

## 5. Independent sum over disjoint plateau defects

Let `w` be a boundary word. Let `J_-(w)` be the set of deterministic plateau starts at which `w` has the left orientation `10`.

Form `w^+` by flipping every such pair to `01` and leaving all other digits fixed.

All these moves are admissible and commute. Their pair sums are unchanged, so every one-ordinal `ell_j` is unchanged by the other plateau flips.

Therefore the real correction is **exactly additive**:

\[
\boxed{
E(w^+)-E(w)
=
\sum_{j\in J_-(w)}
2^{j-L}3^{q-\ell_j}.
}
\]

The dyadic canonical address shift is simultaneously

\[
\boxed{
r(w)-r(w^+)
\equiv
\sum_{j\in J_-(w)}
2^j3^{-\ell_j}
\pmod{2^L}.}
\]

Each summand has exact 2-adic valuation `j`, so distinct plateau coordinates occupy distinct formation levels.

## 6. Lower bound on total mechanical defect

Let `w_chr` denote the mechanical/Christoffel remainder maximizer in the relevant first-crossing class. Since moving all plateau `10` defects to `01` produces another admissible word,

\[
E(w_{chr})\ge E(w^+)\ge E(w).
\]

Hence

\[
\boxed{
E(w_{chr})-E(w)
\ge
\sum_{j\in J_-(w)}
2^{j-L}3^{q-\ell_j}.
}
\]

This gives a rigorous piece of the total defect using only deterministic plateau coordinates. It loses no information by first reducing to a defect count.

## 7. Relation to the earlier two-place defect theorem

Earlier work obtained globally that a Christoffel defect lowers the real rational shadow and moves the strong dyadic renewal address.

The present theorem resolves part of that global defect into independent coordinates:

\[
\boxed{
\text{plateau coordinate }j
\longmapsto
\left(
2^{j-L}3^{q-\ell_j},
\;2^j3^{-\ell_j}\bmod2^L
\right).
}
\]

Thus a single Boolean local change is observed simultaneously as

- an Archimedean loss in the first-crossing remainder;
- a 2-adic displacement in the canonical start address.

This is the local two-place form of the real-shadow/address coupling.

## 8. Next use

For the current R1 resonance, the useful object is no longer only the number of defects. One can retain the exact weighted plateau vector

\[
\left\{
(j,\ell_j):j\in J_-(w)
\right\}
\]

and impose simultaneously

\[
\sum_{j\in J_-}
2^{j-L}3^{q-\ell_j}
\le\text{real defect budget}
\]

and

\[
r(w)
\equiv r(w^+)
+
\sum_{j\in J_-}2^j3^{-\ell_j}
\pmod{2^L}.
\]

This is a weighted knapsack in the real place coupled to a collision-free valuation hierarchy in the dyadic place. It is a more faithful target than the previous defect-density reduction.

## External relation

Rozier and Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948 / Discrete Mathematics 349 (2026), Section 2, prove the partial order under adjacent `01/10` moves and its monotone effect on the remainder. The exact canonical-residue shift and the deterministic plateau-coordinate coupling above are project-derived.
