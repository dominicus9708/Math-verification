# MATH-108 regression accounting audit

Date: 2026-09-13

Status: `IMPLEMENTATION ACCOUNTING REPAIR / MATHEMATICAL PARTITION SEMANTICS UNCHANGED`

## Observed r=14 regression behavior

The earlier generalized-engine r=14 workflow processed the exact MATH-071 source stream successfully through the full AP-union audit and reached the final post-audit assertion. The only failure was

```text
assert(stats.source_parts == total_cylinders)
```

after approximately 55 minutes of exact closure computation.

No `depth limit exceeded`, uncaught `TooBig`, source-stream mismatch, or AP transition error occurred before that assertion.

## Why the assertion was wrong

A resource split of one AP

\[
P(a,b,m)
\]

into

\[
P(a,b,m_1)\cup P(a+b m_1,b,m_2),\qquad m_1+m_2=m,
\]

preserves the represented source set exactly, but changes the number of source AP records from one to two.

Therefore raw source-record count is not invariant under exact parameter bisection.

The additive invariant is input multiplicity mass

\[
\sum m.
\]

The engine was repaired to accumulate `closed_occurrence_mass` at successful closure leaves and require

```text
closed_occurrence_mass == total_occurrences
```

exactly.

## DSD audit

### SAFE

- source-record chunking is a disjoint partition of the input record stream;
- multi-record bisection is an exact partition of that stream;
- single-AP parameter bisection is an exact set identity;
- AP normalization/propagation logic is unchanged from the MATH-071 core;
- the new coverage invariant is additive under every resource split.

### INVALIDATED IMPLEMENTATION CHECK

The old `source_parts == total_cylinders` assertion is retired. It conflated original source-record identity with exact computational source partitions after parameter bisection.

### CLAIM BOUNDARY

This repair does not by itself close `r=13`. It repairs the executable regression/coverage accounting needed before promoting any new layer closure.

## Current execution gate

The exact `r=13` source stream is being partitioned into 16 disjoint source-record shards by record index modulo 16. Every shard independently runs the same generalized exact AP-union engine. A global `r=13` closure may be recorded only if all 16 shards pass and the union of their source records is checked to equal the complete MATH-107 source stream.
