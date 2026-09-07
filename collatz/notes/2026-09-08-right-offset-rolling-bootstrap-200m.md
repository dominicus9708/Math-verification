# MATH-026 — rolling right-offset bootstrap through 2e8

## Status

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`
- result: `CONFIRMED / FINITE ONLY / ROLLING-OPERATOR ACCELERATED`
- internal adjacent-block same-endpoint coupling excluded through depth `600,000,003` in the audited scope

## 1. Purpose

MATH-024 extended the finite right-offset bootstrap to

\[
0\le r\le10^8
\]

using scalar shortcut continuation.

MATH-025 provides an exact 11-step rolling operator. MATH-026 uses that operator as the actual continuation engine and doubles the right-offset domain to

\[
\boxed{0\le r\le2\cdot10^8}.
\]

## 2. Stage 1 — exact depth-61 filter

For every integer `r` in the finite domain, the shortcut orbit of `r` is followed exactly through depth 61 and tested against the frozen coefficient-survival threshold.

The result is

\[
\boxed{358,907}
\]

depth-61 surviving right offsets.

The first and last are

\[
\boxed{703},
\qquad
\boxed{199,999,983}.
\]

## 3. Stage 2 — exact rolling continuation

For each surviving `r` and every internal right-side address label

\[
1025\le b\le1363,
\]

the exact depth-61 endpoint is

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}}.
\]

From there the computation advances in exact 11-step windows using MATH-025:

\[
u=n\bmod2048,
\]

\[
q\ge H_K(u)
\]

for survival of the entire next window, and when the window survives,

\[
q'=q+s(u),
\]

\[
n'=\frac{3^{s(u)}n+c(u)}{2^{11}}.
\]

The rolling audit is continued through depth

\[
K_{\rm end}=1029=61+88\cdot11.
\]

## 4. Exact output

Across all

\[
358,907\times339
\]

finite right-side states:

- states surviving every rolling window through depth 1029: **0**;
- deepest base depth of a failing 11-step window: **501**;
- all finite endpoint arithmetic remained within the explicitly guarded 128-bit range.

The `501` result means the longest audited states fail somewhere inside the window

\[
502,\dots,512.
\]

No state comes remotely close to the earliest possible collision-halo entry

\[
3(703)+1=2110.
\]

## 5. Collision-exclusion consequence

MATH-021 proves that a same-endpoint cross-boundary collision at depth `k` requires

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

For

\[
k\le3(2\cdot10^8)+3,
\]

this necessary right offset lies inside the exact MATH-026 domain.

Therefore

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le600,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

## 6. What MATH-025 changed computationally

This extension is not just a larger repetition of MATH-024.

After depth 61, an 11-step segment is no longer evaluated by eleven scalar shortcut transitions and eleven coefficient comparisons. It is evaluated by

1. `n mod 2048`;
2. one `H_K` comparison;
3. one exact affine update if the window survives.

Thus MATH-025 has moved from a validation result to the actual finite-search execution path.

## 7. Scope and prohibited upgrades

This result excludes one **internal adjacent-block same-endpoint coupling mechanism** over a finite depth range.

It does not prove:

- that all first-cell candidates are absent;
- that non-coupled candidates are absent;
- that the finite lifespan behavior persists for all offsets;
- that depth `600,000,003` is a Collatz verification limit;
- that the Collatz conjecture is solved.

The first universal cell and the Collatz conjecture remain `OPEN`.

## Reproduction

Certificate:

`collatz/src/2026_09_08_right_offset_rolling_bootstrap_200m_certificate.cpp`
