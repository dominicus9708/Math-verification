# MATH-050 — complete depth-40 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-40 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-049

MATH-049 leaves exactly

\[
2,962,750,556
\]

nested coefficient+Hensel survivors at depth 39. At depth 40,

\[
q_{\min}(40)=26.
\]

Therefore depth-39 q=25 survivors have only an odd child, while q>=26 survivors have both children. The exact depth-40 pre-Hensel population is

\[
\boxed{5,259,076,592}.
\]

## 2. Exact computation

The terminal class-max reduction from MATH-045 remains in force. For fixed final q, every arbitrary length-40 parity word is assigned to

\[
(q,r),\qquad r=C\bmod 3^q.
\]

For each exact residue class the computation stores only

\[
\max C_{\rm arbitrary},\qquad \max C_{\rm coefficient}.
\]

A coefficient-valid class survives exactly when these maxima agree. Coefficient admissibility remains an all-prefix condition.

The last BT odd positions fix `C mod 3^BT`, so every exact class belongs to one and only one tail-residue bucket. Bucket-range sums are therefore mathematically identical to one monolithic exact class-max audit.

Depth 40 required an implementation guard because a full correction can exceed `2^63`. The MATH-050 certificate never tags the reconstructed full correction `X`. A high-bit tag is used only on the shorter early-prefix correction and is protected by an explicit abort if that early correction reaches bit 63 in the audited configuration.

Memory scheduling is also separated from mathematics: buckets above an expected population of 8,000,000 are processed serially, and smaller buckets are processed in parallel. This changes execution order only.

## 3. Complete depth-40 result

Canonical ledger:

`collatz/results/2026-09-10-depth40-complete-one-sided-hensel.tsv`

Central layers:

- q=26: `1,547,552,873 -> 1,546,488,816`, newly removed `1,064,057`;
- q=27: `1,574,857,210 -> 1,574,486,076`, newly removed `371,134`;
- q=28: `1,102,206,039 -> 1,102,103,404`, newly removed `102,635`;
- q=29: `605,093,585 -> 605,066,710`, newly removed `26,875`;
- q=30: `275,923,233 -> 275,916,261`, newly removed `6,972`.

The remaining q>=31 tail removes another `2,287` states.

Hence

\[
\boxed{5,259,076,592\to5,257,502,632},
\]

and the exact number newly removed at depth 40 is

\[
\boxed{1,573,960}.
\]

The all-prefix coefficient language at depth 40 contains

\[
\boxed{6,402,835,000}
\]

words. Therefore cumulative Hensel removal through depth 40 is

\[
\boxed{1,145,332,368}.
\]

These are finite prefix-language counts, not a proof of the Collatz conjecture.

## 4. Heavy-layer exact audits

### q=27

The unrestricted language contains

\[
\binom{40}{13}=12,033,222,880
\]

words and was partitioned into `3^12 = 531,441` exact tail-residue buckets.

Final diagnostics:

- arbitrary classes: `6,913,364,174`;
- coefficient-valid words: `1,924,081,230`;
- candidate classes: `1,924,079,997`;
- candidate collision excess: `1,233`;
- terminal class-max survivors: `1,574,486,076`.

The previously carried 0--150,000 bucket partial sum was independently rerun with the final memory-aware implementation. Its exact triple

`arbitrary=3,326,594,398`, `coefficient=542,590,830`, `survivors=444,029,524`

was reproduced without discrepancy.

### q=26

The unrestricted language contains

\[
\binom{40}{14}=23,206,929,840
\]

words and was partitioned into `3^13 = 1,594,323` exact tail-residue buckets.

Final diagnostics:

- arbitrary classes: `11,726,349,348`;
- coefficient-valid words: `1,899,474,678`;
- candidate classes: `1,899,468,055`;
- candidate collision excess: `6,623`;
- terminal class-max survivors: `1,546,488,816`.

The complete per-range raw sums for q=26 and q=27 are stored at

`collatz/results/2026-09-10-depth40-q26-q27-range-audit.tsv`.

## 5. Independent arithmetic checks

- q=26 unrestricted range sum = `23,206,929,840 = C(40,14)`.
- q=27 unrestricted range sum = `12,033,222,880 = C(40,13)`.
- q=26 coefficient-valid range sum = `1,899,474,678`, matching an independent all-prefix coefficient DP.
- q=27 coefficient-valid range sum = `1,924,081,230`, matching the same DP.
- the independent coefficient DP totals `6,402,835,000` over q=26..40.
- the child expansion of the MATH-049 q-layer survivor table totals `5,259,076,592` pre-Hensel candidates.
- all depth-40 q-layer survivors sum to `5,257,502,632`.
- all layerwise new removals sum to `1,573,960`.
- `6,402,835,000 - 5,257,502,632 = 1,145,332,368`, agreeing with cumulative removal.

## 6. DSD audit consequence

The depth-40 computation keeps three layers distinct:

1. all-prefix coefficient-valid language;
2. nested children of the previous coefficient+Hensel survivor language;
3. current terminal exact class-max selection.

Tail-residue buckets are execution partitions, not coarse equivalence classes. Candidate multiplicity inside one residue class does not create multiple surviving classes; the arbitrary-class maximum remains the governing comparison.

The memory-aware scheduler likewise changes only resource usage. No mathematical predicate is relaxed when a bucket is moved between serial and parallel execution.

## 7. Reproducibility

- main certificate: `collatz/src/2026_09_10_depth40_tailhash_memoryaware_range_certificate.cpp`
- canonical ledger: `collatz/results/2026-09-10-depth40-complete-one-sided-hensel.tsv`
- q26/q27 range ledger: `collatz/results/2026-09-10-depth40-q26-q27-range-audit.tsv`

Representative heavy runs:

- q=27: `K=40, Q=27, BT=12`, disjoint ranges covering `[0,531441)`;
- q=26: `K=40, Q=26, BT=13`, disjoint ranges covering `[0,1594323)`.

## 8. Next exact starting point

At depth 41,

\[
q_{\min}(41)=26.
\]

Since every depth-40 survivor already has q>=26, both children remain coefficient-admissible. Therefore the exact MATH-051 pre-Hensel population would be

\[
\boxed{2\cdot5,257,502,632=10,515,005,264}.
\]

The depth-41 all-prefix coefficient language would likewise be

\[
\boxed{12,805,670,000}.
\]

This is only the next finite-computation input, not an arbitrary-depth conclusion.

## 9. Prohibited upgrades

- finite depth-40 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- exact bucket partition => approximate residue quotient — **PROHIBITED**;
- candidate-class collision => multiple independent survivor classes — **PROHIBITED**;
- scheduler stability => mathematical strengthening — **PROHIBITED**;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**.
