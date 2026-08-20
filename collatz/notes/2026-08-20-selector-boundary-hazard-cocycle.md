# Selector-boundary hazard cocycle

Date: 2026-08-20

Status: **exact reformulation of coefficient-overlap growth at Beatty rises + finite exact calibration.** This is not a proof of the Collatz conjecture.

## 1. Weighted and unweighted boundary hazards

At a Beatty rise from parent depth L to L+1, let

- C_L be the ternary-selector mass in coefficient-surviving parent residues;
- D_L be the selector mass in one-child coefficient-boundary parents;
- K_L be the oriented sibling-correlation repair term;
- U_L be the unweighted number of coefficient-surviving parents;
- B_L be the unweighted number of one-child boundary parents.

The exact weighted transport identity is

\[
\boxed{2C_{L+1}=2C_L-D_L+K_L.}
\]

For the uniform binary language there is no sibling imbalance, so

\[
\boxed{U_{L+1}=2U_L-B_L.}
\]

## 2. Normalized overlap cocycle

Define the mod-4-normalized selector/coefficient overlap at parent depth L by

\[
\Xi_L
:=
\frac{C_L/2^m}{U_L/2^{L-2}}.
\]

At a plateau, every coefficient-surviving parent has both children and the survival probability is unchanged, so

\[
\boxed{\Xi_{L+1}=\Xi_L.}
\]

At a Beatty rise, cancellation of the fixed selector mass gives the exact ratio

\[
\boxed{
\frac{\Xi_{L+1}}{\Xi_L}
=
\frac{1-\frac{D_L-K_L}{2C_L}}
     {1-\frac{B_L}{2U_L}}.
}
\]

Thus the only source of logarithmic overlap growth is the difference between the **effective selector hazard**

\[
\boxed{h_L^{\rm sel}:=\frac{D_L-K_L}{C_L}}
\]

and the uniform coefficient hazard

\[
\boxed{h_L^{\rm unif}:=\frac{B_L}{U_L}.}
\]

The corrected Stage-4 target

\[
\Xi_H=2^{o(H)}
\]

is therefore equivalent to requiring that the cumulative logarithmic hazard distortion over Beatty rises be sublinear in H.

## 3. Boundary support density before orientation

It is useful to separate

\[
\Xi_D(L)
:=
\frac{D_L/C_L}{B_L/U_L}.
\]

This measures whether selector mass lands on the boundary support at the same conditional frequency as uniform dyadic mass, before the orientation repair K is applied.

Using the existing exact m=44 mass-transport checkpoints gives values extremely close to one.  Examples are

\[
\begin{array}{c|c}
L&\Xi_D(L)\\\hline
19&1.0000001148\\
20&1.0000010458\\
22&0.9999987848\\
25&1.0000011634
\end{array}
\]

This is stronger finite evidence than the coarse inequality U<D: the selector is not merely failing to concentrate on the surviving orientation; it is already hitting the boundary support at essentially the uniform conditional rate.

## 4. Effective-hazard calibration

Including the exact K term, selected m=44 checkpoints give

\[
\begin{array}{c|c|c}
L&h_L^{\rm sel}/h_L^{\rm unif}&\log_2(\Xi_{L+1}/\Xi_L)\\\hline
14&1.0000000179&-3.45\times10^{-9}\\
17&0.9999994397& 1.04\times10^{-7}\\
19&0.9999995267& 6.63\times10^{-8}\\
20&1.0000014294&-3.56\times10^{-7}\\
22&0.9999986325& 2.06\times10^{-7}
\end{array}
\]

The exact arithmetic identity and integer checkpoints are reproduced by

`collatz/src/selector_boundary_hazard_cocycle_certificate.py`.

## 5. Selector-only resonance does not force hazard resonance

The selector collision diagnostic has a relatively large finite resonance at

\[
(m,r)=(29,17),
\qquad
2^{29}e_{17}(29)\approx3.25473466.
\]

The corresponding L=19 mass transport nevertheless has

\[
C=61{,}397{,}829,
\qquad
D=10{,}865{,}114,
\qquad
K=5{,}842,
\]

so

\[
\boxed{|K|/D\approx5.38\times10^{-4}}
\]

and

\[
\boxed{\Xi_D\approx1.0002519.}
\]

Hence a large selector-only L2 sibling resonance need not align with the Beatty boundary support or orientation.  This supports attacking the actual hazard cocycle directly rather than insisting on a very small universal selector-only collision constant.

## 6. Revised Stage-4 target

The most economical remaining form is now:

> **Hazard distortion theorem.**  Along the reduced ternary-selector core, the cumulative logarithmic difference between the effective selector boundary hazard and the uniform coefficient boundary hazard is o(H).

Equivalently,

\[
\boxed{
\sum_{\substack{L<H\\\text{Beatty rise}}}
\log_2
\left(
\frac{1-h_L^{\rm sel}/2}
     {1-h_L^{\rm unif}/2}
\right)
=o(H).
}
\]

This is exactly the normalized-overlap theorem, but it localizes the missing cross-base information to one scalar conditional boundary statistic at each Beatty rise.
