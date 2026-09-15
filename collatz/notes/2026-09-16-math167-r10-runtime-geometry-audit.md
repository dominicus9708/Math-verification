# MATH-167 — r=10 exact-closure runtime geometry audit

Date: 2026-09-16

## Scope

This is a scheduling/support audit only. It does not alter the represented integer sets, the exact MATH-108 closure semantics, the original-shard certificates, or any proof claim.

The sample compares completed exact `source_chunk=1` jobs from MATH-161 and MATH-162. All sampled jobs have exactly one input AP cylinder and the same occurrence mass:

```text
3,363,923,805
```

## Observed sample

```text
sample            wall_s    leaves  splits  max_depth  max_state
MATH161 sub 5     325.851      128     127        483     755300
MATH161 sub 7     623.022      128     127        472     755286
MATH161 sub 2     579.784      128     127        459     873408
MATH161 sub 11    649.291      128     127        413     785732
MATH162 micro 0   435.635       64      63        457     998653
```

Authoritative raw sample:

```text
collatz/results/2026-09-16-math167-r10-runtime-geometry-sample.tsv
```

## Result

`mass-balanced` is not equivalent to `runtime-balanced`.

Even among the four MATH-161 samples, occurrence mass, cylinder count, closure-leaf count, resource-split count, and source chunk are identical, while observed exact-closure wall time ranges from about 326 s to 649 s, almost a factor of two.

Neither `max_depth` nor `max_state` alone orders runtime. For example, subshard 11 has a smaller `max_depth` than subshard 5 but takes substantially longer; subshard 2 has a larger `max_state` than subshard 7 but finishes faster in this sample.

Therefore runtime depends on finer exact state-evolution geometry, including the AP start/step and the distribution of intermediate states, not merely represented occurrence mass.

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

MATH-167 proves no new Collatz statement and closes no additional `r=10` mass. It only demonstrates empirically, on exact completed jobs, that occurrence-mass balance is insufficient as a runtime model.
