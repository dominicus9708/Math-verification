# MATH-084 — finite horizon for multi-source one-paid chains

Date: 2026-09-12

Status: `EXACT THEOREM FOR CURRENT FIRST-CELL SOURCE WINDOW / MULTI-SOURCE ONE-PAID HORIZON <=23 MACROS`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This theorem concerns only source multiplicity/resolution for the audited one-paid cylinder architecture.

## 1. Source window

The corrected MATH-058 construction uses source anchors in

\[
2^{71}<Y<2U,
\qquad
U=1364\cdot2^{61}+\frac{Q_0}{3},
\qquad
Q_0=72,057,431,991.
\]

The exact window width satisfies

\[
\boxed{2U-2^{71}<2^{72}}.
\]

## 2. Multi-source source-cylinder criterion

An exact composed source cylinder has the form

\[
Y=A+2^Hs,
\]

with consecutive source parameters separated by exactly \(2^H\).

If at least two ordinary source anchors remain, two members of the same cylinder must fit inside the complete audited source window. Therefore

\[
2^H<2^{72}.
\]

Hence

\[
\boxed{\text{multi-source}\Longrightarrow H\le71.}
\]

Equivalently,

\[
\boxed{H\ge72\Longrightarrow\text{source count}\le1.}
\]

This is stronger than treating `H>=73` merely as a convenient coarse singleton threshold. It follows directly from the actual current source-window width.

## 3. One-paid macro horizon

For every one-paid macro,

\[
H_e=L+2+\varepsilon,
\qquad L\ge1,\quad\varepsilon\ge0,
\]

so

\[
\boxed{H_e\ge3.}
\]

After \(t\) one-paid macros,

\[
H\ge3t.
\]

A multi-source chain requires \(H\le71\), therefore

\[
3t\le71,
\]

and consequently

\[
\boxed{t\le23.}
\]

Thus, if an exact one-paid chain continues to a 24th macro at all, its source has already resolved to at most one ordinary anchor:

\[
\boxed{\text{24th one-paid macro}\Rightarrow\text{singleton-resolved source}.}
\]

## 4. What this closes

The result removes the possibility of an arbitrarily long symbolic **multi-source** one-paid chain in the current first-cell source window.

The symbolic multi-source problem is therefore finite in macro count.

## 5. What this does not close

The theorem does not imply:

- every singleton terminal is Bellman-safe;
- every singleton terminal descends to the frozen floor;
- all one-paid chains are globally closed;
- the first universal Farey cell is empty;
- the Collatz conjecture is proved.

A singleton source may still require a reduced-cost/Bellman certificate or an ordinary same-integer continuation.

## 6. Relation to MATH-082/083

MATH-082 supplied the resolution-bit Bellman wedge. MATH-083 supplied the current-phase representation

\[
J'=\rho_e(J\cap I_e),
\qquad
\alpha'=\frac{\alpha}{\rho_e}+c_e,
\qquad
c_e\in\left\{\frac14,\frac18\right\}.
\]

MATH-084 now supplies an independent finite symbolic horizon:

\[
\boxed{\text{multi-source macro depth}\le23.}
\]

The remaining one-paid Bellman problem is therefore a finite-depth exact compatibility/cost problem, not an infinite symbolic-depth problem.

## Reproducibility

`collatz/src/2026_09_12_math084_onepaid_multisource_horizon_certificate.py`
