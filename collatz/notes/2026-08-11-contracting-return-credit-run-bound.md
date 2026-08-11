# Contracting-return credit-run bound

Date: 2026-08-11

Status: **exact auxiliary theorem** combining the harmonic correction corridor with the maximal `v=1` run identity. It does not prove termination.

Let `n>=3` be a fixed nonperiodic odd-event orbit with no first descent. At odd-event index `i`, let

\[
\lambda_i=\frac{2^{A_i}}{3^i},
\qquad
c_i=\frac13\sum_{j<i}\lambda_j,
\qquad
x_i=\frac{n+c_i}{\lambda_i}.
\]

The harmonic correction theorem gives

\[
\boxed{c_i=O_n(i^{1/9}).}
\]

## 1. Small state at a contracting checkpoint

If

\[
\lambda_i>1,
\]

then

\[
x_i=\frac{n+c_i}{\lambda_i}<n+c_i,
\]

so

\[
\boxed{x_i=O_n(i^{1/9}).}
\]

## 2. Exact credit-run identity

Suppose the maximal run beginning at `x_i` consists of

\[
v_i=v_{i+1}=\cdots=v_{i+\ell-1}=1,
\qquad
v_{i+\ell}\ge2.
\]

For `v=1`,

\[
x_{j+1}+1=\frac32(x_j+1).
\]

The exact maximal-run identity is

\[
\boxed{
\ell=v_2(x_i+1)-1.
}
\]

Therefore

\[
2^{\ell+1}\mid x_i+1
\]

and hence

\[
2^{\ell+1}\le x_i+1.
\]

## 3. Logarithmic run bound after contraction

Using `x_i=O_n(i^{1/9})`,

\[
2^{\ell+1}\le O_n(i^{1/9}),
\]

so

\[
\boxed{
\ell\le\frac19\log_2 i+O_n(1).
}
\]

Thus after every contracting odd-event checkpoint of a hypothetical nonperiodic first-descent counterexample, a debit event `v>=2` must occur within `O_n(log i)` odd events.

Equivalently, for the macroblock credit depth `h=ell+1`,

\[
\boxed{
h\le\frac19\log_2 i+O_n(1).}
\]

## 4. Consequence for critical macroblocks

The unique near-resonant debit associated with a credit depth `h` is

\[
d_*(h)=\left\lceil h\log_2\frac32\right\rceil.
\]

Therefore a critical macroblock beginning at a contracting return satisfies

\[
\boxed{
d_*(h)=O_n(\log i).}
\]

More precisely its leading logarithmic coefficient is at most

\[
\frac19\log_2\frac32.
\]

This does not exclude the block; it shows that the contracting-return hard core cannot immediately hide inside an arbitrarily long credit run. The next debit structure becomes visible after logarithmically many event steps.
