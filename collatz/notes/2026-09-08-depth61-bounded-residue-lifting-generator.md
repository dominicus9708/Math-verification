# MATH-027 — bounded depth-61 residue-lifting generator

## Status

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`
- result: `CONFIRMED / EXACT BOUNDED GENERATOR / STAGE-1 ACCELERATION`

## 1. Problem

MATH-024 and MATH-026 filter every right offset

\[
0\le r\le R_{\max}
\]

independently through depth 61 before later continuation.

That is exact but repeats many identical binary-prefix calculations.

## 2. Exact binary lift

Suppose a lower-bit prefix satisfies

\[
x<2^k,
\qquad T^k(x)=y,
\qquad q=q_k(x).
\]

For the next binary digit `e in {0,1}`, define

\[
x'=x+e2^k.
\]

The first `k` parity decisions remain the same, and the affine slope of the shortcut prefix is `3^q/2^k`. Therefore

\[
\boxed{
T^k(x')=y+e3^q
}.
\]

The next parity bit is exactly the parity of this lifted endpoint.

After applying that next shortcut step, the new exact state

\[
(x',T^{k+1}(x'),q_{k+1}(x'))
\]

is retained only if the depth-`k+1` coefficient threshold survives.

Any branch with

\[
x'>R_{\max}
\]

is never created.

## 3. Why this is not a coarse FSM

The state stores the exact ordinary prefix `x`, exact endpoint `y`, and exact odd count `q`.

No two states are merged merely because they share a residue or parity summary.

Thus this generator is a reordering of exact enumeration, not an aliasing quotient.

## 4. Independent full-vector regression

Two finite domains were audited against an independent scalar scan:

\[
R_{\max}=10^8,\qquad2\cdot10^8.
\]

The comparison is not only by count. The complete sorted vectors

\[
(r,T^{61}(r),q_{61})
\]

are required to agree element-by-element.

They do.

### `RMAX = 100,000,000`

- final survivors: `179,754`
- first: `703`
- last: `99,999,855`
- scalar shortcut-prefix steps: `345,676,746`
- residue-lift branch attempts: `23,802,595`
- peak live lift states: `1,312,797` at depth 27

### `RMAX = 200,000,000`

- final survivors: `358,907`
- first: `703`
- last: `199,999,983`
- scalar shortcut-prefix steps: `691,370,987`
- residue-lift branch attempts: `44,150,751`
- peak live lift states: `2,625,819` at depth 28

At `2e8`, the elementary stage-1 transition count is reduced by

\[
\frac{691,370,987}{44,150,751}\approx15.66.
\]

This factor refers only to the audited stage-1 prefix-transition layer.

## 5. Role in the proof architecture

MATH-025 accelerates depth-61+ continuation in 11-step windows.

MATH-027 now accelerates the complementary **depth-0 to depth-61 candidate generation** layer.

The next finite bootstrap can therefore use:

\[
\text{exact bounded residue lifting}
\to
\text{exact address lift}
\to
\text{exact rolling 11-step continuation}.
\]

## 6. Prohibited upgrades

Do not infer:

- exact finite generator ⇒ universal finite-state proof;
- fewer branch attempts ⇒ fewer mathematical candidates beyond the stated coefficient gate;
- successful regression at `2e8` ⇒ arbitrary-bound completeness without the exact recurrence proof;
- stage-1 acceleration ⇒ first-cell emptiness;
- finite computation ⇒ Collatz proof.

## Reproduction

`collatz/src/2026_09_08_depth61_bounded_residue_lifting_generator_certificate.cpp`
