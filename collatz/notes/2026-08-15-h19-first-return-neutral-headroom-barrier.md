# Neutral H19 first-return headroom barrier

Date: 2026-08-15

Status: **exact finite local-to-global obstruction for neutral same-state Hensel relations over one complete first-return phase cycle**.  It proves that the neutral length-19 predecessor mechanism is never globally useful against the current minimal start: before block 34 no local relation exists, and after block 34 every local relation begins from too much global headroom.  This concerns neutral local fibres only and does not prove Collatz.

## 1. Mechanical 19-block cycle

Use the mechanical time-expanded word determined by

\[
q(t)=\lceil t\log_3 2\rceil.
\]

Split the first return interval into length-19 blocks

\[
b=0,1,\ldots,81.
\]

There are exactly twenty distinct Sturmian factor types in this cycle.

For each factor `H_b`, enumerate its full neutral fibre

\[
\mathcal F_b
=\{w:\Sigma=0,\ M=0\text{ relative to }H_b\}.
\]

Inside each fibre use the exact same-state Hensel sibling-max integerization test.

## 2. Local relation onset

For blocks

\[
\boxed{0\le b\le33}
\]

there are no neutral same-state Hensel removals at all.

The first nonempty relation set occurs at

\[
\boxed{b=34},
\]

in agreement with the companion `d=5` birth theorem.

## 3. Local multiplicative factor

For a partial integerization witness with

\[
s=v_3(R_u-R_w),
\qquad d=q-s,
\]

and `d`-th alternate odd time `t_d`, define

\[
\boxed{
\mu=\frac{3^d}{2^{t_d}}<1.
}
\]

This is the multiplicative factor carrying the block-start state into the integerized alternate predecessor, before its bounded additive correction.

For each locally removable orientation retain the smallest available `mu`, and for each factor retain the smallest such value.

## 4. Global block-start headroom

At global time

\[
t_b=19b,
\]

coefficient survival implies the actual odd count is at least

\[
q_b=\lceil19b\log_3 2\rceil.
\]

Hence every actual block-start state satisfies

\[
\boxed{
x_b\ge\frac{3^{q_b}}{2^{19b}}N.}
\]

The exact certificate evaluates, for every locally eliminative factor in the first-return cycle,

\[
\boxed{
\frac{3^{q_b}}{2^{19b}}\mu.
}
\]

Every value satisfies

\[
\boxed{
\frac{3^{q_b}}{2^{19b}}\mu>\frac32.
}
\]

The smallest product occurs at block

\[
\boxed{b=55}
\]

for the factor

\[
0110110101101101101.
\]

Its best local multiplier is

\[
\boxed{\mu=729/1024.}
\]

The product is still strictly larger than `3/2` by exact integer comparison.

## 5. Additive correction cannot bridge the gap

For a length-19 word with at most twelve odd symbols, the affine correction satisfies the crude bound

\[
R<2^{18}3^{12}.
\]

After division by the Hensel factor `3^s2^{t_d}`, the negative additive advantage of a local alternate predecessor is therefore less than

\[
2^{18}\frac{3^d}{2^{t_d}}
<2^{18}.
\]

Thus every neutral local relation in the first-return cycle gives an alternate integer satisfying

\[
\boxed{
m>\frac32N-2^{18}.}
\]

At the current verified floor `N>V_33`, this is overwhelmingly larger than `N`.

Therefore no neutral length-19 same-state Hensel relation anywhere in the first-return cycle can directly contradict global minimality.

## 6. Structural interpretation

The local and global channels are phase-complementary:

- in the low-headroom hard corridor, the neutral Hensel relation set is empty;
- once neutral Hensel relations begin to appear, the global coefficient/headroom is already so large that even the strongest local contraction remains above the original start.

Hence

\[
\boxed{
\text{local neutral Hensel availability}
\not\Rightarrow
\text{global smaller predecessor}
}
\]

through the whole first-return phase cycle.

This provides a precise stopping criterion for further length-19 neutral predecessor refinement.  A successful R1 argument must transport a relation across Euclidean scales, use non-neutral skew state, or use the ordinary dyadic / renewal-gap channels simultaneously.

## 7. Limitation

The theorem does **not** cover local fibres entered with nonzero relative skew, nor arbitrary long gate orientations.  It therefore does not exclude the current R1 resonance.

Its role is to remove one tempting but inadequate route: increasing the resolution of the neutral local Hensel sieve inside the first-return cycle cannot by itself yield the global contradiction.

## Reproducibility

Exact certificate:

`collatz/src/h19_first_return_global_headroom_certificate.py`
