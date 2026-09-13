# MATH-118 — layer-independent exact AP lineage lemma

Status: `MAINLINE REPRESENTATION LEMMA / EXACT / NO NEW PAID-LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Motivation

MATH-107 through MATH-117 show a recurring pattern as paid count `r` decreases:

- the number of compressed AP source records decreases strongly;
- AP multiplicities increase strongly;
- the downstream closure dynamics remain the same unchanged MATH-108 shortcut-map AP engine.

Therefore the correct common object is not occurrence mass alone, but the exact AP lineage under the shortcut map

```text
T(n) = n/2             if n is even,
T(n) = (3n+1)/2        if n is odd.
```

MATH-118 isolates the part of that dynamics that is completely independent of paid layer `r`.

## Lemma 1 — one-step parity AP decomposition

Let

```text
P(a,b,m) = {a+b*k : 0 <= k < m}
```

with `b>0`, `b` odd, and `m>=1`.

Because `b` is odd, the parity of `a+b*k` alternates with `k`. Split the parameter set into

```text
k = rho + 2j,   rho in {0,1}.
```

For each nonempty parity class, put

```text
base_rho = a + b*rho,
count_rho = floor((m-1-rho)/2)+1.
```

Then exactly:

- if `base_rho` is even,

```text
T(base_rho + 2*b*j)
= base_rho/2 + b*j,
```

so the child is `P(base_rho/2, b, count_rho)`;

- if `base_rho` is odd,

```text
T(base_rho + 2*b*j)
= (3*base_rho+1)/2 + 3*b*j,
```

so the child is `P((3*base_rho+1)/2, 3*b, count_rho)`.

Thus one odd-step AP produces at most two exact odd-step AP children.

## Lemma 2 — source-lineage parameter-mass conservation

Before the frozen-floor deletion `n<=2^71`, the two parity parameter classes are disjoint and exhaustive. Hence

```text
count_0 + count_1 = m.
```

This is a source-lineage statement. Different source APs may later map to overlapping ordinary integers, and MATH-108 may merge such overlaps as a set representation. Therefore `m` is not asserted to equal the cardinality of the normalized union after cross-source merging.

What is preserved is the exact parameter-lineage accounting used by the source partition certificate.

After deleting descendants that have reached the frozen floor, surviving parameter mass is nonincreasing.

## Lemma 3 — d-step parity-word representation

Fix a parity word `w` of length `d` containing `q(w)` odd steps.

For every source parameter class compatible with `w`, the `d`-step shortcut iterate has the affine form

```text
T^d(n) = (3^q * n + c_w) / 2^d
```

for an integer word constant `c_w`.

Restricting `k` to its exact residue class modulo `2^d` therefore turns the descendant family into an AP whose step is

```text
3^q * b.
```

The original AP is partitioned by the feasible parameter residues modulo `2^d`; their parameter counts sum to `m` before floor deletion.

This is the algebraic reason the MATH-108 engine can propagate a huge AP without enumerating all represented ordinary integers.

## Consequence — paid-layer independence of downstream dynamics

The paid layer `r` affects how MATH-065 constructs the initial exact negative-candidate AP source family. Once a source row

```text
target0, odd_step, count
```

has been emitted, the subsequent exact shortcut-map AP dynamics do not depend on `r`.

Hence the multi-paid closure problem separates into two mathematically distinct components:

```text
A. r-dependent exact source generation/classification;
B. r-independent AP-lineage closure dynamics.
```

MATH-110/MATH-112/MATH-113 already audit component A for `r=12..2`.
MATH-108/MATH-114/MATH-115/MATH-118 provide a common representation framework for component B.

## Why this matters for the remaining frontier

The observed growth in total represented occurrence mass as `r` decreases does not by itself imply proportional growth in closure complexity.

At one AP transition, the engine processes at most two parity children regardless of `m`. The important unresolved quantities are instead:

- intermediate normalized AP/singleton state count;
- number of exact resource splits;
- closure depth;
- whether a genuine nonclosing lineage appears.

For comparison, the already-closed `r=13` shard 0 reached:

```text
max_depth = 480
max_state = 999,768
STATE_CAP = 1,000,000
```

and still closed exactly after source/parameter splitting. Thus a near-cap state is not itself evidence of a mathematical obstruction.

## Candidate next theorem

MATH-118 does **not** yet provide a uniform closure theorem for `2<=r<=12`.

The next useful target is a layer-independent sufficient condition of the form

```text
AP state descriptor D
+ exact shortcut transition
=> a well-founded decrease after a bounded number of steps,
```

or an equivalent rank/potential function that is preserved under exact AP splitting and decreases on every surviving lineage.

Such a result could replace some or all layer-by-layer closure runs. It must be proved on the exact same-integer AP state; density, average drift, or occurrence-mass arguments are insufficient.

## Claim boundary

MATH-118 proves only the exact layer-independent AP lineage representation. It does not close `r=12`, `r=11`, `r=10`, any lower layer, the first universal Farey cell, or the Collatz conjecture.
