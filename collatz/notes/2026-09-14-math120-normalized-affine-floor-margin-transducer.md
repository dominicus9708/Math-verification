# MATH-120 — normalized affine frozen-floor margin transducer

Status: `MAINLINE EXACT REFORMULATION / LAYER-INDEPENDENT / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Motivation

MATH-119 gives the exact same-word affine form

```text
T^d(n) = (3^q n + c)/2^d
```

and the exact frozen-floor gate

```text
3^q n_max + c <= 2^d LO,
LO = 2^71.
```

The raw integers `2^d`, `3^q`, and `c` can become large. MATH-120 normalizes them without losing information relevant to the affine iterate or floor gate.

## Normalized state

Define

```text
z = 2^d / 3^q,
u = c / 3^q.
```

Then exactly

```text
T^d(n) = (n + u) / z.
```

The frozen-floor condition becomes

```text
n_max + u <= z * LO.
```

Thus the same-word affine dynamics relevant to closure can be represented by the exact rational pair `(z,u)` plus the branch source maximum `n_max`.

## Exact transition

Append one feasible shortcut parity step.

### Even step

Because `d` increases by one while `q,c` are unchanged,

```text
z' = 2z,
u' = u.
```

### Odd step

Using `q'=q+1` and `c'=3c+2^d`,

```text
z' = 2z/3,
u' = u + z/3.
```

Therefore the exact layer-independent normalized transducer is

```text
E: (z,u) -> (2z, u)
O: (z,u) -> (2z/3, u+z/3).
```

No paid-count parameter `r` appears.

## Frozen-floor margin

For a fixed exact source branch with largest original source member `n_max`, define

```text
F = z*LO - n_max - u.
```

Then

```text
F >= 0
```

is exactly equivalent to whole-branch frozen-floor closure at the current common parity prefix.

The margin has especially simple transitions.

### Even

```text
F' = F + z*LO.
```

### Odd

```text
F' = F - z*(LO+1)/3.
```

where `z` on the right side is the pre-step value.

Thus the floor-closure question becomes an exact two-variable weighted walk:

```text
z -> 2z             on E,
F -> F + z*LO,

z -> 2z/3           on O,
F -> F - z*(LO+1)/3.
```

Closure occurs exactly when `F>=0`.

## Branch-local source maximum

When an AP source is refined by a parity prefix, its parameter set becomes a smaller exact source subset. The strongest Gate-B test uses that branch's exact `n_max`.

Using the parent `n_max` remains a safe sufficient test but may be weaker. Therefore a future optimized certificate should carry the exact branch-local maximum or an equivalent exact AP endpoint.

## Relation to MATH-108

MATH-108 carries exact AP endpoints and step/count data and directly advances the represented sets. MATH-120 does not replace that certified engine.

It supplies a theorem-facing compressed descriptor for a common parity prefix that may support:

- early exact floor-closure tests;
- a uniform `r=11..2` rank search;
- comparison of closure difficulty across paid layers without ordinary-integer enumeration.

## Candidate rank problem

The remaining general theorem problem can now be stated more sharply:

```text
For every feasible exact AP branch from the remaining source families,
prove that the normalized margin F reaches F>=0 in finite time,
or find a stronger well-founded rank on (z,F,branch endpoint data).
```

An even step strictly raises `F`, while an odd step lowers it. Therefore `F` alone is not monotone. Any uniform rank must also control feasible parity structure through `z` and the exact source/address constraints.

This explicitly explains why an average-drift scalar is insufficient and identifies the minimum extra channel required by this affine reformulation.

## Claim boundary

MATH-120 is an exact reformulation, not a closure theorem. It closes no new paid layer by itself and does not change the `OPEN` status of the first universal Farey cell or the Collatz conjecture.
