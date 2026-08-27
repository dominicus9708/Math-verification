#!/usr/bin/env python3
"""Exact arithmetic certificate for the A0 checkpoint surplus-tax bound.

This certificate supports the structural lemma proved in the companion note.
It verifies the continued-fraction phase facts at the tenth J0 checkpoint,
the local position of the next mechanical odd event, and the numerical endpoint
credit bounds used after imposing a checkpoint surplus s>=1.

This does not prove the Collatz conjecture.
"""

from fractions import Fraction

BASE = 1 << 71
G = 1 << 33
J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
U = 9_809_721_694
P = 6_189_245_291
T0 = 10 * J0
JBASE = 10 * R0 + 1
NLOG = 90

assert T0 + U == A0
assert 10 * R0 + P == Q0


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


# ln 2 and ln 3 bounds.
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3

# At T0=10J0 the mechanical prefix count is exactly 10R0+1.
assert Fraction(10 * R0, T0) < alpha_lo
assert alpha_hi < Fraction(10 * R0 + 1, T0)

# The next mechanical odd ordinal JBASE+1 occurs exactly at step T0+2:
# ceil(alpha*(T0+1)) = JBASE and ceil(alpha*(T0+2)) = JBASE+1.
assert alpha_hi * (T0 + 1) < JBASE
assert alpha_lo * (T0 + 2) > JBASE

# A0 is a lower resonance.
delta_A_lo = A0 * l2 - Q0 * u3
delta_A_hi = A0 * u2 - Q0 * l3
assert delta_A_lo > 0
assert delta_A_hi > 0

# e^{-delta_A} > 1-delta_A_hi.
C_A_lower = 1 - delta_A_hi
assert C_A_lower > 0

# Mechanical first-crossing normalized correction ceiling and root-loss floor.
loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
A_credit_upper = S_A_upper - loss_A_lower
assert A_credit_upper < Fraction(503, 1000) * G

# Structural lemma from the companion proof:
# if the tenth-checkpoint surplus is s and r=s-1>=1 extra odd ordinals have
# crossed left of T0, the normalized correction loses strictly more than
#     r/6 - 1/12.
# The script checks the endpoint consequences of this exact symbolic bound.
def tax_lower(r: int) -> Fraction:
    assert r >= 1
    return Fraction(r, 6) - Fraction(1, 12)

# At the largest arithmetically possible transported surplus, s=P,
# r=P-1 and the surplus tax is already >0.120 G.
rmax = P - 1
max_tax = tax_lower(rmax)
assert max_tax > Fraction(120, 1000) * G

# Because the endpoint receives the tax multiplied by C_A, the worst-case
# A0 gap credit at s=P is below 0.383 G.
max_surplus_credit = A_credit_upper - C_A_lower * max_tax
assert max_surplus_credit < Fraction(383, 1000) * G

print("PASS A0 checkpoint surplus-tax certificate")
print("A0_credit_upper_over_G", float(A_credit_upper / G))
print("max_surplus_tax_lower_over_G", float(max_tax / G))
print("max_surplus_credit_over_G", float(max_surplus_credit / G))
print("checkpoint", T0, JBASE)
print("next_mechanical_odd_step", T0 + 2)
