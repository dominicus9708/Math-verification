# Christoffel renewal equality branch: two-block alphabet

Date: 2026-08-11

Status: **exact consequence of the Christoffel ceiling definition in the supercritical Collatz slope window plus the macroblock sign theorem**.

## 1. Supercritical Christoffel slope window

For an aggregate-supercritical renewal shadow, the Christoffel bound already implies

\[
\log_2 3<\frac AH<2.
\]

Let

\[
\rho:=\frac HA.
\]

Then

\[
\boxed{
\frac12<\rho<\frac1{\log_2 3}<\frac23.
}
\]

Use the standard upper mechanical/Christoffel representative

\[
b_i
=\left\lceil i\rho\right\rceil
-\left\lceil(i-1)\rho\right\rceil
\in\{0,1\}.
\]

## 2. No consecutive zeros

Suppose `b_i=b_{i+1}=0`. Then

\[
\left\lceil(i+1)\rho\right\rceil
=\left\lceil(i-1)\rho\right\rceil.
\]

But the underlying real arguments differ by

\[
2\rho>1,
\]

so their ceilings cannot be equal. Hence

\[
\boxed{00\text{ does not occur}.}
\]

Thus every zero run has length exactly `1`.

## 3. No three consecutive ones

Suppose `b_i=b_{i+1}=b_{i+2}=1`. Then

\[
\left\lceil(i+2)\rho\right\rceil
-
\left\lceil(i-1)\rho\right\rceil
=3.
\]

However the real arguments differ by

\[
3\rho<2,
\]

so the difference of their ceilings is at most `2`. Contradiction.

Hence

\[
\boxed{111\text{ does not occur}.}
\]

Since zeros are isolated and the word has more ones than zeros, every maximal one-run has length exactly `1` or `2`.

## 4. Maximal-block alphabet

A maximal debit block at accelerated parity resolution is `1^h0^d`. The two run restrictions imply

\[
\boxed{
(h,d)\in\{(1,1),(2,1)\}.
}
\]

Their block multipliers are

\[
M_{1,1}=\frac{2^2}{3}=\frac43>1,
\]

and

\[
M_{2,1}=\frac{2^3}{3^2}=\frac89<1.
\]

Therefore, on a nonperiodic orbit, the macroblock sign theorem gives

\[
\boxed{
(2,1): X' > X,
\qquad
(1,1): X' < X.
}
\]

Thus the exact Christoffel equality branch reduces to a two-symbol block alphabet:

- `U := (2,1)` — increasing block;
- `D := (1,1)` — decreasing block.

## 5. Renewal endpoint orientation

At a renewal floor `N`, the first interior block start must be strictly larger than the next renewal floor and hence larger than `N`. Therefore the first maximal block must be increasing:

\[
\boxed{\text{first block}=U=(2,1).}
\]

Immediately before the next renewal floor `N'`, the final interior block start is strictly larger than `N'`; therefore the last maximal block must be decreasing:

\[
\boxed{\text{last block}=D=(1,1).}
\]

Consequently every exact Christoffel supercritical renewal equality word has block form

\[
\boxed{U\,\cdots\,D}
\]

using only the two block types `U,D`.

## 6. Count relation

If `u` denotes the number of `U=(2,1)` blocks and `d` the number of `D=(1,1)` blocks, then

\[
\boxed{
H=2u+d,
\qquad
D_{\rm tot}=u+d,
\qquad
A=3u+2d.
}
\]

Hence the aggregate slope information is encoded entirely by the ratio `d/u`.

For near-critical Collatz slope,

\[
\frac{D_{\rm tot}}H\approx\alpha=\log_2(3/2),
\]

so the asymptotic block-count ratio is

\[
\frac du
\approx
\frac{2\alpha-1}{1-\alpha}.
\]

## 7. Role

This theorem applies to the exact Christoffel equality class, not to arbitrary near-Christoffel renewal words.

Its significance is that the sharpest arithmetic-resonance branch no longer involves arbitrary valuation sequences. It reduces to an exact two-block integer dynamics coupled to the renewal-floor condition.
