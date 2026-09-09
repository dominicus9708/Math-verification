# MATH-048 — complete depth-38 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-38 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-047

MATH-047 leaves

\[
793{,}742{,}593
\]

nested coefficient+Hensel survivors at depth 37.

At depth 38,

\[
q_{\min}(38)=24.
\]

Every depth-37 survivor already has `q>=24`, so both children remain coefficient-admissible at the new terminal depth. Hence the exact depth-38 pre-Hensel population is

\[
\boxed{2\cdot793{,}742{,}593=1{,}587{,}485{,}186}.
\]

The q-layer prefilter is obtained exactly from

\[
P_{38}(q)=S_{37}(q)+S_{37}(q-1).
\]

## 2. Exact terminal reduction retained

MATH-045 proved that if a prefix is non-maximal in its exact root-Hensel class

\[
(q,C\bmod3^q),
\]

then appending a common suffix preserves the class relation and strict correction ordering. Therefore, for a fixed full word,

\[
\boxed{\text{terminal exact class-max}\iff\text{class-max at every Hensel prefix}.}
\]

Coefficient admissibility remains an all-prefix condition and is not replaced by this reduction.

The depth-38 engine was regression-checked against the canonical MATH-047 depth-37 q=30 result and reproduced

\[
4{,}936{,}909
\]

survivors exactly before any depth-38 value was accepted.

## 3. Tail-residue flat-hash partition

For fixed `(K,Q)` choose `BT` final odd positions. Writing the correction as

\[
C=3^{BT}C_{\rm early}+C_{\rm tail},
\]

gives

\[
C\bmod3^{BT}=C_{\rm tail}\bmod3^{BT}.
\]

Thus every exact Hensel class belongs to exactly one tail-residue bucket. Inside each bucket the implementation stores only

- maximum arbitrary correction `C` for each exact residue `C mod 3^Q`;
- maximum coefficient-valid correction for that same exact residue.

A candidate class survives exactly when these two maxima are equal.

This is an exact partition, not a probabilistic hash approximation. Hash collisions are resolved by exact key equality.

Central settings:

- q=25,26: `BT=10`, `3^10=59,049` buckets, processed in disjoint ranges;
- q=24: `BT=11`, `3^11=177,147` buckets, processed in 18 disjoint ranges;
- smaller layers used fewer tail digits where sufficient.

## 4. Complete depth-38 result

Canonical ledger:

`collatz/results/2026-09-10-depth38-complete-one-sided-hensel.tsv`

Key central layers:

\[
q=24:\quad209{,}704{,}242\to209{,}249{,}761,
\]

newly removed `454,481`;

\[
q=25:\quad458{,}291{,}343\to458{,}015{,}704,
\]

newly removed `275,639`;

\[
q=26:\quad423{,}515{,}692\to423{,}434{,}881,
\]

newly removed `80,811`;

\[
q=27:\quad270{,}407{,}638\to270{,}385{,}523,
\]

newly removed `22,115`.

All layers combined give

\[
\boxed{1{,}587{,}485{,}186\to1{,}586{,}644{,}081}.
\]

Therefore the exact number newly removed at depth 38 is

\[
\boxed{841{,}105}.
\]

The full all-prefix coefficient language at depth 38 contains

\[
\boxed{1{,}934{,}757{,}182}
\]

words, exactly twice the depth-37 coefficient-language count because `q_min` stays 24 from depth 37 to 38. Hence cumulative Hensel removal through depth 38 is

\[
\boxed{348{,}113{,}101}.
\]

## 5. Independent arithmetic checks

- q=24 unrestricted range sum:

\[
\boxed{9{,}669{,}554{,}100}=\binom{38}{14}.
\]

- q=25 unrestricted range sum:

\[
\boxed{5{,}414{,}950{,}296}=\binom{38}{13}.
\]

- q=26 unrestricted range sum:

\[
\boxed{2{,}707{,}475{,}148}=\binom{38}{12}.
\]

- all q-layer prefilters sum to `1,587,485,186`;
- all q-layer survivors sum to `1,586,644,081`;
- all q-layer removals sum to `841,105`;
- coefficient-language total is `1,934,757,182`;
- `1,934,757,182 - 1,586,644,081 = 348,113,101`.

Candidate-class collision excesses were `267` at q=24, `641` at q=25, and `41` at q=26. These are exact same-residue candidate multiplicities and do not change the one-sided rule, because the comparison uses the maximum correction in the unrestricted class.

## 6. DSD audit consequence

The calculation again keeps three layers distinct:

1. all-prefix coefficient language;
2. nested children of the previous depth's full survivors;
3. current terminal exact class-max selection.

The tail-residue descriptor is used only as an exact computational partition. It is not promoted to a full Collatz state descriptor, and different buckets/classes are not asserted dynamically independent beyond this fixed class-max calculation.

## 7. Reproducibility

Certificate:

`collatz/src/2026_09_10_depth38_tailhash_range_certificate.cpp`

Canonical ledger:

`collatz/results/2026-09-10-depth38-complete-one-sided-hensel.tsv`

## 8. Next target

At depth 39,

\[
q_{\min}(39)=25.
\]

Therefore the depth-38 q=24 survivors have only odd coefficient-admissible children, while every q>=25 survivor has both children. The exact MATH-049 pre-Hensel population is

\[
2\cdot1{,}586{,}644{,}081-209{,}249{,}761
=\boxed{2{,}964{,}038{,}401}.
\]

The next calculation should reuse the terminal class-max reduction and tail-residue flat-hash partition, with the threshold rise at depth 39 explicitly reflected in the nested prefilter.

## 9. Prohibited upgrades

- finite depth-38 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- terminal Hensel reduction => coefficient-prefix reduction — **PROHIBITED**;
- tail-residue partition => full-state equivalence — **PROHIBITED**;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**;
- growth of prefix survivor counts => growth of ordinary-integer counterexamples — **PROHIBITED**.
