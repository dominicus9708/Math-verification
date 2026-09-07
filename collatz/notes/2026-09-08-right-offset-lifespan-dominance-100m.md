# MATH-024 — right-offset lifespan dominance frontier through 1e8

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result class: `FINITE ONLY / CONFIRMED WITHIN SCOPE`
- New finite internal-boundary exclusion depth: `300,000,003`
- New evidence compression: `179,754` depth-61 survivor offsets -> `13` running-max dominance records

## 1. Input from MATH-021

For two universal-spine candidates in adjacent address blocks that meet at the same endpoint, q-lock gives

\[
d=N_R-N_L=S_L-S_R,
\]

with

\[
0<S_R,
\qquad
S_L\le Q/3.
\]

Hence any same-endpoint cross-boundary displacement satisfies

\[
0<d<Q/3\le k/3.
\]

For integer right offset `r`, a collision at depth `k` therefore requires

\[
\boxed{r\le\left\lfloor\frac{k-1}{3}\right\rfloor}.
\]

Equivalently the first possible halo-entry depth of offset `r` is

\[
\boxed{k_{\rm enter}(r)=3r+1}.
\]

## 2. Finite domain

This audit expands the MATH-022 bootstrap from

\[
0\le r\le10^7
\]

to

\[
\boxed{0\le r\le10^8}.
\]

The internal right-side starts are

\[
N=b2^{61}+r,
\qquad1025\le b\le1363.
\]

The first 61 shortcut parities depend only on `r`. Every `r` in the finite range is therefore first filtered against the exact coefficient-survival thresholds through depth 61.

The frozen published-floor threshold

\[
(3+2^{-71})^q>2^k
\]

was checked to agree with the simpler integer threshold

\[
3^q\ge2^k
\]

for every depth used in the continuation certificate, `1..700`.

## 3. Exact finite counts

Exhaustive depth-61 filtering gives

\[
\boxed{179,754}
\]

surviving right offsets in `[0,10^8]`.

The first and last are

\[
\boxed{r_{\min}=703},
\qquad
\boxed{r_{\max}=99,999,855}.
\]

For every survivor and all 339 internal boundary labels, the exact affine continuation

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}}
\]

was continued until coefficient survival failed or depth 700 was reached.

No state remained unresolved at depth 700.

The largest observed candidate lifespan is

\[
\boxed{L_{\max}=504}
\]

at

\[
\boxed{r=31,595,291,\qquad b=1218}.
\]

No audited state reaches its own halo-entry depth:

\[
\boxed{L(b,r)<3r+1}
\]

for every audited `(b,r)`.

## 4. Minimum surviving offset by depth

Define

\[
r_{\min}(k)
=\min\{r:\exists b\text{ such that }b2^{61}+r\text{ survives through depth }k\}.
\]

Selected exact values are:

| depth `k` | `r_min(k)` | collision halo `floor((k-1)/3)` |
|---:|---:|---:|
| 61 | 703 | 20 |
| 100 | 703 | 33 |
| 150 | 703 | 49 |
| 200 | 6,383 | 66 |
| 250 | 18,599 | 83 |
| 300 | 18,599 | 99 |
| 350 | 276,199 | 116 |
| 400 | 276,199 | 133 |
| 450 | 29,660,287 | 149 |
| 500 | 31,595,291 | 166 |

Within the audited continuation range there is no depth with

\[
r_{\min}(k)\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

## 5. DSD lifespan-dominance compression

For a depth-61 survivor offset `r`, define

\[
L(r)=\max_{1025\le b\le1363}L(b,r).
\]

Order the survivor offsets increasingly. A state is a running-max dominance record when its `L(r)` exceeds every previous survivor's lifespan.

Only 13 records occur among all 179,754 survivors:

| `r` | `L(r)` | witness `b` | `q61` |
|---:|---:|---:|---:|
| 703 | 161 | 1147 | 42 |
| 1,055 | 182 | 1055 | 42 |
| 1,407 | 194 | 1264 | 41 |
| 1,583 | 199 | 1087 | 42 |
| 6,383 | 226 | 1243 | 42 |
| 17,023 | 245 | 1263 | 42 |
| 18,599 | 305 | 1229 | 41 |
| 106,239 | 345 | 1328 | 41 |
| 276,199 | 429 | 1177 | 42 |
| 11,991,359 | 439 | 1144 | 43 |
| 27,454,695 | 440 | 1152 | 45 |
| 29,660,287 | 462 | 1306 | 42 |
| 31,595,291 | 504 | 1218 | 42 |

Why these 13 are sufficient as a finite evidence summary:

If `(r_i,L_i)` is a running-max record, every survivor before the next record satisfies

\[
r\ge r_i,
\qquad
L(r)\le L_i.
\]

Therefore

\[
L_i<3r_i+1
\]

implies

\[
L(r)<3r+1
\]

for the whole record interval.

Thus the finite output evidence is reduced from `179,754` survivor offsets to `13` dominance records without weakening the audited finite conclusion.

This is an **audit/evidence compression**, not yet a way to avoid computing the input states.

## 6. Extended finite collision-exclusion depth

For any

\[
k\le3\cdot10^8+3=300,000,003,
\]

MATH-021 requires a colliding right offset to satisfy

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor\le10^8.
\]

Every such offset is included in the finite audit above and every surviving offset dies before its halo-entry depth.

Hence

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le300,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

## 7. DSD interpretation

MATH-023 showed that low endpoint phase truncation is not a useful lifespan descriptor: conflict disappears only at 26 bits, where essentially no compression remains.

MATH-024 finds a different safe compression:

- not a quotient of the dynamical state;
- not a predictor of one state's lifespan;
- instead a dominance quotient of the **finite audited output relation** `(r,L(r))`.

The descriptor is therefore useful for audit presentation and regression, but it must not be used to skip future input-state computation unless an independent upper-bound rule is proved.

## 8. Prohibited upgrades

Do not infer any of the following:

- `finite 1e8 offset audit => all right offsets`;
- `depth 300,000,003 collision exclusion => first universal cell empty`;
- `no adjacent-block endpoint coupling => no candidate exists`;
- `13 dominance records => only 13 dynamical states matter`;
- `maximum lifespan 504 in this finite domain => universal lifespan bound 504`;
- `finite computation => Collatz proof`.

The first universal cell remains `OPEN`, and the Collatz conjecture remains `OPEN`.

## Reproduction

Certificate:

`collatz/src/2026_09_08_right_offset_lifespan_dominance_100m_certificate.cpp`
