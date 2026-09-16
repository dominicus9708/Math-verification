# Low-slack endpoint no-wrap window

Date: 2026-08-09

Status: **DERIVED LEMMA / SEARCH-SPACE REDUCTION**

This note combines the exact coefficient-surviving cell correction envelope with the finite-horizon carry modulus.

## 1. Setup

Fix a target depth

\[
K=h+m.
\]

At depth `h`, consider a coefficient-surviving canonical state

\[
(h,q;r,y)
\]

with

\[
q=a_h+s,
\qquad
a_h=\lceil h\log_3 2\rceil,
\qquad s\ge0.
\]

Assume a candidate threshold

\[
0<r\le U.
\]

The exact affine identity is

\[
2^h y=3^q r+R.
\]

From the coefficient-surviving odd-position constraint,

\[
R\le q3^{q-1}.
\]

Also

\[
\frac{3^q}{2^h}<3^{s+1}.
\]

Hence

\[
\boxed{
y<3^s(3U+q).}
\]

## 2. No-wrap criterion

The exact finite-horizon carry state uses

\[
\eta=y\bmod2^m,
\qquad m=K-h.
\]

If

\[
\boxed{
3^s(3U+q)<2^m,
}
\]

then automatically

\[
0\le y<2^m
\]

and therefore

\[
\boxed{
\eta=y.
}
\]

Thus no 2-adic endpoint aliasing is possible for any threshold candidate in that `(h,q)` cell.

## 3. State-count consequence

Without the magnitude information, an exact finite-horizon transfer may nominally allow up to `2^m` endpoint residues.

Under the no-wrap criterion, every threshold candidate instead lies in the ordinary integer interval

\[
0\le y<3^s(3U+q).
\]

Hence the number of possible endpoint states in the cell is bounded by

\[
\boxed{
N_y(h,q;U)
\le
\left\lceil3^s(3U+q)\right\rceil,
}
\]

before applying any further parity, residue, or min-plus restrictions.

The useful envelope is therefore

\[
\boxed{
N_y
\le
\min\!\left(
2^{K-h},
\lceil3^s(3U+q)\rceil
\right).
}
\]

This is the endpoint analogue of the earlier count-plane / carry-residue minimum envelope.

## 4. Polynomial-threshold regime

Suppose

\[
U(K)=C K^p
\]

and a branch has certified slack

\[
s\le c\log_3 K+O(1).
\]

Then

\[
3^s(3U+q)
=K^{p+c+o(1)}
\]

for `h<=K`.

Therefore the no-wrap criterion certainly holds whenever

\[
K-h>(p+c+\varepsilon)\log_2K
\]

for sufficiently large `K` (with constants absorbed into `epsilon`).

So on any branch with logarithmically bounded slack, the arithmetic endpoint remains an ordinary polynomial-size integer through all but an `O(log K)` terminal boundary layer.

This statement is conditional only on the stated slack bound; no global logarithmic slack bound for every survivor is claimed.

## 5. Interaction with exact slack saturation

There are now two structurally different regimes.

### Low/moderate slack

When `s` is bounded and the no-wrap inequality holds, the endpoint fiber is an ordinary bounded integer interval rather than a full `2^m` residue space.

### Very high slack

If

\[
s\ge a_K-a_h,
\]

then the high-slack saturation lemma says every future parity suffix is coefficient-admissible and the exact future lift value is zero.

The difficult states lie between these two easy regimes: enough slack to make the endpoint potentially large, but not enough slack to trivialize future coefficient survival.

## 6. Proof-program use

For a threshold search `mu(K)<=U`, a block-transfer implementation can safely replace the endpoint-residue capacity

\[
2^{K-h}
\]

by

\[
\min\left(2^{K-h},\,3^s(3U+q)\right)
\]

in every cell where the candidate threshold `r<=U` is enforced.

Combined with the prefix first-hit lower bound, this suggests an exact branch strategy:

1. prune by `r+2^h L_ell >= U` when possible;
2. otherwise use the cell correction envelope to bound `y`;
3. if the no-wrap criterion holds, carry `y` as an ordinary bounded integer;
4. enter the full modular carry representation only in the remaining cells / terminal layer.

This is a search-space theorem, not yet an asymptotic Collatz proof.