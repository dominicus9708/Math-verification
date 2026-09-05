# Stage 4 low-height tail reduces to four incoming states

Date: 2026-08-23

Status: **exact low-height finite-state reduction. The recurrent H<=4 L7 tail has weighted dyadic growth below 2^28/25, and incoming H=4 is automatically below the corresponding K<25 cross-base threshold. This is not a proof of the Collatz conjecture.**

## 1. Start from the high-height closure

The companion high-height theorem proves that every incoming relative height

\[
H\ge5
\]

already satisfies the original Stage-4 conditional-window target

\[
K<15
\]

without any selector regularity assumption.

Therefore a still-dangerous recurrent tail can be restricted to

\[
H\in\{0,1,2,3,4\}.
\]

## 2. Exact low-to-low 28-step transition matrices

For each of the 29 length-28 mechanical factors, enumerate the four concatenated length-7 residue-maximal words and retain only paths that

1. never make relative height negative; and
2. end in H'=0,...,4.

This gives a 5x5 nonnegative integer transition matrix M_f for each mechanical phase f.

Taking the entrywise maximum over all 29 phases gives

\[
\boxed{
M_{\max}=\begin{pmatrix}
707250&1085037&1074609&753120&408810\\
1466790&2004684&2090340&1590685&966818\\
2079878&2667698&2878633&2447289&1711766\\
2248621&3088826&3232283&3106984&2515663\\
2021037&2995290&3332320&3352635&3137392
\end{pmatrix}.
}
\]

Certificate:

`collatz/src/stage4_five_state_low_height_tail_certificate.py`.

## 3. Exact 1/25 weighted growth certificate

Use the positive integer potential

\[
\boxed{v=(1000,2044,3038,3774,4088)^T.}
\]

The certificate verifies the five strict integer inequalities

\[
\boxed{
25M_{\max}v<2^{28}v
}
\]

entrywise.

The exact margins are respectively

\[
855,007,750,
\quad1,921,717,314,
\quad2,714,218,828,
\quad3,284,284,494,
\quad3,726,621,478.
\]

Therefore every product of the actual phase matrices is dominated in this positive potential by a per-window factor strictly below

\[
\frac{2^{28}}{25}.
\]

Equivalently, the recurrent low-height dyadic language has exclusion rate strictly larger than

\[
\boxed{
\frac{\log_2 25}{28}
\approx0.165852.
}
\]

This is stronger than the generic Stage-4 L7 rate 7/50=0.14 because paths that escape to H>=5 have already been removed into the automatically controlled branch.

## 4. New branch-specific cross-base allowance

For this recurrent low-height branch it is therefore sufficient to establish a conditional selector/dyadic amplification

\[
\boxed{K_{\rm low}<25}
\]

per normalized 28-step low-to-low transfer.

This is substantially weaker than the previous universal K<15 target.

## 5. Incoming H=4 closes automatically

For each incoming state H, take the minimum over all 29 phases of the total number of low-to-low continuations. The exact values are

\[
\boxed{\begin{array}{c|r}
H&\min_f\sum_{H'=0}^4 M_f(H,H')\\\hline
0&961,664\\
1&3,750,104\\
2&7,424,983\\
3&10,555,305\\
4&12,076,300
\end{array}}
\]

For H=4,

\[
25\cdot12,076,300
=301,907,500
>2^{28}=268,435,456.
\]

Thus under dyadic measure every phase has low-to-low probability greater than 1/25. Any conditioned selector probability is at most one, so

\[
\boxed{K_{\rm low}(H=4)<25}
\]

without any cross-base hypothesis.

Hence H=4 joins H>=5 as an automatically controlled incoming state.

## 6. Remaining incoming heights and exact selector-loss targets

Only

\[
\boxed{H=0,1,2,3}
\]

remain genuinely cross-base.

Using the same K<25 criterion, a sufficient selector survival cap in the next low-to-low window is

\[
\mu(A_{\rm low}\mid\text{past})
<25\frac{M_H^{\min}}{2^{28}}.
\]

Numerically,

\[
\boxed{\begin{array}{c|c|c}
H&\text{sufficient selector survival cap}&\text{required selector loss}\\\hline
0&0.08956194\ldots&0.91043806\ldots\\
1&0.34925565\ldots&0.65074435\ldots\\
2&0.69150543\ldots&0.30849457\ldots\\
3&0.98303938\ldots&0.01696062\ldots
\end{array}}
\]

The H=3 state is therefore extremely close to automatic closure: only about 1.70% selector-side loss is needed in the worst mechanical phase.

## 7. Structural simplification of Stage 4

The L7 residue-maximal condition is itself a local seven-bit property. Once it is used as the coarse minimal-counterexample language, no separate carried Hensel-syndrome state is required to describe the binary tail language. The older depth-28 Hensel syndrome graph remains useful as a stronger finite pruning certificate, but it is not mandatory in the coarse Stage-4 tail automaton.

The remaining asymptotic cross-base object can therefore be stated more simply as

\[
\boxed{
\text{ternary selector address}
\quad\text{vs}\quad
\text{four-state incoming height core }H=0,1,2,3,
}
\]

with deterministic mechanical phase and the already proved subexponential predecessor-credit information.

## 8. Next target

The next calculation should attack H=3 first:

> prove that after arbitrary previous low-height conditioning, at least 1.70% of the conditioned selector mass fails the next H=3 low-to-low L7 window, or obtain the equivalent weighted transfer inequality directly.

If H=3 closes, the target then moves to H=2 with a 30.85% required selector loss, followed by H=1 and the neutral renewal state H=0.
