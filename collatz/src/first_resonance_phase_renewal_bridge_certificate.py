#!/usr/bin/env python3
"""Exact continued-fraction certificate for the first-resonance phase-renewal bridge.

Let alpha=log_3(2), b(n)=ceil(alpha*n), and let

    (A0,Q0)=(114208327604,72057431991)

be the repaired first lower resonance.  Put eps0=alpha*A0-Q0>0.
The next opposite-sided convergent is

    (K1,P1)=(103768467013,65470613321),

with eta1=P1-alpha*K1>0.  The preceding convergent denominator is
10439860591.  Exact rational log intervals certify

    0 < eta1 < eps0 < ||10439860591*alpha||.

By the standard best-approximation-of-the-second-kind theorem for continued
fractions, every 1<=k<K1 has ||k*alpha||>eps0.  Therefore

    b(A0+k)=Q0+b(k)              for 1<=k<K1,
    b(A0+K1)=Q0+b(K1)+1.

The endpoint K1 combines with A0 to give the next lower convergent

    (A2,Q2)=(217976794617,137528045312).

The script certifies only the exact continued-fraction and interval data used
by that analytic lemma; it does not replace the classical best-approximation
theorem and it is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

A0 = 114_208_327_604
Q0 = 72_057_431_991
K1 = 103_768_467_013
P1 = 65_470_613_321
A2 = 217_976_794_617
Q2 = 137_528_045_312
PREV_DEN = 10_439_860_591
PREV_NUM = 6_586_818_670
NLOG = 80


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


# ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2).
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3

cf = interval_cf(alpha_lo, alpha_hi, 26)
cv = convergents(cf)

assert cv[22] == (PREV_NUM, PREV_DEN)
assert cv[23] == (P1, K1)
assert cv[24] == (Q2, A2)

# eps0 = alpha*A0-Q0, positive lower-resonance phase defect.
eps0_lo = A0 * alpha_lo - Q0
eps0_hi = A0 * alpha_hi - Q0

# eta1 = P1-alpha*K1, positive upper-resonance phase defect.
eta1_lo = P1 - K1 * alpha_hi
eta1_hi = P1 - K1 * alpha_lo

# The preceding convergent is below alpha, so this is its absolute error.
prev_gap_lo = PREV_DEN * alpha_lo - PREV_NUM
prev_gap_hi = PREV_DEN * alpha_hi - PREV_NUM

# The sum pair is the next lower convergent.
eps2_lo = A2 * alpha_lo - Q2
eps2_hi = A2 * alpha_hi - Q2

assert 0 < eta1_lo <= eta1_hi
assert eta1_hi < eps0_lo <= eps0_hi
assert eps0_hi < prev_gap_lo <= prev_gap_hi

assert A0 + K1 == A2
assert Q0 + P1 == Q2
assert 0 < eps2_lo <= eps2_hi

# eps2 = eps0-eta1 at the exact alpha; interval enclosure cross-check.
assert eps2_lo >= eps0_lo - eta1_hi
assert eps2_hi <= eps0_hi - eta1_lo

# Sign checks for the three resonant coefficients.
# Q0/A0 and Q2/A2 lie below alpha; P1/K1 lies above alpha.
assert Q0 < A0 * alpha_lo
assert P1 > K1 * alpha_hi
assert Q2 < A2 * alpha_lo

print("PASS first-resonance phase-renewal bridge certificate")
print("preceding_convergent", PREV_NUM, PREV_DEN)
print("upper_bridge_convergent", P1, K1)
print("next_lower_convergent", Q2, A2)
print("eta1_upper", float(eta1_hi))
print("eps0_lower", float(eps0_lo))
print("preceding_gap_lower", float(prev_gap_lo))
print("eps2_upper", float(eps2_hi))
