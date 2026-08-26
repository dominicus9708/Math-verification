# Terminal Hensel controllability audit and corrected min-plus target

Date: 2026-08-26

Status: **exact local arithmetic audit + proof-target correction.** This note corrects the overly strong sign-only correlation target from the previous first-resonance reduction. It does not prove the Collatz conjecture.

## 1. Zero-target Hensel state

Write the current higher ternary carry as a 3-adic integer `K`.  If the next earlier mechanical exponent is

\[
e=B-A,
\]

and a new displacement \(d\ge0\) is chosen, then a one-digit Hensel lift has

\[
\boxed{
K' = \frac{K+2^{e-d}}{3}
}
\]

provided

\[
K+2^{e-d}\equiv0\pmod3.
\]

For a fixed current carry \(K\bmod3\), this congruence fixes exactly one parity class of \(d\).

## 2. Three-class controllability modulo 9

Fix the required parity and consider three consecutive representatives

\[
d,\qquad d+2,\qquad d+4.
\]

Modulo 9,

\[
2^{-2}\equiv7\pmod9,
\]

and the three same-parity powers exhaust the three units in one fixed residue class modulo 3:

\[
\{1,4,7\}
\quad\text{or}\quad
\{2,5,8\}.
\]

Because the divisibility condition already makes

\[
K+2^{e-d}\equiv0\pmod3,
\]

dividing the three possible sums by 3 yields all three next carry digits:

\[
\boxed{
K'\bmod3\in\{0,1,2\}
}
\]

exactly once each.

Thus, after the current required parity is fixed:

- one of the three same-parity classes kills the Hensel chain (`next carry = 0`);
- one produces next carry 1;
- one produces next carry 2.

This statement is independent of the first-resonance numerical constants.

## 3. Ordering memory

Let \(p\) be the previous earliest displacement and let

\[
g\in\{1,2\}
\]

be the new mechanical gap.  Strict ordering of odd positions gives

\[
\boxed{
d\ge p-g+1.}
\]

After truncation at zero, define

\[
L=\max\{0,p-g+1\}.
\]

Let \(d_0\) be the smallest integer at least \(L\) in the currently required parity class.  Then:

- some live child always exists with \(d\le d_0+2\);
- either prescribed nonzero next carry can be realized with \(d\le d_0+4\).

So the Hensel sign sequence has substantial local controllability.  It is **not** an externally fixed pseudorandom sign sequence.

## 4. Correction to the previous correlation target

The previous note identified the sufficient condition

\[
\sum c_j\mathbf 1_{\{\varepsilon_j\ne\sigma_j\}}
\ge \frac12\sum c_j
\]

for closing the first resonance.

That condition remains sufficient, but the intended route

> prove that Hensel signs cannot correlate with mechanical signs

is not justified as a standalone theorem.  The three-class lemma shows that displacement choices can steer the next Hensel carry/sign.

Therefore the correct unresolved object is not a correlation of two externally fixed sign sequences.

It is a **controlled weighted path**.

## 5. Exact control cost

For a displacement \(d\), the normalized real correction charge at odd ordinal \(j\) is

\[
\boxed{
\kappa_j(d)
=
\frac{2^{b_j}-2^{b_j-d}}{3^j}
=
2c_j(1-2^{-d}),
}
\]

where

\[
c_j=\frac{2^{b_j-1}}{3^j}.
\]

The proof problem must retain simultaneously:

1. current 3-adic Hensel carry;
2. previous displacement through the one-sided ordering memory;
3. the mechanical gap \(g\in\{1,2\}\);
4. real correction cost \(\kappa_j(d)\);
5. terminal endpoint boundary;
6. initial dyadic formation boundary.

## 6. Correct Bellman/min-plus formulation

A proof-level finite-horizon value function has the schematic form

\[
\boxed{
V_m(K,p)=
\min_d
\left\{
\kappa_m(d)
+
V_{m+1}\!\left(
\frac{K+2^{e_m-d}}3,
 d
\right)
\right\},
}
\]

where the minimization is only over \(d\) satisfying

\[
\begin{aligned}
&d\ge\max\{0,p-g_m+1\},\\
&K+2^{e_m-d}\equiv0\pmod3,\\
&\frac{K+2^{e_m-d}}3\not\equiv0\pmod3
\quad\text{when further continuation is required.}
\end{aligned}
\]

The first-resonance contradiction target is

\[
\boxed{
V_{\rm two-boundary}>4{,}314{,}000{,}000.
}
\]

The key word is **two-boundary**.  If one drops the endpoint/start boundary and allows an arbitrary Hensel state, the mechanical path \(d=0\) can survive an arbitrarily long finite local block for a suitably chosen state.  Hence no positive local block-cost theorem can be valid uniformly over arbitrary boundary states.

## 7. DSD audit interpretation

The DSD chain has prevented a false final reduction.

The earlier descriptor chain was

\[
\text{Hensel carry}
\to
\text{required sign}
\to
\text{sign correlation}.
\]

The local controllability audit shows that the last arrow loses essential state information.  The repaired chain is

\[
\boxed{
\text{Hensel carry}
+\text{ordering memory}
+\text{boundary state}
\to
\text{allowed control }d
\to
\text{real defect cost}.
}
\]

This is precisely the kind of domain/state loss that DSD bookkeeping is intended to expose.

## 8. Next target

The preferred route is now:

1. construct the exact two-boundary min-plus transfer for a mechanical block;
2. exploit that the first-resonance gap word is a rational Christoffel word with continued-fraction recursion;
3. compose block transfer operators through the Euclidean/continued-fraction decomposition rather than iterating \(Q\approx7.2\times10^{10}\) positions;
4. seek a Bellman dual/potential certificate proving the minimum full-bridge defect exceeds the existing budget.

The terminal low-support ladder remains a useful regression suite for the block operator, but it is no longer the intended asymptotic engine.

Companion certificate:

`collatz/src/terminal_hensel_three_class_controllability_certificate.py`.
