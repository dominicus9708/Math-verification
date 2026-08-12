# R2 terminal checkpoint: coefficient survivor as a Beatty-driven 2-adic naturalness problem

Date: 2026-08-12

Status: **proof-architecture consolidation**. No Collatz proof is claimed.

## 1. R2 is exactly an infinite coefficient-survivor problem

Choose a sufficiently late renewal floor `N` in branch R2. By definition,

\[
\boxed{\tau_c(N)=\infty.}
\]

For every accelerated prefix,

\[
3^{q_k}>2^k.
\]

The affine prefix formula is

\[
T^k(N)=\frac{3^{q_k}N+R_k}{2^k},
\qquad R_k\ge0.
\]

Hence

\[
T^k(N)>N
\]

for every positive prefix length. Thus coefficient survival automatically implies no first descent from `N`.

Therefore eliminating R2 is equivalent to proving that no positive ordinary integer has infinite coefficient stopping time.

In frontier language this is the infinite version of

\[
\mu(K):=\min\{n:\tau_c(n)>K\}:
\]

\[
\boxed{\text{R2 exclusion}\iff\mu(K)\to\infty.}
\]

The present work adds stronger structural necessary conditions to the raw coefficient-survivor tree.

## 2. Exact critical Beatty skew product

Let

\[
\gamma=\log_2 3,
\qquad
r_i=\lfloor(i+1)\gamma\rfloor-\lfloor i\gamma\rfloor\in\{1,2\}.
\]

An R2 valuation tail is exactly one nonnegative integer path satisfying

\[
\boxed{s_0=0,}
\]

\[
\boxed{0\le s_{i+1}\le s_i+r_i-1.}
\]

The valuations are recovered by

\[
\boxed{v_i=s_i+r_i-s_{i+1}.}
\]

Every finite admissible `s` prefix is locally realizable by one dyadic residue class. Thus no further finite local filter can prove R2 exclusion.

## 3. Harmonic survivor conditions

For a nonperiodic positive-integer survivor,

\[
\boxed{
\sum_{i<q}2^{-s_i}=O_N(q^{1/9}).
}
\]

Consequently

\[
\boxed{
\sum_{i<q}s_i
\ge
\frac89q\log_2q-O_N(q).
}
\]

and for each `theta<8/9`, displacement below `theta log_2 q` occurs with density zero.

At the same time the rational-2-adic critical-density boundary requires compatibility with

\[
\boxed{\liminf s_i/i=0.}
\]

Thus R2 requires a path with large average displacement area but recurrent sublinear height.

## 4. Economical renewal excursions

For an R2 renewal segment with `H` odd events and `A` accelerated steps, define

\[
s_H^{(j)}=\lfloor H\gamma\rfloor-A\ge0.
\]

If `s_H^{(j)}>=1`, the segment coefficient surplus exceeds one bit and

\[
\boxed{N_{j+1}>2N_j.}
\]

Therefore every non-doubling R2 renewal segment has

\[
\boxed{A=\lfloor H\gamma\rfloor}
\]

and is a finite critical Beatty excursion

\[
\boxed{s_0=0,\quad s_k\ge0,\quad s_H=0.}
\]

The global displacement evaluated at renewal floors is nondecreasing.

## 5. Lower-layer tri-place defect

For one economical excursion, the actual and critical-reference words have the same aggregate counts `(A,H)`. Define

\[
\xi=c_*-c\ge0.
\]

The same defect gives:

\[
\boxed{\text{2-adic formation shift}:\quad +\xi,}
\]

\[
\boxed{\text{gap-residue shift}:\quad -\xi.}
\]

The real affine shadow, however, is negative because the aggregate coefficient is greater than one:

\[
C=-\frac{ac}{a-1}<0.
\]

The local renewal-compatible starts for a fixed lower-layer word form an unbounded arithmetic progression above a finite threshold, not a bounded interval. This is the fundamental sign asymmetry with R1.

Therefore no fixed-word residue-window separation can eliminate R2.

## 6. Exact 2-adic naturalness map

The infinite path determines

\[
\boxed{
\Phi(s)
=-\sum_{i=0}^{\infty}
\frac{2^{\lfloor i\gamma\rfloor-s_i}}{3^{i+1}}
\in\mathbb Z_2.
}
\]

R2 survives in the ordinary positive integers iff an admissible path satisfying the harmonic/critical conditions has

\[
\boxed{\Phi(s)=N\in\mathbb N_{>1}.}
\]

This is the remaining global arithmetic condition.

## 7. Final R2 theorem target

### Critical Beatty Skew Naturalness Exclusion

Prove there is no infinite integer sequence `s_i` satisfying simultaneously

\[
s_0=0,
\]

\[
0\le s_{i+1}\le s_i+r_i-1,
\]

\[
\sum_{i<q}2^{-s_i}=O(q^{1/9}),
\]

\[
\liminf s_i/i=0,
\]

and

\[
\Phi(s)\in\mathbb N_{>1}.
\]

This theorem is exactly sufficient to eliminate R2.

## 8. What will not close R2 by itself

The following are now known to be insufficient on their own:

- finite parity/valuation prefix exclusion, because every finite admissible skew prefix is realizable;
- Haar/measure-zero contraction, because an individual ordinary integer is already a measure-zero point;
- parity-density equality alone, because abstract sublinear unbounded skew paths exist;
- a one-word rational-shadow window, because the lower-layer fixed point is negative and local candidate starts remain unbounded;
- standard p-adic approximation bounds at exponent one, which do not yield a contradiction at the critical scale.

The missing result must use the infinite naturalness condition or a genuinely transported arithmetic invariant across arbitrarily many critical excursions.