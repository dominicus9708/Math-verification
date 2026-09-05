# Global Branch Specification

**Status:** OPEN — canonical specification scaffold, not a global completeness theorem.

## 1. Purpose

This file is the single conservative interface between hypothetical ordinary Collatz counterexample sources and the branch-local calculations in this repository.

A branch is admitted here only when it has an exact source/orbit predicate or is explicitly marked `UNSPECIFIED`.

A branch label, checkpoint label, control coordinate, compressed state, or downstream terminal observation is **not** by itself a source-level branch definition.

Let

\[
CE:=\{x\in\mathbb N_{>0}:x\text{ is a hypothetical positive Collatz counterexample start}\}.
\]

For each source-level branch \(B_\alpha\), the required definition is

\[
\boxed{x\in B_\alpha\iff P_\alpha(x,\mathcal O_x)}.
\]

The eventual global theorem must prove

\[
\boxed{CE\subseteq\bigcup_{\alpha\in A}B_\alpha.}
\]

This file does not yet prove that cover.

## 2. Canonical audit notation

To avoid conflict with older bare `s` notation, use

\[
s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus}
\]

for the directly inspected checkpoint-control quantity.

The locally recorded `s=1` checkpoint condition is

\[
\tau_{j_0}\le t_0<\tau_{j_0+1}.
\]

The low-surplus certificate family uses

\[
r=s_{\mathrm{cp}}-1.
\]

The identity

\[
s_{\mathrm{cp}}=A_0-j_\star
\]

is **not part of this canonical specification** unless and until a separate ordinary-orbit provenance theorem establishes it.

The lower-case checkpoint surplus `s_cp` is distinct from the upper-case Route-B persistent source-control coordinate `S`.

## 3. Source-branch table

| branch id | exact entrance/source predicate | checkpoint/control status | ordinary-source domain | closure status | classification |
|---|---|---|---|---|---|
| `B_cp1_RouteB_current` | exact current Route-B predicate/domain supplied by the existing `A0,s=1,Route-B` source-preserving stack | local `s_cp=1`; Route-B-specific downstream controls | explicit current physical Route-B source corridor and 14-root source family | **CLOSED on external-dependency path**; internal reconstruction OPEN | **SPECIFIED LOCALLY** |
| `B_cp1_RouteA` | **UNSPECIFIED** — exact `P_A(x,O_x)` not recovered | roadmap label only; naive `U_t>=0` interpretation rejected | **UNSPECIFIED** | OPEN | **NOT YET A CERTIFIED SOURCE BRANCH** |
| `B_cp_ge2` | checkpoint condition exists only as low-surplus control data; exact source predicate pending | `s_cp>=2`, with local control relation `r=s_cp-1` where certificate prerequisites hold | **OPEN — requires checkpoint-to-source realization transport** | OPEN | **CHECKPOINT SECTOR, NOT YET EXACT SOURCE BRANCH** |
| `B_other` | **UNSPECIFIED** until coverage analysis proves whether additional branches are required | unknown | unknown | OPEN | **PLACEHOLDER ONLY** |

### Scope of the first row

`B_cp1_RouteB_current` denotes only the already source-preservingly constructed current physical Route-B sector. It does not mean that every source satisfying some abstract checkpoint condition `s_cp=1` is already known to enter this row.

Its external closure is therefore local to the source corridor actually proved in the Route-B stack.

## 4. Current Route-B external closure

For the current specified Route-B physical sector, the internally certified source corridor lies below the accepted external recursive-sufficiency coverage bound

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

Hence, if the audited Bařina/Ansari finite-range results are accepted as lemmas,

\[
B_{cp1,RouteB,current}\cap CE=\varnothing.
\]

This is a branch-sector closure only.

It does not imply

\[
CE=\varnothing.
\]

## 5. Checkpoint-to-source transport requirement for `s_cp>=2`

Let \(\Sigma_s\) be a checkpoint-state space, \(A_s(\sigma)\) its admissibility predicate, and \(R(x,\sigma)\) the same-source/same-orbit realization relation.

