# MATH-165 — `r=10` fragmented recursive64 single-AP/core-tail geometry

Date: 2026-09-16

## Status

`SUPPORT / RESOURCE-GEOMETRY REFINEMENT / NO NEW CLOSURE CLAIM`

## Motivation

MATH-161 shows that every fragmented original shard `14..127` can be re-partitioned exactly into 64 nearly equal occurrence-mass subshards with cap `3,363,923,805` and within-original mass spread at most six.

The number of AP pieces inside each mass-balanced subshard is not uniform. This audit separates the single-AP core from the composite tail.

## Shard-18 exact geometry

The recursive MATH-114 partition of original shard 18 has 2,491 exact pieces and 64 subshards.

Subshards `0..46` are each exactly one AP:

```text
single-AP subshards       47 / 64
mass of each              3363923805
pieces in each            1
```

The remaining subshards `47..63` form the composite tail:

```text
composite subshards       17 / 64
pieces/subshard            136 .. 146
subshard mass              3363923801 .. 3363923802
largest AP piece           3302008528 down to 1100669509 by tail position
```

With MATH-161 execution fixed to `source_chunk=1`, every emitted AP piece is audited independently by unchanged MATH-108 and the subshard job sums exact closed occurrence mass.

## All fragmented original shards

The prior exhaustive MATH-161 geometry audit found `45..54` single-piece subshards out of 64 for every fragmented original shard. Therefore only `10..19` subshards per original are composite under the recursive64 schedule.

This means the fragmented workload has a dominant single-AP component at the same occurrence-mass scale already validated by MATH-153/MATH-159 giant-AP microclosures, plus a smaller composite tail whose exact records are individually no larger than the same cap.

## Diagnostic consequence

If a recursive64 original-shard run does not complete uniformly, classify failures separately:

```text
A. single-AP subshard failure/timeout
B. composite-tail subshard failure/timeout
```

Do not treat them as one resource phenomenon.

If A succeeds broadly and B alone remains slow, subsequent refinement should target only the composite tail while preserving the already certified single-AP coverage. Any refinement must retain the exact AP set identities and complete occurrence-mass accounting required by MATH-160.

## Claim boundary

This is a resource-geometry classification only. It neither closes shard 18 nor any other fragmented original shard. MATH-161 final closure still requires all 64 subshard PASS logs and the dependent complete original-shard certificate.
