# MATH-119 — layer-independent exact affine descent gate

Status: `MAINLINE EXACT LEMMA / UNIFORM DESCENT TEST / NO NEW PAID-LAYER CLOSURE CLAIM`

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

## Exact descent criterion

For a fixed feasible word `w` and source integer `n>0`,

```text
T^d(n) < n
```

is equivalent to

```text
(2^d - 3^q) n > c_w.
```

Therefore:

1. if `2^d <= 3^q`, descent cannot be certified by this word-level gate;
2. if `2^d > 3^q`, then descent is exact whenever

```text
n > c_w / (2^d - 3^q).
```

For an exact AP cylinder all of whose members share the same length-`d` parity word, it is enough to test the smallest source member `n_min`:

```text
(2^d - 3^q) n_min > c_w
```

because the left side is increasing in `n`.

Thus an entire AP cylinder can be discharged without enumerating its represented integers.

## Why this is stronger than an average-drift argument

The gate keeps all three exact quantities:

```text
d  = shortcut depth,
q  = actual odd-step count,
c_w = exact affine correction.
```

It does not replace `c_w` by zero and does not infer descent from `q/d` alone.

The familiar coefficient condition

```text
3^q < 2^d
```

is necessary for this positive-source affine gate but is not, by itself, the complete condition. The correction term must still be paid.

This avoids the forbidden upgrade

```text
negative average drift => every exact lineage descends.
```

## Relation to MATH-108

MATH-108 already propagates exact AP cylinders rather than ordinary integers. MATH-119 identifies a theorem-facing terminal test that can be inserted into the same exact lineage representation:

```text
exact AP state
-> common parity word / affine descriptor (d,q,c_w)
-> minimum-member descent inequality
-> discharge entire cylinder.
```

A future engine may use this as an early exact closure certificate. The current MATH-108 engine need not be modified for already-running MATH-111/MATH-116 certificates.

## Layer independence

The paid-count parameter `r` is used upstream to construct the exact source family. Once an AP cylinder and its feasible shortcut lineage are fixed, the MATH-119 gate contains no `r`.

Hence this is a genuine common formula candidate for all remaining `r=11..2` layers.

## Important limitation

MATH-119 does not prove that every surviving AP lineage will reach a depth `d` satisfying the inequality.

The remaining uniform-closure problem is now sharpened to:

```text
For every exact surviving source lineage in the remaining paid layers,
prove or certify that some finite prefix w satisfies
(2^d - 3^q)n_min > c_w.
```

This may still require finite exact computation, or a new well-founded bound on feasible `(d,q,c_w)` states.

## Claim boundary

No new paid-count layer is closed by MATH-119 alone. In particular, `r=11..2`, the first universal Farey cell, and the Collatz conjecture remain subject to their existing gates.
