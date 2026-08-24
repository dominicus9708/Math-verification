#!/usr/bin/env python3
"""Exact-rational start-ceiling consequence of the q<=8 level-set window bound.

No floating-point comparison is used in assertions.
"""
from fractions import Fraction

A = 217_976_794_617
H = 137_528_045_312
W6 = 917_388_026_368
SCALAR_R = 26_990_139_680
NLOG = 70


def log_ratio_bounds(x: Fraction, n: int):
    # ln((1+x)/(1-x)) = 2 sum_{k>=0} x^(2k+1)/(2k+1)
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


def floorq(x: Fraction) -> int:
    return x.numerator // x.denominator


l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)

# ln P = A ln 2 - H ln 3.
logP_lo = A*l2 - H*u3
logP_hi = A*u2 - H*l3
assert 0 < logP_lo < logP_hi

# Safe lower bound P >= 1 + ln P >= 1 + logP_lo.
P_lo = 1 + logP_lo

# Denjoy--Koksma correction envelope.
S_up = Fraction(H, 1)/(6*l2) + Fraction(1, 3)

# Six-level run-average/window consequence:
# eta >= (5/1536) W6.
eta6 = Fraction(5*W6, 1536)
assert eta6 == Fraction(8_958_867_445, 3)

# Previous scalar q<=8 consequence for comparison.
eta_scalar = Fraction(5*SCALAR_R, 48)

# From (P-1)N + P g = c_chr - eta, g>=4:
# N <= [S_up - eta - 4 P_lo] / logP_lo.
def safe_upper(eta: Fraction) -> Fraction:
    num = S_up - eta - 4*P_lo
    assert num > 0
    return num / logP_lo

U0 = safe_upper(Fraction(0))
Us = safe_upper(eta_scalar)
U6 = safe_upper(eta6)

assert floorq(U0) == 36_797_780_654_565_556_495_673
assert floorq(Us) == 33_669_246_025_206_472_572_429
assert floorq(U6) == 33_474_714_987_020_083_379_399
assert U6 < Us < U0 < 2**75
assert U6 > 2**74

print('q8 level-set start ceiling: PASS')
print('eta6 =', eta6, '=', float(eta6))
print('floor no-defect safe ceiling =', floorq(U0))
print('floor scalar-q8 safe ceiling =', floorq(Us))
print('floor level6-weighted safe ceiling =', floorq(U6))
print('gain vs scalar-q8 =', floorq(Us)-floorq(U6))
print('gain vs zero-defect =', floorq(U0)-floorq(U6))
print('dyadic band: 2^74 < U6 < 2^75')
