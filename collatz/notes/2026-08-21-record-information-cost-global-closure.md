# Record-side information-cost closure for all unbounded record lengths

Date: 2026-08-21

Status: **record-side analytic closure.** Combining the short-record ballot lower bound with the long-record loop lower bound proves vanishing critical information cost per bit whenever both record height and record length diverge. The final selector/Hensel splice and bounded-length record tail remain open. This is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2
\]

and let \(\mathcal R_{s,r}(L)\) be a nonempty record first-passage language at record height \(r\), mechanical phase \(s\), and record length \(L\). Define its critical Bernoulli information cost

\[
K_\alpha(\mathcal R)
=-\ln P_\alpha(\mathcal R).
\]

The two companion theorems give complementary estimates.

## 1. Short-record theorem

For every fixed finite \(A\), there are constants such that, uniformly in phase,

\[
L\le Ar
\]

implies

\[
P_\alpha(\mathcal R_{s,r}(L))
\ge c_A L^{-3/2}
\]

for all sufficiently large \(r,L\). Hence

\[
\boxed{
K_\alpha(\mathcal R)
\le\frac32\ln L+O_A(1).
}
\]

In particular

\[
\sup_{r\ge R,\ M\le L\le Ar}
\frac{K_\alpha}{L}
\longrightarrow0
\]

as \(M\to\infty\), after \(R\) is large enough for the theorem.

## 2. Long-record loop theorem

The strengthened \(r^2\)-bridge construction gives constants depending only on \(\alpha\) such that

\[
\boxed{
K_\alpha(\mathcal R)
\le
C_\alpha
\left[
r+
\left(\frac{L}{r^2}+1\right)\ln r
\right].
}
\]

Therefore, on the complementary region

\[
L>Ar,
\]

we have

\[
\frac{K_\alpha}{L}
\le
\frac{C_\alpha}{A}
+
C_\alpha\frac{\ln r}{r^2}
+
C_\alpha\frac{\ln r}{L}.
\]

For fixed \(A\), the last two terms vanish uniformly as \(r\to\infty\).

## 3. Two-parameter closure

Fix \(\varepsilon>0\).

First choose \(A\) so large that

\[
C_\alpha/A<\varepsilon/3.
\]

Then choose \(R\) so large that the two residual long-record terms are each below \(\varepsilon/3\) for every \(r\ge R\). Finally choose \(M\) so large that the short-record bound satisfies

\[
\frac{(3/2)\ln L+O_A(1)}{L}<\varepsilon
\qquad(L\ge M).
\]

Thus

\[
\boxed{
\lim_{R,M\to\infty}
\sup_{\substack{
r\ge R,\ L\ge M,\\
\mathcal R_{s,r}(L)\ne\varnothing
}}
\frac{K_\alpha(\mathcal R_{s,r}(L))}{L}
=0.
}
\]

The convergence is uniform in the mechanical phase \(s\).

Equivalently, for every sequence of nonempty record excursions with

\[
r_n\to\infty,
\qquad
L_n\to\infty,
\]

we have

\[
\boxed{
K_\alpha(\mathcal R_n)=o(L_n).
}
\]

## 4. Fourier consequence

The entropy-Haar theorem gives, for every fixed \(\eta>0\),

\[
\#\left\{j:
\sup_{v_2(t)=L-j-1}
|\widehat\mu_{\mathcal R}(t)|
>\delta_\alpha+\eta
\right\}
\le
\frac{2K_\alpha(\mathcal R)}{\eta^2},
\]

where

\[
\delta_\alpha=|2\alpha-1|
\approx0.2618595071.
\]

Hence whenever \(r,L\to\infty\),

\[
\boxed{
\frac{\#\mathrm{Bad}_\eta}{L}\to0.
}
\]

Thus asymptotically almost every dyadic valuation level in every large record excursion has uniform record-side Fourier contraction

\[
|\widehat\mu(t)|\le\delta_\alpha+\eta<1
\]

for any fixed \(\eta<1-\delta_\alpha\).

## 5. Exact remaining tail

The Garcia--Tal height-escape theorem already forces

\[
r\to\infty
\]

along any hypothetical infinite nonperiodic coefficient-surviving orbit.

Therefore, after the present result, the record-side obstruction can persist only on record excursions whose lengths do **not** tend to infinity.

More quantitatively: for every cutoff \(M\), all sufficiently high records with

\[
L\ge M
\]

are Fourier-regular except for an arbitrarily small fraction of dyadic levels once \(M\) is chosen large. The unresolved component is the bounded-length family

\[
\boxed{L<M,}
\]

a finite macro alphabet at every fixed cutoff.

This is the next deterministic/Hensel target.

Inputs:

- `2026-08-21-short-record-ballot-lower-bound.md`;
- `2026-08-21-long-record-loop-lower-bound-and-coarse-fourier.md`;
- `2026-08-21-record-strip-logconcavity-and-entropy-haar-dichotomy.md`.
