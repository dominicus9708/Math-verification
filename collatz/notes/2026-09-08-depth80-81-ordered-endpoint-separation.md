# MATH-020 — ordered internal-boundary endpoint separation through depths 80–81

Date: 2026-09-08

Status: `CONFIRMED / FINITE EXACT / ORDERED-SEPARATION PERSISTS THROUGH DEPTH 81`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## 1. Why depths 80 and 81 are the next useful check

MATH-019 showed that at depth 79 the zero-collision mechanism is not final odd-count mismatch.  Instead, every common `(boundary,Q)` cell satisfies the strict order

\[
\max E_L<\min E_R.
\]

The next DSD question is whether this is a one-depth accident or a persistent transition pattern.

For depths 80 and 81,

\[
80-q_{\min}(80)=29,
\]

\[
81-q_{\min}(81)=29.
\]

Therefore the same complete `m=29` local halo used at depth 79 can be reused.  No new outer shell enters before depth 82.

Local state counts remain

\[
963,422\text{ left},
\qquad
964,227\text{ right}.
\]

Only the tail descriptor resolution changes from `2^18` to `2^19` and `2^20`.

## 2. Exact normalized endpoint comparison

At depth `K=61+L`, define

\[
Z_K=2^L E_K-a3^Q.
\]

For adjacent block labels `a` and `a+1`, common-final-`Q` endpoint equality remains exactly

\[
Z_{K,L}-Z_{K,R}=3^Q.
\]

Thus for each boundary and common final `Q`, it is sufficient to compare

\[
Z_L^{\max}
\quad\text{with}\quad
Z_R^{\min}+3^Q.
\]

The range generator enumerates the complete `m=29` local state sets, applies the exact tail coefficient-survival descriptor, and emits normalized min/max ranges.  A separate small post-audit checks all cells and expected summary constants.

## 3. Depth 80

There are exactly

\[
\boxed{4,993}
\]

common `(boundary,Q)` cells.

Common-Q counts per boundary:

| common Q values | boundaries |
|---:|---:|
|14|114|
|15|203|
|16|22|

Every cell satisfies

\[
\boxed{
Z_L^{\max}<Z_R^{\min}+3^Q
}
\]

and hence

\[
\boxed{
\max E_L<\min E_R.
}
\]

The minimum normalized-numerator gap is

\[
656,932,864
=1253\cdot2^{19}.
\]

Therefore the minimum same-`Q` endpoint separation at depth 80 is

\[
\boxed{1253}.
\]

It occurs at boundary `1275`, final `Q=51`.

## 4. Depth 81

There are exactly

\[
\boxed{4,899}
\]

common `(boundary,Q)` cells.

Common-Q counts per boundary:

| common Q values | boundaries |
|---:|---:|
|13|6|
|14|179|
|15|149|
|16|5|

Again every cell satisfies

\[
\boxed{
Z_L^{\max}<Z_R^{\min}+3^Q
}
\]

and therefore

\[
\boxed{
\max E_L<\min E_R.
}
\]

The minimum numerator gap is

\[
1,971,322,880
=1880\cdot2^{20}.
\]

Hence the minimum same-`Q` endpoint separation is

\[
\boxed{1880}.
\]

It occurs at boundary `1073`, final `Q=52`.

## 5. Current finite separation sequence

The audited minima are now

\[
\boxed{
\Delta_{79}^{\min}=837,
\qquad
\Delta_{80}^{\min}=1253,
\qquad
\Delta_{81}^{\min}=1880.
}
\]

The minimum does not shrink toward zero over these three depths.  More importantly, the **sign is uniform** in every common-Q cell at every audited depth:

\[
\boxed{E_L<E_R.}
\]

This is stronger diagnostic information than repeated `collision=0` statements.

## 6. DSD route decision

This three-depth persistence changes the preferred next calculation.

Continuing brute-force depth extension is no longer the highest-value move.  The next structural target is the transition of the separation envelope itself.

Define

\[
\Delta_k(b,Q)
=
\min E_R(k;b,Q)-\max E_L(k;b,Q).
\]

For `k=79,80,81`, every defined cell has

\[
\Delta_k(b,Q)>0.
\]

The next task is to determine which additional endpoint-residue descriptor is sufficient to propagate a positive lower bound on `Delta` from depth `k` to `k+1` without re-enumerating the full ordinary-start state set.

Because one shortcut step depends on endpoint parity, a scalar interval alone is not a complete recursive state.  A residue-refined interval descriptor is required.  The DSD rule is therefore:

- do not assert monotonicity from the three finite depths;
- do not keep increasing depth blindly;
- search for the smallest exact residue-refined envelope that makes the ordered-separation transition closed.

Depth 82 also introduces a new `m=30` halo shell, so any recursion must distinguish:

1. propagation of the existing `m=29` core;
2. injection of the new shell.

## 7. Prohibited upgrades

- ordered separation at depths 79–81 does not imply arbitrary-depth separation;
- the sequence `837,1253,1880` is not an asymptotic law;
- candidate-set endpoint order is not global monotonicity of the Collatz map;
- internal-boundary exclusion through depth 81 does not close the first universal cell.

## Reproducibility

Range generator:

`collatz/src/2026_09_08_depth80_81_normalized_range_generator.cpp`

Commit:

`f9763f3e54290a76ed371b70d1f0e4d79de3a542`

Post-audit:

`collatz/src/2026_09_08_depth80_81_normalized_range_postaudit.py`

Commit:

`05b72fab5151ae37787aa4002608c838d82c49c8`

The four exact range runs (`left/right × depth80/81`) were separately completed and the post-audit summary was independently reproduced in-session before this note was recorded.
