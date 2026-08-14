#!/usr/bin/env python3
"""Exact rational certificate for the G81/G82 gate conjugacy theorem.

No floating-point arithmetic is used.
The only transcendental input is bracketed by two certified convergents
L < alpha=log_3(2) < U.
The power inequalities proving those bounds are intended to be checked
independently by any big-integer system:
    3**15601 < 2**24727
    3**31867 > 2**50508
"""

from fractions import Fraction

LOW = Fraction(15601, 24727)
HIGH = Fraction(31867, 50508)

# epsilon-delta = 983 - 1558 alpha.
# G81 chronological start phase: [0, cut)
# G82 chronological start phase: [cut, epsilon)


def ceil_alpha_j(j: int) -> int:
    fl = (j * LOW.numerator) // LOW.denominator
    fh = (j * HIGH.numerator) // HIGH.denominator
    assert fl == fh, (j, fl, fh)
    return fl + 1


def p_less_than_cut(j: int, d: int) -> bool:
    # p_j - cut = (d-983) + (1558-j) alpha.
    lo = Fraction(d - 983, 1) + Fraction(1558 - j, 1) * LOW
    hi = Fraction(d - 983, 1) + Fraction(1558 - j, 1) * HIGH
    if hi < 0:
        return True
    if lo >= 0:
        return False
    raise AssertionError(("ambiguous cut", j, lo, hi))


def p_less_than_epsilon(j: int, d: int) -> bool:
    # p_j - epsilon = (d-12) + (19-j) alpha.
    c = 19 - j
    if c >= 0:
        lo = Fraction(d - 12, 1) + c * LOW
        hi = Fraction(d - 12, 1) + c * HIGH
    else:
        lo = Fraction(d - 12, 1) + c * HIGH
        hi = Fraction(d - 12, 1) + c * LOW
    if hi < 0:
        return True
    if lo >= 0:
        return False
    raise AssertionError(("ambiguous epsilon", j, lo, hi))


# G81 interior discontinuities.
g81 = []
for j in range(1, 1540):
    d = ceil_alpha_j(j)
    if p_less_than_cut(j, d):
        g81.append((j, d))

expected_numeric = [
    (84, 53), (168, 106), (252, 159), (336, 212),
    (420, 265), (504, 318), (569, 359), (653, 412),
    (737, 465), (821, 518), (905, 571), (989, 624),
    (1054, 665), (1138, 718), (1222, 771), (1306, 824),
    (1390, 877), (1474, 930),
]
assert g81 == expected_numeric
assert len(g81) == 18

# G82 has no discontinuity strictly inside [cut, epsilon).
g82 = []
for j in range(1, 1559):
    d = ceil_alpha_j(j)
    above_cut = not p_less_than_cut(j, d)
    below_eps = p_less_than_epsilon(j, d)
    if above_cut and below_eps:
        # j=1558 is the left endpoint p_j=cut, not an interior point.
        # Exact endpoint identity follows algebraically:
        # ceil(1558 alpha)=983, p_1558=983-1558 alpha=cut.
        if j != 1558:
            g82.append((j, d))
assert g82 == []

# Phase order of the 18 G81 discontinuities.
phase_order = []
for a in range(6):
    for b in range(3):
        j = 1054 + 84 * a - 485 * b
        d = 665 + 53 * a - 306 * b
        r = 971 - d
        phase_order.append((j, d, r))

assert sorted((j, d) for j, d, _ in phase_order) == expected_numeric
assert len({r for _, _, r in phase_order}) == 18

# The declared continued-fraction lattice determinants.
assert 53 * 485 - 306 * 84 == 1
assert 665 * 485 - 306 * 1054 == 1

print("G81 factor types:", len(g81) + 1)
print("G82 factor types: 1")
print("phase-order (j,d,r):")
for row in phase_order:
    print(row)
print("certificate: PASS")