Before `s_cp>=2` can be split into exact source branches, prove source charts

\[
\Phi_{s,\lambda}:I_{s,\lambda}\to\mathbb N
\]

such that

\[
A_s(\sigma)\land R(x,\sigma)
\Longrightarrow
\exists\lambda,m:\ x=\Phi_{s,\lambda}(m),\quad m\in I_{s,\lambda}.
\]

If the charts are claimed exact, also prove reflection:

\[
x=\Phi_{s,\lambda}(m),\ m\in I_{s,\lambda}
\Longrightarrow
\exists\sigma:\ A_s(\sigma)\land R(x,\sigma).
\]

Until this theorem is closed, `B_cp_ge2` is deliberately not expanded into apparently precise but unproved source branches.

Canonical obligation:

`CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`

Audit:

`../audits/DSD_CHECKPOINT_SOURCE_TRANSPORT_AUDIT.md`

## 6. Route-A requirement

Route-A must obtain an exact predicate

\[
P_A(x,\mathcal O_x)
\]

with explicit:

1. entrance event/checkpoint;
2. prerequisites and control quantities;
3. source chart/domain;
4. downstream obligations;
5. closure criterion.

The historical phrase `independent lower-bound obligation` is descriptive only and is not sufficient.

The rejected shortcut

\[
U_t\ge0\quad\Longrightarrow\quad\text{Route-A}
\]

must not be reinstated without a new theorem proving the equivalence from the source/orbit definitions.

## 7. Global cover obligation

The eventual source-level branch family must satisfy

\[
CE\subseteq
B_{cp1,RouteB,current}
\cup B_{cp1,RouteA}
\cup \bigcup_{s\ge2}B_{cp=s}
\cup B_{other},
\]

**only after every symbol on the right has been replaced by an exact predicate/domain and the inclusion itself is proved.**

The display above is an obligation schema, not a theorem.

If `B_other` can be proved empty or unnecessary, remove it only by a cover theorem. If additional branches are discovered, add them before declaring completeness.

## 8. Overlap accounting

A cover is sufficient for global closure; a partition is optional.

If the branch family overlaps, record explicitly which sources can appear in more than one branch and ensure that no cardinality, density, or survival calculation treats the overlap as independent/disjoint.

If a partition is claimed, prove

\[
B_\alpha\cap B_\beta=\varnothing
\qquad(\alpha\ne\beta).
\]

## 9. DSD source-preservation rule

The permitted ordering is

\[
\boxed{
L0\ \text{ordinary source/orbit}
\to
L1\ \text{applicability/realization}
\to
L2\ \text{branch/checkpoint representation}
\to
L3\ \text{derived completion}.
}
\]

A genuine source branch must be traceable back to L0.

A difference in `s_cp`, route label, H/L descriptor, terminal defect, projective residue, endpoint lattice, or other L2/L3 state is not enough unless the corresponding source predicate and same-orbit transport are proved.

## 10. Closure criteria

For every final source branch \(B_\alpha\), require

\[
B_\alpha\cap CE=\varnothing.
\]

A branch may be closed internally or by an explicitly declared external finite-range lemma.

External finite-range inheritance is permitted only after proving the exact ordinary-source inclusion into the verified interval.

## 11. Current global verdict

- current physical `s_cp=1,Route-B` sector: **CLOSED on external-dependency path**;
- optional internal reconstruction of the same Route-B sector: **OPEN**;
- `s_cp>=2` checkpoint-to-source transport: **OPEN**;
- Route-A source predicate: **OPEN / UNSPECIFIED**;
- need for any additional branches: **OPEN until cover theorem**;
- global branch cover: **OPEN**;
- global Collatz conclusion: **OPEN**.

## 12. Canonical dependencies

- `../PROOF_MAP.md`;
- `../audits/C0_C6_BRANCH_SPECIFICATION_COMPLETENESS_GAP_AUDIT.md`;
- `CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`;
- `../audits/DSD_CHECKPOINT_SOURCE_TRANSPORT_AUDIT.md`;
- `../frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`;
- `EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`.
