# MATH-134 — r=11 exact batched D=27 remainder audit

Status: `MAINLINE FINITE AUDIT / EXACT D=27 REMAINDER / r=11 OPEN`

Date: 2026-09-14

## Purpose

MATH-133 showed that the exact dyadic parity recursion remains valid at D=27, but a monolithic scan of all 32 observed odd-step classes exceeded the local execution window because every class scans the full modulus `2^27`.

MATH-134 changes only the resource schedule. It keeps the same exact threshold ranks and exact cyclic remainder semantics, but partitions the 32 odd-step classes by descending raw remainder mass and processes them in independent batches.

Because odd-step classes are disjoint source rows, summing their exact remainder counts introduces no overlap.

## Execution audit

The prepared r=11 source contains exactly 32 distinct odd steps, all powers of 3. The first 24 classes were processed as three 8-class batches. The final 8 classes, whose total raw remainder mass is only 14,109, were processed as four 2-class batches to avoid memory-bandwidth contention.

Exact D=27 remainder result:

```text
first 24 classes exact new safe mass  3,583,578,466
last 8 classes exact new safe mass               67
---------------------------------------------------
exact D=27 remainder increment        3,583,578,533
```

This increment is pairwise disjoint from the D<=26 exact remainder certificates and from the MATH-131 complete-cycle increments, because MATH-133/134 count only residues whose D=27 threshold rank strictly improves over the best rank at all previous depths.

## Updated finite bound

Starting from the MATH-133 cumulative certified safe mass

```text
3,290,266,127,590
```

MATH-134 gives

```text
certified safe mass through D=27  3,293,849,706,123
uncertified tail                     125,869,355,437
safe fraction                         96.31930713689735%
```

The remaining tail is not a counterexample set. It is exactly source mass not yet discharged by the current correction-envelope/address certificates.

## Claim boundary

`96.3193071369%` exact safe mass does not imply `r=11 CLOSED`. MATH-116 remains the complete exact AP-union closure gate, while the MATH-129--134 chain is an independently auditable exact pruning route.

## Next target

The next depth is D=28. A monolithic `2^28 x 32-class` remainder scan is not the preferred route. The D=27 result shows that exact class batching is valid, so D=28 should either use a further memory-compressed batch implementation or switch to a direct tail-support representation that visits only unresolved address families.
