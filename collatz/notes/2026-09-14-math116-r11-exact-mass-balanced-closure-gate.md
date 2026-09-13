# MATH-116 — r=11 exact mass-balanced sharded closure gate

Status: `MAINLINE CANDIDATE GATE / EXECUTION REQUIRED / NO r=11 CLOSURE CLAIM YET`

Date: 2026-09-14

## Purpose

MATH-112 froze the exact `r=11` workload. MATH-114 proved that exact consecutive-parameter AP splitting plus deterministic mass-balanced scheduling preserves the source union exactly. MATH-115 generalized the exact source exporter and one-shot shard preparation.

MATH-116 connects those already-audited components to the unchanged MATH-108 generalized exact AP-union closure engine.

## Frozen r=11 source

```text
classification:             1013 total
safe:                        119
singleton:                   414
critical:                    480
branch-and-bound nodes:  3,994,436
AP source cylinders:       605,972
represented occurrence mass: 3,419,719,061,560
max unsplit multiplicity:     51,905,193,085
```

These totals are enforced by the MATH-115 generic exporter before any partitioning is accepted.

## Exact partition

Use 128 shards and the MATH-114 exact split identity

```text
AP(a,b,m)
= disjoint union_j AP(a+b*s_j,b,m_j),
```

where the `m_j` are consecutive parameter intervals summing exactly to `m`.

The independently audited MATH-114 totals for `r=11` are:

```text
total source records: 605,972
exact split pieces:    605,977
total mass:            3,419,719,061,560
cap:                       26,716,555,169
min shard mass:            26,716,555,168
max shard mass:            26,716,555,169
```

Every shard total and every split-piece multiplicity are below `2^64-1`, so the unchanged MATH-108 C++ engine remains inside its audited count domain.

## Acceptance gate

`r=11` may be promoted to `CLOSED` only after all of the following hold:

1. the generic exporter reproduces the frozen MATH-112 source totals exactly;
2. the one-shot MATH-115 partition certificate reproduces the MATH-114 128-shard totals exactly;
3. all 128 shard jobs execute the unchanged MATH-108 AP-union engine;
4. every shard reports `PASS generalized exact AP-union audit`;
5. the summed shard occurrence mass equals exactly `3,419,719,061,560`;
6. no shard failure is reclassified as a mathematical counterexample until its job log is audited.

## DSD audit classification

```text
source semantics: unchanged
ordinary-integer membership: preserved exactly
parameter partition: exact/disjoint/exhaustive within each AP
transition engine: unchanged MATH-108
new object: execution certificate for r=11
```

The scheduler is not a theorem-strengthening device. It is an exact resource representation.

## Claim boundary

Until all 128 closure jobs pass, the formal state remains:

```text
r>=13 CLOSED
r=12 OPEN (MATH-111 final jobs pending)
r=11 OPEN (MATH-116 gate prepared)
2<=r<=10 OPEN
First universal Farey cell OPEN
Collatz conjecture OPEN
```
