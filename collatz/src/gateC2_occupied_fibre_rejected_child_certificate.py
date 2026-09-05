#!/usr/bin/env python3
"""Gate-C2 occupied-fibre / rejected-child certificate.

Checks the exact local identity
    c - v*u = 2 * rejected_mass
on a one-child parent, and evaluates the robust D-U contraction budget for
existing authoritative m=44 rows.

Finite diagnostics are not asymptotic theorems and do not prove Collatz.
"""

from fractions import Fraction
from math import log2


# Exhaustive local algebra over representative small child counts.
for c0 in range(33):
    for c1 in range(33):
        c = c0 + c1
        u = c0 - c1

        # child 0 survives, child 1 is rejected
        v = +1
        rejected = c1
        assert c - v * u == 2 * rejected

        # child 1 survives, child 0 is rejected
        v = -1
        rejected = c0
        assert c - v * u == 2 * rejected


# (L, C_L, D_L, U_L) from m44_full_mass_transport_certificate.cpp.
ROWS = (
    (3,  17592186044416, 8796093022208, 4194304),
    (4,  13194139533312, 8796095119360, 2048),
    (6,   8796091972608, 3298534882832, 40),
    (7,   7146824531190, 3848290434574, 56),
    (9,   5222679313909, 1649267244880, 8907),
    (11,  4398045691348, 1030791994834, 693772),
    (12,  3882649683210, 1460288668299, 494762),
    (14,  3152505354815, 743029190277, 3580205),
    (15,  2780990752541, 1022202010104, 6650859),
    (17,  2269889787451, 515932831671, 18318991),
    (19,  2011923507477, 355945413895, 76621889),
    (20,  1833950905184, 539891337183, 52632776),
    (22,  1564005133050, 295899305006, 117886560),
    (23,  1416055503075, 428095694704, 244836127),
    (25,  1202007610492, 228484933625, 440762934),
)

prod = Fraction(1, 1)
print("L  robust_delta=(D-U)/(2C)")
for L, C, D, U in ROWS:
    assert 0 <= U < D <= C
    delta = Fraction(D - U, 2 * C)
    assert 0 < delta < 1
    prod *= 1 - delta
    print(f"{L:2d}  {float(delta):.15f}")

initial = 1 << 44
robust_upper = Fraction(initial, 1) * prod
actual_C26 = 1087765074138

assert robust_upper >= actual_C26
assert actual_C26 > 0

robust_bits = -log2(float(prod))
actual_bits = 44.0 - log2(actual_C26)

print()
print("robust C26 upper bound =", float(robust_upper))
print("actual C26             =", actual_C26)
print("robust certified bit loss =", robust_bits)
print("actual bit loss           =", actual_bits)
print("gap in bit loss           =", actual_bits - robust_bits)

print("\nPASS: occupied-fibre rejected-child identity and m=44 robust budget verified.")
