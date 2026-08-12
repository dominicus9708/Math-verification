# First-coefficient-crossing mechanical-envelope theorem

Date: 2026-08-12

Status: **exact structural theorem**. Among all parity words whose coefficient stays at least one until the final step and first crosses below one at that final step, the affine remainder is maximized by the unique Beatty/mechanical boundary word. This identifies the Christoffel/mechanical word as an extremal envelope for the entire first-crossing language, not merely as a convenient candidate. This does not prove the Collatz conjecture or the coefficient-stopping-time conjecture.

## 1. Time-expanded setup

Use

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For a binary parity word of prefix length `i`, let

\[
q_i=\#\{\text{odd symbols among the first }i\text{ positions}\}.
\]

Then

\[
T^i(N)=\frac{3^{q_i}N+R_i}{2^i}.
\]

Put

\[
\boxed{\alpha=\log_3 2}
\]

and define the Beatty boundary

\[
\boxed{k_i=\lceil i\alpha\rceil.}
\]

Since `alpha` is irrational,

\[
k_i-k_{i-1}\in\{0,1\}.
\]

## 2. Exact structure of a first coefficient crossing

Suppose length `j` is the **first coefficient crossing**, i.e.

\[
3^{q_i}\ge2^i\qquad(1\le i<j)
\]

but

\[
3^{q_j}<2^j.
\]

Equivalently,

\[
q_i\ge k_i\qquad(i<j),
\]

and

\[
q_j<k_j.
\]

Because `q_i` is nondecreasing and increases by at most one per step, such a crossing is possible only when

\[
\boxed{k_j=k_{j-1}+1.}
\]

Moreover one must have exactly

\[
\boxed{q_{j-1}=k_{j-1}=k_j-1}
\]

and the final parity symbol is even:

\[
\boxed{v_{j-1}=0.}
\]

Indeed, if `k_j=k_(j-1)`, then `q_j>=q_(j-1)>=k_j`, impossible. If `q_(j-1)>k_(j-1)=k_j-1`, the same contradiction occurs. Hence equality and a final zero are forced.

Thus every first-crossing word has:

1. prefix sums `q_i>=k_i` for all `i<j`;
2. total weight exactly `k_(j-1)` on the first `j-1` positions;
3. a final even symbol.

## 3. Latest-one mechanical boundary word

Define the mechanical boundary word `m_1,...,m_(j-1)` by

\[
\boxed{m_i=k_i-k_{i-1},\qquad k_0=0.}
\]

Its prefix sums are exactly

\[
\sum_{t=1}^{i}m_t=k_i.
\]

Any other first-crossing prefix `w` satisfies

\[
\sum_{t=1}^{i}w_t\ge k_i
=\sum_{t=1}^{i}m_t
\qquad(i<j),
\]

while both words have the same total number of ones at `j-1`.

Therefore every other admissible word places its ones weakly **earlier** than the mechanical word. Equivalently the mechanical word is the unique admissible arrangement that delays every optional odd symbol as far to the right as the coefficient-survival constraints permit.

## 4. Remainder dominance

For fixed length and fixed number of odd symbols, the affine remainder increases when an adjacent pattern

\[
10
\]

is changed to

\[
01.
\]

This follows directly from the correction recurrence

\[
R_{i+1}=\begin{cases}
R_i,&w_i=0,\\
3R_i+2^i,&w_i=1,
\end{cases}
\]

and is the same unordered-majorization/remainder ordering proved by Rozier and Terracol.

Since every first-crossing word can be transformed toward the mechanical boundary word by moving optional ones to the right while preserving the prefix constraints, one obtains

\[
\boxed{R_j(w)\le R_j(m0),}
\]

where `m0` denotes the mechanical length-`j-1` prefix followed by the forced final zero.

Equality holds only for the mechanical boundary word itself.

Hence:

\[
\boxed{
\text{mechanical/Beatty first-crossing word}
=\text{unique maximal-remainder envelope of the whole first-crossing language}.
}
\]

## 5. Consequence for paradoxical first crossings

At a first coefficient crossing one has

\[
q_j=k_j-1
\]

and therefore

\[
T^j(N)\ge N
\]

can occur only if

\[
N\le\frac{R_j(w)}{2^j-3^{k_j-1}}.
\]

By the envelope theorem,

\[
\boxed{
N\le
\frac{R_j(m0)}{2^j-3^{k_j-1}}
=:\mathcal P_j.
}
\]

Thus `P_j` is a universal Archimedean ceiling for **every** first-crossing parity word at depth `j`.

A finite DP evaluation through `j<=2000` gives

\[
\max_{j\le2000}\mathcal P_j\approx2.38671\times10^5,
\]

far below the current m=44 floor. This finite observation is diagnostic only; no uniform bound in `j` is claimed.

## 6. Connection to the odd-only Christoffel formulation

The boundary increments

\[
m_i=k_i-k_{i-1}
\]

are the binary mechanical word of slope

\[
\alpha=\log_3 2=1/\log_2 3.
\]

Reading the distances between successive odd positions converts this time-expanded mechanical word into the odd-only valuation/Christoffel word used in the R1 analysis.

Thus the earlier Christoffel reference path is not an ad hoc low-defect model. It is the odd-only representation of the exact remainder-maximizing envelope of all coefficient-surviving first-crossing words.

This upgrades the logical role of the R1 mechanical branch:

\[
\boxed{
\text{arbitrary first-crossing word}
\preceq_{\rm remainder}
\text{mechanical/Christoffel envelope}.
}
\]

## 7. Why this still does not solve the branch

A smaller remainder does not by itself imply a larger dyadic start representative. Different parity words occupy different residue classes modulo `2^j`.

Therefore one cannot eliminate all nonmechanical first-crossing words merely because their Archimedean ceiling is below the mechanical ceiling unless that ceiling is already below the global candidate floor.

At sufficiently deep continued-fraction resonances, `P_j` may grow substantially because

\[
2^j-3^{k_j-1}
\]

can be unusually small relative to `2^j`.

The remaining problem is consequently two-place:

1. the mechanical envelope controls the largest possible real/additive allowance;
2. the actual word determines a dyadic start address;
3. nonmechanical displacement lowers the real allowance while shifting the dyadic address.

This is exactly the strengthened renewal-address / defect-potential structure already developed in the R1 program.

## External background

Rozier and Terracol, *Paradoxical behavior in Collatz sequences* (2025/2026), Section 2, prove the parity-vector partial order and show that moving ones to the right increases the remainder; their Theorem 2.4 gives the unconstrained extremal remainder. The theorem above adds the **first-coefficient-crossing prefix constraint**, under which the unique rightmost admissible arrangement is the Beatty/mechanical boundary word.
