# Universal first-crossing Beatty frame

Date: 2026-08-12

Status: **exact universal structure for first coefficient crossings**. This removes the need to assume a continued-fraction layer before defining the extremal reference word.

## 1. First coefficient crossing is always the nearest upper integer layer

Let a Collatz parity prefix have accelerated length `A` and `H` odd steps. Its multiplicative coefficient is

\[
\frac{3^H}{2^A}.
\]

Assume `A` is the first time this coefficient becomes strictly smaller than `1`.

The crossing step must be even, because an odd step multiplies the coefficient by `3/2` and cannot move it from `>=1` to `<1`.

Immediately before the crossing,

\[
\frac{3^H}{2^{A-1}}\ge1,
\]

while after it

\[
\frac{3^H}{2^A}<1.
\]

Therefore

\[
2^{A-1}\le3^H<2^A.
\]

Since `log_2 3` is irrational,

\[
\boxed{
A=\lceil H\log_2 3\rceil.
}
\]

Thus every first coefficient crossing lies on the minimal upper integer layer. No continued-fraction assumption is required.

## 2. Universal latest odd positions

Put

\[
\gamma:=\log_2 3.
\]

Let

\[
1=i_1<i_2<\cdots<i_H
\]

be the one-based positions of the odd steps in a first-crossing word.

Immediately before the `k`th odd step (`k>=2`), the prefix has length `i_k-1` and contains `k-1` odd steps. Since the coefficient has not yet crossed,

\[
2^{i_k-1}<3^{k-1}.
\]

Hence

\[
\boxed{
i_k\le i_k^*:=\lfloor\gamma(k-1)\rfloor+1.}
\]

For `k=1`, `i_1=i_1^*=1`.

Therefore every first-crossing word is obtained from one universal reference configuration by shifting some odd positions to the left.

## 3. Critical Beatty/Sturmian reference word

Define the reference positions

\[
\boxed{
i_k^*=\lfloor\gamma(k-1)\rfloor+1.}
\]

and let `w_H^*` be the length

\[
A_H:=\lceil\gamma H\rceil
\]

binary word with ones exactly at these positions.

This is the finite prefix of the irrational mechanical/Beatty word associated with the critical slope. It is the coordinatewise latest parity word compatible with first coefficient survival.

## 4. Exact maximal normalized correction

For a word with odd positions `i_k`, the normalized affine correction is

\[
\boxed{
r(w)=\frac{R(w)}{3^H}
=\sum_{k=1}^H\frac{2^{i_k-1}}{3^k}.}
\]

Since every summand increases with `i_k`, the reference word maximizes the correction among all first-crossing words:

\[
\boxed{r(w)\le r_*(H):=r(w_H^*).}
\]

Using

\[
2^{\gamma m}=3^m,
\]

we obtain the exact Beatty sum

\[
\boxed{
r_*(H)
=\frac13\sum_{m=0}^{H-1}2^{-\{m\gamma\}}.}
\]

In particular, because

\[
\frac12<2^{-\{m\gamma\}}\le1,
\]

\[
\boxed{
\frac H6<r_*(H)\le\frac H3.
}
\]

## 5. Asymptotic correction constant

The sequence `{m gamma}` is equidistributed modulo `1`. Therefore

\[
\frac{r_*(H)}H
\longrightarrow
\frac13\int_0^1 2^{-x}\,dx
=\boxed{\frac1{6\ln2}}.
\]

Numerically,

\[
\boxed{
\frac1{6\ln2}\approx0.2404491735.
}
\]

Hence the earlier universal bound `r<H/3` can asymptotically be sharpened to

\[
\boxed{
r(w)\le\left(\frac1{6\ln2}+o(1)\right)H.}
\]

At continued-fraction denominator lengths, the classical Denjoy–Koksma inequality gives an effective `O(1)` discrepancy for this bounded-variation rotation sum.

## 6. Universal displacement defect

Define

\[
s_k:=i_k^*-i_k\ge0.
\]

Then

\[
\boxed{
\xi_H(w):=r_*(H)-r(w)
=\sum_{k=1}^H
\frac{2^{i_k^*-1}}{3^k}
\left(1-2^{-s_k}\right).
}
\]

Every nonzero displacement contributes at least

\[
\frac1{12}
\]

to the defect, because

\[
\frac{2^{i_k^*-1}}{3^k}>\frac16,
\qquad
1-2^{-s_k}\ge\frac12
\]

when `s_k>=1`.

Thus

\[
\boxed{
\xi_H(w)>\frac{\#\{k:s_k>0\}}{12}.
}
\]

## 7. First-crossing endpoint budget

Let a suffix-minimum start `N` have its first coefficient crossing at this word, with endpoint

\[
N'=N+g>N.
\]

Put

\[
P_H:=\frac{2^{A_H}}{3^H}=2^{A_H-\gamma H}>1.
\]

The endpoint identity gives

\[
\boxed{
(P_H-1)N+P_Hg=r(w)=r_*(H)-\xi_H(w).
}
\]

Hence

\[
\boxed{
(P_H-1)N+P_Hg\le r_*(H).
}
\]

Asymptotically,

\[
\boxed{
(P_H-1)N+P_Hg
\le
\left(\frac1{6\ln2}+o(1)\right)H.
}
\]

This is stronger than the earlier `H/3` ceiling and applies to every first coefficient crossing, not only continued-fraction renewals.

## 8. First-crossing Diophantine dichotomy

The rational slope is

\[
\frac{A_H}{H}>\gamma.
\]

If its reduced form is not a continued-fraction convergent of `gamma`, Legendre's theorem gives

\[
\frac{A_H}{H}-\gamma\ge\frac1{2H^2}.
\]

Equivalently,

\[
\delta_H:=A_H-\gamma H\ge\frac1{2H}.
\]

Since

\[
P_H-1=2^{\delta_H}-1\ge(\ln2)\delta_H,
\]

the coarse exact correction bound gives

\[
\boxed{
N<\frac{2}{3\ln2}H^2
}
\]

for every non-convergent first crossing.

Using the asymptotic Beatty maximum improves this to

\[
\boxed{
N\le\left(\frac1{3(\ln2)^2}+o(1)\right)H^2
}
\]

with

\[
\frac1{3(\ln2)^2}\approx0.6937.
\]

Thus every sufficiently large first-crossing paradoxical segment belongs to one of two arithmetic classes:

1. `A_H/H` reduces to a continued-fraction convergent of `log_2 3`;
2. its odd-event depth satisfies `H = Omega(sqrt(N))`.

## 9. Role

This frame replaces the earlier branch-specific Christoffel reference by a universal irrational critical reference for all first coefficient crossings.

The Christoffel machinery remains valuable for full renewal words and periodic shadows, but the CST/paradoxical first-passage hard core can now be written solely in terms of:

- one integer parameter `H`;
- the nearest upper layer `A_H=ceil(H log_2 3)`;
- the universal Beatty reference positions `i_k^*`;
- the displacement defect `xi_H`;
- and the exact ordinary starting integer/endpoint gap.

This is the cleanest current representation of the first-crossing branch.
