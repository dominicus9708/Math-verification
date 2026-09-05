# Gate S reduction: selector discrepancy threshold and harmonic accumulation

Date: 2026-09-06

Status: **SAFE CONDITIONAL REDUCTION + FINITE DIAGNOSTIC + OPEN ASYMPTOTIC SPECTRAL GATE.**

This note continues the Beatty one-child exposure + selector repair bridge.  The previous sufficient condition

\[
\inf_L \rho_L>\frac13,
\qquad
\rho_L=\frac{h_{\min}(L)}{h_{\max}(L)},
\]

is stronger than necessary.  Here it is reduced first to one-sided selector discrepancy and then to a Fourier-tail sufficient condition.

Nothing in this note proves the Collatz conjecture.  The asymptotic selector-discrepancy estimate, exact-fibre compatibility, and terminal Gate C remain open.

---

## 1. One-sided selector discrepancy

Let `h_L(x)` be the exact selector multiplicity on the finite child fibre used at scale `L`, with positive mean

\[
\bar h_L>0.
\]

Assume one-sided relative bounds

\[
h_L(x)\ge (1-d_L)\bar h_L,
\qquad
h_L(x)\le (1+u_L)\bar h_L,
\]

where

\[
0\le d_L\le1,
\qquad
u_L:=u_L\ge0.
\]

To avoid conflict with the Collatz iterate, below we continue to write the upper discrepancy as `u_L`.

Then

\[
h_{\min}(L)\ge(1-d_L)\bar h_L,
\qquad
h_{\max}(L)\le(1+u_L)\bar h_L,
\]

so

\[
\boxed{
\rho_L
\ge
\frac{1-d_L}{1+u_L}.
}
\]

The earlier Beatty-repair bridge has rise-step loss coefficient

\[
\kappa_L=\frac{3\rho_L-1}{10}.
\]

Therefore

\[
\boxed{
\kappa_L
\ge
\frac{2-3d_L-u_L}{10(1+u_L)}.
}
\]

Hence a positive one-rise contraction is guaranteed whenever

\[
\boxed{
3d_L+u_L<2.
}
\]

This asymmetric form is sharper than a symmetric `L^\infty` discrepancy bound: a depressed minimum is three times as costly as an inflated maximum in this particular repair inequality.

Status: **SAFE LEMMA.**

---

## 2. Symmetric discrepancy corollary

Define

\[
\varepsilon_L
:=
\frac{\|h_L-\bar h_L\|_\infty}{\bar h_L}.
\]

If `0<=epsilon_L<1`, then

\[
d_L,u_L\le\varepsilon_L,
\]

and therefore

\[
\rho_L
\ge
\frac{1-\varepsilon_L}{1+\varepsilon_L}.
\]

The rise-step loss coefficient obeys

\[
\boxed{
\kappa_L
\ge
\frac{1-2\varepsilon_L}{5(1+\varepsilon_L)}.
}
\]

Thus

\[
\boxed{
\varepsilon_L<\frac12
}
\]

is a sufficient condition for positive contraction at that rise.

This is only a sufficient threshold; it is not necessary because the asymmetric condition `3d_L+u_L<2` can hold even when the symmetric discrepancy exceeds `1/2`.

Status: **SAFE LEMMA.**

---

## 3. Uniform control is not necessary

Let `R` denote the Beatty rise set.  The cumulative bridge only needs the sum of positive rise losses to diverge.

From the asymmetric bound, a sufficient condition is

\[
\boxed{
\sum_{L\in R}
\frac{(2-3d_L-u_L)_+}{(1+u_L)L}
=+\infty.
}
\]

The irrelevant constant factor `1/10` has been removed.

From the symmetric bound, it is enough that

\[
\boxed{
\sum_{L\in R}
\frac{(1-2\varepsilon_L)_+}{(1+\varepsilon_L)L}
=+\infty.
}
\]

Again the constant factor `1/5` is irrelevant to divergence.

Therefore the old target

\[
\inf_L\rho_L>\frac13
\]

can be replaced by a strictly weaker **harmonic good-scale condition**.  Bad scales, including scales with `rho_L<=1/3`, are allowed provided sufficiently many rise scales retain enough positive margin.

