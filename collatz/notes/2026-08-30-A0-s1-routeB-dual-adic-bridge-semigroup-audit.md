# A0 s=1 Route-B finite dual-adic bridge semigroup audit

Date: 2026-08-30

Status: **G3 fixed-resolution correction congruence CLOSED; G4 adaptive interior-language decoder remains OPEN**.

## 1. Why another state is needed

The dual-adic and lazy-frontier certificates show that shallow start and end constraints can be pushed to small opposite-facing boundary nodes.  That leaves the interior bridge.

At any fixed boundary resolution `(K,L)`, the interior correction can be represented without its expanded parity word.

Let

\[
M_{K,L}=2^K3^L.
\]

For a block `W`, define

\[
S_{K,L}(W)=\bigl(A(W),B(W),C(W)\bigr)\pmod{M_{K,L}},
\]

where

\[
A(W)=3^{q(W)},\qquad B(W)=2^{h(W)}.
\]

## 2. Exact semigroup composition

For `W=UV`,

\[
A(UV)=A(U)A(V),
\]

\[
B(UV)=B(U)B(V),
\]

and the correction law gives

\[
C(UV)=A(V)C(U)+B(U)C(V).
\]

Therefore

\[
\boxed{
S(UV)=
\left(
A_UA_V,
B_UB_V,
A_VC_U+B_UC_V
\right)
\pmod M
}.
\]

This depends only on the two child states.  Consequently equality of `S_{K,L}` states is a two-sided finite congruence of parity-word concatenation at that fixed resolution.

This is stronger than merely storing two endpoint residues: the state is closed under arbitrary further block composition.

## 3. Boundary equivalence by CRT

If `h(W)>=K` and `q(W)>=L`, then

\[
D_K(W)=-C(W)A(W)^{-1}\pmod{2^K},
\]

\[
E_L(W)=C(W)B(W)^{-1}\pmod{3^L}.
\]

Conversely, knowing `A`, `B`, `D_K`, and `E_L` determines

\[
C\pmod{2^K}
\]

and

\[
C\pmod{3^L},
\]

hence a unique

\[
\boxed{C\pmod{2^K3^L}}
\]

by the Chinese remainder theorem.

Thus the dual boundary pair and the bridge correction coordinate are two exact views of the same fixed-resolution information once the exponent metadata are retained.

## 4. Independent certificate

New source:

`collatz/src/A0_s1_routeB_dual_adic_bridge_semigroup_certificate.py`

Results:

- arbitrary parity words through depth 9: `1,022`;
- split composition checks: `35,860`;
- boundary decoding checks: `2,630`;
- CRT round-trip checks: `2,630`;
- projective refinement checks: `9,198`;
- explicit associativity checks: `2,808`.

The resolution chain includes the current `(27,28)` checkpoint exposure point and larger resolutions, verifying that larger bridge states project exactly onto smaller ones.

## 5. Primary 27 x 28 state

At

\[
(K,L)=(27,28),
\]

\[
M=2^{27}3^{28}
=3,070,471,107,232,407,748,608.
\]

All 129 nodes of the existing Christoffel DAG have distinct bridge states at this resolution.

For the base block `L`, the exact state is

\[
S_{27,28}(L)=
(
1,610,141,332,549,784,591,097,
565,366,337,311,908,823,040,
2,684,321,817,012,090,078,622
).
\]

It decodes to the same boundary residues found independently by the lazy-frontier certificate:

\[
D_{27}(L)=87,757,810,
\]

\[
E_{28}(L)=2,158,791,402,581.
\]

The CRT round trip reconstructs the correction component of the bridge state exactly.

## 6. Direct finite-congruence regression

A semigroup homomorphism already proves the congruence algebraically.  To audit the implementation independently, small resolutions were chosen where distinct parity words actually collide in the same finite state.

The certificate found `145` equal-state collision pairs and appended every right extension through length 3.  All `2,175` extension checks preserved equality.

This explicitly tests the operational statement

\[
S(U)=S(U')\Longrightarrow S(UV)=S(U'V)
\]

on genuine collisions rather than only on distinct states.

## 7. Important limitation

The existence of a finite congruence at fixed `(K,L)` does **not** imply that the admissible Route-B correction language is recognized by that congruence.

A finite quotient can identify two words that have the same modular correction state but differ in:

- deeper correction information;
- pure-ballot legality;
- first-passage structure;
- renewal / formation compatibility;
- eventual same-orbit connectivity.

Therefore the following implication is rejected:

\[
S_{27,28}(W)=S_{27,28}(W_{target})
\quad\not\Rightarrow\quad
W\in\mathcal C_{pre}.
\]

What is now available is a rigorous finite **correction-sector** quotient that an adaptive decoder can refine when a collision survives.

## 8. Projective adaptive route

Because

\[
S_{K',L'}(W)\bmod 2^K3^L=S_{K,L}(W)
\]

whenever `K<=K'` and `L<=L'`, the decoder need not restart when a shallow state matches.

It may proceed by exact refinement:

\[
(27,28)
\to (K_1,L_1)
\to (K_2,L_2)
\to\cdots
\]

and retain every previously established residue automatically.

This gives the next G4 design target: an adaptive bridge decoder that raises resolution only on surviving interior blocks and intersects the correction quotient with the already-certified ballot state.

## 9. Formation / Axis / DSD audit

### Formation Axiom System

The finite bridge state is formed only from child states and the exact concatenation operation.  No hidden expanded word is introduced.

### Axis Property

Start-facing dyadic and end-facing ternary information are joined through one CRT-compatible correction coordinate while preserving their distinct boundary roles.

### DSD

- fixed-resolution correction semigroup: ✅ CLOSED;
- finite congruence property: ✅ CLOSED;
- CRT equivalence with dual boundaries: ✅ CLOSED;
- projective refinement across resolutions: ✅ CLOSED;
- quotient recognizes full admissible Route-B language: OPEN;
- target-aware adaptive interior decoder: OPEN;
- G5 universal membership verdict: OPEN;
- Collatz conjecture: OPEN.

## 10. Updated status

- `G1`: CLOSED;
- `G2`: CLOSED;
- `G3`: **fixed-resolution correction congruence now CLOSED**; combined correction+ballot finite recognizer remains OPEN;
- `G4`: block jump, dual localization, lazy frontier, and finite bridge state CLOSED; **adaptive interior-language decoder OPEN**;
- `G5`: OPEN.

The next calculation should combine projective bridge refinement with the exact phase-critical ballot summary, rather than increasing a shallow brute-force radius.
