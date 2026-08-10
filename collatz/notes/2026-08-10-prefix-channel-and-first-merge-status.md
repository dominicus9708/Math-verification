# Prefix-channel interval scan and corrected first-merge status

Date: 2026-08-10

Status: **exact finite computation + corrected structural diagnostics**. This is not a proof of the Collatz conjecture or of coefficient/classical stopping-time equality.

## 1. Prefix-channel interval decomposition

For a depth-B coefficient-surviving canonical state

\[
(r,q,y),\qquad y=T^B(r),
\]

every integer in the same residue cylinder has the form

\[
n=r+m2^B
\]

and satisfies exactly

\[
\boxed{T^B(n)=y+3^q m.}
\]

This gives the exact prefix-channel interval scanner

`collatz/src/prefix_channel_interval_scan.cpp`.

The scanner was cross-checked against the known exact value

\[
\mu(447)=12,235,060,455,
\]

which it reproduces exactly.

Using the prefix-channel scanner, the previously continuous exact scan for depth 547 was extended through

\[
[156,235,060,456,400,000,000,000).
\]

The new runs tested 3,373,594,268 prefix-channel candidates with zero detected 128-bit overflows and no depth-547 survivor. Combined with the previous continuous scan,

\[
\boxed{\mu(547)\ge400,000,000,000.}
\]

No extrapolation is made beyond the scanned interval.

## 2. Correction to the earlier first-merge diagnostic

The first version of `endpoint_first_merge_diagnostics.cpp` compared the unlifted depth-(k-1) parent endpoints. That is not the correct predecessor of a depth-k canonical child when the child uses the lift by 2^(k-1).

If the parent state is (r,y,q) and the child lift bit is c, the actual time-(k-1) value of that child is

\[
\boxed{\widetilde y=y+c3^q.}
\]

Therefore a true first merge must compare these lifted predecessors. The code has been corrected.

Consequently, the earlier figures

- 2,760,811 cumulative new merge pairs through depth 32;
- the associated q-difference distribution and first-merge order statistics

were based on an overinclusive first-merge test and are **superseded**. They must not be used as evidence.

The prefix-channel scan and the bound on mu(547) are unaffected by this correction because they do not use endpoint first-merge classification.

## 3. Corrected Delta-q=1 system

The corrected algebra and finite diagnostics are maintained separately in

`collatz/notes/2026-08-10-deltaq1-true-first-merge-system.md`.

Using the true lifted-predecessor definition, exact enumeration through depth 28 gives:

- true first-merge pairs: 805;
- equal-q true first merges: 0;
- Delta q=1: 507;
- Delta q=2: 276;
- Delta q=3: 22;
- correction-order failures: 0;
- start-order failures: 0.

For Delta q=1, defining

\[
G=r_L-3r_H=\frac{R_H-R_L}{3^{q_L}},
\]

the observed gap distribution through depth 28 is

\[
G=2\quad(504\text{ cases}),
\qquad
G=6\quad(3\text{ cases}).
\]

These are corrected finite computations, not a theorem.

## 4. Current structural target

For a coefficient-surviving true first merge with

\[
q_H=q_L+1,
\]

prove

\[
\boxed{G=r_L-3r_H>0.}
\]

This is equivalent to

\[
R_H>R_L.
\]

The refined note also derives an exact two-channel affine transition and a backward 3-adic carry formulation in which the target becomes the sign of one terminal carry.
