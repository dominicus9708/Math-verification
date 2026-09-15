# MATH-157 — `r=10` bimodal exact scheduler composition

Date: 2026-09-15

## Status

`SUPPORT / EXACT SCHEDULER-COMPOSITION LEMMA / NO r=10 CLOSURE CLAIM`

## Motivation

MATH-143 shows that the frozen MATH-117 `r=10` 128-shard partition is occurrence-mass balanced but geometrically bimodal:

- shards `0..13` contain one giant AP piece each, with multiplicity `215291123465`;
- the remaining shards are fragmented, with roughly 2400 source pieces per shard;
- global shard mass differs by only 2, while source-record count ranges from 1 to 2448.

Therefore one resource schedule is not a natural runtime model for both regimes.

MATH-153/MATH-156 provide exact external parameter-interval microsharding for a single giant AP. MATH-154 provides exact source-record chunk scheduling for a fragmented shard while leaving the MATH-108 transition engine unchanged.

## Exact decomposition principle

Let a theorem-facing prepared shard source be `S`.

### Regime A — one giant AP

For

```text
P(a,b,m) = {a+b*k : 0 <= k < m},
```

choose consecutive parameter intervals with offsets `s_j` and lengths `m_j`. Then

```text
P(a,b,m) = disjoint_union_j P(a+b*s_j,b,m_j),
sum_j m_j = m.
```

MATH-156 implements this identity generically. For the MATH-143 giant `r=10` shards, `K=64` gives

```text
m                  215291123465
parts              64
large part mass      3363923805  (9 parts)
small part mass      3363923804  (55 parts)
```

and preserves the exact total mass.

### Regime B — fragmented source list

Let the exact prepared shard contain the ordered source-record list

```text
S = [R_0, ..., R_{n-1}].
```

Partition that list into consecutive record chunks `C_j`. MATH-108 already audits initial source chunks independently and adds exact closed occurrence mass. Hence

```text
S = union_j C_j
```

at the source-record level, with no record deletion or alteration.

For MATH-154 shard 18,

```text
n = 2444 = 19*128 + 12,
```

so `source_chunk=128` gives exactly 20 initial chunks while retaining the unchanged shard source and unchanged MATH-108 transition arithmetic.

## Composition lemma

Suppose every exact subproblem produced by either decomposition satisfies all of the following under the unchanged MATH-108 engine:

1. its source metadata matches the frozen source partition;
2. the engine returns `PASS generalized exact AP-union audit`;
3. certified closed occurrence mass equals that subproblem's exact input occurrence mass;
4. the collection of subproblems has an exact partition certificate whose total source mass equals the parent shard mass.

Then the parent shard is exactly closed.

Applying this recursively across all 128 frozen MATH-117 shards gives a sufficient exact execution architecture for the complete `r=10` gate. This is a composition of already-audited exact partitions; it does not introduce a new arithmetic exclusion criterion.

## Current routing architecture

```text
prepared r=10 shard
|
|-- shard 0..13: giant-AP regime
|      -> MATH-156 exact K-way parameter microsharding
|      -> unchanged MATH-108 on every micro-AP
|
`-- shard 14..127: fragmented regime
       -> MATH-154-style source-record chunk scheduling
       -> unchanged MATH-108 on the unchanged source list
```

The current MATH-153 shard-0 run is the execution pilot for Regime A. MATH-154 shard 18 remains the prepared execution pilot for Regime B.

## What this does and does not prove

This lemma proves only that the two resource schedules can be composed without changing the frozen theorem-facing `r=10` source, provided every subproblem passes with exact mass accounting.

It does **not** assert that:

- every remaining microshard will pass;
- `source_chunk=128` is runtime-optimal;
- every fragmented shard will finish within the current timeout;
- `r=10` is closed;
- the first universal cell is empty;
- the Collatz conjecture is proved.

Runtime behavior remains an execution question. Mathematical closure is promoted only after complete exact certificates are available.