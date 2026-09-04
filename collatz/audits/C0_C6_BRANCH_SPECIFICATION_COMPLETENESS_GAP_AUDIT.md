# C0/C6 audit — branch specification and completeness gap

Date: **2026-09-05**

Status: **SPECIFICATION GAP CONFIRMED / principal global gate**

## Purpose

After the current `A0,s=1,Route-B` physical source corridor became closed on the
accepted external finite-range proof path, the shortest remaining global path
moves to C6:

- Route-A;
- all surplus sectors `s>=2`;
- any other branch families required by the global decomposition;
- final global branch completeness.

This audit asks a prerequisite question before any theorem is transferred from
Route-B:

> Are those remaining branches already specified in the repository with enough
> exact information to support a proof obligation?

The answer is **no** at the current canonical interface level.

The repository names Route-A and `s>=2` as unresolved obligations, but the live
canonical stack/open-gate register does not yet provide a complete exact branch
specification comparable to the existing `A0,s=1,Route-B` specification.

## 1. What is already specified for the current Route-B sector

The active Route-B stack has an exact working domain with at least the following
objects explicitly defined:

1. fixed target data
   \[
   t_0=104{,}398{,}605{,}910,
   \qquad
   j_0=65{,}868{,}186{,}701;
   \]
2. exact source channels
   \[
   X=r+2^h m,
   \qquad
   T^h(X)=y+3^q m;
   \]
3. finite parameter intervals;
4. the `s=1` surplus/control state;
5. the retained 14-root source forest after stated SAFE cuts;
6. exact transition rules and downstream predicates;
7. an explicit physical source corridor;
8. a dependency chain showing which bounds are available only after
   Route-B-specific reductions.

This is sufficient to state and audit individual Route-B implications.

## 2. Current C6 labels are not yet branch specifications

The canonical proof stack currently ends by stating that

```text
Route-A, all s>=2 sectors, remaining branches, and global branch completeness
must be independently closed.
```

The open-gate register similarly contains only:

```text
G8 — Route-A completion
G9 — All-surplus s>=2
G10 — Global branch completeness
```

These are correct proof obligations, but they are **labels for obligations**, not
complete mathematical definitions of the branch domains.

At the current canonical interface, no single source of truth supplies all of
the following for Route-A or for general `s>=2`:

- branch membership predicate;
- ordinary-integer/source domain;
- source coordinate chart;
- branch boundary conditions;
- relation to the A0 checkpoint/target data;
- disjointness or overlap policy relative to Route-B;
- proof that every hypothetical counterexample is assigned to at least one
  listed branch.

Therefore a long computation cannot yet be interpreted as "closing Route-A" or
"closing all `s>=2`" without first supplying those definitions.

## 3. Required Branch Specification Theorem

For each live branch label `B_alpha`, the global proof needs an exact predicate

\[
\boxed{P_\alpha(x,\mathcal O_x)}
\]

on an ordinary positive start `x` and/or its deterministic Collatz orbit
`\mathcal O_x`, such that branch membership means

\[
x\in B_\alpha
\iff
P_\alpha(x,\mathcal O_x).
\]

The theorem must then derive the branch-local coordinates actually used by the
computation.

At minimum each branch specification must state:

1. **entrance condition** — the first orbit event/checkpoint at which the branch
   is assigned;
2. **control labels** — e.g. Route-A/Route-B and surplus `s`, with exact formulas;
3. **source domain** — the allowed ordinary `X` values or a proved source chart;
4. **target/checkpoint data** — fixed or variable quantities and their domain;
5. **continuation obligations** — which formation/tail/renewal predicates remain;
6. **exit/closure criterion** — what mathematical result eliminates or
   discharges the branch.

A branch name is not itself a predicate.

## 4. Required Global Branch Completeness Theorem

Let `CE` denote the set of hypothetical positive Collatz counterexample starts.
Let the completed branch family be

\[
\mathcal B=\{B_\alpha:\alpha\in A\}.
\]

The proof needs an exact covering statement

\[
\boxed{
CE\subseteq\bigcup_{\alpha\in A}B_\alpha.
}
\]

If the branch computation assumes a partition rather than a cover, it must also
prove pairwise disjointness:

