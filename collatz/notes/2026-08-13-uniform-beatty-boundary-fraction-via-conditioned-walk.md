# Uniform positive Beatty-boundary fraction via exponential tilting and conditioned-walk local estimates

Date: 2026-08-13

Status: **asymptotic theorem obtained from standard probability results**. It upgrades the earlier elementary `O(1/L)` lower bound for the coefficient-survival boundary fraction to a uniform positive constant for all sufficiently large depths. The theorem concerns the symbolic coefficient-survival language; it is not a Collatz proof.

## 1. Beatty survivor and boundary languages

Put

\[
\alpha:=\log_3 2\in(1/2,1),
\qquad
b_L:=\lceil \alpha L\rceil.
\]

For a binary word of length `L`, let `q_j` be the number of ones in its first `j` positions.

Define

\[
\mathcal R_L
:=
\{w:q_j\ge\lceil\alpha j\rceil\text{ for all }1\le j\le L\}
\]

and the terminal boundary layer

\[
\mathcal B_L
:=
\{w\in\mathcal R_L:q_L=b_L\}.
\]

Write

\[
C_L^{\rm class}:=|\mathcal R_L|,
\qquad
D_L^{\rm class}:=|\mathcal B_L|.
\]

The earlier cycle argument gives only a harmonic lower bound for `D/C`. Here we prove that the ratio is actually bounded away from zero asymptotically.

## 2. Tilt to a zero-mean random walk

Under the original counting measure, each parity digit is Bernoulli `1/2`.

Introduce instead the tilted Bernoulli law

\[
\mathbf Q(X_i=1)=\alpha,
\qquad
\mathbf Q(X_i=0)=1-\alpha,
\]

and define the centered walk

\[
\boxed{
S_j:=\sum_{i=1}^j(X_i-\alpha)=q_j-\alpha j.
}
\]

The increments have mean zero, finite positive variance

\[
\sigma^2=\alpha(1-\alpha),
\]

and support

\[
\{-\alpha,1-\alpha\}
=(1-\alpha)+\{-1,0\}.
\]

Thus the increment distribution is `(h,a)`-lattice with

\[
\boxed{h=1,\qquad a=1-\alpha.}
\]

Because `alpha` is irrational,

\[
q_j\ge\lceil\alpha j\rceil
\iff
S_j>0.
\]

Hence, with

\[
\tau^-:=\min\{j\ge1:S_j\le0\},
\]

coefficient survival is exactly

\[
\boxed{\tau^->L.}
\]

Let

\[
\delta_L:=b_L-\alpha L\in(0,1).
\]

Then the boundary event is

\[
\boxed{\{\tau^->L,\ S_L=\delta_L\}.}
\]

All possible surviving terminal positions are

\[
S_L=\delta_L+s,
\qquad s=0,1,2,\ldots.
\]

## 3. Exact Radon--Nikodym weight

Let `P` denote the original Bernoulli-`1/2` word measure and `Q` the tilted Bernoulli-`alpha` measure.

For a length-`L` word with terminal centered displacement `S_L=x`,

\[
\frac{d\mathbf P}{d\mathbf Q}
=A_L e^{-\theta x},
\]

where `A_L` depends only on `L` and

\[
\boxed{
\theta:=\log\frac{\alpha}{1-\alpha}>0.
}
\]

Therefore the common factor cancels in the boundary/survivor ratio and gives the exact identity

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
=
\frac{
\mathbf Q(\tau^->L,S_L=\delta_L)
}{
\sum_{s\ge0}
e^{-\theta s}
\mathbf Q(\tau^->L,S_L=\delta_L+s)
}.
}
\]

This is the key reduction: the combinatorial boundary fraction is a tilted endpoint ratio for a zero-mean conditioned random walk.

## 4. Vatutin--Wachtel shifted-lattice local theorem

Vatutin and Wachtel, *Local probabilities for random walks conditioned to stay positive* (Probability Theory and Related Fields 143, 2009; arXiv:0711.1302), treat general `(h,a)`-lattice increments, not only integer-centered lattice walks.

Their Theorem 5 states, in the present finite-variance setting, that for lattice endpoints in the small-deviation region,

\[
\boxed{
\mathbf Q(S_L=x,\tau^->L)
\sim
\frac{c_0 H(x)}{L c_L},
}
\]

