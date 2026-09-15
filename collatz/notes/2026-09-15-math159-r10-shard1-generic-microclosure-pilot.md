# MATH-159 — `r=10` original shard 1 generic exact microclosure pilot

Date: 2026-09-15

## Status

`SUPPORT / EXACT GIANT-AP GENERALIZATION PILOT / RUNNING / NO r=10 LAYER CLOSURE CLAIM`

Workflow run: `34962500310`

## Motivation

MATH-153 exactly closed original `r=10` shard 0 by a 64-way consecutive parameter partition. MATH-143 shows original shards `0..13` share the same giant-single-AP geometry class. MATH-156 then generalized the exact single-AP partition into a reusable script.

MATH-159 tests that generalization on the next independent giant AP, original shard 1.

## Exact source

The workflow regenerates the frozen MATH-115/MATH-114 `r=10` prepared source and selects

```text
/tmp/r10-shards/shard-001.tsv
```

MATH-143 establishes that shards `0..13` each contain exactly one prepared AP piece with multiplicity equal to the shard cap

```text
215291123465.
```

## Exact external partition

The workflow calls

```text
collatz/src/2026_09_15_math156_exact_single_ap_microsharder.py
```

with

```text
parts = 64
expected_mass = 215291123465.
```

MATH-156 constructs consecutive parameter intervals

```text
P(a,b,m) = disjoint union_j P(a+b*s_j,b,m_j)
```

with exact mass conservation and child masses differing by at most one.

## Closure gate

Each of the 64 exact micro-APs is audited independently by the unchanged MATH-108 engine with `source_chunk=1`.

The final dependent job succeeds only if every micro log exists and contains

```text
PASS generalized exact AP-union audit
occurrences=<certified micro mass>
closed_occurrence_mass=<certified micro mass>
```

and the 64 certified masses sum exactly to

```text
215291123465.
```

## Interpretation

A successful MATH-159 run closes original shard 1 and provides an independent execution validation of the MATH-156 generic microsharder beyond shard 0.

It does not by itself close any other original shard or the full `r=10` layer.
