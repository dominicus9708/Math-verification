# Stage 4 two-state recurrent core has K=117 allowance

Date: 2026-08-23

Status: **exact two-state 12-window phase-coupled reduction. After treating H>=2 as already controlled exits, the remaining H=0,1 recurrent dyadic core has growth below 2^336/117^12. This weakens the remaining cross-base requirements but does not yet eliminate H=0 or H=1. This is not a proof of the Collatz conjecture.**

## 1. Two-state unresolved core

The previous exact reductions show that incoming H>=2 needs no new selector-regularity theorem at the corresponding branch budgets.

Thus the still-unresolved recurrent state space can be reduced to

\[
\boxed{H\in\{0,1\}.}
\]

Transitions from H=0 or H=1 into H>=2 are treated as exits into already controlled sectors.

## 2. Exact one-window masses

For each length-28 mechanical phase, retain only residue-maximal L7 paths that remain nonnegative and end again in H'=0 or 1.

The exact worst-phase row masses are

\[
\boxed{
M_0=405,550,
\qquad
M_1=1,513,565.
}
\]

## 3. Twelve-window genuine phase products

There are exactly 337 length-336 mechanical factors. Multiplying the twelve actual two-state 28-step matrices for each factor and taking the entrywise maximum gives

\[
P_{\max}^{(12)}=
\begin{pmatrix}
5420989033005741994466829925744616150372978448553471085632422011649601422480 &
6535758559679090596615964974758100454723656321310415866171578871628607490208\\
9986846317718188796227476512967599231780531055101592900704821147103202624960 &
15428773549657007353811384502892045440367157385919481503148660803568995111440
\end{pmatrix}.
\]

The exact verifier is

`collatz/src/stage4_two_state_twelve_window_certificate.py`.

## 4. Exact K=117 potential

The very small positive integer potential

\[
\boxed{v=(1,2)^T}
\]

already suffices. The certificate proves

\[
\boxed{
117^{12}P_{\max}^{(12)}v<2^{336}v
}
\]

componentwise.

Therefore the two-state recurrent dyadic core has a twelve-window average exclusion allowance strictly larger than

\[
\boxed{
\frac{\log_2 117}{28}
\approx0.245370169.
}
\]

The remaining cross-base theorem may therefore be much weaker than the original K<15 target whenever the orbit remains inside H=0,1.

## 5. Remaining selector-loss targets

At the K=117 scale, sufficient one-window conditioned-selector survival caps are

\[
\mu(A_H\mid\text{past})<117\frac{M_H}{2^{28}}.
\]

Hence

\[
\boxed{\begin{array}{c|c|c}
H&\text{sufficient selector survival cap}&\text{required selector loss}\\\hline
0&0.1767626032\ldots&0.8232373968\ldots\\
1&0.6597008742\ldots&0.3402991258\ldots
\end{array}}
\]

So H=1 no longer needs a majority selector loss: approximately 34.03% is sufficient.

H=0 remains the dominant obstruction.

## 6. What is and is not proved

This calculation proves only a stronger deterministic dyadic exclusion budget for the unresolved two-state branch.

It does not prove that the conditioned ternary selector measure actually loses 34.03% at H=1 or 82.32% at H=0. That remains the genuine same-word cross-base problem.

The significance is that all other relative-height states have been removed from the analytic target, and the required correlation theorem has been weakened substantially.

## 7. Next target

The next useful object is no longer a full renewal-height automaton. It is the signed selector correlation with the two-state H=0,1 transition language.

The existing odd-frequency child-correlation identity can be specialized to this two-state boundary. H=1 should be attacked first because its required conditioned selector loss is only about 34%, while H=0 is the final neutral-renewal core.