uniformly in the permitted shifted lattice, where

- `c_L` is the normalizing scale, here `c_L asymp sqrt(L)`;
- `c_0>0` is a distribution-dependent constant;
- `H(x)` is the strict ascending-ladder-height renewal function.

The shifted lattice condition is exactly compatible with our endpoints because

\[
S_L=(1-\alpha)L+x_L,
\qquad x_L\in\mathbb Z.
\]

In particular, the theorem is uniform at the moving endpoint

\[
\delta_L\in(0,1).
\]

Since by definition

\[
H(x)\ge1
\qquad(x>0),
\]

there exists `c_1>0` such that for all sufficiently large `L`,

\[
\boxed{
\mathbf Q(\tau^->L,S_L=\delta_L)
\ge
\frac{c_1}{L c_L}.
}
\]

## 5. Uniform upper bound for the denominator

The same paper's Lemma 19 gives a global small-deviation upper estimate

\[
\boxed{
\mathbf Q(S_L\in[x,x+1),\tau^->L)
\le
C\frac{H(x)}{L c_L}
}
\]

for `0<x<=c_L`.

Because our time-`L` support has spacing one, the half-open interval

\[
[\delta_L+s,\delta_L+s+1)
\]

contains exactly the one possible lattice endpoint `delta_L+s`.

The ladder renewal function has at most linear growth in the finite-variance case; in particular one may use

\[
H(x)\le C'(1+x).
\]

Hence

\[
\sum_{0\le s\le c_L}
e^{-\theta s}
\mathbf Q(\tau^->L,S_L=\delta_L+s)
\le
\frac{C_2}{L c_L}
\sum_{s\ge0}e^{-\theta s}(1+s)
\le
\boxed{
\frac{C_3}{L c_L}.
}
\]

For `s>c_L`, the ordinary lattice local-limit upper bound

\[
\mathbf Q(S_L=\delta_L+s)
\le C/c_L
\]

and the exponential factor `e^{-theta s}` give a tail

\[
O\!\left(c_L^{-1}e^{-\theta c_L}\right)
=o((L c_L)^{-1}).
\]

Therefore the entire denominator in the exact tilted ratio is bounded by

\[
\boxed{
\frac{C_4}{L c_L}
}
\]

for all sufficiently large `L`.

## 6. Uniform positive boundary fraction

Combining Sections 4--5 yields a constant

\[
\boxed{c_*>0}
\]

depending only on `alpha=log_3 2` such that

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
\ge c_*
}
\]

for every sufficiently large `L`.

This is strictly stronger than the elementary cycle-lemma estimate

\[
D_L^{\rm class}/C_L^{\rm class}\gg1/L.
\]

The theorem does not identify the optimal constant.

## 7. Relation to finite diagnostics

Exact/normalized ballot dynamic programming through very large finite depths shows boundary fractions remaining near a positive constant; particularly small observed values are around `0.0737` near close Diophantine resonances of `alpha`.

These numerical values are **not** used in the theorem above. The probability theorem proves only existence of some unspecified positive `c_*`.

Thus the finite `~7.37%` floor should be interpreted as evidence about the sharp constant, not as the proved constant itself.

## 8. Consequence for cross-base mass transport

The weighted ternary mass transport is

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2}.
\]

Once Fourier discrepancy transfers the class boundary fraction to the ternary-weighted family and spectral complementarity gives

\[
|K_L|=o(D_L),
\]

the present theorem changes the ideal contraction scale from

\[
1-O(1/L)
\]

to

\[
\boxed{1-c+o(1)}
\]

at every Beatty barrier rise, for some `c>0`.

This is a major strengthening: only logarithmically many successful rise steps would then be needed to drive a finite survivor family below one, rather than relying on a harmonic product.

## 9. Remaining gap

The symbolic boundary channel is therefore no longer the main asymptotic obstruction.

The principal unresolved step becomes cross-base harmonic compatibility:

\[
\boxed{
\text{transfer class boundary mass to ternary-weighted mass}
\quad\text{and}\quad
|K_L|/D_L\to0
}
\]

at a sufficiently strong near-linear growing resolution.

The spectral-exception splitting lemma and exact spectral-renewal identities isolate this remaining task.
