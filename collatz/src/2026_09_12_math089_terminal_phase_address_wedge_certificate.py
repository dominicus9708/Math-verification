#!/usr/bin/env python3
"""MATH-089: exact terminal phase/address wedge for one-paid cylinders.

Let a multi-source parent contain M source parameters 0<=s<M and let
R=ceil(log2 M).  A next canonical edge with dyadic resolution h requires the
unique residue

    s_h = (A-B) * (3^Q)^(-1) mod 2^h.

For h>R write

    s_h = s_R + 2^R * zeta,  0<=s_R<2^R.

Then exact compatibility is equivalent to

    zeta=0 and s_R<M.

Thus h-R is exactly the number of high residue bits that must all extend by
zero beyond the parent family-resolution height.

MATH-074's resolution potential leaves only the terminal charge

    lambda * (h-R)_+, lambda=19/503.

For a one-paid edge the exact current-phase penalty is

    p = c * Omega_out, c in {1/4,1/8},

with branch ranges

    c=1/4: Omega_out in (1/2,2/3),
    c=1/8: Omega_out in (8/9,1).

Hence an actual negative local terminal contribution requires BOTH exact
zero-extension compatibility and

    c*Omega_out < lambda*z,
    z=(h-R)_+.

This certificate checks the arithmetic thresholds and synthetic exact residue
factorization.  It is a local Bellman/address lemma, not a Collatz proof.
"""
from fractions import Fraction

LAM = Fraction(19,503)


def ceil_log2(m: int) -> int:
    assert m >= 1
    return 0 if m == 1 else (m - 1).bit_length()


def compatible_factored(s_h: int, h: int, m: int) -> bool:
    R = ceil_log2(m)
    assert 0 <= s_h < (1 << h)
    if h <= R:
        return s_h < m
    low = s_h & ((1 << R) - 1) if R else 0
    high = s_h >> R
    return high == 0 and low < m


def main() -> None:
    # Exact residue-factorization regression on a broad finite synthetic grid.
    for m in range(1,257):
        R = ceil_log2(m)
        for h in range(1,13):
            for s in range(1 << h):
                assert compatible_factored(s,h,m) == (s < m)

    # Universal one-paid phase lower bounds.
    assert Fraction(1,9) > 2*LAM
    assert Fraction(1,8) > 3*LAM

    # z=3 can be dangerous only on the c=1/8 branch, and only below 456/503.
    assert 8 * (3*LAM) == Fraction(456,503)
    assert Fraction(8,9) < Fraction(456,503) < 1

    # On the c=1/4 branch, z=4 first opens a genuine phase subregion.
    assert 4 * (4*LAM) == Fraction(304,503)
    assert Fraction(1,2) < Fraction(304,503) < Fraction(2,3)

    print("PASS MATH-089 terminal phase-address wedge")
    print("lambda", LAM)
    print("z<=2 universally local-safe")
    print("z=3 danger only if c=1/8 and Omega_out < 456/503")
    print("z=4 c=1/4 danger threshold Omega_out < 304/503")


if __name__ == '__main__':
    main()
