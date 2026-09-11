#!/usr/bin/env python3
"""
MATH-060 exact first-cell envelope/slope target certificate.

This certificate does NOT prove the required global penalty lower bound.
It proves the arithmetic target that would suffice to close the first
universal Farey cell, using the classical Denjoy-Koksma inequality as an
external theorem.

All logarithmic/continued-fraction facts are certified with rational interval
arithmetic from the atanh series for log, so no floating-point decision is
used.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

A0 = 114_208_327_604
Q0 = 72_057_431_991
D0 = A0 - Q0
K = A0 - 1
N_FLOOR = 1 << 71
OVERHEAD = 89


def log_interval(x: Fraction, terms: int = 120):
    """Rigorous rational interval for log(x), x>0, using atanh series."""
    z = (x - 1) / (x + 1)
    assert 0 < z < 1
    s = Fraction(0)
    for n in range(terms):
        s += 2 * z ** (2 * n + 1) / (2 * n + 1)
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return s, s + tail


def cf_from_interval(lo: Fraction, hi: Fraction, nmax: int = 35):
    """Common continued-fraction prefix of every x in [lo,hi]."""
    out = []
    L, U = lo, hi
    for _ in range(nmax):
        aL = L.numerator // L.denominator
        aU = U.numerator // U.denominator
        assert aL == aU, (aL, aU)
        a = aL
        out.append(a)
        L -= a
        U -= a
        if L == 0:
            break
        L, U = 1 / U, 1 / L
    return out


def convergents(digits):
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    out = []
    for a in digits:
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        out.append((p, q))
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q
    return out


def dec(x: Fraction, digits=30):
    getcontext().prec = digits
    return Decimal(x.numerator) / Decimal(x.denominator)


def main():
    l15, u15 = log_interval(Fraction(3, 2))
    l2, u2 = log_interval(Fraction(2, 1))
    theta_lo = l15 / u2
    theta_hi = u15 / l2

    digits = cf_from_interval(theta_lo, theta_hi)
    expected_prefix = [
        0, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1,
        4, 3, 1, 1, 15, 1, 9,
    ]
    assert digits[:len(expected_prefix)] == expected_prefix
    conv = convergents(digits)

    left = (3_853_041_921, 6_586_818_670)
    right = (38_297_853_692, 65_470_613_321)
    assert left in conv and right in conv
    i = conv.index(left)
    assert conv[i + 1] == right
    assert right[0] * left[1] - left[0] * right[1] == -1
    assert left[0] + right[0] == D0
    assert left[1] + right[1] == Q0

    # For f(x)=2^{-x} on the circle, integral f = 1/(2 log 2) and
    # total variation (monotone drop plus the periodic jump) is 1.
    # Denjoy-Koksma on each convergent-denominator block gives total error <=2.
    # S_boundary=(1/3) Sum_{n<q0} f({n theta}), hence error <=2/3.
    S_boundary_upper = Fraction(Q0, 6) / l2 + Fraction(2, 3)

    # log(2^A0/3^Q0)=D0 log2-Q0 log(3/2).
    log_delta_lower = D0 * l2 - Q0 * u15
    assert log_delta_lower > 0
    # For x>0, exp(x)-1>x. Therefore terminal delta is strictly above
    # log_delta_lower, and N>2^71 gives the following strict correction demand.
    terminal_correction_lower = log_delta_lower * N_FLOOR
    penalty_upper = S_boundary_upper - terminal_correction_lower
    assert penalty_upper > 0

    required = penalty_upper / (K - OVERHEAD)
    lam_old = Fraction(17, 450)
    lam_opt = Fraction(19, 503)
    assert lam_old > required
    assert lam_opt > required

    # Exact optimization: smallest rational > required with denominator <=1000.
    best = None
    for q in range(1, 1001):
        p = (required.numerator * q) // required.denominator + 1
        f = Fraction(p, q)
        if best is None or f < best:
            best = f
    assert best == lam_opt

    margin_old = lam_old * (K - OVERHEAD) - penalty_upper
    margin_opt = lam_opt * (K - OVERHEAD) - penalty_upper
    assert margin_old > 0 and margin_opt > 0

    print("theta_CF_pair", left, right)
    print("mediant", (D0, Q0))
    print("S_boundary_upper", dec(S_boundary_upper, 40))
    print("terminal_correction_lower", dec(terminal_correction_lower, 40))
    print("penalty_upper", dec(penalty_upper, 40))
    print("required_lambda_C89", dec(required, 40))
    print("lambda_17_450_margin", dec(margin_old, 40))
    print("lambda_19_503_margin", dec(margin_opt, 40))
    print("best_denominator_le_1000", lam_opt)
    print("PASS MATH-060 exact first-cell slope target certificate")


if __name__ == "__main__":
    main()
