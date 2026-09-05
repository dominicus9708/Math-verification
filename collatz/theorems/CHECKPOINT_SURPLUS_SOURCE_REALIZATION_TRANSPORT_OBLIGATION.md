# Checkpoint-Surplus Source-Realization Transport Obligation

**Status:** OPEN — theorem obligation, not a proved theorem.

## 1. Scope and provenance

The low-surplus checkpoint certificates currently provide a **checkpoint-control parameterization**. They do not by themselves provide an ordinary-source branch decomposition.

To prevent notation drift, this document writes

\[
s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus},
\]

although older certificate code uses the bare variable `s`.

The directly recorded `s=1` checkpoint condition in the Xi/Minkowski note is

\[
\tau_{j_0}\le t_0<\tau_{j_0+1}.
\]

For the directly inspected low-surplus certificate family, the supported control displacement is

\[
\boxed{r=s_{\mathrm{cp}}-1},
\]

where `r` is interpreted there as the number of extra odd ordinals crossed to the left of \(T_0\).

A previously recorded relation

\[
q_\star=Q0-r
\]

was **not found in the directly inspected current canonical certificate files** and is therefore excluded from this theorem interface. It must not be used unless its exact provenance is independently recovered and audited.

The sampled low-surplus certificate files also use the file-local constants

\[
A0=114{,}208{,}327{,}604,
\qquad
Q0=72{,}057{,}431{,}991.
\]

These constants are recorded here only as **file-local certificate parameters**. This document does not promote them to global canonical constants without a separate provenance theorem.

Likewise, any identification of the checkpoint surplus with a formula of the form

\[
s_{\mathrm{cp}}=A_0-j_\star
\]

is **not established here**. If such an identity is needed globally, it is a separate provenance/transport obligation and must be proved from the ordinary-orbit definitions.

## 2. State spaces and realization relation

For a fixed checkpoint surplus \(s\), let

\[
\Sigma_s
\]

denote the admissible checkpoint-state space produced by the upstream checkpoint construction.

Let

\[
A_s(\sigma)
\]
mean that the checkpoint state \(\sigma\in\Sigma_s\) satisfies every prerequisite and checkpoint-local admissibility condition that is actually active at that stage.

Let

\[
R(x,\sigma)
\]
be the **same-source / same-orbit realization relation**: the ordinary positive integer source \(x\) genuinely generates the orbit data from which the checkpoint state \(\sigma\) was obtained.

The relation \(R\) is essential. CRT compatibility, equal compressed coordinates, equal checkpoint labels, or equal derived terminal data are not substitutes for same-orbit realization.

## 3. Desired ordinary-source charts

For each surplus sector \(s\), the goal is to construct a finite or otherwise explicitly controlled chart family

\[
\Phi_{s,\lambda}:I_{s,\lambda}\longrightarrow \mathbb N,
\]

where \(\lambda\) records the source-preserving branch/chart label and \(I_{s,\lambda}\) is an exact integer parameter interval or admissible set.

Define the corresponding ordinary-source domain

\[
\mathcal D_s
=
\bigcup_{\lambda}
\Phi_{s,\lambda}(I_{s,\lambda}).
\]

## 4. Forward transport obligation

The principal OPEN theorem is

\[
\boxed{
A_s(\sigma)\land R(x,\sigma)
\Longrightarrow
\exists\lambda\,\exists m\in I_{s,\lambda}:
\ x=\Phi_{s,\lambda}(m)
}
\]

for every live checkpoint-surplus sector under consideration.

This is the step that turns a checkpoint-control statement into an ordinary-source statement.

Without this implication, a surviving checkpoint state cannot be counted as an ordinary-source branch and cannot inherit a source bound merely because its control coordinates resemble a previously closed Route-B state.

## 5. Reflection / exactness obligation

If the charts are used to define or exhaust a branch, the reverse direction is also required:

