# MATH-112 — exact r=11 workload and sharding plan

Status: `EXACT FINITE r=11 WORKLOAD AUDIT / r=11 OPEN / MAINLINE REPRESENTATION PIVOT`

## Exact arithmetic path

The unchanged MATH-065 classifier and negative-candidate cylinder generator are reused.  As an independent implementation check, the same exact arithmetic was reconstructed separately and first reproduced every frozen MATH-110 `r=12` core total exactly before being applied to `r=11`.

This is not an `r=11` closure certificate.

## Exact classifier

```text
1013 total cells
= 119 cost-safe
+ 414 singleton-resolution
+ 480 critical
```

## Exact negative-candidate stream

```text
branch-and-bound nodes          3,994,436
negative AP cylinders             605,972
represented occurrences     3,419,719,061,560
maximum AP multiplicity         51,905,193,085
occupied multiplicity intervals             343
```

Heavy tail:

```text
m >= 1,000              241,328 cylinders   3,419,677,356,627 occurrences
m >= 10,000             149,504 cylinders   3,419,293,778,624 occurrences
m >= 100,000             77,418 cylinders   3,416,001,689,360 occurrences
m >= 1,000,000           36,170 cylinders   3,397,436,981,913 occurrences
m >= 10,000,000          13,697 cylinders   3,307,517,564,955 occurrences
m >= 100,000,000          3,789 cylinders   2,970,493,671,360 occurrences
m >= 1,000,000,000          564 cylinders   2,001,769,706,501 occurrences
m >= 10,000,000,000          28 cylinders     574,823,013,486 occurrences
```

## Structural comparison

Relative to `r=12`, the number of AP source cylinders falls from `1,053,555` to `605,972`, while represented ordinary-integer mass rises from `580,472,268,528` to `3,419,719,061,560` and maximum single-cylinder multiplicity rises from `12,976,298,271` to `51,905,193,085`.

The trend therefore continues: lower paid count is not a smaller problem merely because the compressed source-record count decreases.  Multiplicity mass becomes increasingly concentrated in a small heavy tail.

## Proof-safe implementation partition

A record-index partition remains mathematically exact because MATH-108 established source-record and single-AP parameter bisection as exact set-union decompositions.

For the ordered exact `r=11` source stream, record index modulo 256 gives:

```text
256 shards
2,367 <= source records per shard <= 2,368
maximum shard occurrence mass = 61,047,101,694
```

The maximum is dominated by very large individual APs, so simply increasing the number of source-record shards cannot remove the heavy tail.  The generalized engine's exact single-AP parameter bisection must remain active.

## Acceptance gate for a future r=11 closure

1. independently certify the 256-way partition as disjoint and exhaustive;
2. conserve all `605,972` source cylinders and occurrence mass `3,419,719,061,560`;
3. run the same generalized exact AP-union dynamics used at `r=13` and currently at `r=12`;
4. preserve exact recursive source bisection and single-AP parameter bisection;
5. require every shard to pass the exact AP-union audit;
6. only then promote `r=11 CLOSED` under a later MATH claim.

## Claim boundary

MATH-112 fixes the exact finite workload and proof-safe scheduling plan only.

It does not establish `r=11 CLOSED`, first-cell emptiness, or the Collatz conjecture.
