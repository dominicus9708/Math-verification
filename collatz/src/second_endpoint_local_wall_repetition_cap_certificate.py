#!/usr/bin/env python3
"""Exact certificate for the second-endpoint local coefficient wall and repetition cap.

Input from the repaired branch:
  N > 2^71 and every future orbit value is >= N;
  a current tail endpoint X=N+d has 0<=d<7*2^33.

If (j,q) is the first coefficient-subcritical prefix from X, proper-prefix
coefficient survival gives R<=q*3^(q-1), hence the necessary inequality

  1-3^q/2^j <= (d+q/3)/X < (7*2^33+q/3)/2^71.

For j<J0=10,439,860,591 this forces, by Legendre's theorem, the reduced q/j
to be a continued-fraction convergent of alpha=log_3(2).  Exact rational
log intervals and a concavity check exclude every positive multiple of every
lower convergent before J0.  At j=J0 the unique surviving lower convergent is
R0/J0=6,586,818,670/10,439,860,591.

For an actual J0/R0 crossing, the same exact log bounds show that the gap to
N drops by more than (5/2)*2^33.  Therefore from an initial gap <7*2^33 this
same local resonance can occur at most twice consecutively.

No floating-point arithmetic is used in assertions.  The only external
mathematical input is the classical Legendre continued-fraction theorem.
This is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

BASE = 1 << 71
G = 1 << 33
J0 = 10_439_860_591
R0 = 6_586_818_670
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


# ln2 and ln3 exact rational enclosures.
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))
alpha_lo = l2 / u3
alpha_hi = u2 / l3

cf = interval_cf(alpha_lo, alpha_hi, 26)
cv = convergents(cf)
assert (R0, J0) in cv

# For a hypothetical first subcritical pair j<J0, q<=R0 and
# H=(7G+q/3)/BASE <= HMAX.  Then delta<=H/(1-H), and
# |alpha-q/j| < KMAX/j^2 with KMAX<1/2.  Legendre applies after reduction.
HMAX = (Fraction(7 * G, 1) + Fraction(R0, 3)) / BASE
UDELTA = HMAX / (1 - HMAX)
KMAX = Fraction(J0 - 1, 1) * UDELTA / l3
assert KMAX < Fraction(1, 2)

# Rigorously lower convergents before R0/J0.
lower_before = []
for a, b in cv:
    if a <= 0 or b >= J0:
        continue
    if Fraction(a, b) < alpha_lo:
        lower_before.append((a, b))

expected = [
    (1, 2),
    (5, 8),
    (41, 65),
    (306, 485),
    (15_601, 24_727),
    (79_335, 125_743),
    (190_537, 301_994),
    (10_781_274, 17_087_915),
    (171_928_773, 272_500_658),
    (397_573_379, 630_138_897),
]
assert lower_before == expected

# If q/j reduces to a/b, write (q,j)=m(a,b).  Let
# D0=b ln2-a ln3>0.  Then
# 1-exp(-mD0) >= mD0/(1+mD0).
# Subtracting the affine allowance gives a concave function of real m,
# so positivity at m=1 and the largest permitted m excludes the whole range.
checked = 0
for a, b in lower_before:
    dlo = b * l2 - a * u3
    assert dlo > 0
    mmax = (J0 - 1) // b
    assert mmax >= 1

    def deficit_lower(m: int):
        x = m * dlo
        return x / (1 + x)

    def allowance(m: int):
        return (Fraction(7 * G, 1) + Fraction(m * a, 3)) / BASE

    assert deficit_lower(1) > allowance(1)
    assert deficit_lower(mmax) > allowance(mmax)
    checked += 1

assert checked == len(expected)

# At J0 the current lower convergent itself is not ruled out by the necessary
# inequality: 1-exp(-delta)<delta and delta is below the allowance.
delta0_hi = J0 * u2 - R0 * l3
current_allowance = (Fraction(7 * G, 1) + Fraction(R0, 3)) / BASE
assert delta0_hi < current_allowance

# Gap decrement at an actual J0/R0 crossing.
# With delta0=J0 ln2-R0 ln3>0 and C=exp(-delta0),
# 1-C >= delta0/(1+delta0).  Since X=N+d and N>BASE,
# the new gap d' obeys
#   d' < d + R0/3 - BASE*delta0/(1+delta0).
# Certify the fixed decrement exceeds (5/2)G.
delta0_lo = J0 * l2 - R0 * u3
assert delta0_lo > 0
loss_lower = delta0_lo / (1 + delta0_lo)
decrement = BASE * loss_lower - Fraction(R0, 3)
assert decrement > Fraction(5, 2) * G

# Consecutive-gap envelopes: <7G -> <9G/2 -> <2G -> contradiction on third.
assert Fraction(7, 1) * G - decrement < Fraction(9, 2) * G
assert Fraction(9, 2) * G - decrement < Fraction(2, 1) * G
assert Fraction(2, 1) * G - decrement < 0

print("PASS second-endpoint local wall / repetition cap certificate")
print("Legendre_KMAX", float(KMAX))
print("lower_convergents_excluded", checked)
print("first_possible_local_crossing", J0, R0)
print("fixed_gap_decrement_over_2^33", float(decrement / G))
print("consecutive_J0_crossings_cap", 2)
