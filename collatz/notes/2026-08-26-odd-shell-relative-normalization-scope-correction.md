# Odd-shell relative normalization audit and spectral-complementarity scope correction

Date: 2026-08-26

Status: **exact normalization identity + scope correction.**  The direct triangular near-one defect-code theorem remains valid as a normalized Fourier-decay theorem for the Beatty boundary.  What is corrected here is the stronger inference that boundary `L1` decay alone makes the relative Stage-4 repair exponentially small.  The selector Riesz product must still be used in the relative repair norm.  This note does not prove the Collatz conjecture.

## 1. Raw odd-shell identity

At parent modulus

\[
M=2^{L-2},
\]

the child modulus is `2M`.  Let

\[
C(x)=\#\{a:Y(a)\equiv x\pmod{2M}\}
\]

be the ternary selector count function with total mass `2^d`.  For a parent residue `r`, put

\[
u(r)=C(r)-C(r+M).
\]

Let `D` be a one-child dynamical boundary and let

\[
g(r)=v(r)1_D(r),\qquad v(r)\in\{-1,+1\}.
\]

Using the child-frequency convention

\[
\widehat C(s)=\sum_xC(x)\zeta^{-sx},
\qquad
G(s)=\sum_rg(r)\zeta^{sr},
\qquad
\zeta=e^{2\pi i/(2M)},
\]

the exact fresh odd-shell correlation is

\[
\boxed{
K=\sum_{r\in D}v(r)u(r)
=\frac1M\sum_{s\ {m odd}}\widehat C(s)G(s).
}
\]

This identity is unchanged.

## 2. Normalize the selector and boundary transforms

Write

\[
\boxed{
P(s):=\frac{\widehat C(s)}{2^d}
}
\]

for the normalized selector transform.  In the ternary subset-sum family this is the usual finite Riesz product up to the harmless base phase, and

\[
|P(s)|\le1.
\]

Normalize the signed dynamical boundary by its cardinality:

\[
\boxed{
\gamma(s):=\frac{G(s)}{|D|}.
}
\]

The triangular Beatty-boundary Fourier theorems naturally control this type of normalized transform.

Define the uniform selector mass expected on the one-child parent set by

\[
\boxed{
U_D:=\frac{2^d}{M}|D|.
}
\]

Then substitution into the raw identity gives the exact relative formula

\[
\boxed{
\frac{K}{U_D}
=\sum_{s\ {m odd}}P(s)\gamma(s).
}
\]

The important point is that the factor `1/M` has disappeared after normalization by the uniform one-child mass.

## 3. Relation to the actual one-child selector mass

The actual ternary mass on the one-child parents is

\[
S_D:=\sum_{r\in D}c(r),
\qquad
c(r)=C(r)+C(r+M).
\]

Therefore

\[
\boxed{
\frac{K}{S_D}
=\frac{U_D}{S_D}
\sum_{s\ {m odd}}P(s)\gamma(s).
}
\]

Thus two logically separate ingredients are sufficient for a small relative repair:

1. a noncollapse bound `S_D/U_D >= c_0>0` (or another direct comparison of actual and uniform one-child mass);
2. a small **spectral overlap sum**
   \[
   \boxed{
   \sum_{s\ {m odd}}P(s)\gamma(s).
   }
   \]

The second object, not the boundary `L1` average alone, is the sharp cross-base target.

## 4. Why boundary L1 decay alone is insufficient

The direct triangular theorem gives, schematically,

\[
\boxed{
\frac1M\sum_{s\ {m odd}}|\gamma(s)|
\le2^{-\eta L+o(L)}
}
\]

for some explicit `eta>0` on the pure Beatty boundary (and compatible late fibres).

But using only `|P(s)|<=1` gives

\[
\begin{aligned}
\left|\frac{K}{U_D}\right|
&\le\sum_{s\ {m odd}}|\gamma(s)|\\
&=M\left(\frac1M\sum_{s\ {m odd}}|\gamma(s)|\right)\\
&\le M\,2^{-\eta L+o(L)}.
\end{aligned}
\]

