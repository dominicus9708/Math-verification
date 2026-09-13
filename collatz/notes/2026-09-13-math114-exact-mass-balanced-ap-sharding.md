# MATH-114 — exact mass-balanced AP sharding

Status: `EXACT REPRESENTATION LEMMA / RESOURCE-SCHEDULING GENERALIZATION / NO NEW CLOSURE CLAIM`

## Motivation

MATH-113 shows that lower paid-count layers contain fewer compressed AP records but vastly larger AP multiplicities.  Record-index modulo sharding is exact but can place several very heavy APs in one job and does not solve the `r=2` uint64 count-width problem.

The correct object to balance is therefore source **parameter mass**, without changing the underlying AP union.

## Exact split identity

For an AP source record

```text
P(a,b,m) = {a+b*k : 0 <= k < m},
```

choose consecutive parameter lengths `m_0,...,m_{p-1}` with cumulative offsets `s_j` and sum `m`.

Then exactly

```text
P(a,b,m) = disjoint union_j P(a+b*s_j, b, m_j).
```

This is the same single-AP parameter-bisection/set-union principle already used by MATH-071/MATH-108, generalized from recursive bisection to an arbitrary finite consecutive parameter partition.

No candidate is removed and no new ordinary integer is introduced.

## Deterministic mass-balanced schedule

For `N` shards and global source multiplicity mass `T`:

```text
cap = ceil(T/N).
```

1. split every source AP into consecutive exact pieces of mass at most `cap`;
2. sort pieces by decreasing mass with deterministic source/piece tiebreaks;
3. assign each piece to the currently least-mass shard.

The scheduling step changes only which exact source pieces are audited together.

## Exact audits

For 128 shards:

```text
r=12:
  T = 580,472,268,528
  cap = 4,534,939,598
  exact pieces = 1,053,560
  shard mass range = 4,534,939,597 .. 4,534,939,598

r=11:
  T = 3,419,719,061,560
  cap = 26,716,555,169
  exact pieces = 605,977
  shard mass range = 26,716,555,168 .. 26,716,555,169

r=2:
  T = 74,283,701,945,452,943,666
  cap = 580,341,421,448,851,123
  exact pieces = 1,235
  shard mass range =
    580,341,421,448,851,114 .. 580,341,421,448,851,123
```

All `r=2` shard masses and all split-piece multiplicities are below `2^64-1`.

## Consequence for the r=2 count-width barrier

MATH-113 identified that the *global* `r=2` occurrence mass and the largest unsplit AP multiplicity exceed uint64.  MATH-114 shows that this does not require changing the already-audited AP transition engine.

Instead:

- a Python arbitrary-precision partition certificate handles the global source family;
- each oversized source AP is split into exact disjoint consecutive parameter pieces;
- each engine invocation receives a shard whose total mass and each AP count fit uint64;
- the existing MATH-108 engine then operates within its audited count domain;
- global closure is accepted only if every exact shard closes and the arbitrary-precision partition certificate proves exhaustive coverage.

This is preferable to changing the core transition engine because it preserves the already-audited `normalize`, `advance`, and recursive closure dynamics unchanged.

## DSD audit classification

The old `record_index mod N` partition remains mathematically valid.  MATH-114 does **not** invalidate it.

MATH-114 supersedes it only as the preferred resource schedule for increasingly heavy low-r AP families.

Classification:

```text
mathematical source semantics: unchanged
ordinary-integer address lineage: preserved
AP transition dynamics: unchanged
new object: exact implementation partition only
```

## Claim boundary

MATH-114 does not close `r=12`, `r=11`, `r=2`, any other paid-count layer, the first universal Farey cell, or Collatz.
