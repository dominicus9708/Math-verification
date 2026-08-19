# Selector collision-halving and boundary Cauchy reduction

Date: 2026-08-20

Status: **exact dyadic refinement identity + exact boundary-correlation bound + finite diagnostics.** This is not a proof of the Collatz conjecture.

## 1. Selector measure and collision probability

For the ternary-selector core, ignore the fixed translation `3^m`, which does not affect collision probabilities, and write

\[
S(a)=\sum_{i=0}^{m-1} a_i3^i,\qquad a_i\in\{0,1\}.
\]

Let `mu_r` be the uniform selector distribution modulo `2^r`:

\[
\mu_r(x)=2^{-m}\#\{a:S(a)\equiv x\pmod{2^r}\}.
\]

Define its collision probability

\[
\boxed{p_r:=\sum_{x\bmod 2^r}\mu_r(x)^2.}
\]

Equivalently, if `A,B` are independent selector sums,

\[
p_r=\Pr(A\equiv B\pmod{2^r}).
\]

## 2. Exact dyadic collision-halving identity

For each parent residue `x mod 2^r`, let

\[
a_x:=\mu_{r+1}(x),\qquad b_x:=\mu_{r+1}(x+2^r).
\]

Then

\[
\mu_r(x)=a_x+b_x.
\]

Therefore

\[
\begin{aligned}
2p_{r+1}-p_r
&=2\sum_x(a_x^2+b_x^2)-\sum_x(a_x+b_x)^2\\
&=\sum_x(a_x-b_x)^2.
\end{aligned}
\]

Hence

\[
\boxed{
2p_{r+1}-p_r
=\sum_{x\bmod2^r}
\bigl(\mu_{r+1}(x)-\mu_{r+1}(x+2^r)\bigr)^2\ge0.
}
\]

So `p_(r+1) >= p_r/2` for every selector measure, and equality holds exactly when every dyadic sibling pair has equal mass.

This quantity is the exact `L^2` sibling-imbalance energy.

## 3. Difference-variable / balanced-ternary form

Let

\[
Z=A-B=\sum_{i=0}^{m-1}\varepsilon_i3^i,
\]

where independently

\[
\Pr(\varepsilon_i=0)=\frac12,
\qquad
\Pr(\varepsilon_i=1)=\Pr(\varepsilon_i=-1)=\frac14.
\]

Then

\[
p_r=\Pr(2^r\mid Z).
\]

Balanced ternary with digits `-1,0,1` is unique on

\[
|Z|\le\frac{3^m-1}{2}.
\]

Let `w_bal(z)` be the number of nonzero balanced-ternary digits of `z`. The unique digit vector has probability

\[
\Pr(Z=z)=2^{-m-w_{\rm bal}(z)}.
\]

Writing `z=j2^r`, the collision-halving energy has the exact cross-base form

\[
\boxed{
2p_{r+1}-p_r
=2^{-m}
\sum_{\substack{j\in\mathbb Z\\
|j2^r|\le(3^m-1)/2}}
(-1)^j\,2^{-w_{\rm bal}(j2^r)}.
}
\]

Indeed, even `j` are exactly the multiples of `2^(r+1)` and odd `j` are the other multiples of `2^r`.

Thus selector dyadic sibling imbalance is reduced to an alternating weighted balanced-ternary digit-sum problem on multiples of a power of two.

## 4. Exact boundary correlation identity

At a Beatty rise from parent depth `L` to child depth `L+1`, use the reduced parent coordinate modulo

\[
M=2^{L-2}.
\]

Let `c_0(x),c_1(x)` be the unnormalized selector multiplicities in the two child residues `x` and `x+M`, so the child modulus is `2M=2^(L-1)`.

For every one-child coefficient-boundary parent define its orientation

\[
v(x)=+1
\]

if the lower child survives and

\[
v(x)=-1
\]

if the upper child survives. Let `B_L` be the number of such unweighted boundary parents.

The mass-transport correlation term is exactly

