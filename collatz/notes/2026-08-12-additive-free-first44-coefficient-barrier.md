# Additive-free coefficient barrier through the first 44 steps of the m=44 core

Date: 2026-08-12

Status: **exact affine theorem**. For every start in the current `m=44` recursively sufficient block, actual descent below the start and multiplicative-coefficient descent are exactly equivalent through time 44. Thus the first 44 steps may be studied using only the parity odd-count lattice path; the affine `+1` correction cannot change the sign. This does not prove convergence after time 44.

## 1. General affine iterate

For the accelerated Collatz map

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even},
\end{cases}
\]

a length-`k` parity prefix has an exact affine form

\[
\boxed{
T^k(n)=\frac{3^{q_k}n+R_k}{2^k},
}
\]

where `q_k` is the number of odd steps among the first `k` iterations and `R_k` is a nonnegative integer correction numerator.

## 2. Uniform correction bound

The correction satisfies

\[
\boxed{
0\le R_k\le 3^k-2^k.
}
\]

### Proof

Use induction on `k`.

At `k=0`, `R_0=0`.

If the next step is even, then

\[
R_{k+1}=R_k,
\]

so

\[
R_{k+1}\le3^k-2^k<3^{k+1}-2^{k+1}.
\]

If the next step is odd, then

\[
R_{k+1}=3R_k+2^k.
\]

Hence

\[
R_{k+1}
\le3(3^k-2^k)+2^k
=3^{k+1}-2^{k+1}.
\]

Equality is attained by the all-odd parity word, whose correction is exactly

\[
3^k-2^k.
\]

## 3. General additive-free descent lemma

Fix `B>=1` and suppose

\[
\boxed{
n>3^B-2^B.
}
\]

Then for every `1<=k<=B`,

\[
\boxed{
T^k(n)<n
\iff
3^{q_k}<2^k.
}
\]

### Proof

If `3^{q_k}>2^k`, then because `R_k>=0`,

\[
T^k(n)>n.
\]

The equality `3^{q_k}=2^k` is impossible for positive `k` because powers of 2 and 3 are distinct.

Now assume

\[
3^{q_k}<2^k.
\]

Put

\[
D_k:=2^k-3^{q_k}.
\]

Then `D_k` is a positive integer, so `D_k>=1`. Moreover,

\[
R_k\le3^k-2^k\le3^B-2^B<n.
\]

Therefore

\[
D_kn\ge n>R_k.
\]

This is equivalent to

\[
3^{q_k}n+R_k<2^kn,
\]

hence

\[
T^k(n)<n.
\]

## 4. Application to the current m=44 block

Every representative in the first unresolved recursively sufficient block has

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

In particular,

\[
N>4\cdot3^{44}>3^{44}-2^{44}.
\]

Thus the lemma applies with

\[
\boxed{B=44.}
\]

For every `m=44` representative and every `1<=k<=44`,

\[
\boxed{
T^k(N)<N
\iff
3^{q_k}<2^k.
}
\]

Equivalently, survival above the start through time 44 is exactly

\[
\boxed{
q_k\ge\left\lceil k\log_3 2\right\rceil
\qquad(1\le k\le44).
}
\]

There is no additive-correction ambiguity in this range.

## 5. Exact coefficient-survivor count at depth 44

Let `P_44` be the set of length-44 parity words satisfying the prefix barrier

\[
q_k\ge\lceil k\log_3 2\rceil
\qquad(1\le k\le44).
\]

Exact dynamic programming gives

\[
\boxed{|P_{44}|=83,401,400,116.}
\]

At the endpoint,

\[
\boxed{q_{44}\ge28.}
\]

The number of boundary words with exactly `q_44=28` is

\[
\boxed{12,809,477,536.}
\]

Since the first two barrier conditions force the first two parity bits to be odd, the relevant reduced `N=3 mod4` residue space modulo `2^44` has size

\[
2^{42}.
\]

Thus the exact coefficient-survivor density in that reduced dyadic address space is

\[
\boxed{
\frac{83,401,400,116}{2^{42}}
\approx0.01896328288148652.
}
\]

An independent Wolfram integer DP reproduces these values.

## 6. Relation to the growing-resolution child transport

Up to resolution 44, the dangerous dyadic tree can therefore be taken to be the **pure coefficient-barrier tree**. Its branching is completely determined by the Beatty/Sturmian threshold

\[
a_k:=\lceil k\log_3 2\rceil.
\]

At a transition `k -> k+1`:

- if `a_{k+1}=a_k`, every surviving parent has two surviving parity children;
- if `a_{k+1}=a_k+1`, a parent at the boundary `q_k=a_k` has only the odd child, while parents with `q_k>a_k` have both children.

Thus in the child-transport notation,

\[
D_k=\{\text{surviving parents with }q_k=a_k\}
\]

at the active threshold increments.

This gives an exact dynamical description of the `m(r)=1` channel through time 44; the only remaining difficulty in that range is how the ternary Cantor representatives distribute between the two dyadic children.

## 7. Strategic consequence

The first 44 steps are now separated cleanly into two independent objects:

1. **dynamical channel:** the coefficient-barrier lattice path, with no affine correction;
2. **formation/address channel:** which of those surviving parity cylinders are actually hit by
   \[
   3^{44}+\sum a_i3^i.
   \]

Therefore any further work below time 44 should not spend effort tracking the `+1` correction term. The exact target is the cross-base intersection of the ternary selector measure with the pure coefficient-survivor tree.

After time 44 this simplification is no longer automatic and the affine/two-place potential must be restored unless a stronger start-dependent correction bound is proved.