# Canonical live proof stack

This file records the **shortest current live implication chain**. Detailed internal Route-B reconstruction data remain in the frontier/status/theorem files and are not discarded, but the current physical Route-B sector is already closed on the accepted external-dependency path.

Global Collatz closure remains OPEN.

## S0 — Ordinary counterexample-source domain

Let

\[
CE:=\{x\in\mathbb N_{>0}:x\text{ is a hypothetical positive Collatz counterexample start}\}.
\]

Every later branch object used for a global conclusion must be connected back to an ordinary source \(x\) and its deterministic orbit \(\mathcal O_x\).

Status: **DOMAIN / GLOBAL SOURCE LAYER**.

## S1 — Canonical branch specification scaffold

For every source branch \(B_\alpha\), require

\[
\boxed{x\in B_\alpha\iff P_\alpha(x,\mathcal O_x)}.
\]

Canonical scaffold:

- `theorems/GLOBAL_BRANCH_SPECIFICATION.md`.

Current rows distinguish:

1. current source-preservingly specified `s_cp=1,Route-B` physical sector;
2. `s_cp=1,Route-A`, exact source predicate still UNSPECIFIED;
3. `s_cp>=2`, checkpoint sector with source transport OPEN;
4. any additional branch required by the eventual cover theorem.

Status: **OPEN / PARTIALLY SPECIFIED**.

## S2 — Checkpoint-surplus provenance layer

Canonical audit notation is

\[
\boxed{s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus}.}
\]

The directly inspected local `s=1` checkpoint condition is

\[
\boxed{\tau_{j_0}\le t_0<\tau_{j_0+1}.}
\]

The low-surplus certificate family uses

\[
\boxed{r=s_{\mathrm{cp}}-1,}
\]

with `r` interpreted there as extra odd ordinals crossed to the left of `T0`.

The sampled low-surplus files use file-local

\[
A0=114{,}208{,}327{,}604,
\qquad
Q0=72{,}057{,}431{,}991.
\]

These constants are not promoted to global canonical values here.

The identity

\[
s_{\mathrm{cp}}=A_0-j_\star
\]

is **NOT ESTABLISHED** by the currently inspected canonical source chain. It is a separate provenance theorem obligation if later needed.

Status: **LOCAL CHECKPOINT PROVENANCE PARTLY CLOSED / GLOBAL IDENTITY OPEN**.

## S3 — Current `s_cp=1,Route-B` source sector

The existing Route-B stack has an exact source-preserving family representation

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with finite parameter intervals, a retained 14-root source forest, and an explicit physical source corridor.

The persistent Route-B coordinate

\[
S=q-Q(h)
\]

is **not** the checkpoint surplus `s_cp`.

The internal Route-B stack also contains exact source/checkpoint provenance joins and derived-observation minimization theorems.

Status: **SPECIFIED SOURCE SECTOR**.

## S4 — Current Route-B external finite-range closure

The current Route-B physical source corridor lies below

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

On the proof path that accepts the audited Bařina/Ansari finite-range results as external lemmas,

\[
\boxed{B_{cp1,RouteB,current}\cap CE=\varnothing.}
\]

Canonical dependencies:

- `theorems/EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`;
- `src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`;
- `audits/S10_EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CLOSURE_AUDIT.md`;
- `frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`.

Status: **CLOSED — EXTERNAL-DEPENDENCY PATH, CURRENT PHYSICAL ROUTE-B SECTOR ONLY**.

This is not an A0/global closure theorem.

## S5 — Checkpoint-to-source realization transport for `s_cp>=2`

Checkpoint control must be transported back to ordinary sources before `s_cp>=2` can be treated as an exact source branch family.

Let \(\Sigma_s\) be the checkpoint-state space, \(A_s(\sigma)\) checkpoint admissibility, and \(R(x,\sigma)\) same-source/same-orbit realization.

Required forward transport:

\[
\boxed{
A_s(\sigma)\land R(x,\sigma)
\Longrightarrow
\exists\lambda,m:\ x=\Phi_{s,\lambda}(m),\quad m\in I_{s,\lambda}.
}
\]

If the charts are used as exact branch definitions, reflection is also required.

Canonical obligation:

- `theorems/CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`;
- `audits/DSD_CHECKPOINT_SOURCE_TRANSPORT_AUDIT.md`.

Status: **OPEN — PRINCIPAL GLOBAL GATE**.

