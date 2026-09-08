# MATH-044 — depth-34 q-partitioned one-sided Hensel audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FINITE EXACT / ONE-SIDED ROOT-HENSEL`

## Input and coefficient gate

MATH-043 supplies `67,727,277` depth-33 all-prefix coefficient+Hensel states.
At depth 34 the frozen coefficient threshold is `q_min(34)=22`.
The `q=21` states therefore keep only their odd children; all higher-q states may generate both children.
The exact pre-Hensel candidate count is

\[
\boxed{124{,}547{,}105}.
\]

## Exact class-max method

The computation remains one-sided:

\[
\text{candidate}\in\mathcal L_{\rm coeff+previous\ Hensel},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

Each final-q layer is independent.  For length 34, arbitrary corrections are enumerated with a `17+17` meet-in-the-middle split,

\[
C=3^{q-t}C_{17,t}+2^{17}C_{17,q-t}.
\]

The `q=22` layer is processed by a custom flat hash with atomic maximum updates.  The largest `q=23` layer exceeded the monolithic memory envelope, so the exact Hensel residue space was divided into four disjoint buckets.  A Hensel class cannot cross buckets, hence summing the four audits is exactly equivalent to the monolithic layer.

## Exact result

All-prefix depth-34 survivors:

\[
\boxed{124{,}486{,}440}.
\]

Newly Hensel-pruned at depth 34:

\[
\boxed{60{,}665}.
\]

The full coefficient language at depth 34 contains

\[
151{,}917{,}636
\]

prefixes, so cumulative Hensel removal through depth 34 is

\[
\boxed{27{,}431{,}196}.
\]

The complete layer table is stored in `collatz/results/2026-09-08-depth34-q-partitioned-one-sided-hensel.tsv`.

### Largest layers

`q=22`:

\[
32{,}474{,}274\to32{,}432{,}663,
\]

newly removed `41,611`, credit range `2..287`.

This layer contains four candidate-candidate Hensel-class collisions:

\[
32{,}474{,}274\text{ candidates}
\to
32{,}474{,}270\text{ distinct classes}.
\]

`q=23`:

\[
39{,}151{,}495\to39{,}138{,}196,
\]

newly removed `13,299`, credit range `2..71`.

No candidate-class collision occurs in the q=23 layer.

## Relation to MATH-037

MATH-037 found five two-sided coefficient-language Hensel collisions at depth 34 in the full coefficient language.  MATH-040 corrected the actual selection rule: arbitrary competitors are allowed on the Hensel side.  MATH-044 now gives the complete nested one-sided depth-34 pruning count.

Therefore the MATH-037 five-event structure remains valid as a narrower two-sided subproblem, but it is not the total root-Hensel pruning mechanism.

## Ordinary-start interpretation

Every surviving low-34-bit class is nonzero, and each appears exactly

\[
340\cdot2^{27}
\]

times in the current 340-block first-cell window.  Thus the depth-34 prefix survivors correspond to

\[
\boxed{5{,}680{,}817{,}628{,}826{,}828{,}800}
\]

ordinary starts in that finite window.

This is a prefix count only.

## DSD calculation-direction consequence

The computation has crossed a new resource threshold.  One q-layer is no longer a sufficient partition at depth 34: the `q=23` layer needs an additional exact residue partition.  This is not a mathematical loss of information; it is a memory-layout refinement.

Depth 35 has roughly `2.17e8` pre-Hensel candidates and its two central q-layers are much larger.  The next engine should therefore use a permanent two-level partition `(q, residue-bucket)` rather than attempting a monolithic per-q target map.

## Prohibited upgrades

- finite depth-34 result ⇒ arbitrary-depth Hensel theorem — **PROHIBITED**;
- four candidate-class collisions ⇒ only four Hensel removals — **PROHIBITED**;
- MATH-037 five two-sided collisions ⇒ complete depth-34 pruning — **PROHIBITED**;
- prefix survivor count ⇒ first-cell terminal survivor count — **PROHIBITED**.