\[
B_\alpha\cap B_\beta=\varnothing
\qquad(\alpha\ne\beta).
\]

Disjointness is not mandatory if overlaps are explicitly allowed, but then the
proof accounting must specify how overlapping branches are handled and must not
multiply or add marginal counts as though they were disjoint.

Finally, each branch closure theorem must have the implication

\[
B_\alpha\cap CE=\varnothing.
\]

Only after every `alpha` is closed may one infer

\[
CE=\varnothing.
\]

## 5. Route-B refined X bound is not currently transferable

The current refined source corridor

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}
\]

is recorded downstream of the `A0,s=1,Route-B` near-threshold / radius-7 /
defect reduction chain.

Therefore the logical implication presently certified is of the form

\[
\boxed{
P_{A0,s=1,RouteB}
\Longrightarrow
X\in I_B,
}
\]

not

\[
\text{arbitrary remaining Collatz branch}
\Longrightarrow X\in I_B.
\]

Accordingly the external recursive-sufficiency closure of `I_B` cannot be
transferred to Route-A or `s>=2` until a separate theorem proves that their
source domains lie inside the same externally verified interval.

This is a dependency issue, not merely a missing numerical comparison.

## 6. DSD analysis

### Branch label as a control coordinate

A branch label is a **control coordinate** only after a mathematical predicate
makes it observable from the underlying orbit state.

Until then, labels such as

```text
Route-A
Route-B
s=1
s>=2
```

are bookkeeping names rather than proven quotient coordinates.

### Source payload remains independent

Even when two branches share a control label or target geometry, their ordinary
source payloads cannot be merged unless every remaining predicate is invariant
under that identification.

### Resolution rule

The correct DSD order is therefore

```text
ordinary orbit
  -> exact branch-observation predicate
  -> branch/control coordinate
  -> branch-specific source chart
  -> branch-local compressed state
  -> branch closure predicate.
```

It is invalid to reverse the order by inventing a convenient compressed branch
state first and then assuming every counterexample maps into it.

## 7. Audit classification

### CONFIRMED / CLOSED AS AN AUDIT FINDING

- Route-A is named as an open C6 obligation but lacks a complete canonical exact
  branch specification at the current live interface;
- `s>=2` is named as an open C6 obligation but lacks a complete canonical exact
  all-surplus source/domain theorem at the current live interface;
- global branch completeness remains explicitly open;
- the Route-B refined `X` bound is downstream of Route-B-specific dependencies
  and cannot presently be inherited by those sectors.

### PRINCIPAL GLOBAL OPEN GATE

Construct and certify:

1. the exact Route-A predicate/source domain;
2. the exact surplus-sector definition for arbitrary `s>=2`;
3. any additional branch labels needed for exhaustiveness;
4. the global cover/partition theorem mapping every hypothetical counterexample
   into the completed branch family.

### REJECTED

- `Route-A` appearing in a roadmap -> Route-A mathematically specified;
- `s>=2` appearing in a roadmap -> all surplus sectors specified;
- Route-B source bound -> same bound for Route-A;
- `s=1` formula -> unchanged all-surplus formula without proof;
- Route-B external closure -> A0 closure;
- A0 closure -> global Collatz;
- finite branch names -> exhaustive counterexample partition.

## 8. Immediate next construction

The next proof object should be

```text
GLOBAL_BRANCH_SPECIFICATION.md
```

or an equivalent theorem series, beginning upstream of all Route-B-specific
SAFE cuts.

It should recover the exact definitions from the earliest A0/formation
construction and produce a machine-checkable branch table of the form

| branch id | entrance predicate | surplus domain | ordinary source domain | required closure module |
|---|---|---|---|---|

Only after that table is certified should external finite-range closure or
Route-B structural theorems be inherited by another row.

## Canonical dependencies inspected

- `../CANONICAL_PROOF_STACK.md`;
- `../PROOF_MAP.md`;
- `../status/OPEN_GATES.md`;
- `../status/CURRENT_STATUS.md`;
- `../status/DEPENDENCY_LEDGER.md`;
- `../frontier/A0_S1_ROUTEB.md`;
- `../frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`.
