# Depth-36 q>=25 one-sided root-Hensel checkpoint

## Status

- Collatz conjecture: `OPEN`
- Full depth-36 audit: `OPEN`
- Current result: `CONFIRMED / FINITE EXACT / q>=25 COMPLETE`

## Input

MATH-045 leaves

\[
216{,}467{,}460
\]

nested coefficient+Hensel survivors at depth 35.

Since

\[
q_{\min}(36)=23,
\]

every depth-35 survivor has both coefficient-admissible children. Therefore the complete depth-36 pre-Hensel population is

\[
\boxed{432{,}934{,}920}.
\]

## Exact q>=25 results

The completed layers are stored in

`collatz/results/2026-09-09-depth36-q25plus-terminal-classmax.tsv`.

Their aggregate is

\[
\boxed{222{,}830{,}411\to222{,}805{,}931},
\]

with

\[
\boxed{24{,}480}
\]

new depth-36 Hensel removals in q>=25.

Largest completed layers:

\[
q=25:\quad110{,}150{,}906\to110{,}133{,}317,
\]

newly removed `17,589`;

\[
q=26:\quad64{,}820{,}158\to64{,}815{,}098,
\]

newly removed `5,060`;

\[
q=27:\quad30{,}670{,}758\to30{,}669{,}475,
\]

newly removed `1,283`.

The smaller q>=28 tail contributes another `548` removals in total, including one removal at q=34.

## Computation method

The MATH-045 terminal class-max reduction is retained unchanged:

\[
\text{terminal exact class-max}\iff\text{root-Hensel class-max at every prefix},
\]

while coefficient admissibility is checked at every prefix.

- q>=27 was handled by direct fixed-q complete enumeration and exact residue-class sorting.
- q=26 used 64 exact residue buckets over `254,186,856` arbitrary words.
- q=25 used 128 exact residue buckets over

\[
\binom{36}{11}=600{,}805{,}296
\]

arbitrary words.

The first monolithic q=25 bucket-processing pass reached the execution boundary after generation. No lost partial aggregate was reused. Deleted buckets were regenerated, and the 128 buckets were reprocessed in four explicit ranges whose populations summed back to exactly `600,805,296`.

The q=25 coefficient-language population also re-summed to exactly `134,288,135`.

## Remaining depth-36 layers

Only q=23 and q=24 remain.

Their nested prefilter populations are

\[
q=23:\ 71{,}519{,}838,
\]

\[
q=24:\ 138{,}584{,}671,
\]

for a remaining total

\[
\boxed{210{,}104{,}509}.
\]

The unrestricted competitor languages are much larger:

\[
\binom{36}{13}=2{,}310{,}789{,}600
\]

for q=23 and

\[
\binom{36}{12}=1{,}251{,}677{,}700
\]

for q=24.

Thus the next exact engine should use prefix sharding plus residue buckets from generation onward rather than any monolithic representation.

## Prohibited upgrades

- q>=25 closure => full depth-36 closure — **PROHIBITED**;
- finite depth-36 partial result => arbitrary-depth theorem — **PROHIBITED**;
- coefficient-language count => nested Hensel prefilter count — **PROHIBITED**;
- historical two-sided depth-36 q=24 collision files => current one-sided q=24 result — **PROHIBITED**.
