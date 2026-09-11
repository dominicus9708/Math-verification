#!/usr/bin/env python3
"""
MATH-062 exact paid-cluster phase-sum certificate.

For a paid cluster containing r>=2 positive-slack odd events, MATH-058 gives
macro length <= 73+2r.  Every paid odd occurs at slack u>=1, hence its exact
MATH-053 penalty is at least Omega/6.  Successive paid odds advance q by one,
so their Omega values are consecutive iterates of the exact phase map,
independent of the intervening even steps.

This certificate minimizes the sum of r consecutive phase values exactly over
the complete source phase interval (1/2,1), using the rational phase partition.
It proves that for the MATH-060 target lambda=19/503 every r>=65 multi-paid
cluster has nonnegative adjusted cost P-lambda*length.  Therefore only
2<=r<=64 multi-paid clusters require detailed Bellman graph treatment.

Finite exact arithmetic only.  This is not a proof of first-cell emptiness or
of the Collatz conjecture.
"""
from fractions import Fraction

LAMBDA = Fraction(19, 503)
MAXR = 129

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
    """A with sum_{j<r} Omega_j = A*Omega_0 on one phase cell."""
    g = Fraction(1)
    total = Fraction(0)
    for _ in range(r):
        total += g
        current = g * omega
        eps = 0 if current > Fraction(3, 4) else 1
        g *= Fraction(2, 3) if eps == 0 else Fraction(4, 3)
    return total


def minimum_phase_sum(r: int):
    """Exact infimum of r consecutive Omega values over Omega_0 in (1/2,1)."""
    best = None
    best_interval = None
    best_coefficient = None
    for lo, hi in phase_intervals(r):
        mid = (lo + hi) / 2
        a = phase_sum_coefficient(r, mid)
        value = a * lo  # infimum on this open cell, approached from the right
        if best is None or value < best:
            best = value
            best_interval = (lo, hi)
            best_coefficient = a
    return best, best_interval, best_coefficient


def pair_bound(r: int) -> Fraction:
    """Uniform lower bound for sum of r consecutive phases.

    For any Omega in (1/2,1), the next phase is 2Omega/3 when Omega>3/4
    and 4Omega/3 when Omega<3/4.  Hence every consecutive pair has sum >7/6.
    """
    if r % 2 == 0:
        return Fraction(7 * r, 12)
    return Fraction(7 * r - 1, 12)


def adjusted_margin_from_sum(r: int, phase_sum_lb: Fraction) -> Fraction:
    penalty_lb = phase_sum_lb / 6
    length_ub = 73 + 2 * r
    return penalty_lb - LAMBDA * length_ub


def main():
    # No r<65 is automatically safe by the exact phase-sum bound.
    for r in range(2, 65):
        s, _, _ = minimum_phase_sum(r)
        assert adjusted_margin_from_sum(r, s) < 0, r

    # Exact phase partition closes the finite transition zone 65..127.
    margins = []
    for r in range(65, 128):
        s, interval, coeff = minimum_phase_sum(r)
        margin = adjusted_margin_from_sum(r, s)
        assert margin > 0, (r, margin, interval, coeff)
        margins.append((margin, r))

    min_margin, min_r = min(margins)
    assert min_r == 65
    assert min_margin == Fraction(
        1274361128696688015500375548948475,
        20682482655386529667021920924598272,
    )

    # For all larger r, the elementary two-phase pairing is enough.
    m128 = adjusted_margin_from_sum(128, pair_bound(128))
    m129 = adjusted_margin_from_sum(129, pair_bound(129))
    assert m128 == Fraction(77, 4527) > 0
    assert m129 == Fraction(449, 18108) > 0

    # Increasing r by two adds 7/6 to the phase-sum lower bound, hence 7/36
    # to penalty, while the length target rises by 4*lambda.  The difference
    # is strictly positive, so the two base parities cover every r>=128.
    assert Fraction(7, 36) - 4 * LAMBDA > 0

    s65, i65, _ = minimum_phase_sum(65)
    print("first_automatic_paid_count", 65)
    print("r65_phase_sum_inf", s65)
    print("r65_minimizing_phase_cell", i65)
    print("r65_adjusted_margin", min_margin)
    print("r128_pair_margin", m128)
    print("r129_pair_margin", m129)
    print("detailed_multi_paid_range", "2..64")
    print("PASS MATH-062 exact paid-cluster phase-sum certificate")


if __name__ == "__main__":
    main()
