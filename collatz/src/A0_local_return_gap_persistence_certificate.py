#!/usr/bin/env python3
"""Exact certificate for one promoted A0 return and persistence of the A0 wall.

Starting state after two J0 debits:
    X=N+d,  0<=d<2*G,  G=2^33, N>2^71.
Assume the first local coefficient-subcritical block is the promoted pair
    (A0,Q0)=(114208327604,72057431991).

Using the first-crossing mechanical correction ceiling and exact log bounds,
the new endpoint gap d' satisfies
    d' < d + 0.51 G < 2.51 G.

The J0 necessary-gap threshold is >2.527 G, so J0 remains impossible after
this A0 return.  A complete Worley-Dujella rs<=4 audit at gap 2.51 G excludes
all subcritical pairs below A0 again.  Hence the next possible local crossing
is still A0.

No floating-point arithmetic is used in assertions.  This is not a proof of
Collatz.
"""

from fractions import Fraction
from math import gcd

BASE = 1 << 71
G = 1 << 33
J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
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

# A0 first-crossing normalized correction ceiling.
delta_A_lo = A0 * l2 - Q0 * u3
assert delta_A_lo > 0
loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
A_gap_increase = S_A_upper - loss_A_lower
assert A_gap_increase < Fraction(51, 100) * G

# Hence d<2G -> d'<2.51G.
H1 = Fraction(251, 100) * G
assert 2 * G + A_gap_increase < H1

# J0's exact necessary-gap threshold exceeds 2.527G, in particular 2.51G.
delta_J_lo = J0 * l2 - R0 * u3
assert delta_J_lo > 0
loss_J_lower = BASE * delta_J_lo / (1 + delta_J_lo)
J_threshold_lower = loss_J_lower - Fraction(R0, 3)
assert J_threshold_lower > Fraction(2527, 1000) * G
assert H1 < J_threshold_lower

# Re-audit every possible subcritical pair below A0 with the enlarged H1 gap.
HMAX = (H1 + Fraction(Q0, 3)) / BASE
UDELTA = HMAX / (1 - HMAX)
KMAX = Fraction(A0 - 1, 1) * UDELTA / l3
assert KMAX < Fraction(2007, 1000)
assert 2 * KMAX < Fraction(4014, 1000)

# rs<4.014 implies integral rs<=4.
rs_pairs = [
    (1, 0), (0, 1), (1, 1),
    (1, 2), (2, 1), (1, 3), (3, 1),
    (1, 4), (4, 1), (2, 2),
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
            err_lo = alpha_lo - Fraction(a, b)
            if err_lo <= 0:
                continue
            if err_lo >= KMAX / (b * b):
                continue
            worley[(a, b)] = (n, r, s, sign)

assert len(worley) == 27

for a, b in worley:
    dlo = b * l2 - a * u3
    assert dlo > 0
    mmax = (A0 - 1) // b
    assert mmax >= 1

    def deficit_lower(m: int):
        x = m * dlo
        return x / (1 + x)

    def allowance(m: int):
        return (H1 + Fraction(m * a, 3)) / BASE

    assert deficit_lower(1) > allowance(1)
    assert deficit_lower(mmax) > allowance(mmax)

# A0 itself remains nonexcluded.
delta_A_hi = A0 * u2 - Q0 * l3
A_allowance = (H1 + Fraction(Q0, 3)) / BASE
assert delta_A_hi < A_allowance

print("PASS A0 local-return gap persistence certificate")
print("A0_gap_increase_over_G", float(A_gap_increase / G))
print("post_A0_gap_bound_over_G", 2.51)
print("J0_threshold_lower_over_G", float(J_threshold_lower / G))
print("Worley_KMAX_at_2p51G", float(KMAX))
print("primitive_ranges_excluded", len(worley))
print("next_possible_scale_remains_A0", A0, Q0)
