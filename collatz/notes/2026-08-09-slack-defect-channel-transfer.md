# Slack-defect channel transfer inside a surviving E/O cell

Date: 2026-08-09

Status: **DERIVED EXACT REPARAMETRIZATION / TRANSFER-MATRIX FORM**

This note reparametrizes the order-sensitive affine correction inside a fixed coefficient-surviving `(h,q)` cell. It is a bookkeeping / transfer result, not a Collatz proof.

## 1. Cell extremal positions

For a coefficient-surviving length-`h` word with `q` odd steps, let

\[
0\le d_0<\cdots<d_{q-1}<h
\]

be the odd positions.

From the exact cell-envelope lemma,

\[
\boxed{
d_i\le d_i^*
:=\min\!\left(
\lfloor i\log_2 3\rfloor,
\ h-q+i
\right).}
\]

The vector `d*` is feasible and uniquely maximizes the correction

\[
R=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
\]

## 2. Defect coordinates

Define the left-displacement / defect channel

\[
\boxed{z_i=d_i^*-d_i\ge0.}
\]

Then

\[
d_i=d_i^*-z_i.
\]

Since always `d_i>=i`,

\[
\boxed{0\le z_i\le d_i^*-i.}
\]

Strict increase of the odd positions gives a local transition constraint. Put

\[
g_i=d_{i+1}^*-d_i^*\ge1.
\]

From

\[
d_{i+1}\ge d_i+1
\]

we obtain

\[
\boxed{
z_{i+1}\le z_i+g_i-1.}
\]

Together with `z_{i+1}>=0` and its individual cap, this is an exact nearest-neighbor description of the admissible defect vectors.

In the mechanical-boundary portion,

\[
g_i\in\{1,2\};
\]

in the packed finite-length tail, `g_i=1`.

Thus the nominally global odd-position ordering becomes a sparse one-step transfer in the defect coordinate.

## 3. Exact additive correction defect

Let

\[
R^*=\sum_{i=0}^{q-1}2^{d_i^*}3^{q-1-i}.
\]

Then

\[
\boxed{
R
=R^*-
\sum_{i=0}^{q-1}
3^{q-1-i}
\left(2^{d_i^*}-2^{d_i^*-z_i}\right).
}
\]

Therefore the difference from the cell maximum is a sum of independent one-coordinate defect channels:

\[
\boxed{
R^*-R
=
\sum_i \Delta R_i(z_i),
}
\]

where

\[
\Delta R_i(z)
=3^{q-1-i}
\left(2^{d_i^*}-2^{d_i^*-z}\right).
\]

There are no higher mixed correction terms; coupling enters only through the admissibility transfer for neighboring `z_i`.

## 4. Canonical-residue channel decomposition

For the cell,

\[
3^q r+R\equiv0\pmod{2^h}.
\]

Let the extremal-path canonical residue be

\[
\boxed{
r^*\equiv-3^{-q}R^*\pmod{2^h}.}
\]

Substituting the defect expansion gives

\[
\boxed{
r(z)
\equiv
r^*
+
\sum_{i=0}^{q-1}
3^{-(i+1)}
\left(2^{d_i^*}-2^{d_i^*-z_i}\right)
\pmod{2^h}.}
\]

All inverse powers of 3 are well-defined modulo `2^h`.

Hence the canonical residue is an extremal base point plus an additive sum of defect-channel contributions.

This is the precise arithmetic version of the desired

\[
\text{E/O cell base}+\text{order-sensitive dependent channels}
\]

organization.

## 5. 2-adic triangularity

If `z_i>0`, then

\[
2^{d_i^*}-2^{d_i^*-z_i}
=2^{d_i}(2^{z_i}-1),
\]

and the factor in parentheses is odd. Therefore

\[
\boxed{
v_2(\Delta r_i)=d_i.}
\]

Consequently a defect channel whose actual odd position satisfies

\[
d_i\ge B
\]

has no effect modulo `2^B`.

Thus low canonical bits are triangular in the odd-position channels:

\[
\boxed{
r\bmod2^B
\text{ depends only on defect channels with }d_i<B.}
\]

Since `d_i>=i`, at most the first `B` odd-position channels can influence the low `B` bits.

This recovers the finite-core / tail-independence phenomenon from a channel-valuation viewpoint.

## 6. Sparse transfer-matrix form

For each coordinate `i`, use the allowed defect values as transfer states.
A transition `z -> z'` from coordinate `i` to `i+1` is allowed iff

\[
0\le z'\le\min(d_{i+1}^*-(i+1),\ z+g_i-1).
\]

Attach the group-algebra weight

\[
\boxed{
w_i(z)
=X^{\,3^{-(i+1)}(2^{d_i^*}-2^{d_i^*-z})}
}
\]

with the exponent taken modulo `2^h`.

The resulting sparse matrices have entries either zero or the corresponding monomial weight. Their ordered product generates exactly the canonical-residue support of the fixed `(h,q)` cell, up to the global base factor `X^{r^*}`.

Symbolically,

\[
\boxed{
F_{h,q}(X)
=X^{r^*}
\mathbf u^T
M_0(X)M_1(X)\cdots M_{q-1}(X)
\mathbf v
\quad\bmod(X^{2^h}-1),
}
\]

for suitable initial/final indicator vectors.

The exact indexing convention can be chosen so that the weight of a state is attached on entry or exit; the support is unchanged.

## 7. Semiring interpretations

The same sparse defect transfer can be evaluated in several ways:

- Boolean support: which canonical residues occur;
- ordinary counting: how many admissible orderings produce each class;
- group algebra / polynomial: full residue generating function;
- Fourier: evaluate `X` at a `2^h`-th root of unity;
- interval certification: propagate only the residue blocks relevant to a target;
- min-plus after an exact support/cylinder reduction: search for the least canonical representative.

Thus the earlier static-aggregation, Fourier, and min-plus views can be attached to one common cell-level channel skeleton.

## 8. Relation to slack excursions

For a zero-final-slack cell `q=a_h`, the maximizing vector is the mechanical boundary. A defect `z_i>0` moves the corresponding odd step earlier.

Equivalently, relative to the mechanical E/O word, every completed slack excursion pairs

- an extra early odd at a boundary-even position,
- with a later even at a boundary-odd position.

Such a pair moves an odd operation leftward and therefore decreases `R`, exactly as encoded by the positive defect term `R^*-R` above.

Unmatched extra odds correspond to positive final slack and are handled by the finite-length packed-tail part of `d_i^*`.

## 9. Proof-program consequence

The hard arithmetic realization problem inside a cell is now separated into:

1. a sparse local admissibility transfer in `z_i`;
2. additive modular defect channels with known 2-adic valuations;
3. a fixed extremal base residue `r^*`.

A useful next theorem would bound the ability of the early low-valuation defect channels to cancel the extremal base residue into a very small positive canonical representative. Such a bound would directly attack the small-residue obstruction while preserving the exact E/O/slack structure.