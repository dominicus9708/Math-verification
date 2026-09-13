# MATH-113 — remaining multi-paid workload landscape and count-width barrier

Status: `EXACT FINITE r=2..10 WORKLOAD AUDIT / REPRESENTATION BARRIER / NO CLOSURE CLAIM`

## Purpose

After MATH-110 (`r=12`) and MATH-112 (`r=11`) showed decreasing compressed source count but rapidly increasing represented ordinary-integer mass, the unchanged MATH-065 exact classifier/generator was applied to every remaining layer `r=10..2`.

The purpose is not to close these layers in advance. It is to determine the exact representation/resource landscape before choosing sharding or changing the engine.

## Exact landscape

| r | negative AP cylinders | represented occurrences | max multiplicity | multiplicity intervals |
|---:|---:|---:|---:|---:|
| 10 | 278,725 | 27,557,263,803,397 | 830,483,089,363 | 376 |
| 9 | 141,002 | 172,107,496,438,700 | 3,381,256,733,001 | 400 |
| 8 | 65,811 | 1,281,026,785,265,013 | 67,269,130,238,384 | 444 |
| 7 | 29,342 | 8,499,072,326,407,060 | 807,229,562,860,607 | 473 |
| 6 | 15,133 | 53,251,059,016,858,758 | 3,228,918,251,442,427 | 517 |
| 5 | 6,525 | 407,471,475,426,308,081 | 51,662,692,023,078,828 | 551 |
| 4 | 3,675 | 1,845,330,088,960,999,169 | 227,070,381,217,324,903 | 580 |
| 3 | 1,873 | 13,093,636,650,601,823,230 | 1,816,563,049,738,599,228 | 627 |
| 2 | 1,116 | 74,283,701,945,452,943,666 | 21,350,398,233,904,928,148 | 662 |

The classifier totals are also frozen in the result TSV and executable certificate.

## Main structural finding

Lower `r` is not a larger problem in source-record count.  It is a **more compressed** problem:

- the number of exact AP cylinders collapses from more than a million at `r=12` to only `1,116` at `r=2`;
- the ordinary-integer multiplicity represented by those cylinders grows to more than `7.4e19`.

Therefore ordinary-integer enumeration is increasingly inappropriate.  The proof-facing object must remain the exact AP union itself.

## Implementation barrier at r=2

The current MATH-108 generalized AP-union engine stores:

```cpp
using u64 = std::uint64_t;
struct AP { cpp_int a, b; u64 m; };
```

and also keeps occurrence-mass bookkeeping in `u64`.

For `r=3`, both the full occurrence mass and largest AP multiplicity remain below `2^64-1`.

For `r=2`:

```text
full occurrence mass   = 74,283,701,945,452,943,666
max AP multiplicity    = 21,350,398,233,904,928,148
2^64 - 1               = 18,446,744,073,709,551,615
```

Both exceed the representation range of the current engine.

This is an **implementation/representation barrier**, not a mathematical surviving candidate and not evidence against Collatz.

## Required repair before r=2

One of the following exact-equivalent representations is required:

1. widen AP multiplicity and occurrence-mass bookkeeping from `u64` to arbitrary-precision integer arithmetic; or
2. pre-partition every oversized AP into an exact union of sub-AP parameter intervals whose multiplicities fit the engine, while using arbitrary-precision total-mass bookkeeping.

The first route is cleaner because the AP transition algebra already operates on arbitrary-precision intercept and step values and does not enumerate all `m` members.

Any widened engine must be regression-tested on an already closed layer before being used as proof-facing evidence at `r=2`.

## Claim boundary

MATH-113 is an exact workload and representation audit only.

It does not close any of `r=2..10`, the first universal Farey cell, or the Collatz conjecture.
