# MATH-070 — complete closure of the r=15 multi-paid layer by multiplicity-banded AP union

Date: 2026-09-11

Status: `EXACT FINITE r=15 CLOSURE / r>=15 CLOSED / 2<=r<=14 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-069 closes the `r=16` layer.
- MATH-070 closes the next layer `r=15` without materializing the raw 1.835 billion target occurrences.

## 1. Exact r=15 workload

Applying the unchanged MATH-065 exact dyadic branch-and-bound to paid count

\[
r=15
\]

gives

\[
\boxed{
1061
=206\text{ cost-safe cells}
+542\text{ singleton-resolution cells}
+313\text{ critical cells}.
}
\]

The unresolved lower-cost part contains

\[
\boxed{35,343,449}
\]

branch-and-bound nodes and exactly

\[
\boxed{2,928,669}
\]

negative-candidate arithmetic-progression cylinders representing, with multiplicity,

\[
\boxed{1,835,780,279}
\]

ordinary target occurrences.

The largest single completed cylinder has multiplicity

\[
\boxed{14,315,470}.
\]

Each completed cylinder has the exact form

\[
P(a,b,m)=\{a+bk:0\le k<m\},
\qquad b=3^Q\text{ odd}.
\]

## 2. Why one global propagation is the wrong representation

A first exact global AP-union trial showed that the number of *representations* can grow sharply even while the represented ordinary target count decreases.

For example, after 12 shortcut steps the global representation had already expanded to roughly

\[
13.57\text{ million non-singleton APs}
+15.92\text{ million singleton states}.
\]

This is not a mathematical obstruction. It is a representation-cost problem: unrelated initial multiplicity scales are being sorted and merged together even though closure of each scale can be proved independently.

Therefore MATH-070 partitions the **initial cylinder representation** by multiplicity and audits each band independently.

This partition does not assume the target sets are disjoint. If the same ordinary integer is represented in two different bands, proving descent in each band separately merely duplicates work; it cannot remove a candidate.

## 3. Exact AP-union transition

Inside one band, non-singleton targets are represented as arithmetic progressions and singleton targets as ordinary integers.

For

\[
P(a,b,m),\qquad b\text{ odd},
\]

parameter parity fixes endpoint parity. Writing

\[
k=\rho+2s,\qquad \rho\in\{0,1\},
\]

gives an exact child progression.

If `a+b rho` is even,

\[
T(a+b(\rho+2s))
=\frac{a+b\rho}{2}+bs.
\]

If it is odd,

\[
T(a+b(\rho+2s))
=\frac{3(a+b\rho)+1}{2}+3bs.
\]

At every shortcut sweep the certificate performs only exact set operations:

1. remove the initial AP parameter segment whose ordinary values are already `<=2^71`;
2. split by parameter parity;
3. apply the exact shortcut affine image;
4. union overlapping or adjacent intervals only when they lie on the identical `(b,a mod b)` arithmetic grid;
5. canonicalize singleton states to their ordinary integer value and deduplicate identical values.

No density, independence, random-parity, or average-drift assumption is used.

## 4. Multiplicity partition

The certificate uses 33 contiguous disjoint bands covering

\[
1\le m\le2^{24}-1=16,777,215.
\]

This strictly contains the observed maximum multiplicity `14,315,470`.

Two bands, `48..63` and `12288..16383`, happen to contain no r=15 candidate cylinder; they remain in the partition so that the coverage audit has no hidden gaps.

The raw cylinder and occurrence sums across all bands reproduce the source workload exactly:

\[
\sum_B \#\mathrm{cylinders}(B)=2,928,669,
\]

\[
\sum_B \#\mathrm{occurrences}(B)=1,835,780,279.
\]

## 5. Closure results

Every nonempty multiplicity band becomes empty under exact AP-union shortcut propagation after all represented targets reach the frozen floor.

Representative audited closure sweep bounds include:

| initial multiplicity band | raw cylinders | raw target occurrences | certified closure sweep bound |
|---:|---:|---:|---:|
| `1..3` | 1,610,075 | 2,385,287 | 251 |
| `64..95` | 149,070 | 11,547,278 | 305 |
| `512..767` | 53,583 | 36,249,397 | 394 |
| `1024..1535` | 17,891 | 20,885,004 | 344 |
| `6144..8191` | 7,895 | 52,594,388 | 393 |
| `16384..24575` | 8,963 | 169,713,284 | 393 |
| `65536..131071` | 757 | 71,540,502 | 400 |
| `131072..262143` | 1,700 | 286,466,944 | **443** |
| `262144..524287` | 548 | 224,156,149 | 372 |
| `1048576..4194303` | 157 | 259,265,611 | 438 |
| `4194304..16777215` | 21 | 108,239,377 | 389 |

All omitted nonempty bands are asserted in the executable certificate as well.

The largest certified sweep bound among the 33 bands is

\[
\boxed{443}.
\]

This is used as a safe finite closure bound for MATH-070. The implementation does not need to claim that 443 is the mathematically minimal possible maximum trajectory length.

## 6. r=15 verdict

Every negative-candidate completed `r=15` cylinder belongs to exactly one initial multiplicity band, and every band is closed by exact ordinary-target propagation to

\[
\le2^{71}.
\]

Therefore

\[
\boxed{r=15\text{ is closed}.}
\]

Together with MATH-069 and the earlier higher-paid certificates,

\[
\boxed{r\ge15\text{ is closed}.}
\]

The remaining detailed multi-paid frontier is now

\[
\boxed{2\le r\le14.}
\]

## 7. DSD audit

### SAFE

1. MATH-065 same-integer dyadic lineage is retained through completion of every macro cylinder.
2. The multiplicity partition is a partition of representations, not a claim of statistical independence.
3. Every original cylinder is assigned to exactly one contiguous initial multiplicity band.
4. Cross-band overlap is harmless because each band is proved closed independently.
5. Within a band, AP merging occurs only on identical arithmetic grids and exact overlapping/adjacent parameter intervals.
6. Singleton deduplication is safe because future shortcut dynamics depend only on the ordinary integer.
7. Floor trimming removes only ordinary values already at or below the frozen verified floor.
8. All arithmetic uses exact integers with explicit unsigned-128 overflow guards in the AP-union engine.

### OPEN

- `2<=r<=14` multi-paid layers;
- mixed one-paid / remaining multi-paid Bellman problem;
- genuinely aperiodic low-cost same-integer path after all remaining paid counts are incorporated;
- first universal Farey cell emptiness;
- later Farey cells;
- the full Collatz conjecture.

### PROHIBITED UPGRADES

- `r>=15` closure `=>` all multi-paid layers are closed;
- bandwise finite closure `=>` a universal Collatz descent theorem;
- reduction of the paid-count frontier `=>` first-cell closure;
- computational ease of a multiplicity band `=>` a dynamical theorem about numbers of that multiplicity.

## 8. Next target

Proceed to

\[
\boxed{r=14}
\]

with the same hierarchy:

1. exact MATH-065 cylinder export;
2. inspect the initial multiplicity distribution;
3. use multiplicity-banded AP union to keep representation sizes bounded;
4. if a band becomes too large, refine that band rather than materializing ordinary targets;
5. retain exact same-integer and claim-scope audit throughout.

## Reproducibility

Stage A:

`collatz/src/2026_09_11_math070_r15_leaf_export.py`

Stage B:

`collatz/src/2026_09_11_math070_r15_banded_ap_union_engine.cpp`
