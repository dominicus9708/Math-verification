# Conditional growing-resolution transport theorem for the coefficient-survival core

Date: 2026-08-13

Status: **general conditional theorem**. It proves that a quantitative Fourier-energy condition, together with the unconditional Beatty boundary lower bound, forces repeated contraction of ternary-weighted coefficient-survivor mass. The Fourier-energy hypothesis is not yet proved at arbitrary growing resolution. Thus this is a reduction theorem, not a Collatz proof.

## 1. Setup

Let

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil \alpha L\rceil,
\qquad
M=2^{L-2}.
\]

Let `R_L` be the set of reduced dyadic classes `Y mod M`, `N=4Y+3`, whose parity words satisfy

\[
q_j\ge b_j
\qquad(1\le j\le L).
\]

At a Beatty barrier-rise step

\[
b_{L+1}=b_L+1,
\]

let `B_L subset R_L` be the boundary classes with terminal odd count `q_L=b_L`.

Define class densities

\[
\boxed{
\sigma_L:=\frac{|R_L|}{M},
\qquad
\beta_L:=\frac{|B_L|}{M}.
}
\]

For a ternary selector family of size `2^d`, let `mu` be its normalized distribution on the parent group `Z/MZ` and let `C_L,D_L,K_L` be the weighted survivor mass, weighted boundary mass, and signed child-correlation term from the mass-transport theorem:

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2}.
\]

## 2. Parent Fourier discrepancy

Let

\[
E_{d,L}^{\rm par}
:=
\sum_{k=1}^{M-1}
|\widehat\mu(k)|^2.
\]

Parseval gives

\[
\sum_x\left|\mu(x)-\frac1M\right|^2
=\frac1M E_{d,L}^{\rm par}.
\]

For any subset `A subset Z/MZ` of density `a=|A|/M`, Cauchy--Schwarz yields

\[
\boxed{
\left|
\mu(A)-a
\right|
\le
\sqrt{aE_{d,L}^{\rm par}}.
}
\]

Applying this to `B_L` and `R_L`,

\[
\boxed{
\frac{D_L}{2^d}
\ge
\beta_L-\sqrt{\beta_LE_{d,L}^{\rm par}},
}
\]

\[
\boxed{
\frac{C_L}{2^d}
\le
\sigma_L+\sqrt{\sigma_LE_{d,L}^{\rm par}}.
}
\]

## 3. Odd child Fourier energy and transport correlation

At child modulus `2M`, let the normalized ternary distribution have odd-frequency energy

\[
\boxed{
E_{d,L}^{\rm odd}
:=
\sum_{k\ {m odd}}
|\widehat\mu_{2M}(k)|^2.
}
\]

The anti-periodic boundary-orientation function has squared norm `2|B_L|`. The spectral-correlation identity plus Cauchy--Parseval gives

\[
\boxed{
\frac{|K_L|}{2^d}
\le
\sqrt{\beta_LE_{d,L}^{\rm odd}}.
}
\]

## 4. One common energy hypothesis

Assume that at a barrier-rise depth

\[
\boxed{
E_{d,L}^{\rm par}
\le\varepsilon^2\beta_L,
\qquad
E_{d,L}^{\rm odd}
\le\varepsilon^2\beta_L
}
\]

for some

\[
0<\varepsilon<\frac12.
\]

Because `beta_L<=sigma_L`, Sections 2--3 imply

\[
\frac{D_L}{2^d}
\ge(1-\varepsilon)\beta_L,
\]

\[
\frac{|K_L|}{2^d}
\le\varepsilon\beta_L,
\]

and

\[
\frac{C_L}{2^d}
\le(1+\varepsilon)\sigma_L.
\]

Therefore

\[
\boxed{
\frac{D_L-|K_L|}{C_L}
\ge
\frac{1-2\varepsilon}{1+\varepsilon}
\frac{\beta_L}{\sigma_L}.
}
\]

