# Coefficient-stopping record-growth criterion for the finite-crossing branch

Date: 2026-08-09

## 1. Coefficient stopping record

For the accelerated Collatz map, define

\[
\tau_c(n)=\min\{k\ge1:3^{q_k(n)}<2^k\},
\]

with \(\tau_c(n)=\infty\) if no such \(k\) exists.

Define the bit-window record

\[
M(B)=\max_{1\le n<2^B}\tau_c(n).
\]

An exact scanner is provided in `collatz/src/coefficient_record_scan.cpp`.

Computed records through B=27 include:

| B | M(B) | record holder |
|---:|---:|---:|
| 4 | 7 | 7 |
| 5 | 59 | 27 |
| 10 | 81 | 703 |
| 14 | 105 | 10087 |
| 16 | 135 | 35655 |
| 19 | 173 | 381727 |
| 20 | 183 | 1027431 |
| 21 | 224 | 1126015 |
| 23 | 246 | 8088063 |
| 24 | 287 | 13421671 |
| 25 | 298 | 26716671 |
| 26 | 376 | 63728127 |
| 27 | 376 | 63728127 |

These are computational observations, not asymptotic evidence strong enough for
an extrapolation.

---

## 2. Why a weak exponential-rate bound would close FCS asymptotically

At a first coefficient crossing of length \(\sigma\) with \(q\) odd entries,
write

\[
\Lambda=\sigma\log2-q\log3>0.
\]

The mechanical-boundary correction estimate used in the project is

\[
S\le \frac{7q+1}{24}.
\]

For a paradoxical first crossing,

\[
x\le\frac{S}{e^\Lambda-1}.
\]

Using the effective Rhin-type bound recorded in the Rozier--Terracol program,

\[
\Lambda\ge\sigma^{-13.3},
\]

and \(e^\Lambda-1\ge\Lambda\), one obtains

\[
x\le C\sigma^{14.3}
\]

for an absolute constant \(C\) (asymptotically one may take a constant larger
than \(7(\log2/\log3)/24\)).

Let

\[
B_\sigma=\left\lceil\log_2(C\sigma^{14.3})\right\rceil.
\]

A first-crossing counterexample at length \(\sigma\) would satisfy
\(x<2^{B_\sigma}\) and \(\tau_c(x)=\sigma\).  Therefore

\[
M(B_\sigma)\ge\sigma.
\]

Since

\[
B_\sigma=14.3\log_2\sigma+O(1),
\]

an unbounded sequence of first-crossing counterexamples would force

\[
\boxed{
\limsup_{B\to\infty}\frac{\log_2M(B)}{B}
\ge \frac1{14.3}
\approx0.06993007.
}
\]

Consequently the strict inequality

\[
\boxed{
\limsup_{B\to\infty}\frac{\log_2M(B)}{B}
<\frac1{14.3}
}
\]

is a sufficient asymptotic theorem for eliminating all sufficiently large FCS
counterexamples.  The remaining bounded range would then be a finite
verification problem.

This criterion is substantially weaker than proving a uniform or polynomial
upper bound for all Collatz stopping times.  It only requires the *record*
coefficient stopping time below \(2^B\) to have exponential rate strictly below
\(2^{B/14.3}\).

---

## 3. Recursively sufficient ternary-Cantor restriction

For Ansari's recursively sufficient limiting set, write a depth-m element as

\[
x=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Let \(M_F(m)\) denote the maximum coefficient stopping time among such elements
through ternary depth \(m\).

A depth-m element obeys \(x\ge4\cdot3^m+3\).  Combining this lower bound with
\(x\le C\sigma^{14.3}\), an unbounded sequence of minimal first-crossing
counterexamples inside the recursively sufficient set would force

\[
\boxed{
\limsup_{m\to\infty}\frac{\log_2 M_F(m)}{m}
\ge\frac{\log_2 3}{14.3}
\approx0.11083654.
}
\]

Thus

\[
\boxed{
\limsup_{m\to\infty}\frac{\log_2 M_F(m)}{m}
<0.11083654\ldots
}
\]

would suffice to close the large first-crossing branch for a minimal
counterexample constrained to the recursively sufficient core.

Small-depth exact scans currently show the ratio decreasing but still far above
this threshold; no asymptotic inference is justified from those data.

---

## 4. Interpretation

The unresolved first-crossing problem can now be stated without reference to an
exponentially large parity-word search:

> How fast can the record coefficient stopping time grow as a function of the
> bit length (or recursively sufficient ternary depth) of the starting integer?

A proof of sufficiently slow record growth would close FCS even if individual
record holders continue to have very large coefficient stopping times.
