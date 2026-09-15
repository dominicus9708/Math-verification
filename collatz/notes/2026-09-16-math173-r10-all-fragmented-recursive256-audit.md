# MATH-173 — all fragmented `r=10` recursive256 static geometry audit

Date: 2026-09-16

## Classification

`SIDE / SUPPORT ONLY`

MATH-173 tests whether the MATH-171 recursive256 fallback is a shard-18-specific construction or a uniformly viable exact scheduling refinement for all 114 fragmented original `r=10` shards `14..127`.

No MATH-108 closure is executed here. No original shard, `r=10` layer, first universal cell, or Collatz statement is closed by this audit.

## Exact source regeneration

The audit regenerates the frozen MATH-115 `r=10` source from the unchanged MATH-065/MATH-058R chain and verifies

```text
classification               994 = 91 safe + 396 singleton + 507 critical
AP source cylinders          278,725
represented occurrence mass 27,557,263,803,397
maximum multiplicity            830,483,089,363
```

It then applies unchanged MATH-114 to reconstruct the original 128-way `r=10` partition.

## Mandatory MATH-161 cross-check

Before any 256-way result is accepted, the script recursively repartitions every fragmented original shard into 64 subshards and requires the already-recorded MATH-161 aggregate exactly:

```text
source records/shard       2,427 .. 2,448
source mass                215,291,123,463 .. 215,291,123,464
recursive64 pieces         2,481 .. 2,494
cap                        3,363,923,805
mass spread                3 .. 6
max pieces/subshard        244
```

The regenerated calculation matched every one of these bounds.

## 256-way result across all 114 fragmented originals

For both fragmented source masses,

```text
cap256 = 840,980,952.
```

Across original shards `14..127`:

```text
source records/shard              2,427 .. 2,448
source mass                       215,291,123,463 .. 215,291,123,464
recursive256 pieces/shard         2,657 .. 2,669
full-cap prefixes/shard             219 .. 230
terminal remainders/shard         2,427 .. 2,448
split source rows/shard              12 .. 29
max pieces from one source           42 .. 220
subshard mass spread                  7 .. 10
min pieces/subshard                    1
max pieces/subshard                   68 .. 95
```

Global exact accounting across all 114 fragmented originals is

```text
fragmented occurrence mass      24,543,188,074,887
shard-local source rows                 278,725
full-cap prefix pieces                   25,229
recursive256 emitted pieces             303,954
```

No shard-local source multiplicity is an exact multiple of `840,980,952`; consequently every source row contributes exactly one terminal remainder and

```text
303,954 = 278,725 + 25,229.
```

## Worst static geometry

Original shard 14 is the strongest static fallback workload in this audit:

```text
source records                  2,427
source mass             215,291,123,464
recursive256 pieces             2,657
maximum source m       184,609,718,968
maximum pieces/source             220
subshard mass spread               10
maximum pieces/subshard            95
```

Thus the global worst `pieces/subshard` bound decreases from MATH-161's `244` at 64-way granularity to `95` at 256-way granularity, a reduction of about `61.07%`.

The occurrence-mass cap is simultaneously reduced from

```text
3,363,923,805 -> 840,980,952,
```

approximately one quarter.

## Interpretation

The 256-way fallback is not tailored to shard 18. Static exact geometry improves across all 114 fragmented original shards: every matrix workload is bounded by a much smaller occurrence cap, and the worst source-piece packing also falls materially.

This does **not** prove that every 256-way job will finish within 180 minutes. MATH-167 already shows that equal occurrence mass does not imply equal wall time. Runtime remains an execution property and exact closure remains an MATH-108 obligation.

Therefore the scheduling policy remains:

```text
healthy 64-way run -> continue it
resource timeout without mathematical FAIL -> recursive256 is an admissible exact fallback
unexecuted fallback -> no closure claim
```

## Reproducibility

Authoritative generator:

```text
collatz/src/2026_09_16_math173_r10_fragmented_recursive256_geometry_audit.py
```

Recorded summary:

```text
collatz/results/2026-09-16-math173-r10-fragmented-recursive256-summary.tsv
```

The script emits the complete per-original-shard TSV when run and contains frozen aggregate assertions for the values above.

## Claim boundary

MATH-173 is a scheduling/support result only. It certifies exact static partition geometry, not Collatz descent or original-shard closure.
