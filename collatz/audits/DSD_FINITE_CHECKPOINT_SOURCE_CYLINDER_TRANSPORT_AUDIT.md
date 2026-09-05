# DSD audit — finite checkpoint predicate to ordinary-source cylinders

Status: **CORE PASS / global surplus application still partial.**

This audit reviews `../theorems/FINITE_CHECKPOINT_PREDICATE_SOURCE_CYLINDER_TRANSPORT.md` against the current DSD source-preservation rules.

## 1. Audit question

Can a finite checkpoint predicate be treated as an ordinary-source branch without losing same-source provenance?

Answer:

\[
\boxed{\text{YES inside a supplied exact finite parent source family, by exact valuation-cylinder refinement.}}
\]

This does not mean that every currently named global surplus sector is already specified or globally covered.

## 2. Layer separation

### L0 — ordinary source/orbit

Start from

\[
X(m)=x+A m,
\qquad A\text{ odd},
\qquad m\in I\cap\mathbb Z.
\]

The parameter interval and affine source formula are retained throughout refinement.

### L1 — event realization / activation

Each next odd event is selected by the exact condition

\[
v_2(Y)=a.
\]

This is an active ordinary-orbit predicate, not a derived terminal observation.

### L2 — checkpoint representation

Finite ordered odd-event positions, parity-prefix descriptors, checkpoint counts, and a checkpoint-surplus predicate may be represented here **only after their exact definitions are supplied**.

### L3 — derived completion

Surplus tax, defect budgets, terminal defects, projective observations, and endpoint coordinates derived after checkpoint selection remain derived/completion data.

## 3. Provenance preservation

At one valuation step, odd affine coefficient invertibility modulo `2^(a+1)` gives one exact parameter residue cylinder.

Repeated refinement gives

\[
m=\rho_{\mathbf a}+2^{H(\mathbf a)}k
\]

and hence

\[
X=R_{\mathbf a}+A2^{H(\mathbf a)}k.
\]

The source formula is never replaced by a marginal checkpoint label.

Therefore the path

\[
\text{source}
\to
\text{valuation word}
\to
\text{checkpoint predicate}
\]

preserves source identity.

Verdict: **PASS**.

## 4. Reflection

The construction is not merely forward-preserving.

If a source realizes a fixed finite valuation word, it must lie in the unique nested residue cylinder selected by the successive exact valuation congruences.

Thus

\[
X\text{ realizes }w
\iff
X\in\Phi_w(I_w).
\]

For an exact finite checkpoint predicate `P`,

\[
X\text{ satisfies }P
\iff
X\in\bigsqcup_{w\in\mathcal W_P}\Phi_w(I_w).
\]

This is the reflection property needed to use the cylinder union as an exact branch **relative to the parent source family**.

Verdict: **PASS**.

## 5. Branching audit

The first mathematical source branching occurs when two ordinary sources satisfy different exact finite orbit-prefix predicates, not merely when a later control coordinate differs.

Therefore:

- different exact valuation/parity prefixes: genuine source-level branch distinction;
- different checkpoint-surplus sectors: genuine source-level distinction **only once the sector predicate itself is exactly defined on the orbit prefix**;
- different `r=s_cp-1`, tax, budget, defect, or projective observation: not an additional independent branch merely because the values differ.

Verdict: **PASS with surplus-definition precondition**.

## 6. Disjointness

Distinct finite valuation words differ at a first valuation event and hence occupy disjoint exact residue cylinders at that stage.

Thus the source-cylinder union over exact prefix descriptors is disjoint after empty children are removed.

This is stronger than a mere union bound and avoids multiplicity ambiguity inside one fixed parent family.

Verdict: **PASS**.

## 7. Truncated horizon

A finite checkpoint horizon may end before the next odd event.  The terminal no-event condition is

\[
v_2(Y)\ge\ell
\iff
Y\equiv0\pmod{2^\ell}.
\]

Because the active affine coefficient is odd, this is again one exact dyadic parameter cylinder.

Therefore the theorem does not require the finite horizon to terminate on an odd event.

Verdict: **PASS**.

## 8. Compression warning

The exact theorem may generate an astronomically large number of cylinders at a large checkpoint horizon.

Any later compression

\[
Q:\mathcal S\to\mathcal Q
\]

must satisfy, for every remaining source-sensitive predicate `P_i`,

\[
P_i(S)\iff\widehat P_i(Q(S))
\]

whenever exact branch decisions use `P_i`.

Equal aggregate counts or checkpoint labels are insufficient.

Verdict: **compression remains OPEN unless separately proved admissible**.

## 9. Global-surplus consequence

The previous transport obligation contained two logically different gaps:

1. **structural transport mechanism:** how an exact finite checkpoint predicate maps to ordinary sources;
2. **global surplus specification:** what the exact `s_cp>=2` predicate is, what parent source family it acts on, and whether those parent families cover all relevant candidate counterexamples.

The new theorem closes (1) for exact finite parent families.

It does **not** close (2).

Accordingly G9 should no longer be described as lacking a source-preserving mechanism in principle.  Its live content is now:

- recover/prove the exact general `s_cp` orbit-prefix predicate;
- specify the upstream exact source-family cover;
- instantiate the finite transport theorem;
- compress or bound the resulting exact source-cylinder union without losing provenance;
- prove any source upper bound needed for external closure.

## 10. Relation to late activation/checkpoint join

The finite checkpoint transport theorem maps source prefixes to source cylinders.

`SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md` instead joins an already provenanced late activation cylinder to a terminal suffix and ordinary checkpoint `Z`.

These are successive interfaces, not statistically independent filters.

Verdict: **PASS / no double counting**.

## 11. Final verdict

### CLOSED

- finite checkpoint predicate -> exact source-cylinder union inside one exact finite parent family;
- reflection from those cylinders to the checkpoint predicate;
- source-disjointness of distinct exact finite prefix descriptors;
- same-source provenance through the transport.

### STILL OPEN

- general `s_cp>=2` predicate provenance/definition;
- global or otherwise sufficient parent source-family cover;
- practical exact compression at the A0 horizon;
- source-domain upper bounds for new sectors;
- Route-A predicate;
- global branch cover;
- Collatz.

No global conclusion is promoted by this audit.
