# Stage 4 reduces to two genuinely cross-base incoming heights

Date: 2026-08-23

Status: **exact 12-window phase-coupled reduction on the H=0,1,2 recurrent core. Incoming H=2 is automatically below the available branch repair budget, leaving only H=0,1 as genuinely cross-base incoming states. This is not a proof of the Collatz conjecture.**

## 1. Remove the already automatic heights

The preceding certificates established:

- H>=5 is automatic at the universal K<15 scale;
- H=4 is automatic in the five-state low-height branch;
- H=3 becomes automatic after exact two-window phase coupling.

Hence only

\[
H\in\{0,1,2\}
\]

need remain in the recurrent cross-base core.

Any transition ending at H>=3 is now an escape from this unresolved core rather than a new recurrent state.

## 2. Exact three-state 28-step matrices

For each of the 29 length-28 mechanical factors, enumerate the four concatenated residue-maximal seven-bit words, enforce nonnegative relative height internally, and retain only endpoints H'=0,1,2.

The exact minimum row masses over all phases are

\[
\boxed{
(M_0,M_1,M_2)=(683512,2588174,4867480).
}
\]

Thus the worst one-window dyadic survival probabilities inside this three-state core are respectively

\[
0.00254628\ldots,
\quad0.00964170\ldots,
\quad0.01813278\ldots.
\]

## 3. Twelve-window phase coupling

A run of twelve 28-step windows has length

\[
336.
\]

By Sturmian complexity there are exactly

\[
\boxed{337}
\]

genuine length-336 mechanical factors.

For each factor, multiply its twelve actual three-state transition matrices. Taking the entrywise maximum over these 337 genuine products gives a single conservative matrix Pmax^(12).

The exact verifier is

`collatz/src/stage4_three_state_twelve_window_certificate.py`.

## 4. Exact K=56 potential inequality

Use the positive integer potential

\[
\boxed{v=(1000,1903,2829)^T.}
\]

The verifier proves componentwise, with integer arithmetic only,

\[
\boxed{
56^{12}P_{\max}^{(12)}v<2^{336}v.
}
\]

Therefore the recurrent H=0,1,2 dyadic core has twelve-window growth strictly below

\[
\frac{2^{336}}{56^{12}}.
\]

Equivalently its per-28-step exclusion allowance is strictly larger than

\[
\boxed{
\frac{\log_2 56}{28}
\approx0.207405533.
}
\]

Thus a conditional selector/dyadic amplification below 56 at an incoming state is already compatible with extinction of this three-state recurrent branch.

## 5. H=2 is automatic

The exact worst-phase H=2 low-to-{0,1,2} mass is

\[
M_2=4,867,480.
\]

The decisive comparison is

\[
56\cdot4,867,480
=272,578,880
>268,435,456
=2^{28}.
\]

Hence every mechanical phase has dyadic three-state survival probability greater than 1/56 from incoming H=2.

For any conditioned selector measure, the corresponding event probability is at most one. Therefore

\[
\boxed{K(H=2)<56}
\]

without selector equidistribution, Fourier decay, or independence.

So incoming H=2 requires no separate cross-base theorem.

## 6. Remaining incoming states

The only incoming heights that can still require genuine same-integer cross-base control are

\[
\boxed{H=0,1.}
\]

At the K=56 scale, one-window sufficient selector survival caps would be

\[
\begin{array}{c|c|c}
H&56M_H/2^{28}&\text{required selector loss}\\\hline
0&0.142591715\ldots&0.857408285\ldots\\
1&0.539935172\ldots&0.460064828\ldots
\end{array}
\]

The H=1 target is therefore already below a 50% selector-side loss requirement.

## 7. Interpretation

The sequence of reductions is now:

\[
\text{unbounded height}
\to H\le4
\to H\le3
\to H\le2
\to\boxed{H=0,1\text{ only need cross-base control}}.
\]

No random model has been introduced. Each removed height was eliminated by exact dyadic language capacity compared with a rigorously available repair allowance.

The predecessor-credit channel remains subexponential by the phase-adjusted cocycle theorem, and the original m=45 selector-active prefix remains bounded by the nonaccumulating factor 65/64.

The remaining obstruction is therefore a two-state same-word address problem rather than a generic renewal-tail theorem.

## 8. Next target

The next reduction should discard transitions from H=0,1 into H>=2 as already controlled escapes, and compute the phase-coupled two-state recurrent language. This can substantially increase the available repair allowance for the still-unresolved H=0,1 cross-base core before any new Fourier theorem is attempted.