## S6 — Route-A exact source predicate

Route-A currently remains a roadmap/control label.

Required theorem:

\[
\boxed{x\in B_A\iff P_A(x,\mathcal O_x)}
\]

with exact entrance event, prerequisites, source domain/chart, continuation obligations, and closure criterion.

The rejected naive rule based only on a sign such as `U_t>=0` is not reinstated.

Status: **OPEN / UNSPECIFIED — PRINCIPAL GLOBAL GATE**.

## S7 — Branch-specific source closure

Once S5 or S6 supplies an exact source domain \(\mathcal D_\alpha\), close that branch either internally or through a declared external dependency.

The external finite-range path may be inherited only after proving an inclusion such as

\[
\mathcal D_\alpha\subseteq[1,L_{RS}].
\]

The current Route-B source bound is branch-specific and cannot be transferred without such a theorem.

Status: **OPEN FOR REMAINING BRANCHES**.

## S8 — Global branch cover / overlap theorem

After every live branch has an exact source predicate, prove

\[
\boxed{CE\subseteq\bigcup_{\alpha\in A}B_\alpha.}
\]

If a partition is claimed, prove pairwise disjointness. If overlap is allowed, specify overlap accounting and do not combine marginal counts as though the branches were independent.

Status: **OPEN — FINAL C0/C6 COMPLETENESS GATE**.

## S9 — Global Collatz conclusion

Only after S8 and branchwise closure

\[
B_\alpha\cap CE=\varnothing
\qquad\text{for every covered branch}
\]

may one infer

\[
CE=\varnothing.
\]

Status: **OPEN**.

---

# Optional internal Route-B reconstruction stack

The previous detailed S0–S16 Route-B chain is preserved in the repository's frontier, theorem, audit, source, and status history. Its live unresolved endpoint is the source-preserving event/valuation exporter to the `q_rem=28` activation seam plus low-precision carry/source provenance.

Important retained facts include:

- first-defect roots `{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`;
- exact source families `X=r+2^h m`, `T^h(X)=y+3^q m`;
- persistent state `(r,y,m_lo,m_hi,h,S)`;
- `14,224` source cylinders;
- source-parameter multiplicity `26,859,837,368,455,538,464`;
- `H0=40,H1=44,H2=45,H3=48,H4=50`, `H5<=50`;
- `D51>=6`, `eta_future>1/2`;
- exact source/checkpoint same-orbit join once a paired activation record is supplied;
- `z_2`, `z_H`, `F28`, and related terminal quantities are derived/associated observations, not independent filters.

Status: **OPEN OPTIONAL SELF-CONTAINED PATH / NOT PRINCIPAL GLOBAL PATH**.

---

# Current shortest implication chain

\[
\boxed{
CE
\to
\text{exact source branch specification}
\to
\begin{cases}
\text{current Route-B sector: externally closed},\\
\text{Route-A: source predicate OPEN},\\
\text{s}_{cp}\ge2:\ \text{checkpoint→source transport OPEN}
\end{cases}
\to
\text{branchwise closure}
\to
\text{global cover}
\to
CE=\varnothing.
}
\]

The final two implications are not yet established.

# Immediate next work

1. Prove or recover the ordinary-orbit provenance of checkpoint surplus only as far as required; do not assume `s_cp=A0-j_*`.
2. Starting upstream of Route-B-specific SAFE cuts, identify the first checkpoint stage where `s_cp>=2` changes a source-compatible state.
3. Construct the same-source realization relation and exact source charts for that stage.
4. Independently recover/prove the exact Route-A predicate.
5. Compare newly proved source domains with `L_RS` only after their bounds are source-level theorems.
6. Build the global cover theorem from exact predicates, not roadmap labels.

# Forbidden shortcuts

- checkpoint-control difference -> source-branch difference;
- historical `s=A0-j_*` notation -> canonical identity without provenance proof;
- file-local constants -> universal constants;
- Route-B source bound -> Route-A/`s_cp>=2` source bound;
- branch label -> branch predicate;
- finite branch names -> exhaustive cover;
- equal compressed/derived state -> equal source payload;
- exact-pair uniqueness -> family uniqueness;
- CRT compatibility -> same orbit;
- multiplying marginal survival fractions without independence;
- extrapolating finite `H_c` data;
- `H5<=50 -> H5=50`;
- derived `F28` and `z_H` as independent filters;
- local Route-B closure -> global Collatz.
