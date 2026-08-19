# Exact selector Fourier 3-orbit product law

Date: 2026-08-20

Status: **exact low-order dyadic Fourier product theorem for the ternary selector measure.** This is not a proof of the Collatz conjecture.

## 1. Selector Fourier coefficient

For

\[
S_m=\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

view the uniform selector measure modulo \(2^K\). Its normalized Fourier coefficient is

\[
\widehat\mu_{m,K}(t)
=
\prod_{i=0}^{m-1}
\frac{1+e^{2\pi i t3^i/2^K}}2.
\]

Hence

\[
\boxed{
|\widehat\mu_{m,K}(t)|
=
\prod_{i=0}^{m-1}
\left|\cos\frac{\pi t3^i}{2^K}\right|.
}
\]

If t has exact additive order \(2^r\), write

\[
t=2^{K-r}a,
\qquad a\text{ odd}.
\]

Then

\[
|\widehat\mu_{m,K}(t)|
=
\prod_{i=0}^{m-1}
\left|\cos\frac{\pi a3^i}{2^r}\right|.
\]

Thus the shell depends only on r and the multiplicative 3-orbit of the odd residue a.

## 2. Multiplicative orbit modulo \(2^r\)

For \(r\ge3\), the element 3 has exact multiplicative order

\[
\boxed{M_r=2^{r-2}}
\]

modulo \(2^r\).

Let

\[
H_r:=\langle3\rangle
\subset(\mathbb Z/2^r\mathbb Z)^\times.
\]

Then

\[
|H_r|=2^{r-2}.
\]

Moreover \(-1\notin H_r\), so

\[
\boxed{
(\mathbb Z/2^r\mathbb Z)^\times
=H_r\sqcup(-H_r).
}
\]

Consequently, for every odd a, the orbit \(aH_r\) is either \(H_r\) or \(-H_r\) up to the same absolute trigonometric values.

## 3. Product over all odd residues

The standard sine product is

\[
\prod_{k=1}^{n-1}\sin\frac{\pi k}{n}
=
\frac{n}{2^{n-1}}.
\]

Take \(n=2^r\). The even-k subproduct is the complete sine product at \(n/2\):

\[
\prod_{\substack{1\le k<n\\k\text{ even}}}
\sin\frac{\pi k}{n}
=
\frac{n/2}{2^{n/2-1}}.
\]

Dividing gives the odd-residue product

\[
\boxed{
\prod_{\substack{1\le k<2^r\\k\text{ odd}}}
\sin\frac{\pi k}{2^r}
=2^{1-2^{r-1}}.
}
\]

Under absolute value, shifting an odd residue by \(2^{r-1}\) converts sine/cosine and permutes the odd residue set, so equivalently

\[
\prod_{k\text{ odd}}
\left|\cos\frac{\pi k}{2^r}\right|
=2^{1-2^{r-1}}.
\]

## 4. Exact one-orbit product

Since the odd units split into \(H_r\) and \(-H_r\), and absolute cosine agrees on h and -h,

\[
\left(
\prod_{h\in H_r}
\left|\cos\frac{\pi h}{2^r}\right|
\right)^2
=2^{1-2^{r-1}}.
\]

Therefore

\[
\boxed{
\prod_{j=0}^{M_r-1}
\left|\cos\frac{\pi a3^j}{2^r}\right|
=2^{-M_r+1/2},
\qquad
M_r=2^{r-2},\ r\ge3,\ a\text{ odd}.
}
\]

This value is independent of the starting odd frequency a.

For r=2 the complete two-step orbit has product 1/2. For r=1 the first selector factor is zero, so that Fourier coefficient vanishes exactly.

## 5. Consequence for m selector digits

Split m into complete multiplicative periods and a remainder:

\[
m=cM_r+b,
\qquad0\le b<M_r.
\]

Every remainder cosine has absolute value at most one, hence for \(r\ge3\)

\[
\boxed{
|\widehat\mu_{m,K}(t)|
\le
2^{-c(M_r-1/2)},
\qquad
c=\left\lfloor\frac{m}{M_r}\right\rfloor.
}
\]

Thus every dyadic shell with \(2^{r-2}\ll m\) is uniformly and deterministically suppressed by the selector measure, without a statistical independence assumption.

This is especially useful for coarse dyadic projections and for renewal windows whose effective unresolved modulus has small exact order relative to the number of still-active ternary selectors.

## 6. What this theorem does not do

When

\[
2^{r-2}>m,
\]

there is no complete multiplicative orbit inside the selector prefix, so the complete-period estimate alone gives no nontrivial bound. Short-orbit segments must then be controlled separately.

This is expected in the current proof geometry: selector activity can directly mix only the dyadic address range comparable to the binary size of the ternary core, roughly

\[
\log_2N=O(m\log_2 3),
\]

whereas the unconditional coefficient-survival extinction horizon is approximately \(20m\). The remaining long tail must therefore use a different mechanism, such as coefficient-boundary renewal/minimal-survivor growth, rather than pretending that fresh selector entropy remains available forever.

## 7. Proof-program role

The theorem gives an exact first component of the corrected Stage 4 decomposition:

\[
\boxed{
\text{selector-active coarse transversality}
+
\text{deterministic coefficient tail}.
}
\]

It should be combined with

- `selector_tv_scaling_certificate.cpp` for finite total-variation calibration;
- `coefficient_projection_collision_certificate.py` for coefficient-language projection energy;
- `ballot_fourier_transfer.py` and `beatty_boundary_fourier_transfer.py` for the dyadic language spectrum;
- `minimal_survivor_bestfirst.cpp` for the post-selector deterministic tail.
