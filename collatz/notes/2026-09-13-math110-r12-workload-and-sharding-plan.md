# MATH-110 — exact r=12 workload and sharding plan

Status: `EXACT FINITE r=12 WORKLOAD AUDIT / r=12 OPEN / MAINLINE REPRESENTATION PIVOT`

## Scope

This note freezes the exact `r=12` multi-paid workload obtained by reusing the unchanged MATH-065 classifier and negative-candidate AP-cylinder generator.

It is not an `r=12` closure certificate. The first universal Farey cell and the Collatz conjecture remain open.

## Exact classifier

```text
1013 total cells
= 126 cost-safe
+ 457 singleton-resolution
+ 430 critical
```

## Exact negative-candidate stream

```text
branch-and-bound nodes          8,278,602
negative AP cylinders           1,053,555
represented occurrences       580,472,268,528
maximum AP multiplicity        12,976,298,271
occupied multiplicity intervals          305
```

Heavy-tail exact counts:

```text
m >= 1,000           271,732 cylinders   580,373,566,138 occurrences
m >= 10,000          145,303 cylinders   579,804,318,984 occurrences
m >= 100,000          65,979 cylinders   576,712,999,139 occurrences
m >= 1,000,000        24,175 cylinders   562,035,216,524 occurrences
m >= 10,000,000        6,347 cylinders   507,000,843,603 occurrences
m >= 100,000,000       1,118 cylinders   368,990,167,363 occurrences
m >= 1,000,000,000        75 cylinders   141,078,443,336 occurrences
```

## Comparison with r=13

The `r=12` source has fewer AP cylinders than `r=13`, but its represented ordinary-integer mass is much larger and the largest single-cylinder multiplicity rises from `687,142,557` at `r=13` to `12,976,298,271` at `r=12`.

Therefore source-record count alone is not an adequate resource proxy. The exact closure engine remains mathematically valid under source and parameter bisection, but a finer source partition is prudent for implementation scheduling.

## Sharding decision

Use an exact 128-way source-record partition by record index modulo 128:

```text
shard(i) = i mod 128.
```

This is an implementation partition only. It does not change theorem state, AP dynamics, ordinary-integer membership, or the closure criterion.

Before accepting an `r=12` closure claim:

1. certify the 128 shards are disjoint and exhaustive over all `1,053,555` source records;
2. certify the sum of shard occurrence masses is exactly `580,472,268,528`;
3. run the same generalized exact AP-union engine used for the audited `r=13` closure on every shard;
4. require every shard to emit `PASS generalized exact AP-union audit`;
5. require exact occurrence-mass accounting inside every shard;
6. only then promote the layer to `r=12 CLOSED` under a new MATH claim.

## Claim boundary

MATH-110 establishes exact finite workload structure and a proof-safe implementation partition plan only.

It does **not** establish:

- `r=12 CLOSED`;
- first-cell emptiness;
- the Collatz conjecture.
