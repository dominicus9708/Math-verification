# Staged global-closure status after the height-credit cocycle

Date: 2026-08-19

Status: **Stages 1--3 structurally closed; Stage 4 reduced to one weaker cross-base growth inequality.**  This is a proof-program reduction, not a proof of the Collatz conjecture.

## Stage 1 — coordinate alignment: closed

The depth-28 p=8 value `290` was audited against the ordinary gate-credit coordinate.

Exact result:

\[
\Delta_{\rm return}=2^{18}\cdot290,
\qquad
\Delta_{\rm end}=3^{11}\cdot290.
\]

Thus `290` is a projective/common-suffix normalized credit, not the ordinary integer gate credit used by the G81/G82 Hensel recurrence.

After eleven forced ternary zero lifts its gate-normalized primitive value would be

\[
4^{11}\cdot290=1,216,348,160,
\]

so the old bounded-credit scan `1<=delta<=397` cannot be invoked by direct substitution.

Certificate:

`collatz/src/m45_p8_projective_credit_alignment_certificate.py`.

## Stage 2 — finite depth-28 renewal syndrome: closed

The exact q-sliced depth-28 Hensel language was regenerated from the repository algorithm.  Its union has

\[
1,976,972
\]

retained canonical residues.

The ordinary first-defect hard sizes are

\[
\begin{array}{c|rrrrrrrrrr}
p&2&5&8&10&13&16&18&21&24&27\\\hline
|S_p|&1623807&286895&51825&11763&2151&404&100&20&5&1.
\end{array}
\]

Under one fixed immediate-return normalization, all ordinary renewal translations are exact set equalities except

\[
p=8\to10:
\quad 14,443=11,763+2,680,
\]

and

\[
p=16\to18:
\quad125=100+25.
\]

Call the two exceptional states \(E_{10}\) and \(E_{18}\).  Auditing every finite first-return group of \(E_{10}\) produces only two exceptional normalized descendants:

\[
\boxed{
E_{10}\to E_{18},
\qquad
E_{10}\to E_{21},\quad |E_{21}|=5.
}
\]

Every finite return from \(E_{18}\) or \(E_{21}\) normalizes back into an ordinary later hard state.  Thus the recursive depth-28 syndrome graph has only three named exceptional states

\[
\boxed{E_{10},E_{18},E_{21}}.
\]

The no-return-at-depth-28 counts are

\[
865,\quad7,\quad1,
\]

respectively.  They are open positive-height excursions, not permanent new syndrome types.

Certificate:

`collatz/src/m45_depth28_renewal_syndrome_graph_certificate.cpp`.

This supersedes the earlier exploratory `2680->529->125->25->5` interpretation, which is not reproduced under the single consistent normalization used by the exact graph certificate.

## Stage 3A — height/credit exchange: closed

For each of the complete twenty length-19 Sturmian factor types, all binary orientations were enumerated against incoming relative height \(H\).

For every same-q surviving pair,

\[
\boxed{
\frac{|R_u-R_w|}{3^{q+H}}<8.
}
\]

The exact worst value is

\[
\frac{3,909,437}{531,441}<8.
\]

If the pair is in one full-Hensel correction class, so

\[
R_u-R_w=3^q\Delta,
\]

then

\[
\boxed{|\Delta|<7\,3^H.}
\]

The exact worst normalized value is \(55/9<7\).

Certificate:

`collatz/src/h19_allfactor_height_credit_source_certificate.cpp`.

## Stage 3B — phase-cocycle normalization: closed

For one 19-step factor let \(Q\in\{11,12\}\) be its mechanical odd count, \(q\) the actual odd count, and

\[
H'=H+q-Q.
\]

The ordinary credit concatenation law becomes, after defining

\[
\chi=\frac{\delta_{\rm credit}}{3^H},
\]

\[
\boxed{
\chi_L
=
\frac{R_u-R_w}{3^{q+H}}
+
\frac{2^{19}}{3^Q}\chi_R.
}
\]

The actual q and the height change disappear from the homogeneous multiplier.

At the exact G81/G82 phase-return scale, with

\[
\varepsilon=12-19\log_3 2,
\qquad
\delta=1-81\varepsilon,
\]

the gate multiplier is exactly

