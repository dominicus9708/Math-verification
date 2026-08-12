# Universal first-crossing tri-place defect

Date: 2026-08-12

Status: **exact mixed-place identity for every first coefficient crossing from a renewal floor**. This generalizes the earlier Christoffel tri-place coordinate and does not assume a continued-fraction convergent.

## 1. Universal first-crossing reference

Put

\[
\gamma:=\log_2 3.
\]

For a first coefficient crossing with `H` odd steps,

\[
\boxed{A=A_H:=\lceil\gamma H\rceil.}
\]

The universal latest allowed odd positions are

\[
\boxed{
i_k^*=\lfloor\gamma(k-1)\rfloor+1,
\qquad1\le k\le H.
}
\]

Let `w_H^*` be the reference word with ones at these positions. Its correction numerator and normalized correction are

\[
R_*(H),
\qquad
r_*(H):=\frac{R_*(H)}{3^H}
=\frac13\sum_{m=0}^{H-1}2^{-\{m\gamma\}}.
\]

Every first-crossing word has positions

\[
i_k=i_k^*-s_k,
\qquad s_k\ge0.
\]

Define the integer defect

\[
\boxed{E:=R_*(H)-R(w)\ge0,}
\]

and its normalized form

\[
\boxed{\xi:=\frac{E}{3^H}.}
\]

Then

\[
\boxed{
\xi
=\sum_{k=1}^H
\frac{2^{i_k^*-1}}{3^k}
(1-2^{-s_k}).
}
\]

## 2. Real action

Let

\[
P_H:=\frac{2^A}{3^H}>1,
\qquad
Z_H:=2^A-3^H=3^H(P_H-1).
\]

For a renewal-floor start `N` whose first coefficient crossing endpoint is

\[
Y=T^A(N)=N+g
\]

with `g>=0`, the affine endpoint identity is

\[
N+\frac{R(w)}{3^H}=P_H(N+g).
\]

Therefore

\[
\boxed{
(P_H-1)N+P_Hg
=r_*(H)-\xi.
}
\]

In the aperiodic no-first-descent branch `g>0` unless the prefix is an exact return.

Thus positive defect consumes the same real correction budget that must pay both coefficient crossing and endpoint rise.

## 3. 2-adic formation action

For the length-`A` first-crossing prefix, integrality requires

\[
3^HN+R(w)\equiv0\pmod{2^A}.
\]

Hence the starting residue is

\[
\rho_w\equiv-R(w)3^{-H}\pmod{2^A}.
\]

The reference residue is

\[
\rho_*\equiv-R_*(H)3^{-H}\pmod{2^A}.
\]

Subtracting gives

\[
\boxed{
\rho_w
\equiv
\rho_*+\xi
\pmod{2^A},
}
\]

where `3^{-H}` is interpreted as the odd unit modulo `2^A`.

If the crossing endpoint `Y` is additionally odd, exact endpoint oddness upgrades both formation classes from modulus `2^A` to modulus `2^{A+1}`, and the same difference formula holds:

\[
\boxed{
\rho_w
\equiv
\rho_*+\xi
\pmod{2^{A+1}}.
}
\]

## 4. Modular gap action

From

\[
2^A(N+g)=3^HN+R(w)
\]

we obtain

\[
2^Ag=R(w)-Z_HN.
\]

Reducing modulo `Z_H` and using

\[
2^A\equiv3^H\pmod{Z_H}
\]

gives

\[
\boxed{
g\equiv R(w)3^{-H}\pmod{Z_H}.}
\]

Let

\[
g_*(H)\equiv R_*(H)3^{-H}\pmod{Z_H}.
\]

Then

\[
\boxed{
g\equiv g_*(H)-\xi\pmod{Z_H}.}
\]

Thus the same defect moves the start address and the gap address in opposite directions.

## 5. Earliest displaced odd step

Let

\[
k_*:=\min\{k:s_k>0\}.
\]

The integer defect can be written

\[
E
=\sum_{k:s_k>0}
3^{H-k}2^{i_k-1}(2^{s_k}-1).
\]

Actual odd positions `i_k` are strictly increasing, so the first displaced term has the unique smallest power of two. Its remaining factor is odd. Hence

\[
\boxed{v_2(E)=i_{k_*}-1.}
\]

Since `3^H` is odd,

\[
\boxed{v_2(\xi)=i_{k_*}-1.}
\]

Therefore the first combinatorial displacement is exactly the first 2-adic bit at which the actual start residue can differ from the universal Beatty reference residue.

For a renewal floor the first maximal block must be subcritical, so its parity begins `11`. Since the universal reference also begins `11`,

\[
\boxed{s_1=s_2=0.}
\]

Thus every nonzero renewal-floor first-crossing defect has

\[
\boxed{v_2(\xi)\ge2.}
\]

## 6. Endpoint parity cost

The first coefficient crossing occurs on an even step. Its endpoint `Y=N+g` need not be odd.

Let

\[
e:=v_2(Y).
\]

If `e>0`, the following `e` halving steps must all remain at least `N` because `N` is a suffix minimum. Therefore

\[
Y\ge2^eN.
\]

But

\[
Y=\frac{N+r(w)}{P_H}<N+r(w)<N+\frac H3.
\]

Hence

\[
\boxed{
H>3(2^e-1)N.
}
\]

Consequently

\[
\boxed{
H\le3N
\Longrightarrow
Y\text{ is odd}.
}
\]

More generally, every additional post-crossing even step costs another factor of two in the required linear-depth overload.

## 7. Current role

The first-crossing hard core is now a single tri-place compatibility problem indexed only by `H` and an admissible displacement vector `s`:

\[
\boxed{
\begin{array}{ll}
\text{real:}&(P_H-1)N+P_Hg=r_*(H)-\xi,\\[1mm]
\text{2-adic:}&\rho_w\equiv\rho_*+\xi,\\[1mm]
\text{gap modulus:}&g\equiv g_*(H)-\xi\pmod{Z_H}.
\end{array}
}
\]

The endpoint-parity theorem gives a useful secondary split:

1. if `H<=3N`, the endpoint is odd and the stronger modulus `2^{A+1}` is available;
2. if the endpoint remains even, then `H>3N`, an explicit linear-depth overload.

This universalizes the earlier Christoffel tri-place architecture and isolates continued fractions as a Diophantine subcase rather than the primary state space.
