# Current status — 2026-09-05

## Current branch

Research branch: `collatz-stage4-window-threshold`.

## One-line global status

\[
\boxed{\text{current physical }s_{cp}=1\text{ Route-B sector externally CLOSED; C0/C6 global specification remains OPEN}.}
\]

The optional self-contained Route-B reconstruction remains open, but it is no longer the shortest global path.

## Canonical global objects

- `../PROOF_MAP.md`;
- `../theorems/GLOBAL_BRANCH_SPECIFICATION.md`;
- `../theorems/CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`;
- `../audits/C0_C6_BRANCH_SPECIFICATION_COMPLETENESS_GAP_AUDIT.md`;
- `../audits/DSD_CHECKPOINT_SOURCE_TRANSPORT_AUDIT.md`;
- `OPEN_GATES.md`.

## Surplus notation/provenance correction

Canonical audit notation is now

\[
\boxed{s_{\mathrm{cp}}:=\text{tenth-checkpoint surplus}.}
\]

The directly inspected Xi/checkpoint note records the local `s=1` condition

\[
\boxed{\tau_{j_0}\le t_0<\tau_{j_0+1}.}
\]

The low-surplus certificate family uses

\[
\boxed{r=s_{\mathrm{cp}}-1,}
\]

with `r` interpreted there as the number of extra odd ordinals crossed to the left of `T0`.

The sampled low-surplus certificate files use the file-local constants

\[
A0=114{,}208{,}327{,}604,
\qquad
Q0=72{,}057{,}431{,}991.
\]

These are **not promoted to global canonical constants** by this status file.

The previously asserted canonical identity

\[
s_{\mathrm{cp}}=A_0-j_\star
\]

is currently **NOT ESTABLISHED**. If required, it must be proved as a separate ordinary-orbit/checkpoint provenance theorem.

The lower-case `s_cp` is also distinct from the upper-case persistent Route-B coordinate `S` in expressions such as

\[
q=Q(h)+S.
\]

## Current Route-B physical sector — external-dependency path

**Status: CLOSED for counterexample-source rejection.**

The current Route-B source corridor is below the accepted external recursive-sufficiency coverage limit

\[
L_{RS}=4\cdot3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

Thus, conditional on the audited external Bařina/Ansari finite-range results being accepted as lemmas, the currently source-preservingly constructed physical Route-B sector contains no Collatz counterexample source.

Canonical closure files:

- `../theorems/EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`;
- `../src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`;
- `../audits/S10_EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CLOSURE_AUDIT.md`;
- `../frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`.

This does **not** close Route-A, `s_cp>=2`, C0, or global Collatz.

## Exact retained Route-B internal family

The optional internal/self-contained path still retains the first-defect roots

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Each live source family has the exact affine form

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with a finite integer parameter interval.

The persistent source/control state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)},
\qquad S=q-Q(h).
\]

The canonical jump-8 source-cylinder count is `14,224`, with source-parameter multiplicity

\[
26{,}859{,}837{,}368{,}455{,}538{,}464.
\]

That multiplicity is not automatically a count of distinct ordinary source integers.

## Exact bounded-displacement status on internal Route-B path

\[
\boxed{H_0=40,\ H_1=44,\ H_2=45,\ H_3=48,\ H_4=50.}
\]

For budget five only

\[
\boxed{H_5\le50}
\]

is proved. Therefore

\[
\boxed{D_{51}\ge6},
\qquad
\boxed{\eta_{future}>\frac12}.
\]

Do not strengthen `H_5<=50` to `H_5=50` without a horizon-50 witness.

## Closed local same-orbit kernels on internal Route-B path

The source/checkpoint provenance join is closed once a paired activation record and ordinary checkpoint candidate are supplied.

At the activation seam,

\[
X=r+2^h k,
\qquad
T^h(X)=y+3^qk,
\qquad q=j_0-28.
\]

