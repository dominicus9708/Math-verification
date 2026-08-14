#!/usr/bin/env python3
"""Exact integer certificate for the first two type-0 gate return levels.

The proof note derives return times from irrational rotation.  This script
only checks the rational/power inequalities and macroblock arithmetic used
there.  Python integers make all power comparisons exact.
"""
from fractions import Fraction


def main() -> None:
    # Base length-19 type-0 gate exists because 12/19 is above log_3 2.
    assert 3**12 > 2**19

    # Exact bracket giving 81*epsilon < 1 < 82*epsilon.
    lo1 = Fraction(971, 1539)
    hi1 = Fraction(983, 1558)
    assert 3**lo1.numerator < 2**lo1.denominator
    assert 3**hi1.numerator > 2**hi1.denominator

    # First-return macroblock vectors.
    G81 = (19 * 81, 12 * 81 - 1)
    G82 = (19 * 82, 12 * 82 - 1)
    assert G81 == (1539, 971)
    assert G82 == (1558, 983)
    assert 3**G81[1] < 2**G81[0]
    assert 3**G82[1] > 2**G82[0]

    # Exact bracket giving 13*rho < 1 < 14*rho.
    lo2 = Fraction(13606, 21565)
    hi2 = Fraction(12635, 20026)
    assert hi2 == Fraction(665, 1054)
    assert 3**lo2.numerator < 2**lo2.denominator
    assert 3**hi2.numerator > 2**hi2.denominator

    # Second-return macroblock vectors.  Order/conjugacy is irrelevant here;
    # these are count vectors only.
    G13 = (12 * G81[0] + G82[0], 12 * G81[1] + G82[1])
    G14 = (13 * G81[0] + G82[0], 13 * G81[1] + G82[1])
    assert G13 == (20026, 12635)
    assert G14 == (21565, 13606)
    assert Fraction(G13[1], G13[0]) == Fraction(665, 1054)
    assert 3**G13[1] > 2**G13[0]
    assert 3**G14[1] < 2**G14[0]

    print("base: 3^12 > 2^19")
    print("first return times: 81 / 82")
    print("G81:", G81, "contracting")
    print("G82:", G82, "expanding")
    print("second return times: 13 / 14")
    print("G13:", G13, "expanding; reduced q/L = 665/1054")
    print("G14:", G14, "contracting")
    print("all exact integer comparisons passed")


if __name__ == "__main__":
    main()
