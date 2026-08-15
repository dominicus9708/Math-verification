#!/usr/bin/env python3
"""Exact no-wrap + 2-adic mismatch barrier for gate transition repairs.

This certificate uses only universal Sturmian prefix lower bounds, so it is
safe across all conjugate gate phases. It treats the enlarged transition
sections 1^(F-h) B (01/10)^(J-h) 0 with |B|=3h, |B|_1=2h, and bounded incoming
integer credits 1<=delta<=397.
"""

CASES = (
    # name, F, J, q, L, relative floor slack s, expected uniform h ceiling
    ("G81-neutral", 404, 567, 971, 1539, 0, 392),
    ("G81-one-slack", 402, 568, 970, 1539, 1, 389),
    ("G82-neutral", 409, 574, 983, 1558, 0, 397),
    ("G82-one-slack", 407, 575, 982, 1558, 1, 394),
    ("G13-neutral", 5245, 7390, 12635, 20026, 0, 5230),
    ("G13-one-slack", 5243, 7391, 12634, 20026, 1, 5226),
    ("G14-neutral", 5648, 7958, 13606, 21565, 0, 5632),
    ("G14-one-slack", 5646, 7959, 13605, 21565, 1, 5629),
)

DELTA_MAX = 397


def safe(F, q, L, slack, h):
    f = F - h
    if f < 0:
        return False

    # Universal factor prefix: Q_mech(t) >= floor(t log_3 2).
    # A relative floor -slack therefore gives
    #   |D_B| < h * 3^(F+h+slack+1) / 2^f.
    # Hence the whole boundary-difference range lies in (-M/2,M/2) if
    #   2^f > 2 h 3^(slack+1).
    boundary_no_wrap = (1 << f) > 2 * h * 3 ** (slack + 1)

    # For a_n after n balanced lifts,
    #   a_n < (8 delta + 4)(4/3)^n.
    # With lambda=3^q/2^L and n=J-h this implies the raw target lies in
    # (-3^(F+h)/2,3^(F+h)/2) whenever
    #   2^f lambda > 2 delta + 1.
    # Check the worst delta exactly without floating point:
    target_no_wrap = (1 << f) * 3 ** q > (2 * DELTA_MAX + 1) * (1 << L)

    return boundary_no_wrap and target_no_wrap


def audit(case):
    name, F, J, q, L, slack, expected = case
    hs = [h for h in range(1, min(F, J - 1) + 1) if safe(F, q, L, slack, h)]
    # Both inequalities are monotone in the relevant range, so the safe h's
    # form an initial interval.
    assert hs == list(range(1, expected + 1)), (name, hs[-3:] if hs else hs)
    assert not safe(F, q, L, slack, expected + 1)
    print(name, "safe_through", expected, "F", F, "unresolved_front", F - expected)


if __name__ == "__main__":
    for c in CASES:
        audit(c)
