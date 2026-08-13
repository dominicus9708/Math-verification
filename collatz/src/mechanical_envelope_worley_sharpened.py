#!/usr/bin/env python3
"""Exact mechanical-envelope sharpening of the Worley resonance isolation.

This certificate replaces the older all-parity correction ceiling

    S <= (7q+1)/24

by the first-crossing mechanical/Christoffel envelope

    S <= q/(6 ln 2) + 1/3.

At the current verified floor V_32 this lowers the Worley constant below
1.666, so the Worley--Dujella product restriction improves from rs<=4 to
rs<=3.  Exact rational logarithm intervals are used throughout.
"""

from fractions import Fraction
from math import gcd

Q0 = 72_057_431_991
Q1 = 137_528_045_312
LOW = 4 * (3**44 + 3**32) + 2
NLOG = 60


def log_ratio_bounds(x: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


def interval_cf(lo: Fraction, hi: Fraction, n: int):
    out = []
    for _ in range(n):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1
        a = a0
        out.append(a)
        lo -= a
        hi -= a
        assert lo > 0
        lo, hi = 1/hi, 1/lo
    return out


def convergents(cf):
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out = []
    for a in cf:
        p = a*p1 + p2
        q = a*q1 + q2
        out.append((p, q))
        p2, p1 = p1, p
        q2, q1 = q1, q
    return out


l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)
alpha_lo = l3 / u2
alpha_hi = u3 / l2
cf = interval_cf(alpha_lo, alpha_hi, 26)
cv = convergents(cf)

# Mechanical-envelope first-crossing bound:
#
#   x(P-1) <= q/(6 ln2)+1/3,
#   P-1 >= q ln2 (sigma/q-alpha).
#
# Hence
#
#   0 < sigma/q-alpha
#     < 1/(6*x*(ln2)^2) + 1/(3*x*q*ln2).
#
# Rewriting as error < k(q)/q^2 gives
#
#   k(q)=q^2/(6*x*(ln2)^2)+q/(3*x*ln2).
#
# It is increasing in q and decreasing in x, so Q1 and LOW give a rigorous
# interval-wide upper bound.  Lower log bound l2 makes the rational bound safe.
KMAX = (
    Fraction(Q1 * Q1, 1) / (6 * LOW * l2 * l2)
    + Fraction(Q1, 1) / (3 * LOW * l2)
)
assert KMAX < Fraction(1666, 1000)

# Direct approximation error bound, maximized over q in (Q0,Q1].
CMAX = (
    Fraction(1, 1) / (6 * LOW * l2 * l2)
    + Fraction(1, 1) / (3 * LOW * (Q0 + 1) * l2)
)

# Worley--Dujella gives rs < 2*KMAX < 3.332, hence integral rs<=3.
# Zero cases reproduce convergents after reduction.
pairs = [
    (1, 0), (0, 1),
    (1, 1), (1, 2), (2, 1),
    (1, 3), (3, 1),
]

worley = {}
for j in range(len(cv) - 1):
    p0, b0 = cv[j]
    p1, b1 = cv[j + 1]
    for r, s in pairs:
        for sign in (-1, 1):
            pp = r*p1 + sign*s*p0
            bb = r*b1 + sign*s*b0
            if pp <= 0 or bb <= 0:
                continue
            d = gcd(pp, bb)
            a, b = pp // d, bb // d
            if b > Q1:
                continue

            gmin = Q0 // b + 1
            gmax = Q1 // b
            if gmin > gmax:
                continue

            err_lo = Fraction(a, b) - alpha_hi
            err_hi = Fraction(a, b) - alpha_lo
            if err_hi <= 0:
                continue
            assert err_lo > 0

            if err_lo >= KMAX / (b*b):
                continue
            worley[(a, b)] = (j, r, s, sign, gmin, gmax, err_lo, err_hi)

survivors = []
fail_ratios = []
for (a, b), meta in worley.items():
    err_lo = meta[-2]
    if err_lo < CMAX:
        survivors.append((a, b, meta))
    else:
        fail_ratios.append((err_lo / CMAX, a, b))

assert len(worley) == 29
assert len(survivors) == 1

a, b, meta = survivors[0]
assert (a, b) == (217_976_794_617, 137_528_045_312)
assert meta[4] == 1 and meta[5] == 1

nearest_fail = min(fail_ratios)
assert (nearest_fail[1], nearest_fail[2]) == (10_439_860_591, 6_586_818_670)
assert nearest_fail[0] > Fraction(2517, 100)

print("mechanical-envelope Worley sharpening: PASS")
print("verified floor:", LOW)
print("KMAX <", float(KMAX))
print("Worley primitive superset count:", len(worley))
print("unique surviving pair:", (a, b))
print("nearest rejected primitive:", (nearest_fail[1], nearest_fail[2]))
print("nearest rejection factor over direct bound:", float(nearest_fail[0]))
