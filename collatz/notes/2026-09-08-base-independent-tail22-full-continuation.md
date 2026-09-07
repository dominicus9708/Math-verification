# MATH-034 — base-independent 22-step full continuation

Date: 2026-09-08

Status:

`CONFIRMED / EXACT CONTINUATION ACCELERATION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Purpose

MATH-033 proved that one critical prefix per `2^22` residue gives the exact 22-step coefficient-survival threshold at arbitrary base depth `K`:

\[
H_K(u)=q_{\rm pub}(K+j_*(u))-s_*(u).
\]

MATH-034 applies this descriptor to the complete MATH-032 `RMAX=10^9` depth-83+ continuation.

## Endpoint arithmetic choice

A one-shot fixed-width evaluation of

\[
(3^{s_{22}}n+c_{22})/2^{22}
\]

can overflow a 128-bit intermediate even when the exact post-division value remains representable.

Therefore the final engine deliberately evaluates each 22-step endpoint transition as **two previously audited exact 11-step affine updates**.

The 22-step critical descriptor is used for the threshold gate; the two 11-step maps are used for safe exact endpoint arithmetic.

This separates proof-state compression from machine-integer representation.

## Exact finite regression

The calculation reproduces the established finite input counts:

\[
\boxed{1,796,718}
\]

depth-61 right-offset survivors and

\[
\boxed{189,767,400}
\]

exact depth-83 address-state instantiations after the MATH-031 prefilter.

From base depth 83 onward, the base-independent 22-step gate is evaluated

\[
\boxed{294,223,428}
\]

times.

The final result exactly matches MATH-028 and MATH-032:

- audited-end survivors: `0`;
- endpoint overflow after sequential 11-step evaluation: `0`;
- deepest failing block base:

\[
\boxed{545};
\]

- first witness:

\[
\boxed{r=378,620,799,\qquad b=1183}.
\]

Thus the finite internal adjacent-block same-endpoint coupling exclusion remains

\[
\boxed{61\le k\le3,000,000,003}.
\]

## Threshold-gate reduction

MATH-032 used

\[
467,202,551
\]

11-step threshold checks from base depth 83 onward.

MATH-034 uses

\[
294,223,428
\]

22-step threshold gates for the same finite continuation.

The reduction is

\[
\boxed{172,979,123}
\]

threshold-gate evaluations, or about

\[
\boxed{37.02\%}.
\]

Equivalently, the threshold-gate count is smaller by a factor of about

\[
\boxed{1.5879}.
\]

This is not an equal wall-clock speedup: a successful 22-step state still executes two exact 11-step affine endpoint updates.

## DSD interpretation

The calculation now separates two roles:

1. **descriptor/gate:** `(j_*,s_*)` determines whether a 22-step block can survive the coefficient predicate at arbitrary base `K`;
2. **exact state transition:** the ordinary endpoint is propagated by two safe 11-step affine updates.

This avoids both over-resolution in the threshold metadata and under-resolution in the propagated state.

## Scope boundary

Do not infer:

- 37.02% threshold-gate reduction ⇒ equal runtime reduction;
- 22-step local descriptor ⇒ global finite-state quotient;
- finite `RMAX=10^9` regression ⇒ all right offsets;
- same-endpoint coupling exclusion ⇒ first-cell emptiness;
- computational acceleration ⇒ Collatz proof.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_base_independent_tail22_full_continuation_certificate.cpp`

Certificate commit:

`be0f5423aecd179bff64f75bc8bbef1d7f1d93ee`
