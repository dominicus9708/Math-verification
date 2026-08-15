#!/usr/bin/env python3
"""Universal balanced-Hensel transition threshold certificate.

This file compresses the transition-band magnitude calculation for gate cubes
    1^F (01/10)^J 0.

For a positive integer predecessor credit delta, the normalized initial Hensel
residual is exactly U_0 = -8 delta (before modular wrap).  Writing x_n=-U_n>0,
the balanced recurrence becomes the universal integer map

    x_{n+1} = 4 * floor((x_n+1)/3),    x_0 = 8 delta.

At transition width h, after n=J-h low-Hensel lifts, the required boundary
correction magnitude is

    T_h(delta) = 2^(3h-2) x_{J-h}(delta),

provided this representative lies below half the ternary modulus.  The exact
boundary capacity of an arbitrary length-3h, weight-2h binary transition block is

    M_h = (2^h-1)(9^h-4^h).

The map x -> 4 floor((x+1)/3) is monotone, so delta=1 minimizes T_h among all
positive credits.  Hence one universal orbit replaces a bounded-credit scan.

For x_n>=8,

    T_h/T_{h-1} = 8 x_{J-h}/x_{J-h+1} <= 7,

while M_h/M_{h-1}>18 for h>=2.  Therefore M_h/T_h is strictly increasing and
the magnitude barrier has at most one crossing in the no-wrap regime.

The normalized orbit y_n=(3/4)^n x_n converges to kappa(delta), with exact tail
bound

    |x_n - kappa(delta) (4/3)^n| <= 4.

For delta=1 this gives the asymptotic threshold law

    h_*(J) = J log_3(4/3) + log_3(kappa_1/4) + o(1).

All threshold claims printed below are nevertheless checked by exact integer
arithmetic, not by floating-point asymptotics.
"""

from fractions import Fraction
from decimal import Decimal, getcontext
import argparse
import math

CASES = (
    ("G81-neutral", 404, 567, 150),
    ("G81-one-slack", 402, 568, 150),
    ("G82-neutral", 409, 574, 151),
    ("G82-one-slack", 407, 575, 152),
    ("G13-neutral", 5245, 7390, 1936),
    ("G13-one-slack", 5243, 7391, 1937),
    ("G14-neutral", 5648, 7958, 2085),
    ("G14-one-slack", 5646, 7959, 2085),
)

MAX_CREDIT = 397


