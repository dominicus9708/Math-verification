# MATH-019 — depth-79 normalized endpoint interval separation

Date: 2026-09-08

Status: `CONFIRMED / FINITE EXACT / INTERNAL-BOUNDARY COLLISION EXCLUSION THROUGH DEPTH 79`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## 1. DSD cause classification after MATH-018

MATH-017 established zero internal cross-boundary endpoint mergers through depth 78.  MATH-018 replaced the repeated 18-step depth-61→79 tail by the exact descriptor

\[
G_{18}(r)=\bigl(H_{18}(r),s_{18}(r),T^{18}(r)\bigr).
\]

The next question was not merely whether depth 79 also has zero collisions, but **which gate causes the exclusion**.

Two gates were tested in order:

1. final odd-count support (`Q`-support);
2. normalized endpoint interval separation.

## 2. Exact depth-79 halo

Since

\[
q_{\min}(79)=50,
\]

we have

\[
79-q_{\min}(79)=29.
\]

The complete positive displacement bound needed for the finite internal-boundary audit is therefore

\[
D_{79}=2^{29}-1.
\]

For a cross-boundary pair with left offset `ell>=1` and right offset `r>=0`,

\[
ell+r\le D_{79}.
\]

Hence the local ranges are asymmetric at exactly one endpoint:

- left: `1 <= ell <= D79`;
- right: `0 <= r <= D79-1`.

This explains and confirms the MATH-017 generator counts:

\[
\boxed{963,422\text{ left local states}},
\qquad
\boxed{964,227\text{ right local states}}.
\]

The excluded right endpoint `r=D79` cannot occur in any legal pair because `ell>=1` would force `ell+r>D79`.

## 3. Q-support gate is saturated

The depth-79 final odd-count supports were computed for all 339 internal boundaries using the exact G18 threshold/odd-count descriptor.

No boundary is closed by `Q` mismatch alone.

Every one of the 339 boundaries has common final `Q` values on both sides.

The number of common `Q` values per boundary is distributed as:

| common Q values | boundaries |
|---:|---:|
|14|43|
|15|240|
|16|54|
|17|2|

Thus the zero-collision mechanism is **not** disjoint odd-count support.

This is a useful DSD route-pruning result: deeper computation must retain endpoint/correction information.

## 4. Normalized endpoint numerator

Let the tail length be

\[
L=18,
\qquad M=2^{18}.
\]

For an ordinary start

\[
N=a2^{61}+x
\]

with lower-61 endpoint `(q,y)`, let the address-lifted tail start be

\[
n=y+a3^q.
\]

After the 18-step tail let the final odd-count be

\[
Q=q+s.
\]

Define the normalized endpoint numerator

\[
\boxed{
Z=M E-a3^Q,
}
\]

where

\[
E=T^{79}(N).
\]

If

\[
r=n\bmod M,
\]

then the exact tail affine identity gives

\[
\boxed{
Z=3^{s_{18}(r)}y+C_{18}(r),
}
\]

with

\[
C_{18}(r)=M T^{18}(r)-3^{s_{18}(r)}r.
\]

Equivalently,

\[
Z=M T^{18}(r)+(y-r)3^{s_{18}(r)}.
\]

The high address-linear term has disappeared.  The address still affects which residue `r` is selected, but it no longer appears as a large additive endpoint term.

## 5. Adjacent-boundary collision equation

For an internal boundary between block labels `a` and `a+1`, a left candidate has

\[
M E_L=Z_L+a3^{Q_L},
\]

and a right candidate has

\[
M E_R=Z_R+(a+1)3^{Q_R}.
\]

If the endpoints are equal, the previously audited endpoint q-lock requires

\[
Q_L=Q_R=Q.
\]

Then endpoint equality is exactly equivalent to

\[
\boxed{
Z_L-Z_R=3^Q.
}
\]

Thus all 339 boundaries can be tested by comparing normalized endpoint ranges inside each common `(boundary,Q)` cell.

## 6. Exact interval result

There are exactly

\[
\boxed{5,100}
\]

common `(boundary,Q)` cells.

For every one of them, the exhaustive finite calculation gives

\[
\boxed{
Z_L^{\max}<Z_R^{\min}+3^Q.
}
\]

Equivalently,

\[
\boxed{
\max E_L<\min E_R
}
\]

inside every same-`Q` cell.

Therefore no same-endpoint cross-boundary pair exists at depth 79.

Combined with MATH-017:

\[
\boxed{
\text{no internal adjacent-block endpoint merger through depth }79.
}
\]

This is a finite exact statement only.

## 7. Exact minimum separation

The smallest normalized-numerator gap over all 5,100 cells is

\[
219,414,528
=837\cdot2^{18}.
\]

Hence the exact minimum same-`Q` endpoint separation is

\[
\boxed{837}.
\]

It occurs at boundary

\[
b=1241
\]

with final odd-count

\[
Q=50.
\]

A pair attaining the separation is

\[
N_L=1241\cdot2^{61}-5,
\]

\[
N_R=1241\cdot2^{61}+703.
\]

Direct 79-step shortcut-map regression gives

\[
T^{79}(N_L)=3,398,557,291,891,437,769,562,
\]

\[
T^{79}(N_R)=3,398,557,291,891,437,770,399,
\]

with

\[
Q_L=Q_R=50
\]

and

\[
\boxed{
T^{79}(N_R)-T^{79}(N_L)=837.
}
\]

## 8. DSD interpretation

This gives a much sharper cause classification than a bare `collision=0` result.

- `Q`-support gate: **SATURATED** — all 339 boundaries retain common final odd-counts.
- normalized endpoint-order gate: **COMPLETE AT DEPTH 79** — every common-Q cell is strictly one-sided.
- endpoint hash/equality gate: not needed once interval separation is established.

Thus the current structural candidate is not `Q` mismatch but persistent ordered separation:

\[
E_L<E_R.
\]

The next useful calculation is to test whether this one-sided interval ordering persists at depths 80 and 81, where the same `m=29` halo can be reused.  If it persists, the finite pattern should be analyzed for a depth-recursive inequality rather than merely extended by brute force.

## 9. Prohibited upgrades

- finite ordered separation through depth 79 does not imply arbitrary-depth monotonicity;
- `E_L<E_R` on audited candidate sets does not imply the Collatz map is globally monotone;
- no conclusion about outer-window competitors follows from this internal-boundary audit;
- first-cell and Collatz closure remain open.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_depth79_normalized_endpoint_interval_certificate.cpp`

Certificate commit:

`ef9eae15695e0fcb8f8a9c747485f2b3c3800d8a`
