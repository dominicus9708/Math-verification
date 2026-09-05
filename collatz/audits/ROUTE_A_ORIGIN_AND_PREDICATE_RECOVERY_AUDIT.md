# Route-A Origin and Predicate-Recovery Audit

Date: **2026-09-05**

**Status:** ORIGIN LOCATED AS ROADMAP OBLIGATION / EXACT SOURCE PREDICATE NOT RECOVERED

## 1. Question

Was Route-A originally introduced as an exact mathematical branch and later lost, or was it introduced only as a roadmap obligation requiring later formalization?

This matters because the global branch-completeness theorem cannot treat a historical label as though its source predicate were already proved.

## 2. Earliest canonical proof-map occurrence

The initial `collatz/PROOF_MAP.md` creation commit is

`9487fdd2f03c46f0e06b5b6c2997b907bdfda056`

with commit message

`collatz: add proof module map`.

In that initial proof map, C6 was introduced as

`Route-A, s>=2, and remaining global branches`

and its minimum listed obligations included

`Route-A independent lower-bound obligation`.

The same initial C6 section did **not** state an exact ordinary-source entrance predicate

\[
P_A(x,\mathcal O_x),
\]

a source chart/domain, a checkpoint equivalence, or a proved exhaustiveness relation involving Route-A.

## 3. Classification of the original label

The phrase

`independent lower-bound obligation`

specifies a proof-program role, not a mathematical branch predicate.

Therefore the earliest canonical occurrence supports the classification

\[
\boxed{
\text{Route-A at introduction}=
\text{roadmap / proof-obligation label},
}
\]

not

\[
\boxed{
\text{Route-A at introduction}=
\text{already defined source branch}.
}
\]

This does not prove that no older research note anywhere contained a precursor idea. It does establish that the canonical proof-map interface did not import an exact branch definition when Route-A first appeared there.

## 4. Rejected reconstruction by naming alone

The following reconstruction is invalid:

\[
\text{historical name Route-A}
\Longrightarrow
\text{there must exist a unique implicit predicate }P_A.
\]

A label can summarize an intended lower-bound task without specifying which ordinary sources satisfy it.

Similarly, the previously considered shortcut based on a sign condition such as

\[
U_t\ge0
\]

is not accepted as the Route-A definition unless a new theorem proves exact equivalence to the intended ordinary-source branch.

## 5. Exact recovery target

Route-A becomes a certified source branch only after constructing a predicate

\[
\boxed{x\in B_A\iff P_A(x,\mathcal O_x)}
\]

with all of the following data.

### A1 — entrance event

An exact orbit/checkpoint event determining when Route-A becomes applicable.

### A2 — prerequisites and status

A proof that the predicate is applicable/defined for every source that is claimed to enter the branch.

### A3 — same-source provenance

Any checkpoint/control representation used by Route-A must be tied to the same ordinary source/orbit.

### A4 — source chart/domain

An exact source representation, for example

\[
\Phi_{A,\lambda}:I_{A,\lambda}\to\mathbb N,
\]

with its exact domain and source-sensitive coordinates.

### A5 — continuation obligations

The exact inequalities, language constraints, checkpoint conditions, or other predicates that remain to be proved after entrance.

### A6 — exit/closure criterion

A theorem establishing

\[
B_A\cap CE=\varnothing
\]

by an internal argument or by an explicitly declared external finite-range dependency after a source-domain inclusion theorem.

## 6. Relation to checkpoint surplus

No exact relation of the form

\[
B_A=\{x:s_{\mathrm{cp}}(x)=\cdots\}
\]

is currently established.

Route-A and the `s_cp>=2` checkpoint-surplus transport problem must therefore be kept as distinct open specifications until a theorem proves a relation between them.

In particular, it is invalid to infer that Route-A is simply the complement of the current Route-B sector inside `s_cp=1`, unless the corresponding source-level dichotomy is proved.

## 7. Global-cover consequence

The eventual global proof requires

\[
CE\subseteq\bigcup_\alpha B_\alpha.
\]

The historical appearance of the names `Route-A`, `Route-B`, and `s>=2` does not establish that this union is exhaustive.

Before Route-A contributes to a global cover theorem, both its exact predicate and its overlap/disjointness relation with all other live source branches must be proved.

## 8. DSD audit interpretation

Route-A's earliest canonical occurrence is a **label at the proof-management/representation layer**, not yet an L0 source partition.

The safe order is

\[
L0\ \text{ordinary source/orbit}
\to
L1\ \text{entrance/applicability/provenance}
\to
L2\ \text{Route-A control representation}
\to
L3\ \text{derived closure data}.
\]

One may not reverse this order by taking the L2 name `Route-A` and retroactively declaring an L0 source predicate.

## 9. Audit verdict

| Question | Verdict |
|---|---|
| earliest canonical proof-map Route-A occurrence located | YES |
| introduced there with an exact `P_A(x,O_x)` | NO |
| introduced there with a source chart/domain | NO |
| introduced there as an independent lower-bound obligation | YES |
| exact source predicate recovered elsewhere in current canonical stack | NO |
| naive sign-condition reconstruction accepted | NO |
| Route-A usable in global cover today | NO — specification remains OPEN |

Hence

\[
\boxed{
\text{Route-A origin}=\text{roadmap obligation},
\qquad
\text{exact source predicate}=\mathrm{OPEN}.
}
\]

## 10. Next search/construction rule

Historical searches may still be used to find a mathematically stronger precursor, but any candidate must be checked against the six recovery requirements A1–A6.

If no such precursor exists, Route-A should be **defined anew from the ordinary-orbit interface**, rather than reconstructed from an ambiguous label.

## Canonical dependencies

- initial proof-map commit `9487fdd2f03c46f0e06b5b6c2997b907bdfda056`;
- `../PROOF_MAP.md`;
- `C0_C6_BRANCH_SPECIFICATION_COMPLETENESS_GAP_AUDIT.md`;
- `../theorems/GLOBAL_BRANCH_SPECIFICATION.md`;
- `SURPLUS_FIRST_DIVERGENCE_STAGE_AUDIT.md`;
- `../status/OPEN_GATES.md`.
