#!/usr/bin/env python3
"""Exact certificate for the A0/J0 activation ladder.

Let G=2^33 and N>2^71 be a hypothetical minimal-counterexample root.
Suppose a local endpoint X=N+d has d<2G and repeatedly realizes the
first coefficient-subcritical resonance

    A0/Q0 = 114208327604 / 72057431991.

Each genuine A0 first crossing can increase d by less than a fixed exact
quantity a<0.5023 G.  For the previous lower convergent

    J0/R0 = 10439860591 / 6586818670,

a first crossing at the multiple m(J0,R0), 1<=m<=10, consumes more than
an exact debit D_m.  Since 10 J0 < A0 < 11 J0, these are all J0 multiples
that can occur before A0.

The certificate proves:
  * after two consecutive A0 returns from d<2G, the only nonexcluded
    subcritical pair below A0 is exactly (J0,R0), not any multiple m>=2;
  * if that J0 crossing occurs, the macro A0,A0,J0 sends d below 0.478 G;
  * one J0 debit dominates five A0 credits;
  * more generally D_m > 2.526 m G for 1<=m<=10;
  * under an A0-only run starting from d<2G, the multiple m J0 cannot even
    become admissible before the (5m-3)-rd A0 return.

The continued-fraction reduction uses the classical Worley-Dujella theorem;
all numerical/logarithmic assertions below are exact rational inequalities.
This is not a proof of the Collatz conjecture.
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

# Uniform A0 credit bound from the mechanical first-crossing envelope.
delta_A_lo = A0 * l2 - Q0 * u3
assert delta_A_lo > 0
loss_A_lower = BASE * delta_A_lo / (1 + delta_A_lo)
S_A_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
A_credit = S_A_upper - loss_A_lower
assert A_credit < Fraction(5023, 10000) * G

# J0 primitive debit and the five-credit domination margin.
delta_J_lo = J0 * l2 - R0 * u3
assert delta_J_lo > 0
J_debit = BASE * delta_J_lo / (1 + delta_J_lo) - Fraction(R0, 3)
assert J_debit > Fraction(2527, 1000) * G
assert 5 * A_credit < J_debit
assert J_debit - 5 * A_credit > Fraction(15, 1000) * G

# Two A0 returns from d<2G.
H2 = 2 * G + 2 * A_credit
assert H2 < Fraction(3005, 1000) * G

# Complete Worley-Dujella audit below A0 at this H2 gap.
HMAX = (H2 + Fraction(Q0, 3)) / BASE
UDELTA = HMAX / (1 - HMAX)
KMAX = Fraction(A0 - 1, 1) * UDELTA / l3
assert KMAX < Fraction(2195, 1000)
assert 2 * KMAX < Fraction(439, 100)

# Since rs < 4.39, integral rs is at most 4.
rs_pairs = []
for r in range(5):
    for s in range(5):
        if r == 0 and s == 0:
            continue
        if r * s <= 4:
            rs_pairs.append((r, s))

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

assert len(worley) == 28

survivors = []
for a, b in worley:
    dlo = b * l2 - a * u3
    assert dlo > 0
    mmax = (A0 - 1) // b
    assert mmax >= 1

    def deficit_lower(m: int):
        x = m * dlo
        return x / (1 + x)

    def allowance(m: int):
        return (H2 + Fraction(m * a, 3)) / BASE

    # Concavity of deficit_lower(m)-allowance(m): if both endpoints are
    # positive, the complete integer multiplicity range is excluded.
    if deficit_lower(1) > allowance(1) and deficit_lower(mmax) > allowance(mmax):
        continue

    # The only endpoint-uncertain primitive is J0/R0 and it has only ten
    # multiples below A0, so inspect that complete range exactly.
    assert (a, b) == (R0, J0)
    assert mmax == 10
    for m in range(1, mmax + 1):
        if deficit_lower(m) <= allowance(m):
            survivors.append((m * a, m * b, m))

assert survivors == [(R0, J0, 1)]

# J0 itself is genuinely nonexcluded by the necessary wall at H2.
delta_J_hi = J0 * u2 - R0 * l3
assert delta_J_hi > 0
assert delta_J_hi < (H2 + Fraction(R0, 3)) / BASE

# If A0,A0,J0 occurs, the gap is forced back below 0.478 G.
post_AAJ = 2 * G + 2 * A_credit - J_debit
assert post_AAJ < Fraction(478, 1000) * G

# Multiplicity debit ladder.  These are all J0 multiples before A0.
assert 10 * J0 < A0 < 11 * J0
activation = []
for m in range(1, 11):
    x = m * delta_J_lo
    Dm = BASE * x / (1 + x) - Fraction(m * R0, 3)
    assert Dm > Fraction(2526 * m, 1000) * G
    assert 5 * m * A_credit < Dm

    # Minimal k for which the coarse A0-only envelope 2G+k*A_credit is no
    # longer strictly below the mJ0 necessary-gap threshold Dm.
    k = 0
    while 2 * G + k * A_credit < Dm:
        k += 1
    assert k == 5 * m - 3
    activation.append((m, k))

print("PASS A0/J0 activation ladder certificate")
print("A0_credit_over_G", float(A_credit / G))
print("J0_debit_over_G", float(J_debit / G))
print("five_A_credit_over_G", float(5 * A_credit / G))
print("two_A_gap_over_G", float(H2 / G))
print("post_A0_A0_J0_gap_over_G", float(post_AAJ / G))
print("only_sub_A0_candidate_after_two_A", survivors)
print("activation_ladder", activation)
