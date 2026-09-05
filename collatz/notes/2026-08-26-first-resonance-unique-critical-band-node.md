# First resonance: the root is the unique critical-band node in the full Christoffel DAG

Date: 2026-08-26

Status: **exact structural classification** for the repaired first-resonance branch.  This is a major proof-architecture reduction, not a proof of the Collatz conjecture.

## 1. Critical slopes

With the published finite verification base

\[
B=2^{71},
\]

define

\[
\beta=\log_{3+1/B}2,
\qquad
\alpha=\log_3 2.
\]

For a Christoffel DAG node `(P,Q)`, interpret

\[
Q=\text{odd-event count},
\qquad
A=P+Q=\text{accelerated time}.
\]

Classify the node by its odd/time slope `Q/A`:

- **RS-safe** if `Q/A < beta`;
- **critical-band** if `beta < Q/A < alpha`;
- **coefficient-supercritical** if `Q/A > alpha`.

## 2. Exact classification of all 138 nodes

The complete anchored first-resonance Farey/Christoffel DAG has 138 distinct nodes.

Exact rational logarithmic comparison gives

\[
\boxed{43\text{ RS-safe nodes},}
\]

\[
\boxed{94\text{ coefficient-supercritical nodes},}
\]

and

\[
\boxed{1\text{ critical-band node}.}
\]

The unique critical-band node is exactly the root

\[
\boxed{
(P_0,Q_0)
=(42150895613,72057431991),}
\]

whose total time is

\[
A_0=P_0+Q_0=114208327604.
\]

Thus

\[
\boxed{
\beta<\frac{Q_0}{A_0}<\alpha}
\]

while **every proper recursive subblock lies outside this open interval**.

## 3. Root children are already decided

The ordered root factorization is

\[
C_{P_0,Q_0}
=
C_{38297853692,65470613321}
\;C_{3853041921,6586818670}.
\]

The first child is coefficient-supercritical:

\[
\frac{65470613321}{103768467013}>\alpha.
\]

The second child is finite-base RS-safe:

\[
\frac{6586818670}{10439860591}<\beta.
\]

The earlier block

\[
(P,Q)=(111457,190537),
\qquad A=301994,
\]

used for the earlier parity-RS wall is likewise one of the 43 safe nodes.

## 4. What this does and does not prove

This result means the recursive grammar contains no hidden secondary resonance scale requiring a new coefficient classification.  The only block whose slope is not already decided by the finite-base safe condition or by true coefficient supercriticality is the full root itself.

It does **not** mean that every safe subblock forces the whole orbit below the original start.  A safe block can be entered at an elevated internal state.  Therefore the two-boundary Bellman state remains necessary.

The valid conclusion is structural:

\[
\boxed{
\text{all proper block slopes are decided;}
\quad
\text{only their boundary-preserving composition remains unresolved}.}
\]

## 5. DSD proof-chain reduction

Before this classification the first resonance could be pictured as 138 recursively nested blocks, each potentially requiring a separate analytic decision.

The classification collapses that description to

\[
\boxed{
\begin{array}{c}
\text{one critical root}\\
\downarrow\\
\text{decided supercritical/safe child grammar}\\
\downarrow\\
\text{Hensel + ordering + cost interface composition}
\end{array}}
\]

Hence the remaining first-resonance theorem is not a coefficient-classification theorem.  It is purely an **interface compatibility theorem**:

> Can a path glue already-decided safe and supercritical Christoffel blocks while satisfying both exposed ordinary boundaries, Hensel congruences, ordering debt, and the global correction budget?

The desired answer remains no, equivalently

\[
V_{\rm two-boundary}>4314000000.
\]

## 6. Generalization implication

Together with the RS/Farey-parent identification, this suggests a reusable form for the finite-crossing branch:

1. locate the unique Farey/Christoffel node in the finite-base critical band;
2. certify that its proper recursive children are all on decided sides of the band;
3. prove a uniform two-boundary interface exclusion for such a critical mediant root.

This would replace resonance-by-resonance orbit enumeration with a structural Farey theorem.

Companion certificate:

`collatz/src/first_resonance_dag_critical_band_uniqueness_certificate.py`.
