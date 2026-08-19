# Stage 3C pullback correction and safe Stage 4 fallback

Date: 2026-08-20

Status: **logical correction to repeated residue-maximality; coefficient-only Stage 4 restored as the unconditional fallback.** This is not a proof of the Collatz conjecture.

## 1. What remains valid from the previous Stage 3C

For a fixed length-L block with q odd steps, write the endpoint in the usual affine form

\[
T^L(x)=\frac{3^q x+R_w}{2^L}.
\]

If two words u,w belong to the same full-Hensel correction class and

\[
R_u-R_w=3^q\Delta,\qquad \Delta>0,
\]

then the exact local merge identity is

\[
\frac{3^q(x-\Delta)+R_u}{2^L}
=
\frac{3^q x+R_w}{2^L}.
\]

This local algebra is correct and remains useful.

## 2. Correction: local decrease is not automatically a global minimality contradiction

Let N be a hypothetical minimal counterexample and let a later aligned block begin at

\[
x=T^s(N).
\]

Minimality gives only

\[
x\ge N.
\]

The fact that the alternate local start satisfies

\[
x-\Delta<x
\]

does **not** imply

\[
x-\Delta<N.
\]

Therefore a local residue deficit gives an immediate minimality contradiction only when

\[
\boxed{\Delta>x-N.}
\]

Equivalently, the correct necessary condition for a later block is

\[
\boxed{\Delta\le x-N.}
\]

The first block remains a special case: when x=N, every positive local deficit is contradictory, so the first aligned block must be residue-maximal.

The previous statement that every later block of a sufficiently large minimal counterexample must automatically be residue-maximal is therefore withdrawn unless a separate prefix-pullback theorem is supplied.

## 3. Correct global pullback equation

To turn a local merge into a smaller start at the original coordinate, compare the actual length-s prefix P with an alternate prefix P'. Let a be their common odd count and let their prefix corrections be C_P and C_{P'}.

A local credit \(\Delta\) at depth s pulls back to an integer original-start credit d only if

