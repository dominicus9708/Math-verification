# Support-size barrier for uniform selector Fourier mixing

Date: 2026-08-13

Status: **exact finite-group lower bound**. It proves that uniform `L^2` mixing of a `2^d`-point ternary selector family modulo `2^r` is structurally impossible once the binary modulus contains substantially more points than the selector family. This is a proof-strategy limitation theorem, not a Collatz result.

## 1. Selector measure

Let

\[
S_d=
\left\{
\sum_{i=0}^{d-1}a_i3^i:
 a_i\in\{0,1\}
\right\}
\]

with the uniform selector measure reduced modulo

\[
q=2^r.
\]

Denote the resulting probability mass function by `mu`.

There are at most

\[
2^d
\]

atoms with positive mass, even if all residues are distinct.

## 2. Collision lower bound

By Cauchy--Schwarz on the support,

\[
1
=\left(\sum_x\mu(x)\right)^2
\le
|\operatorname{supp}\mu|
\sum_x\mu(x)^2
\le
2^d\sum_x\mu(x)^2.
\]

Hence

\[
\boxed{
\sum_x\mu(x)^2
\ge2^{-d}.
}
\]

The normalized nontrivial Fourier energy is

\[
E_{d,r}
:=
\sum_{k=1}^{q-1}|\widehat\mu(k)|^2.
\]

Parseval gives

\[
E_{d,r}+1
=q\sum_x\mu(x)^2.
\]

Therefore

\[
\boxed{
E_{d,r}
\ge
2^{r-d}-1.
}
\]

This bound is independent of the arithmetic structure of the powers of three.

## 3. Consequence for uniform-energy transport hypotheses

The earlier uniform-energy transport theorem asks, schematically,

\[
E_{d,r}\le\varepsilon^2\beta_L
\]

with `epsilon<1/2` and boundary density `beta_L<=1`.

Thus its right side is strictly smaller than `1/4`.

But if

\[
r\ge d+1,
\]

then

\[
E_{d,r}\ge1.
\]

Consequently

\[
\boxed{
\text{the uniform-energy hypothesis is impossible whenever }r>d.
}
\]

Even at `r=d`, the lower bound is zero only in the ideal injective/uniform case and gives no generic margin.

## 4. Meaning for the full m=44 block

The full recursively sufficient block has only

\[
2^{44}
\]

ternary selector assignments.

The reduced binary coordinate at Collatz depth `L` has exponent

\[
r=L-2.
\]

Therefore any proof route demanding small **global** selector Fourier energy must encounter a hard support-size barrier once

\[
L-2>44,
\]

i.e. once binary resolution passes roughly the selector depth.

This is not a computational limitation. It is an exact cardinality obstruction.

## 5. Why spectral complementarity is necessary

The signed transport error is not the total selector discrepancy. It is

\[
K_L
=\frac1N
\sum_{k\text{ odd}}
\widehat c(k)
\overline{\widehat w_L(k)}.
\]

Thus selector Fourier coefficients may remain large on many frequencies, provided the coefficient-survivor / boundary transform is small precisely there.

The spectral-exception splitting lemma exploits this distinction:

- a large frequency set can be handled by selector attenuation;
- the unavoidable high-resolution exceptional set can be handled by Beatty-survivor or oriented-boundary cancellation.

Hence spectral complementarity is not merely a way to sharpen constants. Beyond `r~d`, it is structurally required if the proof is to continue in Fourier space.

## 6. DSD/set-aggregation interpretation

This barrier identifies exactly where one descriptive channel ceases to carry enough information:

\[
\boxed{
\text{finite ternary selector channel}
\not\Rightarrow
\text{global high-resolution dyadic uniformity}.
}
\]

The correct next operation is not to force more information from that exhausted channel, but to preserve the cross-channel correlation with the independent Beatty boundary structure.

This is the same methodological pattern that previously ruled out fixed-low-bit sieves and scalar defect-density refinement.
