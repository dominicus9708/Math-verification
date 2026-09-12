# MATH-086 — one-paid phase-only horizon and stronger penalty floor

Date: 2026-09-12

Status: `EXACT PHASE OVER-APPROXIMATION / MULTI-SOURCE HORIZON <=19 / FIRST-CELL OPEN`

The Collatz conjecture and the first universal Farey cell remain open.  This note strengthens the one-paid part of the current Bellman program.

## 1. Stronger one-paid penalty floor

In the current-phase coordinates of MATH-085, a one-paid edge has

\[
\Omega' = \rho_e\Omega,
\qquad
p_e=c_e\Omega',
\]

with exactly two cases.

For the `c_e=1/8` branch the paid-exit construction gives

\[
\Omega'\in(8/9,1),
\]

so

\[
p_e=\Omega'/8>1/9.
\]

For the `c_e=1/4` branch,

\[
\Omega'\in(1/2,2/3),
\]

so

\[
p_e=\Omega'/4>1/8>1/9.
\]

Hence every canonical one-paid macro satisfies

\[
\boxed{p_e>1/9}.
\]

This improves the MATH-082 coarse lower bound `p_e>1/12`.

With `lambda=19/503`, the phase-free resolution wedge becomes

\[
\mathcal P>t/9,
\]

and therefore a sufficient terminal condition is

\[
\boxed{171(H-73)\le503t}
\]

for `H>73`; `H<=73` remains automatically safe under the 73-bit coarse resolution potential.

## 2. Phase-only over-approximation

The next calculation deliberately removes dyadic address compatibility after the first multi-source macro.

This does **not** prune actual paths.  It enlarges the language: every actual same-integer continuation remains present, while additional phase-compatible but address-incompatible paths may appear.

Edges with identical

\[
(H,\rho_e,c_e)
\]

and overlapping phase domains are unioned exactly.  The 910 canonical address cylinders reduce to

\[
\boxed{126}
\]

phase-edge components.

The 857 actual multi-source first macros project to

\[
\boxed{113}
\]

initial phase states.

## 3. Multi-source cutoff supplied by MATH-084

MATH-084 proves

\[
\text{actual multi-source}\Longrightarrow H\le71.
\]

Therefore, in the phase-only over-approximation, only states with `H<=71` need be propagated as possible multi-source states.  An edge taking the phase state to `H>71` is treated as a terminal-crossing candidate.

Because address has been forgotten, extinction of this larger `H<=71` phase language is sufficient to bound the actual multi-source horizon.

## 4. Exact phase-state counts

The exact surviving phase-state counts are:

| macro depth | phase-only `H<=71` states | terminal crossings |
|---:|---:|---:|
| 2 | 1,293 | 2,992 |
| 3 | 3,127 | 38,415 |
| 4 | 3,023 | 94,067 |
| 5 | 2,890 | 90,732 |
| 6 | 2,728 | 86,488 |
| 7 | 2,543 | 81,425 |
| 8 | 2,337 | 75,687 |
| 9 | 2,111 | 69,315 |
| 10 | 1,868 | 62,465 |
| 11 | 1,613 | 55,143 |
| 12 | 1,356 | 47,509 |
| 13 | 1,099 | 39,801 |
| 14 | 843 | 32,066 |
| 15 | 607 | 24,467 |
| 16 | 395 | 17,483 |
| 17 | 221 | 11,293 |
| 18 | 93 | 6,259 |
| 19 | 13 | 2,597 |
| 20 | **0** | 361 |

Thus the address-forgotten phase language itself has no `H<=71` state after macro depth 20.

Therefore the actual same-integer language satisfies the stronger horizon

\[
\boxed{\text{actual multi-source one-paid chain has at most 19 macros}.}
\]

Equivalently, if a 20th one-paid macro is compatible, its source family is necessarily singleton-resolving.

This improves the purely length-based MATH-084 bound of 23 multi-source macros.

## 5. Consequence for the already audited depth-4--6 terminals

MATH-085 gives terminal maximum depths

\[
H_{\max}(4)=84,
\qquad
H_{\max}(5)=87,
\qquad
H_{\max}(6)=90.
\]

The stronger `1/9` wedge alone now certifies all three levels:

\[
171(84-73)=1881<503\cdot4=2012,
\]

\[
171(87-73)=2394<503\cdot5=2515,
\]

\[
171(90-73)=2907<503\cdot6=3018.
\]

Hence all terminal handoffs at depths 4, 5 and 6 are Bellman-safe without even invoking their exact phase-infimum refinement.

The exact terminal populations remain

\[
76,585,
\qquad372,841,
\qquad1,358,935.
\]

## 6. What is and is not closed

The new result proves a finite one-paid horizon for source multiplicity, but it does **not** yet prove Bellman safety of every terminal crossing at macro depths 7--20.

The phase-only language is deliberately larger than the actual address-compatible language.  Some phase-only terminal crossings have negative reduced-cost lower bounds at intermediate depths.  These are false-path candidates until exact dyadic compatibility is restored.

The next task is therefore much smaller than raw depth extension:

1. construct the phase-only danger frontier at depths 7--20;
2. restore exact dyadic address only on that frontier;
3. discard address-incompatible false paths;
4. test the residual actual terminal cylinders against the strengthened wedge and exact current-phase penalty.

## 7. Claim boundaries

Do not infer:

- phase-only horizon `=>` phase alone determines actual dynamics;
- multi-source horizon `=>` every singleton terminal is Bellman-safe;
- Bellman safety `=>` ordinary Collatz descent;
- one-paid finite horizon `=>` first universal cell emptiness;
- MATH-086 `=>` the Collatz conjecture.

## Reproducibility

Certificate:

`collatz/src/2026_09_12_math086_onepaid_phase_horizon_certificate.py`
