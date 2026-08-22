# Stage 4 strengthened by short-block residue maximality

Date: 2026-08-19

Correction date: 2026-08-20

Status: **conditional language-exclusion calculation retained; unconditional repeated-minimality interpretation withdrawn pending prefix pullback.** This is not a proof of the Collatz conjecture.

## 0. 2026-08-20 correction

The local Hensel identity used below is exact: if a length-L word w has a larger-correction representative u in the same full-Hensel class,

\[
R_u-R_w=3^q\Delta>0,
\]

then starting u at \(x-\Delta\) merges with w started at x after L steps.

However, for a later block of a hypothetical minimal counterexample N, the block start is \(x=T^s(N)\ge N\). The inequality \(x-\Delta<x\) does not imply \(x-\Delta<N\). Local minimality excludes the block immediately only when

\[
\boxed{\Delta>x-N,}
\]

or when a separate prefix-pullback theorem constructs a smaller positive original start.

Therefore the repeated residue-maximal language used in this note remains a valid conditional combinatorial language, but it is not currently established as a mandatory language for every later block of a minimal counterexample.

Companion correction note:

`collatz/notes/2026-08-20-stage3c-pullback-correction-and-safe-stage4.md`.

Exact headroom certificate:

`collatz/src/stage3c_pullback_headroom_certificate.py`.

## 1. Previous Stage 4 budget

The H19 residue-maximal language gave an exact exclusion rate above 1/9 after rational weight optimization. Under the now-withdrawn unconditional repeated-maximality interpretation this improved the required same-integer overlap theorem to

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}H<\frac19.
\]

The numerical language bound remains correct conditionally.

## 2. Local residue maximality is not intrinsically length 19

For any fixed binary block length L and fixed odd count q, group words by their full-Hensel correction residue

\[
R(w)\pmod{3^q}.
\]

If a word w is not the maximum-correction member of its class, choose u in the same class with larger correction. Then

\[
R_u-R_w=3^q\Delta,\qquad \Delta>0,
\]

and starting u at \(x-\Delta\) gives exactly the same L-step endpoint as starting w at x.

This is an exact **local merge theorem**. It does not by itself imply repeated global maximality at later block starts.

## 3. Exact L=7 local and conditional-language theorem

The complete \(2^7\) cube has full-Hensel class counts

\[
(c_q)_{q=0}^{7}=(1,2,6,15,21,16,7,1).
\]

The largest ordinary local predecessor credit in any class is exactly

\[
\boxed{\Delta_{\max}=21}.
\]

The full positive local-deficit alphabet is

\[
\boxed{D_7=\{1,2,4,5,8,10,16,17,20,21\}.}
\]

At a block with numerical headroom \(h=x-N\), local minimality alone permits every word with \(\Delta(w)\le h\). Exact counts are

\[
\begin{array}{c|rrrrr}
h&0&1&2&5&21\\\hline
\#\text{ locally permitted words}&69&93&106&118&128.
\end{array}
\]

Thus only the first block \(x=N\), or a later block with an independently controlled headroom/pullback, is forced into the maximum-correction sublanguage.

For the **conditional** language in which every aligned seven-step block is residue-maximal, use \(z=4/3\). Writing

\[
P_5(z)=\sum_{q=0}^7 c_q z^{q-5},
\]

a Q=4 block costs the extra factor z.

Over a 700-step macro there are 100 seven-step blocks. Since

\[
3^{441}<2^{700}<3^{442},
\]
there can be at most 59 Q=4 blocks. Hence

\[
F=P_5(4/3)^{100}(4/3)^{59}.
\]

The exact rational certificate proves

\[
F^{50}<2^{30100},
\]
so

\[
F<2^{602}.
\]

Therefore the conditional repeated-residue-maximal language loses strictly more than 98 bits per 700 steps:

\[
\boxed{\eta_{\rm conditional}>\frac7{50}=0.14.}
\]

Certificate:

`collatz/src/l7_residue_maximal_seven_fiftieths_macro_certificate.py`.

## 4. Conditional Stage 4 consequence

If a future prefix-pullback theorem proves that the relevant candidate trajectories really lie in the repeated L7 residue-maximal language, then the same-integer overlap target

\[
\limsup_{H\to\infty}\frac{\log_2\Xi_{m,H}}H<\frac7{50}
\]

and, in the subexponential case, the slope

\[
H>Cm,\qquad C>\frac{50}{7}
\]

become sufficient again.

At present these statements are **conditional strengthening targets**, not the unconditional Stage 4 theorem.

## 5. Mandatory mod-4 normalization

Coefficient survival forces the first two parity bits to be 11, hence

\[
N\equiv3\pmod4.
\]

The reduced Cantor core has the same forced cylinder. Therefore the raw overlap factor contains a constant factor four, and the normalized amplification remains

\[
\boxed{\Xi^\circ_{m,H}=\Xi_{m,H}/4.}
\]

This normalization does not change exponential rates.

## 6. Exact L8 finite calibration: retained as conditional evidence

The L8 verifier checks the candidate family

\[
N=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

under coefficient survival plus repeated aligned L8 residue-maximality.

Selected exact counts remain

\[
\begin{array}{c|rrrr}
m & H=32&H=64&H=96&H=128\\\hline
20&9981&251&9&1\\
21&20200&474&10&0\\
22&40359&1022&28&0.
\end{array}
\]

Certificate:

`collatz/src/l8_small_core_multiwindow_overlap_certificate.cpp`.

These are exact finite facts about the stronger conditional language. They must not be interpreted as coefficient-only extinction.

## 7. Unconditional fallback

The logically safe Stage 4 language is coefficient survival alone:

\[
\mathcal B_H=\{3^{q_k}\ge2^k\text{ for every }k\le H\}.
\]

Its exclusion rate is

\[
\eta_{\rm coeff}
=1-H_2(\log_3 2)
\approx0.05004447.
\]

The unconditional sufficient target is to control the normalized same-integer overlap between the reduced ternary-selector core and \(\mathcal B_H\), preferably by

\[
\boxed{\Xi^{\circ,\rm coeff}_{m,H}=2^{o(H)}.}
\]

Under that stronger form, a horizon slope

\[
\boxed{H>Cm,\qquad C>1/\eta_{\rm coeff}\approx19.9823}
\]

is sufficient up to fixed boundary constants.

The finite m=45 depth-28 selector-transversality and mass-transport certificates remain relevant to this unconditional route because they do not depend on repeated residue-maximality.

## 8. Revised structural target

The main proof-level target is now:

> **Renewal-conditioned coefficient-language transversality theorem.** After conditioning on previously survived dyadic/renewal information, prove that the reduced ternary-selector distribution cannot acquire a positive exponential concentration inside the coefficient-survival language.

A future prefix-pullback theorem may safely reintroduce the stronger L7/H19 conditional entropy gains.
