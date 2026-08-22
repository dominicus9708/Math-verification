# Stage 4 phase coupling reduces the low-height core to H=0,1,2

Date: 2026-08-23

Status: **exact two-window phase-coupled reduction. The recurrent H<=4 dyadic tail has paired-window growth below 2^56/27^2, making incoming H=3 and H=4 automatic under the resulting K<27 allowance. This is not a proof of the Collatz conjecture.**

## 1. Why one-window phase maxima were conservative

The previous five-state theorem took an entrywise maximum over all 29 length-28 mechanical factors. That is safe but treats the phase in each 28-step window as if it could be selected independently at every renewal.

Actual mechanical phases are consecutive pieces of one Sturmian word. Two adjacent 28-step factors must therefore occur as the two halves of one genuine length-56 mechanical factor.

By Sturmian complexity there are exactly

\[
\boxed{57}
\]

length-56 factors.

This permits an exact two-window transfer calculation with no independence assumption.

## 2. Exact phase-coupled products

For every length-56 factor f, let

\[
A_f=M(f_{0:28}),\qquad B_f=M(f_{28:56}),
\]

where M is the exact 5x5 low-height L7 transition matrix on H=0,...,4.

The actual two-window transition is

\[
P_f=A_fB_f.
\]

Taking the entrywise maximum over the 57 valid products gives

\[
\boxed{
P_{\max}=\begin{pmatrix}
4709421358346&7744866676304&7670797286990&5999871745251&3931277521274\\
9521862039229&15725022326620&15695964387979&12411279261747&8577093938463\\
14963913688538&23124916672335&23328486390428&20201136545720&14862015977263\\
20748223588891&28263853200163&31082461023064&27663177870105&20858027238992\\
24261344257732&32371839267296&35900713158080&32627673098366&25216795272193
\end{pmatrix}.
}
\]

Certificate:

`collatz/src/stage4_two_window_phase_coupled_low_height_certificate.py`.

## 3. Exact K=27 positive-potential certificate

Use

\[
\boxed{v=(1000,2079,3295,4436,5216)^T.}
\]

The verifier proves the exact componentwise inequality

\[
\boxed{
27^2P_{\max}v<2^{56}v.
}
\]

The five exact positive margins are

\[
\begin{aligned}
&4,109,508,166,883,587,906,\\
&8,580,796,628,714,270,379,\\
&13,597,251,382,603,218,883,\\
&18,253,510,244,244,237,335,\\
&21,469,173,645,056,837,384.
\end{aligned}
\]

Thus every genuine two-window phase product contracts this positive potential relative to the full dyadic mass by more than a factor

\[
\frac1{27^2}.
\]

Equivalently, the recurrent low-height dyadic language has per-28-step exclusion rate strictly larger than

\[
\boxed{
\frac{\log_2 27}{28}
\approx0.1698174108.
}
\]

Therefore a paired-window selector/dyadic amplification below

\[
\boxed{27}
\]

per 28 steps is sufficient on this recurrent branch.

## 4. H=3 now closes automatically

The exact minimum one-window low-to-low counts over all 29 phases remain

\[
(M_0,M_1,M_2,M_3,M_4)
=(961664,3750104,7424983,10555305,12076300).
\]

For H=3,

\[
27\cdot10,555,305
=284,993,235
>268,435,456
=2^{28}.
\]

Thus the dyadic probability of a low-to-low next window is greater than 1/27 in every phase. Since any conditioned selector probability is at most one,

\[
\boxed{K_{\rm low}(H=3)<27}
\]

without any selector equidistribution or cross-base regularity theorem.

H=4 was already automatic under K<25 and remains so here. Together with the earlier H>=5 K<15 theorem, every incoming state

\[
\boxed{H\ge3}
\]

is now automatically controlled.

## 5. Remaining three incoming states

Only

\[
\boxed{H=0,1,2}
\]

remain genuinely cross-base.

Under the new K<27 allowance, sufficient conditioned-selector survival caps for a next low-to-low window are

\[
\mu(A_H\mid\text{past})
<27\frac{M_H}{2^{28}}.
\]

Numerically,

\[
\boxed{\begin{array}{c|c|c}
H&\text{sufficient selector survival cap}&\text{required selector loss}\\\hline
0&0.0967268944\ldots&0.9032731056\ldots\\
1&0.3771961033\ldots&0.6228038967\ldots\\
2&0.7468258627\ldots&0.2531741373\ldots
\end{array}}
\]

The next natural target is therefore H=2: only about 25.32% conditioned selector loss is needed in the worst mechanical phase.

## 6. Structural consequence

The Stage-4 tail has now been separated into three pieces:

1. selector-active prefix: exact total nested amplification <65/64;
2. incoming H>=3 tail: automatically below the available branch-specific repair budget;
3. incoming H=0,1,2 recurrent core: the only remaining same-word cross-base address problem.

The phase-adjusted predecessor-credit coordinate remains subexponential, so it does not restore an independent linear repair rate.

Hence the remaining proof-level obstruction is narrower than a generic renewal-transversality theorem:

\[
\boxed{
\text{three low-height states }H=0,1,2
+\text{ ternary-selector/dyadic same-address consistency}.
}
\]

## 7. Next target

The shortest next route is to attack H=2 directly. A proof that arbitrary previous low-height conditioning forces at least approximately 25.32% of conditioned selector mass out of the next H=2 low-to-low L7 window would remove H=2 and leave only H=0,1.

The exact odd-frequency child-correlation identity already isolates the relevant cross-base object, so the next calculation should specialize that identity to the H=2 boundary language rather than return to full equidistribution.
