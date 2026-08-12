# Growing-resolution cross-spectrum identity for the ternary core

Date: 2026-08-12

Status: **exact Fourier identity + proof-strategy barrier**. This note rewrites the intersection of the recursively sufficient ternary Cantor representatives with any finite dyadic survivor set as one exact cross-spectrum. It also shows that survivor cardinality plus ideal equidistribution alone is far too weak at the natural binary/ternary scale; a terminal argument must exploit arithmetic correlation/cancellation or a much stronger survivor sieve. This does not prove Collatz.

## 1. Representative family and reduced dyadic coordinate

For `0<=d<44`, use

\[
A_d=\left\{4\left(3^{44}+\sum_{i=0}^{d-1}a_i3^i\right)+3:\ a_i\in\{0,1\}\right\}.
\]

Write

\[
Y(a):=3^{44}+\sum_{i=0}^{d-1}a_i3^i,
\qquad N(a)=4Y(a)+3.
\]

Fix a binary resolution `L>=3` and put

\[
M:=2^{L-2}.
\]

Because every representative is `3 mod 4`, any proposition depending only on `N mod 2^L` is equivalently a proposition on

\[
Y\pmod M.
\]

Let

\[
R\subseteq\mathbb Z/M\mathbb Z
\]

be any retained/dangerous set of reduced dyadic residues. It may come from a forward stopping-time cylinder sieve, a forward/reverse cross-place sieve, or any other exact class proposition at resolution `L`.

Define the exact intersection count

\[
\boxed{
C_{d,L}(R)
:=\#\{a\in\{0,1\}^d:Y(a)\bmod M\in R\}.
}
\]

## 2. Exact Fourier expansion

Let

\[
\omega=e^{2\pi i/M}
\]

and use the unnormalised finite Fourier transform

\[
\widehat{1_R}(t)
:=\sum_{r\in R}\omega^{-tr},
\qquad t\in\mathbb Z/M\mathbb Z.
\]

Fourier inversion gives

\[
1_R(x)=\frac1M\sum_{t=0}^{M-1}\widehat{1_R}(t)\omega^{tx}.
\]

Substitute `x=Y(a)` and sum over all selector vectors. Since the selectors separate multiplicatively,

\[
\sum_{a\in\{0,1\}^d}\omega^{t\sum_i a_i3^i}
=\prod_{i=0}^{d-1}(1+\omega^{t3^i}).
\]

Therefore

\[
\boxed{
C_{d,L}(R)
=\frac1M
\sum_{t=0}^{M-1}
\widehat{1_R}(t)\,
\omega^{t3^{44}}
\prod_{i=0}^{d-1}(1+\omega^{t3^i}).
}
\]

Equivalently, after dividing by `2^d`,

\[
\boxed{
\frac{C_{d,L}(R)}{2^d}
=\frac{|R|}{M}
+\frac1M\sum_{t\ne0}
\widehat{1_R}(t)\omega^{t3^{44}}
\prod_{i=0}^{d-1}
\frac{1+\omega^{t3^i}}2.
}
\]

This is an exact identity, not a probabilistic approximation.

## 3. Ternary Riesz-product channel

The selector factor has magnitude

\[
\left|\frac{1+e^{2\pi i t3^i/M}}2\right|
=\left|\cos\left(\frac{\pi t3^i}{M}\right)\right|.
\]

Hence define the ternary-core spectral weight

\[
\boxed{
P_{d,L}(t)
:=\prod_{i=0}^{d-1}
\frac{1+\omega^{t3^i}}2.
}
\]

and the cross-spectrum

\[
\boxed{
\mathcal X_{d,L}(R)
:=\sum_{t\ne0}
\widehat{1_R}(t)
\omega^{t3^{44}}P_{d,L}(t).
}
\]

Then

\[
\boxed{
C_{d,L}(R)
=\frac{2^d}{M}\left(|R|+\mathcal X_{d,L}(R)\right).
}
\]

The problem is therefore not merely the size of the dyadic survivor set and not merely the mixing of the ternary subset sums. It is the **spectral overlap** between them.

