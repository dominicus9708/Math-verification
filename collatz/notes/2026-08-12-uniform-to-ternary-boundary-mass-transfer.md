# Uniform-dyadic to ternary boundary-mass transfer by discrepancy

Date: 2026-08-12

Status: **exact measure-transfer inequality + full-m44 finite certificate through depth 26**. A single L1 discrepancy between the ternary subset-sum measure and uniform dyadic measure controls how much of the coefficient-tree one-child boundary abundance survives after restricting to the recursively sufficient ternary core. This bridges the cumulative dyadic entropy theorem to the actual representative measure at finite resolution. This does not provide a uniform asymptotic discrepancy theorem for all growing resolutions.

## 1. Measures at a parent modulus

Fix a reduced dyadic parent modulus

\[
M=2^{L-2}.
\]

Let

\[
\mu_d
\]

be the normalized ternary representative distribution of

\[
Y=3^{44}+\sum_{i=0}^{d-1}a_i3^i
\pmod M,
\qquad a_i\in\{0,1\},
\]

and let

\[
U_M(r)=1/M
\]

be uniform measure on `Z/MZ`.

Define the L1 discrepancy

\[
\boxed{
\mathcal E_M(d)
:=\|\mu_d-U_M\|_1.
}
\]

## 2. Set-mass transfer inequality

For any residue subset

\[
A\subseteq\mathbb Z/M\mathbb Z,
\]

total variation gives

\[
\boxed{
\left|
\mu_d(A)-\frac{|A|}{M}
\right|
\le\frac12\mathcal E_M(d).
}
\]

Let `R_L` be the coefficient-survivor parent set and let

\[
D_L\subseteq R_L
\]

be its one-child boundary subset.

Put

\[
p_L:=\frac{|R_L|}{M},
\qquad
\eta_L^{\rm dyn}:=\frac{|D_L|}{|R_L|}.
\]

Then

\[
\mu_d(D_L)
\ge p_L\eta_L^{\rm dyn}-\frac12\mathcal E_M(d),
\]

while

\[
\mu_d(R_L)
\le p_L+rac12\mathcal E_M(d).
\]

Therefore the one-child fraction under the actual ternary representative measure obeys

\[
\boxed{
\eta_L^{\rm tern}
:=\frac{\mu_d(D_L)}{\mu_d(R_L)}
\ge
\frac{p_L\eta_L^{\rm dyn}-\mathcal E_M(d)/2}
{p_L+\mathcal E_M(d)/2}.
}
\]

This is valid whenever the numerator is positive.

## 3. Interpretation

The transfer loss is controlled by the ratio

\[
\boxed{
\mathcal E_M(d)/p_L.
}
\]

Thus absolute equidistribution is not the right requirement. What matters is discrepancy **relative to the already-rare dangerous set density**.

If

\[
\mathcal E_M(d)=o(p_L),
\]

then

\[
\eta_L^{\rm tern}
=\eta_L^{\rm dyn}+o(1).
\]

This is the exact bridge needed to transfer the cumulative one-child entropy lower bound from the dyadic survivor language to the ternary representative mass.

## 4. Full m=44 discrepancy through depth 26

For the complete `m=44` block (`d=44`), exact cyclic subset-sum aggregation gives

\[
\boxed{
\begin{array}{c|c}
L&\mathcal E_{2^{L-2}}(44)\\\hline
17&8.1483292433\times10^{-6}\\
18&1.1459139159\times10^{-5}\\
19&3.7621420688\times10^{-5}\\
20&5.3541781199\times10^{-5}\\
21&6.0664797957\times10^{-5}\\
22&1.3324686074\times10^{-4}\\
23&1.5301387202\times10^{-4}\\
24&2.3074975979\times10^{-4}\\
25&3.3391567990\times10^{-4}\\
26&4.9563922357\times10^{-4}
\end{array}
}
\]

Even at `L=26` the entire ternary block differs from uniform reduced dyadic mass by less than five parts in ten thousand in L1.

## 5. Boundary transfer examples

The following table compares the uniform dyadic one-child fraction, the exact ternary-mass fraction, and the discrepancy-only rigorous lower bound:

\[
\boxed{
\begin{array}{c|c|c|c}
L&\eta_L^{\rm dyn}&\eta_L^{\rm tern}&\text{discrepancy lower bound}\\\hline
17&0.227294229&0.227294221&0.227255477\\
19&0.176917945&0.176917966&0.176724397\\
20&0.294386710&0.294387017&0.294054397\\
22&0.189193538&0.189193308&0.188303034\\
23&0.302315662&0.302315618&0.301079020\\
25&0.190085874&0.190086096&0.187184941
\end{array}
}
\]

Thus the uniform-language boundary abundance transfers to the actual full `m=44` representative mass with very small loss throughout the certified range.

## 6. Combination with formation child imbalance

At a rise step, child transport gives

\[
C_{L+1}
\le
C_L-\frac12\left(M_D^{\rm tern}(L)-U_{L-2}(d)\right).
\]

Divide by `C_L`. Using the discrepancy transfer for

\[
M_D^{\rm tern}(L)/C_L
\]

and the formation-only child-imbalance theorem for `U`, one obtains a fully separated conservative contraction:

\[
\boxed{
\frac{C_{L+1}}{C_L}
\le
1-\frac12
\left(
\underline\eta_L^{\rm tern}
-rac{U_{L-2}(d)}{C_L}
\right).
}
\]

No signed dynamical/formation cancellation is required.

## 7. What remains for a growing-resolution theorem

Three ingredients are now mathematically isolated:

1. **dyadic cumulative boundary abundance** — already controlled by the coefficient-survivor entropy theorem;
2. **uniform-to-ternary boundary transfer** — controlled by `E_M(d)/p_L`;
3. **opposite-child imbalance** — controlled by `U_j(d)`.

A terminal growing-resolution theorem would follow from proving, over enough resolutions, that

\[
\boxed{
\mathcal E_{2^{L-2}}(d)
\ll p_L
}
\]

and

\[
\boxed{
U_{L-2}(d)/C_L
}
\]

is cumulatively smaller than the transferred boundary fraction.

The present full-block data show this regime holds strongly through depth 26; the unresolved problem is to make it uniform as `L` grows with selector depth.