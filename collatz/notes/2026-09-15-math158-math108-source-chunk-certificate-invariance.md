# MATH-158 — MATH-108 `source_chunk` certificate invariance

Date: 2026-09-15

## Status

`SUPPORT / STATIC CODE AUDIT / EXACT CERTIFICATE-INVARIANCE LEMMA / NO LAYER CLOSURE CLAIM`

## Question

MATH-154 changes the MATH-108 invocation for a fragmented `r=10` shard from

```text
source_chunk = 2000
```

to

```text
source_chunk = 128.
```

The required audit question is whether this can change theorem membership or create a false closure certificate.

## Audited implementation

Authoritative engine:

```text
collatz/src/2026_09_13_math108_general_ap_union_engine.cpp
```

The source code fixes the following behavior.

### 1. Every input source record is ingested unchanged

Each TSV row is parsed as

```text
AP{a,b,m}
```

and contributes exactly one to `total_cylinders` and exactly `m` to `total_occurrences`.

The final assertions require

```text
total_cylinders == expected_cylinders
total_occurrences == expected_occurrences
```

so changing `source_chunk` cannot silently drop or add an input record.

### 2. `source_chunk` changes only initial batching

The input loop appends records to `chunk` and calls

```text
audit(std::move(chunk), stats)
```

when

```text
chunk.size() == source_chunk.
```

The final partial chunk is audited as well. Thus every source record is assigned to exactly one initial chunk for every positive `source_chunk`.

### 3. Resource recursion is exact partitioning

Inside `audit(raw, stats)`, if `TooBig` occurs and `raw.size()>1`, the original source-record list is split into two disjoint consecutive halves and both halves are recursively audited.

If one AP remains, its parameter interval is split exactly into two child APs with

```text
m1 + m2 == raw_mass
```

and both children are recursively audited.

Neither branch performs pruning.

### 4. Closure mass is additive and globally checked

A closure leaf adds exactly the current exact source partition's `raw_mass` to

```text
stats.closed_occurrence_mass.
```

After all initial chunks finish, `main()` requires

```text
stats.closed_occurrence_mass == total_occurrences.
```

Only then can the executable print

```text
PASS generalized exact AP-union audit
```

and return success.

## Lemma

For a fixed exact input TSV and fixed MATH-108 transition arithmetic, changing `source_chunk` to any positive value can alter runtime, merge opportunities, resource-split topology, closure-leaf count, and peak state size, but cannot by itself create a false `PASS` through omitted source mass.

A successful run still certifies the full input occurrence mass because:

1. the initial chunks form an exact partition of the source-record stream;
2. every recursive resource split is an exact partition;
3. every successful leaf contributes its exact input mass;
4. the final closed mass must equal the exact full input mass.

Therefore the MATH-154 change `2000 -> 128` is certificate-safe as a scheduling transformation.

## Important asymmetry

Smaller `source_chunk` may lose cross-chunk AP merging and may therefore be slower or require more work. It may also reduce repeated prefix recomputation and therefore be faster. This is an empirical runtime question.

However:

```text
PASS at source_chunk=128  => exact closure of the frozen input source
```

while

```text
timeout/failure-to-finish at source_chunk=128
```

does not imply mathematical non-closure.

## Relation to current r=10 frontier

- MATH-153/MATH-156: giant-AP external parameter microsharding.
- MATH-154: fragmented-shard `source_chunk=128` pilot.
- MATH-157: composition of the two exact scheduler regimes.
- MATH-158: static audit that the fragmented-regime `source_chunk` change preserves the MATH-108 full-mass certificate condition.

## Claim boundary

MATH-158 proves no new Collatz descent result, closes no new `r` layer by itself, and makes no first-cell or universal claim.