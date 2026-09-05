# Nested dyadic-resolution carry tower

Date: 2026-08-26

Status: **exact projection identity and state-space reduction.**  The varying dyadic moduli appearing in deterministic Beatty-boundary cube factors are compatible projections of one inverse-three orbit at a chosen maximal dyadic resolution.  This turns the current boundary problem into a multi-resolution observation of one carry trajectory rather than unrelated trajectories at unrelated moduli.  It is not a Collatz proof.

## 1. Maximal-resolution inverse-three orbit

Fix a maximal dyadic resolution

\[
M_R=2^R
\]

and an odd frequency \(u\pmod{2^R}\).

Define

\[
B_i^{(R)}
:=
\operatorname{cent}_{2^R}(u3^{-i}),
\qquad i\ge0.
\]

For every lower resolution \(r\le R\), define

\[
B_i^{(r)}
:=
\operatorname{cent}_{2^r}(u3^{-i}).
\]

Let

\[
\pi_r(x):=\operatorname{cent}_{2^r}(x)
\]

be centered reduction to the lower dyadic quotient.

## 2. Exact projection compatibility

Because reduction modulo \(2^r\) commutes with multiplication by the odd unit \(3^{-1}\),

\[
B_i^{(R)}
\equiv
u3^{-i}\pmod{2^R}
\]

implies

\[
B_i^{(R)}
\equiv
u3^{-i}\pmod{2^r}.
\]

Taking the unique centered representative gives

\[
\boxed{
B_i^{(r)}
=
\pi_r\!\left(B_i^{(R)}\right)
}
\]

for every

\[
0\le i,
\qquad r\le R.
\]

Thus all lower-resolution inverse-three trajectories are exact projections of one maximal-resolution trajectory.

## 3. Boundary factors as observations of the carry tower

In one deterministic Beatty-boundary cube at total child depth \(L+1\), a plateau coordinate beginning at position \(j\) uses the effective modulus

\[
M_j=2^{L+1-j}.
\]

Set

\[
R=L+1,
\qquad r_j=R-j.
\]

If \(\ell_j\) is the one ordinal attached to that plateau coordinate, the reverse-carry conjugacy gives

\[
\left|
\cos\!\left(
\pi u\frac{[3^{-\ell_j}]_{2^{r_j}}}{2^{r_j}}
\right)
\right|
=
\left|
\cos\!\left(
\pi\frac{B_{\ell_j}^{(r_j)}}{2^{r_j}}
\right)
\right|.
\]

Using projection compatibility,

\[
\boxed{
\left|
\cos\!\left(
\pi u\frac{[3^{-\ell_j}]_{2^{r_j}}}{2^{r_j}}
\right)
\right|
=
\left|
\cos\!\left(
\pi
\frac{\pi_{r_j}(B_{\ell_j}^{(R)})}{2^{r_j}}
\right)
\right|.
}
\]

Therefore every boundary-cube factor is an observation of the same maximal-resolution inverse-three orbit, taken at a coordinate-dependent dyadic resolution.

## 4. Resolution-dependent reverse carry digits

At each resolution \(r\), define the reverse carry digits by

\[
3B_{i+1}^{(r)}
=
B_i^{(r)}+d_i^{(r)}2^r,
\qquad
 d_i^{(r)}\in\{-1,0,1\}.
\]

The state trajectory is shared through the exact projections

\[
B_i^{(r)}=\pi_r(B_i^{(R)}),
\]

but the carry digit itself is resolution dependent.

Hence one must not identify

\[
d_i^{(r)}
\]

with a single scale-independent digit.  The correct object is a **carry tower**

\[
\boxed{
\{d_i^{(r)}:i\ge0,\ r\le R\}
}
\]

derived from one maximal-resolution orbit.

This preserves the resolution distinction required by the DSD audit while still reducing the arithmetic state space.

## 5. Zero-suffix boundary exceptions as tower cylinders

For a boundary coordinate \((r_j,\ell_j)\) and integer \(s\le\ell_j\), the corresponding factor is at least

\[
\theta_s
=
\cos\!\left(\frac{\pi}{2\,3^s}\right)
\]

if and only if

\[
d_{\ell_j-s}^{(r_j)}
=
\cdots
=
d_{\ell_j-1}^{(r_j)}=0.
\]

Equivalently, using the maximal-resolution state,

\[
\boxed{
\left|
\pi_{r_j}
\left(B_{\ell_j}^{(R)}\right)
\right|
<
\frac{2^{r_j}}{2\,3^s}.
}
\]

Thus every dangerous boundary factor is an explicit cylinder condition on a dyadic projection of the one maximal-resolution inverse-three orbit.

## 6. Consequence for the next dynamic program

The previous formulation appeared to require one reverse carry process for every plateau coordinate.  The projection theorem reduces this to:

1. one maximal-resolution inverse-three state \(B_i^{(R)}\);
2. a deterministic resolution schedule \(r_j=R-j\);
3. projection tests \(\pi_{r_j}(B_{\ell_j}^{(R)})\) at the plateau coordinates;
4. the forward selector carry count at the corresponding selector resolution.

Accordingly the next finite-state/compressed calculation should be designed as a **multi-resolution two-sided carry transducer**, not as independent Fourier calculations at every boundary modulus.

## 7. DSD interpretation

This is a direct resolution-layer simplification.

- **underlying state:** one maximal-resolution dyadic orbit;
- **resolution map:** centered quotient \(\pi_r\);
- **channel:** forward or reverse multiplication by three;
- **observables:** resolution-dependent carry digits and central-window tests;
- **aggregation:** selector attenuation plus boundary cube attenuation.

The lower-resolution states are not new physical or arithmetic degrees of freedom.  They are quotient descriptions of the same frequency state.

This allows the proof program to reduce duplicated state variables without conflating resolutions.

Certificate:

`collatz/src/nested_dyadic_resolution_carry_tower_certificate.py`.
