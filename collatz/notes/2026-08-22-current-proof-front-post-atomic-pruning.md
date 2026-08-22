# Current proof front after post-atomic pruning

Date: 2026-08-22

Status: **consolidated safe proof-program frontier.** This document separates closed reductions from the remaining divergent-orbit obstruction. It is not a proof of the Collatz conjecture.

## A. Closed structural reductions

The following items are now established inside the corrected branch.

1. Coefficient-surviving trajectories admit the phase-height coordinate

   \[
   h_k=m_k-b_k,
   \qquad b_k=\lceil k\log_3 2\rceil.
   \]

2. The real normalized correction variable

   \[
   v_k=\frac{2^kT^k(N)}{3^{m_k}}
   \]

   is the positive correction product and, for a hypothetical divergent nonperiodic integer orbit, has a finite positive limit after using the Garcia--Tal orbit-sparsity estimate.

3. Consequently

   \[
   T^k(N)\asymp_N 3^{h_k}
   \]

   and every infinite coefficient-surviving nonperiodic orbit satisfies

   \[
   h_k\to+\infty.
   \]

4. Cutting at first record heights gives exact record first-passage macros in a Beatty strip.

5. Any strict record-height gain macro has nonnegative normalized syndrome penalty-minus-rebate.

6. Record first-passage words of finite strip width have an explicit entropy gap of order `1/(r+1)^2`.

7. Fourier coefficients of a record language reduce exactly to one dyadic critical-bit completion gradient.

8. Shannon/Pinsker recentering at `alpha=log_3 2` converts failure of Fourier cancellation into relative-entropy cost.

9. Long and intermediate record excursions with `L_r -> infinity` have sublinear information cost per bit and therefore near-`|2alpha-1|` contraction on almost all dyadic valuation levels.

10. If record lengths are eventually bounded by `M`, then

    \[
    h_k\ge k/M-O_M(1),
    \qquad
    \liminf m_k/k\ge\alpha+1/M,
    \]

    giving the strengthened entropy deficit

    \[
    \eta_M=1-H_2(\alpha+1/M)>\eta_{\rm coeff}.
    \]

11. Singleton record macros have length at most four and an infinite singleton-only tail is impossible.

12. Every non-singleton bounded record has terminal mechanical tail `1010` or `10110` and carries a fresh Haar shell. For fixed `M`,

    \[
    |\widehat\mu_{\rm rec}(t)|\le\kappa_M<1.
    \]

13. `M<=3` is completely excluded.

14. Eventually periodic high-density parity/odd-gap tails are excluded.

15. Consecutive singleton stretches beginning near record height `r` have length `O_N(r)`, so non-singleton fresh shells occur at least logarithmically often in record height.

## B. Exact bulk/tail boundary for the selector

For the ternary selector of size parameter `m`, once

\[
2^r>\frac{3^m-1}{2},
\]

the dyadic projection is atomic:

\[
p_r=e_r=2^{-m},
\qquad
\|\Delta_rg_m\|_2^2=2^{r-m}.
\]

Therefore the proof architecture must be split exactly into

\[
\boxed{
\text{pre-atomic Haar/Fourier bulk}
\longrightarrow
\text{post-atomic ordinary-integer arithmetic tail}.
}
\]

A pure lifetime-Haar-energy contradiction cannot close the post-atomic side.

## C. Literature-aligned location of the remaining bounded-record case

Monks--Yazinski prove that a divergent rational 2-adic orbit must have parity-one lower density at least `alpha`, and that the Collatz autoconjugacy `Omega` complements parity and preserves divergence.

A hypothetical bounded-record divergent positive integer has lower parity density at least `alpha+1/M`. Its autoconjugate therefore has complementary upper density below `alpha`, so `Omega(N)` cannot be rational.

Thus the remaining bounded-record branch necessarily lies in the irrational-autoconjugacy side of the classical divergent-orbit obstruction.

This confirms that no standard rational-density theorem has been omitted.

## D. Remaining cases

The current proof front can be stated as two arithmetic tails.

### D1. Unbounded record lengths

Record-side Fourier cancellation is available on almost all dyadic levels of sufficiently long excursions, but a complete same-integer selector/Hensel transversality theorem has not yet been proved on the exceptional levels and across post-atomic ordinary starts.

### D2. Eventually bounded record lengths

After all reductions, a remaining candidate must satisfy all of the following:

- some fixed `M>=4` bounds all sufficiently late record lengths;
- the parity lower density is at least `alpha+1/M`;
- the tail is genuinely aperiodic;
- non-singleton records occur infinitely often and at least logarithmically often in record height;
- each non-singleton carries a fresh terminal Haar contraction;
- the selector is eventually atomic;
- the ordinary start is a fixed positive integer;
- its autoconjugate is an irrational 2-adic integer.

The missing theorem is therefore:

> **Post-atomic ordinary-integer transversality theorem.** Exclude a fixed positive integer whose parity vector follows either of the reduced record-tail regimes while satisfying the exact 2-adic/3-adic parity-series and Hensel compatibility conditions indefinitely.

This is the current narrowest safe statement of the unresolved global bridge.

## E. Proof-status warning

The reductions above are substantial, but the last theorem is still a divergent-orbit theorem for a highly structured subclass. Until it is proved, the Collatz conjecture has not been proved by this program.
