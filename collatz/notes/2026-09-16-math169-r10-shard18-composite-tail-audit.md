# MATH-169 — r=10 original shard 18 recursive64 composite-tail audit

Date: 2026-09-16

## Scope

This is a static scheduling/support audit of the exact MATH-161 recursive64 source certificate. It does not add a closure claim.

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

The complete row-level record is:

```text
collatz/results/2026-09-16-math169-r10-shard18-composite-tail.tsv
```

The additive mass check is exact:

```text
158,104,418,835 + 57,186,704,629 = 215,291,123,464.
```

This reproduces the original shard-18 occurrence mass exactly.

A notable structural coincidence is that the composite tail contains `2,444` prepared pieces, equal to the original shard-18 source-record count. This is a statement about counts in this exact partition only; it is not used as a source-record identity claim because MATH-114 may split source AP parameter intervals.

## Interpretation

Occurrence mass is essentially flat across all 64 subshards, but source-record geometry is strongly bimodal:

```text
0..46   one exact AP each
47..63  136..146 exact AP pieces each
```

MATH-167 already shows that equal occurrence mass does not imply equal runtime. Therefore the composite tail must be treated as a distinct runtime regime rather than assumed to behave like the first 47 single-AP subshards.

## Execution rule

MATH-161 remains authoritative. No tail subshard is declared closed from this static audit. Each of `47..63` must independently produce `PASS generalized exact AP-union audit`, and the final `certify-original-shard18` job must verify all 64 logs and the full exact mass before original shard 18 can be promoted to `CLOSED`.

## Claim boundary

MATH-169 is SIDE / SUPPORT only. It closes no new mass and proves no new Collatz statement.
