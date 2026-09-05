# A0 s=1 Route-B two-sided residue localization audit — 2026-08-30

## Result

The Route-B block state admits an exact two-sided localization, but fixed low-resolution boundary data are not sufficient to identify the internal Christoffel formation.

This produces one positive result and one useful negative result for G3/G4:

- ✅ source dyadic and endpoint ternary constraints can be propagated recursively without materializing the giant word;
- ❌ a quotient using only those fixed-resolution boundary constraints is not separating, even after adding one internal cut/interface constraint.

The second result rules out a tempting but insufficient meet-in-the-middle state before it is used as a proof device.

## 1. Exact two-sided boundary coordinates

For a parity block `B` of length `h`, with `q` odd symbols and correction `C(B)`,

\[
2^hY=3^qX+C(B).
\]

For `K<=h`, define the canonical source residue

\[
\boxed{
x_K(B)=-C(B)(3^q)^{-1}\pmod{2^K}.
}
\]

For `R<=q`, define the canonical endpoint residue

\[
\boxed{
y_R(B)=C(B)(2^h)^{-1}\pmod{3^R}.
}
\]

These are exact cylinder projections, not floating or heuristic signatures.

## 2. Concatenation localization

For `W=UV`,

\[
C(UV)=3^{q(V)}C(U)+2^{|U|}C(V).
\]

If `K<=|U|`, the second term vanishes modulo `2^K`, hence

\[
\boxed{x_K(UV)=x_K(U).}
\]

If `R<=q(V)`, the first term vanishes modulo `3^R`, hence

\[
\boxed{y_R(UV)=y_R(V).}
\]

Thus the external low-resolution signature screens to the outer children:

\[
\boxed{
B_{K,R}(UV)=\bigl(x_K(U),y_R(V)\bigr).
}
\]

This is exact whenever the stated depth inequalities hold.

## 3. Internal-cut coordinate

Let

\[
Z=T^{|U|}(X)
\]

be the state at the `U|V` interface.

The left child requires

\[
Z\equiv y_R(U)\pmod{3^R},
\]

while the right child requires

\[
Z\equiv x_K(V)\pmod{2^K}.
\]

Since `2^K` and `3^R` are coprime, these two congruences define one exact CRT class modulo

\[
2^K3^R.
\]

Therefore an internal interface signature is naturally

\[
\boxed{
I_{K,R}(U,V)=\bigl(y_R(U),x_K(V)\bigr).
}
\]

This is a legitimate internal checkpoint coordinate.  The audit question is whether it actually separates the reused Christoffel formations at the Route-B resolutions.

## 4. Exhaustive arbitrary-word regression

All binary words through length 12 and every nontrivial split were checked.

Results:

- exact correction-composition checks: `81,924`;
- front dyadic screening checks: `458,748`;
- rear ternary screening checks: `229,374`;
- mismatches: `0`.

The front tests used every `1<=K<=|U|` for every split.  The rear tests used every `1<=R<=q(V)` for every split.

## 5. 129-node Christoffel DAG regression

Dyadic resolutions:

`1, 2, 4, 8, 16, 27, 32, 39, 64, 72, 74, 75, 128`.

Ternary resolutions:

`1, 2, 4, 8, 16, 24, 28, 32, 40, 64`.

Results:

- dyadic parent correction projections: `1,651`;
- ternary parent correction projections: `1,270`;
- front child screening checks: `1,560`;
- rear child screening checks: `1,191`;
- mismatches: `0`.

Every DAG node of length at most `100,000` was also independently materialized:

- nodes: `45`;
- total materialized bits across node regressions: `457,063`;
- dyadic/ternary projection comparisons: `1,035`;
- mismatches: `0`.

## 6. Giant threshold block

For the existing decomposition

\[
W_{\rm th}=UL^9,
\]

with

\[
|L|=J_0=10{,}439{,}860{,}591,
\qquad q(L)=R_0=6{,}586{,}818{,}670,
\]

and the existing Route-B identity

\[
C(U)=C(L)+3^{R_0},
\]

the whole giant threshold word was evaluated only through recursive modular summaries.

Its source residue satisfies

\[
x_{27}(W_{\rm th})=29{,}252{,}603,
\]

\[
x_{39}(W_{\rm th})=188{,}068{,}289{,}531,
\]

\[
x_{74}(W_{\rm th})=4{,}697{,}939{,}311{,}072{,}332{,}635{,}131=X_{\rm TH}.
\]

At the next bit,

\[
x_{75}(W_{\rm th})
=23{,}587{,}405{,}242{,}550{,}913{,}489{,}915
\ne X_{\rm TH}\pmod{2^{75}}.
\]

This independently reproduces the known first disagreement at the 75th parity symbol.

The rear endpoint projection screens all the way to the final `L` block:

