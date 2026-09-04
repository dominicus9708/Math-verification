#!/usr/bin/env python3
"""Arithmetic regression for external recursive-sufficiency source closure.

This certificate checks only the exact numerical comparison used by
EXTERNAL_RECURSIVE_SUFFICIENCY_SOURCE_CORRIDOR_CLOSURE.md.

The external mathematical dependencies themselves are not reproved here:

* Bařina verification through 2^71;
* Ansari 2025 recursive-sufficiency interval extension.
"""

from fractions import Fraction

TWO71 = 1 << 71
N44 = 2 * (3 ** 44) + 1
L_RS = 2 * N44

assert N44 == 1_969_541_804_367_222_465_763
assert TWO71 == 2_361_183_241_434_822_606_848
assert TWO71 - N44 == 391_641_437_067_600_141_085
assert N44 < TWO71

assert L_RS == 4 * (3 ** 44) + 2
assert L_RS == 3_939_083_608_734_444_931_526

# Current independently certified SAFE source upper endpoint.
U_X = Fraction(4, 3) * TWO71 + Fraction(239, 500) * (1 << 33)
assert U_X == Fraction(1_180_591_620_718_951_049_199_616, 375)
assert U_X.numerator // U_X.denominator == 3_148_244_321_917_202_797_865

MARGIN = Fraction(L_RS, 1) - U_X
assert MARGIN == Fraction(296_564_732_556_465_800_122_634, 375)
assert MARGIN > 0
assert U_X < L_RS

# Any integer satisfying X<U_X obeys this integer upper bound.
INTEGER_SOURCE_MAX = (U_X.numerator - 1) // U_X.denominator
assert INTEGER_SOURCE_MAX == 3_148_244_321_917_202_797_865
assert INTEGER_SOURCE_MAX < L_RS

print("PASS external recursive-sufficiency source-corridor arithmetic")
print("N44", N44)
print("2^71", TWO71)
print("extended_bound", L_RS)
print("source_integer_max", INTEGER_SOURCE_MAX)
print("positive_margin", MARGIN)
print("external_dependency_status", "Barina 2^71 + Ansari Proposition 3.2")
print("route_consequence", "current A0 s=1 Route-B source corridor externally finite-range closed")
