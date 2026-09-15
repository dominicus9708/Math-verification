# MATH-168 — generic exact gate for r=10 giant shards 3..13

Date: 2026-09-16

## Purpose

MATH-153, MATH-159, and the running MATH-162 treat original giant AP shards independently. MATH-163 identified two frozen giant-source step families:

```text
original shards 0..2   odd step = 3^19 = 1,162,261,467
original shards 3..13  odd step = 3^20 = 3,486,784,401
```

MATH-164 is the first dedicated shard-3 pilot for the second family. MATH-168 generalizes the same exact certificate architecture to any original shard in `3..13` after the shard-3 pilot is evaluated.

## Workflow

```text
.github/workflows/collatz-math168-r10-giant-step20-generic-microclosure.yml
```

The workflow is `workflow_dispatch` only. It is not launched by this record.

For each requested original shard it independently:

1. regenerates the frozen exact `r=10` source;
2. rebuilds the exact 128-way MATH-114 prepared source;
3. asserts that the selected original shard contains exactly one AP;
4. asserts occurrence mass `215,291,123,465` and odd step `3^20`;
5. splits that AP into 64 disjoint exact parameter intervals with MATH-156;
6. runs unchanged MATH-108 with `source_chunk=1` on every micro interval;
7. requires all 64 PASS logs and exact additive occurrence-mass coverage before certifying that one original shard.

Runtime telemetry is preserved separately from the exact certificate, following MATH-167. It cannot substitute for a closure PASS.

## Claim boundary

MATH-168 currently closes nothing because it has not been launched. Even a successful invocation closes only the requested original shard. It does not infer closure of sibling shards, the full `r=10` layer, the first universal Farey cell, or the Collatz conjecture.