\[
\boxed{
x=\Phi_{s,\lambda}(m),\ m\in I_{s,\lambda}
\Longrightarrow
\exists\sigma\in\Sigma_s:
A_s(\sigma)\land R(x,\sigma)
}
\]

subject to the exact branch prerequisites.

Forward transport alone can over-approximate a source family. Reflection is what permits the chart family to be treated as an exact branch specification rather than a one-way enclosure.

## 6. DSD audit layers

The transport is audited in the following order.

### L0 — ordinary source / orbit

The integer source and its exact Collatz orbit provenance.

### L1 — status / activation / realization

Whether a checkpoint predicate is applicable, prerequisite-satisfied, defined, and actually realized by the same source/orbit.

### L2 — checkpoint-control representation

Directly supported examples include

\[
s_{\mathrm{cp}},\quad r=s_{\mathrm{cp}}-1,
\]

and the independently defined Hensel-budget or packed-suffix control coordinates in their own certificate domains.

Unsupported or unrecovered coordinate relations are excluded from this layer until provenance is supplied.

### L3 — derived completion

Terminal defects, projective observations, endpoint-lattice coordinates, and other quantities derived after the source/control state has already been fixed.

A difference that first appears only in L2 or L3 does not, by itself, prove that two ordinary sources belong to distinct L0 branches.

## 7. Compression admissibility

For any compression or quotient

\[
Q:\mathcal S\to\mathcal Q,
\]

every later source-sensitive predicate \(P_i\) must be shown to factor through \(Q\):

\[
P_i(S)\iff \widehat P_i(Q(S))
\]

whenever exact branch decisions depend on \(P_i\).

At minimum, the proof must establish the required invariance

\[
Q(S_1)=Q(S_2)
\Longrightarrow
P_i(S_1)=P_i(S_2).
\]

No source coordinate may be dropped merely because a terminal aggregate or control signature agrees.

## 8. External finite-range closure interface

The existing external recursive-sufficiency closure can be inherited by a new surplus sector only **after** an ordinary-source domain theorem has been proved.

A sufficient interface would be an exact inclusion such as

\[
\mathcal D_s\subseteq [1,L_{RS}],
\]

or a proved integer upper bound below

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

Only then, and only on the external-dependency path that accepts the cited finite verification lemmas, may that sector be declared externally closed.

The current Route-B source bound is downstream and branch-specific. It must **not** be transferred to \(s_{\mathrm{cp}}\ge2\), Route-A, or any other sector without this transport theorem.

## 9. Global completeness remains separate

Even if every transported surplus sector is individually closed, the global proof still requires exact branch specifications and a cover theorem

\[
CE\subseteq\bigcup_{\alpha\in A}B_\alpha.
\]

Route-A still needs an exact entrance/source predicate. Named branches or control labels do not establish exhaustiveness.

## 10. Current verdict

- checkpoint-surplus provenance as a checkpoint-control notion: **ESTABLISHED LOCALLY**;
- exact `s=1` checkpoint condition: **ESTABLISHED LOCALLY**;
- \(r=s_{\mathrm{cp}}-1\) in the low-surplus certificate family: **ESTABLISHED LOCALLY**;
- \(q_\star=Q0-r\): **NOT RECOVERED / EXCLUDED FROM CURRENT CANONICAL INTERFACE**;
- identification \(s_{\mathrm{cp}}=A_0-j_\star\): **UNVERIFIED / SEPARATE OBLIGATION**;
- all-\(s_{\mathrm{cp}}\ge2\) same-source realization transport: **OPEN**;
- exact ordinary-source charts \(\mathcal D_s\): **OPEN**;
- transfer of external finite-range closure to new surplus sectors: **BLOCKED UNTIL SOURCE TRANSPORT**;
- Route-A exact predicate: **OPEN / UNSPECIFIED**;
- global branch cover: **OPEN**;
- global Collatz conclusion: **OPEN**.