Status: **SAFE CONDITIONAL LEMMA**, subject to the same exact-fibre and normalized non-expansion hypotheses as the cumulative bridge.

---

## 4. Fourier-tail sufficient condition

Let the exact selector multiplicity `h_L` live on a finite cyclic group `G_L` of size `M_L`.  Use the normalized discrete Fourier transform

\[
\widehat h_L(t)
=
\frac1{M_L}
\sum_{x\in G_L}
h_L(x)e^{-2\pi i tx/M_L}.
\]

Then

\[
\widehat h_L(0)=\bar h_L
\]

and Fourier inversion gives

\[
h_L(x)-\bar h_L
=
\sum_{t\ne0}
\widehat h_L(t)e^{2\pi i tx/M_L}.
\]

Consequently

\[
\|h_L-\bar h_L\|_\infty
\le
\sum_{t\ne0}|\widehat h_L(t)|.
\]

Define the normalized nonzero Fourier-tail ratio

\[
\boxed{
\Theta_L
:=
\frac{\sum_{t\ne0}|\widehat h_L(t)|}
{\widehat h_L(0)}.
}
\]

Then

\[
\boxed{
\varepsilon_L\le\Theta_L.
}
\]

Hence `Theta_L<1/2` is a sufficient Gate-S condition at a rise, with

\[
\boxed{
\kappa_L
\ge
\frac{1-2\Theta_L}{5(1+\Theta_L)}.
}
\]

A sufficient cumulative condition is therefore

\[
\boxed{
\sum_{L\in R}
\frac{(1-2\Theta_L)_+}{(1+\Theta_L)L}
=+\infty.
}
\]

Status: **SAFE FOURIER REDUCTION** for the exact selector function `h_L` under the stated DFT normalization.

The same dimensionless inequality can be rewritten for an unnormalized DFT, because both numerator and zero mode acquire the same scaling factor.

---

## 5. Important compatibility warning with the existing Fourier transfer

The repository already contains

- `collatz/src/ballot_fourier_transfer.py`, and
- `collatz/src/beatty_boundary_fourier_transfer.py`.

These programs compute normalized Fourier coefficients of the coefficient-survival residue language / oriented Beatty boundary.  They are useful diagnostics for spectral cancellation.

However, this note requires the Fourier transform of the **exact selector multiplicity `h_L` on the same candidate fibre used by the one-child repair lemma**.

Therefore the implication

\[
\text{observed decay in `ballot_fourier_transfer.py`}
\Longrightarrow
\Theta_L<\frac12
\]

is **NOT YET A THEOREM**.

A transfer/identification lemma must first prove that the computed normalized character sums represent, dominate, or combine with the exact selector multiplicity in the way required by Section 4.

This is part of Gate F (exact fibre/global conditioning compatibility).

---

## 6. Why fixed-frequency decay is insufficient

The 2026-08-09 Fourier-transfer record observed strong numerical decay for fixed low odd frequencies and explicitly warned that this does not establish a uniform spectral gap.

The present reduction makes the reason sharper.  Gate S needs an `l^1` Fourier-tail control

\[
\sum_{t\ne0}|\widehat h_L(t)|,
\]

not merely smallness of each of finitely many selected frequencies.

If the modulus grows, the number of nonzero frequencies also grows.  Thus even a pointwise estimate

\[
|\widehat h_L(t)|\le 2^{-cL}\widehat h_L(0)
\]

is useful for the full `l^1` tail only if the number of frequencies to which it is applied grows slowly enough, or if the spectrum is split into regions controlled by different mechanisms.

This matches the earlier **spectral complementarity** program:

1. high `2`-adic valuation frequencies: exact Riesz-product attenuation;
2. low frequencies: ballot-transfer cancellation candidate;
3. middle frequencies: still need a uniform bridge/estimate.

The new contribution is that the spectral program now has a concrete target threshold: it does not need full equidistribution; it only needs enough rise scales with `Theta_L<1/2` and divergent harmonic margin.

---

## 7. Finite min/max diagnostics

Existing exact finite selector extrema give the following ratios:

