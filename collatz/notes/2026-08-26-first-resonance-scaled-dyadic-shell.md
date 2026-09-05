# First resonance: displacement is the exact dyadic height shell

Date: 2026-08-26

Status: **exact Farey/scaled-state theorem inside the repaired first-global-resonance branch.** This does not prove the Collatz conjecture.

## 1. Setup

Use the first-resonance time/odd ratio

\[
{A\over Q}={114208327604\over72057431991}.
\]

Its ordered Farey neighbours in the Christoffel root split are

\[
{A_U\over Q_U}
={103768467013\over65470613321}
\]

and

\[
{A_S\over Q_S}
={10439860591\over6586818670}.
\]

Let

\[
\gamma=\log_2 3,
\qquad
\gamma_B=\log_2(3+1/B),
\qquad
B=2^{71}.
\]

Exact logarithmic certificates give

\[
\boxed{
{A_U\over Q_U}<\gamma<{A\over Q}<\gamma_B<{A_S\over Q_S}.
}
\]

Both adjacent determinants are one:

\[
AQ_U-A_UQ=1,
\qquad
A_SQ-AQ_S=1.
\]

## 2. Universal proper-prefix time strip

For `1<=j<Q`, put

\[
A_j=\left\lfloor{jA\over Q}\right\rfloor.
\]

Because `A_U/Q_U` and `A/Q` are Farey neighbours and `gamma` lies between them, no rational with denominator below `Q` can lie between `gamma` and `A/Q`. Therefore

\[
\boxed{A_j=\lfloor j\gamma\rfloor.}
\]

Similarly `A/Q` and `A_S/Q_S` are Farey neighbours and `gamma_B` lies between them. If

\[
A_j+1\le j\gamma_B,
\]

then `(A_j+1)/j` would lie strictly between `A/Q` and `A_S/Q_S` with denominator `j<Q`, contradicting Farey adjacency. Hence

\[
\boxed{j\gamma_B<A_j+1.}
\]

Thus every proper odd prefix lies in the exact strip

\[
\boxed{
\lfloor j\log_2 3\rfloor
=A_j
<j\log_2(3+1/B)
<A_j+1.
}
\]

## 3. Scaled-state shell

Let `x_j` be the actual odd state after `j` odd events, let `d_j` be its displacement from the mechanical odd position, and let

\[
z_j={x_j\over2^{d_j}}.
\]

The exact one-step identity from the scaled-state theorem gives

\[
{z_j\over N}
=\prod_{i<j}{3+1/x_i\over2^{g_i}}.
\]

A minimal-counterexample prefix has `x_i>N>B`. Therefore

\[
{3^j\over2^{A_j}}
<
{z_j\over N}
<
{(3+1/B)^j\over2^{A_j}}.
\]

The proper-prefix strip implies

\[
1<{3^j\over2^{A_j}}
\]

and

\[
{(3+1/B)^j\over2^{A_j}}<2.
\]

Consequently

\[
\boxed{N<z_j<2N\qquad(1\le j<Q).}
\]

## 4. Exact meaning of displacement

Since

\[
x_j=2^{d_j}z_j,
\]

we obtain

\[
\boxed{
2^{d_j}N<x_j<2^{d_j+1}N.
}
\]

Therefore

\[
\boxed{
d_j=\left\lfloor\log_2{x_j\over N}\right\rfloor.}
\]

The displacement descriptor is not merely a combinatorial distance from the mechanical word. It is the exact dyadic height shell of the actual odd state relative to the minimal-counterexample start.

In particular:

- `d_j=0` iff `N<x_j<2N`;
- `d_j=1` iff `2N<x_j<4N`;
- and so on.

## 5. Consequence for the Bellman state

The ordering-debt variable now has an arithmetic interpretation:

\[
\boxed{
\text{positive displacement excursion}
=\text{odd orbit excursion above the base dyadic shell }[N,2N).
}
\]

The previously certified debt-excursion reserve cost can therefore be understood as a cost attached to leaving and later re-entering the base dyadic shell.

This does not by itself prove that such excursions are impossible. Its value is that it identifies the control variable with an observable arithmetic scale and removes an artificial degree of freedom from the DSD proof description.

## 6. DSD chain

The descriptor chain is now

\[
\boxed{
\text{mechanical position defect }d_j
\longleftrightarrow
\text{scaled state }z_j
\longleftrightarrow
\text{actual dyadic orbit shell of }x_j.
}
\]

Thus later Bellman inequalities can be stated either in combinatorial displacement language or directly as statements about excursions of the actual odd orbit through dyadic shells.

Companion certificate:

`collatz/src/first_resonance_scaled_dyadic_shell_certificate.py`.
