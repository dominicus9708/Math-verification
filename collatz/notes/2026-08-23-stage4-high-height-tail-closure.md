# Stage 4 high-height renewal tail closes automatically

Date: 2026-08-23

Status: **exact finite high-height tail theorem. Incoming relative height H>=5 automatically satisfies the current K<15 Stage-4 window target, independently of selector concentration. This is not a proof of the Collatz conjecture.**

## 1. Why height should be tested against the K<15 target

The current Stage-4 reduction only needs the selector/dyadic conditional amplification in each normalized 28-step window to satisfy

\[
K<15,
\]

because

\[
\frac{\log_2 15}{28}<\frac7{50}.
\]

Therefore a tail state need not be close to uniform. It is enough that the dyadic probability of a coarse necessary continuation event exceed 1/15, since any conditioned selector probability is at most one.

## 2. Coarse L7 continuation language

The exact length-7 full-Hensel residue-maximal rule leaves

\[
(c_q)_{q=0}^7=(1,2,6,15,21,16,7,1)
\]

classes, hence exactly

\[
\boxed{69}
\]

residue-maximal seven-bit words.

Take a 28-step window as four aligned seven-step blocks. For a length-28 mechanical/Sturmian factor `m`, incoming relative height H, and a candidate four-block word `w`, require the cumulative actual-minus-mechanical odd-count difference never to drive the relative height below zero.

This is deliberately a **stricter** event than merely ending coefficient-admissibly. Therefore its dyadic mass is a valid lower bound for the coarser Stage-4 continuation language. Optional stronger depth-28 Hensel filters are not imposed here; proving extinction for the coarser L7 language is sufficient.

## 3. Exact all-phase dynamic program

There are exactly 29 length-28 mechanical factors by Sturmian complexity.

For each factor and incoming H, an exact integer dynamic program enumerates the 69 choices in each of the four seven-step blocks while enforcing nonnegative relative height at every internal bit.

The minimum counts over all 29 phases are

\[
\boxed{\begin{array}{c|r|c|c}
H& M_H & M_H/2^{28} & 2^{28}/M_H\\\hline
0&1,010,201&0.00376329\ldots&265.7247\ldots\\
1&4,000,391&0.0149026\ldots&67.1023\ldots\\
2&8,172,518&0.0304450\ldots&32.8461\ldots\\
3&12,307,179&0.0458478\ldots&21.8112\ldots\\
4&15,918,777&0.0593020\ldots&16.8628\ldots\\
5&18,633,853&0.0694165\ldots&14.4057\ldots
\end{array}}
\]

The worst factor for H=0,...,5 is the phase beginning with

`1101101101011011010110110110`.

The certificate is

`collatz/src/stage4_high_height_tail_threshold_certificate.py`.

## 4. Exact H=5 threshold

The decisive integer comparison is

\[
15\cdot18,633,853
=279,507,795
>268,435,456
=2^{28}.
\]

Thus for every mechanical phase and every incoming

\[
H\ge5,
\]

the dyadic probability of the coarse admissible next-window event satisfies

\[
\boxed{
\nu(A\mid\text{past})>\frac1{15}.
}
\]

The parity-vector bijection makes this statement independent of the previous dyadic prefix: after any fixed parity history, the next 28 parity bits are uniformly represented by the 2^28 lifts of the corresponding dyadic cylinder.

For **any** conditioned selector measure mu,

\[
\mu(A\mid\text{past})\le1.
\]

Hence

\[
\boxed{
K
=\frac{\mu(A\mid\text{past})}{\nu(A\mid\text{past})}
<15.
}
\]

No ternary equidistribution, Fourier decay, selector independence, Hensel-syndrome mixing, or hard-set geometry is used.

Monotonicity in incoming height then gives the same conclusion for every H>5.

## 5. H=4 is the exact boundary of this automatic argument

At H=4,

\[
15\cdot15,918,777
=238,781,655
<2^{28}.
\]

So the selector-free `mu<=1` argument does not close H=4.

The remaining low-height states have the following sufficient selector survival caps:

\[
\mu(A\mid\text{past})
<15\frac{M_H}{2^{28}}.
\]

Numerically,

\[
\boxed{\begin{array}{c|c|c}
H&\text{maximum selector survival sufficient for }K<15&\text{required selector loss}\\\hline
0&0.0564494\ldots&0.9435506\ldots\\
1&0.2235393\ldots&0.7764607\ldots\\
2&0.4566750\ldots&0.5433250\ldots\\
3&0.6877172\ldots&0.3122828\ldots\\
4&0.8895310\ldots&0.1104690\ldots
\end{array}}
\]

Thus the hardest low-height state is H=0, while H=4 needs only about eleven percent genuine selector-side pruning.

## 6. Consequence for the renewal tail

The previous tail formulation allowed unbounded relative height. That is no longer necessary.

Every branch reaching

\[
\boxed{H\ge5}
\]

at a normalized 28-step boundary already lies below the Stage-4 repair-rate threshold without any cross-base theorem.

Therefore any still-dangerous recurrent tail must remain in the finite boundary-height set

\[
\boxed{H\in\{0,1,2,3,4\}.}
\]

This combines with the already proved phase-adjusted credit theorem:

\[
\log_3(1+|\delta|)-H=O(\log n),
\]

so predecessor-credit amplitude cannot add a positive exponential state rate.

The asymptotic obstruction is consequently reduced again:

\[
\boxed{
\text{low-height }H=0,1,2,3,4
+\text{ same-word mixed-place address consistency}.
}
\]

High positive excursions are no longer part of the unresolved exponential mechanism.

## 7. Next target

The next useful calculation is now finite-height rather than unbounded-height:

> **Low-height conditional selector theorem.** For H=0,...,4, bound the conditioned selector survival in the next 28-step coarse L7 window by the state-dependent caps in Section 5, after quotienting the already closed active-prefix dynamic range and the subexponential credit coordinate.

The caps become rapidly weaker as H increases, so H=4 and H=3 should be attacked first before the neutral H=0 renewal state.
