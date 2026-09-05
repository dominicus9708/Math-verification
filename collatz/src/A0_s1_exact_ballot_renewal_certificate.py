#!/usr/bin/env python3
"""Exact rational certificate for the s=1 ballot renewal point.

For alpha=log_3 2, prove
    ceil(alpha*t0)=j0=10R0+1
and
    ceil(alpha*A0)=Q0+1.
Thus an A0 first-crossing word in the s=1 sector has height zero at t0 and
first reaches height -1 only at A0.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
t0 = 10 * J0
j0 = 10 * R0 + 1
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3

# 10R0 < alpha*t0 < 10R0+1.
assert 10 * R0 < alpha_lo * t0
assert alpha_hi * t0 < 10 * R0 + 1

# Q0 < alpha*A0 < Q0+1.
assert Q0 < alpha_lo * A0
assert alpha_hi * A0 < Q0 + 1

assert j0 == 10 * R0 + 1

print("PASS A0 s=1 exact ballot renewal certificate")
print("t0", t0)
print("j0", j0)
print("ceil_alpha_t0", j0)
print("ceil_alpha_A0", Q0 + 1)
print("s1_height_at_t0", 0)
print("first_crossing_height_at_A0", -1)
