#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

B0 = 1 << 71

# Neighboring rationals around the verified-floor minimality strip.
PL, QL = 6_586_818_670, 10_439_860_591
PU, QU = 65_470_613_321, 103_768_467_013

FIRST = (114_208_327_604, 72_057_431_991)  # (A,q)
SECOND = (217_976_794_617, 137_528_045_312)


def ln_interval(x: Fraction, n: int = 240):
    """Rigorous rational interval for ln(x), x>=1, via atanh series."""
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)
    z = (x - 1) / (x + 1)
    assert 0 <= z < 1
    z2 = z * z
    term = z
    s = Fraction(0)
    for k in range(n + 1):
        s += term / (2 * k + 1)
        term *= z2
    lo = 2 * s
    # The omitted denominators are all at least 2n+3.
    tail = 2 * (z ** (2 * n + 3)) / ((2 * n + 3) * (1 - z2))
    return lo, lo + tail


def ratio_interval(num, den):
    nl, nu = num
    dl, du = den
    assert dl > 0
    return nl / du, nu / dl


LN2 = ln_interval(Fraction(2), 200)
LN3 = ln_interval(Fraction(3), 260)
LNC = ln_interval(Fraction(3 * B0 + 1, B0), 260)

ALPHA = ratio_interval(LN2, LN3)  # log_3 2
BETA = ratio_interval(LN2, LNC)   # ln2/ln(3+1/B0)


def linear_form_interval(A, q):
    return A * LN2[0] - q * LN3[1], A * LN2[1] - q * LN3[0]


def eps_lt_power3(A, q, i):
    # exp(lambda)-1 < 3^-i iff lambda < ln(1+3^-i).
    lam = linear_form_interval(A, q)
    rhs = ln_interval(Fraction(3**i + 1, 3**i), 100)
    assert lam[1] < rhs[0] or lam[0] > rhs[1]
    return lam[1] < rhs[0]


def dangerous_dimension(A, q):
    # h = #{i>=1: 3^-i >= epsilon}; monotonic, scan a safe range.
    good = []
    for i in range(1, 128):
        if eps_lt_power3(A, q, i):
            good.append(i)
    return max(good) if good else 0


def buffered_B(A, q):
    # D*2^B > q*3^(q-1)
    # iff epsilon > q/(3*2^B)
    # iff lambda > ln(1 + q/(3*2^B)).
    lam = linear_form_interval(A, q)
    for B in range(0, 256):
        rhs = ln_interval(Fraction(3 * (1 << B) + q, 3 * (1 << B)), 180)
        if lam[0] > rhs[1]:
            if B:
                prev = ln_interval(
                    Fraction(3 * (1 << (B - 1)) + q, 3 * (1 << (B - 1))),
                    180,
                )
                assert lam[1] <= prev[0]
            return B
    raise RuntimeError("buffer not found")


def in_open_strip(f):
    return BETA[1] < f < ALPHA[0]


def main():
    # Coarse rational parity-prefix RS spine.
    assert (3 * B0 + 1) ** 306 < (2 ** 485) * (B0 ** 306)

    rL = Fraction(PL, QL)
    rU = Fraction(PU, QU)
    assert rL < BETA[0]
    assert BETA[1] < ALPHA[0]
    assert ALPHA[1] < rU

    # Farey-neighbor certificate.
    assert PU * QL - PL * QU == 1
    A0 = QL + QU
    q0 = PL + PU
    assert (A0, q0) == FIRST
    r0 = Fraction(q0, A0)
    assert in_open_strip(r0)

    # Any reduced fraction strictly between Farey neighbors has denominator
    # at least QL+QU, so FIRST is the exact minimum-denominator strip cell.

    # Enumerate the entire unimodular cone up to the old giant resonance.
    limit = SECOND[0]
    cells = []
    for a in range(1, limit // QL + 1):
        for b in range(1, limit // QU + 1):
            A = a * QL + b * QU
            if A > limit or gcd(a, b) != 1:
                continue
            q = a * PL + b * PU
            f = Fraction(q, A)
            if in_open_strip(f):
                cells.append((A, q, a, b))

    assert cells == [
        (114_208_327_604, 72_057_431_991, 1, 1),
        (217_976_794_617, 137_528_045_312, 1, 2),
    ]

    # Local dangerous-axis and global buffered-core sizes.
    assert dangerous_dimension(*FIRST) == 23
    assert buffered_B(*FIRST) == 72
    assert dangerous_dimension(*SECOND) == 25
    assert buffered_B(*SECOND) == 76

    print("PASS")
    print("B0 =", B0)
    print("first universal strip cell (A,q) =", FIRST)
    print("cells through old giant resonance =", [(A, q) for A, q, _, _ in cells])
    print("FIRST: h=23, B=72")
    print("SECOND: h=25, B=76")


if __name__ == "__main__":
    main()
