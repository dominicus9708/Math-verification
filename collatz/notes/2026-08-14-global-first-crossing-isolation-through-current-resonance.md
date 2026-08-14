# Global first-crossing isolation through the current resonance

Date: 2026-08-14

Status: **exact finite Diophantine isolation theorem at the current verified floor**. It upgrades the previous interval-local Worley certificate to every first coefficient crossing with odd count up to the current resonance. It does not eliminate the current resonance and therefore does not prove the Collatz conjecture.

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

for every possible first-crossing rational in this full denominator range.

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
1\le q\le137,528,045,312
\Longrightarrow
\text{the only possible first-crossing survivor at }N\ge N_0
\text{ is the current resonance.}
}
\]

## 4. What this improves

Previously the same current resonance had been isolated only after choosing a large denominator interval near it. The present result closes the entire lower denominator range in one statement.

Hence R1 no longer needs a list of increasingly large lower convergents/semiconvergents below the current resonance. Every such lower-scale first crossing is already excluded by the verified floor plus the mechanical remainder envelope.

The R1 proof tree is therefore reduced to one finite arithmetic cell:

\[
\boxed{
(A,H)
=(217,976,794,617,
137,528,045,312).
}
\]

## 5. Remaining obstruction

At this resonance the multiplicative excess is exceptionally small. The current start floor gives only a few billion units of mandatory correction, whereas the universal mechanical correction ceiling is still tens of billions.

Therefore the Archimedean correction envelope alone cannot eliminate this last cell. Its closure still requires the already-developed mixed-place information:

- Christoffel defect/displacement;
- strengthened dyadic renewal address;
- ternary recursively-sufficient core;
- 3-adic correction/predecessor structure;
- or an equivalent cross-base incompatibility theorem.

This note isolates the target; it does not solve that final cell.
