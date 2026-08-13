# Renewal-profile asymptotic for the Beatty coefficient-survival boundary

Date: 2026-08-13

Status: **asymptotic profile theorem derived from shifted-lattice conditioned local estimates**. It refines the uniform positive boundary-fraction theorem by identifying the limiting boundary ratio along the irrational Beatty phase. It is a symbolic-language result, not a Collatz proof.

## 1. Notation

Put

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil\alpha L\rceil,
\qquad
\delta_L=b_L-\alpha L\in(0,1).
\]

Let `C_L^class` count binary words satisfying

\[
q_j\ge\lceil\alpha j\rceil
\qquad(1\le j\le L)
\]

and let `D_L^class` count the surviving words with terminal count `q_L=b_L`.

Tilt the fair binary-word measure to Bernoulli success probability `alpha` and define

\[
S_j=q_j-\alpha j.
\]

Then `S` is a centered finite-variance `(1,1-alpha)`-lattice random walk, and survival is exactly `tau^->L`, where

\[
\tau^-=\inf\{j\ge1:S_j\le0\}.
\]

Let `H(x)` be its strict ascending-ladder-height renewal function and put

\[
\theta=\log\frac{\alpha}{1-\alpha}>0.
\]

## 2. Exact tilted ratio

The Radon--Nikodym derivative between the fair word measure and the Bernoulli-`alpha` measure depends on a word only through its terminal centered position:

\[
\frac{dP_{1/2}}{dP_\alpha}
=A_L e^{-\theta S_L}.
\]

Therefore

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
=
\frac{
P_\alpha(\tau^->L,S_L=\delta_L)
}{
\sum_{s\ge0}e^{-\theta s}
P_\alpha(\tau^->L,S_L=\delta_L+s)
}.
}
\]

## 3. Shifted-lattice local asymptotic

Vatutin--Wachtel's lattice small-deviation theorem applies because the increment support is

\[
\{-\alpha,1-\alpha\}
=(1-\alpha)+\{-1,0\}.
\]

For endpoints `x` in the small-deviation lattice range,

\[
P_\alpha(S_L=x,\tau^->L)
\sim
\frac{c_0H(x)}{Lc_L},
\]

uniformly, where `c_L asymp sqrt(L)` and `c_0>0` depends only on the increment law.

In particular this is uniform for every fixed family

\[
x=\delta_L+s,
\qquad0\le s\le K.
\]

## 4. Uniform domination of the endpoint sum

The same paper gives the upper bound

\[
P_\alpha(S_L\in[x,x+1),\tau^->L)
\le
C\frac{H(x)}{Lc_L}
\]

for `0<x<=c_L`.

Because the shifted lattice has spacing one, the half-open interval contains exactly one permitted endpoint.

Moreover the ladder renewal function has at most linear growth:

\[
H(x)\ll1+x.
\]

Therefore

\[
\sum_{s\ge0}e^{-\theta s}H(\delta_L+s)
\]

is bounded uniformly in `delta_L in (0,1)`.

The part with `delta_L+s>c_L` is negligible after exponential weighting, using the ordinary lattice local-limit upper bound.

Hence dominated convergence can be applied to the exact tilted ratio.

## 5. Renewal profile

We obtain

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
=
F(\delta_L)+o(1),
}
\]

where

\[
\boxed{
F(\delta)
:=
\frac{H(\delta)}{
\displaystyle\sum_{s=0}^{\infty}
e^{-\theta s}H(\delta+s)
},
\qquad0<\delta<1.
}
\]

The error tends to zero uniformly along the permitted shifted-lattice endpoints used above.

## 6. Uniform positive floor

By definition of the strict ascending-ladder renewal function,

\[
H(\delta)\ge1
\qquad(0<\delta<1).
\]

The denominator is bounded above uniformly because

\[
H(\delta+s)\ll1+s
\]

and `theta>0`.

Therefore

\[
\boxed{
\inf_{0<\delta<1}F(\delta)>0.
}
\]

This recovers the previously proved existence of a constant `c_*>0` with

\[
D_L^{\rm class}/C_L^{\rm class}\ge c_*
\]

for all sufficiently large `L`.

## 7. Interpretation of finite oscillations

The Beatty phase

\[
\delta_L=1-\{\alpha L\}
\]

moves through `(0,1)` by irrational rotation.

Thus the observed finite variation in boundary ratios is naturally interpreted as sampling the fixed renewal profile `F(delta)` rather than as random fluctuation.

Close continued-fraction resonances correspond to phases `delta_L` close to one endpoint of the interval and can therefore probe near-extremal parts of the profile.

The finite value near `0.0737` observed in large dynamic-programming scans is diagnostic evidence about `inf F`; it is not asserted as the rigorous value of the infimum.

## External input

V. Vatutin and V. Wachtel, *Local probabilities for random walks conditioned to stay positive*, Probability Theory and Related Fields 143 (2009), 177--217, arXiv:0711.1302. The shifted-lattice small-deviation asymptotic is Theorem 5 and the uniform local upper bound is Lemma 19.
