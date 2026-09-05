# First resonance: shell-product squeeze

Date: 2026-08-27

Status: **exact structural identity + exact first-resonance numerical lower moment.** This note does not prove the Collatz conjecture.

## 1. Odd-event product identity

Let \(x_j\) be the actual odd state before the \(j\)-th odd shortcut and let
\(v_j\) be its exact halving valuation:

\[
x_{j+1}=\frac{3x_j+1}{2^{v_j}}.
\]

Across the first resonance,

\[
\sum_{j=0}^{Q-1}v_j=A,
\qquad x_0=N,
\qquad x_Q=y=N+g.
\]

Therefore

\[
\boxed{
\frac{y}{N}
=
\frac{3^Q}{2^A}
\prod_{j=0}^{Q-1}
\left(1+\frac1{3x_j}\right).
}
\]

Taking logarithms and writing

\[
\Lambda=A\ln2-Q\ln3>0,
\]

gives

\[
\boxed{
\sum_j\ln\left(1+\frac1{3x_j}\right)
=\Lambda+\ln(y/N)>\Lambda.
}
\]

## 2. Dyadic-shell insertion

The scaled-shell theorem gives

\[
2^{d_j}N<x_j<2^{d_j+1}N.
\]

Since \(\ln(1+u)<u\),

\[
\Lambda
<\sum_j\frac1{3x_j}
<\frac1{3N}\sum_j2^{-d_j}.
\]

Hence

\[
\boxed{
\sum_j2^{-d_j}>3N\Lambda>3\cdot2^{71}\Lambda.
}
\]

The exact rational-log certificate proves

\[
\boxed{
\sum_j2^{-d_j}>39,036,664,018.560\ldots
}
\]

and therefore

\[
\boxed{
\frac1Q\sum_j2^{-d_j}>0.541743758\ldots .
}
\]

## 3. Two-sided shell interpretation

The local factor theorem pushes the orbit away from the base shell:

\[
\text{every 49-window has at least seven }d_j>0.
\]

The present product theorem pushes in the opposite direction: the average
\(2^{-d_j}\) must remain large enough to compensate the coefficient deficit
\(2^A/3^Q>1\) and still finish at \(y>N\).

Thus the first-resonance shell sequence is squeezed between

\[
\boxed{
\text{not too much }d=0
\qquad\text{and}\qquad
\text{not too much large }d.
}
\]

This is not yet a contradiction, but it puts both Archimedean constraints on
one descriptor \(d_j\), which is the desired DSD state merge.

## 4. Next target

Combine the shell moment

\[
\sum2^{-d_j}
\]

with the exact correction functional

\[
\frac{E}{3^Q}
=
\sum_j
\frac{2^{b_j}}{3^j}
\left(1-2^{-d_j}\right)
\]

and the 49-window local language.  The next useful object is a finite-window
Bellman potential that simultaneously prices

1. shell occupancy \(d_j\),
2. mechanical weight \(2^{b_j}/3^j\), and
3. ordering debt between successive \(d_j\).