\[
y_{24}(W_{\rm th})=y_{24}(L)=181{,}784{,}647{,}214,
\]

\[
y_{28}(W_{\rm th})=y_{28}(L)=2{,}158{,}791{,}402{,}581.
\]

The numeric residues are recorded rather than relying on a most/least-significant trit display convention.

## 7. Boundary-only quotient obstruction

The exact localization identities do **not** imply that the boundary signature identifies the block.

On the existing 129-node Stern-Brocot/Christoffel path:

### `(K,R)=(27,28)`

- nodes admitting the external signature: `120`;
- distinct external `(x_27,y_28)` signatures: `1`;
- internal parents admitting the interface signature: `117`;
- distinct `(y_28(left),x_27(right))` signatures: `1`;
- parents admitting both external and interface signatures: `117`;
- distinct four-coordinate external+interface signatures: `1`.

### `(K,R)=(39,28)`

- external eligible: `120`, distinct: `1`;
- interface eligible: `117`, distinct: `1`;
- combined eligible: `117`, distinct: `1`.

### `(K,R)=(74,28)`

- external eligible: `118`, distinct: `1`;
- interface eligible: `117`, distinct: `1`;
- combined eligible: `117`, distinct: `1`.

Therefore even adding one exact CRT interface checkpoint does not separate these large Christoffel nodes at the fixed Route-B exposure depths.

This is not a failure of the residue identities.  It is a failure of the proposed **sufficiency** of the fixed-resolution quotient.

## 8. Formation Axiom System audit

The Formation Axiom System is again used only as a structural audit lens.

The calculation gives an explicit counterexample to the inference

> same exposed boundaries => same internal formation.

At the tested resolutions, many different Stern-Brocot nodes have the same external boundary projections and the same one-cut interface projection.

Therefore:

- ✅ the boundary projections are well-defined consequences of the block formation;
- ✅ child-to-parent projection rules are explicit;
- ❌ the projections do not reconstruct or distinguish the internal formation;
- ❌ they cannot be promoted to a complete Route-B state by themselves.

## 9. Axis-property audit

The source dyadic and endpoint ternary coordinates are legitimate oriented axes:

- the source/left side screens through powers of `2`;
- the endpoint/right side screens through powers of `3`.

But they are not jointly separating at fixed low resolution.

Thus a correct decoder needs an additional structural coordinate.  The current evidence points to one of two forms:

1. a hierarchical Stern-Brocot/Christoffel address or scale coordinate;
2. a resolution that increases with block scale rather than remaining fixed at `27/28`, `39/28`, or `74/28`.

A raw absolute offset is already known to destroy the DAG compression and remains rejected.

## 10. Updated G3/G4 status

### Closed

- ✅ exact two-sided source/endpoint localization;
- ✅ exact internal-cut CRT coordinate;
- ✅ exhaustive finite regression of both identities;
- ✅ giant threshold source and endpoint projections without word materialization.

### Rejected

- ❌ fixed-resolution boundary-only quotient;
- ❌ fixed-resolution boundary+one-interface quotient.

### Still open

- ❌ scale-aware or hierarchy-aware separating state;
- ❌ recursive target-aware `match_and_jump` decoder;
- ❌ universal Route-B membership verdict;
- ❌ Collatz conjecture proof.

The next G3 calculation should therefore measure **how much resolution or hierarchical depth is required to distinguish successive Christoffel nodes**, rather than adding more fixed low-resolution boundary coordinates.

## Reproducibility

Certificate:

`collatz/src/A0_s1_routeB_two_sided_residue_localization_certificate.py`

Expected headline output:

```text
PASS A0 s=1 Route-B exact two-sided residue localization certificate
arbitrary_word_max_depth 12
arbitrary_correction_composition_checks 81924
arbitrary_front_dyadic_screening_checks 458748
arbitrary_rear_ternary_screening_checks 229374
dag_nodes 129
dag_dyadic_parent_projection_checks 1651
dag_ternary_parent_projection_checks 1270
dag_front_screening_checks 1560
dag_rear_screening_checks 1191
materialized_nodes 45
materialized_total_bits 457063
materialized_projection_checks 1035
threshold_x27 29252603
threshold_x39 188068289531
threshold_x74 4697939311072332635131
threshold_x75 23587405242550913489915
threshold_y24 181784647214
threshold_y28 2158791402581
collision_case (27, 28) boundary (120, 1) interface (117, 1) full (117, 1)
collision_case (39, 28) boundary (120, 1) interface (117, 1) full (117, 1)
collision_case (74, 28) boundary (118, 1) interface (117, 1) full (117, 1)
status EXACT two-sided boundary screening CLOSED; boundary-only quotient REJECTED; scale-aware interior decoder OPEN
```
