#!/usr/bin/env python3
"""Exact-rational start-ceiling consequences of the q<=8 level-set window bounds.

The all-core threshold is the authoritative length-48 result, where the
remaining recursive core itself gives zero-defect states below 2^75 while every
length-48 zero-endpoint local parity word has time-expanded length at least 76.
Thus local parity multiplicity is one across all three remaining 44-trit affine
blocks.  The first-block length-47 threshold is reported separately.
No floating-point comparison is used in assertions.
"""
from fractions import Fraction

A = 217_976_794_617
H = 137_528_045_312
W_FIRST = 917_388_026_368
W_ALL = 894_734_262_659
NLOG = 70


def log_ratio_bounds(x: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


def floorq(x: Fraction) -> int:
    return x.numerator // x.denominator


l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)
logP_lo = A*l2 - H*u3
logP_hi = A*u2 - H*l3
assert 0 < logP_lo < logP_hi
P_lo = 1 + logP_lo
S_up = Fraction(H, 1)/(6*l2) + Fraction(1, 3)

eta_first = Fraction(5*W_FIRST, 1536)
eta_all = Fraction(5*W_ALL, 1536)
assert eta_first == Fraction(8_958_867_445, 3)
assert eta_all == Fraction(4_473_671_313_295, 1536)


def safe_upper(eta: Fraction) -> Fraction:
    # (P-1)N + Pg = c_chr-eta, g>=4,
    # c_chr <= S_up, P-1 >= logP_lo, P >= P_lo.
    num = S_up - eta - 4*P_lo
    assert num > 0
    return num / logP_lo


U0 = safe_upper(Fraction(0))
U_first = safe_upper(eta_first)
U_all = safe_upper(eta_all)

assert floorq(U0) == 36_797_780_654_565_556_495_673
assert floorq(U_first) == 33_474_714_987_020_083_379_399
assert floorq(U_all) == 33_556_773_987_419_405_994_758
assert U_first < U_all < U0 < 2**75
assert U_all > 2**74

p44 = 3**44
first_core_max = 6*p44 + 1
all_core_max = 18*p44 + 1
assert first_core_max == 5_908_625_413_101_667_397_287
assert all_core_max == 17_725_876_239_305_002_191_859
assert first_core_max < 2**73
assert all_core_max < 2**74
assert all_core_max < U_all

print('q8 level-set start ceiling: PASS')
print('eta_first =', eta_first)
print('eta_all_L48 =', eta_all)
print('floor no-defect safe ceiling =', floorq(U0))
print('floor first-block weighted ceiling =', floorq(U_first))
print('floor all-core L48 weighted ceiling =', floorq(U_all))
print('all-core gain vs zero-defect =', floorq(U0)-floorq(U_all))
print('remaining all-core max =', all_core_max)
print('ceiling does not prune the remaining core; all-core max is already < 2^74')
