#!/usr/bin/env python3
"""Exact endpoint near-survival / Worley certificate for the first resonance.

For y=N+g with N>2^71 and 0<g<2^33, assume the orbit never falls below N.
If (j,q) is the *first* coefficient-subcritical prefix of y, then proper-prefix
coefficient survival gives R <= q*3^(q-1), hence

    1 - 3^q/2^j < (2^33 + q/3)/2^71.

This forces a Worley approximation |alpha-q/j| < k/j^2 with k<1.436,
alpha=log_3(2).  We enumerate the complete rs<=2 adjacent-convergent
primitive superset and all multiplicities with j<A0.  Every such pair violates
the necessary near-survival inequality.  The first-resonance pair itself is
not excluded by that inequality.

No floating-point arithmetic is used in the assertions.
"""

from fractions import Fraction
from math import gcd

A0 = 114_208_327_604
Q0 = 72_057_431_991
B = 1 << 71
G = 1 << 33
NLOG = 70


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * z ** (2*n + 3) / ((2*n + 3) * (1 - z*z))
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
        assert lo > 0 and hi > 0
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


# ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2).
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3
cf = interval_cf(alpha_lo, alpha_hi, 32)
cv = convergents(cf)

# If 1-exp(-delta) <= H, then delta <= -ln(1-H) <= H/(1-H).
# For every j<A0 and subcritical q, q<=Q0, so H is bounded by HMAX.
HMAX = (Fraction(G, 1) + Fraction(Q0, 3)) / B
UDELTA = HMAX / (1 - HMAX)
KMAX = Fraction(A0 - 1, 1) * UDELTA / l3
assert KMAX < Fraction(1436, 1000)

# Worley-Dujella: rs < 2*KMAX < 2.872, hence integral rs<=2.
pairs = [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)]
worley = {}
for m in range(len(cv) - 1):
    p0, b0 = cv[m]
    p1, b1 = cv[m + 1]
    for r, s in pairs:
        for sign in (-1, 1):
            pp = r*p1 + sign*s*p0
            bb = r*b1 + sign*s*b0
            if pp <= 0 or bb <= 0:
                continue
            d = gcd(pp, bb)
            a, b = pp // d, bb // d  # primitive q/j
            if b >= A0:
                continue

            # Rigorously below alpha.
            err_lo = alpha_lo - Fraction(a, b)
            err_hi = alpha_hi - Fraction(a, b)
            if err_lo <= 0:
                continue

            # Necessary Worley approximation superset.
            if err_lo >= KMAX / (b*b):
                continue
            worley[(a, b)] = (m, r, s, sign, err_lo, err_hi)

assert len(worley) == 23

# For a primitive candidate a/b, an actual pair can be g(a,b), gb<A0.
# Put delta0=b ln2-a ln3.  A rigorous lower bound is DLO.
# Since 1-exp(-x) >= x/(1+x), every actual multiplicity must satisfy
#
#   g*DLO/(1+g*DLO) <= (G + g*a/3)/B.
#
# The difference is concave in real g, so positivity at g=1 and g=gmax
# proves positivity throughout the integer interval.
checked_multiplicity_ranges = 0
for (a, b), meta in worley.items():
    gmax = (A0 - 1) // b
    assert gmax >= 1
    dlo = b*l2 - a*u3
    assert dlo > 0

    def deficit_lower(g: int):
        x = g*dlo
        return x / (1 + x)

    def allowance(g: int):
        return (Fraction(G, 1) + Fraction(g*a, 3)) / B

    assert deficit_lower(1) > allowance(1)
    assert deficit_lower(gmax) > allowance(gmax)
    checked_multiplicity_ranges += 1

assert checked_multiplicity_ranges == 23

# The first-resonance pair itself lies below alpha and is NOT ruled out by
# the same necessary inequality.  Use 1-exp(-delta)<delta and an upper log
# interval to certify allowance at (A0,Q0).
root_delta_hi = A0*u2 - Q0*l3
root_allowance = (Fraction(G, 1) + Fraction(Q0, 3)) / B
assert root_delta_hi < root_allowance

print("PASS endpoint near-survival coefficient wall")
print("KMAX <", float(KMAX))
print("Worley primitive candidates before A0:", len(worley))
print("multiplicity ranges excluded:", checked_multiplicity_ranges)
print("first possible subcritical depth:", A0)
print("first-resonance odd count:", Q0)
