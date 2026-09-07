# MATH-028 — combined lifting + rolling bootstrap through 1e9

## Status

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`
- result: `CONFIRMED / FINITE ONLY / COMBINED EXACT ACCELERATION`
- audited internal adjacent-block same-endpoint coupling exclusion through depth `3,000,000,003`

## 1. Combined engine

MATH-027 accelerates the bounded right-offset generation from depth 0 to 61.

MATH-025 accelerates each exact depth-61+ continuation in 11-step windows.

MATH-028 combines them:

\[
\boxed{
\text{bounded residue lifting}
\to
\text{exact address lift}
\to
\text{rolling 11-step continuation}
}
\]

for

\[
\boxed{0\le r\le10^9}.
\]

## 2. Exact threshold construction

The final certificate constructs all coefficient thresholds with arbitrary-precision integers.

It directly checks the frozen theorem-facing predicate

\[
(3+2^{-71})^q>2^k
\]

against the simpler integer threshold used by the fast calculation throughout the continuation range.

An exploratory fixed-width threshold calculation was rejected during audit before this result was recorded. No value from that discarded run is used here.

## 3. Stage 1 — exact bounded lifting to depth 61

The exact MATH-027 generator gives

\[
\boxed{1,796,718}
\]

depth-61 surviving right offsets.

First and last:

\[
\boxed{703},
\qquad
\boxed{999,999,207}.
\]

Generator work statistics:

- exact binary-lift branch attempts: `187,063,991`;
- peak live prefix states: `11,894,128`;
- peak depth: `30`.

No coarse state quotient is used: each live prefix retains exact `(r,T^k(r),q_k)` information.

## 4. Stage 2 — all 339 internal boundaries

For each depth-61 survivor and every

\[
1025\le b\le1363,
\]

the exact address lift

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}}
\]

is followed by MATH-025 rolling continuation.

The audit window reaches depth 1029.

Exact output:

- states surviving all rolling windows through depth 1029: **0**;
- deepest failing-window base: **545**;
- lexicographically first witness at that base:
  \[
  \boxed{r=378,620,799,\quad b=1183}.
  \]

Therefore even the longest audited state loses coefficient survival somewhere in the 11-step window

\[
546,\dots,556.
\]

No arithmetic overflow occurs in the explicitly guarded 128-bit finite continuation.

## 5. Collision-exclusion consequence

MATH-021 gives the necessary condition

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor
\]

for an internal adjacent-block same-endpoint collision at depth `k`.

Hence every possible right offset relevant for

\[
k\le3\cdot10^9+3
\]

lies inside the MATH-028 finite domain.

Thus

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le3,000,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

## 6. Interpretation

The earlier finite frontier progressed as

\[
30,000,003
\to300,000,003
\to600,000,003
\to3,000,000,003.
\]

The latest jump is enabled by using exact calculation descriptors on both sides of depth 61 rather than by weakening the candidate predicate.

The maximum relevant first-cell displacement is still much larger, so this does not close the first cell.

## 7. Prohibited upgrades

Do not infer:

- `r<=1e9` ⇒ all endpoint-halo offsets;
- depth `3,000,000,003` ⇒ general Collatz verification to that depth;
- no internal same-endpoint coupling ⇒ no candidate;
- finite longest failing window ⇒ universal lifespan bound;
- computational acceleration ⇒ Collatz proof.

The first universal cell and Collatz conjecture remain `OPEN`.

## Reproduction

`collatz/src/2026_09_08_combined_lifting_rolling_bootstrap_1b_certificate.cpp`
