# G14 supergate conjugacy and exact two-ended valuations

Date: 2026-08-14

Status: **exact second-level gate conjugacy theorem + exact 2-adic/3-adic endpoint valuation law**. This is a state-compression theorem inside the R2 proof program. It does not prove the Collatz conjecture.

Put

\[
\alpha:=\log_3 2.
\]

From the type-0 first-return renormalization, define

\[
\theta:=665-1054\alpha>0.
\]

The second induced return has two chronological supergate types

\[
G_{13}:(L,q)=(20026,12635),
\]

\[
G_{14}:(L,q)=(21565,13606).
\]

Their original-phase start intervals may be taken as

\[
I_{14}=[0,19\theta),
\qquad
I_{13}=[19\theta,\,1539\alpha-971).
\]

The rational enclosure

\[
\frac{15601}{24727}<\alpha<\frac{31867}{50508}
\]

certifies every discontinuity decision below time `21565` by exact rational arithmetic.

## 1. Exact factor counts

The interval `I_13` contains no interior mechanical discontinuity. Therefore

\[
\boxed{G_{13}\text{ has one full-parity factor type}.}
\]

The interval `I_14` contains exactly 18 interior discontinuities, hence

\[
\boxed{G_{14}\text{ has exactly }19\text{ conjugate full-parity factor types}.}
\]

Write them in increasing phase order as

\[
W_0,W_1,\ldots,W_{18}.
\]

## 2. Exact self-similar discontinuity lattice

The 18 interior discontinuities are exactly

\[
\boxed{
 j_n=1054n,
 \qquad
 d_n=\lceil j_n\alpha\rceil=665n,
 \qquad n=1,\ldots,18.
}
\]

The next multiple `n=19` gives

\[
j_{19}=20026,
\qquad d_{19}=12635,
\]

which lies exactly on the right endpoint `19 theta` of the interval and is therefore not an interior discontinuity.

Thus the second gate renormalization aligns the original parity discontinuities on integer multiples of the previous convergent vector

\[
\boxed{(1054,665).}
\]

This is an exact self-similarity statement rather than a numerical pattern.

## 3. Adjacent correction channels

Crossing the `n`-th discontinuity changes one adjacent pair

\[
01\longrightarrow10
\]

at zero-based positions `j_n-1,j_n`.

Since every `G_14` factor has total odd count

\[
q=13606,
\]

the number of odd symbols strictly after this adjacent pair is

\[
\boxed{
r_n=13606-665n.}
\]

The affine correction difference across that edge is therefore

\[
\boxed{
D_n
=R(W_{n-1})-R(W_n)
=2^{1054n-1}3^{13606-665n}.
}
\]

Consequently

\[
\boxed{v_2(D_n)=1054n-1,}
\]

\[
\boxed{v_3(D_n)=13606-665n.}
\]

The normalized rational displacement is

\[
\boxed{
\frac{D_n}{3^{13606}}
=\frac12\left(\frac{2^{1054}}{3^{665}}\right)^n
=\frac12\,3^{-n\theta}.
}
\]

Because `theta>0`, these edge displacements decrease monotonically but remain close to one half throughout the finite 18-edge fibre.

## 4. Exact two-ended valuation theorem

For any pair `0<=a<b<=18`,

\[
R(W_a)-R(W_b)
=\sum_{n=a+1}^{b}D_n.
\]

The 2-adic valuations of the summands strictly increase with `n`. Hence the first edge is the unique term of minimal 2-adic valuation and cannot be cancelled:

\[
\boxed{
 v_2(R(W_a)-R(W_b))
 =1054(a+1)-1.
}
\]

The 3-adic valuations strictly decrease with `n`. Hence the last edge is the unique term of minimal 3-adic valuation and cannot be cancelled:

\[
\boxed{
 v_3(R(W_a)-R(W_b))
 =13606-665b.
}
\]

Thus the correction difference has an exact endpoint factorization

\[
\boxed{
R(W_a)-R(W_b)
=2^{1054(a+1)-1}
 3^{13606-665b}
 U_{a,b},
}
\]

where

\[
\boxed{\gcd(U_{a,b},6)=1.}
\]

The earliest differing conjugacy edge controls the first dyadic bit, while the latest differing edge controls the residual 3-adic denominator.

## 5. Relation to the earlier defect endpoint theorem

The same two-ended pattern appeared earlier for Christoffel defects:

- the earliest defect controls the lowest newly changed 2-adic address bit;
- the latest suitable defect controls the residual 3-adic denominator/high-lift period.

The `G_14` supergate proves that this is not peculiar to the original defect coordinates. It is reproduced exactly by continued-fraction conjugacy at a higher Euclidean scale.

Hence the natural renormalized arithmetic state is endpoint-oriented:

\[
\boxed{
(\text{first active dyadic edge},\
 \text{last active 3-adic edge},\
 \text{gate phase/state}).
}
\]

## 6. Limitation

As in the preceding `G_81` theorem, conjugate-gate integerization by itself is neutral for minimality. The denominator clears after the last differing adjacent swap, when the two conjugate paths have already merged to the same actual state.

Therefore this theorem compresses the cross-base address geometry but does not produce a new smaller predecessor by itself.

A terminal use must combine the endpoint valuations with an independent condition such as

1. an alternate word outside the conjugacy fibre;
2. finite-natural dyadic address stabilization;
3. the ternary recursively-sufficient core;
4. or an Archimedean headroom/defect budget.
