# Exact dyadic-fiber orthogonality and the weighted-overlap target

Date: 2026-08-25

Status: **exact odd-frequency orthogonality theorem for every deterministic plateau hypercube fibre + audit of its limitation.  Stage 4 remains open at the selector-weighted boundary overlap.**

This note sharpens the Stage 4 spectral route after the distinct-3-adic-depth calculation.  It avoids the factor-dependent reciprocity correction entirely by working in the original dyadic boundary coordinates.

## 1. Generic theorem

Let

\[
2\le m_1<\cdots<m_r\le M
\]

be distinct dyadic depths and let every \(a_t\) be odd.  Define

\[
F(k)=\prod_{t=1}^r
\cos\!\left(\frac{\pi a_tk}{2^{m_t}}\right).
\]

Then

\[
\boxed{
\frac1{2^{M-1}}
\sum_{\substack{0\le k<2^M\\k\ \mathrm{odd}}}
|F(k)|^2
=2^{-r}.
}
\]

The identity is exact.

## 2. Proof

Use

\[
\cos^2(\pi x)
=\frac12+rac14e^{2\pi ix}+rac14e^{-2\pi ix}.
\]

After lifting every denominator to \(2^M\), every term in the product expansion has character frequency

\[
A_\varepsilon
=\sum_{t=1}^r
\varepsilon_t a_t2^{M-m_t},
\qquad
\varepsilon_t\in\{-1,0,1\}.
\]

Suppose \(\varepsilon\ne0\), and let \(t_*\) be the index with largest \(m_t\) for which \(\varepsilon_t\ne0\).  Because \(a_{t_*}\) is odd, the \(t_*\) term has exact 2-adic valuation

\[
M-m_{t_*}.
\]

Every other nonzero term has valuation at least one larger.  Hence no cancellation can remove the least-valuation term and

\[
\boxed{
\nu_2(A_\varepsilon)=M-m_{t_*}\le M-2.
}
\]

The normalized character average over the odd residues modulo \(2^M\) is nonzero only for frequencies congruent to \(0\) or \(2^{M-1}\) modulo \(2^M\).  The valuation identity excludes both possibilities for every nonconstant expansion term.

Therefore only the product of the constant \(1/2\) terms survives, giving exactly \(2^{-r}\).

No equidistribution assumption is used.

## 3. Specialization to a deterministic Beatty plateau fibre

For a boundary hypercube fibre in `2026-08-13-deterministic-plateau-pair-cube-decomposition.md`, every free mixed plateau coordinate \(j\) has character increment

\[
2^j3^{-\ell_j}\pmod{2^{L+1}}.
\]

After cancelling the common \(2^j\), its normalized fibre Fourier factor is

\[
\left|
\cos\!\left(
\frac{\pi k[3^{-\ell_j}]_{2^{m_j}}}{2^{m_j}}
\right)
\right|,
\qquad
m_j=L+1-j.
\]

The plateau starts are distinct, hence the \(m_j\) are distinct.  Also

\[
[3^{-\ell_j}]_{2^{m_j}}
\]

is odd.  Since every deterministic plateau start obeys \(j\le L-2\), one has \(m_j\ge3\).

Thus for a fibre with \(r_F\) free mixed plateau coordinates,

\[
\boxed{
\frac1{2^{L}}
\sum_{\substack{0\le k<2^{L+1}\\k\ \mathrm{odd}}}
|\widehat\nu_F(k)|^2
=2^{-r_F},
}
\]

where \(\nu_F\) is the uniform probability measure on the fibre, up to the irrelevant affine phase of the chosen base point.

The bound is completely independent of

- the boundary path height;
- the one ordinals \(\ell_j\);
- the 3-adic reciprocity correction;
- the orientation of any other plateau coordinate.

This is stronger and cleaner than first rewriting every factor in reciprocal 3-adic form.

## 4. Consequence for large fibres

The deterministic plateau-cube theorem already proves that, except for an exponentially small portion of boundary words, a boundary word belongs to a fibre with a linear number of free coordinates.  For any such fibre with

\[
r_F\ge cL,
\]

the exact mean square is

\[
\boxed{2^{-r_F}\le2^{-cL}.}
\]

