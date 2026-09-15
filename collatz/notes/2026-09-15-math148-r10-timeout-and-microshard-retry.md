# MATH-148 — `r=10` timeout diagnosis and exact microshard retry

Date: 2026-09-15

## Status

`MAINLINE RESOURCE RETRY / EXACT SET-PRESERVING SPLIT / NO r=10 CLOSURE CLAIM`

## What happened in MATH-117 attempt 1

Run `34881179736` successfully completed:

- exact `r=10` source export,
- MATH-114 mass-balanced source preparation,
- partition certificate audit,
- prepared-shard artifact upload.

The first shard wave then entered the unchanged MATH-108 exact AP-union closure step. The running shard jobs were cancelled after approximately 180 minutes, exactly matching the workflow job setting `timeout-minutes: 180`.

For shard 0, the decoded job log shows:

```text
SHARD 0 pieces 1 mass 215291123465 u64_safe 1
...
The operation was canceled.
```

No `FAIL`, surviving state, depth-limit exception, or contradictory arithmetic output was observed. Attempt 1 is therefore a resource-timeout result, not a mathematical non-closure result.

## Why external microsharding is materially different

MATH-108 handles `TooBig` by recursively splitting the **original source partition** and then calling `audit` again from depth 0. For a single giant AP, repeated state-cap overflows can therefore recompute shared prefix evolution many times.

MATH-143 shows shards `0..13` are each exactly one AP with multiplicity

```text
m = 215291123465.
```

MATH-144 gives the pure state-cap bound of at most 18 internal half-split levels for such an AP.

Instead, split the original AP before entering the engine. For an exact 64-way consecutive parameter partition,

```text
215291123465 = 9 * 3363923805 + 55 * 3363923804.
```

Thus every micro-AP has multiplicity at most `3,363,923,805`, and

```text
ceil(3363923805 / 2^12) = 821271 < 1000000.
```

So the pure state-cap half-split depth after each micro-AP enters MATH-108 is bounded by 12 rather than 18.

## Exactness

For the original AP `P(a,b,m)`, choose consecutive offsets `s_j` and lengths `m_j` with `sum m_j=m`. Then

```text
P(a,b,m) = disjoint union_j P(a+b*s_j,b,m_j).
```

This is the same set identity used by MATH-108/MATH-114. No ordinary integer is added, removed, or duplicated.

## Pilot gate

The first pilot targets original MATH-117 shard 0 only.

1. Regenerate the exact `r=10` source and exact MATH-114 128-way prepared shards.
2. Assert shard 0 has exactly one AP and mass `215291123465`.
3. Split that AP into exactly 64 consecutive micro-APs as above.
4. Assert the 64 micro masses sum exactly to the original shard mass.
5. Run the unchanged MATH-108 engine independently on each micro-AP.
6. Require `PASS generalized exact AP-union audit` on all 64 jobs.
7. Aggregate the 64 certified masses and require exact equality with `215291123465`.

If all 64 pass, original shard 0 is CLOSED under the unchanged theorem-facing AP dynamics, but `r=10` remains OPEN until every original source shard is covered.

## Claim boundary

This retry changes resource scheduling only. A timeout is not promoted to evidence of a survivor, and a successful shard-0 pilot is not promoted to `r=10 CLOSED`.
