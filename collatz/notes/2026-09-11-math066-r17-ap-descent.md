# MATH-066 — r=17 arithmetic-progression descent reduction

Date: 2026-09-11

Status: `PARTIAL EXACT r=17 CLOSURE / SINGLETONS CLOSED / MULTIPLICITY>=1024 CLOSED / 2..1023 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-065 closes every multi-paid layer `r>=18`.
- This note begins the next layer `r=17` without materializing tens of millions of ordinary targets.

## 1. Exact r=17 workload

Applying the unchanged MATH-065 phase/address classification gives

\[
\boxed{
1090
=256\text{ cost-safe}
+596\text{ singleton-resolution}
+238\text{ multi-source critical}
}
\]

phase/address cells.

The exact dyadic branch-and-bound visits

\[
\boxed{42,482,287}
\]

prefix states and leaves

\[
\boxed{1,728,083}
\]

completed cylinders whose lower adjusted cost can still be below

\[
\lambda_* = \frac{19}{503}.
\]

If all of those cylinders are naively materialized, they contain

\[
\boxed{38,457,239}
\]

ordinary target occurrences.

The target range is

\[
\boxed{
2,361,183,794,064,906,256,279
\le n\le
6,290,338,245,370,917,570,478.
}
\]

The upper endpoint is about `2.6641 * 2^71`, so the layer cannot be closed by a trivial floor comparison.

## 2. Why ordinary-target materialization stops being the right resolution

MATH-065 could still materialize every surviving target for `r>=18`.  At `r=17`, doing that would discard the arithmetic structure already present in each completed cylinder.

A completed cylinder has the exact form

\[
\boxed{
P(a,b,m)=\{a+bk:0\le k<m\},
}
\]

where `b` is an odd power of `3`.

Because `b` is odd, parity of `a+bk` is determined by parity of `k`.  Splitting

\[
k=\rho+2s,\qquad \rho\in\{0,1\},
\]

preserves the arithmetic-progression form under one shortcut Collatz step.

If the selected branch is even,

\[
\boxed{
\frac{a+b\rho}{2}+bs.
}
\]

If it is odd,

\[
\boxed{
\frac{3(a+b\rho)+1}{2}+3bs.
}
\]

Therefore exact shortcut continuation forms a semigroup on finite arithmetic-progression cylinders.  No probabilistic or density argument is involved.

## 3. Floor trimming is also exact

For `b>0`, values in `P(a,b,m)` are increasing in `k`.

Hence those already satisfying

\[
a+bk\le2^{71}
\]

form one initial subinterval of the parameter range and may be removed exactly.  Only the remaining suffix is propagated.

This gives a direct family-level analogue of the MATH-065 ordinary-target descent check.

## 4. Complete singleton closure

Among the `1,728,083` negative-candidate cylinders,

\[
\boxed{1,013,728}
\]

have multiplicity exactly one.

Every such ordinary target was continued with the same memoized shortcut descent used in MATH-065.

All reach

\[
\le2^{71},
\]

with maximum additional shortcut length

\[
\boxed{258}.
\]

Thus the complete singleton part of the `r=17` layer is closed.

## 5. Large arithmetic-progression closure

Next retain every negative-candidate cylinder with

\[
\boxed{m\ge1024}
\]

as one arithmetic progression rather than materializing its members.

There are only

\[
\boxed{4,086}
\]

such cylinders, but together they represent

\[
\boxed{17,143,582}
\]

ordinary target occurrences.

Exact AP propagation closes every one of them.

The aggregate calculation uses

\[
\boxed{22,556,393}
\]

AP transition nodes in total.

The largest individual family requires

\[
\boxed{130,273}
\]

aggregate nodes, the maximum simultaneous live-family count is

\[
\boxed{8,048},
\]

and the deepest completed family requires

\[
\boxed{341}
\]

shortcut levels.

This is a genuine compression: the largest starting cylinder contains `170,462` ordinary targets, yet it is verified without separately launching `170,462` ordinary trajectories.

## 6. Current exact r=17 split

The two completed tracks account for

\[
1,013,728+17,143,582
=\boxed{18,157,310}
\]

target occurrences.

The unresolved part is therefore

\[
\boxed{710,269}
\]

negative-candidate cylinders representing

\[
\boxed{20,299,929}
\]

target occurrences, with multiplicities restricted to

\[
\boxed{2\le m\le1023}.
\]

Consequently

\[
\boxed{r=17\text{ is not yet closed}.}
\]

The correct next problem is no longer the full `38,457,239`-target enumeration.  It is the medium-multiplicity AP range `2..1023`.

## 7. DSD audit

### SAFE

1. The MATH-065 same-integer dyadic lineage is retained through cluster completion.
2. A completed target family is kept as an exact arithmetic progression.
3. Shortcut parity splitting is exact because the progression step is odd.
4. Both child branches remain exact arithmetic progressions.
5. Floor trimming removes only values already at or below the frozen verified floor.
6. All `1,013,728` singleton cylinders are directly closed.
7. All `4,086` cylinders with multiplicity at least `1024` are directly closed as AP families.

### OPEN

1. `r=17` multiplicities `2..1023`.
2. Paid counts `2..16`.
3. Mixed one-paid / multi-paid Bellman closure.
4. First universal Farey cell and later cells.

### PROHIBITED UPGRADES

- closing `18,157,310` target occurrences does not imply the whole `r=17` layer is closed;
- AP descent is an exact finite compression, not a density argument and not an asymptotic theorem;
- `r>=18` plus a partial `r=17` result does not close the first universal cell.

## 8. Next target

The first attempted uniform cutoff `m>=128` produced excessive branching in some medium-size families, so multiplicity alone is not the correct final ordering.

The next optimization should attach a reduced-cost / Bellman quantity to each AP descent state and prioritize or merge states by

\[
(a\bmod 2^h,\ b,\ m,\ \text{current affine height}),
\]

rather than lowering the multiplicity threshold blindly.

A second practical track is to split the unresolved range into

\[
2\le m\le M_0
\]

for memoized ordinary continuation and

\[
M_0<m<1024
\]

for AP propagation, choosing `M_0` from measured transition cost rather than arbitrarily.

## Reproducibility

`collatz/src/2026_09_11_math066_r17_ap_descent_certificate.py`
