# Affine random-walk mixing and an unconditional selector-energy regime

Date: 2026-08-13

Status: **exact probabilistic reformulation + corrected application of an external all-moduli mixing lemma**. It proves the Fourier-energy hypothesis needed by the coefficient-mass transport theorem in a deep-selector / shallower-binary regime `d >= A L^2` for a sufficiently large constant `A`. It does not reach the sharper linear `d~L` regime seen in finite calculations and does not prove Collatz.

## 1. Selector Fourier energy

Consider the ternary `0/1` selector measure

\[
S_d=\sum_{i=0}^{d-1}a_i3^i,
\qquad a_i\in\{0,1\}
\]

with independent uniform selector bits.

Let `mu_{d,r}` be its reduction modulo

\[
q=2^r.
\]

The nontrivial Fourier energy is

\[
E_{d,r}
:=
\sum_{k=1}^{q-1}
|\widehat\mu_{d,r}(k)|^2.
\]

By Parseval,

\[
\boxed{
E_{d,r}
=q\sum_x\left|
\mu_{d,r}(x)-\frac1q
\right|^2.
}
\]

Equivalently, for two independent selector sums `S_d,S_d'`,

\[
\boxed{
E_{d,r}+1
=q\Pr(S_d\equiv S_d'\pmod q).
}
\]

## 2. Balanced-ternary collision representation

Write

\[
\Delta_d=S_d-S_d'
=\sum_{i=0}^{d-1}\varepsilon_i3^i.
\]

For each difference digit,

\[
\boxed{
\Pr(\varepsilon_i=0)=\frac12,
\qquad
\Pr(\varepsilon_i=1)
=
\Pr(\varepsilon_i=-1)
=\frac14.
}
\]

Hence

\[
\boxed{
E_{d,r}
=q\Pr(\Delta_d\equiv0\pmod q)-1.
}
\]

This is an exact collision identity. It can also be read combinatorially from uniqueness of balanced ternary: a signed digit vector with `s` nonzero digits corresponds to exactly `2^(d-s)` ordered selector pairs.

**Important scope point.** The balanced-difference process is useful for the collision representation, but its own `L^2` mixing would control fourth powers `sum |widehat mu|^4`, not the selector energy `E=sum |widehat mu|^2`. Therefore the external mixing lemma in Section 4 must be applied to the original selector process, not to the difference process.

## 3. The selector distribution is an affine random walk

Because the selector digits are i.i.d., reversing their order does not change the distribution of `S_d`.

Thus `S_d mod q` has exactly the same distribution as the time-homogeneous affine recursion

\[
\boxed{
Y_{n+1}=3Y_n+a_{n+1}\pmod q,
\qquad
Y_0=0,
}
\]

where

\[
\boxed{
\Pr(a_n=0)=\Pr(a_n=1)=\frac12.
}
\]

Indeed,

\[
Y_d
=a_d+3a_{d-1}+\cdots+3^{d-1}a_1,
\]

which has the same law as `S_d` after digit reversal.

Therefore the ternary-selector Riesz product is exactly the Fourier transform of the affine Markov chain with multiplier `a=3` and Bernoulli noise on `{0,1}`.

## 4. External all-moduli mixing lemma

Eberhard and Varju study

\[
X_{n+1}=aX_n+b_n\pmod q
\]

for fixed integer `a>1` and finitely supported i.i.d. noise whose support differences have gcd one.

Their Lemma 4.1 gives an all-moduli small-modulus estimate: if

\[
(q,a)=1
\]

and

\[
n>C\log q\log\log q,
\]

then

\[
\boxed{
q\|\mu_n\bmod q-u_q\|_2^2
\le
\exp\!\left(-c\frac n{\log q}\right)
}
\]

for constants `C,c>0` depending only on `a` and the noise law.

Apply this **directly to the selector chain** of Section 3:

\[
a=3,
\qquad
q=2^r,
\qquad
\Pr(b=0)=\Pr(b=1)=\frac12.
\]

The support-difference gcd is one and `(2^r,3)=1`, so all hypotheses hold.

Since the law at time `d` is exactly `mu_{d,r}`, the left side of the external estimate is precisely `E_{d,r}`. Therefore

\[
\boxed{
E_{d,r}
\le
\exp\!\left(-c\frac d{r\log2}\right)
}
\]

once

\[
d>C'(r\log r).
\]

Absorbing `log 2` into the constants,

\[
\boxed{
E_{d,r}\le e^{-c'd/r}.
}
\]

## 5. Quadratic selector-depth regime

The Beatty-boundary transport theorem only needs Fourier energy below the boundary density scale

\[
\beta_L
=
2^{-(1-H_2(\log_3 2))L+O(\log L)}.
\]

Put

\[
\kappa
=(1-H_2(\log_3 2))\log2>0.
\]

Take binary resolution `r=L+O(1)` and selector depth

\[
\boxed{d\ge A L^2.}
\]

Then the external mixing estimate gives

\[
E_{d,r}
\le
\exp\left(-\frac{c'A}{1+o(1)}L\right).
\]

Choosing `A` sufficiently large makes

\[
\frac{c'A}{1+o(1)}>\kappa.
\]

Hence, for every fixed `epsilon>0` and all sufficiently large `L`,

\[
\boxed{
E_{d,r}
\le
\varepsilon^2\beta_L.
}
\]

The same selector-chain mixing estimate applies to the parent modulus and to the full nonzero child energy, which dominates the odd-frequency child energy used in the signed transport correlation.

Thus the Fourier-energy hypothesis in the conditional growing-resolution transport theorem is **unconditionally valid** in the regime

\[
\boxed{d\ge A L^2}
\]

for a sufficiently large constant `A`.

## 6. Consequence for coefficient-survivor transport

In that regime, the conditional transport theorem becomes unconditional at all sufficiently large Beatty-rise depths:

\[
C_{L+1}
\le
C_L\left(1-\frac{c_0}{L}+O(L^{-2})\right)
\]

for some constant `c_0>0` depending on the chosen energy margin.

Consequently the **fraction** of ternary selector assignments that can remain coefficient-surviving through such resolutions is forced downward by a polynomial factor in `L`, without inspecting individual starts.

This is the first genuinely growing-resolution coefficient-survival estimate in the current program that is backed by an external uniform mixing theorem rather than only finite computation.

## 7. Why this is not yet terminal

For the current finite `m=44` block, the most useful computations have `d=44` and binary depths around `L=20--30`, much closer to a linear relation `d~L` than to `d>=A L^2`.

The external all-moduli lemma is therefore too coarse to replace the exact finite certificates at the present block.

More importantly, polynomial decay of a **fraction** does not by itself make a `2^d`-element representative family empty.

The remaining analytic target is sharper:

> prove selector-energy or direct spectral-correlation decay in a near-linear growing regime, or combine the coarse mixing regime with additional dyadic/3-adic/minimality constraints so that survivor count, not merely survivor fraction, is forced to zero.

## External source

Sean Eberhard and Peter P. Varju, *Mixing time of the Chung--Diaconis--Graham random process*, Probability Theory and Related Fields 179 (2021), 317--344, arXiv:2003.08117. Lemma 4.1 is the all-moduli estimate used above.
