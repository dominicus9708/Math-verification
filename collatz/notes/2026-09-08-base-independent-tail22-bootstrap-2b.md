# MATH-035 — base-independent 22-step bootstrap through right offset 2e9

## Status

`CONFIRMED / FINITE ONLY / EXACT ACCELERATED BOOTSTRAP`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Finite domain

The audited right-offset domain is

\[
0\le r\le 2,000,000,000.
\]

For internal adjacent blocks,

\[
N=b2^{61}+r,
\qquad 1025\le b\le1363.
\]

The calculation uses the current exact DSD-native engine:

1. cut-10 bounded binary residue lifting through depth 61;
2. MATH-031 cyclic 22-step address prefilter through depth 83;
3. MATH-033 base-independent 22-step critical-prefix threshold thereafter;
4. two exact audited 11-step affine endpoint updates for each accepted 22-step block.

No truncated residue replaces the exact endpoint state.

## Exact depth-61 survivors

The domain contains

\[
\boxed{3,592,089}
\]

depth-61 coefficient-surviving right offsets.

First and last:

\[
\boxed{703},
\qquad
\boxed{1,999,999,935}.
\]

The exact `q61` histogram is:

| q61 | survivors |
|---:|---:|
| 39 | 771,761 |
| 40 | 987,601 |
| 41 | 794,250 |
| 42 | 514,554 |
| 43 | 285,599 |
| 44 | 140,125 |
| 45 | 61,616 |
| 46 | 24,051 |
| 47 | 8,723 |
| 48 | 2,770 |
| 49 | 745 |
| 50 | 231 |
| 51 | 54 |
| 52 | 8 |
| 53 | 1 |

The appearance of one `q61=53` survivor is an implementation-boundary warning: future code must not freeze the `q61` range at `39..52` merely because that was sufficient for `RMAX=10^9`.

## Address prefilter and rolling continuation

After the exact 22-step cyclic address prefilter, the number of exact depth-83 address states is

\[
\boxed{379,544,924}.
\]

The base-83+ continuation performs

\[
\boxed{588,381,926}
\]

base-independent 22-step threshold gates.

The final audited results are

\[
\boxed{\text{survive to audited end}=0},
\]

\[
\boxed{\text{fixed-width endpoint overflow}=0}.
\]

The deepest failing 22-step base is still

\[
\boxed{545},
\]

with first witness

\[
\boxed{r=378,620,799,\qquad b=1183}.
\]

Thus enlarging the finite right-offset domain from `10^9` to `2*10^9` does not produce a later audited survivor in this mechanism.

## Consequence via MATH-021 linear collision halo

MATH-021 established the necessary same-endpoint displacement condition

\[
r\le \left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Therefore `r<=2*10^9` contains every right offset relevant through

\[
\boxed{k\le6,000,000,003}.
\]

Hence, within the current universal-spine/coefficient-survival scope,

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le6,000,000,003.
}
\]

## DSD interpretation

This step validates the current calculation direction:

\[
\text{exact bounded lifting}
\to
\text{cyclic complete descriptor}
\to
\text{base-independent rolling gate}
\to
\text{finite exclusion}.
\]

It also exposes a representation rule for later expansions: range-dependent state support such as the observed `q61` maximum is data, not a permanent type bound.

## Prohibited upgrades

Do not infer:

- `r<=2e9` implies all halo offsets;
- depth `6,000,000,003` means ordinary Collatz verification to that depth;
- endpoint coupling exclusion means candidate emptiness;
- repeated deepest failure at 545 is a universal lifespan theorem;
- this finite calculation closes the first Farey cell or Collatz.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_base_independent_tail22_bootstrap_2b_certificate.cpp`
