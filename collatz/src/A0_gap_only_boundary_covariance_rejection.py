#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

A0 = 114208327604
Q0 = 72057431991

# For every finite h<=46 used in the current boundary exposure,
# 3^Q0 vanishes modulo 3^h while 2^A0 is a unit.  Hence the covariance
# shift coefficient 2^A0-3^Q0 is invertible modulo 3^h.
for h in range(1, 47):
    M = 3**h
    c = (pow(2, A0, M) - pow(3, Q0, M)) % M
    assert c == pow(2, A0, M)
    assert gcd(c, M) == 1


def two(exp: int) -> Fraction:
    if exp >= 0:
        return Fraction(2**exp, 1)
    return Fraction(1, 2 ** (-exp))


# Regression only: a toy zero-control Hensel word.  Build a base path
# backwards from a terminal carry, then use the exact two-boundary covariance
# (K_R,K_L)->(K_R+3^q t,K_L+t).  The same controls remain valid and zero-cost,
# while the physical-gap functional Delta=2^A K_L-K_R can be made to occupy
# every residue modulo 3^h.
q = 7
A = 12
e = [-11, -9, -8, -6, -5, -3, -1]
K = [None] * (q + 1)
K[q] = Fraction(1, 1)
for i in range(q - 1, -1, -1):
    K[i] = 3 * K[i + 1] - two(e[i])
for i in range(q):
    assert (K[i] + two(e[i])) / 3 == K[i + 1]

K_R = K[0]
K_L = K[q]
Delta0 = 2**A * K_L - K_R

def frac_mod(x: Fraction, M: int) -> int:
    return (x.numerator * pow(x.denominator, -1, M)) % M


checks = 0
for h in range(1, 6):
    M = 3**h
    c = (2**A - 3**q) % M
    assert gcd(c, M) == 1
    base = frac_mod(Delta0, M)
    for target in range(M):
        t = ((target - base) * pow(c, -1, M)) % M
        KR2 = K_R + 3**q * t
        KL2 = K_L + t

        cur = KR2
        for i in range(q):
            cur = (cur + two(e[i])) / 3
        assert cur == KL2

        Delta2 = 2**A * KL2 - KR2
        assert frac_mod(Delta2, M) == target
        checks += 1

print("PASS gap-only boundary covariance rejection")
print("A0,Q0", A0, Q0)
print("finite_shift_coefficient_is_3adic_unit_through_depth", 46)
print("toy_all_gap_residues_reached", checks)
print("conclusion: finite gap residue alone cannot yield positive uniform Hensel cost")