\[
\boxed{
3^a d
=
2^s\Delta+C_{P'}-C_P.
}
\]

A genuine minimality contradiction requires an integer d with

\[
1\le d<N.
\]

Thus the appropriate replacement for unconditional local maximality is:

> **Pullback-qualified local maximality.** A non-maximal later block is excluded only when its positive local deficit admits an integer prefix pullback to a smaller positive original start.

This turns the missing step into an explicit mixed dyadic/ternary formation problem rather than hiding it inside local Hensel maximality.

## 4. Exact L=7 headroom audit

The full L=7 Hensel class counts remain

\[
(c_q)_{q=0}^7=(1,2,6,15,21,16,7,1).
\]

For each of the 128 binary words define its local deficit from the maximum-correction representative of the same full-Hensel class by

\[
\Delta(w)=\frac{R_{\max}-R_w}{3^q}.
\]

The exact positive deficit alphabet is

\[
\boxed{
D_7=\{1,2,4,5,8,10,16,17,20,21\}.
}
\]

The largest local deficit is still 21, but this number is now interpreted as a **local headroom scale**, not as a universal global minimality threshold.

If the numerical headroom at the block start is

\[
h=x-N,
\]

then the number of seven-bit words not excluded by local minimality alone is exactly

\[
\begin{array}{c|rrrrr}
h&0&1&2&5&21\\\hline
\#\{w:\Delta(w)\le h\}&69&93&106&118&128.
\end{array}
\]

Hence even a small positive headroom rapidly weakens the repeated residue-maximal language restriction.

Certificate:

`collatz/src/stage3c_pullback_headroom_certificate.py`.

## 5. 3-adic terminal localization of the L7 deficits

For the positive L7 deficits,

\[
v_3(21)=1,
\]

while every other element of D7 has 3-adic valuation zero.

Therefore any prefix-pullback construction based on the existing zero-carry/formation recurrence can only repair most L7 local deficits if the actual/alternate prefix has an even-event contribution in the final terminal 3-adic layer; \(\Delta=21\) can extend one layer farther.

This is a useful localization constraint, but it is not by itself a universal pullback theorem because the actual prefix is fixed rather than freely selectable.

## 6. Consequence for the old Stage 3D and L7 entropy calculations

The combinatorial calculations of the residue-maximal languages remain mathematically valid **as conditional language counts**.

In particular the previously certified L7 class polynomial, the 700-step macro bound, and the exclusion estimate

\[
\eta>\frac7{50}
\]

remain correct for the language in which every aligned L7 block is residue-maximal.

However that language is no longer established as a mandatory language for every later block of a minimal counterexample. Therefore the resulting Stage 4 overlap target must be treated as conditional until a repeated pullback theorem is proved.

The same qualification applies to the H19 repeated residue-maximal language.

## 7. Unconditional Stage 4 fallback: coefficient survival only

The safe dyadic language is the coefficient-survival language

\[
\mathcal B_H
=\{\text{parity prefixes}:3^{q_k}\ge2^k\text{ for all }1\le k\le H\}.
\]

Its asymptotic binary exclusion rate is

\[
\boxed{
\eta_{\rm coeff}
=1-H_2(\log_3 2)
\approx0.05004447.
}
\]

Let the reduced ternary-selector core be

\[
\mathcal C_m:
\quad
N=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Define the exact coefficient-only same-integer overlap amplification

\[
\Xi^{\rm coeff}_{m,H}
=
\frac{|
\mathcal C_m\cap\mathcal B_H|/|\mathcal C_m|}
{|
\mathcal B_H|/2^H}.
\]

Both families force the initial cylinder \(N\equiv3\pmod4\), so use the normalized quantity

\[
\boxed{
\Xi^{\circ,\rm coeff}_{m,H}
:=\Xi^{\rm coeff}_{m,H}/4.
}
\]

A sufficient unconditional globalization theorem is again

\[
\boxed{
\Xi^{\circ,\rm coeff}_{m,H}=2^{o(H)}.
}
\]

Under this stronger subexponential form, finite extinction follows for any asymptotic horizon

\[
\boxed{
H>Cm,
\qquad
C>\frac1{\eta_{\rm coeff}}
\approx19.9823.
}
\]

## 8. New coefficient-only finite calibration

Removing every repeated residue-maximality condition and retaining only coefficient survival gives, at H=7m,

\[
\begin{array}{c|rrrrrrrrrr}
m&20&21&22&23&24&25&26&27&28&29\\\hline
|\mathcal C_m\cap\mathcal B_{7m}|
&175&240&361&546&831&1188&1856&2674&3997&5660.
\end{array}
\]

Thus the former 7m extinction is not a coefficient-only phenomenon and depended on the repeated residue-maximal language assumption.

Nevertheless the corresponding mod-4-normalized overlap values stay close to one throughout this finite range (approximately 0.954 to 1.053). This gives finite evidence that the ternary selector core is not exhibiting a positive exponential concentration into the coefficient language.

Exact coefficient-only extinction scans also found

\[
\begin{array}{c|rrrrrrrrrr}
m&20&21&22&23&24&25&26&27&28&29\\\hline
H_0&265&265&317&351&386&340&428&386&441&468,
\end{array}
\]

where H0 is the first depth with no coefficient-surviving candidate.

Together with the smaller-m scan and a separate m=30 exact run,

\[
\boxed{
\mathcal C_m\cap\mathcal B_{17m}=\varnothing
\qquad(8\le m\le30)
}
\]

is a finite computational certificate target. It is **not** proposed as the asymptotic theorem because 17 is below \(1/\eta_{\rm coeff}\).

The last finite survivors die on the coefficient boundary: immediately before failure they satisfy the exact minimal odd-count requirement, and the next required increment occurs on an even parity step.

## 9. Safe mass-transport route

The existing exact selector transport identity is unaffected by the Stage 3C correction. For a coefficient-surviving parent mass C, the next boundary split satisfies

\[
2C_{\rm next}=2C-D+K,
\qquad |K|\le U,
\]

where D is the mass in one-child-surviving boundary parents and U is the selector sibling imbalance.

Hence whenever

\[
U<D,
\]

there is deterministic positive loss

\[
\boxed{
C-C_{\rm next}\ge\frac{D-U}{2}>0.
}
\]

The m=44 finite certificate already verifies this inequality at its checked boundary depths. This provides a logically safe starting point for the remaining cross-base theorem.

## 10. Revised proof front

The main unconditional front is now:

1. retain Stages 1, 2, 3A and 3B;
2. replace Stage 3C by pullback-qualified local minimality;
3. keep residue-maximal entropy results as conditional strengthening lemmas;
4. prove repeated/renewal-conditioned selector transversality for the coefficient-survival language;
5. preferably establish
   \[
   \Xi^{\circ,\rm coeff}_{m,H}=2^{o(H)};
   \]
6. then use a horizon slope strictly above approximately 19.9823.

A future successful prefix-pullback theorem can reintroduce some or all of the residue-maximal entropy gain without compromising the corrected logic.