\[
\boxed{
K_L=\sum_{x\in\partial_L}v(x)\bigl(c_0(x)-c_1(x)\bigr).
}
\]

Cauchy-Schwarz gives

\[
|K_L|^2
\le
B_L\sum_{x\in\partial_L}(c_0-c_1)^2
\le
B_L\sum_{x\bmod M}(c_0-c_1)^2.
\]

Since total selector mass is `2^m`, Section 2 gives

\[
\sum_{x\bmod M}(c_0-c_1)^2
=2^{2m}\bigl(2p_{L-1}-p_{L-2}\bigr).
\]

Therefore

\[
\boxed{
|K_L|
\le
2^m\sqrt{B_L\bigl(2p_{L-1}-p_{L-2}\bigr)}.
}
\]

This bound does **not** use any orientation cancellation. It only requires selector collision-halving.

## 5. Relation to the Fourier formulation

Extend the boundary orientation anti-periodically to the child group `Z/(2M)Z`:

\[
w(x)=v(x),\qquad w(x+M)=-v(x).
\]

If `c` is the selector multiplicity function on the child group, then

\[
K_L=\sum_y w(y)c(y)
=\frac1{2M}\sum_{t\ \mathrm{odd}}\widehat w(t)\overline{\widehat c(t)}.
\]

Only odd frequencies occur. The collision-halving identity is exactly the odd-frequency `L^2` energy of the selector:

\[
\frac{2}{2M}\sum_{t\ \mathrm{odd}}
\left|\frac{\widehat c(t)}{2^m}\right|^2
=2p_{L-1}-p_{L-2}.
\]

Thus the spatial Cauchy bound and the odd-frequency Fourier Cauchy bound are the same theorem.

## 6. Exact m=44 finite calibration

For the existing depth-44 ternary selector and coefficient-boundary rises, the exact sibling energies are:

| parent L | B_L | weighted D | K | sibling energy `sum(c0-c1)^2` | Cauchy bound / D |
|---:|---:|---:|---:|---:|---:|
| 14 | 173 | 743029190277 | -14271 | 159862426028 | 7.07768e-6 |
| 17 | 961 | 515932831671 | 271723 | 960175935454 | 5.88768e-5 |
| 19 | 2652 | 355945413895 | 209309 | 5366299302088 | 3.35152e-4 |
| 20 | 8045 | 539891337183 | -207085 | 1522647717056 | 2.05002e-4 |
| 22 | 17637 | 295899305006 | 45056 | 2638503571582 | 7.29034e-4 |

At `m=44,L=22`, for example,

\[
\boxed{
2p_{21}-p_{20}
=\frac{2638503571582}{2^{88}}
\approx8.52546\times10^{-15}.
}
\]

The orientation-free Cauchy bound is already below `0.001 D`; the actual `|K|/D` is about `1.52e-7`.

## 7. Bulk-versus-sparse interpretation

The collision bound is strongest while many selector points occupy each relevant dyadic scale. Once the modulus is so fine that the selector measure becomes atomic, the collision-halving energy reaches the discreteness floor of order `2^{-m}` and the `L^2` argument eventually becomes too weak.

This suggests the corrected Stage 4 decomposition

\[
\boxed{
\text{collision-controlled bulk}
\;\longrightarrow\;
\text{orientation/spectral middle regime}
\;\longrightarrow\;
\text{sparse deterministic tail}.
}
\]

A sufficient bulk theorem can be phrased directly as an upper bound on

\[
2p_{r+1}-p_r,
\]

rather than on total variation of the selector measure.

## 8. Next target

The most direct new cross-base target is a quantitative **collision-halving theorem** for

\[
Z_m=\sum_{i=0}^{m-1}\varepsilon_i3^i,
\]

uniform over the dyadic range needed before the selector measure becomes sparse. Equivalently, prove cancellation in

\[
\sum_j(-1)^j2^{-w_{\rm bal}(j2^r)}.
\]

This is narrower than proving full selector equidistribution and is exactly the quantity entering the mass-transport `K` term through Cauchy-Schwarz.
