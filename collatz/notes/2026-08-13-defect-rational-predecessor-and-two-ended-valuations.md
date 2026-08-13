# Defect rational predecessor and two-ended 2-adic/3-adic valuation bridge

Date: 2026-08-13

Status: **exact algebraic identities and minimal-counterexample necessary conditions**.  These results connect the Christoffel/mechanical defect channel directly to alternate-predecessor arithmetic.  They do not prove Collatz.

## 1. Same-cell affine setup

Fix a parity-time prefix depth `h` and odd count `q`.  Put

\[
M=2^h,
\qquad P=3^q.
\]

Let `w` be an actual prefix with correction `R`, ordinary start `N`, and endpoint `y`:

\[
\boxed{My=PN+R.}
\]

Let `w*` be a reference prefix in the same `(h,q)` cell with correction

\[
R^*=R+C,
\qquad C\ge0.
\]

In the first-crossing application, `w*` is the mechanical/Christoffel maximal-correction reference and `C` is the defect correction loss.

## 2. Exact rational predecessor identity

Define

\[
\boxed{N^\sharp=N-\frac CP.}
\]

Then

\[
PN^\sharp+R^*
=PN-C+R+C
=PN+R
=My.
\]

Hence

\[
\boxed{
T^h_{w^*}(N^\sharp)=y
}
\]

in the exact affine sense: the reference prefix starting from the rational 2-adic value `N^sharp` merges with the actual prefix at exactly the same endpoint `y` after `h` steps.

The 2-adic congruence is also automatic.  Since

\[
N-r^*\equiv P^{-1}C\pmod{2^h},
\]

we have

\[
N^\sharp\equiv r^*\pmod{2^h}
\]

in `Z_2`, so `N^sharp` realizes the reference parity prefix 2-adically.

Thus the normalized correction defect `C/P` has a direct dynamical meaning: it is exactly the displacement from the actual start to a rational alternate predecessor that follows the reference prefix and reaches the same endpoint.

## 3. First-crossing specialization

For the Christoffel reference at a first crossing,

\[
\eta:=\frac C{3^q}
=c_{\rm chr}-c.
\]

Therefore

\[
\boxed{N^\sharp=N-\eta.}
\]

At the current unresolved resonance the Denjoy--Koksma/rotation estimates give `eta` on the correction scale `O(q)`, whereas the recursively sufficient floor is above `3.9e21`.  Thus every current candidate has

\[
\boxed{0<N^\sharp<N}
\]

whenever `C>0`.

## 4. Integer-defect exclusion for a minimal counterexample

If

\[
P\mid C,
\]

then

\[
\eta=C/P\in\mathbb Z
\]

and `N^sharp` is an ordinary positive integer strictly smaller than `N`.

Because it realizes the reference prefix and reaches the same ordinary endpoint `y`, its future trajectory merges with the candidate trajectory at `y`.

Therefore a hypothetical minimal counterexample in the present positive-start regime must satisfy

\[
\boxed{P\nmid C}
\]

or equivalently

\[
\boxed{\eta\notin\mathbb Z.}
\]

This is a direct minimality condition, not a density heuristic.

## 5. Earliest-defect 2-adic valuation

Write the mechanical odd positions as `kappa_i`, the actual positions as

\[
d_i=\kappa_i-z_i,
\qquad z_i\ge0.
\]

Then

\[
C=
\sum_{i:z_i>0}
3^{q-1-i}2^{d_i}(2^{z_i}-1).
\]

After multiplication by `P^{-1}` modulo powers of two, every defect summand has exact 2-adic valuation `d_i`.  The `d_i` are strictly increasing, so the earliest defect has unique smallest valuation.  Hence, if `i_-` is the earliest defect index,

\[
\boxed{
v_2(P^{-1}C)=d_{i_-}
}
\]

in the high-resolution defect coordinate.

Thus the earliest defect fixes the first binary bit at which the actual and reference canonical starts can differ.

## 6. Latest odd-height defect 3-adic valuation

Let

\[
j=i_+:=\max\{i:z_i>0\}
\]

be the latest defect index.

Factor the last possible power of three:

\[
C
=3^{q-1-j}
\left[
2^{d_j}(2^{z_j}-1)
+3B
\right]
\]

for some integer `B`, because every earlier defect term has at least one additional factor of three.

If the terminal defect height is odd,

\[
z_j\equiv1\pmod2,
\]

then

\[
2^{z_j}-1\not\equiv0\pmod3.
\]

The bracket is therefore nonzero modulo three and cannot be cancelled by the earlier terms.  Consequently

\[
\boxed{
v_3(C)=q-1-j.}
\]

The reduced denominator of `C/P` is then exactly

\[
\boxed{3^{j+1}.}
\]

## 7. High-bit period consequence

By the rational-grid label-orbit theorem, an odd denominator `3^(j+1)` gives a target-resolution binary period

\[
\boxed{2\cdot3^j}
\]

for the corresponding nonintegral high-resolution defect/query coordinate, with exactly half of the bits equal to one in each complete period.

Hence an odd-height latest defect determines not merely a nonzero 3-adic denominator but the exact length of the periodic high-bit forcing pattern.

## 8. Two-ended valuation interpretation

The defect support has an exact two-ended arithmetic role:

\[
\boxed{
\text{earliest defect}
\longrightarrow
\text{first affected 2-adic start bit},
}
\]

while, when the final defect height is odd,

\[
\boxed{
\text{latest defect}
\longrightarrow
\text{3-adic denominator and high-bit period}.
}
\]

This is a literal 2-adic/3-adic two-ended coordinate on the same defect word.

It also clarifies the role of the terminal 3-adic core: information about the last few defects can determine the denominator complexity of the rational alternate predecessor even when those defects are invisible in all fixed low dyadic projections.

## 9. Limitation and next target

The condition `P not dividing C` is necessary for a minimal counterexample but not close to sufficient for exclusion.  A large odd denominator simply makes the rational predecessor nonintegral.

The next useful theorem must exploit the fact that the collision-free defect/suffix direct sum then requires the suffix channel to cancel a deterministic periodic high-bit pattern, while simultaneously staying inside the coefficient-survival language and the 3-adic minimality restrictions.

The current result supplies exact boundary data for that problem; it does not assert that such cancellation is impossible.
