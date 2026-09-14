# MATH-144 — `r=10` single-AP shard resource bound

Date: 2026-09-15

## Status

`SUPPORT / EXACT ENGINE-RESOURCE LEMMA / NO r=10 CLOSURE CLAIM`

MATH-143 shows that MATH-117 shards `0..13` each consist of one exact AP with multiplicity

```text
m = 215,291,123,465.
```

MATH-108 uses `STATE_CAP = 1,000,000`. When `TooBig` occurs on a source partition containing one AP, `audit` bisects that AP's parameter interval exactly into two consecutive APs and recursively audits both halves.

## Record-count bound

For a source partition of occurrence mass `M`, each source occurrence has at most one current deterministic image at each shortcut depth, or has already fallen to the frozen floor and disappeared. Therefore the number of current lineage records represented as AP records plus unique singleton records cannot exceed `M`. Merging and singleton deduplication can only reduce that number.

Consequently,

```text
M <= STATE_CAP
```

is sufficient to rule out any further `TooBig` caused by the state-record cap for that exact source partition.

## `r=10` giant-shard bound

After `k` exact half-interval bisections, the largest descendant source mass is at most

```text
ceil(m / 2^k).
```

For the MATH-117 giant AP mass,

```text
ceil(215291123465 / 2^18) = 821271 < 1000000.
```

Therefore at most 18 levels of exact parameter bisection are sufficient to eliminate the MATH-108 `STATE_CAP` resource obstruction on every branch descending from each single-AP shard `0..13`.

## What remains

This is not a closure theorem. Once state-cap overflow is impossible, a branch could still fail the engine if its exact dynamics did not empty before `MAX_DEPTH = 1000`.

Thus the giant-shard interpretation is cleanly separated:

- resource-state explosion: finitely controlled by <=18 parameter-bisection levels;
- theorem-facing closure: still requires the actual exact AP-union trajectory to empty within the audited depth gate.

A slow single-AP shard is therefore not by itself evidence of a mathematical survivor.
