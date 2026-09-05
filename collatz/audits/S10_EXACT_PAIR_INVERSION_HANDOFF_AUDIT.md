# S10 exact-pair inversion handoff audit

Date: 2026-09-03

Status: **PAIRWISE INVERSION CLOSED / FAMILY COMPRESSION OPEN**

## Audit trigger

The active frontier stated that fixed-`(t,q)` correction injectivity did not by itself provide an inverse algorithm.
That statement is true if one imports only injectivity, but the repository already contains a stronger valuation decoder:

- `../src/A0_s1_correction_language_injective_decoder_certificate.py`;
- `../src/A0_s1_modular_prefix_decoder_certificate.py`.

The new residual theorem integrates those facts with the exact source/end-state equation:

- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../src/A0_s1_residual_valuation_jump_decoder_certificate.py`.

## Corrected S10 classification

For one exact remaining instance `(Y,Z,n,q)`, define

\[
R=2^nZ-3^qY.
\]

If `q>0`, a realizing word must begin with `0^a1`, where

\[
\boxed{a=v_2(R).}
\]

The prefix is then discharged exactly and the same residual problem restarts.
Therefore an exact pair has either zero or one correction word, and that word is deterministically recoverable.

### CLOSED

- uniqueness at fixed `(n,q)`;
- exact inverse for a fully specified `(Y,Z,n,q)` pair;
- exact forced-zero-run jump;
- rejection when the forced valuation exceeds the remaining length;
- exact self-similar restart after the forced prefix.

### STILL OPEN

- running the decoder over the enormous source/checkpoint families without memberwise enumeration;
- proving a nontrivial cylinder/interval quotient that preserves future valuation branches;
- checking H/L/C4F/Route-B formation predicates on the forced family paths;
- S11 checkpoint/debit/tail realization.

## DSD diagnosis

The previous wording mixed two different resolutions:

1. **exact-pair resolution** — the correction-language branch axis is already collapsed to zero-or-one;
2. **family resolution** — different family members may have different `v2(R)` and therefore different forced prefixes.

The unresolved problem belongs to resolution 2, not resolution 1.

This prevents an unnecessary search over correction words at exact-pair resolution and also prevents overclaiming that pairwise determinism automatically yields family compression.

## Next target

Construct an exact **valuation-cylinder quotient** for affine source/checkpoint families.

For a family in which

\[
Y=Y_0+A m,
\qquad
Z=Z_0+B m
\]

or a finite union of such classes, the required residual has affine form

\[
R(m)=R_0+R_1m.
\]

The next useful theorem should characterize parameter subcylinders on which

\[
v_2(R(m))
\]

is constant, or on which the first forced jump is identical.

Because valuation conditions are congruence conditions modulo powers of two, this is the natural exact bridge from pairwise decoding to family-level block jumps.

## Forbidden inference

Do not infer that pairwise decoder uniqueness closes S10 globally.
The family-level quotient and remaining formation predicates are separate obligations.
