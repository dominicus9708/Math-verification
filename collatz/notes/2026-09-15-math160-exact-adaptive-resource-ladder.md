# MATH-160 — exact adaptive resource ladder for the remaining `r=10` shards

Date: 2026-09-15

## Status

`SUPPORT / EXACT RESOURCE-SCHEDULING RULE / NO NEW CLOSURE CLAIM`

## Purpose

MATH-143 shows that the frozen MATH-117 `r=10` source has two sharply different runtime geometries under the same exact theorem partition:

1. giant single-AP shards, including original shards `0..13`;
2. fragmented many-record shards.

MATH-153 has now exactly closed original shard 0 with a 64-way external AP-parameter partition. MATH-154 is testing a smaller `source_chunk` on fragmented shard 18, and MATH-159 is independently testing the generic MATH-156 microsharder on giant shard 1.

This note fixes a deterministic escalation rule for future resource retries so that scheduling changes are not confused with mathematical pruning.

## Invariant source

For every original prepared shard, let `S` denote its frozen exact source and let

```text
M(S) = sum of represented occurrence multiplicities.
```

A scheduler is admissible only if it supplies an exact finite partition

```text
S = disjoint union_i S_i
```

at the represented ordinary-occurrence level and certifies

```text
sum_i M(S_i) = M(S).
```

No scheduler may change the Collatz transition, the frozen floor, `STATE_CAP`, `MAX_DEPTH`, AP membership, or the source occurrence mass.

## Regime A — giant single-AP shards

For one AP

```text
P(a,b,m) = {a + b*k : 0 <= k < m},
```

use the MATH-156 consecutive-parameter partition with a parts ladder

```text
64 -> 128 -> 256 -> 512 -> ...
```

only as needed after a resource timeout.

For `p` parts, write

```text
m = p*q + r,  0 <= r < p.
```

The children have masses `q+1` for exactly `r` parts and `q` for the remaining `p-r` parts, with consecutive offsets. Therefore

```text
P(a,b,m) = disjoint union_{j=0}^{p-1} P(a+b*s_j,b,m_j),
sum_j m_j = m.
```

Increasing `p` changes only external scheduling granularity.

### Acceptance rule

An original giant-AP shard is CLOSED only after:

1. the external partition certificate covers its full source mass exactly;
2. every child run returns `PASS generalized exact AP-union audit`;
3. every child log reports `closed_occurrence_mass == occurrences == certified child mass`;
4. the final child masses sum to the original shard mass.

A timeout at any parts value implies no mathematical non-closure.

## Regime B — fragmented many-record shards

Use the unchanged MATH-108 engine on the unchanged ordered source-record list with a source-chunk ladder

```text
128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
```

only as needed after a resource timeout.

For a fixed source file, `source_chunk` changes only the number of original records initially passed to one `audit()` call. Every record enters exactly one initial chunk. Inside `audit()`, a `TooBig` event causes exact source-list bisection; if one AP remains, the engine performs exact AP-parameter bisection.

MATH-108 accepts only if

```text
total_cylinders == expected_cylinders
total_occurrences == expected_occurrences
closed_occurrence_mass == total_occurrences.
```

Thus changing `source_chunk` cannot turn an uncovered source into a PASS.

### Acceptance rule

A fragmented original shard is CLOSED only if one exact scheduling attempt returns the full MATH-108 PASS for the unchanged shard source and exact expected occurrence mass.

A timeout merely advances the resource ladder and implies no survivor.

## Adaptive choice is not mathematical conditioning

The ladder may react to runtime events such as timeout, memory/state pressure, or excessive recomputation because every permitted rung represents the same frozen mathematical source.

The selection rule is therefore

```text
resource outcome -> equivalent exact representation
```

and never

```text
trajectory/property outcome -> delete or weaken candidates.
```

This distinction is required for every future retry record.

## What MATH-160 does not prove

MATH-160 does not prove that one of the finite listed scheduling rungs must finish within a given wall-clock budget. It also does not replace the execution obligation that every exact branch close before `MAX_DEPTH = 1000`.

MATH-148 gives a finite bound for removing a pure `STATE_CAP` obstruction by exact AP bisection, but runtime and depth closure remain separate obligations.

## Current application

- MATH-153: giant shard 0, 64 parts — exact CLOSED.
- MATH-159: giant shard 1, 64 parts via generic MATH-156 — running.
- MATH-154: fragmented shard 18, `source_chunk=128` — running.

If either running pilot times out without an exact mathematical failure certificate, the next admissible retry is determined by the corresponding ladder above rather than by modifying theorem conditions.

## Claim boundary

MATH-160 is a reproducibility and resource-control result. It creates no new `r=10` closure claim and no first-cell or Collatz claim.
