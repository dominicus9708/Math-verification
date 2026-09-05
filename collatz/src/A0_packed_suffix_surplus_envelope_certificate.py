#!/usr/bin/env python3
"""Arithmetic certificate for the A0 packed-suffix surplus envelope.

The companion note proves the ordered-position envelope structurally.  This
script verifies the exact constants used to turn its packed-suffix length into
a correction-budget loss.

This is not a proof of the Collatz conjecture.
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


l2, u2 = log_bounds(Fraction(1, 3))  # ln 2
l3, u3 = log_bounds(Fraction(1, 2))  # ln 3

# beta = log_2(3/2) = ln3/ln2 - 1.
beta_lo = l3 / u2 - 1
beta_hi = u3 / l2 - 1
assert beta_lo > 0
assert beta_hi < Fraction(117, 200)

# A0 endpoint constants.
delta_A_lo = A0 * l2 - Q0 * u3
delta_A_hi = A0 * u2 - Q0 * l3
assert delta_A_lo > 0
C_A_lower = 1 - delta_A_hi
assert C_A_lower > 0
loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
A_credit_upper = S_A_upper - loss_A_lower
assert A_credit_upper < Fraction(503, 1000) * G

# Structural lower bound from the companion note.  For checkpoint surplus
# r=s-1>=1, if m(r) is the number of odd ordinals in the packed suffix then
#     m(r) >= r + floor(200(r-1)/117),
# because 1/beta > 200/117.
def packed_count_lower(r: int) -> int:
    assert r >= 1
    return r + (200 * (r - 1)) // 117


def packed_loss_lower(r: int) -> Fraction:
    m = packed_count_lower(r)
    return Fraction(m, 6) - Fraction(1, 2)

# At the largest coefficient-wise possible surplus s=P, r=P-1.
rmax = P - 1
mmax_lower = packed_count_lower(rmax)
Lmax_lower = packed_loss_lower(rmax)
assert mmax_lower > 16_700_000_000
assert Lmax_lower > Fraction(325, 1000) * G

# The endpoint A0 credit is reduced by C_A times the normalized loss.
max_surplus_credit = A_credit_upper - C_A_lower * Lmax_lower
assert max_surplus_credit < Fraction(177, 1000) * G

print("PASS A0 packed-suffix surplus envelope certificate")
print("beta_hi", float(beta_hi))
print("rmax", rmax)
print("packed_count_lower", mmax_lower)
print("packed_loss_lower_over_G", float(Lmax_lower / G))
print("max_surplus_credit_over_G", float(max_surplus_credit / G))
