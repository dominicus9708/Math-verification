# Checkpoint-Surplus Source-Realization Transport Obligation

**Status:** PARTIALLY CLOSED — the finite checkpoint-predicate -> source-cylinder transport mechanism is now exact; global surplus specification/coverage remains OPEN.

## 1. Scope and provenance

The low-surplus checkpoint certificates provide a checkpoint-control parameterization.  They do not by themselves define every global ordinary-source branch.

Canonical audit notation is

\[
s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus},
\]

although historical code often uses bare `s`.

The directly recorded `s=1` checkpoint condition is

\[
\boxed{\tau_{j_0}\le t_0<\tau_{j_0+1}.}
\]

The directly inspected surplus-tax certificate records

\[
\boxed{r=s_{\mathrm{cp}}-1},
\]

where `r` is the number of extra odd ordinals crossed to the left of `T0`, and for `r>=1` uses the exact symbolic tax lower bound

\[
\boxed{\operatorname{tax}(r)>\frac r6-\frac1{12}}
\]

in its companion structural lemma interface.

The certificate-local constants include

\[
A0=114{,}208{,}327{,}604,
\qquad
Q0=72{,}057{,}431{,}991.
\]

They are not promoted here to global constants by notation alone.

A global identity of the form

\[
s_{\mathrm{cp}}=A_0-j_\star
\]

is **not established by this document** and must not be used without an ordinary-orbit/checkpoint provenance derivation.

## 2. What is now structurally closed

`FINITE_CHECKPOINT_PREDICATE_SOURCE_CYLINDER_TRANSPORT.md` proves the following exact theorem.

Let

\[
X(m)=x+A m,
\qquad A\text{ odd},
\qquad m\in I\cap\mathbb Z
\]

be an exact finite parent source family, and let `P` be any exact predicate determined by a finite raw/checkpoint prefix.

Then the sources satisfying `P` are exactly a source-disjoint union of dyadic affine cylinders

\[
\boxed{
\mathcal D_P
=
\bigsqcup_{w\in\mathcal W_P}\Phi_w(I_w),
}
\]

and

\[
\boxed{
X\in\mathcal D_P
\iff
X\text{ belongs to the parent family and realizes }P.
}
\]

This provides both forward transport and reflection.  Same-source provenance is carried by the exact valuation-cylinder recursion; it is not inferred from CRT compatibility or equal compressed labels.

Therefore the **generic finite transport mechanism is CLOSED**.

## 3. Remaining surplus-specific state space

For a fixed checkpoint surplus `s`, let

\[
\Sigma_s
\]

denote the checkpoint states admitted by the exact surplus predicate, once that predicate is defined.

Let

\[
A_s(\sigma)
\]
mean that `sigma` satisfies all active checkpoint prerequisites and the exact surplus-sector condition.

Let

\[
R(x,\sigma)
\]
be same-source/same-orbit realization.

For an exact finite parent family `F`, the new theorem supplies an exact chart union

\[
\mathcal D_s(F)
=
\{x\in F:\exists\sigma\in\Sigma_s,\ A_s(\sigma)\land R(x,\sigma)\}
\]

**provided the exact finite predicate defining `Sigma_s` is available**.

## 4. Remaining OPEN obligation A — exact general surplus predicate

For `s_cp=1`, the checkpoint condition

\[
\tau_{j_0}\le t_0<\tau_{j_0+1}
\]

is directly recorded.

For `s_cp>=2`, the repository still needs one canonical orbit-prefix definition specifying exactly which finite checkpoint data distinguish the sectors.

The facts

\[
r=s_{\mathrm{cp}}-1
\]

and the downstream surplus-tax/budget/envelope consequences do not substitute for that source-level predicate.

Required output:

\[
\boxed{
A_s(\sigma)
\iff
\text{explicit finite condition on ordinary checkpoint/orbit-prefix data}.
}
\]

## 5. Remaining OPEN obligation B — upstream parent source cover

The finite transport theorem is relative to a supplied exact parent source family.

Global use therefore requires a theorem identifying the exact parent families `F_lambda` to which the surplus split applies and proving that they cover the relevant counterexample candidates:

\[
\boxed{
CE_{\mathrm{surplus\ scope}}
\subseteq
\bigcup_\lambda F_\lambda.
}
\]

The current Route-B physical corridor is downstream and branch-specific; it is not automatically the parent family for `s_cp>=2`.

## 6. Remaining OPEN obligation C — instantiated source charts

