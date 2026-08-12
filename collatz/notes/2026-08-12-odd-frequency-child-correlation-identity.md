# Odd-frequency spectral identity for one-bit child transport

Date: 2026-08-12

Status: **exact finite Fourier identity**. The cross-base correction in the growing-resolution child-transport theorem depends only on the odd Fourier modes at the doubled dyadic modulus. This is a sharper one-step version of the full cross-spectrum identity and isolates the precise spectral overlap that must be bounded. This does not prove Collatz.

## 1. Parent and child modulus

At reduced dyadic resolution `L`, put

\[
M:=2^{L-2}.
\]

The next binary resolution has modulus

\[
2M.
\]

For the ternary representative family

\[
Y(a)=3^{44}+\sum_{i=0}^{d-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

define the exact child-level count function

\[
\boxed{
C(x):=\#\{a:Y(a)\equiv x\pmod{2M}\},
\qquad x\in\mathbb Z/(2M)\mathbb Z.
}
\]

For a parent residue `r mod M`, its two child masses are

\[
c_0(r)=C(r),
\qquad
c_1(r)=C(r+M).
\]

The next-bit imbalance is

\[
\boxed{
u(r)=C(r)-C(r+M).
}
\]

## 2. Fourier transform at the child modulus

Let

\[
\zeta:=e^{2\pi i/(2M)}
\]

and use

\[
\widehat C(s)
:=\sum_{x=0}^{2M-1}C(x)\zeta^{-sx},
\qquad s\in\mathbb Z/(2M)\mathbb Z.
\]

Then

\[
C(x)=\frac1{2M}
\sum_{s=0}^{2M-1}\widehat C(s)\zeta^{sx}.
\]

Therefore

\[
\begin{aligned}
u(r)
&=\frac1{2M}
\sum_s\widehat C(s)\zeta^{sr}
\left(1-\zeta^{sM}\right)\\
&=\frac1{2M}
\sum_s\widehat C(s)\zeta^{sr}
\left(1-(-1)^s\right).
\end{aligned}
\]

All even frequencies vanish. Hence

\[
\boxed{
u(r)
=\frac1M
\sum_{\substack{0\le s<2M\\s\text{ odd}}}
\widehat C(s)\zeta^{sr}.
}
\]

Thus the newly revealed binary bit is carried **only by odd child-level Fourier modes**.

## 3. Exact ternary Riesz product

By separation of the ternary selector bits,

\[
\begin{aligned}
\widehat C(s)
&=\sum_{a\in\{0,1\}^d}
\zeta^{-sY(a)}\\
&=\zeta^{-s3^{44}}
\prod_{i=0}^{d-1}
\left(1+\zeta^{-s3^i}\right).
\end{aligned}
\]

Hence

\[
\boxed{
\widehat C(s)
=2^d\zeta^{-s3^{44}}P_{d,L+1}(s),
}
\]

where

\[
\boxed{
P_{d,L+1}(s)
:=\prod_{i=0}^{d-1}
\frac{1+\zeta^{-s3^i}}2.
}
\]

Its magnitude is

\[
\boxed{
|P_{d,L+1}(s)|
=\prod_{i=0}^{d-1}
\left|\cos\left(\frac{\pi s3^i}{2M}\right)\right|.
}
\]

## 4. Dynamical one-child preference spectrum

Let

\[
D_L:=\{r\in R_L:m(r)=1\}
\]

be the one-child parent set of the dangerous dyadic tree, and let

\[
v(r)\in\{-1,+1\}
\]

record which raw dyadic child survives.

Define

\[
\boxed{
g_L(r):=v(r)1_{D_L}(r).
}
\]

Its child-frequency transform is

\[
\boxed{
G_L(s):=\sum_{r=0}^{M-1}g_L(r)\zeta^{sr}.
}
\]

The cross-base term in the child-transport identity is

\[
K_L:=\sum_{r\in D_L}v(r)u(r)
=\sum_{r=0}^{M-1}g_L(r)u(r).
\]

Substituting the odd-frequency formula for `u` gives

\[
\boxed{
K_L
=\frac1M
\sum_{\substack{0\le s<2M\\s\text{ odd}}}
\widehat C(s)G_L(s).
}
\]

Equivalently,

\[
\boxed{
K_L
=\frac{2^d}{M}
\sum_{s\text{ odd}}
\zeta^{-s3^{44}}
P_{d,L+1}(s)G_L(s).
}
\]

This is the exact one-step cross-spectrum.

## 5. Why this is sharper than the full cross-spectrum

The full intersection count at resolution `L+1` involves every nonzero Fourier mode.

The **incremental** question

> how much does one newly revealed binary bit prune from the already-dangerous parent mass?

uses only odd frequencies.

Even modes encode information already visible at the parent modulus and cancel identically from the child imbalance.

Thus growing-resolution analysis does not need to re-control the entire previous spectrum at every step. It needs only the new odd-frequency shell.

This is the spectral analogue of a discrete derivative.

## 6. Parseval form

From the exact identity and Cauchy--Schwarz,

\[
\boxed{
|K_L|
\le\frac1M
\left(\sum_{s\text{ odd}}|\widehat C(s)|^2\right)^{1/2}
\left(\sum_{s\text{ odd}}|G_L(s)|^2\right)^{1/2}.
}
\]

The first factor is purely the ternary formation channel. The second is purely the dynamical one-child boundary channel.

Equivalently, in physical space,

\[
\sum_{s\text{ odd}}|\widehat C(s)|^2
=M\sum_{r=0}^{M-1}|u(r)|^2,
\]

and the corresponding half-grid Parseval identity gives the exact norm of the dynamical preference spectrum.

A useful theorem may therefore be obtained either by:

1. pointwise decay/cancellation in the odd Riesz product;
2. an averaged `L^2` estimate for those odd modes;
3. a structural spectral restriction on `G_L`;
4. or a direct physical-space bound on the correlation of `u` with `v` over `D_L`.

## 7. Coefficient-boundary specialization

Through the additive-free range of the current `m=44` block, the dangerous tree may be taken to be the pure coefficient-survivor tree

\[
q_j\ge\lceil j\log_3 2\rceil.
\]

At an active threshold increment, `D_L` consists exactly of the boundary parity words

\[
q_L=\lceil L\log_3 2\rceil.
\]

Thus `G_L(s)` is not an arbitrary set transform: it is the Fourier transform, under the finite parity-vector/2-adic address bijection, of one explicit Beatty-ballot boundary layer with a signed child orientation.

This is the next structural opportunity. If `G_L` admits a recursion or spectral norm bound reflecting that ballot structure, it can be combined directly with the explicit ternary Riesz product above.

## 8. Relation to recent dyadic-Cantor Fourier work

There is active 2025--2026 work on Fourier estimates for the middle-third Cantor measure sampled along dyadic sequences. Those results are conceptually close because the factor `P` above is the finite Cantor-measure Riesz product and the frequencies are dyadic-resolution dependent.

However no direct transfer is asserted here: the present frequencies and the coefficient-boundary spectrum have a project-specific finite-modulus orientation. A precise frequency-reversal or rescaling lemma would be required before importing an external estimate.

## 9. Proof-program target

The transport contraction requirement

\[
|K_L|\le(1-2\delta)M_D(L)
\]

can now be attacked spectrally as

\[
\boxed{
\left|
\sum_{s\text{ odd}}
\zeta^{-s3^{44}}
P_{d,L+1}(s)G_L(s)
\right|
\le
\frac{M}{2^d}(1-2\delta)M_D(L).
}
\]

The problem has therefore been reduced to an explicit overlap between:

- the odd-frequency ternary Riesz product `P`;
- the signed Fourier spectrum `G_L` of the coefficient-boundary child preference.

This is the sharp growing-resolution cross-channel object to preserve.