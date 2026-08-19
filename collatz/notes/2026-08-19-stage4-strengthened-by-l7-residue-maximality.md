# Stage 4 strengthened by short-block residue maximality

Date: 2026-08-19

Status: **deterministic language-exclusion budget strengthened; cross-base theorem still open.**  This is not a proof of the Collatz conjecture.

## 1. Previous Stage 4 budget

The H19 residue-maximal language gave an exact exclusion rate above 1/9 after rational weight optimization.  This already improved the required same-integer overlap theorem to

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}H<\frac19.
\]

Under subexponential overlap this required only \(H>Cm\) with \(C>9\).

Certificate:

`collatz/src/h19_residue_maximal_entropy_one_ninth_certificate.py`.

## 2. Residue maximality is not intrinsically length 19

For any fixed binary block length L and fixed odd count q, group words by their full-Hensel correction residue

\[
R(w)\pmod{3^q}.
\]

If a word w is not the maximum-correction member of its class, choose u in the same class with larger correction.  Then

\[
R_u-R_w=3^q\Delta,\qquad \Delta>0,
\]

and starting u at x-Delta gives exactly the same L-step endpoint as starting w at x.

Therefore a hypothetical minimal counterexample larger than the finite maximum local credit must use a residue-maximal word in every aligned L-step block.

## 3. Exact L=7 local theorem

The complete 2^7 cube has full-Hensel class counts

\[
(c_q)_{q=0}^{7}=(1,2,6,15,21,16,7,1).
\]

The largest ordinary predecessor credit in any class is exactly

\[
\boxed{\Delta_{\max}=21}.
\]

Hence any hypothetical minimal counterexample \(N>21\) must use a maximum-correction representative in every aligned seven-step block.

For a seven-step mechanical reference block the critical odd count is Q=4 or Q=5.  Take

\[
z=\frac43.
\]

Writing

\[
P_5(z)=\sum_{q=0}^7 c_q z^{q-5},
\]

a Q=4 block costs the extra factor z.

Over any 700-step macro there are 100 seven-step blocks.  Since

\[
3^{441}<2^{700}<3^{442},
\]

the mechanical odd-count total is at least 441, so there can be at most 59 Q=4 blocks.  Therefore the full weighted language is bounded by

\[
F=P_5(4/3)^{100}(4/3)^{59}.
\]

The exact rational certificate proves

\[
F^{50}<2^{30100},
\]

hence

\[
\boxed{F<2^{602}}.
\]

Thus a 700-step macro loses strictly more than

\[
700-602=98
\]

binary information bits, and the deterministic language-exclusion rate satisfies

\[
\boxed{\eta>\frac{98}{700}=\frac7{50}=0.14}.
\]

Certificate:

`collatz/src/l7_residue_maximal_seven_fiftieths_macro_certificate.py`.

## 4. New sufficient Stage 4 theorem

Let the exact same-integer overlap amplification be

\[
\Xi_{m,H}
=\frac{|\mathcal C_m\cap\mathcal L_H|/|\mathcal C_m|}
{|\mathcal L_H|/2^H}.
\]

The L7 theorem replaces the previous sufficient target by

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log_2\Xi_{m,H}}H
<\frac7{50}.
}
\]

In the stronger subexponential case \(\Xi=2^{o(H)}\), any

\[
\boxed{H>Cm,\qquad C>\frac{50}{7}\approx7.142857}
\]

is sufficient for finite extinction of the reduced selector mass, up to fixed boundary constants.

This is substantially weaker than all previous overlap targets:

- formation-only: approximately 0.0500445 exclusion, slope approximately 19.982;
- original H19 residue-maximal bound: approximately 0.104613, slope approximately 9.559;
- optimized H19 rational bound: >1/9, slope <9;
- current L7 macro bound: >7/50, slope <50/7.

## 5. Mandatory mod-4 normalization

Coefficient survival itself forces the first two parity bits to be 11:

- after one step one odd event is necessary;
- after two steps two odd events are necessary because 3<4<9.

The corresponding canonical start cylinder is

\[
N\equiv3\pmod4.
\]

The recursively sufficient Cantor core also has the form

\[
N=4Y+3.
\]

Thus the raw overlap factor contains a forced constant factor four.  Define the prefix-normalized amplification

\[
\boxed{\Xi^\circ_{m,H}:=\Xi_{m,H}/4.}
\]

This normalization does not change the exponential rate but explains why the finite repeated-window calibrations naturally cluster near \(\Xi\approx4\), equivalently \(\Xi^\circ\approx1\).

## 6. Exact multiwindow calibration under the stronger L8 rule

A separate exact verifier uses the L=8 residue-maximal rule, which has a slightly weaker asymptotic entropy constant than the phase-aware L7 macro but is convenient for finite block calculations.

Selected exact candidate survivor counts are:

\[
\begin{array}{c|rrrr}
m & H=32&H=64&H=96&H=128\\\hline
20&9981&251&9&1\\
21&20200&474&10&0\\
22&40359&1022&28&0
\end{array}
\]

Thus the m=21 and m=22 small cores are already empty by H=128 under coefficient survival plus local residue maximality.  The exact verifier also computes the complete dyadic language counts, so the same-integer overlap can be calibrated without a statistical independence assumption.

Certificate:

`collatz/src/l8_small_core_multiwindow_overlap_certificate.cpp`.

The observed raw overlap factor remains near the forced value four throughout the bulk-survivor regime; after dividing by the common mod-4 factor, the observed amplification is of order one rather than exponential.  This is finite evidence only, not the remaining theorem.

## 7. Remaining structural target

Stages 1--3 of the credit/renewal program remain closed.  Stage 4 is now reduced to the following weaker theorem:

> **Renewal-conditioned cross-base growth theorem.**  Show that the same-integer overlap amplification between the recursively sufficient ternary-selector core and the coefficient-surviving, locally residue-maximal dyadic language has exponential rate strictly below 7/50.

A proof of the stronger

\[
\Xi_{m,H}=2^{o(H)}
\]

would still be sufficient, but is no longer necessary.

The next proof-level task is to split this amplification into the selector-active prefix and the deterministic renewal tail, and prove that the latter cannot supply a linear-in-H repair budget.
