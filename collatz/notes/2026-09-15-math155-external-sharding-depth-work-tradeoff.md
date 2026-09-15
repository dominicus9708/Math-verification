# MATH-155 — exact external-sharding depth/work tradeoff

Date: 2026-09-15

## Status

`SUPPORT / EXACT RESOURCE-SCHEDULING LEMMA / NO LAYER CLOSURE CLAIM`

## Setting

Let one exact source AP have parameter multiplicity `m`, and let the MATH-108 state-record cap be

```text
C = 1,000,000.
```

MATH-144/MATH-148 use source occurrence mass as a sufficient upper bound on the number of current deterministic lineage records. Hence an isolated source AP of mass `M <= C` cannot trigger `TooBig` solely through the state-record cap.

Externally split the original AP into `K` consecutive exact parameter intervals. The largest micro-AP mass is

```text
M_K = ceil(m / K).
```

If the engine subsequently uses exact half-interval bisection, a sufficient internal depth is the least integer `d_K >= 0` satisfying

```text
ceil(M_K / 2^d_K) <= C.
```

Equivalently,

```text
d_K = max(0, ceil(log2(M_K / C)))
```

with the integer definition above authoritative at boundaries.

## r=10 giant-AP specialization

For MATH-143 giant shards,

```text
m = 215,291,123,465.
```

For power-of-two external splits `K=2^s`, `0<=s<=12`, exact integer arithmetic gives:

```text
K     max micro mass     sufficient internal depth   K*2^depth
1     215291123465       18                          262144
2     107645561733       17                          262144
4      53822780867       16                          262144
8      26911390434       15                          262144
16     13455695217       14                          262144
32      6727847609       13                          262144
64      3363923805       12                          262144
128     1681961903       11                          262144
256      840980952       10                          262144
512      420490476        9                          262144
1024     210245238        8                          262144
2048     105122619        7                          262144
4096      52561310        6                          262144
```

Thus, on this pure source-mass/state-cap worst-case bound,

```text
external split depth + internal sufficient depth = 18
```

and the corresponding worst-case total terminal-partition count `K*2^d_K` remains `2^18 = 262,144` throughout the table.

## Interpretation

External exact sharding does **not** strengthen the theorem and does not, by this worst-case bound alone, reduce total possible terminal partitions. Its guaranteed effect is to move exact bisection levels outside one job:

- shorter recursion depth per job;
- independent exact subproblems;
- parallel execution across runners;
- avoidance of a single-job timeout;
- possible reduction of repeated upper-tree prefix recomputation in MATH-108, which restarts child audits from depth 0 after `TooBig`.

The actual MATH-153 pilot is much better than the pure worst-case source-mass bound on the completed samples. With `K=64`, the first completed micro-APs use exactly `63` resource splits and `64` closure leaves, corresponding to six observed internal split levels rather than the sufficient worst-case bound of twelve. This empirical improvement is not promoted to a universal bound for the remaining micro-APs.

## Claim boundary

MATH-155 is a resource-scheduling lemma. It proves no Collatz descent, no `r=10` closure, no first-cell result, and no universal result.
