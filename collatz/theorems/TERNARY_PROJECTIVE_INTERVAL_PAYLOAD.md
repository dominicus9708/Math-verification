# Ternary projective interval payload quotient

Status: **EXACT / CLOSED at one fixed one-dimensional projective gate**

## Statement

Let a fixed surviving projective gate be written in a displacement coordinate `d` for which the already-certified projective carry map is a 3-adic isometry.

Let the admissible displacement family be a finite consecutive interval

\[
I=[L,U]\cap\mathbb Z,
\qquad N=U-L+1.
\]

For remaining ternary precision `k`, define

\[
\Pi^{(3)}_k(I)=\bigl(N,\;L\bmod 3^k\bigr).
\]

Because the projective displacement map is an isometry, an outgoing carry-cylinder condition modulo `3^ell`, with `ell <= k`, has a unique pullback

\[
d\equiv \rho\pmod{3^\ell}.
\]

Writing

\[
d=\rho+3^\ell n
\]

turns the surviving family into one consecutive integer `n` interval.

If two parent displacement intervals have the same `Pi3_k` state, then every common carry-cylinder pullback of precision `ell <= k` has exactly the same:

- emptiness/non-emptiness;
- cardinality;
- child payload state `Pi3_(k-ell)`.

Hence `Pi3_k` is an exact finite-horizon right-congruence for carry-cylinder queries inside one fixed one-dimensional projective displacement family.

## Proof kernel

If

\[
I' = I+t3^k,
\]

then equal payload states differ only by such a translation. Under

\[
d=\rho+3^\ell n,
\]

the child interval translates by

\[
t3^{k-\ell}.
\]

Therefore its cardinality and lower endpoint modulo `3^(k-ell)` are unchanged.

The projective displacement isometry supplies the unique residue `rho` corresponding to the requested outgoing carry cylinder.

## DSD role separation

**Observation coordinate:** outgoing projective carry cylinder modulo a requested ternary precision.

**Formation coordinate:** finite legal displacement interval.

**Quotient payload:** `(cardinality, lower endpoint mod 3^k)`.

The quotient forgets absolute displacement translation only to the extent that no future predicate through the remaining `k` ternary digits can distinguish it.

## Scope restriction

This theorem does **not** collapse the entire multi-gate right-H problem to one interval payload.

At later ranked-one gates new displacement variables and strict ordering constraints appear. Those coordinates must be added explicitly or discharged by another exact theorem.

Therefore the valid implication is

\[
\text{one fixed projective gate}
\to
\text{carry cylinder}
\to
\text{one displacement residue}
\to
\Pi^{(3)}_k\text{ interval quotient},
\]

not

\[
\Pi^{(3)}_k\Rightarrow\text{full right-H membership state}.
\]

## Certificate

- `../src/A0_s1_routeB_ternary_projective_interval_payload_certificate.py`

The finite regression in that certificate is an implementation guard only; the theorem is the exact residue-pullback/translation identity above.
