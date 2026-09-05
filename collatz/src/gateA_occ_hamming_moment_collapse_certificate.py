#!/usr/bin/env python3
"""Exact algebra for the Gate A occupied-selector Hamming-moment collapse.

The Beatty macro-pair payoff depends only on H=number of odd choices in the
5- or 6-bit extension block.  Therefore the 31/63 local Walsh coefficients are
only one representation of a single scalar exponential moment E[(3/2)^H].

This script certifies the exact contraction thresholds and excess/deficit
identities.  It is not a Collatz proof.
"""

from fractions import Fraction
from math import comb

A = Fraction(3, 2)
PATTERNS = {
    "AB": (5, 3, Fraction(3125, 3456)),
    "BA": (5, 3, Fraction(3125, 3456)),
    "BB": (6, 4, Fraction(15625, 20736)),
}


def main():
    for name, (L, rises, sigma) in PATTERNS.items():
        payoff = [A ** (h - rises) for h in range(L + 1)]
        uniform = sum(Fraction(comb(L, h), 2**L) * payoff[h]
                      for h in range(L + 1))
        assert uniform == sigma

        # Contraction for a probability histogram p_h is exactly
        # sum_h p_h A^h < A^r.
        threshold = A ** rises

        print(name, "L", L, "rises", rises)
        print("  sigma", f"{sigma.numerator}/{sigma.denominator}", float(sigma))
        print("  exponential_moment_threshold_E_A_pow_H_lt",
              f"{threshold.numerator}/{threshold.denominator}", float(threshold))
        print("  payoff_by_h",
              " ".join(f"{v.numerator}/{v.denominator}" for v in payoff))

        deficits = []
        excesses = []
        for h, v in enumerate(payoff):
            if v < 1:
                deficits.append((h, 1 - v))
            elif v > 1:
                excesses.append((h, v - 1))

        print("  deficits", " ".join(f"h{h}:{d.numerator}/{d.denominator}" for h, d in deficits))
        print("  excesses", " ".join(f"h{h}:{e.numerator}/{e.denominator}" for h, e in excesses))

    # Exact failure-pressure identities quoted in the companion note.
    # AB/BA: failure iff
    # 1/2 p4 + 5/4 p5 >= 19/27 p0 + 5/9 p1 + 1/3 p2.
    # BB: failure iff
    # 1/2 p5 + 5/4 p6 >= 65/81 p0 + 19/27 p1 + 5/9 p2 + 1/3 p3.
    assert A**(4-3) - 1 == Fraction(1, 2)
    assert A**(5-3) - 1 == Fraction(5, 4)
    assert 1 - A**(0-3) == Fraction(19, 27)
    assert 1 - A**(1-3) == Fraction(5, 9)
    assert 1 - A**(2-3) == Fraction(1, 3)

    assert A**(5-4) - 1 == Fraction(1, 2)
    assert A**(6-4) - 1 == Fraction(5, 4)
    assert 1 - A**(0-4) == Fraction(65, 81)
    assert 1 - A**(1-4) == Fraction(19, 27)
    assert 1 - A**(2-4) == Fraction(5, 9)
    assert 1 - A**(3-4) == Fraction(1, 3)

    print("PASS")


if __name__ == "__main__":
    main()
