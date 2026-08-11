# Primitive CF renewal as a constrained displacement-gap lattice

Date: 2026-08-11

Status: **exact arithmetic/combinatorial normal form for the residual primitive upper-CF supercritical renewal branch**. It combines the first-coefficient-crossing path, Christoffel position comparison, exact defect identity, and tiny gap channel.

## 1. Critical density path

Let

\[
\gamma:=\log_2 3,
\qquad
\beta:=\gamma^{-1}.
\]

Let `(A,H)` be a primitive upper convergent in the `A/H` coordinate:

\[
\frac AH>\gamma,
\qquad
\frac HA<\beta.
\]

Let `w` be a genuine primitive-CF renewal word and let

\[
Q_j:=\#\{\text{ones among the first }j\text{ symbols of }w\}.
\]

The first-coefficient-crossing theorem gives for every proper prefix `1<=j<A`

\[
2^j<3^{Q_j},
\]

hence

\[
\boxed{Q_j>\beta j.}
\]

Since `Q_j` is integral,

\[
\boxed{Q_j\ge\lceil\beta j\rceil.}
\]

## 2. The convergent and Christoffel prefix baselines coincide

The upper convergent in `A/H` is the lower convergent `H/A` to `beta`.

For `1<=j<A`, if

\[
\left\lceil\frac{jH}{A}\right\rceil
\ne
\lceil\beta j\rceil,
\]

there would be an integer `m` strictly between `jH/A` and `beta j`. Then the rational `m/j`, with denominator `<A`, would lie strictly between the convergent `H/A` and `beta` and would approximate `beta` more closely, contradicting the best-approximation property of the convergent.

Therefore

\[
\boxed{
\left\lceil\frac{jH}{A}\right\rceil
=
\lceil\beta j\rceil
\qquad(1\le j<A).
}
\]

The left side is exactly the prefix-one count of the ceiling Christoffel word. Hence

\[
\boxed{
Q_j\ge Q_j^{\rm chr}
\qquad(1\le j<A).
}
\]

Thus the actual renewal path stays weakly above the Christoffel prefix-count path until the common endpoint `(A,H)`.

## 3. Position-displacement staircase

Let

\[
i_1<\cdots<i_H
\]

be the actual one positions and

\[
i_k^{\rm chr}
=
\left\lfloor\frac{(k-1)A}{H}\right\rfloor+1
\]

the Christoffel positions.

The prefix-count dominance is equivalent to

\[
\boxed{i_k\le i_k^{\rm chr}.}
\]

Define

\[
\boxed{s_k:=i_k^{\rm chr}-i_k\ge0.}
\]

Because the renewal floor leaves through a subcritical first maximal block, its credit depth satisfies `h>=2`; hence the actual word begins with `11`.

In the supercritical Christoffel slope window `1<A/H<2`, the Christoffel word also begins with `11`, so

\[
\boxed{s_1=s_2=0.}
\]

The Christoffel one-position gaps satisfy

\[
\boxed{
i_{k+1}^{\rm chr}-i_k^{\rm chr}\in\{1,2\}.}
\]

Actual strict ordering `i_{k+1}>i_k` gives

\[
\boxed{
s_{k+1}-s_k
\le
 i_{k+1}^{\rm chr}-i_k^{\rm chr}-1
\in\{0,1\}.
}
\]

Therefore the displacement vector cannot rise arbitrarily: it may stay level or fall, and can increase by at most one only across a Christoffel gap of size `2`.

The total area between the actual prefix-count path and the Christoffel path is

\[
\boxed{
\sum_{j=1}^{A-1}(Q_j-Q_j^{\rm chr})
=
\sum_{k=1}^H s_k.
}
\]

## 4. Exact correction defect in displacement coordinates

The actual renewal rotation is simultaneously `C_min`-minimal and position-minimal. Hence the exact Christoffel correction defect is

\[
\boxed{
\mathcal E(s)
=
\sum_{k=1}^H
3^{H-k}2^{i_k-1}(2^{s_k}-1).
}
\]

Equivalently,

\[
\boxed{
\mathcal E(s)
=
\sum_{k:s_k>0}
3^{H-k}2^{i_k^{\rm chr}-1}(1-2^{-s_k}).
}
\]

Thus `s` determines the correction deficit exactly.

## 5. Exact modular effect on the renewal gap

Let

\[
R_{\rm chr}:=C(d_{A,H}^{\rm chr}),
\qquad
R(s):=R_{\rm chr}-\mathcal E(s),
\]

and

\[
Z:=2^A-3^H.
\]

The gap-channel theorem gives

\[
g\equiv R(s)(2^A)^{-1}\pmod Z.
\]

Define the Christoffel gap residue

\[
\boxed{
g_{\rm chr}
:=R_{\rm chr}(2^A)^{-1}\pmod Z.}
\]

Then

\[
\boxed{
g
\equiv
g_{\rm chr}
-
\mathcal E(s)(2^A)^{-1}
\pmod Z.}
\]

Since `2^A congruent 3^H mod Z`, the modular defect may equivalently be written

\[
\boxed{
\mathcal E(s)(2^A)^{-1}
\equiv
\sum_{k:s_k>0}
2^{i_k^{\rm chr}-1}3^{-k}(1-2^{-s_k})
\pmod Z,
}
\]

where inverse powers are taken modulo the odd modulus `Z`.

## 6. Tiny target set for the modular hit

Every genuine aggregate-supercritical renewal satisfies the valid Christoffel-shadow cost

\[
\boxed{0<g<\frac H3.}
\]

Both renewal floors are `3 mod 4`, so

\[
\boxed{g\equiv0\pmod4.}
\]

For all nontrivial sufficiently large pairs `Z>H/3`, the modular residue has no room to add or subtract a copy of `Z`. Therefore the residual primitive-CF branch must solve the exact small-target congruence

\[
\boxed{
\left[
g_{\rm chr}
-
\mathcal E(s)(2^A)^{-1}
\right]_Z
\in
\{4,8,12,\ldots\}\cap(0,H/3).
}
\]

The admissible target set contains at most about `H/12` integers, while the modulus `Z` is exponential in the exponent counts.

## 7. Complete residual lattice

The primitive upper-CF supercritical renewal problem is therefore reduced to finding a nonzero staircase

\[
\boxed{s=(s_1,\ldots,s_H)}
\]

such that simultaneously:

1. `s_1=s_2=0`;
2. `s_k>=0`;
3. `s_{k+1}-s_k <= i_{k+1}^{chr}-i_k^{chr}-1`;
4. actual positions `i_k=i_k^{chr}-s_k` remain strictly increasing;
5. the exact defect budget is satisfied;
6. the exact small-target gap congruence above is satisfied;
7. the fixed-word integer shadow window is nonempty;
8. the resulting segment concatenates into the global renewal-floor chain.

The zero vector is the exact Christoffel equality branch, already reduced to a finite initial audit. Hence every sufficiently large residual candidate must solve this lattice problem with `s != 0`.

## 8. Next target

The next arithmetic theorem should be a **displacement-gap separation theorem**:

> show that for all sufficiently large primitive upper convergents, no nonzero admissible displacement staircase can move the Christoffel gap residue into the tiny target set `4Z intersect (0,H/3)` while remaining inside the exact renewal defect/window budget.

This formulation uses only fixed-dimensional arithmetic data plus a constrained integer staircase and avoids returning to unrestricted parity-word enumeration.
