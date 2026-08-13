# Exact coefficient-survivor entropy and the cross-base resolution scale

Date: 2026-08-13

Status: **unconditional symbolic-language entropy theorem + proof-strategy scale benchmark**. It identifies the exact exponential growth rate of coefficient-surviving binary cylinders and shows why density/equidistribution alone would require binary resolution roughly twenty times the ternary selector depth. It does not prove arithmetic independence or Collatz.

## 1. Survivor language

Put

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil\alpha L\rceil.
\]

Let `R_L` denote the binary words / equivalent dyadic cylinders satisfying

\[
q_j\ge\lceil\alpha j\rceil
\qquad(1\le j\le L).
\]

Let

\[
C_L^{\rm class}=|R_L|.
\]

## 2. Lower bound from the Beatty boundary

The cycle-minimum rotation theorem gives

\[
D_L^{\rm class}
\ge
\frac1L\binom{L}{b_L}.
\]

Since the boundary is contained in the full survivor language,

\[
\boxed{
C_L^{\rm class}
\ge
\frac1L\binom{L}{b_L}.
}
\]

## 3. Upper bound from the terminal odd count

Every coefficient-surviving word must in particular satisfy

\[
q_L\ge b_L.
\]

Therefore

\[
C_L^{\rm class}
\le
\sum_{q=b_L}^L\binom Lq.
\]

Because `alpha>1/2`, the binomial tail is bounded by a polynomial/constant factor times its first term:

\[
\boxed{
C_L^{\rm class}
\le
\binom L{b_L}
\frac{b_L+1}{2b_L+1-L}.
}
\]

## 4. Exact entropy

Stirling's formula gives

\[
\log_2\binom L{b_L}
=H_2(\alpha)L+O(\log L),
\]

where

\[
H_2(x)
=-x\log_2x-(1-x)\log_2(1-x).
\]

The lower and upper bounds differ only by polynomial factors. Hence

\[
\boxed{
\lim_{L\to\infty}
\frac1L\log_2 C_L^{\rm class}
=H_2(\log_3 2).
}
\]

Numerically,

\[
\boxed{
H_2(\log_3 2)
\approx0.9499555272.
}
\]

Thus the coefficient-survival language has exact topological/counting entropy `H_2(alpha)`.

The density among all binary cylinders has exponential rate

\[
\boxed{
\kappa_{\rm bin}
:=1-H_2(\log_3 2)
\approx0.0500444728.
}
\]

## 5. Idealized cross-base intersection benchmark

A ternary selector family of depth `d` has

\[
2^d
\]

members.

If, purely as a benchmark, those representatives were distributed independently across the binary depth-`L` survivor set, the expected surviving number would be at the exponential scale

\[
\boxed{
2^d\,2^{-\kappa_{\rm bin}L}.
}
\]

To push this benchmark below one requires

\[
\boxed{
L>
\frac{d}{\kappa_{\rm bin}}
+O(\log d).
}
\]

Since

\[
\frac1{\kappa_{\rm bin}}
\approx19.982\ldots,
\]

the natural density-only resolution scale is roughly

\[
\boxed{L\approx20d.}
\]

This is a benchmark, not an independence theorem.

## 6. Conflict with uniform selector mixing

The selector support-size theorem gives, for modulus `2^r`,

\[
E_{d,r}
\ge2^{r-d}-1.
\]

At binary depth `L`, the reduced modulus has exponent `r=L-2`.

Thus at the density-balance scale `L~20d`,

\[
r-d\sim19d,
\]

so global selector Fourier energy is necessarily enormous. Uniform equidistribution is structurally impossible there.

Consequently the two statements together imply:

\[
\boxed{
\text{density decay alone needs very deep binary resolution,}
}
\]

while

\[
\boxed{
\text{uniform ternary-to-binary mixing fails long before that depth.}
}
\]

## 7. Required terminal mechanism

Therefore a terminal R2 argument cannot be simply

\[
\text{binary survivor density}\times\text{uniform ternary distribution}.
\]

It must use a stronger arithmetic incompatibility between the two structured address systems, for example:

1. spectral complementarity rather than uniform mixing;
2. exact dyadic canonical-lift consistency across depths;
3. `3`-adic smaller-predecessor constraints;
4. or another cross-base rigidity theorem.

In particular, the relevant theorem must remain meaningful in the sparse-support regime `L>>d`, where the selector measure cannot possibly resemble uniform measure on all binary residues.

## 8. Methodological significance

This gives a quantitative stopping rule for the proof program.

The exponentially small binary survivor density is a real theorem, but improving that density by constants is not enough. The entropy gap is only about five percent per binary bit.

The hard problem has now been isolated to the arithmetic placement of a `2^d`-point ternary set inside a dyadic survivor hierarchy of entropy about `0.95`.
