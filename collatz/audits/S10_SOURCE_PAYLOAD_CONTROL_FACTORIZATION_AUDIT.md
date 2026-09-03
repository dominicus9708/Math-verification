# S10 source-payload / control factorization audit

Date: 2026-09-03

Status: **SAFE structural compression; source-sensitive future quotient remains OPEN**

## 1. State sufficiency correction

The eight-jump pure-ballot certificate used

\[
(y,A,m_{lo},m_{hi},h,S,root_f)
\]

which is sufficient for the stated pure-ballot pruning/counting task.

It is **not** the correct reusable state for later source-sensitive predicates because the exact current ordinary source cylinder

\[
X=r+2^h m
\]

must remain available.

This does not invalidate any previously reported pure-ballot pruning count; it restricts how those states may be handed to later predicates.

## 2. Redundant and required coordinates

Because

\[
S=q-Q(h),
\]

we have exactly

\[
q=Q(h)+S
\]

and

\[
A=3^{Q(h)+S}.
\]

Therefore stored `A` is redundant.

The source-preserving state is normalized to

\[
\boxed{(r,y,m_{lo},m_{hi},h,S;\text{predicate labels}).}
\]

The valuation jump preserves

\[
X=r'+2^{h'}k
\]

exactly with

\[
r'=r+2^h\rho_a,
\qquad h'=h+a+1.
\]

## 3. Control/payload decomposition

Pure-ballot jump legality and outgoing surplus depend only on

\[
(h,S,a).
\]

The source residue calculation and child interval depend on the payload

\[
(r,y,m_{lo},m_{hi}).
\]

Hence transition execution factors as

\[
\boxed{
\text{ballot control template}
\otimes
\text{source arithmetic payload}.
}
\]

This permits implementation sharing without source-family identification.

## 4. Current control compression

At the eight-jump frontier:

- source cylinders: `14,224`;
- surviving ordinary integers: `26,859,837,368,845,079,186` before the secondary defect tightening;
- distinct exact `(h,S)` controls: `90`;
- distinct four-future-jump pure-ballot control signatures: `13`.

Thus transition logic can be substantially deduplicated even though arithmetic payloads remain distinct.

## 5. Secondary first-75 defect-tail tightening

For each exact prefix, the existing monotone normalized defect can be combined with an exact DP floor for the minimum additional first-75 defect needed to reach the already-certified condition `d_75>=8`.

Applying this through the same eight jumps changes the surviving population to

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

The additional exact pruning is

\[
\boxed{256{,}808{,}932}.
\]

Relative to the pure-ballot eight-jump population this is about

\[
9.56\times10^{-12}.
\]

No additional cylinder is closed.

Audit classification: **SAFE but low-yield secondary predicate**. It should not be promoted to the principal S10 engine at this stage.

## 6. DSD classification

### D — domain

The factorization theorem applies to exact accelerated-Collatz source cylinders with certified pure-ballot control.

### R — resolution

`r` must be retained at full current dyadic source resolution for source-sensitive downstream predicates. A coarser representation requires its own invariance theorem.

### S — state sufficiency

For pure-ballot valuation jumping, `(r,y,lo,hi,h,S)` is sufficient and `A` is derived.

### E — equivalence

Equal finite-horizon ballot-control signatures permit reuse of control transition skeletons only. They do not establish source-payload equivalence.

### T — transition

The exact transition is the product of a source-independent ballot-control transition and a source arithmetic valuation-cylinder transition.

### C — closure

No H/L, C4F, checkpoint/debit, tail, Route-B, or Collatz closure follows.

### N — non-independence

The finite-horizon control quotient must not be multiplied as an independent sparsity factor with source survival ratios.

### O — outstanding

1. add exact H/L/pre-bridge future-control update to the source-preserving valuation jump;
2. identify the precise C4F/renewal state required after each jump;
3. determine whether those controls admit a source-sensitive future-equivalence quotient;
4. retain checkpoint/debit information only at the resolution where it becomes active;
5. use `P_min`/defect only as secondary labels unless stronger closure appears.

## Canonical objects

- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `../theorems/FINITE_HORIZON_BALLOT_CONTROL_SIGNATURE.md`;
- `../src/A0_s1_source_payload_control_factorization_certificate.py`;
- `../src/A0_s1_finite_horizon_ballot_control_signature_certificate.py`;
- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`.