Using the exact transport identity,

\[
\boxed{
C_{L+1}
\le
C_L\left[
1-\frac12
\frac{1-2\varepsilon}{1+\varepsilon}
\frac{\beta_L}{\sigma_L}
\right].
}
\]

## 5. Insert the unconditional Beatty boundary theorem

The cycle-lemma boundary result gives, with `b=b_L`,

\[
\boxed{
\frac{\beta_L}{\sigma_L}
\ge
\frac{2b+1-L}{L(b+1)}.
}
\]

Hence every barrier-rise step satisfying the Fourier-energy hypothesis obeys

\[
\boxed{
C_{L+1}
\le
C_L\left[
1-
\frac12
\frac{1-2\varepsilon}{1+\varepsilon}
\frac{2b_L+1-L}{L(b_L+1)}
\right].
}
\]

Asymptotically the bracket subtracts

\[
\frac12
\frac{1-2\varepsilon}{1+\varepsilon}
\frac{2\alpha-1}{\alpha}\frac1L
+O(L^{-2}).
\]

## 6. Divergent cumulative contraction

Beatty barrier rises have positive density `alpha`. Therefore, if a fixed `epsilon<1/2` version of the energy hypothesis holds on all sufficiently large rise depths of a growing-resolution family, then

\[
\sum_{\rm rises}
\frac{D_L-|K_L|}{C_L}
=\infty.
\]

The corresponding product of transport factors tends to zero:

\[
\boxed{
\prod_{\rm rises}
\left[
1-
\frac12
\frac{1-2\varepsilon}{1+\varepsilon}
\frac{\beta_L}{\sigma_L}
\right]
=0.
}
\]

Thus the ternary-weighted coefficient-survivor mass is forced downward to zero in such a growing family.

For a finite integer-valued family, once the upper bound drops below one, no coefficient-surviving member remains.

## 7. Exact size of the remaining analytic target

The cycle-lemma lower density itself has exponential scale

\[
\beta_L
\gtrsim
\frac1L
\frac{\binom L{b_L}}{2^L}.
\]

By Stirling,

\[
\log_2\beta_L
=-(1-H_2(\alpha))L+O(\log L),
\]

where

\[
1-H_2(\log_3 2)
\approx0.05004.
\]

Therefore a sufficient Fourier target is only

\[
\boxed{
E_{d,L}
\ll
2^{-0.0501L}\,\operatorname{poly}(L)^{-1}.
}
\]

The required energy decay is much weaker than square-root-scale random mixing.

## 8. Finite `m=44`, `L=25` scale

For the full `m=44` selector family at `L=25`, the exact class densities are

\[
|R_{25}|=573,162,
\qquad
|B_{25}|=108,950,
\qquad
M=2^{23}.
\]

A direct evaluation of the exact Riesz product gives diagnostically

\[
E_{44,25}^{\rm par}
\approx1.7471\times10^{-7},
\]

while

\[
\beta_{25}\approx0.0129879.
\]

Thus the finite calculation is deep inside the small-energy regime. The resulting Fourier discrepancy lower bound is

\[
D_{25}/C_{25}\ge0.189086\ldots,
\]

against the exact integer value

\[
D_{25}/C_{25}=0.190086\ldots.
\]

These numerical energy values are diagnostics; the exact finite contraction is independently certified by integer subset-sum counts.

## 9. What this theorem does and does not solve

This theorem converts the R2/coefficient-survival branch into a precise harmonic-analysis target:

\[
\boxed{
\text{prove growing-resolution Riesz energy below the Beatty boundary scale}.
}
\]

It does not prove that target. In particular, geometric lacunary sequences can retain arithmetic resonances, so an independent-random model must not be assumed without proof.

Even if coefficient survival is eliminated, paradoxical first coefficient crossings (R1) still require the separate mechanical-envelope / continued-fraction / renewal-address analysis, and nontrivial periodic cycles remain a separate branch.
