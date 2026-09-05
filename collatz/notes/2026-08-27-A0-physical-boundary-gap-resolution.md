# A0 physical two-boundary gap coupling and finite 3-adic exposure

Date: 2026-08-27

Status: **SAFE exact boundary identity + finite-resolution theorem.** This is a proof-architecture reduction, not a proof of the Collatz conjecture.

## 1. Physical carry coupling

For a length-`A` accelerated Collatz block from ordinary start `X` to ordinary endpoint `Y`, the physical Hensel carries are

\[
K_R=-Y,
\qquad
K_L=-2^{-A}X.
\]

Therefore

\[
\boxed{
2^A K_L-K_R=Y-X.
}
\]

This is an exact identity in `Z_3`, and the right-hand side is an ordinary signed integer.

The important point is that the large common root cancels.  If

\[
X=N+d,
\qquad
Y=N+d',
\]

then

\[
\boxed{
2^A K_L-K_R=d'-d.
}
\]

Thus the physical two-boundary condition can be expressed directly in carry coordinates without retaining `N` as a separate state variable.

## 2. Finite-resolution lemma

Suppose an ordinary integer `Delta` is known a priori to lie in an interval

\[
I=(L,U)
\]

of width

\[
U-L<3^h.
\]

Then the pair

\[
(\Delta\bmod3^h, I)
\]

determines `Delta` uniquely, because two different integers in `I` cannot differ by the nonzero multiple `3^h`.

Applied to the physical carry relation,

\[
\boxed{
[2^A K_L-K_R]_{3^h}
}

therefore exposes the complete ordinary boundary difference once its independently certified interval has width below `3^h`.

This is a boundary-resolution theorem only.  It does not assert that the complete interior Hensel dynamics can be represented by a fixed modulus `3^h`.

## 3. First global resonance needs only 21 ternary digits for the gap

At the first global resonance,

\[
Y-X=g,
\qquad
0<g<G,
\qquad
G=2^{33},
\qquad
4\mid g.
\]

Exact integer comparison gives

\[
3^{20}=3486784401<G=8589934592<10460353203=3^{21}.
\]

Hence

\[
\boxed{
[2^{A_0}K_L-K_R]_{3^{21}}=g
}
\]

as the least nonnegative representative.

So although the complete endpoint itself needs 46 ternary digits to be exposed as an ordinary integer, the **near-return difference of the two physical Hensel boundaries needs only 21**.

The divisibility `4|g` remains an additional ordinary constraint on the recovered value.

## 4. Reset A0 branch also needs only 21 ternary digits

After the certified `A0,A0,J0` reset,

\[
0\le d<0.478G.
\]

For one subsequent A0 return the independently certified mechanical-credit bound gives

\[
d'-d<a_A<0.5023G.
\]

Since the endpoint remains above the hypothetical root,

\[
d'\ge0,
\]

we have

\[
\boxed{
-0.478G<d'-d<0.5023G.
}
\]

The interval width is

\[
0.9803G.
\]

Exact arithmetic gives

\[
3^{20}<0.9803G<3^{21}.
\]

Moreover the whole interval lies inside

\[
\left(-\frac{3^{21}}2,\frac{3^{21}}2\right),
\]
so the centered representative itself is the actual signed gap.

Therefore

\[
\boxed{
\operatorname{cent}_{3^{21}}
\left(2^{A_0}K_L-K_R\right)
=d'-d
}
\]

for every A0 return from the reset strip.

This is especially useful for the hard `s=1` branch: the exact physical boundary difference is visible at a very shallow Hensel resolution, before any comparison with the defect ceiling `D<0.981G`.

## 5. Promoted strip comparison

Before the reset, in the broader promoted strip,

\[
0\le d<2G,
\qquad
d'-d<0.51G.
\]

Thus

\[
-2G<d'-d<0.51G,
\]
whose width is `2.51G`.

Exact arithmetic gives

\[
3^{21}<2.51G<3^{22}.
\]

Hence 22 ternary digits are sufficient to recover the signed ordinary difference once the interval is retained.  Twenty-one are not sufficient by interval-width alone.

## 6. Interaction with the s=1 checkpoint

The companion boundary-interface theorem gives

\[
p_{\rm int}\in\{0,1\}
\]

at the tenth-J0 split in the `s=1` sector.

The current physical state compression is therefore:

\[
\boxed{
\begin{aligned}
&K_R=-Y,\\
&K_L=-2^{-A_0}X,\\
&2^{A_0}K_L-K_R=Y-X,\\
&p_{\rm int}\in\{0,1\}.
\end{aligned}}
\]

In the reset strip, the boundary difference is already an exact 21-trit observable.

This does **not** determine the internal interface carry.  Rather, it supplies a shallow exact boundary constraint that any boundary-preserving min-plus transfer must satisfy.

## 7. Circularity audit

### SAFE

\[
\text{physical start/end}
\to
(K_R,K_L)
\to
\text{small ordinary boundary difference}
\to
\text{finite ternary exposure}.
\]

No displacement-cost lower bound is used in this chain.

### REJECTED

Do not infer from the 21-trit boundary relation that the full `Q0`-step Hensel state can be quotiented by `K mod 3^21`.  The earlier fixed-residue global quotient remains rejected.

Do not use the `D<0.981G` defect ceiling to select boundary residues.  The reset gap interval and A0 mechanical credit are separate upstream boundary data.

## 8. Next gate

The next useful operator should accept **boundary sets with a finite exact coupling**, rather than independent arbitrary carries:

\[
\boxed{
\mathcal B_{21}
=
\left\{
(K_R,K_L):
\operatorname{cent}_{3^{21}}(2^{A_0}K_L-K_R)
\in(-0.478G,0.5023G)
\right\}.
}
\]

For the `s=1` reset branch it must be combined with the two checkpoint ordering states

\[
p_{\rm int}=0,1.
\]

The remaining hard task is to propagate a rigorous min-plus lower bound across the long Christoffel blocks while preserving this two-boundary coupling; only afterward may it be compared with the independent defect budget.

Companion certificate:

`collatz/src/A0_physical_boundary_gap_resolution_certificate.py`
