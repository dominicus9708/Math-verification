# Height-neutral phase coboundary

Date: 2026-08-20

Status: **exact mechanical-scale identity.** This removes a spurious long-run multiplicative obstruction from the height-neutral sparse-tail analysis. It is not a coefficient-stopping theorem and not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_s=\lceil s\alpha\rceil,
\]

and define the normalized phase-height scale

\[
\boxed{
c_{s,h}=\frac{2^s}{3^{b_s+h}}.
}
\]

For \(s>0\), write

\[
\delta_s=b_s-s\alpha\in(0,1).
\]

Then

\[
\boxed{
c_{s,h}=3^{-h-\delta_s}.}
\]

## 1. A height-neutral macro has an exact endpoint ratio

Take a length-\(L\) macro that starts and ends at the same height \(h\).

Height neutrality means

\[
Q=b_{s+L}-b_s,
\]

where \(Q\) is the total odd count of the macro.

Therefore

\[
\boxed{
\frac{c_{s+L,h}}{c_{s,h}}
=\frac{2^L}{3^Q}.
}
\]

By the mechanical one-slack lemma,

\[
Q\in\{b_L-1,b_L\}.
\]

The two cases are therefore exactly:

\[
\frac{2^L}{3^{b_L-1}}>1
\]

for a one-slack neutral macro, and

\[
\frac{2^L}{3^{b_L}}<1
\]

for a full-barrier neutral macro.

Neither factor should be treated as an independent long-run growth or decay rate.

## 2. Exact telescoping over arbitrary neutral concatenations

Let neutral macros have lengths

\[
L_1,\ldots,L_m
\]

with phase starts

\[
s_0<s_1<\cdots<s_m,
\qquad
s_{i+1}=s_i+L_i,
\]

all at the same height \(h\).

For each macro,

\[
Q_i=b_{s_{i+1}}-b_{s_i}.
\]

Hence

\[
\begin{aligned}
\prod_{i=0}^{m-1}
\frac{2^{L_i}}{3^{Q_i}}
&=
\frac{2^{s_m-s_0}}
{3^{\sum_i(b_{s_{i+1}}-b_{s_i})}}\\
&=
\frac{2^{s_m-s_0}}
{3^{b_{s_m}-b_{s_0}}}\\
&=
\boxed{
\frac{c_{s_m,h}}{c_{s_0,h}}.
}
\end{aligned}
\]

Using \(c_{s,h}=3^{-h-\delta_s}\),

\[
\boxed{
\prod_i\frac{2^{L_i}}{3^{Q_i}}
=3^{\delta_{s_0}-\delta_{s_m}}.
}
\]

Since both phase defects lie in \((0,1)\),

\[
\boxed{
\frac13
<
\prod_i\frac{2^{L_i}}{3^{Q_i}}
<3.
}
\]

This bound is independent of the number of neutral excursions.

## 3. Interpretation

A one-slack neutral macro can have an apparent normalized expansion

\[
1<2^L/3^Q<3,
\]

but this expansion merely moves the mechanical phase defect \(\delta_s\).

A later full-barrier neutral macro moves it back in the opposite direction. Across any concatenation the factors telescope to the endpoint phase ratio.

Therefore the low-q/high-q alternation inside a bounded-height neutral tail does **not** create an additional exponential coefficient factor.

The unresolved long-run quantity must come from the genuinely arithmetic part:

- ternary syndrome mismatch;
- affine correction;
- their cross-base interaction with the dyadic Hensel query.

The mechanical coefficient factor is already an exact bounded coboundary.

## 4. Relation to the rank-one boundary cocycle

The earlier Fourier/slack transfer identity isolated failures of exact 3-frequency covariance at Beatty rises as rank-one slack-zero boundary insertions.

The present result is the min-plus/sparse-tail counterpart of the same fact:

\[
\boxed{
\text{one-slack coefficient expansion}
=
\text{phase-boundary coboundary, not a free exponential loss.}
}
\]

Thus the bulk Haar analysis and the sparse-tail min-plus analysis are now using the same mechanical boundary object from two different representations.

## 5. Revised front

After the height-excursion reduction and this coboundary identity, the deterministic tail target can be stated more narrowly:

> On height-neutral excursions, quotient out the exact phase coboundary and prove that the remaining ternary syndrome/correction cocycle cannot support an infinite eventual-zero Hensel tail.

Strict height-gain macros are already nonnegative in normalized transport. Neutral coefficient scaling is now bounded exactly. What remains is a cross-base arithmetic obstruction rather than a coefficient-growth obstruction.

Finite exact regression:

`collatz/src/height_neutral_phase_coboundary_certificate.py`.
