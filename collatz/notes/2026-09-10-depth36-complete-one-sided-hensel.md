# MATH-046 — complete depth-36 one-sided root-Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-36 ONE-SIDED ROOT-HENSEL`

## 1. Input from MATH-045

MATH-045 leaves exactly

\[
216{,}467{,}460
\]

nested coefficient+Hensel survivors at depth 35.

Since

\[
q_{\min}(36)=23,
\]

every depth-35 survivor has both coefficient-admissible children. Therefore the exact depth-36 pre-Hensel population is

\[
\boxed{432{,}934{,}920}.
\]

The terminal exact class-max reduction from MATH-045 is retained: root-Hensel maximality at every prefix is equivalent, for a fixed full parity word, to terminal maximality in the exact class

\[
(q,C\bmod3^q).
\]

Coefficient admissibility remains an all-prefix condition.

## 2. Previously completed q>=25 tail

The q>=25 layers were already certified in

`collatz/results/2026-09-09-depth36-q25plus-terminal-classmax.tsv`.

They give

\[
222{,}830{,}411\to222{,}805{,}931,
\]

with exactly

\[
24{,}480
\]

new depth-36 Hensel removals.

## 3. q=24 exact residue-bucket audit

The q=24 unrestricted language contains

\[
\binom{36}{12}=1{,}251{,}677{,}700
\]

parity words.

The calculation used 256 disjoint interval buckets of the exact residue

\[
r=C\bmod3^{24}.
\]

A complete exact Hensel class belongs to one and only one bucket, so summing the bucket audits is identical to a monolithic class-max computation.

Three completed 2-bit prefix shards had populations

- mask 0: `131,128,140`, coefficient-valid `0`;
- mask 1: `286,097,760`, coefficient-valid `0`;
- mask 2: `286,097,760`, coefficient-valid `0`.

The remaining 2-bit mask was subdivided into four 4-bit shards whose populations were

- mask 3: `64,512,240`, coefficient-valid `0`;
- mask 7: `129,024,480`, coefficient-valid `30,083,729`;
- mask 11: `129,024,480`, coefficient-valid `30,083,729`;
- mask 15: `225,792,840`, coefficient-valid `109,824,127`.

The seven shard populations sum exactly to

\[
1{,}251{,}677{,}700,
\]

and their coefficient-valid populations sum to

\[
169{,}991{,}585.
\]

The exact unrestricted class count is

\[
701{,}631{,}910.
\]

There are 30 excess coefficient-candidate collisions inside candidate classes. The exact terminal survivors are

\[
\boxed{138{,}524{,}197}.
\]

Against the nested prefilter

\[
138{,}584{,}671,
\]

this gives

\[
\boxed{60{,}474}
\]

new q=24 removals. The positive translation-credit range among dominated candidate classes is `1..287`.

## 4. q=23 tail-10 exact flat-hash audit

The final q=23 unrestricted language contains

\[
\binom{36}{13}=2{,}310{,}789{,}600
\]

parity words.

A direct 8-byte external record approach would require a much larger temporary disk image. Instead the exact correction decomposition was used.

Let the last ten odd positions be fixed. Write the correction as

\[
C=3^{10}C_{13}+T_{10},
\]

where `C_13` is the correction supplied by the first thirteen odd positions and `T_10` is the correction supplied by the last ten odd positions.

Then

\[
\boxed{C\bmod3^{10}=T_{10}\bmod3^{10}}.
\]

Therefore `C mod 3^10` is an exact downstream-safe bucket key determined only by the last ten odd positions. There are

\[
3^{10}=59{,}049
\]

possible buckets. A full class modulo `3^23` cannot cross these buckets.

The implementation precomputed exactly `20,058,300` early correction states and `1,144,066` admissible last-ten-position tuples. Their induced word-count sum is exactly

\[
\boxed{2{,}310{,}789{,}600}.
\]

There are `39,276` nonempty tail buckets; the largest contains `13,873,869` words.

Inside each bucket a flat open-address table stores only

1. the maximum unrestricted correction `C` for each exact residue `C mod 3^23`, and
2. the maximum coefficient-valid correction `C` in that exact class.

A coefficient-valid class survives iff these two maxima are equal. This is the same terminal class-max criterion as the sorting implementation, without an ordering pass.

### Regression

The same tail-10 flat-hash program was first run at q=26 and reproduced the previously certified depth-36 survivor count exactly:

