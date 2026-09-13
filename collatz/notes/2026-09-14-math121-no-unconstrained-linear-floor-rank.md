# MATH-121 — no unconstrained positive-deficit linear floor-rank

Status: `EXACT BARRIER / RANK-DESIGN CONSTRAINT / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

From MATH-120, while a branch is still above the frozen floor define

```text
LO = 2^71,
D = -F > 0.
```

The exact normalized transitions are

```text
E: (D,z) -> (D - z*LO, 2z),
O: (D,z) -> (D + z*(LO+1)/3, 2z/3).
```

Consider a linear candidate rank that is positively oriented with the unresolved floor deficit,

```text
R(D,z) = a D + b z,
a > 0.
```

## Exact increment test

For an even step,

```text
Delta_E R = z(-a*LO + b).
```

For an odd step,

```text
Delta_O R = z(a*(LO+1) - b)/3.
```

To force strict decrease under every unconstrained even and odd step, one would need simultaneously

```text
b < a*LO,
b > a*(LO+1).
```

These inequalities are incompatible.

Therefore no linear rank of the form

```text
R = aD + bz,
with a>0,
```

can decrease under both raw shortcut transitions without using additional feasibility information.

## Interpretation

This does not prove that no useful rank exists.

It proves that any useful common rank must use at least one of:

- exact parity/address feasibility;
- a macro transition rather than a single shortcut step;
- AP resolution/multiplicity information;
- a nonlinear state function.

This is consistent with the earlier MATH-095 barrier: scalar phase/resolution information without exact address was insufficient.

## Claim boundary

MATH-121 is a negative structural result. It closes no paid layer and makes no claim about the first universal Farey cell or the Collatz conjecture.
