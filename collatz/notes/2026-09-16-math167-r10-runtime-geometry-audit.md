# MATH-167 — r=10 exact-closure runtime geometry audit

Date: 2026-09-16

## Scope

This is a scheduling/support audit only. It does not alter the represented integer sets, the exact MATH-108 closure semantics, the original-shard certificates, or any proof claim.

The sample compares completed exact `source_chunk=1` jobs from MATH-161 and MATH-162. The jobs are single-AP exact workloads with occurrence mass approximately `3.364e9`.

## Observed sample

```text
sample              wall_s    leaves  splits  max_depth  max_state
MATH161 sub 5       325.851      128     127        483     755300
MATH161 sub 7       623.022      128     127        472     755286
MATH161 sub 2       579.784      128     127        459     873408
MATH161 sub 11      649.291      128     127        413     785732
MATH162 micro 0     435.635       64      63        457     998653
MATH161 sub 29      426.706      128     127        453     880176
MATH162 micro 21    501.181      128     127        489     827676
```

The first six mass-equal samples shown in the result table use `3,363,923,805`; MATH162 micro 21 uses `3,363,923,804`, a one-occurrence difference that is immaterial to the scheduling observation but is retained exactly in the raw table.

Authoritative raw sample:

```text
collatz/results/2026-09-16-math167-r10-runtime-geometry-sample.tsv
```

## Result

`mass-balanced` is not equivalent to `runtime-balanced`.

Even among MATH-161 single-AP jobs with identical occurrence mass, cylinder count, closure-leaf count, resource-split count, and source chunk, observed exact-closure wall time varies substantially.

Neither `max_depth` nor `max_state` alone orders runtime. The later completed samples strengthen that conclusion: MATH161 subshard 29 has `max_depth=453` and `max_state=880176` but finishes in about 427 s, while earlier subshard 11 has a smaller `max_depth=413` and smaller `max_state=785732` yet takes about 649 s.

MATH162 micro 21 also shows that increasing matrix index does not by itself imply monotone runtime growth: it closes with `128` leaves and `127` resource splits in about 501 s, still well inside the existing 180-minute job gate.

Therefore runtime depends on finer exact state-evolution geometry, including the AP start/step and the distribution of intermediate states, not merely represented occurrence mass or matrix position.

## Scheduling consequence

Future resource scheduling should preserve proof-neutral telemetry alongside every exact closure log:

```text
AP start / odd step
cylinders
occurrence mass
wall time
closure_leaves
resource_splits
max_depth
max_state
source_chunk
```

These values may guide recursive partition size and launch order. They must not be used as a pruning criterion, as a substitute for exact closure, or as evidence that an unexecuted shard closes.

## Claim boundary

MATH-167 proves no new Collatz statement and closes no additional `r=10` mass. It only demonstrates empirically, on exact completed jobs, that occurrence-mass balance and matrix position are insufficient as runtime models.
