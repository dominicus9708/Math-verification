# Safe m=44 cross-place extension: Q=7, B=20

Date: 2026-08-25

Status: **exact finite root-safe extension of the cross-place cylinder sieve.** This is not a proof of Collatz.

## 1. Baseline

The independently audited `Q=6, BMAX=20, KMAX=36` certificate leaves

\[
1,204,234,610,789
\]

of the exact `2^44` ternary-selector starts.

The next test raises only the low ternary resolution from `Q=6` to `Q=7`, keeping `BMAX=20` and `KMAX=36` fixed.

## 2. Exact partitioned computation

A single Q=7 run exceeded the current execution window, so the 128 low-ternary masks were split into eight disjoint blocks of 16 masks each.

Each block has exact mass

\[
16\cdot2^{44-7}=2^{41}=2,199,023,255,552.
\]

The exact block totals were:

| low masks | forward-labelled | reverse-labelled | surviving |
|---|---:|---:|---:|
| 0--15 | 1,780,633,258,994 | 273,963,250,738 | 144,426,745,820 |
| 16--31 | 1,780,633,210,365 | 273,963,460,484 | 144,426,584,703 |
| 32--47 | 1,780,632,894,377 | 273,963,704,793 | 144,426,656,382 |
| 48--63 | 1,780,633,361,923 | 273,963,318,142 | 144,426,575,487 |
| 64--79 | 1,780,633,172,122 | 273,963,593,031 | 144,426,490,399 |
| 80--95 | 1,780,632,810,254 | 273,963,693,844 | 144,426,751,454 |
| 96--111 | 1,780,633,332,476 | 273,963,440,360 | 144,426,482,716 |
| 112--127 | 1,780,633,225,887 | 273,963,484,879 | 144,426,544,786 |

Every row sums exactly to `2^41`.

Summing the eight disjoint blocks gives

\[
\boxed{
\begin{aligned}
\text{forward-labelled}&=14,245,065,266,398,\\
\text{reverse-labelled}&=2,191,707,946,271,\\
\text{surviving}&=1,155,412,831,747.
\end{aligned}}
\]

and the grand total is exactly

\[
17,592,186,044,416=2^{44}.
\]

## 3. Improvement over Q=6

Relative to the `Q=6, B=20` survivor count,

\[
1,204,234,610,789-1,155,412,831,747
=\boxed{48,821,779,042}
\]

additional starts are safely excluded.

This is approximately

\[
\boxed{4.054175\%}
\]

of the Q=6/B=20 survivors.

The surviving fraction of the complete 44-selector core is now

\[
\boxed{0.06567761555\ldots},
\]

so the safe excluded fraction is

\[
\boxed{0.93432238445\ldots}
\]

or about `93.43224%`.

## 4. Why the reason labels need not be monotone

The forward-labelled count is slightly smaller at Q=7 than at Q=6 even though the total survivor set shrinks.

This is not a loss of forward certificates. The implementation scans increasing binary depths and stops at the first valid reason. A newly available Q=7 reverse witness may therefore claim a class at an earlier depth that would otherwise have been labelled by a later forward descent.

Accordingly, `forward-labelled` and `reverse-labelled` are bookkeeping partitions of the excluded set; the invariant quantity for comparing sieve strength is the final survivor count.

## 5. Audit status

The Q=7 calculation used the same independent overflow-safe C++ implementation that first reproduced the original Python Q=6/B=18 regression exactly and then produced the certified Q=6/B=20 extension.

The Q=7 run was partitioned solely for execution time. The mathematical partition is exact and disjoint, and every block independently conserved its full selector mass.

The result supports continuing the main line in two dimensions:

- binary depth `B` adds new forward and reverse opportunities;
- ternary resolution `Q` also adds genuinely new reverse certificates.

The next efficiency question is whether increasing Q again is cheaper and more productive than increasing B beyond 20.
