# Exponent-code / defect bridge and external comparison

Date: 2026-08-10

Status: **DERIVED NOTATIONAL BRIDGE + LITERATURE COMPARISON**

This note compares the current first-crossing defect formalism with the exponent-code viewpoint used in recent Collatz literature. It does not import an external proof claim and does not alter the project’s exact first-crossing results.

## 1. From odd positions to exponent codes

Let

\[
d_0<d_1<\cdots<d_{q-1}
\]

be the odd positions of a first-crossing parity word, with

\[
\kappa_i=\lfloor i\log_2 3\rfloor,
\qquad
z_i=\kappa_i-d_i.
\]

For internal odd-to-odd transitions define

\[
a_i=d_i-d_{i-1}
\qquad(i\ge1).
\]

The mechanical critical code is

\[
a_i^*=\kappa_i-\kappa_{i-1}\in\{1,2\}.
\]

Therefore

\[
\boxed{
a_i=a_i^*-(z_i-z_{i-1}).
}
\]

Thus the defect process `z_i` is exactly the cumulative displacement between the actual exponent code and the mechanical critical exponent code.

This is a change of coordinates only. The project continues to use the time-expanded accelerated map

\[
T(n)=n/2\text{ (even)},\qquad T(n)=(3n+1)/2\text{ (odd)},
\]

while exponent-code papers often use the odd-to-odd accelerated map with one exponent `a_i=v_2(3x_i+1)` per odd step.

## 2. Relation to the 2026 Kramer diagnostic

Oliver Kramer (arXiv:2607.10041, 2026) studies finite exponent codes through three simultaneous compatibility diagnostics:

1. real drift near the critical average exponent `log_2 3`;
2. a small 2-adic forced start representative;
3. a 3-adic endpoint representative compatible with real orbit growth.

The paper explicitly states that this is a diagnostic search framework, not a verification/proof of Collatz.

The present project’s first-crossing setup has a closely related obstruction, but uses different exact objects:

- the coefficient crossing fixes the real drift channel;
- the canonical start `x` is the exact 2-adic representative;
- the endpoint `y` is an actual integer endpoint, not merely an abstract residue;
- the correction `R`, defect process `z_i`, and correction-gap certificates retain the additive `+1` arithmetic exactly.

## 3. Extreme compatibility required at the next resonance

For the next unresolved convergent resonance,

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617,
\]

the Denjoy--Koksma refinement gives the deterministic candidate bound

\[
x<2^{75}.
\]

Thus, by the time the exponent code has accumulated total binary exponent `sigma`, its forced start representative is already the fixed ordinary integer `x` of at most 75 bits.

In any logarithmic normalization of start-representative size by the total exponent scale, this is of order

\[
\frac{75}{\sigma}
<3.45\times10^{-10}.
\]

Likewise

\[
y=\frac{x+S}{1+\delta}<x+S^*<2^{76}
\]

at this layer, so the actual endpoint is also tiny compared with the available `3^q` residue scale.

Kramer’s finite experiments at code lengths 100, 200, and 400 report clearly positive normalized residue rates for random, mechanical, and adaptive codes rather than values approaching zero. This comparison is diagnostic only: it does not supply a lower bound valid for the present enormous code length.

## 4. Project-specific extra condition

The current project also has a condition absent from the external diagnostic search:

\[
S^*-S\ge\frac5{48}N_{\rm def}.
\]

For the `m=46` candidate layer this forces

\[
N_{\rm def}/q<0.084435883,
\]

so more than `91.556%` of the cumulative odd-position coordinates must lie exactly on the mechanical cap.

Therefore a hypothetical candidate must combine all three features:

\[
\boxed{
\text{near-critical mechanical drift}
+
\text{extremely small 2-adic start}
+
\text{very sparse cumulative defects}.
}
\]

This is the current independent proof target.

## 5. Scope discipline

The exponent-code bridge is used for comparison and possible future transfer of external techniques. The following remain project-derived and should be cited separately from Kramer’s work:

- first-crossing correction-gap certificate;
- parity-time cylinder correction range;
- exact-count first-crossing Bellman recurrence;
- Denjoy--Koksma application to the mechanical correction channel;
- defect-run average and defect-level density bounds;
- recursively-sufficient four-block reduction at the next resonance.
