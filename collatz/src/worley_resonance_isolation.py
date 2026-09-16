#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

Q0 = 72_057_431_991
Q1 = 137_528_045_312
LOW = 4 * 3**44 + 2
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

# If a paradoxical first crossing with q in (Q0,Q1] has x >= LOW, then
# |alpha - sigma/q| < C(q).  After reduction sigma/q=a/b with q=g*b,
# the Worley constant is at most the rational KMAX below.
KMAX = Fraction(Q1 * (7*Q1 + 1), 1) / (24 * LOW * l2)
assert KMAX < Fraction(2021, 1000)

# Direct approximation bound, maximized over q in (Q0,Q1].
CMAX = (Fraction(7, 1) + Fraction(1, Q0 + 1)) / (24 * LOW * l2)

# Worley--Dujella: rs < 2 KMAX < 4.042.  Since rs is integral, rs <= 4.
# Zero coefficients only reproduce a convergent after reduction, so one
# representative for each zero case is enough.
pairs = [
    (1, 0), (0, 1),
    (1, 1), (1, 2), (2, 1),
    (1, 3), (3, 1),
    (1, 4), (4, 1), (2, 2),
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

            # At least one multiple q=g*b must lie in the target interval.
            gmin = Q0 // b + 1
            gmax = Q1 // b
            if gmin > gmax:
                continue

            err_lo = Fraction(a, b) - alpha_hi
            err_hi = Fraction(a, b) - alpha_lo
            if err_hi <= 0:
                continue
            assert err_lo > 0

            # Necessary Worley superset condition.
            if err_lo >= KMAX / (b*b):
                continue
            worley[(a, b)] = (j, r, s, sign, gmin, gmax, err_lo, err_hi)

# Apply the stronger direct first-crossing/paradoxical necessary condition.
survivors = []
fail_ratios = []
for (a, b), meta in worley.items():
    err_lo = meta[-2]
    if err_lo < CMAX:
        survivors.append((a, b, meta))
    else:
        fail_ratios.append((err_lo / CMAX, a, b))

assert len(worley) == 30
assert len(survivors) == 1

a, b, meta = survivors[0]
assert (a, b) == (217_976_794_617, 137_528_045_312)
assert meta[4] == 1 and meta[5] == 1

nearest_fail = min(fail_ratios)
assert (nearest_fail[1], nearest_fail[2]) == (124_648_188_195, 78_644_250_661)
assert nearest_fail[0] > Fraction(268, 100)

print("rational Worley isolation: PASS")
print("certified continued-fraction terms:", cf[:25])
print("KMAX <", float(KMAX))
print("Worley primitive superset count:", len(worley))
print("unique surviving reduced pair:", (a, b))
print("nearest rejected primitive:", (nearest_fail[1], nearest_fail[2]))
print("nearest rejection factor over CMAX:", float(nearest_fail[0]))
