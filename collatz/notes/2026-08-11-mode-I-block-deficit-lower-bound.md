# Mode I block-deficit lower bound

Date: 2026-08-11

Status: **exact asymptotic lower bound inside an all-subcritical maximal-block tail**. This theorem is internal to the block dynamics and does not use external parity-density results.

## 1. Setup

Consider a Mode I tail of a nonperiodic odd block-start orbit

\[
N=X_0<X_1<X_2<\cdots
\]

such that every maximal block is subcritical:

\[
M_r=\frac{2^{h_r+d_r}}{3^{h_r}}<1.
\]

After discarding at most the first block, every odd block start is nonzero modulo `3`, hence

\[
X_r\equiv1\text{ or }5\pmod6.
\]

Set

\[
\alpha:=\log_2\frac32,
\qquad
\varepsilon_r:=\alpha h_r-d_r>0,
\]

and

\[
\boxed{
L_R:=\sum_{r=0}^{R-1}\varepsilon_r.
}
\]

Then

\[
\boxed{
\prod_{r<R}M_r=2^{-L_R}.
}
\]

## 2. Exact block product

The exact maximal-block product identity gives

\[
\boxed{
2^{-L_R}\frac{X_R}{N}
=
\prod_{r=0}^{R-1}
\left(
1+\frac{1-(2/3)^{h_r}}{X_r}
\right).
}
\]

Since

\[
0<1-(2/3)^{h_r}<1,
\]

the correction factor is bounded by

\[
\boxed{
\mathcal C_R
:=
\prod_{r<R}
\left(1+\frac{1-(2/3)^{h_r}}{X_r}\right)
<
\prod_{r<R}\left(1+\frac1{X_r}\right).
}
\]

Therefore

\[
\boxed{
2^{L_R}
=
\frac{X_R/N}{\mathcal C_R}.
}
\]

## 3. Spacing of block starts

The positive odd integers not divisible by `3` are exactly the residue classes `1,5 mod 6`.

For any increasing sequence in these two residue classes beginning at `N`, the `r`th later value satisfies

\[
\boxed{
X_r\ge N+3r-1
\qquad(r\ge1).
}
\]

Indeed, the successive allowed gaps alternate between `2` and `4`, so the smallest possible displacement after `r` transitions is at least `3r-1`.

In particular,

\[
\boxed{
\frac{X_R}{N}
\ge
1+\frac{3R-1}{N}.
}
\]

## 4. Upper bound on the correction product

Using `log(1+t)<=t`,

\[
\log\mathcal C_R
<
\sum_{r=0}^{R-1}\frac1{X_r}.
\]

By the spacing bound,

\[
\sum_{r=0}^{R-1}\frac1{X_r}
\le
\frac1N
+
\sum_{r=1}^{R-1}
\frac1{N+3r-1}.
\]

Since the summand is decreasing,

\[
\sum_{r=1}^{R-1}
\frac1{N+3r-1}
\le
\frac13
\log\!\left(
\frac{N+3R-4}{N-1}
\right)
\]

for `N>1`.

Hence

\[
\boxed{
\mathcal C_R
\le
\exp(1/N)
\left(
\frac{N+3R-4}{N-1}
\right)^{1/3}.
}
\]

## 5. Deficit lower bound

Combining the state-spacing lower bound with the correction upper bound,

\[
2^{L_R}
\ge
\frac{
1+(3R-1)/N
}{
\exp(1/N)
\left((N+3R-4)/(N-1)\right)^{1/3}
}.
\]

Therefore

\[
\boxed{
L_R
\ge
\log_2\!\left(1+\frac{3R-1}{N}\right)
-\frac{1}{N\log2}
-\frac13
\log_2\!\left(
\frac{N+3R-4}{N-1}
\right).
}
\]

In particular, for fixed `N`,

\[
\boxed{
L_R
\ge
\frac23\log_2 R-O_N(1).
}
\]

Equivalently, the block-boundary multiplicative coefficient

\[
\Lambda_R:=2^{-L_R}
\]

obeys

\[
\boxed{
\Lambda_R=O_N(R^{-2/3}).
}
\]

## 6. Interpretation

An infinite Mode I tail cannot remain at a bounded cumulative distance below the critical block slope.

Even if every individual block is arbitrarily close to criticality,

\[
\alpha h_r-d_r\downarrow0,
\]

the integer spacing of the strictly increasing block starts forces the total deficit to diverge at least logarithmically in block count.

Thus any rational-positive Mode I hard core must satisfy simultaneously:

1. `L_R -> infinity` at least as `(2/3) log_2 R`;
2. along the López–Stoll critical subsequence, `L_R/H_R -> 0`;
3. therefore the total odd-event mass `H_R` must overwhelm this logarithmic deficit, and bounded block depths have asymptotically zero weight.

This does not yet exclude Mode I, but it narrows it to a long-block regime with diverging yet sublinear cumulative critical deficit.