For a validated terminal suffix descriptor `(n,C_B)` and checkpoint `Z`,

\[
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}},
\]

and same-source realization is checked by

\[
Y_B(Z)-y\equiv0\pmod{3^q}
\]

plus the exact source-parameter interval test.

Canonical files:

- `../theorems/SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`;
- `../src/A0_s1_source_activation_checkpoint_provenance_join_certificate.py`;
- `../audits/S10_SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN_AUDIT.md`.

Derived checkpoint observations such as `z_2` and `z_H` remain derived coordinates after provenanced `Z` exposure, not independent filters.

## Principal global bottleneck

The global bottleneck is now

\[
\boxed{
\text{exact branch predicates}
+\text{checkpoint→same-source transport}
+\text{global cover}.}
\]

More concretely:

1. recover/prove exact Route-A entrance/source predicate;
2. prove checkpoint-surplus provenance if a global formula such as `s_cp=A0-j_*` is needed;
3. for every live `s_cp>=2` checkpoint sector, construct exact ordinary-source charts through a same-source/same-orbit realization relation;
4. prove whether any additional branch family is needed;
5. prove
   \[
   CE\subseteq\bigcup_\alpha B_\alpha;
   \]
6. close every covered source branch.

The canonical transport obligation is

`../theorems/CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`.

## External closure inheritance test

A newly specified Route-A or `s_cp>=2` branch may use the existing external finite-range lemma only after proving its exact ordinary-source domain \(\mathcal D\) satisfies an inclusion such as

\[
\mathcal D\subseteq[1,L_{RS}].
\]

The current Route-B source bound is downstream and branch-specific; it cannot be copied to another sector.

## Optional internal Route-B bottleneck

The internal path remains open at the source-preserving event/valuation exporter to the `q_rem=28` activation seam and the low-precision terminal carry family with source provenance.

This is now a secondary research/audit path rather than the principal global path.

## Still OPEN

### Principal global

- Route-A exact entrance/source predicate;
- checkpoint-surplus global provenance relation, if needed;
- `s_cp>=2` same-source realization transport;
- exact ordinary-source charts for all remaining sectors;
- global branch cover/overlap theorem;
- global Collatz conclusion.

### Optional internal Route-B

- exact `H_5` equality;
- compressed source-preserving paired late-activation / ordinary-`Z` exporter;
- low-precision terminal carry-family export with source provenance;
- exact self-contained 14-root source/checkpoint realization;
- remaining tail/renewal membership predicates.

## Closed / do not reopen by accident

- current physical Route-B source sector on external-dependency path;
- terminal target-dominance-only pruning as an independent gate;
- local source/checkpoint same-orbit join once a paired activation record is supplied;
- exposed-checkpoint observation state minimization;
- `q_rem=28` means 28 future one-events, not a universal short raw-bit suffix.

## Forbidden shortcuts

- `s_cp>=2` checkpoint difference -> exact source branch;
- historical `s=A0-j_*` notation -> canonical identity without provenance proof;
- file-local constants -> global constants;
- Route-B source bound -> Route-A/`s_cp>=2` source bound;
- branch name -> branch predicate;
- finite list of branch names -> exhaustive cover;
- equal control/compressed state -> equal source payload;
- CRT compatibility -> same orbit;
- debit-corridor localization -> same orbit;
- derived terminal observations as independent filters;
- `H_5<=50 -> H_5=50`;
- local Route-B closure -> global Collatz.

## Immediate next work

1. Use `GLOBAL_BRANCH_SPECIFICATION.md` as the source-level branch table.
2. Develop `CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md` from the first checkpoint stage at which `s_cp>=2` changes an ordinary-source-compatible state.
3. Search upstream history only for an exact Route-A predicate; do not invent one from downstream signs or labels.
4. If a transported source domain is proved below `L_RS`, close that branch on the external-dependency path and record the dependency explicitly.
5. Keep the optional internal Route-B exporter work separate from the principal global proof route.