\[
64{,}820{,}158\to64{,}815{,}098.
\]

The unrestricted q=26 class count also reproduced `172,335,487`.

### Exact q=23 result

The q=23 audit gives

- unrestricted words: `2,310,789,600`;
- unrestricted exact classes: `1,112,317,281`;
- coefficient-valid words: `87,986,917`;
- coefficient candidate classes: `87,986,897`;
- candidate collision excess: `20`;
- terminal survivors: `71,408,693`;
- dominated candidate classes: `16,578,204`;
- positive translation-credit range: `1..383`.

Thus

\[
71{,}519{,}838\to\boxed{71{,}408{,}693},
\]

and the newly removed q=23 population is

\[
\boxed{111{,}145}.
\]

## 5. Complete depth-36 result

Combining q=23, q=24, and the previously certified q>=25 tail gives

\[
\boxed{432{,}934{,}920\to432{,}738{,}821}.
\]

Hence the exact number newly removed by the depth-36 one-sided root-Hensel step is

\[
\boxed{196{,}099}.
\]

The complete all-prefix coefficient language at depth 36 contains

\[
\boxed{527{,}682{,}754}
\]

words. Therefore cumulative Hensel removal through depth 36 is

\[
\boxed{94{,}943{,}933}.
\]

The canonical layer table is stored in

`collatz/results/2026-09-10-depth36-complete-one-sided-hensel.tsv`.

## 6. Independent arithmetic checks

- q=24 shard population sum = `1,251,677,700 = C(36,12)`;
- q=24 coefficient population sum = `169,991,585`;
- q=23 tail-bucket word-count sum = `2,310,789,600 = C(36,13)`;
- q=23 flat-hash q=26 regression reproduces the existing q=26 survivor and class counts;
- all depth-36 prefilter layers sum to `432,934,920`;
- all depth-36 survivor layers sum to `432,738,821`;
- layerwise removals sum to `196,099`, equal to prefilter minus survivors;
- coefficient-language layers sum to `527,682,754`;
- `527,682,754 - 432,738,821 = 94,943,933`.

## 7. DSD audit consequence

The depth-36 computation confirms that the exact root-Hensel descriptor admits two independent computational decompositions without information loss:

1. prefix-shard plus full-residue interval buckets;
2. low-ternary tail buckets plus exact-residue class-max hashing.

The second decomposition is stronger computationally for the largest central layer because the last `b` odd positions determine `C mod 3^b` exactly:

\[
C=3^bC_{q-b}+T_b.
\]

This is an exact descriptor decomposition, not a probabilistic hash or heuristic approximation.

## 8. Reproducibility

q=24 generator:

`collatz/src/2026_09_10_depth36_q24_residue_bucket_generator.cpp`

q=24 mixed-shard processor:

`collatz/src/2026_09_10_depth36_q24_mixed_shard_processor.cpp`

q=23 tail-10 flat-hash certificate:

`collatz/src/2026_09_10_depth36_q23_tail10_flat_hash_certificate.cpp`

q>=25 checkpoint:

`collatz/results/2026-09-09-depth36-q25plus-terminal-classmax.tsv`

Canonical result ledger:

`collatz/results/2026-09-10-depth36-complete-one-sided-hensel.tsv`

## 9. Next target: depth 37

At depth 37 the coefficient threshold rises:

\[
q_{\min}(37)=24.
\]

Therefore q=23 depth-36 survivors may produce only their odd children, while every q>=24 survivor may produce both children.

The exact depth-37 pre-Hensel population is consequently

\[
2\cdot432{,}738{,}821-71{,}408{,}693
=\boxed{794{,}068{,}949}.
\]

The next one-sided audit should retain terminal class-max reduction and use the tail-ternary flat-hash decomposition as the default central-layer engine.

## 10. Prohibited upgrades

- finite depth-36 closure => arbitrary-depth Hensel theorem — **PROHIBITED**;
- flat hash => probabilistic class identification — **PROHIBITED**; keys are the exact residues and collisions in the implementation are resolved by equality;
- tail bucket equality => full Hensel-class equality — **PROHIBITED**; the tail bucket is only an exact partition before full-residue comparison;
- cumulative Hensel removal => Collatz proof — **PROHIBITED**;
- depth-37 prefilter count => depth-37 survivor count — **PROHIBITED**.
