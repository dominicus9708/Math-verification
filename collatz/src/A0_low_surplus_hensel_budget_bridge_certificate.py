#!/usr/bin/env python3
"""Exact numeric certificate for the low-surplus A0 defect-cost budget.

The companion note proves the algebraic bridge between ordered-position defect
and the boundary-preserving Hensel min-plus cost.  This script certifies the
coarse global budgets in the promoted strip and after the A0,A0,J0 reset.

This is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

BASE = 1 << 71
G = 1 << 33
A0 = 114_208_327_604
Q0 = 72_057_431_991
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

delta_A_lo = A0 * l2 - Q0 * u3
delta_A_hi = A0 * u2 - Q0 * l3
assert delta_A_lo > 0

# C_A=e^{-delta_A}>1-delta_A_hi.
C_A_lower = 1 - delta_A_hi
assert C_A_lower > 0

loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
a_A = S_A_upper - loss_A_lower
assert a_A < Fraction(503, 1000) * G

# If an A0 first-crossing word has ordered-position defect D relative to the
# mechanical envelope and its endpoint remains >=N, then C_A*D < d+a_A.
# Thus D < (d+a_A)/C_A_lower.
promoted_budget = (2 * G + a_A) / C_A_lower
assert promoted_budget < Fraction(2503, 1000) * G

reset_budget = (Fraction(478, 1000) * G + a_A) / C_A_lower
assert reset_budget < Fraction(981, 1000) * G

print("PASS A0 low-surplus Hensel budget bridge certificate")
print("promoted_defect_budget_over_G", float(promoted_budget / G))
print("reset_defect_budget_over_G", float(reset_budget / G))