Once A and B are supplied, instantiate the finite transport theorem:

\[
\boxed{
\mathcal D_s
=
\bigcup_\lambda\mathcal D_s(F_\lambda).
}
\]

Inside each parent family, the constituent exact prefix cylinders are source-disjoint.

Across different parent families, overlap or disjointness must be accounted for explicitly.

The exact theorem does not guarantee that the raw cylinder enumeration is computationally small.  A compact representation is a separate algorithmic/proof obligation.

## 7. Compression admissibility

For any compression

\[
Q:\mathcal S\to\mathcal Q,
\]

every later source-sensitive predicate `P_i` must factor through `Q` whenever exact branch decisions depend on it:

\[
P_i(S)\iff\widehat P_i(Q(S)).
\]

At minimum,

\[
Q(S_1)=Q(S_2)
\Longrightarrow
P_i(S_1)=P_i(S_2).
\]

No source coordinate may be dropped merely because a surplus tax, defect, terminal aggregate, or projective observation agrees.

## 8. External finite-range closure interface

A new surplus sector can inherit the existing external recursive-sufficiency closure only after its ordinary-source domain has been proved and bounded.

A sufficient interface is

\[
\boxed{\mathcal D_s\subseteq[1,L_{RS}]}
\]

with

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

The finite transport theorem gives exact source provenance, but it does **not** by itself provide this numerical upper bound.

## 9. Relation to the late activation/checkpoint join

`SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md` proves a later local same-orbit splice once an exact activation cylinder, terminal descriptor, and checkpoint `Z` are supplied.

The interfaces are:

\[
\text{finite checkpoint predicate}
\longleftrightarrow
\text{exact source cylinders}
\]

followed, where needed downstream, by

\[
\text{activation source cylinder}+\text{terminal descriptor}+Z
\longleftrightarrow
\text{same ordinary orbit}.
\]

They are successive provenance steps and must not be counted as independent probabilistic filters.

## 10. DSD audit layers

### L0 — ordinary source/orbit

Exact affine source cylinder and parameter interval.

### L1 — event realization / predicate activation

Exact valuation/parity prefix and prerequisite status.

### L2 — checkpoint-control representation

` s_cp`, `r=s_cp-1`, and any independently defined checkpoint controls.

### L3 — derived completion

Tax, Hensel budgets, terminal defects, projective observations, endpoint data, and other derived quantities.

The new finite transport theorem proves forward preservation and reflection between L0 and an exactly defined finite L1/L2 checkpoint predicate.  It does not promote L3 differences to source branches.

## 11. Global completeness remains separate

Even if every surplus sector is instantiated and individually closed, global Collatz still requires exact branch specifications and a cover theorem

\[
CE\subseteq\bigcup_{\alpha\in A}B_\alpha.
\]

Route-A still needs an exact source predicate.

## 12. Current verdict

- local checkpoint-surplus notion: **ESTABLISHED LOCALLY**;
- exact `s_cp=1` checkpoint predicate: **ESTABLISHED LOCALLY**;
- `r=s_cp-1` in the inspected surplus-tax interface: **ESTABLISHED LOCALLY**;
- symbolic surplus-tax lower bound `r/6-1/12` for `r>=1`: **ESTABLISHED IN THE COMPANION STRUCTURAL/CERTIFICATE INTERFACE**;
- generic finite checkpoint predicate -> exact source-cylinder transport: **CLOSED**;
- reflection/source provenance for those finite cylinders: **CLOSED**;
- exact canonical `s_cp>=2` orbit-prefix predicate: **OPEN**;
- upstream parent source-family cover for the surplus split: **OPEN**;
- compact instantiated `s_cp>=2` source charts: **OPEN**;
- source upper bounds for external closure: **OPEN**;
- global identity `s_cp=A0-j_*`: **UNVERIFIED / NOT REQUIRED BY THE FINITE TRANSPORT THEOREM**;
- Route-A exact predicate: **OPEN / UNSPECIFIED**;
- global branch cover: **OPEN**;
- global Collatz conclusion: **OPEN**.

## Canonical references

- `FINITE_CHECKPOINT_PREDICATE_SOURCE_CYLINDER_TRANSPORT.md`
- `AFFINE_VALUATION_CYLINDER_JUMP.md`
- `SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`
- `../audits/DSD_FINITE_CHECKPOINT_SOURCE_CYLINDER_TRANSPORT_AUDIT.md`