\[
\begin{array}{c|c|c}
\text{case}&\rho=h_{\min}/h_{\max}&
\varepsilon_{\mathrm{proxy}}=(1-\rho)/(1+\rho)\\\hline
H24\_full&0.9972718937&0.0013659163\\
H25\_full&0.9956608777&0.0021742784\\
H24,Q7&0.9557318856&0.0226350630\\
H24,Q8&0.9403365328&0.0307490305\\
H24,Q9&0.9116961789&0.0461913467\\
H25,Q7&0.9352951604&0.0334340936
\end{array}
\]

Here `epsilon_proxy` is only the symmetric spread proxy that reconstructs the same min/max ratio:

\[
\rho=
\frac{1-\varepsilon_{\mathrm{proxy}}}
{1+\varepsilon_{\mathrm{proxy}}}.
\]

It is **not** asserted to equal the true discrepancy from the actual mean unless the extrema happen to be symmetric about that mean.

All tested finite ratios are far above the critical `rho=1/3`, equivalently their spread proxies are far below `1/2`.  This is encouraging finite evidence only.

Reproducibility algebra certificate:

`collatz/src/selector_discrepancy_gateS_certificate.py`

---

## 8. DSD analysis — structural compression

The proof-attempt dependency can now be compressed as

\[
\boxed{
\begin{array}{c}
\text{exact selector multiplicity on canonical fibre}\\
\Downarrow\\
\text{one-sided discrepancy }(d_L,u_L)
\quad\text{or Fourier tail }\Theta_L\\
\Downarrow\\
3d_L+u_L<2
\quad\text{or}\quad
\Theta_L<1/2\\
\Downarrow\\
\text{Beatty-rise loss }\asymp 1/L\\
\Downarrow\\
\text{harmonic good-scale accumulation}\\
\Downarrow\\
\text{candidate-mass decay}\\
\Downarrow\\
\text{Gate C: eliminate a single nested integer path}
\end{array}
}
\]

This removes the unnecessary requirement of global uniform equidistribution.

---

## 9. DSD audit

### SAFE

1. `rho >= (1-d)/(1+u)` from one-sided relative extrema.
2. Positive repair threshold is exactly `3d+u<2` for the lower-bound ratio.
3. Symmetric sufficient threshold is `epsilon<1/2`.
4. Uniform control can be weakened to divergence of positive harmonic margins.
5. Fourier `l^1` tail bounds relative `L^infinity` discrepancy by inversion and the triangle inequality.

### FINITE ONLY

1. H24/H25 min/max ratios.
2. Existing fixed-frequency Fourier decay observations.
3. Existing boundary Fourier scans.

### OPEN GATE S

Prove a growing-scale theorem giving either

\[
\sum_{L\in R}
\frac{(2-3d_L-u_L)_+}{(1+u_L)L}=\infty,
\]

or the Fourier sufficient version

\[
\sum_{L\in R}
\frac{(1-2\Theta_L)_+}{(1+\Theta_L)L}=\infty.
\]

### OPEN GATE F

Identify/control the exact selector multiplicity on the same growing canonical fibres as the Beatty boundary and repair lemma.  Fixed-Q compatibility cannot be silently promoted to growing-Q compatibility.

### OPEN GATE C

Even after candidate mass tends to zero, exclude the possibility of one nested canonical residue path arising from a fixed positive integer counterexample.

### PROHIBITED UPGRADES

1. Do not infer an `l^1` Fourier-tail bound from finitely many low-frequency coefficients.
2. Do not infer asymptotic Gate S from H24/H25 extrema.
3. Do not replace the exact selector multiplicity by the coefficient-survival distribution without Gate-F compatibility.
4. Do not conclude set emptiness from density/mass decay alone.

---

## 10. Next target

The highest-value next step is **not** to demand full spectral equidistribution.

First attempt the weakest sufficient statement:

\[
\boxed{
\sum_{L\in R}
\frac{(1-2\Theta_L)_+}{(1+\Theta_L)L}=\infty
}
\]

for an exact selector transform, possibly by decomposing the spectrum into low-, middle-, and high-valuation regions and using the existing spectral-complementarity mechanisms.

If direct `l^1` control is too expensive, return to the asymmetric spatial target `3d_L+u_L<2`, because min/max convolution estimates may close Gate S without a full Fourier theorem.
