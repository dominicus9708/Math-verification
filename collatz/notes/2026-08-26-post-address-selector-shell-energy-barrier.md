# Post-address selector shell-energy barrier

Date: 2026-08-26

Status: **exact finite-group identity + proof-strategy barrier.**  This note isolates what happens to the `m=45` ternary selector spectrum once the complete binary address is exposed.  It proves that the high odd-frequency shells are not a continuation of the low-shell mixing regime.  It is not a Collatz proof.

## 1. The full m=45 selector layer lies in one binary half

For

\[
N(a)=4\left(3^{45}+\sum_{i=0}^{44}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

the exact extreme values are

\[
N_{\min}=4\,3^{45}+3
=11817250826203334794575,
\]

\[
N_{\max}=6\,3^{45}+1
=17725876239305002191859.
\]

They satisfy

\[
2^{73}<N_{\min}\le N\le N_{\max}<2^{74},
\]

and the total span satisfies

\[
N_{\max}-N_{\min}=2\,3^{45}-2<2^{73}.
\]

Consequently, at modulus `2^74` all selector starts lie in the upper dyadic half and no two are siblings modulo `2^73`.  For every larger modulus `2^K`, `K>=75`, all starts lie in the lower half and again no two are siblings modulo `2^(K-1)`.

The same statement holds for either fixed 44-selector affine block, since each is a subset of the full layer.

## 2. Exact odd-shell energy after address exhaustion

Let `S` be either the full selector layer or one fixed affine block, let `A=|S|`, and let

\[
c_K(x)=\mathbf1_{S}(x),\qquad x\in\mathbb Z/2^K\mathbb Z.
\]

For unnormalised Fourier transform

\[
\widehat c_K(u)=\sum_x c_K(x)e^{-2\pi iux/2^K},
\]

the sibling-difference Parseval identity gives

\[
\sum_{u\text{ odd}}|\widehat c_K(u)|^2
=2^{K-1}\sum_{r\bmod2^{K-1}}
|c_K(r)-c_K(r+2^{K-1})|^2.
\]

For every `K>=74`, each occupied sibling pair contains exactly one selector atom.  Hence the square-sum is exactly `A`, and therefore

\[
\boxed{
E^{\rm sel}_K
:=\sum_{u\text{ odd}}|\widehat c_K(u)|^2
=2^{K-1}A,
\qquad K\ge74.
}
\]

For the normalized uniform selector measure `mu=c_K/A`,

\[
\boxed{
\sum_{u\text{ odd}}|\widehat\mu(u)|^2
=\frac{2^{K-1}}A.
}
\]

Thus:

- full `m=45` layer, `A=2^45`:
  \[
  \boxed{E^{\rm norm}_K=2^{K-46}};
  \]
- one fixed affine block, `A=2^44`:
  \[
  \boxed{E^{\rm norm}_K=2^{K-45}}.
  \]

At the address-exhaustion shell `K=74`, these are already `2^28` and `2^29`, respectively.

This is the exact spectral form of the finite-address handoff: after the selector atoms become individually resolved, global shell energy grows rather than mixes away.

## 3. Consequence for the existing H=900 low-shell Cauchy route

The existing certificate

`collatz/src/m45_h900_low_shell_cauchy_certificate.py`

controls the zero mode and all effective shells `K<=28` by selector mass/imbalance bounds plus exact survivor-shell energy.

One might try to extend the same shellwise Cauchy estimate to high `K`.  At `H=900`, `K=74`, for one fixed affine block the exact selector shell energy is

\[
E^{\rm sel}_{74}=2^{73}2^{44}.
\]

Let `E^sur_{900,74}` be the exact coefficient-survivor shell energy from the ballot/tail DP identity.  Exact integer evaluation gives

\[
E^{\rm sel}_{74}E^{\rm sur}_{900,74}>2^{1800}.
\]

Therefore the raw shellwise Cauchy bound

\[
\frac{\sqrt{E^{\rm sel}_{74}E^{\rm sur}_{900,74}}}{2^{900}}
\]

is already greater than `1` at the first completely exposed shell.  This does **not** prove that every possible spectral argument fails; it proves only that the already-used unsigned shellwise Cauchy mechanism cannot by itself bridge the post-address regime.

## 4. DSD audit: channel handoff

The calculation separates two genuinely different descriptive regimes.

### Pre-exhaustion selector channel

Before complete address exposure, many ternary selector atoms occupy the same dyadic cells.  Local mass balance and low-shell `L2` control can be useful.

### Post-exhaustion correlation channel

After `K=74`, selector atoms are individually resolved.  Marginal selector energy is necessarily large.  The remaining useful object is therefore not

\[
|\widehat\mu|^2
\]

alone but the signed cross-spectrum

\[
\widehat\mu(u)\,\overline{\widehat\rho_{\rm survivor}(u)}.
\]

Accordingly the high shells must be handled by arithmetic complementarity: boundary-excursion cancellation, forced-OO forward correction, or an equivalent same-address carry theorem.

## 5. Proof-strategy conclusion

The verified division of labour is now

\[
\boxed{
\text{low shells: mass/energy Cauchy}
\quad\longrightarrow\quad
\text{high shells: signed boundary/carry cancellation}.
}
\]

The next proof-level target is therefore not another global selector-energy estimate.  It is a signed estimate for the Beatty height-zero boundary excursion transform after the forced-OO resonant rewrite, preferably expressed in the common ternary/dyadic carry state space.

Certificate:

`collatz/src/post_address_selector_shell_energy_barrier_certificate.py`.
