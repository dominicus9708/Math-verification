# MATH-045 — complete depth-35 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-35 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-044

MATH-044 leaves exactly

\[
124{,}486{,}440
\]

nested coefficient+Hensel survivors at depth 34.

At depth 35,

\[
q_{\min}(35)=23.
\]

Hence a depth-34 state with q=22 may produce only its odd child, while every q>=23 state may produce both children. Using the exact MATH-044 q-layer counts gives the depth-35 pre-Hensel population

\[
\boxed{216{,}540{,}217}.
\]

## 2. Terminal class-max reduction

For a prefix correction

\[
C=h3^q+r,\qquad 0\le r<3^q,
\]

suppose another arbitrary prefix in the same exact class `(q,r)` has strictly larger correction. Appending the same parity suffix preserves the exact Hensel class relation and strict correction ordering: an even child preserves the correction difference and an odd child multiplies it by 3.

Therefore a non-maximal prefix can never regain maximality along a common suffix. Thus for a fixed full parity word,

\[
\boxed{\text{terminal exact class-max}\iff\text{root-Hensel class-max at every prefix}.}
\]

This equivalence applies only to root-Hensel maximality. Coefficient admissibility remains an all-prefix condition.

The reduction was regression-checked at depth 34 against MATH-044 for q=25,26,27 and reproduced all three canonical survivor counts exactly.

## 3. Central residue-bucket computation

The remaining heavy depth-35 layers were q=23,24,25.

For fixed q, every arbitrary length-35 parity word with q odd bits was enumerated. Each word was assigned to the exact Hensel key

\[
(q,r),\qquad r=C\bmod3^q.
\]

The residue space was divided into disjoint buckets by an interval map. A complete Hensel class belongs to exactly one bucket, so no class can cross a bucket boundary. Consequently the sum of the per-bucket class-max audits is exactly equal to a monolithic global audit.

The q=25 layer used 32 buckets and enumerated

\[
\binom{35}{10}=183{,}579{,}396
\]

arbitrary words.

The q=24 layer used 64 buckets and enumerated

\[
\binom{35}{11}=417{,}225{,}900
\]

arbitrary words.

The q=23 layer used 128 buckets. To keep each generation step bounded, it was additionally split by the first two parity bits into four disjoint prefix shards. Their exact populations were

\[
92{,}561{,}040,
193{,}536{,}720,
193{,}536{,}720,
354{,}817{,}320,
\]

which sum to

\[
\boxed{834{,}451{,}800}=\binom{35}{12}.
\]

The first three prefix shards contain no coefficient-valid candidates but remain in the unrestricted competitor language, as required by the one-sided selection rule.

## 4. Exact depth-35 result

The complete q-layer table is stored in

`collatz/results/2026-09-09-depth35-complete-one-sided-hensel.tsv`.

The three newly completed central layers are

\[
q=23:\quad71{,}570{,}859\to71{,}519{,}838,
\]

newly removed `51,021`;

\[
q=24:\quad67{,}080{,}250\to67{,}064{,}833,
\]

newly removed `15,417`;

\[
q=25:\quad43{,}090{,}675\to43{,}086{,}073,
\]

newly removed `4,602`.

Combining these with the already certified q>=26 tail gives

\[
\boxed{216{,}540{,}217\to216{,}467{,}460}.
\]

Thus the exact number newly removed by the depth-35 Hensel step is

\[
\boxed{72{,}757}.
\]

The full all-prefix coefficient language at depth 35 contains

\[
\boxed{263{,}841{,}377}
\]

words. Hence cumulative Hensel removal through depth 35 is

\[
\boxed{47{,}373{,}917}.
\]

These are prefix-language counts, not a proof of Collatz and not a terminal first-cell counterexample count.

## 5. Independent arithmetic checks

- q=23 four-shard population sum equals exactly `C(35,12)=834,451,800`.
- The 128 q=23 bucket populations sum back to exactly `834,451,800`.
- The 13 final-q prefilter layers sum to exactly `216,540,217`.
- The 13 survivor layers sum to exactly `216,467,460`.
- The layerwise removal sum is exactly `72,757`, equal to prefilter minus survivors.
- The coefficient-language q-distribution sums to exactly `263,841,377`.

At q=23, the unrestricted exact-class computation found `448,679,415` distinct Hensel classes. Twenty excess coefficient-candidate collisions occur inside candidate classes; this does not alter the one-sided rule because arbitrary competitors, not only candidate competitors, determine the class maximum.

## 6. DSD audit consequence

The depth-35 calculation confirms three distinct levels that must not be conflated:

1. **coefficient language** — all-prefix coefficient admissibility;
2. **nested prefilter** — children of the previous depth's coefficient+Hensel survivors;
3. **terminal exact class-max** — the current depth's one-sided root-Hensel selection.

The terminal reduction removes redundant historical Hensel-prefix recomputation, while the residue-bucket partition removes the memory bottleneck without losing exact class information.

The central computation also confirms that the unrestricted competitor language must remain larger than the candidate language. In particular, q=23 has three large prefix shards with zero coefficient-valid candidates that still contribute valid competitors.

## 7. Reproducibility

Central bucket/shard certificate:

`collatz/src/2026_09_09_depth35_central_residue_bucket_terminal_classmax_certificate.cpp`

High-q certificate:

`collatz/src/2026_09_09_depth35_highq_d7_one_sided_hensel_certificate.cpp`

q=26,27 terminal certificate:

`collatz/src/2026_09_09_fixed_q_terminal_classmax_certificate.cpp`

Canonical result ledger:

`collatz/results/2026-09-09-depth35-complete-one-sided-hensel.tsv`

## 8. Next target

Since

\[
q_{\min}(36)=23,
\]

every depth-35 survivor has both coefficient-admissible children at depth 36. Therefore the exact depth-36 pre-Hensel population is already fixed as

\[
\boxed{2\cdot216{,}467{,}460=432{,}934{,}920}.
\]

The next computation should retain the terminal class-max reduction permanently and use external residue-bucket/shard processing from the start. Historical two-sided coefficient-Hensel depth-36 files must not be substituted for this one-sided nested continuation.

## 9. Prohibited upgrades

- finite depth-35 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- terminal Hensel reduction => coefficient-prefix reduction — **PROHIBITED**;
- bucket independence => independence of different Hensel classes or depths — **PROHIBITED**;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**;
- historical two-sided depth-36 collision results => one-sided MATH-046 result — **PROHIBITED**.
