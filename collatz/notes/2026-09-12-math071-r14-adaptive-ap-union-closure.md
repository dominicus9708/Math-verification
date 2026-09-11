# MATH-071 — complete closure of the r=14 multi-paid layer

Date: 2026-09-12

Status: `EXACT FINITE r=14 CLOSURE / r>=14 CLOSED / 2<=r<=13 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-070 closes `r=15`.
- MATH-071 fills the next paid-count gap `r=14`.

## 1. Exact r=14 workload

Applying the unchanged MATH-065 exact dyadic branch-and-bound to

\[
r=14
\]

gives

\[
\boxed{
1035
=175\text{ cost-safe cells}
+507\text{ singleton-resolution cells}
+353\text{ critical cells}.
}
\]

The lower-cost unresolved part contains

\[
\boxed{24,614,018}
\]

branch-and-bound nodes and exactly

\[
\boxed{2,599,692}
\]

negative-candidate AP cylinders representing, with multiplicity,

\[
\boxed{10,691,937,078}
\]

ordinary target occurrences.

The largest completed cylinder has multiplicity

\[
\boxed{171,785,639}.
\]

Every cylinder has the exact form

\[
P(a,b,m)=\{a+bk:0\le k<m\},\qquad b\text{ odd}.
\]

## 2. Occupied multiplicity support

The exact cylinder stream has support only in five multiplicity regions:

| region | multiplicity support | cylinders | raw occurrences |
|---:|---:|---:|---:|
| A | `1..767077` | 2,598,422 | 5,455,767,618 |
| B | `1526617..2385912` | 856 | 1,673,761,049 |
| C | `4579851..7157735` | 344 | 1,968,444,716 |
| D | `13739556..16283918` | 20 | 311,052,788 |
| E | `17155074..171785639` | 50 | 1,282,910,907 |

The sums are exactly

\[
2,598,422+856+344+20+50
=\boxed{2,599,692},
\]

and

\[
5,455,767,618
+1,673,761,049
+1,968,444,716
+311,052,788
+1,282,910,907
=\boxed{10,691,937,078}.
\]

Thus there is no source cylinder outside the manifested regions.
In particular, the large visible gaps between those regions are genuinely empty in the exact r=14 source stream; they are not skipped search ranges.

## 3. Exact AP propagation

For an AP

\[
P(a,b,m),\qquad b\text{ odd},
\]

write

\[
k=\rho+2s,\qquad \rho\in\{0,1\}.
\]

Then parameter parity fixes ordinary-value parity.
The shortcut map sends each parity slice to another exact AP:

\[
T(a+b(\rho+2s))
=\frac{a+b\rho}{2}+bs
\]

for an even base, and

\[
T(a+b(\rho+2s))
=\frac{3(a+b\rho)+1}{2}+3bs
\]

for an odd base.

At every sweep the audit uses only exact set operations:

1. trim the initial AP parameter segment already `<=2^71`;
2. split by parameter parity;
3. apply the exact affine shortcut image;
4. merge only identical `(b,a mod b)` arithmetic grids with overlapping or adjacent parameter intervals;
5. deduplicate equal singleton ordinary integers.

No density, random-parity, independence, average-drift, or probabilistic inference is used.

## 4. Resource sharding has no mathematical pruning meaning

At r=14 several broad multiplicity bands create large intermediate AP-union representations.
The calculation therefore uses exact source sharding.

If a represented state becomes too large for the chosen resource cap, the ORIGINAL source-cylinder list is bisected and both halves are audited independently.
If a shard consists of one source AP, its parameter interval is bisected exactly:

\[
P(a,b,m)
=P(a,b,m_1)\cup P(a+bm_1,b,m-m_1).
\]

This is a set identity.
No candidate is discarded.
If the same ordinary target occurs in different shards, proving descent in both shards merely duplicates work.

The canonical verifier uses arbitrary-precision integers, so the proof does not depend on unsigned-128 wraparound or a hidden fixed-width bound.

## 5. Closure computation

The low and middle occupied regions were closed by exact AP-union propagation with progressively refined source shards whenever a broad representation exceeded the resource limit.
The largest closure sweep encountered there was

\[
\boxed{479}.
\]

The previously troublesome high-multiplicity tail was then completed separately.

For region D (`13739556..16283918`) all 20 source APs close directly; the largest depth observed is

\[
\boxed{438}.
\]

For region E (`17155074..171785639`) all 50 source APs close.
The largest source cylinder

\[
m=171,785,639
\]

requires exact parameter sharding under the resource cap, but every shard reaches the frozen floor.
The largest depth observed in region E is

\[
\boxed{421}.
\]

Therefore neither upper region exceeds the already certified lower/middle global bound 479.

Hence every negative-candidate completed r=14 cylinder reaches

\[
\le2^{71}
\]

within the finite certified audit.

## 6. r=14 verdict

Combining the MATH-065 cost-safe cells with complete closure of every remaining negative-candidate cylinder gives

\[
\boxed{r=14\text{ is closed}.}
\]

Together with MATH-070 and the earlier certificates,

\[
\boxed{r\ge14\text{ is closed}.}
\]

The remaining detailed multi-paid frontier is

\[
\boxed{2\le r\le13.}
\]

## 7. DSD audit

### SAFE

1. The initial MATH-065 dyadic source lineage is unchanged.
2. The five support regions are derived from the exact source stream and their counts sum exactly to the full workload.
3. Empty multiplicity gaps contain zero source cylinders; they are not inferred from sampling.
4. Every source cylinder is assigned to exactly one computational shard.
5. Source sharding is an exact union identity and has no pruning semantics.
6. Same-grid AP union preserves the represented ordinary integer set exactly.
7. Singleton deduplication is safe because future shortcut dynamics depend only on the ordinary integer.
8. Floor trimming removes only values already at or below the frozen floor.
9. Arbitrary-precision arithmetic removes the fixed-width overflow issue encountered in the upper tail.

### OPEN

- `2<=r<=13` multi-paid layers;
- mixed one-paid / multi-paid Bellman problem;
- common potential/invariant linking depth, paid count, phase/slack, address resolution, and AP multiplicity;
- first universal Farey cell emptiness;
- later Farey cells;
- the full Collatz conjecture.

### PROHIBITED UPGRADES

- `r>=14` closure `=>` all multi-paid layers are closed;
- finite AP closure `=>` a universal Collatz descent theorem;
- closure of the current paid-count tail `=>` first-cell emptiness;
- resource-shard success `=>` a dynamical theorem about multiplicity itself.

## 8. Methodological consequence

MATH-071 completes the intended comparison set

\[
r=14,15,16,17.
\]

These adjacent paid-count layers close under visibly different computational representations:

- r=17: low-bit block to singleton handoff;
- r=16: AP + block + streaming terminal audit;
- r=15: multiplicity-banded AP union;
- r=14: adaptive AP union plus exact source/parameter sharding.

The next priority is therefore not automatically r=13.
The next priority is to compare these four layers with the earlier depth-41 finite-state calculation and extract a state quantity common to the different representations.

## Reproducibility

Stage A:

`collatz/src/2026_09_12_math071_r14_leaf_export.py`

Stage B:

`collatz/src/2026_09_12_math071_r14_adaptive_ap_union_engine.cpp`