By Markov, for any threshold \(\tau>0\), the fraction of odd dyadic frequencies satisfying

\[
|\widehat\nu_F(k)|>\tau
\]

is at most

\[
\boxed{2^{-r_F}\tau^{-2}.}
\]

Thus every large deterministic boundary fibre has an exponentially sparse set of Fourier frequencies on which its normalized transform can be large.

## 5. Audit: why this still does not close Stage 4

The selector measure at growing dyadic resolution has support only \(2^d\) points.  The repository support-size theorem proves that its global Fourier energy cannot become uniformly small once the dyadic modulus greatly exceeds the selector support.

Therefore the unweighted identity

\[
\operatorname*{avg}_{k\ \mathrm{odd}}
|\widehat\nu_F(k)|^2=2^{-r_F}
\]

does not by itself control the required transport correlation

\[
\sum_{k\ \mathrm{odd}}
\widehat\mu(k)\overline{\widehat\nu_F(k)}.
\]

In particular, a small exceptional frequency set for \(\nu_F\) might still carry a disproportionate fraction of selector Fourier mass.

Accordingly the previous statement that the dyadic reciprocity correction was the final assembly obstruction was too narrow.  Working directly in dyadic coordinates removes that correction from the theorem, but exposes the genuine remaining issue:

\[
\boxed{
\text{selector-weighted concentration on the fibre's exceptional frequencies.}
}
\]

## 6. Exact weighted-overlap reformulation

Let \(G=\mathbb Z/N\mathbb Z\), and let \(\mu\) and \(\nu\) be probability measures on \(G\).  Put

\[
\widetilde\mu(x)=\mu(-x),
\qquad
\widetilde\nu(x)=\nu(-x).
\]

With the normalized probability-measure Fourier transform,

\[
\widehat\mu(k)=\sum_x\mu(x)e^{-2\pi ikx/N},
\]

Parseval/convolution gives the exact nonnegative weighted identity

\[
\boxed{
\frac1N\sum_k
|\widehat\mu(k)|^2|\widehat\nu(k)|^2
=
(\mu*\widetilde\mu*\nu*\widetilde\nu)(0).
}
\]

Equivalently, for independent

\[
X,X'\sim\mu,
\qquad
Y,Y'\sim\nu,
\]

the right side is

\[
\boxed{
\Pr[X-X'+Y-Y'\equiv0\pmod N].
}
\]

For the odd-frequency half only,

\[
\boxed{
\frac1N\sum_{k\ \mathrm{odd}}
|\widehat\mu(k)|^2|\widehat\nu(k)|^2
=
\frac12\left(
\Pr[Z=0]-\Pr[Z=N/2]
\right),
}
\]

where

\[
Z=X-X'+Y-Y'\pmod N.
\]

This follows by inserting

\[
1_{k\ \mathrm{odd}}=\frac{1-(-1)^k}{2}
\]

into Fourier inversion.

The expression is nonnegative, so necessarily the displayed difference of collision probabilities is nonnegative.

## 7. New Stage 4 target

For a ternary selector \(\mu\) and deterministic boundary fibre \(\nu_F\), the remaining harmonic problem can therefore be replaced by a static additive problem:

> bound the probability that a ternary selector difference is cancelled by a plateau-fibre difference modulo the current dyadic modulus, with the half-modulus collision subtracted automatically in the odd shell.

The selector difference has the form

\[
\sum_i c_i3^i,
\qquad c_i\in\{-1,0,1\},
\]

while a boundary-fibre difference has the form

\[
\sum_{j\in F}d_j2^j3^{-\ell_j}\pmod{2^{L+1}},
\qquad d_j\in\{-1,0,1\},
\]

with all \(j\) distinct.

Thus the open cross-base theorem is now a collision/transversality theorem between two explicit additive difference systems, rather than a generic Fourier-mixing statement.

This formulation is especially compatible with the existing residue-maximality, Hensel, and same-integer overlap machinery.

## 8. Reproducibility

Regression certificate:

`collatz/src/distinct_dyadic_depth_odd_frequency_orthogonality_certificate.py`

The certificate checks the exact valuation obstruction on a finite grid.  The theorem itself is the symbolic valuation proof above.
