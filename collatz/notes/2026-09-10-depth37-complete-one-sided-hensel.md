# MATH-047 — complete depth-37 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-37 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-046

MATH-046 leaves

\[
432{,}738{,}821
\]

nested coefficient+Hensel survivors at depth 36.

At depth 37 the coefficient threshold rises to

\[
q_{\min}(37)=24.
\]

Hence the q=23 depth-36 survivors may produce only odd children, while every q>=24 survivor produces both children. Therefore

\[
2\cdot432{,}738{,}821-71{,}408{,}693
=\boxed{794{,}068{,}949}
\]

is the exact depth-37 pre-Hensel population.

The terminal exact class-max reduction remains in force. Coefficient admissibility is still checked at every prefix.

## 2. Tail-10 flat-hash engine

For a fixed final q, split the q odd positions into an early part of q-10 positions and the last ten odd positions. Then

\[
C=3^{10}C_{q-10}+T_{10},
\]

so

\[
C\bmod3^{10}=T_{10}\bmod3^{10}.
\]

Thus the last ten odd positions determine one of

\[
3^{10}=59{,}049
\]

exact partition buckets. A complete class modulo `3^q` cannot cross this partition.

Inside each bucket a flat open-address table stores only the maximum unrestricted correction and maximum coefficient-valid correction for each exact residue. Equality of these maxima is exactly the terminal one-sided root-Hensel survival criterion.

The implementation used for this depth is

`collatz/src/2026_09_10_depth37_tail10_flat_hash_range_certificate.cpp`.

Local source SHA-256 during the calculation:

`bb5101ae9d2635d427e6ba7d6199b5a11f981145900dc5ff6e613b627e1e7804`.

## 3. q>=26 tail

The exact q>=26 aggregate is

\[
335{,}478{,}545\to\boxed{335{,}451{,}250},
\]

with

\[
\boxed{27{,}295}
\]

new removals.

The largest removal in this tail is q=26:

\[
174{,}948{,}415\to174{,}928{,}591,
\]

newly removed `19,824`.

The q=27 through q=31 removals are respectively `5,526`, `1,366`, `415`, `119`, and `44`. q=32,33,34,36,37 have no new removal; q=35 has one.

## 4. q=25 exact result

The unrestricted q=25 language contains

\[
\binom{37}{12}=1{,}852{,}482{,}996
\]

words.

The exact flat-hash audit gives

- unrestricted classes: `1,076,466,252`;
- coefficient-valid words: `304,279,720`;
- coefficient candidate classes: `304,279,685`;
- candidate collision excess: `35`;
- terminal survivors: `248,587,101`;
- dominated candidate classes: `55,692,584`;
- positive translation-credit range: `1..287`.

Therefore

\[
248{,}657{,}514\to\boxed{248{,}587{,}101},
\]

with

\[
\boxed{70{,}413}
\]

new removals.

## 5. q=24 exact ranged audit

The unrestricted q=24 language contains

\[
\binom{37}{13}=3{,}562{,}467{,}300
\]

words.

A monolithic 5-thread tail-10 run exceeded the memory envelope because the largest buckets can occur simultaneously. A 3-thread full run remained within memory but exceeded the single execution window. Therefore the same 59,049 exact buckets were processed as four disjoint ranges:

- `[0,15000)`;
- `[15000,30000)`;
- `[30000,45000)`;
- `[45000,59049)`.

No exact Hensel class can cross these ranges because every class is already confined to a unique `C mod 3^10` bucket.

The four unrestricted word counts are

`916,366,057`, `917,751,655`, `907,125,814`, and `821,223,774`,

which sum exactly to

\[
3{,}562{,}467{,}300.
\]

Their exact class counts sum to

\[
1{,}811{,}393{,}651.
\]

Their coefficient-valid counts sum to

\[
257{,}978{,}502,
\]

and candidate-class collision excess sums to `267`.

The four survivor partial sums are

`54,164,472`, `53,500,615`, `53,060,813`, and `48,978,342`,

hence

\[
\boxed{209{,}704{,}242}
\]

terminal survivors.

Against the nested prefilter

\[
209{,}932{,}890,
\]

this gives

\[
\boxed{228{,}648}
\]

new removals. The positive translation-credit range is `1..383`.

## 6. Complete depth-37 result

Combining q=24, q=25, and q>=26 gives

\[
\boxed{794{,}068{,}949\to793{,}742{,}593}.
\]

Thus the exact number newly removed at depth 37 is

\[
\boxed{326{,}356}.
\]

The complete all-prefix coefficient language contains

\[
\boxed{967{,}378{,}591}
\]

words, so cumulative Hensel removal through depth 37 is

\[
\boxed{173{,}635{,}998}.
\]

The canonical result ledger is

`collatz/results/2026-09-10-depth37-complete-one-sided-hensel.tsv`.

## 7. Independent checks

- q=24 four range populations sum to `C(37,13)` exactly;
- q=24 coefficient-valid range sum equals the independently derived coefficient layer `257,978,502`;
- all prefilter layers sum to `794,068,949`;
- all survivor layers sum to `793,742,593`;
- layerwise new removals sum to `326,356`;
- coefficient layers sum to `967,378,591`;
- `967,378,591 - 793,742,593 = 173,635,998`.

## 8. DSD audit consequence

The depth-37 calculation confirms that resource partitions can be refined independently of the mathematical descriptor. Thread count, bucket ranges, and execution segmentation changed, while the exact Hensel object remained `(q,C mod 3^q)` and every partition was a disjoint cover of that object space.

This separates computational implementation boundaries from mathematical state boundaries.

## 9. Next target: depth 38

Since

\[
q_{\min}(38)=24,
\]

every depth-37 survivor already satisfies the threshold and both children are coefficient-admissible. Therefore the exact depth-38 pre-Hensel population is

\[
\boxed{2\cdot793{,}742{,}593=1{,}587{,}485{,}186}.
\]

The tail-10 flat-hash range engine should remain the default central-layer implementation.

## 10. Prohibited upgrades

- finite depth-37 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- disjoint execution ranges => independence of mathematical classes — **PROHIBITED**;
- flat hashing => probabilistic equality — **PROHIBITED**; exact residue keys are compared explicitly;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**;
- depth-38 prefilter => depth-38 survivor count — **PROHIBITED**.
