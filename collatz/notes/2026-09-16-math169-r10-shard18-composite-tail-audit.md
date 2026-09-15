# MATH-169 — r=10 original shard 18 recursive64 composite-tail audit

Date: 2026-09-16

## Scope

This is a static scheduling/support audit of the exact MATH-161 recursive64 source certificate and preserved source artifact. It does not add a closure claim.

MATH-161 partitions original `r=10` shard 18 into 64 exact mass-balanced subshards. The partition has a sharp two-regime geometry.

## Regime A — single-AP front

Subshards `0..46` are 47 one-piece exact AP workloads:

```text
pieces per subshard   1
mass per subshard     3,363,923,805
number of subshards   47
combined mass         158,104,418,835
```

## Regime B — composite tail

Subshards `47..63` are 17 composite workloads:

```text
pieces per subshard   136..146
mass per subshard     3,363,923,801 or 3,363,923,802
number of subshards   17
combined pieces       2,444
combined mass         57,186,704,629
```

The row-level records are:

```text
collatz/results/2026-09-16-math169-r10-shard18-composite-tail.tsv
collatz/results/2026-09-16-math169-r10-shard18-composite-tail-detail.tsv
```

The additive mass check is exact:

```text
158,104,418,835 + 57,186,704,629 = 215,291,123,464.
```

This reproduces the original shard-18 occurrence mass exactly.

A notable structural coincidence is that the composite tail contains `2,444` prepared pieces, equal to the original shard-18 source-record count. This is a statement about counts in this exact partition only; it is not used as a source-record identity claim because MATH-114 may split source AP parameter intervals.

## Preserved-source geometry

The MATH-161 source artifact (`math161-r10-shard18-sub64-source`, artifact ID `10404997414`) was audited directly.

Across the 2,444 composite-tail pieces:

```text
distinct odd-step values    28
step form                    every observed step is exactly 3^q
observed q set               {21} union {23,...,49}
minimum step                 3^21 = 10,460,353,203
maximum step                 3^49 = 239,299,329,230,617,529,590,083
multiplicity-one pieces      258
maximum piece mass           3,302,008,528
pieces with mass >= 10^9     19
mass in those 19 pieces      34,089,607,502
fraction of tail mass        about 59.6110717%
```

Thus most tail source records are individually small, while a very small number of high-multiplicity pieces carry most represented occurrence mass. At the subshard level, `47..61` each contain one piece of mass at least `10^9`; subshards `62` and `63` each contain two such pieces.

Because MATH-161 invokes MATH-108 with `source_chunk=1`, a composite-tail job does not ingest its 136–146 pieces as one initial union state. Each exact source piece enters an independent initial audit in sequence inside the job. Consequently the tail runtime is a serial aggregate over heterogeneous AP start/step geometries, not a single `3.36e9`-mass AP workload.

## Interpretation

Occurrence mass is essentially flat across all 64 subshards, but source-record geometry is strongly bimodal:

```text
0..46   one exact AP each
47..63  136..146 heterogeneous exact AP pieces each
```

MATH-167 already shows that equal occurrence mass does not imply equal runtime. The direct source audit strengthens the scheduling conclusion: the composite tail must be treated as a distinct runtime regime rather than assumed to behave like the first 47 single-AP subshards.

The detailed geometry is diagnostic only. It is not a pruning rule and it does not allow extrapolation from completed single-AP front jobs to unexecuted tail pieces.

## Execution rule

MATH-161 remains authoritative. No tail subshard is declared closed from this static audit. Each of `47..63` must independently produce `PASS generalized exact AP-union audit`, and the final `certify-original-shard18` job must verify all 64 logs and the full exact mass before original shard 18 can be promoted to `CLOSED`.

If a composite-tail job later reaches a resource timeout, the exact fallback is further source-piece/parameter partitioning with additive coverage certificates. Such a retry would change scheduling only and would require its own complete exact certificate before any closure promotion.

## Claim boundary

MATH-169 is SIDE / SUPPORT only. It closes no new mass and proves no new Collatz statement.
