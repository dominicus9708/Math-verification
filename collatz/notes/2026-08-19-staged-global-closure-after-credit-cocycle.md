# Staged global-closure status after the height-credit cocycle

Date: 2026-08-19

Correction date: 2026-08-20

Status: **Stages 1, 2, 3A and 3B remain structurally closed. Stage 3C is corrected to a local/pullback-qualified theorem. The unconditional Stage 4 front is coefficient-only cross-base transversality.** This is a proof-program reduction, not a proof of the Collatz conjecture.

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

The exact q-sliced depth-28 Hensel language has 1,976,972 retained canonical residues.

The ordinary first-defect hard sizes are

\[
\begin{array}{c|rrrrrrrrrr}
p&2&5&8&10&13&16&18&21&24&27\\\hline
|S_p|&1623807&286895&51825&11763&2151&404&100&20&5&1.
\end{array}
\]

Under one fixed immediate-return normalization, all ordinary renewal translations are exact set equalities except

\[
p=8\to10:\quad14,443=11,763+2,680,
\]

and

\[
p=16\to18:\quad125=100+25.
\]

The recursive exceptional graph has only

\[
\boxed{E_{10},E_{18},E_{21}},
\]

with exceptional finite edges

\[
E_{10}\to E_{18},
\qquad
E_{10}\to E_{21}.
\]

Open no-return counts at depth 28 are 865, 7 and 1.

Certificate:

`collatz/src/m45_depth28_renewal_syndrome_graph_certificate.cpp`.

## Stage 3A — height/credit exchange: closed

For every complete length-19 Sturmian factor type, every incoming height H and every same-q surviving pair,

\[
\boxed{
\frac{|R_u-R_w|}{3^{q+H}}<8.
}
\]

The exact worst value is

\[
\frac{3,909,437}{531,441}<8.
\]

For a full-Hensel pair,

\[
R_u-R_w=3^q\Delta,
\]

and

\[
\boxed{|\Delta|<7\,3^H.}
\]

The exact worst normalized value is \(55/9<7\).

Certificate:

`collatz/src/h19_allfactor_height_credit_source_certificate.cpp`.

## Stage 3B — phase-cocycle normalization: closed

For a length-19 factor with mechanical odd count \(Q\in\{11,12\}\), actual odd count q and relative heights H,H',

\[
H'=H+q-Q.
\]

With

\[
\chi=\frac{\delta_{\rm credit}}{3^H},
\]

the credit recurrence becomes

\[
\boxed{
\chi_L
=
\frac{R_u-R_w}{3^{q+H}}
+
\frac{2^{19}}{3^Q}\chi_R.
}
\]

At the exact G81/G82 first-return scale the homogeneous multiplier is a phase coboundary. With

\[
\Psi=3^x\chi,
\]

the gate recurrence is additive and satisfies

\[
\boxed{|\Psi_L-\Psi_R|<5904.}
\]

Across n first-return gates,

\[
\boxed{|\Psi_0-\Psi_n|<5904n.}
\]

Hence renewal-boundary predecessor-credit amplitude is only O(n), with O(log n) excess information rather than a positive exponential repair rate.

Certificates:

- `collatz/src/height_credit_phase_cocycle_certificate.py`;
- `collatz/notes/2026-08-19-height-credit-phase-cocycle-globalization.md`.

## Stage 3C — corrected: local merge theorem + prefix-pullback requirement

The unrestricted length-19 cube still has exact full-Hensel class counts

\[
(c_q)_{q=0}^{19}
=
(1,2,6,18,54,162,486,1458,4352,11692,
23557,31072,27469,17527,8411,3048,817,154,19,1),
\]

and maximum local ordinary credit

\[
\boxed{\Delta_{\max}=87,381.}
\]

For a same-class pair,

\[
R_u-R_w=3^q\Delta>0,
\]

the exact local identity

\[
\frac{3^q(x-\Delta)+R_u}{2^{19}}
=
\frac{3^q x+R_w}{2^{19}}
\]

