# Spectral-correlation form of the coefficient-survivor transport error

Date: 2026-08-13

Status: **exact Fourier reformulation** of the signed transport error `K_L`. It strengthens the crude absolute-imbalance viewpoint by showing that only spectral overlap between the ternary selector measure and the oriented Beatty boundary matters. Finite numerical margins are diagnostics unless backed by the exact integer transport certificate.

## 1. Transport error

At a Beatty barrier-rise step let

\[
M=2^{L-2}
\]

be the reduced parent modulus and `2M` the child modulus.

For parent `r`, let the two ternary child masses be

\[
c_r,\qquad c_{r+M}.
\]

On a one-child coefficient-survival boundary parent, let

\[
v(r)=+1
\]

if the lower child survives and

\[
v(r)=-1
\]

if the upper child survives. Put `v(r)=0` away from the one-child boundary.

The exact signed transport correction is

\[
\boxed{
K_L=
\sum_{r=0}^{M-1}
v(r)(c_r-c_{r+M}).
}
\]

The mass transport identity is

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2}.
\]

## 2. Anti-periodic boundary orientation

Extend `v` to a function `w` on the child group

\[
G=\mathbb Z/(2M)\mathbb Z
\]

by

\[
\boxed{
w(r)=v(r),\qquad w(r+M)=-v(r).}
\]

Then

\[
w(x+M)=-w(x),
\]

and

\[
\boxed{
K_L=\sum_{x\in G}c_xw(x).
}
\]

Because `w` is anti-periodic, its discrete Fourier transform vanishes at every even frequency.

## 3. Exact odd-frequency correlation identity

Use the unnormalized transform

\[
\widehat f(k)=
\sum_{x=0}^{2M-1}
f(x)e^{-2\pi ikx/(2M)}.
\]

Parseval gives

\[
\boxed{
K_L
=\frac1{2M}
\sum_{\substack{0\le k<2M\\k\ {m odd}}}
\widehat c(k)\,\overline{\widehat w(k)}.
}
\]

Thus the transport error is not controlled by the total nonuniformity of the ternary distribution. It is controlled only by **spectral overlap on the odd frequencies selected by the child orientation**.

## 4. Boundary spectrum as a ballot character sum

On a one-child parent at a barrier rise, the surviving child is necessarily the child whose new parity symbol supplies the required additional odd count.

For odd Fourier frequency `k`, the two child characters are negatives of each other. Therefore the contribution of one boundary parent to `widehat w(k)` is twice the character of its surviving child.

Consequently

\[
\boxed{
\frac12\widehat w(k)
}
\]

is exactly the Fourier character sum over depth-`L+1` coefficient-surviving parity words that

1. end on the minimal Beatty odd count;
2. have an odd final symbol;
3. arise from a boundary parent at depth `L`.

This character sum can be evaluated by the same odd-count transfer used in `collatz/src/ballot_fourier_transfer.py`, with the final transition restricted to the odd branch and the terminal odd count fixed.

No exponential enumeration of parity residues is required for one frequency.

## 5. Cauchy--Parseval overlap bound

Let

\[
N:=2M
\]

and normalize the ternary selector distribution by its total mass `T=2^d`:

\[
\mu_x=c_x/T.
\]

Put

\[
E_L^{\rm odd}
:=
\sum_{k\ {m odd}}|\widehat\mu(k)|^2.
\]

Let `B_L` be the number of one-child **classes** at the parent boundary. Since `w` takes values `+/-1` on exactly two child residues for each such class,

\[
\sum_x|w(x)|^2=2B_L.
\]

Parseval therefore gives

\[
\sum_{k\ {m odd}}|\widehat w(k)|^2
=2NB_L.
\]

Applying Cauchy to the exact spectral correlation yields

\[
\boxed{
|K_L|
\le
T\sqrt{\frac{2B_LE_L^{\rm odd}}{N}}.
}
\]

This is already sharper than routing through the total variation imbalance `U_L`, because it uses only the boundary support rather than every surviving parent.

## 6. Full-`m=44`, `L=25` diagnostic

For the full `m=44` selector family (`T=2^44`) at the transition `25->26`:

- exact boundary class count: `B_25=108950`;
- exact weighted boundary mass:
  \[
  D_{25}=228,484,933,625;
  \]
- exact signed transport correlation:
  \[
  \boxed{K_{25}=-139,083.}
  \]

Thus

\[
\boxed{
|K_{25}|/D_{25}
\approx6.09\times10^{-7}.
}
\]

A direct numerical summation of the exact ternary Riesz product gives

\[
E_{25}^{\rm odd}\approx2.1073\times10^{-7}.
\]

The Cauchy--Parseval overlap bound then gives approximately

\[
|K_{25}|\lesssim9.21\times10^8,
\]

or

\[
|K_{25}|/D_{25}<0.00403.
\]

The exact finite certificate for contraction remains the integer calculation in `m44_full_mass_transport_certificate.cpp`; the numerical Fourier energy here is diagnostic evidence that the spectral route has substantial margin.

## 7. Spectral complementarity target

The ternary selector Riesz product is not uniformly Fourier-small at all growing binary resolutions. Conversely, the Beatty boundary spectrum is not expected to be uniformly small at every frequency.

The transport identity shows that neither separate uniform statement is necessary.

The required theorem can instead be formulated as spectral complementarity:

\[
\boxed{
\left|
\frac1N
\sum_{k\ {m odd}}
\widehat\mu_d(k)
\overline{\widehat w_L(k)}
\right|
=o\!\left(\frac{D_L}{2^d}\right)
}
\]

on a suitable growing relation `L=L(d)`.

Equivalently,

\[
\boxed{|K_L|=o(D_L).}
\]

Combined with a lower bound for the weighted Beatty boundary mass, this would make the transport step asymptotically close to the ideal half-boundary deletion

\[
C_{L+1}\approx C_L-\frac12D_L.
\]

## 8. Methodological significance

The proof target has now been reduced from an intersection of trillions of starts to an inner product of two finite harmonic objects:

\[
\boxed{
\text{ternary Riesz spectrum}
\quad\cdot\quad
\text{Beatty-boundary spectrum}.
}
\]

This is exactly the kind of cross-channel compatibility statement sought by the set/proposition/static-aggregation program: the two channels are analyzed independently and only their overlap must be controlled.
