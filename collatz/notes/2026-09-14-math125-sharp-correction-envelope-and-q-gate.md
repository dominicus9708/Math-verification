# MATH-125 — sharp affine-correction envelope and odd-count floor gate

Status: `MAINLINE EXACT LEMMA / ADDRESS-FORGOTTEN SAFE GATE / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

For a parity word `w` of length `d` with `q` odd shortcut steps, write

```text
T^d(n) = (3^q n + c_w)/2^d.
```

Let the odd positions be

```text
0 <= j_1 < j_2 < ... < j_q <= d-1.
```

Then the exact correction is

```text
c_w = sum_{i=1}^q 3^(q-i) 2^(j_i).
```

## Sharp correction envelope

For fixed `(d,q)`, the minimum occurs when the odd positions are the earliest possible positions

```text
j_i = i-1,
```

and equals

```text
c_min(d,q) = 3^q - 2^q.
```

The maximum occurs when the odd positions are the latest possible positions

```text
j_i = d-q+i-1,
```

and equals

```text
c_max(d,q) = 2^(d-q)(3^q-2^q).
```

Thus for every parity word with exactly `q` odd steps,

```text
3^q-2^q <= c_w <= 2^(d-q)(3^q-2^q).
```

Both bounds are attained, so the envelope is sharp over the full parity-word class.

For `q=0`, `c_w=0`.

## Uniform frozen-floor gate for a whole odd-count class

Let `N` be a valid upper bound on the source maximum for the branch family under consideration. Then every length-`d` word with exactly `q` odd steps satisfies

```text
T^d(n) <= 3^q N / 2^d + c_max(d,q)/2^d.
```

Using the closed form for `c_max`,

```text
T^d(n) <= (3^q/2^d) N + (3/2)^q - 1.
```

Therefore the exact safe sufficient condition

```text
(3^q/2^d) N + (3/2)^q - 1 <= LO,
LO=2^71,
```

closes **every** parity word of length `d` with `q` odd steps for every source `n<=N`.

Equivalently in integer arithmetic,

```text
3^q N + 2^(d-q)(3^q-2^q) <= 2^d LO.
```

## Monotone odd-count threshold

For fixed `d` and `N>0`, the upper envelope

```text
U(d,q;N) = (3^q/2^d) N + (3/2)^q - 1
```

is strictly increasing in `q`.

Hence there is a largest safe odd count

```text
Q_safe(d,N)
```

such that every word with

```text
q <= Q_safe(d,N)
```

closes at depth `d` without any exact-address inspection.

Only the high-odd-count tail

```text
q > Q_safe(d,N)
```

requires the MATH-124 direct address calculation and exact MATH-119 floor gate.

## Role in the remaining layers

This yields a hybrid theorem-facing decomposition:

```text
source AP
-> choose common depth d
-> low/intermediate q classes: close by MATH-125 envelope
-> high-q tail: retain exact MATH-124 parameter residue
-> apply exact MATH-119/MATH-120 floor test.
```

This does not contradict the MATH-095 scalar barrier. MATH-125 is only a one-sided safe gate; it does not claim that high-q words are realizable or that the coarse `(d,q)` descriptor is complete.

## Claim boundary

MATH-125 closes no paid layer by itself. It is a sharp address-forgotten pruning lemma intended to reduce the exact-address tail in the remaining `r=11..2` work.
