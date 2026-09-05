# DSD Checkpoint-to-Source Transport Audit

**Status:** OPEN

**Scope:** C0/C6 branch specification, checkpoint-surplus provenance, and source-realization transport.

## 1. Audit question

The question is not whether a low-surplus checkpoint computation is internally consistent.

The stronger question is whether every checkpoint state used for branch closure is tied to an exact ordinary source/orbit and whether the resulting source families exhaust precisely the intended branch.

The audited chain is

\[
\boxed{
\text{ordinary source/orbit}
\to
\text{checkpoint applicability and realization}
\to
\text{checkpoint-control representation}
\to
\text{derived completion}
}
\]

and, for branch construction, the proof must also justify the reverse transport from admitted checkpoint states back to exact ordinary-source charts.

## 2. P0 — provenance and symbol identity

### Directly supported checkpoint meaning

Use

\[
s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus}
\]

as the audit notation for the code variable historically named `s`.

The `s=1` Xi/checkpoint note gives the exact local checkpoint condition

\[
\tau_{j_0}\le t_0<\tau_{j_0+1}.
\]

The low-surplus certificate family uses

\[
r=s_{\mathrm{cp}}-1,
\qquad
q_\star=Q0-r,
\]

with `r` interpreted as the number of extra odd ordinals crossed to the left of \(T_0\).

The sampled files use file-local

\[
A0=114{,}208{,}327{,}604,
\qquad
Q0=72{,}057{,}431{,}991.
\]

### Audit verdict

- checkpoint meaning of `s`: **PASS (local provenance)**;
- relation \(r=s_{\mathrm{cp}}-1\): **PASS (certificate-family local)**;
- promotion of file-local `A0`, `Q0` to global canonical constants: **NOT AUTHORIZED**;
- identity \(s_{\mathrm{cp}}=A_0-j_\star\): **NOT ESTABLISHED**.

The latter must not be used as an upstream global definition until a source-level provenance derivation is supplied.

## 3. P1 — applicability and activation

A checkpoint predicate is not automatically a Boolean predicate on every ordinary source.

Before evaluating a checkpoint-surplus condition, the proof must establish that the relevant checkpoint exists and that all prerequisite orbit data have been reached.

Audit states must therefore distinguish:

1. prerequisite not satisfied / not applicable;
2. applicable but undefined;
3. defined and zero;
4. defined and nonzero/value-bearing.

### Verdict

**OPEN for global branch use.**

Local certificates implement concrete checkpoint computations, but no global branch theorem currently proves that every candidate counterexample reaches exactly the checkpoint interface required by the surplus classification.

## 4. P2 — same-source realization

Introduce an explicit relation

\[
R(x,\sigma)
\]

meaning that ordinary source \(x\) generates the orbit data represented by checkpoint state \(\sigma\).

The following are insufficient replacements:

- CRT compatibility;
- equal \((h,S)\) or other compressed control coordinates;
- equal parity/macroblock descriptors;
- equal terminal defect or projective observation;
- equal endpoint-lattice residue;
- equal aggregate/checksum.

### Required theorem

\[
A_s(\sigma)\land R(x,\sigma)
\Longrightarrow
x\in\mathcal D_s.
\]

### Verdict

**OPEN for \(s_{\mathrm{cp}}\ge2\) and any new global sector.**

The currently closed Route-B sector has its own source-preserving construction; that downstream result does not automatically transport to other surplus sectors.

## 5. P3 — exact ordinary-source charts

For each branch/surplus sector, source charts should take the form

\[
\Phi_{s,\lambda}:I_{s,\lambda}\to\mathbb N,
\qquad
\mathcal D_s=\bigcup_\lambda\Phi_{s,\lambda}(I_{s,\lambda}).
\]

For exact branch use, both directions are needed:

\[
A_s(\sigma)\land R(x,\sigma)
\Rightarrow
x\in\mathcal D_s,
\]

and

\[
x\in\mathcal D_s
\Rightarrow
\exists\sigma:\ A_s(\sigma)\land R(x,\sigma),
\]

with the exact branch prerequisites attached.

### Verdict

