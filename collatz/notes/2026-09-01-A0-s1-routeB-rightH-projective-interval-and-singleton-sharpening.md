# A0 s=1 Route-B — right-H projective interval quotient and singleton sharpening

Date: 2026-09-01

## Purpose

Continue G2 without flat enumeration of the right-H carry residue family.

Two exact pieces are added.

## 1. Ternary projective interval payload

At one fixed projective gate, the displacement isometry converts a requested outgoing carry cylinder modulo `3^ell` into one exact displacement residue

\[
d\equiv\rho\pmod{3^\ell}.
\]

For a finite displacement interval `I=[L,U]` and remaining precision `k`, define

\[
\Pi^{(3)}_k(I)=(|I|,L\bmod3^k).
\]

Equal payloads have equal emptiness/cardinality and equal child payload after every common residue pullback through precision `ell<=k`.

This closes the one-dimensional projective interval-family quotient.

It does not close the multi-gate right-H filter, because later ranks introduce new displacement variables and ordering constraints.

Certificate:

- `../src/A0_s1_routeB_ternary_projective_interval_payload_certificate.py`

Regression guard only:

- 912,900 equivalent interval/cylinder pullback checks;
- 6,375 exact residue partition checks.

## 2. Right-H singleton threshold sharpening

For any length-h, q-one binary block, right-indexed target capacity obeys

\[
D_t\le h-q.
\]

For the current right H block,

\[
h_R=630,138,897,\qquad q_R=397,573,380,
\]

hence

\[
D_t\le232,565,517.
\]

The projective slack-cylinder period is

\[
\lambda_m=2\cdot3^{m-1}.
\]

Since

\[
\lambda_{17}=86,093,442\le232,565,517
\]

but

\[
\lambda_{18}=258,280,326>232,565,517,
\]

we obtain the exact current-block sharpening

\[
\boxed{m\ge18\Longrightarrow\text{every prescribed right-H projective slack cylinder is empty or singleton}.}
\]

This replaces the older generic `m>=23` bound for this right block.

Thus prescribed-cylinder high-precision ranges are at least:

- terminal L=24: 7 gates;
- terminal L=28: 11 gates;
- terminal L=47: 30 gates.

Certificate:

- `../src/A0_s1_routeB_rightH_projective_singleton_threshold_certificate.py`

## DSD audit

### EXACT / CLOSED

- one fixed projective carry cylinder -> one displacement residue class;
- finite displacement interval payload `Pi3_k` is an exact finite-horizon quotient for those cylinder queries;
- universal capacity `D_t<=h-q`;
- current right-H prescribed-cylinder singleton threshold `m>=18`.

### REGRESSION ONLY

- all finite enumeration counts in the interval-payload and singleton-threshold certificates.

### SAFE INTERPRETATION

The high-precision range is non-branching **inside each prescribed cylinder**.

### REJECTED INFERENCE

Do not infer

`prescribed cylinder singleton => unique carry path`.

Distinct prescribed outgoing carry/cylinder states may still coexist.

### OPEN

The next G2 object is the exact multi-gate symbolic carry-family state combining:

- projective cylinder family;
- `Pi3_k` interval payload;
- max-slack formation label `S_max`;
- new displacement/order coordinate when a new rank is introduced.

The objective is to traverse the 7/11/30 high-precision singleton ranges without raw carry enumeration and export an exact state at `m=17`.

No 14-root family is closed by this note. Route-B and the Collatz conjecture remain open.
