# Spectral exception splitting for ternary--Beatty transport

Date: 2026-08-13

Status: **exact finite-group inequality**. It replaces a uniform Fourier-mixing requirement by a complementary two-channel requirement: the ternary selector spectrum must be small on a large good set, while the coefficient-survivor / Beatty-boundary spectrum only needs to be small on the remaining sparse exceptional frequencies. This is a reduction theorem, not a Collatz proof.

## 1. Generic subset discrepancy identity

Let `G=Z/NZ`, let `mu` be a probability measure on `G`, and let `A subset G` have density

\[
a:=\frac{|A|}{N}>0.
\]

Use the normalized character transform

\[
\widehat\mu(k)
=\sum_{x\in G}\mu(x)e^{-2\pi ikx/N}
\]

and the normalized transform of the set

\[
\rho_A(k)
:=\frac1{|A|}
\sum_{x\in A}e^{-2\pi ikx/N}.
\]

Fourier inversion gives

\[
\boxed{
\frac{\mu(A)}a
=1+
\sum_{k\ne0}
\widehat\mu(k)
\overline{\rho_A(k)}.
}
\]

Parseval for the normalized set transform gives

\[
\boxed{
\sum_{k\in G}|\rho_A(k)|^2
=\frac1a.
}
\]

## 2. Good/exceptional frequency split

Partition the nonzero frequencies into

\[
G\setminus\{0\}
=\mathcal G\dot\cup\mathcal E.
\]

Assume

\[
\boxed{
\eta
:=
\sum_{k\in\mathcal G}
|\widehat\mu(k)|^2
}
\]

and define

\[
\boxed{
\tau_A
:=
\max_{k\in\mathcal E}
|\rho_A(k)|,
\qquad
m:=|\mathcal E|.
}
\]

Since `|widehat mu(k)|<=1`, Cauchy--Schwarz on the good set and the triangle inequality on the exceptional set yield

\[
\begin{aligned}
\left|
\frac{\mu(A)}a-1
\right|
&\le
\sqrt{
\sum_{k\in\mathcal G}|\widehat\mu(k)|^2
}
\sqrt{
\sum_{k\in\mathcal G}|\rho_A(k)|^2
}
+
\sum_{k\in\mathcal E}|ho_A(k)|\\
&\le
\boxed{
\sqrt{\frac\eta a}+m\tau_A.
}
\end{aligned}
\]

Thus no uniform Fourier decay of `mu` is required.

## 3. Application to coefficient-survivor and boundary mass

At reduced parent modulus `M=2^(L-2)`, let

\[
R_L\subseteq\mathbb Z/M\mathbb Z
\]

be the coefficient-survivor set and

\[
B_L\subseteq R_L
\]

the one-child Beatty boundary.

Put

\[
\sigma_L=|R_L|/M,
\qquad
\beta_L=|B_L|/M.
\]

For the normalized ternary selector measure `mu`, the generic inequality gives

\[
\boxed{
\frac{C_L}{2^d}
\le
\sigma_L
\left(1+\delta_R\right),
}
\]

\[
\boxed{
\frac{D_L}{2^d}
\ge
\beta_L
\left(1-\delta_B\right),
}
\]

where one may take

\[
\delta_R
=
\sqrt{\eta_R/\sigma_L}
+m_R\tau_R,
\]

\[
\delta_B
=
\sqrt{\eta_B/\beta_L}
+m_B\tau_B.
\]

The good/exceptional partitions may be chosen differently for the two tests if useful.

## 4. Oriented boundary correlation

Now work on the child group `Z/(2M)Z`. Let `w_L` be the anti-periodic orientation function:

\[
w_L(r)=v(r),
\qquad
w_L(r+M)=-v(r),
\]

on the boundary pairs and zero elsewhere.

Normalize its Fourier transform by the total absolute boundary support:

\[
\boxed{
\rho_w(k)
:=
\frac{\widehat w_L(k)}{2|B_L|}.
}
\]

Since `w_L` is anti-periodic, only odd frequencies contribute.

The exact signed transport correction satisfies

\[
\boxed{
\frac{K_L}{2^d\beta_L}
=
\sum_{k\ {m odd}}
\widehat\mu_{2M}(k)
\overline{\rho_w(k)}.
}
\]

Also Parseval gives

\[
\boxed{
\sum_{k\ {m odd}}|\rho_w(k)|^2
=\frac1{\beta_L}.
}
\]

Split the odd frequencies into good and exceptional sets. If

\[
\eta_w
=
\sum_{k\in\mathcal G_w}
|\widehat\mu_{2M}(k)|^2,
\]

\[
\tau_w
=
\max_{k\in\mathcal E_w}
|\rho_w(k)|,
\qquad
m_w=|\mathcal E_w|,
\]

then exactly as before,

\[
\boxed{
\frac{|K_L|}{2^d\beta_L}
\le
\sqrt{\frac{\eta_w}{\beta_L}}
+m_w\tau_w.
}
\]

## 5. One common error parameter

Suppose the three normalized errors satisfy

\[
\delta_R\le\delta,
\qquad
\delta_B\le\delta,
\qquad
\delta_w\le\delta
\]

for some

\[
0<\delta<\frac12.
\]

Then

\[
D_L-|K_L|
\ge
2^d\beta_L(1-2\delta)
\]

and

\[
C_L
\le
2^d\sigma_L(1+\delta).
\]

Therefore

\[
\boxed{
\frac{D_L-|K_L|}{C_L}
\ge
\frac{1-2\delta}{1+\delta}
\frac{\beta_L}{\sigma_L}.
}
\]

Inserted into

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2},
\]

this yields

\[
\boxed{
C_{L+1}
\le
C_L\left[
1-
\frac12
\frac{1-2\delta}{1+\delta}
\frac{\beta_L}{\sigma_L}
\right].
}
\]

## 6. Why this is stronger than uniform selector mixing

A uniform selector-mixing strategy asks `widehat mu(k)` to be small at every nonzero frequency.

The present lemma allows a sparse exceptional family `E` on which selector Fourier coefficients may be large. It is sufficient that the relevant set/orientation transforms be small on those frequencies.

This fits the arithmetic structure of the affine selector walk:

- Fourier frequencies with many base-3 digit changes are naturally damped by the selector Riesz product / affine-walk mechanism;
- exceptional frequencies with very few base-3 digit changes form a much smaller structured family;
- the Beatty survivor and boundary transfer can be studied directly on that exceptional family.

Thus the terminal target can be spectral **complementarity** rather than uniform equidistribution.

## 7. Exact next target

Choose an exceptional family `E_L`, for example frequencies whose relevant base-3 expansion has at most `A` digit changes.

A sufficient growing-resolution theorem would establish simultaneously

\[
\sum_{k\notin E_L}|\widehat\mu(k)|^2
=o(\beta_L),
\]

and

\[
|E_L|
\max_{k\in E_L}
\left(
|\rho_{R_L}(k)|
+|\rho_{B_L}(k)|
+|\rho_{w_L}(k)|
\right)
=o(1).
\]

Under a positive lower bound or even the previously proved harmonic lower bound for `beta_L/sigma_L`, the mass-transport theorem then forces repeated global contraction without enumerating starts.