**OPEN.**

The low-surplus checkpoint envelopes currently give control/budget information, not a completed theorem identifying the exact ordinary-source domain for every live \(s_{\mathrm{cp}}\ge2\) sector.

## 6. P4 — quotient/compression sufficiency

If a source-sensitive state \(S\) is replaced by a compressed state \(Q(S)\), every remaining predicate \(P_i\) used in the proof must be reconstructible or at least invariant on quotient fibres:

\[
P_i(S)\iff\widehat P_i(Q(S))
\]

where exact reflection is needed, or minimally

\[
Q(S_1)=Q(S_2)
\Rightarrow
P_i(S_1)=P_i(S_2).
\]

### Verdict

**CONDITIONAL / PER-COMPRESSION PROOF REQUIRED.**

No blanket inference from equal compressed coordinates to equal source payload is allowed.

## 7. P5 — representation versus branch origin

DSD audit layers:

- **L0:** ordinary source/orbit;
- **L1:** applicability, prerequisites, definition status, same-source realization;
- **L2:** checkpoint-control representation, including \(s_{\mathrm{cp}}\), \(r\), \(q_\star\), Hensel budgets, packed suffixes;
- **L3:** derived completion, including terminal/projective/endpoint data.

A branch difference that appears only at L2 or L3 is not automatically an L0 source branch.

### Verdict

**PASS as an audit rule; OPEN as a global branch theorem.**

This rule blocks treating `s>=2`, Route-A labels, or downstream descriptor differences as exhaustive source branches before their source predicates are proved.

## 8. P6 — external finite-range closure interface

The accepted external-dependency path provides a finite verified range at least through

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

A new sector may inherit that closure only after proving an ordinary-source inclusion such as

\[
\mathcal D_s\subseteq[1,L_{RS}].
\]

The existing Route-B source bound is branch-specific and cannot be copied to another sector.

### Verdict

- current Route-B physical sector, external-dependency path: **CLOSED**;
- new surplus sectors: **BLOCKED UNTIL SOURCE-DOMAIN THEOREM**;
- optional self-contained Route-B reconstruction: **OPEN**.

## 9. P7 — branch cover and overlap accounting

For every live branch \(B_\alpha\), require an exact predicate

\[
x\in B_\alpha\iff P_\alpha(x,\mathcal O_x).
\]

Then prove

\[
CE\subseteq\bigcup_{\alpha\in A}B_\alpha.
\]

If branches overlap, the overlap must be explicit and harmless. If they are claimed to partition candidate counterexamples, prove disjointness.

### Verdict

- Route-A exact entrance predicate: **UNSPECIFIED / OPEN**;
- checkpoint-surplus source branches for all \(s_{\mathrm{cp}}\ge2\): **OPEN**;
- global cover: **OPEN**.

## 10. Dependency order

The permitted order is

\[
\boxed{
\text{checkpoint provenance}
\to
\text{applicability}
\to
\text{same-source realization}
\to
\text{exact source charts}
\to
\text{branch closure}
\to
\text{global cover}
}
\]

External finite verification may enter only at `branch closure`, after exact source-domain transport.

## 11. Current audit table

| Item | Status |
|---|---|
| checkpoint-surplus local provenance | PASS |
| exact local `s=1` checkpoint condition | PASS |
| \(r=s_{\mathrm{cp}}-1\) in low-surplus certificates | PASS |
| \(s_{\mathrm{cp}}=A_0-j_\star\) | NOT ESTABLISHED |
| global checkpoint applicability theorem | OPEN |
| same-source realization transport for \(s_{\mathrm{cp}}\ge2\) | OPEN |
| exact ordinary-source charts for \(s_{\mathrm{cp}}\ge2\) | OPEN |
| Route-A exact predicate | OPEN |
| global branch cover | OPEN |
| current Route-B physical sector, external path | CLOSED |
| global Collatz conclusion | OPEN |

## 12. Linked theorem obligation

See:

`collatz/theorems/CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`

This audit does not assert the theorem. It records the exact missing implications that must be proved before low-surplus checkpoint control can be promoted to global source-branch closure.
