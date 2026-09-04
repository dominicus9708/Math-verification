# S10 audit — external recursive-sufficiency source closure

Date: **2026-09-05**

Status: **EXTERNAL FINITE-RANGE CLOSURE ACCEPTABLE / INTERNAL BRIDGE REMAINS OPTIONAL-OPEN**

## Audit question

Does the current `A0,s=1,Route-B` source-preserving late-activation bridge still
need to be completed in order to reject the current finite physical source
corridor as a counterexample source set?

## Inputs

### Internal certified source corridor

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}.
\]

### External verified baseline

Bařina's convergence verification includes all positive starting values below
`2^71`.

### External recursive-sufficiency theorem

Ansari (2025), Proposition 3.2 and its supporting recursively sufficient set,
give the following finite extension: if `[1,2*3^n+1]` is already verified, then
all integers through

\[
4\,3^n+2
\]

are verified as well.

For `n=44`,

\[
2\,3^{44}+1<2^{71},
\]

so the verified baseline contains the premise.

## Independent arithmetic audit

Exactly,

\[
N_{44}=2\,3^{44}+1
=1{,}969{,}541{,}804{,}367{,}222{,}465{,}763,
\]

\[
2^{71}=2{,}361{,}183{,}241{,}434{,}822{,}606{,}848,
\]

and therefore

\[
N_{44}<2^{71}.
\]

The extended bound is

\[
L_{RS}=4\,3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
\]

The exact current source upper endpoint is

\[
U_X
=\frac43 2^{71}+\frac{239}{500}2^{33}
=\frac{1180591620718951049199616}{375}.
\]

The margin is

\[
L_{RS}-U_X
=\frac{296564732556465800122634}{375}>0.
\]

Thus

\[
\boxed{X<L_{RS}}
\]

for every current ordinary source integer.

## Logical audit

The conclusion used here is weaker than global Collatz:

> every ordinary positive source `X` in the current finite Route-B physical
> corridor has already been covered by a finite convergence theorem.

A hypothetical nonconvergent orbit cannot pass through a positive integer whose
forward orbit is known to reach `1`.  Therefore a true counterexample cannot
realize any of the current Route-B source states.

This rejects the **current source corridor**, not the infinite Collatz problem.

## DSD classification

### Internal axis

The current long bridge tracks increasingly fine source/parity/formation
coordinates in order to determine whether a source can reach the late terminal
seam.

### External predicate

The external finite-range result observes a much coarser property:

```text
ordinary source integer X belongs to an interval already known to converge
```

This predicate is source-sensitive and is already decisive at the entrance of
the current Route-B source forest.  Once it is accepted, all downstream
coordinates become irrelevant for counterexample rejection in this finite
sector.

### Legal forgetting

It is therefore legal, **for the external-closure proof path**, to forget:

- late activation coordinates;
- terminal `(n,C_B)` descriptors;
- `F_28` and `z_H`;
- checkpoint `Z`;
- right-H and post-checkpoint membership states;

because the source has already been discharged by a stronger decisive
predicate.

This does not authorize forgetting those coordinates in the separate
self-contained internal research path.

## Dependency audit

The arithmetic comparison has been independently checked in-repository.

The mathematical closure additionally depends on accepting:

1. Bařina's finite computational verification result;
2. Ansari's recursively sufficient set construction and Proposition 3.2.

The Ansari proof was inspected through the published paper, including:

- Theorem 2.1 / Corollary 2.2 for recursively sufficient sets;
- Lemma 3.1 establishing the nested recursively sufficient sieves;
- Lemma 3.2 identifying their intersection;
- Proposition 3.2 proving the interval gap `(N,2N] cap F = empty`.

No independence assumption, probabilistic multiplication, or extrapolation of
finite trajectory statistics is used.

## Verdict

### CLOSED under accepted external literature dependency

\[
\boxed{\text{current }A0,s=1,Route-B\text{ physical source corridor contains no counterexample source}.}
\]

### INTERNAL STATUS

The source-preserving late-activation bridge remains mathematically interesting
and may continue as a **self-contained independent derivation**, but it is no
longer necessary to reject this particular finite source corridor if external
finite-range results are allowed as lemmas.

### GLOBAL STATUS

Still open:

- Route-A;
- all `s>=2` sectors;
- remaining branch families;
- proof that the branch decomposition is globally exhaustive;
- the Collatz conjecture itself.

## Rejected overclaims

- current Route-B source closure -> global Collatz;
- finite verified bound -> asymptotic theorem;
- external dependency -> internally original theorem;
- published result -> automatically error-free without scope auditing;
- source convergence -> every unrelated formal candidate descriptor is valid.

## Canonical dependencies

- `../theorems/EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`;
- `../src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`.
