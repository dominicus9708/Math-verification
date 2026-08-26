#!/usr/bin/env python3
"""Exact certificate for the resonance-scale promotion after two J0 debits.

After two consecutive local J0/R0 crossings, the repaired gap-debit theorem
gives a current endpoint X=N+d with

    0 <= d < 2*2^33,   N > 2^71.

If (j,q) is the first coefficient-subcritical prefix from X, the standard
proper-prefix correction bound gives the necessary near-survival inequality

    1-3^q/2^j < (2*2^33+q/3)/2^71.

For j<A0=114,208,327,604 this yields a Worley constant K<1.814, so rs<2K
forces rs<=3.  The script enumerates the complete adjacent-convergent primitive
superset with rs<=3, then excludes every positive multiplicity range by exact
rational logarithm inequalities and concavity.  The pair (A0,Q0) itself is not
excluded by the same necessary inequality.

Thus, after two J0 gap debits, the first possible coefficient-subcritical
prefix is promoted from J0 to the A0 scale.

No floating-point arithmetic is used in assertions.  The external theorem is
the standard Worley-Dujella adjacent-convergent approximation theorem already
used elsewhere in this repository.  This is not a proof of Collatz.
"""

from fractions import Fraction
from math import gcd

BASE = 1 << 71
G = 1 << 33
A0 = 114_208_327_604
Q0 = 72_057_431_991
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


def interval_cf(lo: Fraction, hi: Fraction, n: int):
    out = []
    for _ in range(n):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1
        out.append(a0)
        lo -= a0
        hi -= a0
        assert lo > 0 and hi > 0
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


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3
cf = interval_cf(alpha_lo, alpha_hi, 28)
cv = convergents(cf)

# Uniform approximation constant for j<A0, q<=Q0.
HMAX = (Fraction(2 * G, 1) + Fraction(Q0, 3)) / BASE
UDELTA = HMAX / (1 - HMAX)
KMAX = Fraction(A0 - 1, 1) * UDELTA / l3
assert KMAX < Fraction(1814, 1000)
assert 2 * KMAX < Fraction(3628, 1000)

# Since rs is a nonnegative integer and rs<2K<3.628, rs<=3.
rs_pairs = [
    (1, 0), (0, 1),
    (1, 1),
    (1, 2), (2, 1),
    (1, 3), (3, 1),
]

worley = {}
for n in range(len(cv) - 1):
    p0, b0 = cv[n]
    p1, b1 = cv[n + 1]
    for r, s in rs_pairs:
        for sign in (-1, 1):
            pp = r * p1 + sign * s * p0
            bb = r * b1 + sign * s * b0
            if pp <= 0 or bb <= 0:
                continue
            d = gcd(pp, bb)
            a, b = pp // d, bb // d
            if b >= A0:
                continue

            # Rigorously below alpha: coefficient-subcritical side.
            err_lo = alpha_lo - Fraction(a, b)
            if err_lo <= 0:
                continue

            # Necessary Worley approximation superset.
            if err_lo >= KMAX / (b * b):
                continue
            worley[(a, b)] = (n, r, s, sign)

assert len(worley) == 27

# Exclude every multiplicity with mb<A0.  As in the earlier repaired endpoint
# certificate, use 1-exp(-mD)>=mD/(1+mD); after subtracting the linear
# allowance the resulting function is concave, so endpoint positivity closes
# the full multiplicity interval.
checked = 0
for a, b in worley:
    dlo = b * l2 - a * u3
    assert dlo > 0
    mmax = (A0 - 1) // b
    assert mmax >= 1

    def deficit_lower(m: int):
        x = m * dlo
        return x / (1 + x)

    def allowance(m: int):
        return (Fraction(2 * G, 1) + Fraction(m * a, 3)) / BASE

    assert deficit_lower(1) > allowance(1)
    assert deficit_lower(mmax) > allowance(mmax)
    checked += 1

assert checked == 27

# The A0/Q0 pair itself is on the subcritical side and is not excluded by the
# same necessary inequality.  1-exp(-delta)<delta suffices.
delta_A0_hi = A0 * u2 - Q0 * l3
A0_allowance = (Fraction(2 * G, 1) + Fraction(Q0, 3)) / BASE
assert delta_A0_hi < A0_allowance

print("PASS post-two-J0 next-scale A0 certificate")
print("Worley_KMAX", float(KMAX))
print("primitive_candidate_ranges_excluded", checked)
print("first_possible_promoted_depth", A0)
print("first_possible_promoted_odd_count", Q0)
