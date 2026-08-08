# Minimal-survivor growth target

Date: 2026-08-09

## 1. Definition

For the accelerated Collatz coefficient stopping time

\[
\tau_c(n)=\min\{k\ge1:3^{q_k(n)}<2^k\},
\]

define the inverse record function

\[
\boxed{
\mu(k)=\min\{n\ge1:\tau_c(n)>k\}.
}
\]

If some positive integer has infinite coefficient stopping time, then \(\mu(k)\)
is bounded for all sufficiently large \(k\).  Thus any theorem forcing
\(\mu(k)\to\infty\) already rules out the infinite coefficient-survival branch.

The function \(\mu\) is the generalized inverse of the bit-window record
\(M(B)=\max_{n<2^B}\tau_c(n)\):

\[
M(B)>k\iff \mu(k)<2^B.
\]

---

## 2. First-crossing upper bound

At a first coefficient crossing of length \(\sigma\), the project uses the
mechanical-boundary correction estimate

\[
S\le\frac{7q+1}{24}=O(\sigma).
\]

A paradoxical first crossing satisfies

\[
x\le\frac{S}{e^\Lambda-1},
\qquad
\Lambda=\sigma\log2-q\log3>0.
\]

Rozier--Terracol quote Rhin's effective linear-form estimate

\[
|\Lambda|\ge \sigma^{-13.3}
\]

for all relevant \(\sigma\ge2\), and the stronger asymptotic estimate

\[
|\Lambda|\ge\sigma^{-7.616}
\]

for \(\sigma\ge H_0\), where \(H_0\) is effectively computable.
Consequently, for sufficiently large \(\sigma\),

\[
\boxed{x=O(\sigma^{8.616}).}
\]

(For explicit finite calculations before an explicit value of \(H_0\) is
inserted, continue to use the unconditional-all-H exponent 13.3 and the
corresponding \(O(\sigma^{14.3})\) bound.)

---

## 3. Single growth target that attacks both proof branches

Suppose one proves an eventual lower bound stronger than the first-crossing
upper scale, for example

\[
\boxed{
\liminf_{k\to\infty}
\frac{\log\mu(k)}{\log k}>8.616.
}
\]

Then:

1. an integer with \(\tau_c(n)=\infty\) is impossible, because it would keep
   \(\mu(k)\le n\) for all k;
2. a sufficiently large paradoxical first coefficient crossing is impossible,
   because its starting integer would simultaneously satisfy
   \(x\ge\mu(\sigma-1)\) and \(x=O(\sigma^{8.616})\).

After a finite verification of the remaining bounded range, this would close
both the finite-crossing and infinite-coefficient-survival branches of the
current proof decomposition.

Equivalently, in terms of the record function M(B), it suffices to prove

\[
\boxed{
\limsup_{B\to\infty}
\frac{\log_2M(B)}{B}<\frac1{8.616}
\approx0.1160631383.
}
\]

---

## 4. Recursively sufficient ternary-Cantor version

For the limiting recursively sufficient core

\[
x=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

let \(M_F(m)\) denote the coefficient-stopping record through ternary depth m.
Since such a depth-m integer is at least \(4\cdot3^m+3\), the analogous
sufficient asymptotic condition is

\[
\boxed{
\limsup_{m\to\infty}
\frac{\log_2M_F(m)}{m}
<\frac{\log_2 3}{8.616}
\approx0.1839557220.
}
\]

Again, this is a sufficient target, not a theorem currently proved.

---

## 5. Exact small scans

For all positive integers, exact scans give selected records

\[
(B,M(B))=(16,135),(19,173),(20,183),(21,224),(24,287),(26,376).
\]

Thus \(M(26)/26\approx14.46\).  On the recursively sufficient ternary core,
exact scans through m=22 give \(M_F(22)=317\).

These finite data are compatible with much slower than exponential record
growth, but they are far too small to justify an asymptotic claim.

A purely heuristic model based on the exact survivor-language entropy
\(H_2(\log_3 2)\) would predict

\[
M(B)\asymp\frac{B}{1-H_2(\log_3 2)}
\approx19.98 B,
\]

provided canonical survivor residues were sufficiently equidistributed.  No
such equidistribution theorem is currently established here, so this is only a
scale comparison.
