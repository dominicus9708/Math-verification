# C0/C6 audit — branch specification and completeness gap

Date: **2026-09-05**

Status: **SPECIFICATION GAP CONFIRMED / surplus coordinate recovered / principal global gate refined**

## Purpose

After the current `A0,s=1,Route-B` physical source corridor became closed on the
accepted external finite-range proof path, the shortest remaining global path
moves to C6:

- Route-A;
- all surplus sectors `s>=2`;
- any other branch families required by the global decomposition;
- final global branch completeness.

This audit asks which of those objects are already mathematically specified and
which remain only roadmap labels.

## 1. Exact upstream surplus coordinate is already recovered

The canonical upstream proof map defines

\[
\gamma:=\log_2 3,
\qquad
A_0:=\lceil \gamma C\rceil,
\]

and the lower-case surplus coordinate by

\[
\boxed{
s:=\lceil \gamma C\rceil-j_\star=A_0-j_\star.
}
\]

Therefore

\[
\boxed{j_\star=A_0-s.}
\]

The `s=0` sector is structurally eliminated upstream, and the live minimal
surplus sector is therefore `s=1`, where

\[
A_0=j_\star+1.
\]

This corrects the earlier provisional wording of this audit: **the scalar
surplus coordinate `s` is not undefined**.

The remaining `s>=2` gap is instead the absence, at the current canonical live
interface, of a complete theorem transporting those surplus values into exact
ordinary-source domains, branch-local coordinates, and closure obligations.

### Notation warning

This lower-case surplus `s` is distinct from the persistent Route-B source
control coordinate `S` occurring in relations such as

\[
q=Q(h)+S.
\]

They must not be identified.

## 2. What is already specified for the current Route-B sector

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
4. the exact upstream surplus condition `s=1`;
5. the retained 14-root source forest after stated SAFE cuts;
6. exact transition rules and downstream predicates;
7. an explicit physical source corridor;
8. a dependency chain showing which bounds are available only after
   Route-B-specific reductions.

This is sufficient to state and audit individual Route-B implications.

## 3. Route-A remains an unresolved semantic branch label

The live proof map and open-gate register name Route-A as a remaining global
obligation. However, at the current canonical interface no exact predicate has
yet been recovered of the form

\[
\boxed{P_A(x,\mathcal O_x)}
\]

such that

\[
x\in\mathrm{RouteA}\iff P_A(x,\mathcal O_x).
\]

The same repository also records an important correction: the older naive
prefix interpretation based only on a sign condition such as `U_t>=0` is
structurally invalid. Consequently Route-A must **not** be reconstructed by
relabeling the rejected naive surplus-prefix branch.

Until its original exact entrance predicate is recovered or replaced by a newly
proved equivalent predicate, `Route-A` is a roadmap/control label rather than a
certified quotient coordinate.

## 4. The remaining `s>=2` obligation is a transport/domain theorem

Because `s` itself is exact, the unresolved all-surplus task should be stated as:

> Given the exact upstream condition `s>=2`, derive the complete ordinary-source
> domain, any necessary subordinate route predicates, the branch-local source
> charts, and the exact closure criterion without importing Route-B-only SAFE
> reductions.

At minimum this requires proving how

\[
s=A_0-j_\star\ge2
\]

propagates into the later formation / first-failure / checkpoint variables used
by the computation.

It is not enough to substitute `s>=2` into formulas proved only after the
`s=1,Route-B` specialization.

## 5. Required Branch Specification Theorem

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
2. **control labels** — Route-A/Route-B and surplus `s`, with exact formulas;
3. **source domain** — the allowed ordinary `X` values or a proved source chart;
4. **target/checkpoint data** — fixed or variable quantities and their domain;
5. **continuation obligations** — which formation/tail/renewal predicates remain;
6. **exit/closure criterion** — what mathematical result eliminates or
   discharges the branch.

A branch name is not itself a predicate.

## 6. Required Global Branch Completeness Theorem

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

## 7. Route-B refined X bound is not currently transferable

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

## 8. DSD analysis

### Surplus as a certified coordinate

The lower-case surplus `s=A_0-j_*` is an exact integer observation derived from
upstream data. It may be used as a genuine branch coordinate.

### Route label as an uncertified coordinate until a predicate is recovered

A Route-A/Route-B label is a **control coordinate** only after a mathematical
predicate makes it observable from the underlying orbit state.

### Source payload remains independent

Even when two branches share a surplus value or target geometry, their ordinary
source payloads cannot be merged unless every remaining predicate is invariant
under that identification.

### Resolution rule

The correct DSD order is

```text
ordinary orbit
  -> exact upstream surplus s
  -> exact route/branch observation predicate
  -> branch-specific source chart
  -> branch-local compressed state
  -> branch closure predicate.
```

It is invalid to reverse the order by inventing a convenient compressed branch
state first and then assuming every counterexample maps into it.

## 9. Audit classification

### CONFIRMED / CLOSED AS AUDIT FINDINGS

- lower-case surplus
  \[
  s=A_0-j_\star
  \]
  is already exactly defined upstream;
- `s=0` is structurally eliminated in the upstream proof map;
- `s=1` is therefore the minimal live surplus sector;
- Route-A is named as an open C6 obligation but currently lacks a recovered
  canonical exact entrance predicate/source specification;
- `s>=2` has an exact scalar definition but lacks a complete all-surplus
  source/domain/closure transport theorem;
- global branch completeness remains explicitly open;
- the Route-B refined `X` bound is downstream of Route-B-specific dependencies
  and cannot presently be inherited by those sectors.

### PRINCIPAL GLOBAL OPEN GATE

Construct and certify:

1. the exact Route-A predicate/source domain;
2. the exact transport theorem for every `s>=2` sector;
3. any additional branch labels needed for exhaustiveness;
4. the global cover/partition theorem mapping every hypothetical counterexample
   into the completed branch family.

### REJECTED

- `Route-A` appearing in a roadmap -> Route-A mathematically specified;
- naive `U_t>=0` prefix sign -> Route-A definition;
- `s>=2` appearing in a roadmap -> all surplus source domains specified;
- Route-B source bound -> same bound for Route-A;
- `s=1` downstream formula -> unchanged all-surplus formula without proof;
- Route-B external closure -> A0 closure;
- A0 closure -> global Collatz;
- finite branch names -> exhaustive counterexample partition.

## 10. Immediate next construction

The next proof object remains

```text
GLOBAL_BRANCH_SPECIFICATION.md
```

or an equivalent theorem series, beginning upstream of all Route-B-specific
SAFE cuts.

Its first certified rows may already use the recovered surplus coordinate, but
Route-A must remain explicitly `UNSPECIFIED` until its entrance predicate is
recovered from history or replaced by a new proved equivalent definition.

A machine-checkable table should have the form

| branch id | entrance predicate | surplus domain | ordinary source domain | required closure module |
|---|---|---|---|---|

Only after a row is fully specified should external finite-range closure or
Route-B structural theorems be inherited by that row.

## Canonical dependencies inspected

- `../CANONICAL_PROOF_STACK.md`;
- `../PROOF_MAP.md`;
- `../status/OPEN_GATES.md`;
- `../status/CURRENT_STATUS.md`;
- `../status/DEPENDENCY_LEDGER.md`;
- `../frontier/A0_S1_ROUTEB.md`;
- `../frontier/A0_S1_ROUTEB_EXTERNAL_CLOSURE.md`;
- `../notes/2026-08-27-A0-s1-Xi-Minkowski-factorization.md`.