is valid.

The previous conclusion that every later block of a sufficiently large minimal counterexample must therefore be residue-maximal is withdrawn. If the minimal counterexample is N and a later block begins at \(x=T^s(N)\), minimality only gives \(x\ge N\). A direct local contradiction requires

\[
\boxed{\Delta>x-N.}
\]

More generally a local credit must be pulled back through the actual prefix to an integer smaller original start. If the actual and alternate prefixes have common odd count a and corrections \(C_P,C_{P'}\), the required original-start credit d obeys

\[
\boxed{
3^a d=2^s\Delta+C_{P'}-C_P.
}
\]

Therefore Stage 3C is now classified as:

- local Hensel merge identity: closed;
- finite local credit bounds: closed;
- unconditional repeated residue-maximality: not established;
- prefix-pullback qualification: open/global.

Certificates and note:

- `collatz/src/h19_unrestricted_residue_maximality_certificate.cpp`;
- `collatz/src/stage3c_pullback_headroom_certificate.py`;
- `collatz/notes/2026-08-20-stage3c-pullback-correction-and-safe-stage4.md`.

## Stage 3D — residue-maximal entropy: retained conditionally

The H19 and L7 residue-maximal language counts remain exact combinatorial statements for their respective conditional languages.

They may be used as strengthening lemmas only after a theorem places the relevant trajectories inside the repeated residue-maximal language. Until then their 1/9, 7/50, and related optimized entropy gains are not part of the unconditional Stage 4 budget.

## Stage 4 — unconditional global bridge

Let

\[
\mathcal C_m
=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
a_i\in\{0,1\}
\right\}
\]

be the reduced ternary-selector core.

Let \(\mathcal B_H\) be the coefficient-survival dyadic language satisfying

\[
3^{q_k}\ge2^k
\qquad(1\le k\le H).
\]

Its unconditional exclusion rate is

\[
\boxed{
\eta_{\rm coeff}
=1-H_2(\log_3 2)
\approx0.05004447.
}
\]

Define

\[
\Xi^{\rm coeff}_{m,H}
=
\frac{|\mathcal C_m\cap\mathcal B_H|/|\mathcal C_m|}
{|\mathcal B_H|/2^H}.
\]

Because both families force \(N\equiv3\pmod4\), use

\[
\boxed{\Xi^{\circ,\rm coeff}_{m,H}=\Xi^{\rm coeff}_{m,H}/4.}
\]

The preferred sufficient theorem is

\[
\boxed{
\Xi^{\circ,\rm coeff}_{m,H}=2^{o(H)}.
}
\]

Under this stronger form, any asymptotic horizon

\[
\boxed{
H>Cm,
\qquad
C>\frac1{\eta_{\rm coeff}}
\approx19.9823
}
\]

forces finite extinction up to fixed boundary constants.

## Finite calibration that remains unconditional

The m=45 depth-28 selector distribution proves, independently of repeated residue-maximality:

- conditional TV < 1/1600 in each remaining first-defect cylinder;
- hard-set-independent one-window amplification < 76/75 for hard fractions at least 3/64;
- one-window repair budget < 1/50 bit;
- strong parent/child selector balance in the companion transport calculations.

The exact mass-transport identity

\[
2C_{\rm next}=2C-D+K,
\qquad |K|\le U,
\]

gives

\[
\boxed{
C-C_{\rm next}\ge\frac{D-U}{2}
}
\]

whenever \(U<D\). The checked m=44 boundary depths satisfy this positive-loss condition.

These calculations remain on the safe unconditional path.

## Revised remaining theorem

> **Renewal-conditioned coefficient-language transversality theorem.** Prove that repeated conditioning on survived dyadic/renewal information cannot make the reduced ternary-selector distribution acquire a positive exponential same-integer concentration inside the coefficient-survival language.

A proof of subexponential normalized overlap is sufficient. A future prefix-pullback theorem may then reintroduce the stronger conditional residue-maximal entropy savings.
