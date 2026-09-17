#!/usr/bin/env python3
"""MATH-183 exact-rational regression for resolution-bit contraction.

Structural identities are algebraic.  This script exhaustively checks a broad
small exact grid to guard the implementation and endpoint conventions.
No Collatz layer closure is claimed.
"""

from fractions import Fraction
from math import ceil, log2


def rheight(M: int) -> int:
    if M <= 1:
        return 0
    return (M - 1).bit_length()


def bad_count(a: int, H: int, M: int, S: Fraction, rho: Fraction) -> int:
    assert rho > 1
    return sum(
        1
        for s in range(M)
        if S - (a + (1 << H) * s) * (rho - 1) >= 0
    )


def sigma_from(S: Fraction, rho: Fraction) -> Fraction:
    # S = 1 + Sigma - rho.
    return S + rho - 1


def kappa(a: int, H: int, M: int, S: Fraction, rho: Fraction) -> int:
    R = rheight(M)
    if R == 0:
        return 0
    Sigma = sigma_from(S, rho)
    out = 0
    for t in range(1, R + 1):
        st = 1 << (R - t)
        assert st < M
        rhs = Fraction(a + (1 << H) * st + 1) * (rho - 1)
        if Sigma < rhs:
            out = t
    return out


def main() -> None:
    cases = 0
    contraction_hits = 0

    # Exact rational test grid.  rho>1 values are deliberately varied around
    # small first-crossing-like overshoots as well as larger values.
    rhos = [
        Fraction(17, 16),
        Fraction(9, 8),
        Fraction(5, 4),
        Fraction(3, 2),
        Fraction(7, 4),
        Fraction(2, 1),
    ]

    for a in range(1, 18):
        for H in range(0, 6):
            for M in range(1, 65):
                R = rheight(M)
                for rho in rhos:
                    # Include negative, zero, and positive master defects at
                    # the left endpoint by sweeping exact S values.
                    for snum in range(0, 65):
                        S = Fraction(snum, 4)
                        Sigma = sigma_from(S, rho)

                        # Algebraic defect-coordinate identity.
                        for s in (0, M - 1):
                            N = a + (1 << H) * s
                            d_s = S - N * (rho - 1)
                            d_sig = Sigma - (N + 1) * (rho - 1)
                            assert d_s == d_sig

                        B = bad_count(a, H, M, S, rho)
                        Rb = rheight(B)

                        # Bad states must be one initial prefix.
                        for s in range(M):
                            bad = S - (a + (1 << H) * s) * (rho - 1) >= 0
                            assert bad == (s < B)

                        kap = kappa(a, H, M, S, rho)
                        assert Rb <= R - kap, (a, H, M, S, rho, B, Rb, R, kap)

                        # Check every t-bit implication directly.
                        if R >= 1:
                            for t in range(1, R + 1):
                                st = 1 << (R - t)
                                lhs = Sigma
                                rhs = Fraction(a + (1 << H) * st + 1) * (rho - 1)
                                if lhs < rhs:
                                    assert B <= st
                                    assert Rb <= R - t
                                    contraction_hits += 1

                        cases += 1

    print("PASS MATH-183 exact resolution-bit contraction regression")
    print(f"cases={cases}")
    print(f"verified_contraction_implications={contraction_hits}")
    print("NO r=10 LAYER CLOSURE CLAIM")


if __name__ == "__main__":
    main()
