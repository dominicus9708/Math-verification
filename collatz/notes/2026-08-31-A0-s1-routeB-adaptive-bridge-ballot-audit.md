# A0 s=1 Route-B adaptive bridge + ballot audit

## Scope

This audit closes the adaptive refinement law for the fixed-resolution dual-adic correction bridge and verifies its exact compatibility with the previously closed phase-critical ballot summary.

It does **not** claim that the resulting finite quotient recognizes the universal Route-B admissible language.

## Exact correction refinement law

For two parity blocks `U,V` with the same exact length `h` and odd-count `q`, write

\[
\Delta=C(U)-C(V)\ne 0.
\]

At resolution `(K,L)` the correction bridge state is

\[
S_{K,L}(W)=\bigl(3^{q(W)},2^{h(W)},C(W)\bmod 2^K3^L\bigr).
\]

Because `h,q` agree, the first two coordinates agree automatically. Therefore

\[
S_{K,L}(U)=S_{K,L}(V)
\iff
2^K3^L\mid\Delta.
\]

Equivalently,

\[
S_{K,L}(U)=S_{K,L}(V)
\iff
K\le v_2(\Delta),\quad L\le v_3(\Delta).
\]

Hence either one-axis refinement

\[
K_*=v_2(\Delta)+1
\]

or

\[
L_*=v_3(\Delta)+1
\]

separates the correction candidates exactly.

This is the required adaptive rule: resolution is increased only for a colliding candidate class.

## Combined ballot state

The correction bridge was paired with the exact ballot summary

\[
(h,q,m,a),
\]

where `m` is the base ballot minimum and `a` the phase-critical prefix.

The combined fixed-resolution state is therefore

\[
\Sigma_{K,L}(W)
=
\bigl(h,q,3^q,2^h,C\bmod 2^K3^L,m,a\bigr).
\]

Both sectors are compositionally closed. The certificate explicitly finds collisions in this combined state and appends all common right extensions up to length 3; every collision remains a collision after the same extension.

Thus the combined state is a finite right-congruence at each fixed `(K,L)`.

## Regression results

The certificate `collatz/src/A0_s1_routeB_adaptive_bridge_ballot_certificate.py` reports:

```text
PASS A0 s=1 Route-B adaptive bridge + ballot congruence certificate
pair_depth 10
same_hq_pair_checks 124453
collision_equivalence_checks 3540948
adaptive_dyadic_separation_checks 124453
adaptive_ternary_separation_checks 124453
valuation_classes 45
max_v2 8
max_v3 8
combined_collision_pairs 1233
combined_extension_checks 18495
```

No mismatch occurred.

## Formation-Axiom audit

The intrinsic block description remains fixed while only an externally requested correction resolution is refined. No hidden materialized word is introduced into parent-state formation.

Status: ✅ structurally admissible.

## Axis-property audit

Dyadic resolution `K` and ternary resolution `L` are treated as external observation axes. They can be refined independently without changing the intrinsic block coordinates or the ballot critical-prefix coordinate.

Status: ✅ axis separation preserved.

## DSD audit

✅ exact collision criterion established;

✅ adaptive one-axis separator established;

✅ combined correction+ballot right-extension congruence verified;

❌ no inference from finite congruence to universal Route-B language recognition;

❌ G5 universal membership remains open.

## Updated gate status

- G1 minimal correction state: CLOSED.
- G2 correction + ballot block composition: CLOSED.
- G3 fixed-resolution correction congruence: CLOSED for the correction sector.
- G4 adaptive correction refinement: CLOSED.
- G4 correction+ballot finite right-congruence: CLOSED.
- G4 target-aware adaptive lazy decoder: NEXT.
- G5 universal Route-B membership: OPEN.

The next task is not to increase a global fixed resolution. It is to construct the target-aware lazy decoder that maintains a partition of candidates by `Sigma_{K,L}`, refines only colliding classes, and descends through the Christoffel hierarchy only when the current block summary cannot decide admissibility.
