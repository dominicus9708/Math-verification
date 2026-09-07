# MATH-032 — 22-step prefilter full-continuation regression

Date: 2026-09-08

Status:

`CONFIRMED / EXACT CONTINUATION ACCELERATION / FINITE ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Purpose

MATH-031 proved that the first 22 address-continuation steps can be represented by an exact `2^22` residue descriptor and a cyclic-window prefilter.  MATH-032 tests whether that prefilter can replace the first two 11-step rolling windows in the actual MATH-028 `RMAX=10^9` continuation without changing any finite mathematical output.

## Engine replacement

Legacy MATH-028 continuation starts at depth 61 and checks 11-step windows at bases

\[
61,72,83,94,\ldots.
\]

MATH-032 instead performs:

1. one exact 22-step cyclic-window prefilter at depth 61;
2. exact endpoint reconstruction only for states surviving through depth 83;
3. the audited 11-step rolling continuation from base depth 83 onward.

For a surviving local residue `u mod 2^22`,

\[
q_{83}=q_{61}+s_{22}(u)
\]

and

\[
T^{83}(N)=\frac{3^{s_{22}(u)}T^{61}(N)+c_{22}(u)}{2^{22}}.
\]

Thus no approximate or residue-only endpoint is propagated.

## Exact finite counts

The depth-61 right-offset survivor count remains

\[
\boxed{1,796,718}.
\]

Raw internal address states:

\[
1,796,718\cdot339
=\boxed{609,087,402}.
\]

States surviving the first legacy 11-step address window:

\[
\boxed{333,913,383}.
\]

States surviving both first windows, equivalently surviving the exact 22-step prefilter through depth 83:

\[
\boxed{189,767,400}.
\]

Only these 189,767,400 states are instantiated as exact depth-83 endpoints.

## Full continuation regression

From depth 83 onward the exact 11-step rolling engine performs

\[
\boxed{467,202,551}
\]

window checks.

The final finite result exactly reproduces MATH-028:

- states surviving through the audited end: `0`;
- fixed-width endpoint overflow: `0`;
- deepest failing rolling-window base:

\[
\boxed{545};
\]

- first witness:

\[
\boxed{r=378,620,799,\qquad b=1183}.
\]

Therefore the inherited internal adjacent-block same-endpoint coupling exclusion remains

\[
\boxed{61\le k\le3,000,000,003}
\]

within the audited finite scope.

## Address-window operation reduction

The legacy 11-step engine would execute

\[
609,087,402
\]

individual address-window threshold checks at base 61 and

\[
333,913,383
\]

more at base 72.

Hence the first two windows alone require

\[
\boxed{943,000,785}
\]

per-address threshold checks.

Including the identical base-83-and-later work, the legacy finite continuation would perform

\[
609,087,402+333,913,383+467,202,551
=\boxed{1,410,203,336}
\]

address-level 11-step window checks.

MATH-032 replaces the first `943,000,785` per-address checks by one cyclic range query per depth-61 leaf plus exact endpoint instantiation only for the 189,767,400 depth-83 survivors.

This is a computational acceleration statement; the range-query construction and table precomputation have their own cost and the count is not a wall-clock speedup factor.

## DSD interpretation

The DSD calculation chain is now:

\[
\text{exact prefix state}
\to
\text{complete local descriptor}
\to
\text{cyclic aggregate gate}
\to
\text{exact surviving endpoints only}.
\]

The descriptor changes how a local predicate is evaluated, not the meaning of the underlying ordinary-integer state.

## Scope boundary

Do not infer:

- removal of 943,000,785 finite checks ⇒ equal wall-clock reduction;
- local 22-step completeness ⇒ arbitrary-depth completeness;
- finite `RMAX=10^9` regression ⇒ arbitrary right-offset domain;
- internal same-endpoint coupling exclusion ⇒ first-cell emptiness;
- any computational acceleration ⇒ Collatz proof.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_tail22_prefilter_full_continuation_regression.cpp`

Certificate commit:

`6944b085859df1740e12e535e4d8dbb54f1c212c`
