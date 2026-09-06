#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
A0 = 114_208_327_604
Q0 = 72_057_431_991


def ln_interval(x: Fraction, n: int = 260):
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
    tail = 2 * (z ** (2 * n + 3)) / ((2 * n + 3) * (1 - z2))
    return lo, lo + tail


LN2 = ln_interval(Fraction(2), 200)
LN3 = ln_interval(Fraction(3), 260)


def linear_form_interval(A: int, q: int):
    """Rigorous interval for A ln 2 - q ln 3."""
    return A * LN2[0] - q * LN3[1], A * LN2[1] - q * LN3[0]


def main():
    # The first universal Farey cell has odd q.
    assert Q0 & 1

    # For the latest-possible mechanical first-crossing word, put
    #   p_r = floor((r-1) log_2 3),  r=1,...,q.
    # Its normalized correction is
    #   S_* = R/3^q = (1/3) sum_{n=0}^{q-1} 2^{- {n log_2 3}}.
    #
    # Let theta = log_2(3/2). Pair x={2m log_2 3} with
    # {x+theta}.  Using 2^{-theta}=2/3 and 2^{1-theta}=4/3,
    # every pair contributes strictly more than 7/6.  Since q is odd,
    # the last unpaired term is >1/2. Therefore
    #
    #   S_* > (7q-1)/36.
    S_LOWER = Fraction(7 * Q0 - 1, 36)

    # The standard pair upper bound retained elsewhere in the repository is
    # S_* <= (7q+1)/24.  It is not used for the barrier assertion, but the
    # inequality below records the expected ordering of the two exact bounds.
    S_UPPER = Fraction(7 * Q0 + 1, 24)
    assert S_LOWER < S_UPPER

    # For the first cell, let
    #   epsilon = (2^A - 3^q)/3^q = exp(delta)-1,
    #   delta   = A ln 2 - q ln 3.
    #
    # A correction-only elimination at the verified floor B0 would require
    # every admissible word to satisfy S < B0*epsilon.  We instead certify the
    # opposite for the explicit latest mechanical word, with more than 7%
    # headroom:
    #
    #   S_* > 1.07 * B0 * epsilon.
    #
    # It is enough to prove
    #   delta < ln(1 + S_LOWER/(1.07*B0)).
    delta = linear_form_interval(A0, Q0)
    rhs = ln_interval(
        Fraction(1) + S_LOWER * Fraction(100, 107) / Fraction(B0),
        180,
    )
    assert delta[1] < rhs[0]

    # We also record the zero-slack inequality separately as a regression.
    rhs_zero_slack = ln_interval(Fraction(1) + S_LOWER / Fraction(B0), 180)
    assert delta[1] < rhs_zero_slack[0]

    print("PASS")
    print("first universal cell (A,q) =", (A0, Q0))
    print("mechanical normalized correction lower bound = (7q-1)/36")
    print("correction-only floor barrier: S_* > B0*epsilon")
    print("certified slack: S_* > 1.07*B0*epsilon")
    print("same-integer dyadic address remains the required obstruction")


if __name__ == "__main__":
    main()
