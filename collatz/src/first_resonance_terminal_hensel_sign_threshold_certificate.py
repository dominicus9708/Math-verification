#!/usr/bin/env python3
"""Exact arithmetic certificate for the first-resonance terminal Hensel-sign threshold.

This file proves two ingredients used in the next proof stage:

1. one-class terminal Hensel lift at a new earliest odd ordinal;
2. a 50%-weighted sign-mismatch threshold which would already exceed the
   repaired first-resonance defect budget.

It does not prove the Collatz conjecture.
"""

from fractions import Fraction

A = 114_208_327_604
Q = 72_057_431_991
BUDGET = 4_314_000_000
OMITTED_LAST = 46
NLOG = 120


def log_bounds(z: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


def mech(j: int) -> int:
    return ((j - 1) * A) // Q


def endpoint(m: int, dmap: dict[int, int]) -> int:
    M = 3**m
    inv = pow(2, -A, M)
    total = 0
    for t in range(m):
        j = Q - m + 1 + t
        a = mech(j) - dmap.get(t, 0)
        total = (total + pow(3, m - 1 - t, M) * pow(2, a, M)) % M
    return (inv * total) % M


def carry(m: int, dmap: dict[int, int], y: int) -> int:
    M = 3 ** (m + 1)
    inv = pow(2, -A, M)
    total = 0
    for t in range(m):
        j = Q - m + 1 + t
        a = mech(j) - dmap.get(t, 0)
        total = (total + pow(3, m - 1 - t, M) * pow(2, a, M)) % M
    z = (inv * total) % M
    assert (z - y) % (3**m) == 0
    return ((z - y) // (3**m)) % 3


def required_parity(m: int, c: int):
    """Parity class of a new earliest displacement d.

    A lift from m to m+1 must satisfy
        c + 2^(b_{Q-m}-A-d) == 0 (mod 3).
    If c=0 there is no lift.  Otherwise exactly one parity class works.
    """
    if c == 0:
        return None
    B0 = mech(Q - m)
    good = []
    for d in (0, 1):
        if (c + pow(2, B0 - A - d, 3)) % 3 == 0:
            good.append(d)
    assert len(good) == 1
    return good[0]


def shift(dmap: dict[int, int], new_d: int) -> dict[int, int]:
    out = {0: new_d}
    for t, d in dmap.items():
        out[t + 1] = d
    return out


def ordering_ok(m: int, dmap: dict[int, int]) -> bool:
    B = [mech(Q - m + 1 + t) for t in range(m)]
    for t in range(1, m):
        gap = B[t] - B[t - 1]
        if dmap.get(t, 0) > dmap.get(t - 1, 0) + gap - 1:
            return False
    return True


def main() -> None:
    # ---------------------------------------------------------------
    # Exact one-class Hensel-lift regression on the surviving m=66
    # support-11 state from the exhaustive split computation.
    # ---------------------------------------------------------------
    y = 2_620_472_197_936_414_017_727
    d66 = {
        2: 1, 12: 1, 13: 1,
        22: 1, 23: 1, 24: 2,
        48: 1, 49: 2, 50: 1, 51: 1, 55: 1,
    }
    assert endpoint(66, d66) == y
    c66 = carry(66, d66, y)
    assert c66 == 1
    assert required_parity(66, c66) == 0

    # New leading gap at m=67 is 2, so d=0 is ordering-compatible.
    d67 = shift(d66, 0)
    assert ordering_ok(67, d67)
    assert endpoint(67, d67) == y

    # At the next lift the required parity is odd.  Hence support cannot stay 11.
    c67 = carry(67, d67, y)
    assert c67 == 1
    assert required_parity(67, c67) == 1
    d68 = shift(d67, 1)
    assert ordering_ok(68, d68)
    assert endpoint(68, d68) == y

    # ---------------------------------------------------------------
    # Weighted 50% threshold.
    # For b_j=floor((j-1)log_2 3), a parity mismatch forces odd d_j>=1,
    # and therefore normalized defect at least
    #   c_j = 2^(b_j-1)/3^j.
    # Farey-floor permutation gives total single-step mass
    #   C_all > Q/(12 ln 2).
    # Dropping the final 46 terms costs at most 46/6.
    # ---------------------------------------------------------------
    _, u2 = log_bounds(Fraction(1, 3), NLOG)
    C_pre_lower = Fraction(Q, 1) / (12 * u2) - Fraction(OMITTED_LAST, 6)
    half_lower = C_pre_lower / 2
    assert half_lower > BUDGET

    margin = half_lower - BUDGET
    correlation_margin = C_pre_lower - 2 * BUDGET
    assert margin > 17_500_000
    assert correlation_margin > 35_000_000

    # Candidate survival therefore requires weighted mismatch < 1/2.
    # Equivalently the weighted sign correlation must retain a positive bias.
    # The exact rational lower bound below is about 0.00404879 of C_pre.
    bias_lower = correlation_margin / C_pre_lower
    assert bias_lower > Fraction(4, 1000)

    print("PASS terminal Hensel-sign threshold certificate")
    print("m66_carry", c66, "required_parity", 0)
    print("m67_carry", c67, "required_parity", 1)
    print("support-11 preserving lift fails at m68")
    print("support-12 explicit lift endpoint", y)
    print("C_pre_lower", float(C_pre_lower))
    print("half_mass_lower", float(half_lower))
    print("half_mass_minus_budget", float(margin))
    print("required_positive_correlation_margin", float(correlation_margin))
    print("relative_bias_lower", float(bias_lower))


if __name__ == "__main__":
    main()
