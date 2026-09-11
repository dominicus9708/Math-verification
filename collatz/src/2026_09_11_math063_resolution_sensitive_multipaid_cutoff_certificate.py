#!/usr/bin/env python3
"""
MATH-063 exact resolution-sensitive multi-paid cutoff certificate.

MATH-061 proves that an exact macro cylinder of total shortcut length H has
source congruence modulus 2^H, while every audited pre-first-cell u=0 anchor is
strictly below 2^73.  Hence any cylinder containing at least two ordinary
source anchors must satisfy H<=72.

MATH-062 proves for a paid cluster with r paid odd events
    P_cluster >= (1/6) * sum_{j<r} Omega_j,
where the Omega_j are r consecutive iterates of the exact phase map.

This certificate combines those two facts.  It minimizes the exact consecutive
phase sum and compares it to lambda*72, lambda=19/503.  The first paid count
for which every multi-source cylinder is automatically nonnegative is r=24.
Thus only 2<=r<=23 require detailed symbolic multi-paid Bellman treatment.

Singleton cylinders are NOT closed by this theorem; they are handed to the
same-integer direct track.  Collatz and first-cell emptiness remain open.
"""
from fractions import Fraction

LAMBDA = Fraction(19, 503)
MAXR = 64

M = [0] * (MAXR + 1)
for q in range(MAXR + 1):
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    M[q] = d

TAU = [None] * (MAXR + 1)
for r in range(1, MAXR + 1):
    TAU[r] = Fraction(3**r, 2 ** (r + M[r] + 1))


def phase_intervals(r: int):
    cuts = {Fraction(1, 2), Fraction(1, 1)}
    for j in range(1, r + 1):
        cuts.add(TAU[j])
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def phase_sum_coefficient(r: int, omega: Fraction) -> Fraction:
    g = Fraction(1)
    total = Fraction(0)
    for _ in range(r):
        total += g
        current = g * omega
        eps = 0 if current > Fraction(3, 4) else 1
        g *= Fraction(2, 3) if eps == 0 else Fraction(4, 3)
    return total


def minimum_phase_sum(r: int):
    best = None
    best_interval = None
    for lo, hi in phase_intervals(r):
        coeff = phase_sum_coefficient(r, (lo + hi) / 2)
        value = coeff * lo
        if best is None or value < best:
            best = value
            best_interval = (lo, hi)
    return best, best_interval


def multi_source_margin(r: int) -> Fraction:
    phase_sum, _ = minimum_phase_sum(r)
    # Every multi-source exact cylinder has total shortcut length H<=72.
    return phase_sum / 6 - 72 * LAMBDA


def main():
    # r=23 is still not automatically safe, r=24 is.
    assert multi_source_margin(23) == Fraction(
        -8_718_910_501_493,
        147_647_688_081_408,
    ) < 0
    assert multi_source_margin(24) == Fraction(
        47_327_533_441_417,
        560_599_815_684_096,
    ) > 0

    # Every later r through the only still-interesting MATH-062 range is safe.
    margins = []
    for r in range(24, 65):
        margin = multi_source_margin(r)
        assert margin > 0, (r, margin)
        margins.append((margin, r))

    min_margin, min_r = min(margins)
    assert min_r == 24

    s23, i23 = minimum_phase_sum(23)
    s24, i24 = minimum_phase_sum(24)

    print("last_unresolved_multi_source_paid_count", 23)
    print("first_automatic_multi_source_paid_count", 24)
    print("r23_phase_sum_inf", s23)
    print("r23_minimizing_phase_cell", i23)
    print("r23_adjusted_margin_at_H72", multi_source_margin(23))
    print("r24_phase_sum_inf", s24)
    print("r24_minimizing_phase_cell", i24)
    print("r24_adjusted_margin_at_H72", multi_source_margin(24))
    print("detailed_symbolic_multi_paid_range", "2..23")
    print("singleton_handoff_range_before_MATH062_auto_cutoff", "24..64")
    print("PASS MATH-063 resolution-sensitive multi-paid cutoff certificate")


if __name__ == "__main__":
    main()
