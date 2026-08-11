# Two-sided continued-fraction filter for nearest-layer renewals

Date: 2026-08-11

Status: **exact consequence of the nearest-critical-layer reduction, renewal product, Christoffel upper bound, and Legendre's continued-fraction criterion**.

## 1. Setup

Let

\[
\alpha:=\log_2(3/2),
\qquad
f_H:=\{\alpha H\}\in(0,1).
\]

The two economical renewal layers are

\[
D_-(H)=\lfloor\alpha H\rfloor,
\qquad
D_+(H)=\lceil\alpha H\rceil.
\]

Let consecutive renewal floors be

\[
N<N',
\qquad
g:=N'-N.
\]

## 2. Lower critical layer

Assume

\[
D=\lfloor\alpha H\rfloor.
\]

Then

\[
D-\alpha H=-f_H,
\]

so the aggregate multiplier is

\[
\boxed{P=2^{-f_H}.}
\]

The exact renewal product satisfies

\[
P\frac{N'}N=Q,
\qquad Q>1.
\]

Therefore

\[
\frac{N'}N>\frac1P=2^{f_H},
\]

hence

\[
\boxed{
f_H<\log_2\left(1+\frac gN\right).
}
\]

### Legendre alternative

Let the rational

\[
\frac{\lfloor\alpha H\rfloor}{H}
\]

be reduced before applying continued-fraction theory. If its reduced form is not a convergent of `alpha`, Legendre's theorem gives

\[
\left|
\alpha-
\frac{\lfloor\alpha H\rfloor}{H}
\right|
\ge
\frac1{2H^2}.
\]

Since the left side is `f_H/H`,

\[
\boxed{f_H\ge\frac1{2H}.}
\]

Combining with the floor-ratio inequality,

\[
\boxed{
\frac gN
>
2^{1/(2H)}-1.
}
\]

Thus every lower-critical renewal satisfies the dichotomy

\[
\boxed{
\begin{array}{ll}
\text{lower CF resonance:}&(\lfloor\alpha H\rfloor/H)_{\rm red}\text{ is a convergent of }\alpha,\\[1mm]
\text{gap overload:}&g>N\left(2^{1/(2H)}-1\right).
\end{array}
}
\]

For large `H`,

\[
\boxed{
gH>\left(\frac{\ln2}{2}+o(1)\right)N
\approx(0.34657+o(1))N.}
\]

## 3. Upper critical layer

Assume

\[
D=\lceil\alpha H\rceil.
\]

Put

\[
\delta_H:=1-f_H
=\lceil\alpha H\rceil-\alpha H.
\]

The Christoffel renewal-shadow bound gives

\[
\delta_H
<
H\log_2\left(1+\frac1{3N'}\right).
\]

If the reduced rational

\[
\frac{\lceil\alpha H\rceil}{H}
\]

is not a convergent of `alpha`, Legendre yields

\[
\delta_H\ge\frac1{2H}.
\]

Therefore

\[
\log_2\left(1+\frac1{3N'}\right)
>
\frac1{2H^2},
\]

and so

\[
\boxed{
N'
<
\frac{1}{3\left(2^{1/(2H^2)}-1\right)}.
}
\]

Asymptotically,

\[
\boxed{
N'
<
\left(\frac{2}{3\ln2}+o(1)\right)H^2
\approx(0.9618+o(1))H^2.
}
\]

Hence every upper-critical renewal satisfies

\[
\boxed{
\begin{array}{ll}
\text{upper CF resonance:}&(\lceil\alpha H\rceil/H)_{\rm red}\text{ is a convergent of }\alpha,\\[1mm]
\text{quadratic-floor overload:}&N'=O(H^2).
\end{array}
}
\]

## 4. Unified economical hard core

Suppose a renewal transition avoids all previously identified macroscopic costs:

- no floor doubling;
- no linear-depth overload;
- no lower-layer gap overload;
- no upper-layer quadratic-floor overload.

Then it must lie on one of the two nearest critical layers, and its corresponding rational approximation to `alpha` must be a continued-fraction convergent.

Thus the residual economical renewal language is supported on the sparse two-sided convergent structure of

\[
\boxed{\alpha=\log_2(3/2).}
\]

The remaining global problem is not to control arbitrary exponent pairs `(H,D)`, but to show that an exact positive-integer Collatz renewal chain cannot indefinitely concatenate these sparse lower/upper optimal-approximation layers while keeping all renewal floors valid.
