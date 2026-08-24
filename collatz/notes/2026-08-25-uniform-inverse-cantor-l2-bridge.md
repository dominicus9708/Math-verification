# Uniform inverse-Cantor L2 bridge for the Stage 4 boundary spectrum

Date: 2026-08-25

Status: **exact finite reverse-orbit cosine-square identity + uniform inverse truncated-product consequence; triangular boundary assembly remains open.**

This note strengthens the inverse-dyadic bridge recorded earlier on 2026-08-25. The previous Bandi-based route carried a `3`-adic valuation factor. A second June-2026 result of Dai--Li--Wang--Wu gives a stronger uniform Fourier average, and its finite residue proof reverses naturally to the inverse-dyadic orbit that occurs in the repository's boundary reciprocity coordinate.

This is not a proof of the Collatz conjecture.

## 1. Stronger external Fourier input

Xin-Rong Dai, Bing Li, Bo Wang and Yu-Feng Wu, *Metric results for dyadic approximation on the middle-third Cantor set*, arXiv:2606.25305v1 (2026), prove that for the Cantor--Lebesgue measure `mu` there is an absolute constant `c` such that, uniformly for every nonzero integer `h`, every `a>=0`, and every `N>=1`,

\[
\boxed{
\sum_{n=a}^{a+N-1}
|\widehat\mu(h2^n)|^2
\le c^2N^{1-\gamma},
}
\]

and hence

\[
\boxed{
\sum_{n=a}^{a+N-1}
|\widehat\mu(h2^n)|
\le cN^{1-\gamma/2},
}
\]

where

\[
\gamma=\frac{\log2}{\log3}.
\]

Crucially, the constant is independent of the `3`-adic valuation of `h`.

Reference: arXiv:2606.25305v1, Lemma 2.2.

## 2. Exact finite cosine-square identity behind the theorem

Write

\[
P(x)
:=
\prod_{j=1}^{\infty}
\left|\cos\frac{\pi x}{3^j}\right|.
\]

The external proof reduces the uniform estimate to an exact finite average. For every unit

\[
3\nmid u
\]

and every `r>=0`, the powers `4^n`, `0<=n<3^r`, run once through all residues modulo `3^(r+1)` congruent to `1 mod 3`. Therefore

\[
\{u4^n\bmod3^{r+1}:0\le n<3^r\}
=
\{y\bmod3^{r+1}:y\equiv u\pmod3\}.
\]

Dai--Li--Wang--Wu prove the exact cosine-square average

\[
\boxed{
\frac1{3^r}
\sum_{\substack{y\bmod3^{r+1}\\y\equiv u\ (3)}}
\prod_{q=1}^{r+1}
\cos^2\left(\frac{\pi y}{3^q}\right)
=2^{-r-2}.
}
\]

This is their Lemma 2.8.

## 3. Exact reverse-orbit version

The inverse `4^{-1}` has the same order as `4` in the cyclic subgroup modulo every power of three. Hence reversing the powers merely reverses the same finite orbit:

\[
\boxed{
\{u4^{-n}\bmod3^{r+1}:0\le n<3^r\}
=
\{y\bmod3^{r+1}:y\equiv u\pmod3\}.
}
\]

Therefore the exact external finite identity immediately yields the reverse form

\[
\boxed{
\frac1{3^r}
\sum_{n=0}^{3^r-1}
\prod_{q=1}^{r+1}
\cos^2\left(
\frac{\pi [u4^{-n}]_{3^{r+1}}}{3^q}
\right)
=2^{-r-2}.
}
\]

Equivalently,

\[
\boxed{
\sum_{n=0}^{3^r-1}
Q_{r+1}(u4^{-n})
=3^r2^{-r-2},
}
\]

where

\[
Q_R(x):=\prod_{q=1}^{R}
\cos^2\left(\frac{\pi x}{3^q}\right)
\]

is interpreted by residues modulo `3^R`.

This equality is exact; no probabilistic or floating-point argument is involved.

## 4. Uniformity after removing a common 3-adic factor

Let

\[
h=3^m u,
\qquad3\nmid u.
\]

Then the first `m` cosine factors of `P(hx)` are equal to one. Relabelling gives

\[
\prod_{j=m+1}^{m+r+1}
\cos^2\left(\frac{\pi h4^{-n}}{3^j}\right)
=
\prod_{q=1}^{r+1}
\cos^2\left(\frac{\pi u4^{-n}}{3^q}\right).
\]

Hence the reverse-orbit identity is **uniform in `v_3(h)` after the forced unit factors are removed**.

