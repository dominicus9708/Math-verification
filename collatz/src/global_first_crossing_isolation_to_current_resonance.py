#!/usr/bin/env python3
"""Exact global first-crossing isolation through the current resonance.

For every odd-count denominator 1 <= q <= H_CURRENT, this certificate combines

  * the mechanical/Christoffel first-crossing correction envelope,
  * the current verified floor V_33,
  * Worley--Dujella with rs <= 3,
  * exact rational intervals for ln 2 and ln 3,

to prove that the only coefficient pair which can support a first-crossing
minimal-counterexample candidate at N >= V_33+1 is

    (A,q) = (217976794617, 137528045312).

No floating-point comparisons are used in the assertions.
"""

from fractions import Fraction
from math import gcd

H_CURRENT = 137_528_045_312
A_CURRENT = 217_976_794_617
NMIN = 4 * (3**44 + 3**33) + 3
NLOG = 70


def log_ratio_bounds(x: Fraction, n: int):
    # ln((1+x)/(1-x)) = 2 sum x^(2k+1)/(2k+1)
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
        lo, hi = 1 / hi, 1 / lo
    return out


def convergents(cf):
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out = []
    for a in cf:
        p = a * p1 + p2
        q = a * q1 + q2
        out.append((p, q))
        p2, p1 = p1, p
        q2, q1 = q1, q
    return out


# ln 2 uses x=1/3; ln 3 uses x=1/2.
l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)

# alpha = log_2 3.
alpha_lo = l3 / u2
alpha_hi = u3 / l2
cf = interval_cf(alpha_lo, alpha_hi, 35)
cv = convergents(cf)

# If a first-crossing survivor exists at N>=NMIN, the mechanical envelope gives
#
#   N(P-1) <= q/(6 ln2)+1/3,
#
# and P-1 >= q ln2 (A/q-alpha). Therefore
#
#   |A/q-alpha| < K(q)/q^2.
#
# K(q) is increasing in q, so H_CURRENT gives a global upper bound.
KMAX = (
    Fraction(H_CURRENT * H_CURRENT, 1) / (6 * NMIN * l2 * l2)
    + Fraction(H_CURRENT, 1) / (3 * NMIN * l2)
)
assert KMAX < Fraction(1666, 1000)

# Worley--Dujella: rs < 2*KMAX < 3.332, hence integral rs<=3.
rs_pairs = [
    (1, 0), (0, 1),
    (1, 1), (1, 2), (2, 1),
    (1, 3), (3, 1),
]

primitive = {}
for j in range(len(cv) - 1):
    p0, b0 = cv[j]
    p1, b1 = cv[j + 1]
    for r, s in rs_pairs:
        for sign in (-1, 1):
            pp = r * p1 + sign * s * p0
            bb = r * b1 + sign * s * b0
            if pp <= 0 or bb <= 0 or bb > H_CURRENT:
                continue
            d = gcd(pp, bb)
            a, b = pp // d, bb // d

            # Keep only upper approximants that can satisfy the Worley error.
            err_lo = Fraction(a, b) - alpha_hi
            err_hi = Fraction(a, b) - alpha_lo
            if err_hi <= 0:
                continue
            if err_lo > 0 and err_lo >= KMAX / (b * b):
                continue
            primitive[(a, b)] = (j, r, s, sign)

# Expand non-reduced multiples only as far as they can remain a first crossing.
# For A=g*a, q=g*b we need 0 < A-q*alpha < 1.
actual_first_crossings = []
for (a, b), meta in primitive.items():
    diff_lo = Fraction(a, 1) - b * alpha_hi
    diff_hi = Fraction(a, 1) - b * alpha_lo
    if diff_hi <= 0:
        continue

    gmax = H_CURRENT // b
    if diff_lo > 0:
        # strict g*diff_lo < 1
        gmax = min(gmax, (diff_lo.denominator - 1) // diff_lo.numerator)

    for g in range(1, gmax + 1):
        d_lo = g * diff_lo
        d_hi = g * diff_hi
        if d_hi <= 0 or d_lo >= 1:
            continue
        # With 70 log terms every retained comparison is separated.
        assert d_lo > 0

        A = g * a
        q = g * b

        # Exact lower bound on ln P = A ln2 - q ln3.
        logP_lo = A * l2 - q * u3
        assert logP_lo > 0

        # Exact upper bound on the mechanical first-crossing correction.
        S_upper = Fraction(q, 1) / (6 * l2) + Fraction(1, 3)

        actual_first_crossings.append(
            (A, q, NMIN * logP_lo <= S_upper)
        )

survivors = [(A, q) for A, q, ok in actual_first_crossings if ok]
assert survivors == [(A_CURRENT, H_CURRENT)]

print("global first-crossing isolation: PASS")
print("verified lower start:", NMIN)
print("KMAX <", float(KMAX))
print("Worley primitive upper candidates:", len(primitive))
print("actual first-crossing multiples tested:", len(actual_first_crossings))
print("unique surviving coefficient pair:", survivors[0])
