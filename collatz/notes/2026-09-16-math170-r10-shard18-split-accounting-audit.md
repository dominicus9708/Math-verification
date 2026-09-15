# MATH-170 — r=10 shard 18 recursive split-accounting audit

Date: 2026-09-16

## Scope

This is a representation/scheduling audit of MATH-161 using the exact MATH-114 partition algorithm and the preserved recursive64 source. It is not a closure claim.

MATH-114 computes

```text
cap = ceil(total occurrence mass / number of shards)
```

and splits every source AP into consecutive disjoint parameter intervals of multiplicity at most `cap`. The resulting pieces are then sorted by descending multiplicity and assigned by least-current-mass scheduling.

For original `r=10` shard 18:

```text
source records       2,444
recursive pieces     2,491
extra pieces            47
cap                 3,363,923,805
```

The preserved recursive source contains exactly 47 pieces whose multiplicity equals the cap, namely subshards `0..46`, each containing one such piece. No composite-tail piece has multiplicity equal to the cap.

Therefore the observed 47 cap-sized pieces account exactly for the 47-piece increase introduced by exact AP parameter splitting. At the count level, the remaining 2,444 non-cap pieces are the one terminal/remainder piece contributed by each original source record after all full-cap prefixes are removed. LPT scheduling subsequently distributes those terminal pieces across subshards `47..63`.

This is stronger than the numerical coincidence `tail pieces = source records`: it follows from the MATH-114 splitting rule together with the observed equality

```text
number of cap-sized pieces = total pieces - source records = 47.
```

It does not assert that the emitted tail file order preserves original source-record order; LPT scheduling deliberately changes placement.

## Exact witness from the largest source AP

The largest original shard-18 multiplicity is

```text
116,786,684,442.
```

For cap `3,363,923,805`:

```text
116,786,684,442 = 34 * 3,363,923,805 + 2,413,275,072.
```

The first 34 recursive subshards `0..33` are consecutive full-cap pieces with odd step

```text
3^21 = 10,460,353,203.
```

The exact next parameter-interval start after subshard 33 is

```text
4,225,529,956,779,630,822,332.
```

The preserved recursive source contains precisely the continuation

```text
start = 4,225,529,956,779,630,822,332
step  = 10,460,353,203 = 3^21
mass  = 2,413,275,072
```

inside subshard 52. Hence the largest original AP is explicitly witnessed as 34 full-cap intervals plus its exact residual interval.

## Consequence for runtime interpretation

Subshards `0..46` are saturated split prefixes extracted from high-multiplicity original APs. The composite tail `47..63` consists of residual/terminal pieces after these prefixes have been removed, mixed by LPT scheduling.

Thus the front/tail bimodality in MATH-169 is a direct consequence of the exact sharding algorithm, not an accidental feature of shard numbering.

This explains why occurrence mass can be nearly identical while runtime geometry differs sharply: equal shard mass is produced by combining very different exact source-piece structures.

## Claim boundary

MATH-170 changes no set and closes no new mass. Every MATH-161 subshard still requires its own exact MATH-108 PASS, and original shard 18 remains OPEN until the dependent final certificate succeeds.
