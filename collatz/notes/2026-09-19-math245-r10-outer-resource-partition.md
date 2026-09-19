# MATH-245 — exact outer resource partition for the MATH-241 r=10 sign gate

Date: 2026-09-19

Status: EXECUTION-ONLY EXACT PARTITION / SAME MATH-241 THEOREM GATE / NO NEW MATHEMATICAL ASSUMPTION

## Purpose

MATH-240 showed that evaluating all 95,536 MATH-235 post-J survivor families in one union process causes large transient state growth.

MATH-241 repairs this with exact recursive resource splitting.

MATH-245 adds one outer 16-way partition so those exact resource leaves can run in parallel rather than serially.

## Partition

Let the canonical MATH-235 survivor rows be

[
F_0,ldots,F_{95535}.
]

Define chunk (cin{0,ldots,15}) by

[
mathcal F_c={F_i:iequiv cpmod{16}}.
]

These sets are pairwise disjoint and their union is the complete post-J survivor set.

The partition certificate recomputes the frozen source and verifies

[
sum_c |mathcal F_c|=95{,}536
]

and

[
sum_c operatorname{mass}(mathcal F_c)
=
6{,}557{,}104{,}120{,}419.
]

## Closure semantics

Every chunk is sent to the **same** MATH-241 exact recurrence.

A chunk PASS means every source represented in that chunk closes under the unchanged floor / synchronized-first-failure / exact AP continuation rules.

The workflow can declare success only when all 16 matrix jobs PASS and the independent partition certificate reproduces complete row and mass coverage.

Thus

[
igwedge_{c=0}^{15}operatorname{Closed}(mathcal F_c)
Longrightarrow
operatorname{Closed}!left(igcup_cmathcal F_cight).
]

This is set decomposition, not a new Collatz condition.

## Architectural status

MATH-245 must not be presented as a 16-case mathematical proof architecture.

The proof-facing statement remains MATH-243/244 plus one exact synchronized recurrence. The 16 chunks are only parallel memory pages used to evaluate its finite frozen support.

## Claim boundary

Established by construction:
- exact disjoint coverage of all MATH-235 survivor rows;
- exact mass preservation under the 16-way partition;
- same MATH-241 gate on every chunk.

A new r=10 closure claim requires successful completion of all matrix jobs and the final coverage certificate.
