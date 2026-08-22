# Record-strip critical Haar reduction

Date: 2026-08-20

Status: **exact Fourier-to-strip-gradient reduction.** This identifies the dyadic critical scale of every nonzero frequency and reduces its record-strip Fourier coefficient to a finite-state child-completion imbalance. It is not yet the required uniform Hensel transversality theorem and not a proof of the Collatz conjecture.

Let \(\mathcal R_{s,r}(L)\) be the length-\(L\) record first-passage language at mechanical phase \(s\) and record height \(r\):

\[
-r\le g_j\le0\quad(j<L),
\qquad g_L=1,
\]

where

\[
g_j=q_j-(b_{s+j}-b_s).
\]

Every parity word \(w\in\{0,1\}^L\) determines a unique canonical start residue

\[
r(w)\pmod{2^L}.
\]

Define the normalized Fourier coefficient of the record residue set by

\[
\widehat\mu_{s,r,L}(t)
=
\frac1{|\mathcal R_{s,r}(L)|}
\sum_{w\in\mathcal R_{s,r}(L)}
\exp\left(\frac{2\pi i t r(w)}{2^L}\right).
\]

## 1. Every nonzero frequency has one exact critical parity bit

Let

\[
0<t<2^L
\]

and write

\[
t=2^v u,
\qquad u\text{ odd}.
\]

Define

\[
\boxed{
j_*=L-v-1.}
\]

Then

\[
\exp\left(\frac{2\pi i t r}{2^L}\right)
=
\exp\left(\frac{2\pi i u r}{2^{j_*+1}}\right),
\]

so the character depends only on the canonical residue modulo \(2^{j_*+1}\), hence only on the first \(j_*+1\) parity bits.

For any common parity prefix of length \(j_*\), its two length-\(j_*+1\) children have canonical residues that differ by exactly

\[
2^{j_*}\pmod{2^{j_*+1}}.
\]

Therefore their characters differ by

\[
\exp\left(\frac{2\pi i u2^{j_*}}{2^{j_*+1}}\right)
=
\exp(\pi i u)
=-1.
\]

Thus

\[
\boxed{
\text{the two critical children have exactly opposite Fourier phase.}
}
\]

This statement is independent of the ternary odd count and of all later suffix bits.

## 2. Strip prefix and suffix kernels

Use the strip coordinate

\[
y_j=-g_j\in\{0,\ldots,r\}.
\]

Let

\[
A_j(y)
\]

be the number of valid strip prefixes of length \(j\) ending at state \(y\).

Let

\[
F_j(y)
\]

be the number of valid completions from state \(y\) after \(j\) steps to the final record exit at length \(L\).

If

\[
d_{j+1}=b_{s+j+1}-b_{s+j}\in\{0,1\},
\]

then the two possible child strip states of a parent state \(y\) are

\[
y_0=y+d_{j+1}
\]

for an even bit and

\[
y_1=y+d_{j+1}-1
\]

for an odd bit, with out-of-strip states assigned completion count zero.

At the critical bit \(j_*\), define

\[
C_0(y)=F_{j_*+1}(y_0),
\qquad
C_1(y)=F_{j_*+1}(y_1).
\]

## 3. Exact pairing by common parent prefix

Fix a particular valid parent prefix \(u\) of length \(j_*\). All full record words extending its even child have one critical character sign, while all full record words extending its odd child have the opposite sign. Since the character already depends only on the first \(j_*+1\) bits, later suffix choices do not change this sign.

Thus the total contribution of this parent is

\[
\chi(u)\bigl(C_0(y)-C_1(y)\bigr)
\]

up to an irrelevant unit sign determined by which child is the lower canonical residue.

Summing over all parent prefixes gives an exact signed gradient representation. Taking absolute values only at the last step yields

\[
\boxed{
|\widehat\mu_{s,r,L}(t)|
\le
\frac{
\sum_{y=0}^{r}
A_{j_*}(y)
|C_0(y)-C_1(y)|
}{|\mathcal R_{s,r}(L)|}.
}
\]

The denominator has the exact decomposition

\[
|\mathcal R_{s,r}(L)|
=
\sum_{y=0}^{r}
A_{j_*}(y)
\bigl(C_0(y)+C_1(y)\bigr).
\]

Hence each dyadic frequency level is controlled by a normalized discrete gradient of the suffix completion kernel.

## 4. Haar interpretation

The previous formula is the record-strip analogue of the selector Haar pairing.

The critical bit separates two dyadic children whose character values are \(+1\) and \(-1\) relative to their common parent. The failure of exact full-cube cancellation is therefore precisely the child-completion imbalance

\[
C_0-C_1.
\]

So the remaining Fourier problem is not an arbitrary exponential sum. It is a finite-state Haar gradient problem on the strip.

The exact correspondence is

\[
\boxed{
\text{dyadic valuation }v_2(t)
\longleftrightarrow
\text{critical bit }j_*=L-v_2(t)-1
\longleftrightarrow
\text{strip suffix-gradient level}.
}
\]

## 5. Coarse/fine frequency split

Let

\[
\ell=L-j_*-1=v_2(t)
\]

be the number of steps after the critical bit.

- Large \(v_2(t)\): the critical bit occurs earlier and there is a long suffix. The suffix completion vector has time to smooth across adjacent strip states, so the gradient term is the natural object to bound.
- Small \(v_2(t)\): the critical bit lies close to the final record exit. The suffix gradient can be order one, so strip smoothing alone is insufficient. These are exactly the finest dyadic levels, where the previously derived selector Haar/martingale bounds are strongest and naturally supply the complementary control.

This leads to the revised Stage-4 splice

\[
\boxed{
\text{record-strip coarse Fourier}
\quad+\quad
\text{selector-Haar fine Fourier}.
}
\]

## 6. Finite exact diagnostics

The companion certificate verifies the critical-child sign algebra exactly and, for \(L=11\), checks every nonzero dyadic frequency directly against the gradient bound.

Long exact integer-transfer diagnostics at \(L=1201\) show that once the critical bit is moved a modest distance away from the terminal exit, the gradient ratio is already substantially below one. For example, the computed interior profiles approach the critical Bernoulli imbalance

\[
|2\alpha-1|
\approx0.2618595
\]

as both prefix and suffix mixing lengths increase.

This numerical convergence is evidence, not the all-width theorem.

## 7. Remaining theorem in its sharpest current form

The required new estimate can now be stated without reference to an unrestricted Fourier sum:

> **Record-strip Harnack/Haar theorem.** Obtain a phase-uniform bound on the normalized adjacent-state completion gradient for critical scales whose suffix is longer than the strip mixing scale, and combine the finitely many terminal dyadic levels with the existing selector Haar energy budget.

The raw strip entropy theorem already supplies a mixing scale of order

\[
(r+1)^2.
\]

The remaining analytic question is whether the completion-kernel gradient admits a correspondingly uniform Harnack-type contraction after that scale.

If so, the previously separate bulk Haar argument and sparse record-tail argument become two halves of the same dyadic martingale decomposition.

Certificate:

`collatz/src/record_strip_critical_haar_certificate.py`.