Since

\[
M=2^{L+O(1)},
\]

this becomes

\[
2^{(1-\eta)L+o(L)},
\]

not a decaying estimate unless the boundary exponent exceeds one.  The present direct triangular exponent is positive but intentionally tiny, so it cannot pay this normalization factor.

Therefore the inference

\[
\text{positive normalized boundary L1 decay}
\Longrightarrow
\text{small relative fresh repair}
\]

is invalid by itself.

This is a normalization issue, not a failure of the triangular defect-code theorem.

## 5. The corrected relative repair norm

The sharp absolute-value target is

\[
\boxed{
\mathcal R_L
:=
\sum_{s\ {m odd}}
|P_{d,L+1}(s)|\,|\gamma_L(s)|.
}
\]

If

\[
\mathcal R_L=o(1)
\]

and `S_D/U_D` stays bounded below, then

\[
|K|/S_D=o(1).
\]

A uniform bound `mathcal R_L <= 1-2 delta` is enough for the one-child contraction inequality; exponential decay would be stronger than necessary.

This formulation restores the original **spectral-complementarity** problem in a sharper form: the two spectra need not each have enormous decay separately; their large-frequency sets merely have to avoid one another enough that their product is summable without the factor `M`.

## 6. What the triangular theorem still contributes

The 2026-08-26 triangular near-one defect-code theorem remains useful and exact:

- it gives a finite-state/mixed-radix description of frequencies where many inverse-power boundary factors are near one;
- it proves that such near-one behaviour consumes dyadic frequency freedom;
- it proves positive normalized `L1` decay for the boundary;
- it is compatible with fixed root low-bit locks and, after the fixed-Q healing theorem, with fixed-Q root-safe backtrace conditioning up to `o(L)` contaminated sites.

What it does **not** supply alone is the missing factor `1/M` in the relative repair normalization.

Its correct next role is to constrain the exceptional frequency set on which `|gamma_L(s)|` can be large, while the forward ternary Riesz product `P(s)` is used on that same set.

## 7. Consequence for the old Stage-4 target

The earlier Stage-4 note formulated a cumulative positive repair rate against an L7 local exclusion rate.  After the 2026-08-25 later-block maximality scope correction, the L7 `7/50` number cannot be used as an unconditional deterministic later-block exclusion rate.

Accordingly the current unconditional target should not be stated as

\[
\text{odd-shell repair rate}<7/50.
\]

The root-safe target is instead to establish a direct growing-resolution contraction or a summable repair bound from valid channels, with the normalized overlap

\[
\boxed{
\mathcal R_L
=\sum_{s\ {m odd}}|P(s)|\,|\gamma_L(s)|
}
\]

as the exact spectral quantity to control on neutral-return boundaries.

## 8. Regression

Portable verifier:

`collatz/src/odd_shell_relative_normalization_regression.py`

It builds actual finite ternary subset-sum count functions and deterministic signed parent sets, then checks numerically at multiple dyadic resolutions:

1. the raw odd-shell identity;
2. the exact relative formula `K/U_D = sum P gamma`;
3. the identity `sum |gamma| = M * ((1/M) sum |gamma|)` that exposes the missing normalization factor.

The regression is an implementation check; Sections 1--5 are exact algebra.

## 9. Revised frontier

For the coefficient-surviving neutral-return branch, the immediate analytic target is now:

> prove a uniform or summable bound for
> \[
> \sum_{s\ {m odd}}|P_{d,L+1}(s)|\,|\gamma_L(s)|
> \]
> using the **forward powers** `3^i` in the selector Riesz product together with the **inverse powers** `3^{-ell}` in the triangular Beatty-boundary defect code.

This is narrower than the former vague cross-base mixing problem and correctly normalized for the child-transport repair ratio.