## 4. Relation to the fixed-resolution mixing theorem

For fixed `L`, every nonzero frequency satisfies

\[
|P_{d,L}(t)|\to0
\]

exponentially as `d->infinity`, which recovers the previously proved fixed-resolution mixing result:

\[
C_{d,L}(R)/2^d\to |R|/M.
\]

The new identity shows exactly what changes when the resolution also grows: one must control the joint quantity

\[
\widehat{1_R}(t)P_{d,L}(t)
\]

for `L=L(d)`, not either factor in isolation.

## 5. A rigorous triangle-inequality certificate

The identity immediately gives the sufficient condition

\[
\boxed{
\frac{2^d}{M}
\left(
|R|+
\sum_{t\ne0}|\widehat{1_R}(t)|\,|P_{d,L}(t)|
\right)<1
\Longrightarrow
C_{d,L}(R)=0.
}
\]

The conclusion follows because `C_{d,L}(R)` is a nonnegative integer.

This criterion is intentionally conservative. A sharper terminal proof may need signed cancellation in `\mathcal X`, but this formula gives an exact finite target for every proposed growing-resolution sieve.

## 6. Entropy-only barrier, even under ideal mixing

Let

\[
\gamma:=\log_2 3,
\qquad
\alpha:=\log_3 2=1/\gamma.
\]

At the natural scale of a `d`-trit representative block,

\[
L\sim\gamma d.
\]

Suppose a dyadic dangerous set has exponential size

\[
|R_L|=2^{\sigma L+o(L)}.
\]

Even in the **idealised best case** in which all nonzero cross-spectrum terms vanished exactly, the expected intersection scale from the zero Fourier mode would be

\[
\frac{2^d|R_L|}{2^L}
=2^{\left[1-(1-\sigma)\gamma\right]d+o(d)}.
\]

For this main term to tend to zero one would need

\[
\boxed{
\sigma<1-\frac1\gamma
=1-\log_3 2
\approx0.3690702464.
}
\]

Thus a mere density/counting argument cannot terminate the program unless the dangerous dyadic language has dimension below about `0.3691`, or unless one proves strong negative arithmetic correlation with the ternary core.

## 7. Comparison with the coefficient-survival entropy

For coefficient-surviving parity words, the endpoint binomial bound gives exponential rate

\[
H_2(\alpha)
=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha)
\approx0.9499555272.
\]

This is enormously larger than the ideal-mixing threshold `0.3690702464`.

Indeed, substituting `sigma=H_2(alpha)` into the natural-scale main exponent gives

\[
\boxed{
1-(1-H_2(\alpha))\gamma
\approx0.9206813872>0.
}
\]

So even **perfect** binary/ternary equidistribution combined only with the classical coefficient-survivor count would leave exponentially many nominal intersections.

This proves a useful strategy barrier:

\[
\boxed{
\text{survivor cardinality + generic mixing is not a terminal mechanism.}
}
\]

The proof must preserve arithmetic compatibility information.

## 8. Correct growing-resolution target

For a nested exact survivor family `R_L`, the terminal object is

\[
\boxed{
C_{d,L(d)}(R_{L(d)}),
}
\]

with `L(d)->infinity`.

There are only two structurally plausible ways for it to vanish:

1. make `R_L` dramatically smaller by adding genuinely stronger forward/reverse/minimality propositions; or
2. prove that the survivor spectrum and the ternary Riesz product have destructive cross-base correlation, so that the nonzero Fourier modes cancel the positive zero-mode contribution on the actual Cantor core.

This is more precise than the earlier generic instruction to use growing resolution. It identifies the exact cross-place quantity that must be controlled.

## 9. DSD-style interpretation

The two channels are now mathematically explicit:

- **ternary formation channel:** `P_{d,L}(t)`;
- **dyadic dynamical-survivor channel:** `widehat{1_R}(t)`.

Their compatibility is not inferred from either marginal descriptor. It is measured by

\[
\boxed{
\mathcal X_{d,L}(R).
}
\]

Thus the next proof stage should keep the cross-channel phase information rather than collapsing either side to a scalar density.