\[
\boxed{A_{\rm gate}=3^{x'-x}}
\]

for the first-return phase map \(x\mapsto x'\).

Therefore

\[
\boxed{
\Psi:=3^x\chi
}
\]

satisfies a purely additive recurrence.  The exact local source theorem and the mechanical prefix discrepancy give

\[
|S_{\rm gate}|<1968,
\]

and hence

\[
\boxed{
|\Psi_L-\Psi_R|<5904.
}
\]

Across n first-return gates,

\[
\boxed{
|\Psi_0-\Psi_n|<5904n.
}
\]

Thus at renewal height H=0 the ordinary predecessor-credit amplitude is only \(O(n)\); its excess information is \(O(\log n)\), not linear in n.

Certificate and proof note:

- `collatz/src/height_credit_phase_cocycle_certificate.py`;
- `collatz/notes/2026-08-19-height-credit-phase-cocycle-globalization.md`.

## Stage 3C — deterministic local residue-maximality: closed

The unrestricted length-19 binary cube has exact full-Hensel class counts

\[
(c_q)_{q=0}^{19}
=
(1,2,6,18,54,162,486,1458,4352,11692,
23557,31072,27469,17527,8411,3048,817,154,19,1).
\]

The maximum ordinary credit difference inside any full-Hensel class is

\[
\boxed{\Delta_{\max}=87,381.}
\]

If a hypothetical minimal counterexample has \(N>87,381\), every later state is at least N.  If an actual 19-step word w were not the maximum-correction representative of its full-Hensel class, there would be a word u and a positive \(\Delta\le87,381\) with

\[
R_u-R_w=3^q\Delta.
\]

Starting u at \(x-\Delta>0\) gives

\[
\frac{3^q(x-\Delta)+R_u}{2^{19}}
=
\frac{3^qx+R_w}{2^{19}},
\]

so the smaller start merges exactly with the counterexample after the block, contradicting minimality.

Hence every block of a sufficiently large minimal counterexample must be a **residue-maximal representative**.

Certificate:

`collatz/src/h19_unrestricted_residue_maximality_certificate.cpp`.

## Stage 3D — residue-maximal language entropy: closed

Use the exact weight

\[
z=\frac54.
\]

For a Q=12 mechanical factor define

\[
P_{12}(z)=\sum_{q=0}^{19}c_qz^{q-12}.
\]

The exact value is

\[
\boxed{
P_{12}(5/4)
=
\frac{477477466377643529}{4000000000000}
<2^{17}.
}
\]

For Q=11,

\[
P_{11}(5/4)=\frac54P_{12}(5/4)<2^{18}.
\]

Since z>1, endpoint positive height only increases the weighted count.  Dropping all intermediate nonnegativity constraints also only enlarges the language.  Therefore these polynomials give rigorous upper bounds on the number of locally residue-maximal coefficient-surviving block words.

A first-return gate contains exactly one Q=11 factor:

\[
971=80\cdot12+11,
\qquad
983=81\cdot12+11.
\]

Thus the complete binary languages satisfy the conservative exact bit ceilings

\[
\boxed{
G81:\quad \#\mathcal L_{81}<2^{1378}
\quad\text{inside }2^{1539},
}
\]

\[
\boxed{
G82:\quad \#\mathcal L_{82}<2^{1395}
\quad\text{inside }2^{1558}.
}
\]

Therefore the deterministic local-maximality exclusion rates are at least

\[
\eta_{81}>\frac{161}{1539},
\qquad
\eta_{82}>\frac{163}{1558}.
\]

Put

\[
\boxed{
\eta_*:=\frac{161}{1539}
\approx0.1046133853.
}
\]

Certificate:

`collatz/src/h19_residue_maximal_language_entropy_certificate.py`.

## Stage 4 — remaining global bridge

Let \(\mathcal C_m\) be the reduced ternary-selector candidate family, \(|\mathcal C_m|\le2^m\).  Let \(\mathcal L_H\) be the dyadic parity-prefix language satisfying coefficient survival and the mandatory local residue-maximality rule through a gate-aligned horizon H.

Define the exact same-integer overlap amplification

\[
\Xi_{m,H}
:=
\frac{
|\mathcal C_m\cap\mathcal L_H|/|\mathcal C_m|
}{
|\mathcal L_H|/2^H
}.
\]

The residue-maximal language theorem gives, up to gate-boundary constants,

\[
\frac{|\mathcal L_H|}{2^H}
\le
2^{-\eta_*H+O(1)}.
\]

Hence

\[
\log_2|\mathcal C_m\cap\mathcal L_H|
\le
m-\eta_*H+\log_2\Xi_{m,H}+O(1).
\]

Therefore the remaining sufficient cross-base theorem is only

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log_2\Xi_{m,H}}{H}
<\eta_*
\approx0.1046133853
}
\]

uniformly on the reduced candidate core in the scaling regime used by the proof decomposition.

This is substantially weaker than the previous formation-only tolerance

\[
0.05004447281.
\]

If the stronger subexponential overlap bound

\[
\Xi_{m,H}=2^{o(H)}
\]

holds, then any asymptotic horizon

\[
\boxed{
H>Cm,
\qquad
C>\frac1{\eta_*}
=\frac{1539}{161}
\approx9.55900621
}
\]

forces finite extinction of the integer candidate mass.

The prior formation-only constant was approximately 19.98223, so deterministic local residue-maximality has reduced the required linear-horizon slope by more than a factor of two.

## Finite calibration of Stage 4

For the current m=45 depth-28 hard cylinders, the exact selector distribution already proves:

- pointwise density amplification `<129/128` for every dyadic hard subset in the four remaining p-cylinders;
- full TV `<1/1600`;
- parent-by-parent binary child imbalance `<1/160`;
- one-window repair budget `<1/80` bit.

These are strong finite calibrations in the required direction.  They do not yet prove that the same bound survives arbitrary repeated conditioning at later renewal windows.

Thus the sole main structural target after Stages 1--3 is now:

> **Renewal-conditioned cross-base transversality theorem.**  Prove that the same-integer overlap amplification of the ternary selector core with the residue-maximal dyadic renewal language has exponential rate strictly below \(161/1539\), preferably zero.

The height/credit amplitude, projective-credit coordinate, local predecessor relation, and finite depth-28 syndrome graph are no longer independent unresolved exponential channels.
