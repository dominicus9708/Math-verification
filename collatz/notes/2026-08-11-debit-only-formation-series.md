# Debit-only formation series

Date: 2026-08-11

Status: **exact summation-by-parts reduction**. The formula removes all pure `v=1` credit events from the 2-adic formation sum and rewrites the hard core in terms of extra-halving/debit events only.

## 1. Extra-halving staircase

Let

\[
E_i:=A_i-i,
\qquad
u_i:=v_i-1\ge0,
\]

so

\[
E_{i+1}-E_i=\nu_i.
\]

Set

\[
u_i:=2^{E_i},
\qquad
r:=\frac23.
\]

Then

\[
c_q
=(1-r)\sum_{i=0}^{q-1}u_i r^i.
\]

## 2. Finite summation by parts

The exact finite identity is

\[
\boxed{
c_q
=1
+\sum_{i=1}^{q-1}(u_i-u_{i-1})r^i
-u_{q-1}r^q.
}
\]

Since

\[
u_i-u_{i-1}
=2^{E_{i-1}}\left(2^{v_{i-1}-1}-1\right),
\]

the middle sum vanishes identically at every event with `v_{i-1}=1`.

## 3. Infinite 2-adic identity

The tail term `u_{q-1}r^q` tends to zero in the 2-adic norm because its 2-adic valuation is `q+E_{q-1}` and tends to infinity.

For a finite positive starting integer `n`,

\[
c_\infty=-n
\quad\text{in }\mathbb Z_2.
\]

Therefore

\[
\boxed{
-(n+1)
=
\sum_{i=1}^{\infty}
2^{E_{i-1}}
\left(2^{v_{i-1}-1}-1\right)
\left(\frac23\right)^i
\quad\text{in }\mathbb Z_2.
}
\]

Only debit events `v>=2` appear.

## 4. Strictly increasing 2-adic valuations

At a debit event the coefficient `2^{v_{i-1}-1}-1` is odd, and the denominator `3^i` is a 2-adic unit. Hence the 2-adic valuation of the `i`th nonzero debit term is

\[
\boxed{
i+E_{i-1}=A_{i-1}+1.}
\]

These valuations strictly increase with event time.

Consequently the first debit term determines the 2-adic valuation of the total:

\[
\boxed{
v_2(n+1)=A_{i_1-1}+1,}
\]

where `i_1` is the first debit index in the summation-by-parts convention.

If the initial `v=1` run has length `ell`, then `A_{i_1-1}=ell`, recovering

\[
\boxed{\ell=v_2(n+1)-1.}
\]

Thus the earlier credit-run theorem is the first digit of the debit-only formation series.

## 5. Real debit budget

Define

\[
J_q
:=
\sum_{i=1}^{q-1}(u_i-u_{i-1})r^i.
\]

The finite identity gives

\[
\boxed{
J_q=c_q-1+u_{q-1}r^q
=c_q-1+\frac23\lambda_{q-1}.
}
\]

Under the harmonic survivor bound,

\[
c_q=O_n(q^{1/9}),
\qquad
\lambda_{q-1}\le1+c_{q-1}/n=O_n(q^{1/9}),
\]

so

\[
\boxed{J_q=O_n(q^{1/9}).}
\]

At a debit event with `d=v_{i-1}-1>=1`, the real debit term is

\[
\boxed{
J_i^{\rm term}
=\frac23(2^d-1)\lambda_{i-1}
=\lambda_i-\frac23\lambda_{i-1}.
}
\]

Equivalently,

\[
J_i^{\rm term}
=\lambda_i(1-2^{-d})
\ge\frac12\lambda_i.
\]

Thus `J` measures the total excess multiplier injected by debit events beyond the baseline `v=1` evolution.

## 6. Refined hard-core formulation

The nonperiodic hard core may now be viewed as a positive debit-event series with all three properties:

1. nonzero terms have strictly increasing 2-adic valuations;
2. their 2-adic sum is exactly the negative ordinary integer `-(n+1)`;
3. their ordinary real partial sums grow only as `O_n(q^{1/9})`.

This is a more compressed target than the full event series and is naturally aligned with the macroblock/debit decomposition.