This is the feature missing from the coarser Bandi-derived inverse estimate: high `3`-adic valuation is not intrinsically an exceptional obstruction for the complete normalized cosine-square block.

## 5. Power-saving consequence for arbitrary inverse-orbit intervals

Take any interval of `N` consecutive inverse exponents and choose `R` so that

\[
3^R\le N<3^{R+1}.
\]

Enlarge it to a complete inverse orbit block of length `3^(R+1)` at truncation `R+2`. Since every cosine-square factor is nonnegative, the interval sum is at most the complete block sum. The exact identity gives

\[
\sum_{n\in I}
Q_{R+2}(u4^{-n})
\le
3^{R+1}2^{-(R+1)-2}.
\]

Since

\[
\left(\frac32\right)^{R+1}
\asymp N^{1-\gamma},
\]

we obtain the uniform finite reverse-orbit estimate

\[
\boxed{
\sum_{n\in I}
Q_{R+2}(u4^{-n})
\ll N^{1-\gamma},
}
\]

with an absolute constant, uniformly in the starting inverse exponent and in the unit `u`.

By Cauchy--Schwarz the corresponding first-power average is

\[
\boxed{
\sum_{n\in I}
Q_{R+2}(u4^{-n})^{1/2}
\ll N^{1-\gamma/2}.
}
\]

Both exponents are strictly sublinear.

## 6. Relation to the Stage 4 boundary reciprocity coordinate

The repository's exact boundary reciprocity theorem rewrites each mixed plateau-pair factor through

\[
[-2^{-m}]_{3^\ell}.
\]

Separating parity of `m`, the sequence of inverse powers contains inverse powers of `4`. Therefore the exact reverse-orbit identity above matches the arithmetic direction of the boundary phase without any appeal to statistical equidistribution.

This strengthens the earlier bridge in two ways:

1. the estimate is based on an exact cosine-square average over a complete inverse orbit;
2. no special high-`3`-adic-valuation exceptional family is required after normalizing away the common factor.

## 7. Audit limitation: complete Cantor blocks versus triangular boundary factors

This still does **not** close Stage 4.

The reverse identity controls complete consecutive products

\[
Q_R(x)
=
\prod_{q=1}^{R}\cos^2(\pi x/3^q).
\]

A Beatty-boundary hypercube gives only selected factors at moving one-ordinals

\[
\ell_j
\]

and moving dyadic remaining lengths

\[
m_j.
\]

The boundary product therefore lies on a triangular path in the `(m,ell)` plane rather than on one vertical complete Cantor block.

The inequality direction matters. Since a complete product is no larger than any one of its individual factors, smallness of `Q_R` cannot simply be assigned to a selected top-level boundary factor.

Thus the missing bridge remains:

\[
\boxed{
\text{complete inverse Cantor-product decay}
\quad\Longrightarrow\quad
\text{decay of the triangular Beatty boundary product}.
}
\]

## 8. Refined assembly target

The appropriate next statement is now more precise.

> **Triangular inverse-Cantor assembly lemma.** For a Beatty-boundary fibre with a positive linear number of deterministic mixed plateau-pair coordinates, partition a positive-density subfamily of those coordinates into groups whose boundary cosine factors collectively dominate enough complete inverse-Cantor blocks (or prove an equivalent direct cosine-square average). The grouping must preserve the upper-bound direction.

If such an assembly loses a positive linear number of logarithmic bits on the boundary transform, the exact odd-shell transport identity can convert it into a Stage 4 repair bound. The present L7 target only requires the cumulative positive repair rate to stay below `7/50`; full subexponentiality is stronger than necessary.

## 9. External references

- Xin-Rong Dai, Bing Li, Bo Wang, Yu-Feng Wu, *Metric results for dyadic approximation on the middle-third Cantor set*, arXiv:2606.25305v1 (2026), especially Lemmas 2.2, 2.5, 2.8.
- Prasuna Bandi, *Averaged Fourier Estimates and Dyadic Approximation on the Cantor set*, arXiv:2606.27034v2 (2026), especially Lemma 7, retained as a complementary first-moment route.

## 10. Related repository results

- `2026-08-13-spectral-exception-splitting-lemma.md`;
- `2026-08-13-spectral-genealogy-boundary-reduction.md`;
- `2026-08-13-deterministic-plateau-pair-cube-decomposition.md`;
- `2026-08-13-boundary-riesz-dyadic-ternary-reciprocity.md`;
- `2026-08-25-stage4-second-window-and-odd-shell-reduction.md`;
- `2026-08-25-inverse-dyadic-cantor-average-bridge.md`.
