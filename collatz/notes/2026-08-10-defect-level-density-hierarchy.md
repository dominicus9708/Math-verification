# Defect-level density hierarchy

Date: 2026-08-10

Status: **DERIVED COROLLARY OF THE DEFECT-RUN AVERAGE LEMMA**

## 1. Level sets of the defect process

Keep

\[
z_i=\kappa_i-d_i\ge0,
\qquad
u_i=\frac13 2^{-\{i\log_2 3\}}.
\]

For each integer `s>=1`, define

\[
E_s=\{i:z_i\ge s\},
\qquad
N_{\ge s}=|E_s|.
\]

Because

\[
z_{i+1}\le z_i+(\kappa_{i+1}-\kappa_i)-1,
\]

a transition from `z_i<s` to `z_{i+1}>=s` can occur only when the mechanical cap increment is two. Thus every connected component of `E_s` starts at the same legal rotation-phase type as an ordinary positive-defect run.

Therefore the run-average lemma applies to every level set:

\[
\sum_{i\in E_s}u_i\ge\frac5{24}N_{\ge s}.
\]

## 2. Correction loss at level s

At every `i in E_s`,

\[
1-2^{-z_i}\ge1-2^{-s}.
\]

Hence

\[
\Delta S=S^*-S
\ge
(1-2^{-s})\sum_{i\in E_s}u_i
\ge
\frac5{24}(1-2^{-s})N_{\ge s}.
\]

Thus

\[
\boxed{
N_{\ge s}
\le
\frac{24\Delta S}{5(1-2^{-s})}
\qquad(s\ge1).
}
\]

For `s=1` this reduces to

\[
N_{\rm def}\le\frac{48}{5}\Delta S.
\]

## 3. Next unresolved convergent resonance, m=46 layer

Using the current correction-loss allowance

\[
\Delta S\lesssim1.2096147806253557\times10^9
\]

at

\[
q=137,528,045,312,
\]

the relative level-set bounds are approximately

\[
\begin{array}{c|ccccc}
s&1&2&3&4&5\\\hline
N_{\ge s}/q
&0.084435883
&0.056290588
&0.048249076
&0.045032471
&0.043579810
\end{array}
\]

Therefore a hypothetical paradoxical candidate must satisfy simultaneously:

- at least `91.5564%` of odd positions have `z_i=0`;
- at least `94.3709%` have `z_i<=1`;
- at least `95.1751%` have `z_i<=2`;
- at least `95.4968%` have `z_i<=3`;
- at least `95.6420%` have `z_i<=4`.

The bounds are deterministic necessary conditions for this resonance/layer. They do not establish nonexistence.