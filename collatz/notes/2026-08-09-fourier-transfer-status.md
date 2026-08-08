# Collatz first-crossing Fourier-transfer status — 2026-08-09

## Scope

This note concerns the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The target is the finite-coefficient-crossing branch of a proof attempt.  Nothing
below proves the Collatz conjecture or Terras' coefficient-stopping conjecture.
The purpose is to isolate exact algebraic reductions and computationally test a
spectral-cancellation theorem candidate.

---

## 1. Ternary Cantor / Ansari coordinate

For the recursively sufficient core used in the accompanying investigation,
write

\[
x=4y+3,\qquad
 y=3^m+\sum_{i=0}^{m-1}a_i3^i,\qquad a_i\in\{0,1\}.
\]

Modulo \(2^r\), the uniform digit measure on these subset sums has normalized
Fourier transform

\[
\widehat\mu_{m,r}(t)
=e^{2\pi i t3^m/2^r}
\prod_{i=0}^{m-1}
\frac{1+e^{2\pi i t3^i/2^r}}2,
\]
so

\[
\bigl|\widehat\mu_{m,r}(t)\bigr|
=
\prod_{i=0}^{m-1}
\left|\cos\frac{\pi t3^i}{2^r}\right|.
\]

This is a finite Riesz product.

---

## 2. Full-orbit Riesz attenuation identity

Let \(t=2^s u\), with \(u\) odd, and put \(R=r-s\ge3\).  Since

\[
\operatorname{ord}_{2^R}(3)=2^{R-2}=:L,
\]

the powers \(3^i\) run through one of the two cosets of the cyclic subgroup
\(\langle3\rangle\) in the odd units modulo \(2^R\).  Multiplication by an odd
\(u\) merely changes the coset, while absolute cosine values are unchanged by
negation.  Consequently

\[
\boxed{
\prod_{i=0}^{L-1}
\left|\cos\frac{\pi u3^i}{2^R}\right|
=2^{-L+1/2}.
}
\]

Proof sketch: the square of the left side is the product over all odd residues
modulo \(2^R\).  Using the standard odd-angle sine product,

\[
\prod_{h\text{ odd }(2^R)}
\left|\cos\frac{\pi h}{2^R}\right|
=2^{-2^{R-1}+1},
\]

and taking the positive square root gives the result.

Hence, if \(m=aL+b\), \(0\le b<L\), then

\[
\boxed{
|\widehat\mu_{m,r}(t)|
\le 2^{-a(L-1/2)}.
}
\]

Thus frequencies with large \(2\)-adic valuation are strongly attenuated after
complete powers-of-3 orbits.  Low-valuation frequencies can remain large and
require a second mechanism.

---

## 3. Exact weighted transfer for the coefficient-survival language

For a length-\(k\) parity word, let \(q_j\) denote its number of odd entries
through position \(j\).  Survival of coefficient contraction through all \(k\)
steps is exactly

\[
3^{q_j}\ge2^{j+1}\qquad(0\le j<k).
\]

If the positions of the odd entries are \(d_0<\cdots<d_{q-1}\), the canonical
starting residue is

\[
r(w)\equiv
-\sum_{\ell=0}^{q-1}2^{d_\ell}3^{-(\ell+1)}
\pmod{2^k}.
\]

Therefore a Fourier character of frequency \(t\) factors along odd transitions.
Let \(v_j(q)\) be the complex character sum over admissible prefixes of length
\(j\) with \(q\) odd entries.  The transfer is lower-bidiagonal:

\[
v_{j+1}(q)
=
\mathbf 1_{3^q\ge2^{j+1}}v_j(q)
+
\mathbf 1_{3^q\ge2^{j+1}}
\omega_{j,q}\,v_j(q-1),
\]

with

\[
\omega_{j,q}
=
\exp\!\left(
-\frac{2\pi i\,t\,[3^{-q}]_{2^{k-j}}}{2^{k-j}}
\right).
\]

The unweighted count obeys the same transfer with \(\omega_{j,q}=1\).  Hence a
fixed-frequency Fourier coefficient can be computed in polynomial time in \(k\)
without enumerating the exponentially many parity words.

Implementation: `collatz/src/ballot_fourier_transfer.py`.

---

## 4. Computational observation: low-frequency square-root scale

Independent enumeration for small \(k\) and the weighted transfer agree exactly.
Wolfram checks for \(t=1,3,5\) give representative normalized magnitudes:

- \(k=20\): worst of these three \(\approx4.14\times10^{-3}\),
- \(k=40\): \(\approx3.78\times10^{-6}\),
- \(k=50\): \(\approx1.56\times10^{-7}\),
- \(k=75\): \(\approx2.84\times10^{-11}\),
- \(k=100\): \(\approx7.86\times10^{-15}\).

A wider fixed odd-frequency scan through 63 (separate exact-threshold transfer
calculation) is broadly consistent with

\[
|\widehat\nu_k(t)|\approx2^{-c k},
\qquad c\text{ near }0.47\text{--}0.50
\]

away from exceptional exact/near cancellations.

The coefficient-survival language has exponential count rate expected to tend to

\[
H_2(\alpha),\qquad
\alpha=\frac{\log2}{\log3},
\]

where

\[
H_2(\alpha)\approx0.9499555272,
\qquad
\frac12H_2(\alpha)\approx0.4749777636.
\]

Thus the observed low-frequency Fourier magnitude is close to the generic
square-root scale \(|P_k|^{-1/2}\).  Parseval explains why square-root size is a
natural *typical-frequency* benchmark; the unproved content would be to show
that the specific low frequencies needed for discrepancy estimates are not
exceptional.

---

## 5. Current theorem candidate

### Ballot Fourier Cancellation (BFC) — unproved

For each fixed nonzero odd frequency \(t\), or for a controlled growing frequency
window, prove a bound of the form

\[
\boxed{
|\widehat\nu_k(t)|
\le k^C |P_k|^{-1/2}
}
\]

or more generally

\[
|\widehat\nu_k(t)|\le 2^{-c k}
\]

with explicit \(c>0\) uniform over the frequency range needed downstream.

A fixed-frequency result alone does **not** prove first-crossing exclusion.  The
actual obstruction is the existence of a very small canonical residue among
full depth-\(\sigma\) coefficient-surviving words.  A useful theorem must
ultimately control a sufficiently broad frequency range or directly control
small-residue discrepancy / canonical-lift stabilization.

---

## 6. Important negative result / scope correction

The ternary Cantor Riesz product is not uniformly Fourier-small: when
\(m\asymp(\log_3 2)r\), low frequencies such as \(t=1,3,5\) can retain large
coefficients.  Therefore the Cantor side alone cannot yield equidistribution.
The relevant possibility is *spectral complementarity*: high-valuation
frequencies are suppressed by the exact Riesz full-orbit identity, while low
frequencies appear numerically suppressed by the coefficient-survival transfer.
The middle-frequency region is still unresolved.

---

## 7. Relation to the actual FCS target

A hypothetical first-crossing counterexample has a polynomial upper bound
\(x<2^B\) with \(B=O(\log\sigma)\), while its full parity prefix has length
\(\sigma\).  Thus the real target is not the intersection of two length-\(B\)
cores.  It is the existence of a length-\(\sigma\) coefficient-surviving residue
inside the tiny interval \([1,2^B)\), possibly also constrained to the recursively
sufficient ternary-Cantor core.

Equivalently, the remaining finite-crossing obstruction can be phrased as a
**small-residue discrepancy / non-stabilization problem** for the weighted
ballot transfer.

This is the point at which the current Fourier/matrix program meets the earlier
2-adic canonical-lift formulation.
