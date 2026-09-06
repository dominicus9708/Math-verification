# Global first-crossing isolation through the current resonance

Date: 2026-08-14

Status: **EXACT CONDITIONAL DIOPHANTINE ISOLATION.**  The arithmetic certificate below is exact under the explicit start-floor hypothesis

\[
N\ge N_0:=V_{33}+1.
\]

However, the 2026-09-06 dependency audit established that `V_33` was promoted from exact finite `m=44` selector certificates to a continuous global floor using Ansari's recursively-sufficient ternary Cantor-core coverage.  That coverage is currently OPEN because the printed induction fails already at `F_1 -> F_2`.  Therefore this note must no longer be cited as an unconditional reduction of **every** hypothetical minimal counterexample to the current resonance.

The correct interpretation is:

\[
\boxed{
N\ge V_{33}+1
\Longrightarrow
\text{the isolation theorem below is SAFE},
}
\]

while

\[
\boxed{
\text{every hypothetical minimal counterexample satisfies }N\ge V_{33}+1
\quad\text{is CONDITIONAL on repaired coverage}.}
\]

See `collatz/notes/2026-09-06-r1-current-floor-dependency-audit.md`.

This correction changes the scope of the theorem, not the finite Worley/Dujella calculation.  It does not prove the Collatz conjecture.

Let

\[
N_0:=V_{33}+1
=4(3^{44}+3^{33})+3.
\]

Let a completed first coefficient crossing have total time `A` and odd count `q`:

\[
A=\lceil q\log_2 3\rceil,
\qquad
P=\frac{2^A}{3^q}>1.
\]

Assume the orbit has remained at least at its start through this first crossing.

## 1. Mechanical first-crossing envelope

The parity-order theorem makes the mechanical/Christoffel word the maximal additive remainder among all first-crossing words with the same `(A,q)`. Hence

\[
S_w\le S_{\rm chr}
\le\frac{q}{6\ln2}+\frac13.
\]

Survival at a start `N>=N_0` requires

\[
N(P-1)\le S_w.
\]

Since

\[
P-1\ge\ln P
=A\ln2-q\ln3,
\]

we get

\[
0<\frac Aq-\log_2 3
<
\frac{1}{6N_0(\ln2)^2}
+
\frac{1}{3N_0q\ln2}.
\]

Equivalently

\[
\left|\frac Aq-\log_2 3\right|
<\frac{k(q)}{q^2},
\]

where

\[
k(q)=
\frac{q^2}{6N_0(\ln2)^2}
+
\frac{q}{3N_0\ln2}.
\]

## 2. Uniform Worley constant through the current resonance

Put

\[
H=137,528,045,312.
\]

The function `k(q)` is increasing, so for every

\[
1\le q\le H
\]

one has

\[
\boxed{k(q)\le k(H)<1.666.}
\]

Therefore the Worley--Dujella theorem gives the same global product budget

\[
\boxed{rs\le3}
\]

for every possible first-crossing rational in this full denominator range under the stated start-floor hypothesis.

This is stronger than the previous use of the theorem only on the final interval immediately below the current resonance.

## 3. Exact exhaustive rational certificate

The accompanying source

`collatz/src/global_first_crossing_isolation_to_current_resonance.py`

uses exact `Fraction` arithmetic and rigorous series intervals for `ln 2`, `ln 3`, and `log_2 3`.

It performs the following complete finite reduction:

1. generate every adjacent-convergent Worley combination with `rs<=3` and denominator at most `H`;
2. retain the complete primitive upper-approximation superset allowed by the uniform `k(H)` bound;
3. expand every non-reduced multiple `g(a,b)` for which
   \[
   0<g(a-b\log_2 3)<1,
   \]
   i.e. for which `A=g a` can actually equal `ceil(q log_2 3)`;
4. test the exact lower bound on
   \[
   N_0\ln P
   \]
   against the exact upper mechanical correction ceiling.

The finite counts are

\[
\boxed{30\text{ primitive Worley upper candidates}.}
\]

After all admissible non-reduced first-crossing multiples are included, the certificate tests

\[
\boxed{1,241,563\text{ coefficient pairs}.}
\]

Exactly one survives:

\[
\boxed{
(A,q)
=
(217,976,794,617,
137,528,045,312).
}
\]

Thus

\[
\boxed{
N\ge N_0,
\quad
1\le q\le137,528,045,312
\Longrightarrow
\text{the only possible first-crossing survivor is the current resonance.}
}
\]

## 4. Revised scope

Within the explicit `N>=N_0` branch, every lower-scale first crossing in the stated denominator range is excluded by the start floor plus the mechanical remainder envelope, except for the single current resonance.

Hence the **selector-coverage branch** of the R1 proof tree is reduced to one finite arithmetic cell:

\[
\boxed{
(A,H)
=(217,976,794,617,
137,528,045,312).
}
\]

It is no longer valid to promote this sentence to the universal R1 proof tree without first repairing the ternary coverage theorem.

The current coverage-independent universal fallback is the older R1 result using the published paradoxical frontier as quoted in the repository, which yields a much weaker but independent lower odd-event bound of about

\[
5.395570552\times10^9.
\]

## 5. Remaining obstruction

At this resonance the multiplicative excess is exceptionally small. The conditional start floor gives only a few billion units of mandatory correction, whereas the universal mechanical correction ceiling is still tens of billions.

Therefore the Archimedean correction envelope alone cannot eliminate this last **selector-conditional** cell. Its closure still requires mixed-place information such as:

- Christoffel defect/displacement;
- strengthened dyadic renewal address;
- repaired ternary recursively-sufficient coverage;
- 3-adic correction/predecessor structure;
- or an equivalent cross-base incompatibility theorem.

This note isolates the target under its stated floor hypothesis; it does not solve that final cell.
