# Depth-72 internal-boundary endpoint exclusion — MATH-015

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `FINITE ONLY / EXACT DEPTH-72 INTERNAL-BOUNDARY EXCLUSION`
- Scope: the current 340-block first-cell candidate language through depth 72

## 1. Why the old halo can be sharpened

MATH-005 used the full-first-cell candidate correction bound to obtain

\[
H=24{,}019{,}143{,}996<2^{35}.
\]

That bound is safe for the whole first-cell endpoint problem, but it is much wider than necessary at a fixed shallow depth.

For a length-k parity word with q odd bits,

\[
T^k(N)=\frac{3^qN+C}{2^k}.
\]

The normalized correction satisfies the elementary envelope

\[
0\le \frac{C}{3^q}
<2^{k-q}\left(1-\left(\frac23\right)^q\right)
<2^{k-q}.
\]

If two candidate prefixes of length k share one endpoint, MATH-004 gives the same q, so their positive integer start displacement d obeys the same envelope.

At depth 61, coefficient survival gives

\[
q\ge39,
\]

hence

\[
\boxed{d\le2^{22}-1=4{,}194{,}303.}
\]

At depth 72,

\[
q\ge46,
\]

hence

\[
\boxed{d\le2^{26}-1=67{,}108{,}863.}
\]

Thus every cross-boundary merge that can occur by depth 72 is contained in a `2^26-1` local halo around its boundary.

## 2. Boundary-local coordinates

Let

\[
W=2^{61}
\]

and let an internal block boundary be

\[
B=bW,
\qquad b=1025,\ldots,1363.
\]

Write a left/right pair as

\[
N_-=B-\ell=(b-1)W+(W-\ell),
\]

\[
N_+=B+r=bW+r.
\]

For the first 61 steps, the parity words depend only on

\[
W-\ell
\quad\text{and}\quad
r,
\]

not on the boundary label b.

If their 61-step odd counts are q, then

\[
T^{61}(N_-)=T^{61}(W-\ell)+(b-1)3^q,
\]

\[
T^{61}(N_+)=T^{61}(r)+b3^q.
\]

In particular an exact depth-61 cross-boundary equality would reduce to

\[
\boxed{T^{61}(W-\ell)-T^{61}(r)=3^q,}
\]

which is independent of b.

Equivalently, if the corresponding length-61 corrections are `C_-` and `C_+`,

\[
\boxed{C_--C_+=3^q(\ell+r).}
\]

Thus a cross-boundary endpoint equality is exactly a wrap-around Hensel translation credit in local boundary coordinates.

## 3. Exact depth-72 scan

The certificate uses the complete depth-72 displacement halo

\[
D=2^{26}-1=67{,}108{,}863.
\]

It first scans the two local lower-61 residue ranges

\[
0\le r<D,
\]

\[
1\le\ell\le D,
\]

and retains only states satisfying coefficient survival at every depth 1 through 61.

Exact counts are

\[
\boxed{120{,}566}
\]

right-side lower-61 survivors and

\[
\boxed{120{,}071}
\]

left-side lower-61 survivors.

For every one of the 339 internal boundaries, the exact affine address lift is then applied and the final 11 shortcut steps are propagated while checking coefficient survival through every depth up to 72.

Across all boundaries, the numbers of depth-72 surviving evaluations are

\[
22{,}527{,}308
\]

on the right and

\[
22{,}306{,}426
\]

on the left.

The endpoint sets were compared with exact integer arithmetic.

Result:

\[
\boxed{
\text{cross-boundary endpoint collisions through depth 72}=0.
}
\]

No equality was found even before requiring equal final q in the lookup key.

## 4. Why checking depth 72 also covers earlier mergers

The shortcut map is deterministic. If two trajectories become equal at any common depth

\[
k\le72,
\]

then all subsequent endpoints are equal, so they are also equal at depth 72.

Therefore the zero depth-72 intersection proves, within the completely scanned halo and candidate language,

\[
\boxed{
\text{no internal adjacent-block endpoint merger occurs at any depth }k\le72.
}
\]

The displacement halo is complete because a candidate merger at depth 72 has common q by the already audited MATH-004 q-lock and hence satisfies the exact fixed-depth correction-credit envelope used above.

## 5. Computational consequence

MATH-005 required synchronized treatment of 339 internal halos in the general first-cell architecture.

MATH-015 closes those interfaces **through the current 61+11 calculation window**:

\[
\boxed{
\text{through depth72, the 340 blocks have no cross-boundary endpoint coupling.}
}
\]

Thus any current depth-72 endpoint quotient / block-label computation may be performed block-locally without an internal halo merge step.

This does not say that cross-boundary mergers never occur at deeper depths.

## 6. DSD interpretation

- `D`: block label, local offset, lower-61 endpoint, address lift, and depth-72 endpoint are kept distinct.
- `R`: exact `2^26-1` displacement halo, all 339 internal boundaries, every prefix through depth72.
- `S`: only universal-spine states are retained.
- `E`: all cross-boundary endpoint equalities through depth72 are excluded by exhaustive exact intersection.
- `T`: 61-step local state followed by exact 11-step address-dependent lift.
- `C`: exact integer certificate; no floating point and no sampling.
- `N`: `FINITE ONLY / ESTABLISHED_WITHIN_SCOPE`.
- `O`: internal halo interfaces are closed through depth72; deeper first-cell problem remains open.

## 7. Prohibited upgrades

Do not infer

\[
\text{no merge through72}\Longrightarrow\text{no merge at larger depth}.
\]

Do not infer that all MATH-005 halos are globally empty through the full first universal cell.

Do not infer that block-locality of endpoint merging makes every other proof constraint block-local.

Do not infer first-cell or Collatz closure.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_depth72_internal_boundary_endpoint_exclusion_certificate.cpp`

Certificate commit:

`656509a9ad6eb83ca7fb3f97174d0d12096e8855`

Local exact run used `g++ -O3 -std=c++17` and returned `PASS` with zero collisions.

## Next target

The shallow internal halo is now closed through depth72. The next useful calculation is to extend the same exact fixed-depth envelope and address-lift machinery beyond 72 in staged windows, stopping when the required halo becomes too large or when a first genuine cross-boundary merger appears. The first such depth is structurally informative either way.
