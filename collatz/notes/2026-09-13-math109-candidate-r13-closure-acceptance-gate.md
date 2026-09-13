# MATH-109 candidate — exact r=13 closure acceptance gate

Date: 2026-09-13

Status: `ACCEPTANCE GATE ONLY / NO r=13 CLOSURE CLAIM YET`

This file fixes the conditions under which the running 16-shard computation may be promoted to MATH-109.

## Required source identity

The exact MATH-107/MATH-108 r=13 source stream must contain

- `1,959,535` AP cylinders;
- multiplicity mass `76,391,629,325` ordinary occurrences.

The independent partition certificate must verify that record-index residue classes modulo 16 are disjoint and exhaustive and that their totals sum exactly to these two values.

## Required per-shard conditions

For every shard `s=0,...,15`:

1. the exact r=13 source exporter passes unchanged MATH-065 classification gates;
2. shard selection is exactly `i mod 16 = s` on source-record index `i`;
3. the generalized AP-union engine receives the shard's exact cylinder count and multiplicity mass;
4. the engine terminates with `PASS generalized exact AP-union audit`;
5. the final exact invariant is

```text
closed_occurrence_mass == shard_occurrence_mass
```

6. no depth-limit exception, source mismatch, overflow, or uncovered resource split occurs.

## Global acceptance condition

Only if all sixteen shard jobs satisfy the per-shard conditions and the partition certificate passes may the project record

```text
r=13 CLOSED
```

for the current exact multi-paid first-cell calculation.

At that point, and only then, the identifier `MATH-109` may be assigned to the closure result.

## DSD audit boundary

Even if accepted, MATH-109 would imply only that the `r=13` multi-paid layer is closed within the current exact first-cell minimal-counterexample framework.

It would NOT imply:

- closure of `2<=r<=12`;
- closure of all paid-count layers;
- first universal Farey cell emptiness;
- later Farey-cell closure;
- the Collatz conjecture.

## Failure classification

A failed shard must be classified before any retry:

- `MATHEMATICAL / REPRESENTATION FAILURE`: exact state survives past the certified depth or an asserted set identity fails;
- `IMPLEMENTATION FAILURE`: code/assertion error not corresponding to a mathematical predicate;
- `RESOURCE FAILURE`: runner time/memory/state cap issue with exact source coverage preserved.

Resource or implementation failure is not mathematical non-closure and must not be reported as a Collatz counterexample or as evidence of divergence.
