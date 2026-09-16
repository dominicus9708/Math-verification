# Denjoy–Koksma refinement of the mechanical-boundary correction at convergent resonances

Date: 2026-08-09

Status: **DERIVED EXTERNAL-THEOREM APPLICATION + HIGH-PRECISION FINITE CHECK**

This note uses the classical Denjoy–Koksma inequality for irrational rotations to sharpen the project’s elementary pair bound at continued-fraction convergent denominators of `alpha=log_2 3`. It does not prove Collatz/CST and does not replace the global pair bound away from these special denominators.

## 1. Mechanical correction as a rotation sum

For a first coefficient crossing with `q` odd entries, the maximal normalized correction is

\[
S^*(q)
=\sum_{i=0}^{q-1}\frac{2^{\lfloor i\log_2 3\rfloor}}{3^{i+1}}
=\frac13\sum_{i=0}^{q-1}2^{-\{i\alpha\}},
\qquad \alpha=\log_2 3.
\]

Define the 1-periodic bounded-variation function

\[
f(x)=\frac13 2^{-x},\qquad 0\le x<1.
\]

On the circle, its continuous decrease contributes variation `1/6` and the jump from the left limit `1/6` back to `1/3` contributes another `1/6`, so

\[
\boxed{\operatorname{Var}(f)=\frac13.}
\]

Also

\[
\boxed{\int_0^1f(x)\,dx=\frac1{6\ln2}.}
\]

## 2. Convergent-denominator bound

Let `p/q` be a continued-fraction convergent of `alpha`. The classical Denjoy–Koksma inequality for irrational rotation by `alpha` gives

\[
\left|
\sum_{i=0}^{q-1}f(i\alpha)
-q\int_0^1 f(x)\,dx
\right|
\le \operatorname{Var}(f).
\]

Therefore at every such denominator

\[
\boxed{
S^*(q)\le \frac{q}{6\ln2}+\frac13.
}
\]

The leading coefficient is

\[
\frac1{6\ln2}\approx0.24044917348,
\]

compared with the project’s elementary all-q pair coefficient

\[
\frac7{24}\approx0.29166666667.
\]

Thus the convergent-denominator leading constant is about `0.8243971662` times the pair-bound constant.

## 3. Consequence for a paradoxical first crossing

At

\[
\sigma=\lceil q\log_2 3\rceil,
\qquad
\delta=\frac{2^\sigma}{3^q}-1>0,
\]

a paradoxical first crossing must satisfy

\[
x\le\frac{S^*(q)}{\delta}.
\]

Hence, for an upper convergent denominator,

\[
\boxed{
x\le
\frac{q/(6\ln2)+1/3}{2^\sigma/3^q-1}.}
\]

This is a special-resonance refinement; the elementary pair bound remains the uniform fallback for arbitrary q.

## 4. Next unresolved convergent resonance

High-precision Wolfram continued-fraction computation for `log_2 3` gives the convergent

\[
\boxed{
\frac{217,976,794,617}{137,528,045,312}.
}
\]

Thus

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617.
\]

Using 100-digit arithmetic,

\[
\delta
\approx8.9865487086219626069\times10^{-13}.
\]

The previous pair bound gives

\[
x<4.4635986350232564\times10^{22}.
\]

The Denjoy–Koksma refinement gives

\[
\boxed{
x<3.6797780659000120\times10^{22}.}
\]

Since

\[
2^{75}=37,778,931,862,957,161,709,568
\approx3.7778931862957162\times10^{22},
\]

we obtain the numerically well-separated bound

\[
\boxed{x<2^{75}.}
\]

The margin is about

\[
9.8115\times10^{20},
\]

or `2.60%` of `2^75`.

Thus this resonance’s binary candidate core drops from the previous 76-bit magnitude window to 75 bits.

## 5. Finite-core diagnostics

The exact coefficient-survivor parity-word counts are

\[
|P_{75}|=31,122,659,145,833,916,004,
\]

\[
|P_{76}|=62,245,318,291,667,832,008.
\]

So the one-bit magnitude improvement exactly halves this particular raw parity-time core count. It is still far too large for flat enumeration.

Using the recursively sufficient ternary-Cantor core as a separate filter, the previous pair-bound interval above the current recursive-sufficiency lower bound contained about

\[
87,960,930,222,080
\]
core integers. A direct ternary digit-DP using the new numerical upper endpoint gives about

\[
62,672,162,783,232
\]
core integers. This is a finite diagnostic reduction only; no independence between the binary and ternary filters is assumed.

## 6. Rigor status

The Denjoy–Koksma inequality itself is classical. The algebraic reduction of `S^*(q)` to the rotation sum and the variation/integral calculation above are elementary.

For a publication-grade certificate of the specific huge convergent and the numerical inequality `x<2^75`, replace high-precision decimal evaluations of `ln 2`, `ln 3`, and the continued fraction by explicit rational interval bounds. The present margin is large, but the repository should still distinguish high-precision verification from a formally rational certificate.

## 7. Relation to the independent route

Rozier–Terracol and related parity-vector work motivate focusing on the near-resonant `(sigma,q)` pairs. The present use of Denjoy–Koksma is not a new Collatz parity theorem: it is an external irrational-rotation estimate applied to the project’s mechanical-boundary correction channel.

The independent proof program remains centered on canonical-start realization, correction gaps, logarithmic parity-time cores, min-plus/Bellman certificates, and cross-base exclusion.