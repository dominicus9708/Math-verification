# MATH-122 — exact AP resolution/value rank

Status: `MAINLINE EXACT LEMMA / NON-SINGLETON WELL-FOUNDED RANK / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

Let one exact AP branch at the current shortcut time be

```text
P(a,b,m) = {a + b k : 0 <= k < m},
```

with odd `b>0` and multiplicity `m>=2`. Let

```text
N = max P = a + b(m-1).
```

Because `b` is odd, source parity alternates with parameter parity. Splitting by the next shortcut parity therefore sends a branch of size `m` to children whose multiplicities satisfy

```text
m' <= ceil(m/2) < m.
```

Hence

```text
R_m = ceil(log2 m)
```

drops by at least one on every unmerged branch refinement until the branch is a singleton.

## Integer resolution/value rank

Define

```text
V(N,m) = (N+1) m^2.
```

This is a positive integer.

### Odd child

For an odd source member,

```text
T(n)+1 = 3(n+1)/2.
```

Therefore the maximum of any odd child satisfies

```text
N' + 1 <= 3(N+1)/2.
```

Together with `m' <= ceil(m/2)`,

```text
V' <= (3/2)(N+1) ceil(m/2)^2.
```

For every integer `m>=2`,

```text
(3/2) ceil(m/2)^2 < m^2.
```

Thus `V'<V` on every odd child.

### Even child

For an even source member,

```text
T(n)=n/2,
```

so `N'+1 < N+1` for `N>0`, while also `m'<m`. Hence again

```text
V'<V.
```

Therefore `V=(N+1)m^2` is a strictly decreasing positive-integer rank on every non-singleton exact AP lineage.

## Exact finite-resolution consequence

Every unmerged AP lineage reaches multiplicity one after at most

```text
R_m = ceil(log2 m)
```

parity refinements.

Using the frozen maximum multiplicities of the remaining paid layers gives:

```text
r=11  max m=51,905,193,085             R_m<=36
r=10  max m=830,483,089,363            R_m<=40
r=9   max m=3,381,256,733,001          R_m<=42
r=8   max m=67,269,130,238,384         R_m<=46
r=7   max m=807,229,562,860,607        R_m<=50
r=6   max m=3,228,918,251,442,427      R_m<=52
r=5   max m=51,662,692,023,078,828     R_m<=56
r=4   max m=227,070,381,217,324,903    R_m<=58
r=3   max m=1,816,563,049,738,599,228  R_m<=61
r=2   max m=21,350,398,233,904,928,148 R_m<=65
```

Thus no remaining source AP can remain parity-unresolved for more than 65 unmerged refinement steps.

## Important distinction from MATH-108 merging

MATH-108 may merge compatible AP intervals after propagation as a computational compression. Such a merge can increase a stored AP multiplicity and therefore need not preserve the branch-local rank `R_m` or `V` record-by-record.

The lemma is about exact source lineages before optional merge compression. Merging changes representation, not the represented integer set.

## What this proves and does not prove

MATH-122 removes one possible infinite obstruction:

```text
an exact AP branch cannot remain forever unresolved in source-parameter parity.
```

It also controls value growth while resolution is being consumed, because `V` strictly decreases.

However when `m=1`, the rank reduces to `V=N+1`; an odd singleton shortcut can increase it. Therefore MATH-122 does not prove that the resulting singleton reaches `LO=2^71`.

The remaining common-closure problem is now split cleanly into:

1. finite AP resolution — solved by MATH-122;
2. frozen-floor descent of fully resolved or re-merged exact branches — still open and must use MATH-119/120 plus exact address/macro feasibility.

## Relation to finite future precision

If the source-size resolution is written as `R=ceil(log2 m)`, MATH-122 shows that the remaining paid layers require at most `R=65` bits of branch-resolution depth from their largest source APs. This is compatible with, but does not extend the scope of, the MATH-096 finite-future-precision rule `P(R)=73+R`.

No arbitrary-depth completeness claim is made.

## Claim boundary

No new paid layer is closed by MATH-122 alone. The first universal Farey cell and Collatz conjecture remain `OPEN`.
