#!/usr/bin/env python3
"""MATH-084: exact finite horizon for multi-source one-paid chains.

This is an algebraic certificate for the current first-cell source window.
It does not enumerate long one-paid chains and does not prove Bellman closure,
first-cell emptiness, or the Collatz conjecture.
"""
from fractions import Fraction

Q0 = 72_057_431_991
LO = 1 << 71
HI = 1364 * (1 << 61)
U = Fraction(HI, 1) + Fraction(Q0, 3)
Y_UPPER = 2 * U

# MATH-058 source anchors satisfy LO < Y < 2U.
WINDOW_WIDTH = Y_UPPER - LO

# The complete admissible source window is strictly narrower than 2^72.
assert WINDOW_WIDTH < (1 << 72)


def multisource_implies_H_le_71(H: int) -> bool:
    """If H>=72, two members A+2^H s cannot fit in the source window."""
    if H >= 72:
        assert (1 << H) >= (1 << 72) > WINDOW_WIDTH
        return False
    return True


# A one-paid macro has H_edge=L+2+eps with L>=1 and eps>=0,
# hence every macro consumes at least 3 source-modulus bits.
MIN_EDGE_H = 3
assert MIN_EDGE_H == 3

# If t>=24, accumulated H >= 72, so the chain cannot remain multi-source.
for t in range(24, 100):
    H_lower = MIN_EDGE_H * t
    assert H_lower >= 72
    assert not multisource_implies_H_le_71(H_lower)

# t=23 is the last count not excluded by this coarse theorem alone.
assert MIN_EDGE_H * 23 == 69 <= 71

print("PASS MATH-084")
print("source_window_width < 2^72")
print("multi_source => H <= 71")
print("one_paid_min_edge_H = 3")
print("multi_source_macro_count <= 23")
print("24th one-paid macro must be singleton-resolved if the chain still exists")
