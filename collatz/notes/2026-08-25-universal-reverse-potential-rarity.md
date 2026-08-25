# Universal rarity of strong reverse potentials

Date: 2026-08-25

## Status

Safe analytic counting theorem, uniform in the ternary reverse resolution `Q`.

This strengthens the preceding fixed-slack barrier.  It is a proof-strategy result, not a Collatz proof.

## 1. Setup

Consider any reverse odd-to-odd exponent string

\[
\mathbf a=(a_1,\ldots,a_r),
\qquad a_i\ge1,
\]

with total exponent

\[
K=\sum_i a_i.
\]

Its coefficient potential is

\[
\boxed{
\Lambda(\mathbf a)=\frac{3^r}{2^K}.
}
\]

For a fixed exponent string of length `r`, the full divisibility condition determines at most one endpoint residue modulo `3^r`.

Therefore, at any larger ternary resolution `Q>=r`, that exponent string occupies at most

\[
3^{Q-r}
\]

endpoint residues modulo `3^Q`, i.e. an all-residue fraction at most

\[
3^{-r}.
\]

Invalid, nonpositive, or prematurely terminated reverse strings only reduce the true set, so using all positive exponent strings gives a safe union bound.

## 2. Resolution-independent union bound

Let `G_Q(d)` be the set of endpoint residues modulo `3^Q` for which at least one reverse code of length at most `Q` has

\[
\Lambda>3^d.
\]

Then

\[
\frac{|G_Q(d)|}{3^Q}
\le
\sum_{r\ge1}
\sum_{a_1,\ldots,a_r\ge1}
3^{-r}
\mathbf 1\!\left\{
\prod_{i=1}^r\frac{3}{2^{a_i}}>3^d
\right\}.
\]

The right-hand side no longer contains `Q`.

Thus increasing the ternary resolution can reveal more reverse codes, but it cannot evade the global weighted rarity of sufficiently strong codes.

## 3. Chernoff bound

For any `t>0`,

\[
\mathbf 1\{\Lambda>3^d\}
\le
\left(\frac{\Lambda}{3^d}\right)^t.
\]

Hence

\[
\frac{|G_Q(d)|}{3^Q}
\le
3^{-td}
\sum_{r\ge1}
\left[
\sum_{a\ge1}
\frac1{3}
\left(\frac3{2^a}\right)^t
\right]^r.
\]

The one-step factor is

\[
A_t
=
\sum_{a\ge1}
3^{t-1}2^{-at}
=
\boxed{
\frac{3^{t-1}}{2^t-1}
}.
\]

For

\[
1<t<2,
\]

we have

\[
A_t<1.
\]

Indeed, define

\[
f(t)=\log(2^t-1)-(t-1)\log3.
\]

Then

\[
f(1)=f(2)=0
\]

and

\[
f''(t)
=-\frac{2^t(\log2)^2}{(2^t-1)^2}<0.
\]

So `f` is strictly concave and therefore positive on `(1,2)`.

The geometric series converges, giving the uniform all-residue estimate

\[
\boxed{
\frac{|G_Q(d)|}{3^Q}
\le
\frac{A_t}{1-A_t}
3^{-td}
\qquad(1<t<2).
}
\]

The favorable residues are automatically nonzero modulo 3, so conditioning on the admissible endpoint residues multiplies the bound by at most `3/2`:

\[
\boxed{
\frac{|G_Q(d)|}{2\cdot3^{Q-1}}
\le
\frac32\frac{A_t}{1-A_t}
3^{-td}.
}
\]

This holds for every `Q`.

## 4. Explicit `t=3/2` form

Choosing

\[
t=\frac32
\]

gives

\[
A_{3/2}
=
\frac{\sqrt3}{2\sqrt2-1}
\approx0.947290041876462<1.
\]

The inequality is exact: after moving the positive denominator it reduces to

\[
1+\sqrt3<2\sqrt2,
\]

and squaring reduces this to

\[
\sqrt3<2,
\]

i.e. `3<4`.

Thus

\[
\boxed{
\frac{|G_Q(d)|}{2\cdot3^{Q-1}}
\le
C_{3/2}\,3^{-3d/2},
}
\]

where

\[
C_{3/2}
=
\frac32\frac{A_{3/2}}{1-A_{3/2}}
\approx26.9576207874.
\]

For example the upper bound is approximately

- `d=5`: `7.1166e-3`;
- `d=10`: `1.8787e-6`;
- `d=20`: `1.3093e-13`.

The bound is intentionally crude at small `d`; its significance is its uniform exponential decay for growing surplus.

## 5. Near-`9^{-d}` family

Because the preceding argument works for every

\[
1<t<2,
\]

for each fixed `epsilon>0` one may choose

\[
t=2-\epsilon
\]

and obtain

\[
\boxed{
\frac{|G_Q(d)|}{2\cdot3^{Q-1}}
=
O_\epsilon\!\left(3^{-(2-\epsilon)d}\right)
}
\]

uniformly in `Q`.

So strong reverse-potential residues are intrinsically close to a `9^{-d}` rarity scale up to an arbitrarily small loss in the exponent.

The constant deteriorates as `t\to2^-`, so this statement is asymptotic rather than an exact `9^{-d}` bound with one uniform constant.

## 6. Consequence for adaptive resolution

The earlier fixed-slack theorem showed that

\[
Q=Q_*(d)+O(1)
\]

cannot provide a uniform positive favorable-residue fraction.

The present theorem is much stronger:

> no choice of ternary resolution `Q`, however large, can make the set of residues carrying reverse potential `>3^d` have a uniform positive density as `d\to\infty`.

Therefore an adaptive-`Q` proof cannot close merely by saying

> increase `Q` until a positive proportion of residues have enough reverse potential.

That architecture is now ruled out.

## 7. What remains viable

This does **not** make reverse minimality useless.

The theorem is a density statement over all ternary residues.  A minimal-counterexample endpoint is not known to be generic in that residue space.

The reverse mechanism can still contribute if one proves a non-generic arithmetic correlation such as

\[
\text{hard-core / eventual-zero-lift endpoint}
\Longrightarrow
\text{membership in the rare strong-reverse set often enough}.
\]

Alternatively, the Beatty macrocycle Lyapunov theorem can control high surplus by weighted mass while fixed finite reverse filters act only in a low-surplus strip.

Thus the proof architecture narrows to two realistic roles:

1. **tail-tightness route:** use Lyapunov/ballot structure to keep the actual candidate language from living in large `d`, then use finite reverse elimination in the low strip;
2. **arithmetic-correlation route:** show that the actual minimal-counterexample residue is forced into the exponentially rare strong-reverse classes much more often than generic residue density predicts.

Uniform adaptive-residue density is no longer a viable terminal mechanism.

## 8. Relation to the stopped-tree dimension barrier

This universal rarity theorem is still distinct from the earlier stopped-tree selector-dimension barrier.

The present result concerns only the internal counting of strong reverse codes.  It is valid before the ternary selector is intersected with the binary coefficient language.

The stopped-tree barrier concerns what happens after such cross-base intersection.

Consequently a future cross-place theorem must either produce exceptional arithmetic correlation at both layers or avoid density-based closure altogether.

## 9. Reproducibility

Numerical companion and exact finite-composition checks:

`collatz/src/dsd_reverse_universal_rarity_certificate.py`

Expected final line:

`PASS`

Related exact finite DP:

`collatz/src/dsd_reverse_edge_rarity_q14_certificate.cpp`

Expected final line:

`PASS`
