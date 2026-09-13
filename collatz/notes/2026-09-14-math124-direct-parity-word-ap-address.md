# MATH-124 — direct parity-word AP address theorem

Status: `MAINLINE EXACT LEMMA / ADDRESS-PRESERVING DIRECT CYLINDER FORMULA / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

Use the shortcut Collatz map

```text
T(n)=n/2            for even n,
T(n)=(3n+1)/2       for odd n.
```

Let `w` be a parity word of length `d`. Let `q=q(w)` be its number of odd steps and let `c_w` be the exact affine correction from MATH-119:

```text
T^d(n) = (3^q n + c_w)/2^d
```

for every source integer realizing `w`.

## Unique source residue of a parity word

Because `3^q` is odd, it is invertible modulo `2^d`. The source residue compatible with `w` is

```text
r_w = -c_w * (3^q)^(-1) mod 2^d.
```

The standard shortcut recurrence gives a bijection

```text
parity words of length d  <->  source residues mod 2^d.
```

Thus `w` is realized exactly by integers

```text
n = r_w mod 2^d.
```

This statement is stronger than a final-divisibility heuristic: the recurrence defining `c_w` and `r_w` encodes the whole parity prefix.

## Direct address inside an odd-step AP

Let the exact source cylinder be

```text
P(a,b,m) = {a+b k : 0<=k<m},
```

with odd `b>0`.

Since `b` is invertible modulo `2^d`, word `w` corresponds to exactly one parameter residue

```text
kappa_w = (r_w-a) * b^(-1) mod 2^d.
```

Hence the exact compatible source parameters are

```text
k = kappa_w + 2^d s,
```

restricted to `0<=k<m`.

If `kappa_w>=m`, this word has no source occurrence. Otherwise its exact multiplicity is

```text
m_w = floor((m-1-kappa_w)/2^d)+1.
```

Its largest source parameter and source integer are

```text
k_max = kappa_w + 2^d(m_w-1),
n_max = a+b*k_max.
```

## Exact child AP after the whole word

Substitute `k=kappa_w+2^d s` into the affine iterate:

```text
T^d(a+b k)
 = (3^q(a+b*kappa_w)+c_w)/2^d + 3^q b s.
```

Therefore the entire word-cylinder maps directly to the exact AP

```text
P(A_w, B_w, m_w),
```

where

```text
A_w = (3^q(a+b*kappa_w)+c_w)/2^d,
B_w = 3^q b,
m_w = floor((m-1-kappa_w)/2^d)+1.
```

No ordinary integer enumeration and no repeated one-bit split are required to state this child exactly.

## Direct frozen-floor gate

The child AP is increasing because `B_w>0`. Therefore the whole word-cylinder closes at the frozen floor `LO=2^71` iff

```text
A_w + B_w(m_w-1) <= LO.
```

Equivalently, using the largest compatible source integer,

```text
3^q n_max + c_w <= 2^d LO.
```

This is exactly MATH-119 Gate B in direct address form.

## Resolution-depth consequence

For

```text
R = ceil(log2 m),
```

we have `2^R>=m`. Therefore at depth `R`, every parity word has

```text
m_w <= 1.
```

This recovers MATH-122/123 finite AP resolution directly from the address formula.

## Relation to MATH-108

MATH-108 obtains the same set by repeated exact parity splitting and optional AP merging. MATH-124 gives the unmerged direct-cylinder formula for an arbitrary common parity prefix.

This supplies a theorem-facing bridge:

```text
exact source AP
-> parity word descriptor (d,q,c_w)
-> exact parameter residue kappa_w
-> exact child AP
-> exact MATH-119 frozen-floor gate.
```

## Claim boundary

MATH-124 is an exact representation theorem. It does not prove that every feasible word-cylinder reaches the floor, and it closes no new paid layer by itself.
