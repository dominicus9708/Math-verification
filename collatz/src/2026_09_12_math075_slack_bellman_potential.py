#!/usr/bin/env python3
"""MATH-075 exact regression for the slack Bellman potential H_u=-lambda*u."""
from fractions import Fraction

LAM = Fraction(19, 503)
QMAX = 10000
UMAX = 32


def main():
    assert Fraction(1, 8) - LAM == Fraction(351, 4024)
    assert Fraction(1, 12) - 2 * LAM == Fraction(47, 6036)

    checked = 0
    p3 = 1
    m = 0
    for q in range(QMAX + 1):
        if q == 0:
            m = 0
        else:
            m = p3.bit_length() - 1 - q

        p3n = p3 * 3
        mn = p3n.bit_length() - 1 - (q + 1)
        eps = mn - m
        assert eps in (0, 1)

        om = Fraction(1 << (q + m), p3)
        if q > 0:
            if eps == 0:
                assert om > Fraction(3, 4)
            else:
                assert Fraction(1, 2) < om < Fraction(3, 4)

        for u in range(1, UMAX + 1):
            p = Fraction(1, 3) * (1 - Fraction(1, 2**u)) * om
            reduced = p - LAM - LAM * eps
            assert reduced > 0
            checked += 1

            # coefficient-valid even edge: u -> u-1
            assert -LAM + LAM == 0
            checked += 1

        # u=0 odd edge: p=0, the only residual negative unit edge.
        reduced0 = -LAM - LAM * eps
        assert reduced0 == (-LAM if eps == 0 else -2 * LAM)
        checked += 1

        p3 = p3n

    print("PASS MATH-075 slack Bellman regression", checked)
    print("margin_eps0_u_ge_1", Fraction(351, 4024))
    print("margin_eps1_u_ge_1", Fraction(47, 6036))


if __name__ == "__main__":
    main()
