# Formation-only child-imbalance contraction under added ternary selectors

Date: 2026-08-12

Status: **exact finite-group L1 contraction theorem**. At any fixed dyadic parent resolution, the total imbalance between the two child lifts of the ternary representative measure cannot increase when additional independent ternary `0/1` selectors are released. This yields a dynamics-independent upper bound on the cross-correlation term in the growing-resolution transport identity. This does not prove Collatz.

## 1. Ternary subset-sum measure

Fix a child modulus

\[
2M=2^{j+1}.
\]

For selector depth `d`, let

\[
Y_d=3^{44}+\sum_{i=0}^{d-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

and let `mu_d` be its normalized probability distribution on

\[
G:=\mathbb Z/(2M)\mathbb Z.
\]

Thus

\[
\mu_d(x)=2^{-d}\#\{a:Y_d\equiv x\pmod{2M}\}.
\]

Adding selector `a_d` convolves the measure with

\[
\kappa_d:=\frac12(\delta_0+\delta_{3^d}),
\]

so

\[
\boxed{
\mu_{d+1}=\mu_d*\kappa_d.
}
\]

## 2. Opposite-child shift

Two residues in `G` have the same parent modulo `M` and opposite newly revealed binary bit exactly when they differ by `M`.

Let

\[
\tau_M\mu(x):=\mu(x+M).
\]

Define the normalized total child imbalance

\[
\boxed{
\Delta_j(d)
:=\|\mu_d-\tau_M\mu_d\|_{\ell^1(G)}.
}
\]

In parent notation this is

\[
\Delta_j(d)
=\sum_{r=0}^{M-1}
|\mu_d(r)-\mu_d(r+M)|.
\]

For unnormalized child counts `c_0,c_1`, define

\[
U_j(d):=\sum_{r=0}^{M-1}|c_0(r)-c_1(r)|.
\]

Then

\[
\boxed{
U_j(d)=2^d\Delta_j(d).
}
\]

## 3. Monotonicity theorem

Translation commutes with convolution, so

\[
\mu_{d+1}-\tau_M\mu_{d+1}
=(\mu_d-\tau_M\mu_d)*\kappa_d.
\]

Convolution by a probability measure is an `L1` contraction. Therefore

\[
\boxed{
\Delta_j(d+1)\le\Delta_j(d).
}
\]

Equivalently,

\[
\boxed{
U_j(d+1)\le2U_j(d).
}
\]

The normalized imbalance can only improve as additional ternary selectors are released.

No Collatz dynamics is used in this theorem.

## 4. Matching interpretation

Inside each parent residue `r mod M`, there are `c_0(r)` representatives in child 0 and `c_1(r)` in child 1.

Pairing one representative from each side cancels its contribution to any signed child preference. A maximum bipartite pairing leaves exactly

\[
|c_0(r)-c_1(r)|
\]

unpaired representatives in that parent.

Hence

\[
\boxed{
U_j(d)
}
\]

is exactly the total number of representatives that remain unmatched after optimal opposite-child pairing over all parent fibers.

Equivalently, one may connect selector vectors whose weighted sums differ by an odd multiple of `2^j`; such pairs share the same parent and occupy opposite children.

## 5. Dynamics-independent correlation bound

In the child-transport theorem let

\[
D_L=\{r:m(r)=1\}
\]

and let `v(r)=+/-1` denote the unique dangerous child direction.

The cross-base correction is

\[
K_L=\sum_{r\in D_L}v(r)u(r),
\qquad
u(r)=c_0(r)-c_1(r).
\]

Regardless of the geometry or arithmetic of the dynamical set `D_L`,

\[
\begin{aligned}
|K_L|
&\le\sum_{r\in D_L}|u(r)|\\
&\le\sum_{r}|u(r)|\\
&=U_j(d).
\end{aligned}
\]

Therefore

\[
\boxed{
|K_L|\le U_j(d).
}
\]

This completely separates a conservative estimate into:

- a **formation-only quantity** `U_j(d)`;
- a dynamical one-child mass `M_D(L)`.

If

\[
U_j(d)<M_D(L),
\]

then one obtains a nontrivial contraction without proving any signed cancellation with `v`:

\[
\boxed{
C_{L+1}
\le C_L-\frac12\left(M_D(L)-U_j(d)\right).
}
\]

In normalized one-child notation,

\[
\left|\frac{K_L}{M_D(L)}\right|
\le\frac{U_j(d)}{M_D(L)}.
\]

## 6. Exact A_30 values in the current coefficient range

For `A_30`, the active coefficient transitions use parent exponent

\[
j=L-2.
\]

The formation-only imbalance bounds are:

\[
\boxed{
\begin{array}{c|r|r|c}
L&j&U_j(30)&U_j(30)/M_D(L)\\\hline
4&2&256&4.7683\times10^{-7}\\
6&4&44&2.1856\times10^{-7}\\
7&5&86&3.6615\times10^{-7}\\
9&7&11,022&1.09496\times10^{-4}\\
11&9&120,446&1.9145\times10^{-3}\\
12&10&313,822&3.5212\times10^{-3}\\
14&12&593,406&1.3086\times10^{-2}\\
15&13&951,612&1.5253\times10^{-2}\\
17&15&2,493,618&7.9190\times10^{-2}
\end{array}
}
\]

Thus even the sign-blind formation-only estimate proves substantial pruning at every active transition through `L=17`.

For example at `L=17`,

\[
M_D=31,489,378,
\qquad
U_{15}=2,493,618,
\]

so

\[
\boxed{
|K_{17}|/M_D\le0.07919.
}
\]

The exact signed correlation found in the stronger diagnostic is much smaller (`1480/31,489,378`), but that extra cancellation is not needed to establish a positive contraction.

## 7. Fourier equivalence

At the child modulus, only odd frequencies contribute to `u`. Therefore `Delta_j(d)` is also a norm of the odd-frequency shell of the ternary Riesz product.

The monotonicity theorem is the physical-space counterpart of multiplying those Fourier coefficients by one additional Bernoulli factor of modulus at most one.

This gives two equivalent proof languages:

\[
\boxed{
\text{opposite-child matching / L1 contraction}
\quad\Longleftrightarrow\quad
\text{odd-frequency damping}.
}
\]

## 8. Strategic consequence

The difficult signed quantity

\[
\sum_{D_L}v(r)u(r)
\]

need not be attacked first.

A robust hierarchy is now available:

1. try the formation-only bound `|K_L|<=U_j(d)`;
2. if that is too weak, use the actual restricted support `D_L`;
3. only then use signed Fourier cancellation between `v` and `u`.

This preserves the proposition/set/channel philosophy while using the weakest sufficient information at each stage.