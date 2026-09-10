# MATH-049 — complete depth-39 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-39 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-048

MATH-048 leaves exactly

\[
1,586,644,081
\]

nested coefficient+Hensel survivors at depth 38. At depth 39,

\[
q_{\min}(39)=25.
\]

Thus depth-38 q=24 survivors may produce only their odd child, while every q>=25 survivor may produce both children. The exact depth-39 pre-Hensel population is

\[
\boxed{2,964,038,401}.
\]

## 2. Exact computation

The terminal class-max reduction from MATH-045 remains in force. For each fixed final q, every arbitrary length-39 parity word is assigned to

\[
(q,r),\qquad r=C\bmod 3^q.
\]

The computation stores, per exact residue class, only

\[
\max C_{\rm arbitrary},\qquad \max C_{\rm coefficient}.
\]

A coefficient-valid class survives exactly when these maxima agree. Coefficient admissibility remains an all-prefix condition.

For the central layers, the last BT odd positions determine `C mod 3^BT`; therefore exact classes can be partitioned into disjoint tail-residue buckets. q=25 used BT=12 (`3^12=531441` buckets); q=26 and q=27 used BT=11 (`3^11=177147` buckets); q>=28 used BT=10 where practical. Bucket ranges are disjoint and their sums are mathematically identical to one monolithic exact audit.

The depth-38 q=30 canonical survivor count `20,801,602` was reproduced before the depth-39 extension.

## 3. Complete depth-39 result

The canonical ledger is

`collatz/results/2026-09-10-depth39-complete-one-sided-hensel.tsv`.

Central layers:

- q=25: `667,265,465 -> 666,424,520`, newly removed `840,945`;
- q=26: `881,450,585 -> 881,128,353`, newly removed `322,232`;
- q=27: `693,820,404 -> 693,728,857`, newly removed `91,547`;
- q=28: `408,501,648 -> 408,477,182`, newly removed `24,466`;
- q=29: `196,622,885 -> 196,616,403`, newly removed `6,482`.

The remaining q>=30 tail removes another `2,173` states.

Hence

\[
\boxed{2,964,038,401\to2,962,750,556},
\]

and the exact number newly removed at depth 39 is

\[
\boxed{1,287,845}.
\]

The all-prefix coefficient language at depth 39 contains

\[
\boxed{3,611,535,862}
\]

words. Therefore cumulative Hensel removal through depth 39 is

\[
\boxed{648,785,306}.
\]

These are finite prefix-language counts, not a Collatz proof.

## 4. Independent arithmetic checks

- q=25 unrestricted bucket sum: `15,084,504,396 = C(39,14)`.
- q=26 unrestricted bucket sum: `8,122,425,444 = C(39,13)`.
- q=27 unrestricted bucket sum: `3,910,797,436 = C(39,12)`.
- q=28 unrestricted bucket sum: `1,676,056,044 = C(39,11)`.
- q=25 coefficient-valid sum: `820,236,724`, matching an independent coefficient-language DP.
- q=26 coefficient-valid sum: `1,079,237,954`, matching the same DP.
- q=27 coefficient-valid sum: `844,843,276`, matching the same DP.
- q=28 coefficient-valid sum: `493,966,536`, matching the same DP.
- all q-layer prefilters sum to `2,964,038,401`.
- all q-layer survivors sum to `2,962,750,556`.
- layerwise removals sum to `1,287,845`.

Candidate collision excesses were `2523` at q=25, `947` at q=26, and `46` at q=27. These are same-residue candidate multiplicities; exact class maxima, not candidate counts, determine survival.

## 5. DSD audit consequence

The calculation preserves the separation among:

1. all-prefix coefficient language;
2. children of the previous nested survivor language (pre-Hensel population);
3. current terminal exact class-max selection.

Tail-residue partitioning changes only execution granularity. It does not merge distinct exact Hensel classes or weaken the comparison predicate.

## 6. Reproducibility

- certificate: `collatz/src/2026_09_10_depth39_tailhash_range_certificate.cpp`
- ledger: `collatz/results/2026-09-10-depth39-complete-one-sided-hensel.tsv`

Representative central executions use disjoint `[b0,b1)` ranges and then sum the printed statistics. q=25 uses BT=12; q=26 and q=27 use BT=11.

## 7. Next target

At depth 40,

\[
q_{\min}(40)=26.
\]

Therefore depth-39 q=25 survivors have only an odd child, while q>=26 survivors have both children. Using the MATH-049 q-layer survivors, the next exact pre-Hensel population is to be derived before MATH-050 execution.

## 8. Prohibited upgrades

- finite depth-39 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- bucket partition => approximate residue equivalence — **PROHIBITED**;
- coefficient-valid class maximum => previous nested-survivor count without terminal maximality — **PROHIBITED**;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**.
