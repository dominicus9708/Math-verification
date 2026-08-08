# Logarithmic slack reduction for coefficient-surviving parity words

Date: 2026-08-09

## Setup

Let

\[
\alpha=\frac{\log 2}{\log 3},\qquad
a_k=\lceil \alpha k\rceil.
\]

A binary parity word of length \(k\) survives multiplicative coefficient
contraction through every prefix iff its prefix odd-count \(q_j\) satisfies

\[
q_j\ge a_j\qquad(1\le j\le k).
\]

At depth \(k\), define the endpoint slack

\[
e=q_k-a_k\ge0.
\]

Let \(P_{k,e}\) denote the surviving words with endpoint slack \(e\), and let
\(P_k=\bigcup_{e\ge0}P_{k,e}\).

---

## 1. Boundary-layer lower bound by cyclic rotation

Consider all binary words of length \(k\) with exactly \(a_k\) ones.  For a
word \(w\), define real partial sums

\[
S_j(w)=q_j(w)-\alpha j,\qquad 0\le j\le k.
\]

Since \(\alpha\) is irrational, the values \(S_0,\ldots,S_{k-1}\) are pairwise
distinct.  Also

\[
S_k=a_k-\alpha k>0.
\]

Rotate the word so that it begins immediately after the unique minimum of the
cyclic partial sums.  The standard minimum-rotation / cycle-lemma argument then
gives a rotation whose every prefix satisfies \(S_j>0\), hence the coefficient
barrier.

Every cyclic orbit contains at most \(k\) words.  Therefore

\[
\boxed{
|P_{k,0}|\ge \frac1k\binom{k}{a_k}.
}
\]

This bound is deliberately crude but completely sufficient for a logarithmic
state-space reduction.

---

## 2. Geometric endpoint-slack tail

Ignoring the prefix barrier can only increase the number of words in a fixed
endpoint layer, hence

\[
|P_{k,e}|\le \binom{k}{a_k+e}.
\]

Moreover,

\[
\frac{\binom{k}{a_k+e}}{\binom{k}{a_k}}
=
\prod_{h=1}^e
\frac{k-a_k-h+1}{a_k+h}.
\]

Since \(a_k\ge\alpha k\), each factor is at most

\[
\rho:=\frac{1-\alpha}{\alpha}
=\log_2 3-1
\approx0.584962500721156\ldots.
\]

Thus

\[
\boxed{
\frac{|P_{k,e}|}{|P_k|}
\le k\rho^e.
}
\]

Summing the geometric tail gives

\[
\boxed{
\Pr_{w\in P_k}(E\ge E_0)
\le
\frac{k\rho^{E_0}}{1-\rho}
=
\frac{k(\log_2 3-1)^{E_0}}{2-\log_2 3}.
}
\]

Hence the endpoint slack is rigorously tight on an \(O(\log k)\) scale.

For any fixed \(A>0\), choosing

\[
E_0\ge
\frac{(A+1)\log k+\log((1-\rho)^{-1})}{-\log\rho}
\]

makes the omitted tail at most \(k^{-A}\).

---

## 3. Consequence for weighted Fourier transfer matrices

The exact Fourier transfer for the coefficient-survival language can be written
in slack coordinates rather than odd-count coordinates.  If

\[
\delta_j=a_{j+1}-a_j\in\{0,1\},
\]

then the unweighted transitions are

- if \(\delta_j=0\): \(e\to e\) (even) and \(e\to e+1\) (odd),
- if \(\delta_j=1\): \(e\to e-1\) (even, for \(e\ge1\)) and \(e\to e\)
  (odd).

The odd transition carries the Fourier phase

\[
\omega_{j,q}
=
\exp\!\left(
-\frac{2\pi i t[3^{-q}]_{2^{k-j}}}{2^{k-j}}
\right).
\]

The geometric slack-tail bound implies that, for normalized Fourier sums, a
matrix truncation to \(e<E_0=O(\log k)\) introduces at most \(k^{-A}\) error.
Thus a depth-\(k\) problem has a rigorously controlled logarithmic-width
weighted transfer representation.

Representative conservative cutoffs from the bound:

| depth k | tail <= k^-2 | tail <= k^-4 | tail <= k^-8 |
|---:|---:|---:|---:|
| 114,208,327,604 | 145 | 240 | 429 |
| 217,976,794,617 | 148 | 246 | 440 |
| 10^12 | 157 | 260 | 466 |

These are upper bounds, not empirical widths.  Direct computations at
\(k=1000\) to \(5000\) show much stronger concentration (mean slack about 3.2
and 99.9% below roughly 16), but no theorem is claimed from those observations.

---

## 4. Exact final-step pair cancellation

There is also a deterministic Fourier cancellation at the last lift.

If \(a_{k+1}=a_k\), every surviving depth-\(k\) prefix has both residue lifts
\(r\) and \(r+2^k\) at depth \(k+1\).  Hence every odd Fourier character changes
sign between the two lifts and

\[
\boxed{\widehat\nu_{k+1}(t)=0\quad(t\text{ odd}).}
\]

If \(a_{k+1}=a_k+1\), prefixes with slack \(e\ge1\) still have both lifts and
cancel at odd frequencies; only the boundary layer \(e=0\) contributes.
Therefore the odd-frequency problem is automatically localized to the critical
slack boundary at each threshold-increase step.

This exact cancellation explains several zero / near-zero Fourier values seen in
independent enumeration and weighted-transfer calculations.

---

## 5. Current proof target

The remaining spectral problem is no longer an unbounded-state transfer.
One may seek a theorem for the \(O(\log k)\)-width complex cocycle after
truncation, with the omitted tail controlled by the rigorous geometric bound.

A useful target remains a power-saving or square-root-scale estimate such as

\[
|\widehat\nu_k(t)|\le k^C|P_k|^{-1/2}
\]

on a sufficiently broad frequency range.

Such a Fourier estimate would still need to be connected to the **small
canonical residue** obstruction; low-frequency cancellation alone does not prove
first-crossing exclusion.
