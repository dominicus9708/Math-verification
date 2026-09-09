# Terminal class-max prefix reduction and depth-35 q=26,27

## Status

- Collatz conjecture: `OPEN`
- Result: `CONFIRMED / EXACT REDUCTION + FINITE EXACT DEPTH-35 EXTENSION`
- Full depth-35 audit: `OPEN`

## 1. Prefix-reduction lemma

For a length-j parity prefix with q odd bits, write its correction as

\[
C=h3^q+r,\qquad 0\le r<3^q.
\]

Suppose another arbitrary prefix lies in the same exact Hensel class `(q,r)` and has larger correction:

\[
\widetilde C-C=m3^q>0.
\]

Append the same parity suffix to both prefixes.

- after an even child, the correction difference is unchanged and q is unchanged;
- after an odd child, the correction difference is multiplied by 3 and q increases by one.

Hence after every common suffix step the two words remain in the same exact Hensel class and the correction ordering remains strict. Therefore a prefix that is non-maximal in its `(q,r)` class can never produce a terminal class-maximum descendant under a common suffix.

Thus

\[
\boxed{\text{terminal class-max}\Longrightarrow\text{class-max at every earlier prefix}.}
\]

Because the terminal prefix itself is included in the all-prefix condition, the converse is immediate. Therefore, for a fixed full parity word, the all-prefix root-Hensel maximality condition is equivalent to terminal exact class-maximality.

This reduction applies only to the Hensel class-max condition. Coefficient admissibility must still be checked at every prefix.

## 2. Direct fixed-q certificate

For fixed `(k,q)`, enumerate every arbitrary length-k parity word with q odd bits. For each word compute

\[
r=C\bmod3^q.
\]

Within every residue class retain the maximum correction among the arbitrary language. Separately mark words satisfying the coefficient threshold at every prefix. A coefficient-valid word survives the full one-sided Hensel chain exactly when its terminal correction equals the arbitrary class maximum.

This removes the need to materialize the previous-depth Hensel checkpoint when only the final survivor count is required.

## 3. MATH-044 regression

The direct terminal method reproduces the MATH-044 depth-34 survivor counts exactly:

| depth | q | direct survivor | MATH-044 |
|---:|---:|---:|---:|
| 34 | 25 | 15,148,621 | 15,148,621 |
| 34 | 26 | 6,586,664 | 6,586,664 |
| 34 | 27 | 2,350,378 | 2,350,378 |

The q=25 regression tests the same deficit `d=k-q=9` used by the new depth-35 q=26 calculation.

## 4. New depth-35 exact results

For q=27:

- MATH-044-derived prefilter: `8,937,042`
- arbitrary words: `23,535,820`
- coefficient-valid full words: `10,623,245`
- arbitrary exact Hensel classes: `17,743,509`
- final survivors: `8,936,673`
- newly pruned at depth 35: `369`

For q=26:

- MATH-044-derived prefilter: `21,735,285`
- arbitrary words: `70,607,460`
- coefficient-valid full words: `26,128,410`
- arbitrary exact Hensel classes: `50,319,787`
- final survivors: `21,734,085`
- newly pruned at depth 35: `1,200`

Combining these with the previously certified q>=28 tail gives

\[
\boxed{34,798,433\to34,796,716}
\]

for q>=26, with exactly

\[
\boxed{1,717}
\]

new depth-35 Hensel removals.

## 5. Remaining central layers

Only q=23,24,25 remain for the complete depth-35 audit. Their exact prefilter count is

\[
\boxed{181,741,784},
\]

which is about 83.93% of the full depth-35 prefilter.

A monolithic q=25 sort reaches the current operational memory/time boundary. The next exact implementation should retain the terminal-class reduction but partition the exact residue space into disjoint buckets, matching the partition strategy already required by MATH-044.

No q=23,24,25 survivor count is inferred here.

## Reproducibility

- certificate: `collatz/src/2026_09_09_fixed_q_terminal_classmax_certificate.cpp`
- result ledger: `collatz/results/2026-09-09-depth35-q26-q27-terminal-classmax.tsv`
- local certificate SHA-256: `6617302087640bf14392b9a82cc6151e28de8dec94181cf1c2588931632bc8bb`

## Prohibited upgrades

- terminal Hensel reduction => coefficient-prefix reduction — **PROHIBITED**;
- q>=26 closure => full depth-35 closure — **PROHIBITED**;
- finite depth-35 closure => Collatz proof — **PROHIBITED**.
