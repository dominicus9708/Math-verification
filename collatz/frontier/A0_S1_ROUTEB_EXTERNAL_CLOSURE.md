# A0 `s=1` Route-B — external closure status

Status: **CLOSED as a counterexample source sector if accepted external finite-range Collatz results are allowed**

Date: **2026-09-05**

## Canonical conclusion

The internally certified physical source corridor is

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}.
\]

Every integer in this corridor lies below

\[
\boxed{4\,3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.}
\]

Bařina's finite verification through `2^71`, combined with Ansari's 2025
recursive-sufficiency Proposition 3.2 specialized to `n=44`, establishes
convergence for every positive integer up to that bound.

Therefore the current `A0,s=1,Route-B` physical source corridor contains no
ordinary positive counterexample source.

## Status split

### External-dependency proof path

\[
\boxed{A0,s=1,Route-B:\ CLOSED}
\]

for counterexample rejection.

No late-activation, terminal-descriptor, checkpoint, or right-H expansion is
needed on this path.

### Internal self-contained DSD path

\[
\boxed{A0,s=1,Route-B:\ OPEN\ as\ an\ independent\ reconstruction}
\]

The existing `A0_S1_ROUTEB.md` remains the canonical resume document for that
independent route.  Its principal open task remains the source-preserving
late-activation / terminal-descriptor construction.

The internal route should not be deleted, because it tests the DSD method and
may produce reusable structural theorems for sectors not covered by this same
finite source interval.

## Dependencies

- `../theorems/EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md`;
- `../src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`;
- `../audits/S10_EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CLOSURE_AUDIT.md`.

External literature:

- D. Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), Article 810;
- M. Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, NNTDM 31(3) (2025), 471--480.

## Global warning

This closes only the current finite `A0,s=1,Route-B` counterexample source
sector under the stated external dependencies.  It does not close Route-A,
`s>=2`, other branches, branch completeness, or the Collatz conjecture.