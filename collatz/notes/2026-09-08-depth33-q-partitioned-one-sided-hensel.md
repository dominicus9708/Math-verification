# MATH-043 — depth-33 q-partitioned one-sided Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL`

## Input

MATH-042 produces exactly

\[
33{,}880{,}411
\]

depth-32 all-prefix coefficient+Hensel states.

Packed checkpoint SHA-256:

`35093b29775e538c99ba692851c4fe6112e86437ddbdae9ad4ea177cd4698013`

Since `q_min(33)=21`, every depth-32 survivor has both even and odd coefficient-admissible children.  Thus the depth-33 pre-Hensel count is exactly

\[
2\cdot33{,}880{,}411
=\boxed{67{,}760{,}822}.
\]

## Exact q-layer method

Hensel classes are partitioned by final q.  For the large layers, arbitrary length-33 parity words are enumerated exactly by a 16+17 meet-in-the-middle split.  If the lower half contains `t` odd positions, then

\[
C=3^{q-t}C_{16,t}+2^{16}C_{17,q-t}.
\]

This enumerates exactly

\[
\binom{33}{q}
\]

arbitrary words in each q-layer without materializing the global unrestricted class table.  Only class residues queried by actual coefficient-surviving candidates are retained.

The q=21 layer was also computed by the reverse-Hensel oracle, and the same class-max criterion is used throughout.

## Exact result

New depth-33 removals:

\[
\boxed{33{,}545}.
\]

All-prefix coefficient+Hensel survivors:

\[
\boxed{67{,}727{,}277}.
\]

The full coefficient language contains

\[
82{,}694{,}966
\]

prefixes at depth 33, so cumulative Hensel removal is

\[
\boxed{14{,}967{,}689}.
\]

Layer results are stored in `collatz/results/2026-09-08-depth33-q-partitioned-one-sided-hensel.tsv`.

The first layers are:

- `q=21`: `10,924,522 -> 10,907,449`, newly removed `17,073`, credit `2..127`;
- `q=22`: `21,578,098 -> 21,566,825`, newly removed `11,273`, credit `2..71`;
- `q=23`: `17,588,380 -> 17,584,670`, newly removed `3,710`, credit `2..47`.

A single credit-1 removal occurs again at `q=31`.

## Ordinary-start interpretation

Every surviving low-33-bit residue is nonzero.  Each appears exactly

\[
340\cdot2^{28}
\]

times in the current 340-block first-cell window.  Hence the depth-33 all-prefix coefficient+Hensel survivors represent

\[
\boxed{6{,}181{,}336{,}844{,}945{,}326{,}080}
\]

ordinary starts in that finite window.

This is again a prefix count, not a terminal candidate count.

## Reproducibility

- q-layer MITM certificate: `collatz/src/2026_09_08_depth33_q_partitioned_mitm_hensel_certificate.cpp`
- result ledger: `collatz/results/2026-09-08-depth33-q-partitioned-one-sided-hensel.tsv`
- depth-33 checkpoint states: `67,727,277`
- depth-33 packed checkpoint SHA-256: `e8696c1f6b9cc027f7d782d288c9cc054a051bae918ee89caf15453fec154941`

## DSD direction consequence

The actual candidate set remains manageable when q-layers are processed independently.  The next depth, 34, has roughly `1.25e8` pre-Hensel candidates and the two central q-layers no longer fit comfortably in one in-memory target map.  Therefore the next exact engine should retain the q-partition and add a second residue-bucket partition inside the heavy layers.

## Prohibited upgrades

- finite depth-33 pruning ⇒ arbitrary-depth theorem — **PROHIBITED**;
- sparse newly-pruned count ⇒ asymptotic sparsity — **PROHIBITED**;
- q-layer independence ⇒ candidate independence across depths — **PROHIBITED**;
- prefix survivor count ⇒ first-cell survivor count — **PROHIBITED**.