def step(x: int) -> int:
    assert x >= 0
    return 4 * ((x + 1) // 3)


def orbit(delta: int, n: int) -> int:
    x = 8 * delta
    for _ in range(n):
        x = step(x)
    return x


def orbit_table(delta: int, n: int):
    xs = [8 * delta]
    for _ in range(n):
        xs.append(step(xs[-1]))
    return xs


def capacity(h: int) -> int:
    return (2**h - 1) * (9**h - 4**h)


def target_from_table(xs, J: int, h: int) -> int:
    assert 1 <= h <= J
    return (1 << (3 * h - 2)) * xs[J - h]


def exact_threshold(J: int, xs=None) -> int | None:
    if xs is None:
        xs = orbit_table(1, J)
    previous_ratio_pass = False
    for h in range(1, J + 1):
        passed = capacity(h) >= target_from_table(xs, J, h)
        if passed:
            return h
        previous_ratio_pass = passed
    return None


def kappa_interval(delta: int, n: int = 250):
    """Exact rational interval from |kappa-y_n| <= 4(3/4)^n."""
    x = orbit(delta, n)
    den = 4**n
    scale = 3**n
    lo = Fraction((x - 4) * scale, den)
    hi = Fraction((x + 4) * scale, den)
    return lo, hi


def decimal_fraction(q: Fraction, digits: int = 60) -> Decimal:
    getcontext().prec = digits
    return Decimal(q.numerator) / Decimal(q.denominator)


def verify_monotone_credit_map(limit: int = MAX_CREDIT, depth: int = 64):
    # Finite regression only.  The mathematical monotonicity follows directly
    # because floor((x+1)/3) is nondecreasing.
    prev = None
    for delta in range(1, limit + 1):
        x = orbit(delta, depth)
        if prev is not None:
            assert prev <= x
        prev = x


def verify_capacity_growth(max_h: int = 100):
    for h in range(2, max_h + 1):
        # Exact identity reduces this to 4*9^h > 9*4^h.
        assert capacity(h) > 18 * capacity(h - 1)


def verify_target_growth_bound(xs, J: int, h0: int, h1: int):
    # For the delta=1 orbit x>=8.  Residue-class inspection gives
    # 8*x_n/x_(n+1) <= 7, hence T_h <= 7 T_(h-1).
    for h in range(max(2, h0), h1 + 1):
        n = J - h
        x = xs[n]
        xp = xs[n + 1]
        assert x >= 8
        assert 8 * x <= 7 * xp
        assert target_from_table(xs, J, h) <= 7 * target_from_table(xs, J, h - 1)


def verify_case(name: str, F: int, J: int, expected: int):
    xs1 = orbit_table(1, J)
    got = exact_threshold(J, xs1)
    assert got == expected, (name, got, expected)

    # Exact single-crossing neighborhood.
    verify_target_growth_bound(xs1, J, max(2, expected - 8), min(J, expected + 8))
    assert capacity(expected - 1) < target_from_table(xs1, J, expected - 1)
    assert capacity(expected) >= target_from_table(xs1, J, expected)

    # No-wrap check for the largest bounded positive credit at the crossing.
    x397 = orbit(MAX_CREDIT, J - expected)
    T397 = (1 << (3 * expected - 2)) * x397
    modulus = 3 ** (F + expected)
    assert 2 * T397 < modulus, (name, "modular wrap")

    print(name, "J", J, "exact_hstar", got,
          "continuous_predictor", J * math.log(4/3, 3) + KAPPA_OFFSET)


def scan_predictor(max_J: int):
    """Compare exact h_*(J) with ceil(d J+c) using exact thresholds.

    The predictor uses a floating value only to nominate one integer.  Every
    accepted/mismatched classification is then checked with exact integers.
    """
    xs = orbit_table(1, max_J)
    max_h = math.ceil(SLOPE * max_J + KAPPA_OFFSET) + 3
    Ms = [0] * (max_h + 1)
    p2 = p4 = p9 = 1
    for h in range(1, max_h + 1):
        p2 *= 2
        p4 *= 4
        p9 *= 9
        Ms[h] = (p2 - 1) * (p9 - p4)

    mismatches = []
    for J in range(2, max_J + 1):
        hp = max(1, math.ceil(SLOPE * J + KAPPA_OFFSET))
        pass_hp = Ms[hp] >= target_from_table(xs, J, hp)
        pass_prev = False if hp == 1 else Ms[hp - 1] >= target_from_table(xs, J, hp - 1)
        if not (pass_hp and not pass_prev):
            # Resolve the exact threshold only for the rare mismatch.
            exact = exact_threshold(J, xs)
            mismatches.append((J, exact, hp))
    print("predictor_scan", "max_J", max_J, "mismatches", mismatches)


# Certified kappa_1 interval first; midpoint is used only for display/predictor.
KAPPA_LO, KAPPA_HI = kappa_interval(1, 250)
KAPPA_MID = (KAPPA_LO + KAPPA_HI) / 2
KAPPA_FLOAT = float(KAPPA_MID)
SLOPE = math.log(4/3, 3)
KAPPA_OFFSET = math.log(KAPPA_FLOAT / 4, 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", type=int, default=0,
                        help="optional exact predictor scan through this J")
    args = parser.parse_args()

    verify_monotone_credit_map()
    verify_capacity_growth()

    print("kappa_1_interval")
    print(decimal_fraction(KAPPA_LO, 70))
    print(decimal_fraction(KAPPA_HI, 70))
    print("slope_log3_4over3", SLOPE)
    print("offset_log3_kappa_over4", KAPPA_OFFSET)

    for case in CASES:
        verify_case(*case)

    if args.scan:
        scan_predictor(args.scan)


if __name__ == "__main__":
    main()
