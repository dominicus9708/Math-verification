# MATH-119 — layer-independent exact affine self-descent and frozen-floor gates

Status: `MAINLINE EXACT LEMMA / UNIFORM AFFINE GATES / NO NEW PAID-LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

Use the shortcut Collatz map

```text
T(n) = n/2              if n is even,
T(n) = (3n+1)/2         if n is odd.
```

Let `w` be an actually feasible parity word of length `d`, and let `q(w)` be the number of odd steps in `w`.

MATH-118 gives the exact affine form

```text
T^d(n) = (3^q n + c_w) / 2^d,
```

where `c_w` is a nonnegative integer determined only by the parity word.

## Exact recurrence for c_w

Starting from `(q,c,d)=(0,0,0)`, append one shortcut step.

If the appended step is even:

```text
q' = q,
c' = c.
```

If the appended step is odd:

```text
q' = q+1,
c' = 3c + 2^d.
```

This follows directly from

```text
(3 * ((3^q n + c)/2^d) + 1)/2
= (3^(q+1)n + 3c + 2^d)/2^(d+1).
```

## Gate A — exact self-descent criterion

For a fixed feasible word `w` and source integer `n>0`,

```text
T^d(n) < n
```

is equivalent to

```text
(2^d - 3^q) n > c_w.
```

Therefore:

1. if `2^d <= 3^q`, self-descent cannot be certified by this gate;
2. if `2^d > 3^q`, then self-descent is exact whenever

```text
n > c_w / (2^d - 3^q).
```

For an exact AP cylinder all of whose members share the same length-`d` parity word, testing the smallest member `n_min` is sufficient to prove **self-descent for every member**:

```text
(2^d - 3^q) n_min > c_w.
```

### Scope correction

Self-descent below the AP source member is **not by itself a MATH-108 closure certificate**.

The MATH-108 finite closure target is the frozen floor

```text
LO = 2^71,
```

and a source AP member may be an intermediate target rather than the original minimality reference. Therefore the earlier wording "discharge entire cylinder" from Gate A was too strong and is retired.

Gate A is an exact structural diagnostic unless an independent theorem supplies the relevant minimality reference.

## Gate B — exact frozen-floor closure criterion

The actual MATH-108 terminal condition is

```text
T^d(n) <= LO.
```

Using the affine form, this is exactly equivalent to

```text
3^q n + c_w <= 2^d LO.
```

For an exact AP cylinder whose members all share the same word `w`, the left side is increasing in `n`. Hence the **largest** source member `n_max` is sufficient and necessary for whole-cylinder floor closure at that prefix:

```text
3^q n_max + c_w <= 2^d LO.
```

Equivalently,

```text
n_max <= (2^d LO - c_w) / 3^q.
```

This is a genuine layer-independent exact closure gate aligned with the current engine semantics.

If it holds, every ordinary integer represented by that exact same-word AP cylinder is at or below the frozen verified floor after `d` shortcut steps.

## Why the correction term cannot be discarded

Both gates retain

```text
d   = shortcut depth,
q   = actual odd-step count,
c_w = exact affine correction.
```

The coefficient comparison `3^q < 2^d` alone is not a complete floor-closure criterion, and it is not even sufficient for Gate A unless the correction term is paid.

Thus MATH-119 does not use average drift, density, or a zero-correction approximation.

## Relation to MATH-108

MATH-108 already propagates exact AP cylinders. MATH-119 exposes theorem-facing affine terminal tests on the same exact lineage:

```text
exact same-word AP cylinder
-> affine descriptor (d,q,c_w)
-> Gate A: self-descent diagnostic using n_min
-> Gate B: frozen-floor closure using n_max
```

Gate B could be used as an exact early terminal certificate in a future engine without altering the correctness of already-running MATH-111/MATH-116 computations.

## Layer independence

The paid-count parameter `r` is used upstream to construct the exact source family. Once an AP cylinder and feasible shortcut word are fixed, neither Gate A nor Gate B contains `r`.

Therefore Gate B is a genuine common closure formula candidate for all remaining `r=11..2` layers.

## Remaining uniform-closure problem

MATH-119 does not prove that every surviving AP lineage reaches a finite prefix satisfying Gate B.

The sharpened common problem is:

```text
For every exact surviving source lineage in the remaining paid layers,
prove or certify that some finite same-word prefix w satisfies
3^q n_max + c_w <= 2^d * 2^71.
```

A future uniform theorem would need a well-founded bound on feasible exact `(d,q,c_w,n_max)` states, or an equivalent rank preserved under exact AP splitting.

## Claim boundary

MATH-119 supplies an exact common floor-closure test, not a proof that every source reaches the test. No new paid-count layer is closed by MATH-119 alone. The first universal Farey cell and Collatz conjecture remain subject to their separate coverage and reduction gates.
