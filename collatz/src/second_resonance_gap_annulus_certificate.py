#!/usr/bin/env python3
"""Exact rational certificate for the repaired second-resonance gap annulus.

Assumptions already proved/isolated on the repaired branch:
  * N is a hypothetical minimal counterexample with N > 2^71.
  * At the first global resonance
      (A0,Q0)=(114208327604,72057431991)
    one has y=T^A0(N)=N+g with 0<g<2^33 and g divisible by 4.
  * y coefficient-survives every proper prefix up to A0.
  * On the exact second-resonance branch at
      (K1,P1)=(103768467013,65470613321)
    the endpoint block has exactly P1 odd steps.

Let z=T^K1(y) and h=z-N.  This certificate proves the numerical inequalities
needed for

    2^33 < h < 7*2^33,

using only exact rational atanh-series bounds for ln2, ln3 and elementary
inequalities exp(x)-1>x and exp(x)<=1/(1-x) for 0<x<1.

The companion note supplies the symbolic Collatz argument, including h=0 mod 4.
This is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

A0 = 114_208_327_604
Q0 = 72_057_431_991
K1 = 103_768_467_013
P1 = 65_470_613_321
BASE = 1 << 71
G = 1 << 33
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2)
        * z ** (2 * n + 3)
        / ((2 * n + 3) * (1 - z * z))
    )
    return s, s + tail


# ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2).
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# First-resonance logarithmic coefficient defect:
# P0=2^A0/3^Q0 = exp(x0), hence P0-1 > x0.
x0_lo = A0 * l2 - Q0 * u3
assert x0_lo > 0

# Mechanical normalized correction ceiling at the first crossing.
Smax_up = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)

# Since g>0, S_w>(P0-1)N>x0*N, so N<Smax/x0.
N_upper = Smax_up / x0_lo
assert N_upper < Fraction(4, 3) * BASE

# Exact second-block logarithmic surplus x1=P1 ln3-K1 ln2.
x1_lo = P1 * l3 - K1 * u2
x1_hi = P1 * u3 - K1 * l2
assert x1_lo > Fraction(1, 1 << 38)
assert x1_hi < Fraction(1, 1 << 37)

# Lower gap: B1=exp(x1), so B1-1>x1. Since y>N>2^71,
# z-y>(B1-1)y>x1*2^71>2^33.
assert x1_lo * BASE > G

# Upper gap: set U=2^-37>x1. For 0<x1<U<1,
# exp(x1)<=1/(1-U), so B1-1<=U/(1-U).
# Proper-prefix coefficient survival gives R1<=P1*3^(P1-1), hence
# z-y <= (B1-1)y + B1*P1/3.
# Also y=N+g < (4/3)2^71+2^33.
U = Fraction(1, 1 << 37)
y_upper = Fraction(4, 3) * BASE + G
second_increment_upper = (
    U * y_upper + Fraction(P1, 3)
) / (1 - U)
h_upper = G + second_increment_upper
assert h_upper < 7 * G

# The same coarse bound is vastly below N and even below N/3,
# which is used in the companion note to force z=3 mod 4.
assert 7 * G < BASE
assert 3 * 7 * G + 1 < BASE

print("PASS repaired second-resonance gap annulus certificate")
print("N_upper_over_2^71", float(N_upper / BASE))
print("second_log_surplus_lower", float(x1_lo))
print("second_log_surplus_upper", float(x1_hi))
print("lower_increment_over_2^33", float(x1_lo * BASE / G))
print("h_upper_over_2^33", float(h_upper / G))
print("certified_annulus: 2^33 < h < 7*2^33")
