# Backward exponential projective carry chart

Status: **EXACT / CLOSED as a symbolic carry-family representation**

## One-gate chart

At remaining ternary precision `m`, let

- `z_plus` be the successor projective carry modulo `3^(m-1)`;
- `A` be the target ranked-one exponent;
- `B` be the candidate exponent.

The carry relation

\[
z+2^A-2^B\equiv3z_+\pmod{3^m}
\]

is equivalent to

\[
\boxed{
\Gamma_{m,z_+,A}(B)
=3z_+-2^A+2^B\pmod{3^m}.
}
\]

This is the exact backward predecessor-carry chart.

## Injectivity on a legal exponent interval

The multiplicative order of `2` modulo `3^m` is

\[
\lambda_m=2\cdot3^{m-1}.
\]

Therefore

\[
\Gamma(B_1)=\Gamma(B_2)
\iff
B_1\equiv B_2\pmod{\lambda_m}.
\]

Consequently the chart is injective on every integer exponent interval of width strictly less than `lambda_m`.

For the current critical-cut right H block,

\[
h_R-q_R=232{,}565{,}517<\lambda_m
\]

for every `m>=18`. Hence every one-layer backward chart is injective on the complete legal right-H slack/exponent interval throughout the high-precision range.

## Projective compatibility

For `1<=r<=m`, reduction of the chart gives

\[
\Gamma_m(B)\bmod3^r
=
3(z_+\bmod3^{r-1})-2^A+2^B
\pmod{3^r}.
\]

Thus the chart is compatible with decreasing ternary precision.

## Multi-gate triangular chart

For `k` backward one-event gates, write

\[
z_i=3z_{i+1}-2^{A_i}+2^{B_i}.
\]

Exact unrolling gives

\[
\boxed{
z_0
=3^kz_k+
\sum_{i=0}^{k-1}3^i(2^{B_i}-2^{A_i})
\pmod{3^m}.
}
\]

The candidate coordinates are not arbitrary: in the right-H formation chart

\[
B_i=(q-i-1)+s_i,
\]

with the exact triangular domain

\[
0\le s_i\le D_i,
\qquad
s_{i+1}\le s_i.
\]

Therefore a high-precision multi-gate carry family may be retained symbolically as an exponential map over an ordered slack domain rather than as a flat list of raw carry residues.

This is a **representation theorem**, not a cardinality theorem. It does not prove that the number of admissible slack vectors is small.

## Necessary base-carry coordinate

Suppose two states have the same target/exponent interval data but different successor carries

\[
z_+^{(1)}\not\equiv z_+^{(2)}\pmod{3^{m-1}}.
\]

For every common candidate exponent `B`,

\[
\Gamma_{z_+^{(1)}}(B)-\Gamma_{z_+^{(2)}}(B)
=3(z_+^{(1)}-z_+^{(2)})
\not\equiv0\pmod{3^m}.
\]

Hence the successor-carry/base coordinate is observable by the next backward layer and cannot generally be forgotten.

In particular,

`Pi3 interval payload × S_max`

without a carry/base coordinate is **not** a complete multi-gate state unless another exact theorem proves recoverability of that carry from retained coordinates.

## DSD separation

**Projective observation:** chart base carry and requested ternary precision.

**Formation:** ordered slack domain / `S_max` feasibility data.

**Interval quotient:** `Pi3_k` where a fixed one-dimensional displacement family is being queried.

**Physical defect:** separate; no defect-cost dominance follows from this chart alone.

## What is now closed

- exact backward one-gate exponential chart;
- injectivity on intervals shorter than `lambda_m`;
- current right-H one-layer injectivity for every `m>=18`;
- projective reduction compatibility;
- exact `k`-gate triangular unrolling;
- necessity of retaining the carry/base coordinate in general.

## What remains open

- a compact quotient of the **distinct chart bases** generated across several gates;
- exact state counts through the `L=24,28,47` high-precision ranges;
- exact export state at `m=17`;
- right-H H-grammar recursion and the forward/backward join.

## Certificate

- `../src/A0_s1_routeB_backward_exponential_carry_chart_certificate.py`

Finite checks in that file are implementation regressions only.
