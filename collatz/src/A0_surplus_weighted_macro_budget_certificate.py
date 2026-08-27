#!/usr/bin/env python3
"""Exact certificate for surplus-weighted A0^k -> J0 macro budgets.

Combines the repaired A0 credit ceiling, the packed-suffix surplus tax, and
the primitive J0 debit.  It certifies minimal uniform surplus thresholds for
k=6,...,14 A0 returns that still force negative net gap drift when followed by
one J0 crossing.

This is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

BASE = 1 << 71
G = 1 << 33
J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
P = 6_189_245_291
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))  # ln 2
l3, u3 = log_bounds(Fraction(1, 2))  # ln 3

# A0 unrestricted credit ceiling.
delta_A_lo = A0 * l2 - Q0 * u3
delta_A_hi = A0 * u2 - Q0 * l3
assert delta_A_lo > 0
C_A_lower = 1 - delta_A_hi
assert C_A_lower > 0
loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
a_A = S_A_upper - loss_A_lower

# Primitive J0 debit floor.
delta_J_lo = J0 * l2 - R0 * u3
assert delta_J_lo > 0
a_J = BASE * delta_J_lo / (1 + delta_J_lo) - Fraction(R0, 3)
assert a_J > Fraction(2527, 1000) * G
assert 5 * a_A < a_J

# Packed-suffix tax lower bound for r=s-1>=1.
def packed_count_lower(r: int) -> int:
    assert r >= 1
    return r + (200 * (r - 1)) // 117


def packed_loss_lower(r: int) -> Fraction:
    if r <= 0:
        return Fraction(0)
    return Fraction(packed_count_lower(r), 6) - Fraction(1, 2)


def A_credit(r: int) -> Fraction:
    # Safe upper bound for one A0 block with checkpoint surplus r=s-1.
    return a_A - C_A_lower * packed_loss_lower(r)


# Minimal uniform r such that k A0 blocks, each with surplus >=r, followed by
# one primitive J0 debit has strictly negative net gap budget.
expected = {
    6: 1_541_530_042,
    7: 2_686_060_404,
    8: 3_544_458_175,
    9: 4_212_100_886,
    10: 4_746_215_055,
    11: 5_183_217_557,
    12: 5_547_386_309,
    13: 5_855_529_099,
    14: 6_119_651_490,
}

for k, rstar in expected.items():
    assert 1 <= rstar <= P - 1
    assert k * A_credit(rstar) < a_J
    assert k * A_credit(rstar - 1) >= a_J

# Even maximal coefficient-wise surplus does not make 15 such A0 blocks
# automatically dominated by one primitive J0 debit using this tax alone.
rmax = P - 1
assert 15 * A_credit(rmax) >= a_J

print("PASS A0 surplus-weighted macro budget certificate")
print("a_A_over_G", float(a_A / G))
print("a_J_over_G", float(a_J / G))
for k, rstar in expected.items():
    print(k, rstar, float(A_credit(rstar) / G))
print("k15_max_surplus_still_open", float(15 * A_credit(rmax) / G))
