# Safe m=44 cross-place cylinder sieve extended through B=20

Date: 2026-08-25

Status: **exact finite root-safe sieve extension, independently reimplemented in C++.** This is not a proof of the Collatz conjecture.

## 1. Independent regression of the existing B=18 result

The existing Python certificate

`collatz/src/m44_cross_place_cylinder_sieve.py`

uses `Q=6`, `BMAX=18`, and `KMAX=36` on the exact ternary Cantor core

\[
N=4\cdot3^{44}+3+4\sum_{i=0}^{43}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

It removes a cross-place cylinder only through one of two root-safe mechanisms:

1. a uniform forward descent `T^B(N)<N`;
2. a positive reverse ancestor `m<N` that merges into the odd endpoint `T^B(N)`.

An independent C++ implementation was written from the affine definitions rather than translated line-for-line. Its first implementation exposed an audit hazard: the reverse affine product

\[
(2^K3^{q_f}-2^B3^{q_r})N
\]

can exceed 128-bit range at the m=44 scale. A naive signed/unsigned 128-bit multiplication produced false reverse exclusions.

The implementation was therefore changed to exact quotient comparisons that decide the same strict affine inequalities without ever forming the large product.

After that correction, the independent C++ result at `BMAX=18` reproduced the Python certificate exactly:

\[
\begin{aligned}
\text{forward excluded}&=14,172,856,036,042,\\
\text{reverse-only excluded}&=2,043,061,564,469,\\
\text{surviving}&=1,376,268,443,905.
\end{aligned}
\]

This independently confirms the existing B=18 aggregate certificate.

## 2. B=19 extension

Keeping `Q=6` and `KMAX=36` fixed while increasing the exact dyadic depth to `BMAX=19` gives

\[
\begin{aligned}
\text{forward excluded}&=14,172,856,036,042,\\
\text{reverse-only excluded}&=2,100,104,303,787,\\
\text{surviving}&=1,319,225,704,587.
\end{aligned}
\]

Thus the nineteenth binary place adds

\[
\boxed{57,042,739,318}
\]

new safe exclusions, all on the reverse side; the forward count is unchanged from B=18.

## 3. B=20 extension

At `BMAX=20` the exact result is

\[
\boxed{
\begin{aligned}
\text{forward excluded}&=14,270,566,604,094,\\
\text{reverse-only excluded}&=2,117,384,829,533,\\
\text{surviving}&=1,204,234,610,789.
\end{aligned}}
\]

The total is still exactly

\[
2^{44}=17,592,186,044,416.
\]

Relative to B=19, the twentieth place removes another

\[
\boxed{114,991,093,798}
\]

starts.

Unlike B=19, B=20 opens both new forward-descent and new reverse-merge certificates:

\[
14,270,566,604,094-14,172,856,036,042
=97,710,568,052
\]

new forward exclusions, and

\[
2,117,384,829,533-2,100,104,303,787
=17,280,525,746
\]

additional reverse-only exclusions after the forward classes have already been removed.

Relative to the old B=18 survivor set, B=20 removes

\[
1,376,268,443,905-1,204,234,610,789
=\boxed{172,033,833,116},
\]

about `12.50002%` of the former survivors.

The surviving fraction of the entire 44-selector core is reduced from

\[
0.07823180362\ldots
\]

at B=18 to

\[
\boxed{0.06845281239\ldots}
\]

at B=20. Equivalently the safe excluded fraction rises from about `92.17682%` to

\[
\boxed{93.15471876\%}.
\]

## 4. Certificate

The new exact certificate is

`collatz/src/m44_cross_place_cylinder_sieve_b20_certificate.cpp`.

It asserts the three B=20 totals above and uses only exact integer arithmetic. OpenMP changes only execution speed, not the arithmetic or partition.

A local optimized run completed with `PASS` after the B=18 regression had first been reproduced exactly.

## 5. Current interpretation

This branch is materially stronger than the marginal root-credit, root-full-max, and reverse23/binary intersections audited earlier:

- those marginal filters were nearly neutral with respect to the other base;
- the cross-place cylinder sieve explicitly combines a ternary residue, a dyadic parity prefix, and a root-level affine inequality in the **same certificate**;
- increasing the binary depth from 18 to 20 continues to create new safe exclusions rather than merely reproducing a stationary ratio.

Therefore the main finite line should now prioritize safe cross-place depth/ternary-resolution extensions, while retaining the previously audited filters as auxiliary intersections.

An attempted B=21 run exceeded the current single-run execution window before producing a certified total. No B=21 number is inferred or recorded.
