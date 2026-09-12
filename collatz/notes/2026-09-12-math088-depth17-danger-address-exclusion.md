# MATH-088 — depth-17 one-paid danger-address exclusion

Date: 2026-09-12

Status: `FINITE EXACT / ONE-PAID MACRO DEPTH 17 BELLMAN-SAFE`

The global Collatz conjecture and the first universal Farey cell remain open.
Paid-count layers `2<=r<=13` remain outside this calculation.

## Result

MATH-086 reduces the one-paid problem to a finite macro horizon and supplies the strengthened universal atom bound `p>1/9`.  For macro depth 17, the phase-only lower-envelope calculation retains only phase cells that can still have negative terminal Bellman margin.  Exact dyadic address compatibility is then restored.

The complete depth-16 danger-corridor parent set contains

\[
\boxed{595,738}
\]

exact address states.

Across those parents, only canonical one-paid edges whose exact phase lower envelope can be negative are tested.  There are

\[
\boxed{5,330,013}
\]

such phase-danger edge attempts.

For every attempt the exact source-parameter congruence

\[
s\equiv (A_e-B)\,(3^Q)^{-1}\pmod{2^{h_e}}
\]

is reconstructed and compared with the surviving source range

\[
0\le s<M.
\]

The complete replay gives

\[
\boxed{0\text{ address-compatible danger edges}.}
\]

Hence there is no actual depth-17 one-paid terminal with negative Bellman margin.

## Address-gap diagnostic

The largest surviving parent count in the danger corridor is

\[
\boxed{M_{\max}=4,239}.
\]

The smallest required residue among all phase-danger edge attempts is

\[
\boxed{s_{\min}=9,498,993,710,400}.
\]

Thus every dangerous residue lies far outside every surviving source-parameter interval:

\[
\boxed{s_{\min}>M_{\max}}.
\]

This diagnostic is stronger than a mere zero-count report, but it is still a finite depth-17 fact rather than a universal residue-gap theorem.

## DSD interpretation

The depth-17 result separates two information channels exactly:

1. phase/penalty information identifies where negative reduced cost is still possible;
2. dyadic address information decides whether such a phase path belongs to any actual same-integer source family.

The phase-only language is an over-approximation.  A phase-danger path is therefore not a mathematical failure.  At depth 17 every such over-approximated path is removed by exact address incompatibility.

## Claim boundary

This result proves Bellman safety for one-paid macro depth 17 only.  It does not prove ordinary descent for every represented integer, first-cell emptiness, later-cell closure, or the Collatz conjecture.

Reproducibility checkpoint:

`collatz/src/2026_09_12_math088_depth17_danger_address_exclusion_certificate.py`
