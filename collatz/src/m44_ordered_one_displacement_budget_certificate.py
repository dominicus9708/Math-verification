#!/usr/bin/env python3
"""Exact rational certificate for ordered-one rigidity at the current R1 resonance.

No huge powers 2^A or 3^H are constructed.  The proof uses exact rational
intervals for ln 2 and ln 3, the upper-convergent phase-grid order, a positive
Taylor lower bound for exp(z)-1, and the current m=44 recursive-sufficiency
floor.

It certifies that 126,613,628,699 displaced ordered ones already force more
Archimedean first-crossing defect than the m=44 candidate can afford.  Hence at
least 10,914,416,614 of the H ordered ones remain exactly at their mechanical
Beatty/Christoffel positions.
"""

from fractions import Fraction
from math import gcd

A = 217_976_794_617
H = 137_528_045_312

# Current exact bootstrap floor V_32=4(3^44+3^32)+2.
V32 = 4 * (3**44 + 3**32) + 2
NMIN = V32 + 1

LOG_TERMS = 60
EXP_TERMS = 40
M0 = 126_613_628_699
FIXED_MIN = 10_914_416_614


def log_ratio_bounds(x: Fraction, n: int):
    """Bounds log((1+x)/(1-x)) by a positive atanh series."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2)
        * x ** (2 * n + 3)
        / ((2 * n + 3) * (1 - x * x))
    )
    return s, s + tail


def expm1_lower(z: Fraction, n: int):
    """Positive Taylor lower bound for exp(z)-1, z>=0."""
    assert z >= 0
    term = Fraction(1)
    s = Fraction(0)
    for k in range(1, n + 1):
        term = term * z / k
        s += term
    return s


l2, u2 = log_ratio_bounds(Fraction(1, 3), LOG_TERMS)
l3, u3 = log_ratio_bounds(Fraction(1, 2), LOG_TERMS)

# lambda = A ln 2 - H ln 3 = ln(2^A/3^H).
lambda_lo = A * l2 - H * u3
lambda_hi = A * u2 - H * l3
assert lambda_lo > 0
assert lambda_lo < lambda_hi
assert gcd(A, H) == 1

# Upper-convergent/no-wrap certificate.
# beta=ln3/ln2 and A/H-beta=lambda/(H ln2).  The assertion below gives
# A/H-beta < 1/H^2.  Therefore, for 1<=n<H,
# {n beta} = {n A/H} - n(A/H-beta) with no circular wrap.
assert lambda_hi * H < l2

# Denjoy--Koksma upper bound for the mechanical odd-only correction.
U_CORRECTION = Fraction(H, 1) / (6 * l2) + Fraction(1, 3)

# P=e^lambda>1.  Actual time-expanded defect is
#   D=(c_chr-c)/P,
# c=(P-1)N+Pg, g>=4.
# Use U_CORRECTION/P <= U_CORRECTION and
#   1-P^{-1}=1-e^{-lambda} >= lambda/(1+lambda)
# with the certified lambda lower bound.
rho_lo = lambda_lo / (1 + lambda_lo)
BUDGET_UPPER = U_CORRECTION - NMIN * rho_lo - 4
assert BUDGET_UPPER > 0


def displaced_cost_lower(m: int):
    """Certified lower bound for m displaced ordered ones.

    Each minimally displaced ordered one has cost
        c_l = (1/(3P)) 2^{-theta_l}.
    The phase multiset is dominated by the exact H-grid because A/H is an
    upper convergent with error <1/H^2.  The m cheapest grid terms obey the
    left-Riemann lower bound
        sum >= H(2^(m/H)-1)/(2 ln2).
    We use e^{-lambda} >= 1-lambda_hi, ln2<=u2, and a positive Taylor lower
    bound for 2^(m/H)-1.
    """
    assert 0 <= m <= H
    z_lo = l2 * Fraction(m, H)
    pow2_minus_1_lo = expm1_lower(z_lo, EXP_TERMS)
    return (
        Fraction(H, 1)
        * (1 - lambda_hi)
        * pow2_minus_1_lo
        / (6 * u2)
    )


lb_prev = displaced_cost_lower(M0 - 1)
lb_here = displaced_cost_lower(M0)

# This pins the first excluded integer for THIS certified lower bound.
assert lb_prev <= BUDGET_UPPER
assert lb_here > BUDGET_UPPER

max_displaced = M0 - 1
fixed_min = H - max_displaced
assert fixed_min == FIXED_MIN

print("m44 ordered-one displacement certificate: PASS")
print("A =", A)
print("H =", H)
print("V32 =", V32)
print("NMIN =", NMIN)
print("lambda interval floats =", float(lambda_lo), float(lambda_hi))
print("upper-convergent no-wrap = PASS")
print("budget upper =", float(BUDGET_UPPER))
print("LB(M0-1) =", float(lb_prev))
print("LB(M0)   =", float(lb_here))
print("max displaced ordered ones =", max_displaced)
print("minimum fixed mechanical ordered ones =", fixed_min)
print("minimum fixed fraction =", float(Fraction(fixed_min, H)))
