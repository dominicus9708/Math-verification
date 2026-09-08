# MATH-042 — depth-32 q-partitioned one-sided Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL`

## Scope correction retained

The actual root-Hensel comparison is asymmetric:

\[
\text{candidate}\in\mathcal L_{\rm coeff},\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

MATH-037~039 remain two-sided coefficient-language collision studies and are not used as the first-pruning frontier.

## Method

MATH-041 is regenerated through depth 31, yielding exactly

\[
19{,}347{,}686
\]

all-prefix coefficient+Hensel survivors.  They are written as a deterministic packed checkpoint (`u64 C + u8 q`).

Checkpoint SHA-256:

`f4d39cf0fd464b99f78d01aa3a38fc20ab5f3664c3c02e69478ccaccedd8a79d`

At depth 32, `q_min(32)=21`.  Candidates are separated by final `q`; Hensel classes never mix different `q`, so the twelve layers `q=21..32` are exact independent audits.

For a queried class `(k,q,r)`, the unrestricted competitor maximum is reconstructed by the exact reverse relation

\[
r_{\rm prev}\equiv\frac{r-2^{p_q}}3\pmod{3^{q-1}}.
\]

## Exact result

Depth-32 pre-Hensel candidate count:

\[
33{,}894{,}412.
\]

Newly removed at depth 32:

\[
\boxed{14{,}001}.
\]

All-prefix survivors:

\[
\boxed{33{,}880{,}411}.
\]

Full coefficient language at depth 32:

\[
41{,}347{,}483,
\]

so cumulative Hensel-removed coefficient classes are

\[
\boxed{7{,}467{,}072}.
\]

Layer table is stored in `collatz/results/2026-09-08-depth32-q-partitioned-one-sided-hensel.tsv`.

The largest new pruning layer is `q=21`:

\[
10{,}933{,}870\to10{,}924{,}522,
\]

with exact credit range `2..71`.  The `q=30` layer contains one legal credit-1 removal, so high-q layers must not be declared vacuous by a monotone heuristic.

## Independent cross-check

A separate 16+16 meet-in-the-middle arbitrary-word scan was run for all q-layers.  The large q=21 and q=22 layers and representative q=24,26,30 layers were additionally rechecked with the reverse-Hensel oracle; survivor counts agree exactly.

## Ordinary-start interpretation

All depth-32 survivors are nonzero residues modulo `2^32`.  Each such residue occurs exactly

\[
340\cdot2^{29}
\]

times in the current 340-block first-cell integer window.  Therefore the depth-32 all-prefix coefficient+Hensel survivors represent exactly

\[
\boxed{6{,}184{,}398{,}431{,}851{,}642{,}880}
\]

ordinary starts in that finite window.

This is a prefix count, not a terminal survivor count and not a proof of first-cell emptiness.

## Reproducibility

- checkpoint generator: `collatz/src/2026_09_08_depth31_packed_hensel_checkpoint_generator.cpp`
- q-layer certificate: `collatz/src/2026_09_08_depth32_q_partitioned_one_sided_hensel_certificate.cpp`
- result ledger: `collatz/results/2026-09-08-depth32-q-partitioned-one-sided-hensel.tsv`
- depth-32 packed checkpoint state count: `33,880,411`
- depth-32 checkpoint SHA-256: `35093b29775e538c99ba692851c4fe6112e86437ddbdae9ad4ea177cd4698013`

## Prohibited upgrades

- finite depth-32 pruning ⇒ arbitrary-depth Hensel theorem — **PROHIBITED**;
- 33,880,411 prefix classes ⇒ final first-cell survivors — **PROHIBITED**;
- high-q layers mostly vacuous ⇒ all higher q vacuous — **PROHIBITED**;
- candidate-class Hensel maximum ⇒ Collatz convergence — **PROHIBITED**.
