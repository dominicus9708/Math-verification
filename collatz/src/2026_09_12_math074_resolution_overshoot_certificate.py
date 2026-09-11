#!/usr/bin/env python3
"""MATH-074: exact resolution-overshoot Bellman lemma regression.

For an exact dyadic cylinder with M ordinary source anchors, appending ell
shortcut bits leaves at most ceil(M/2^ell) anchors.  With
R(M)=ceil(log2 M), R(0)=R(1)=0 for handoff purposes, this implies

    R' <= max(0, R-ell).

Hence for H_R=-lambda R,

    p-lambda*ell + H_R' - H_R
      >= p-lambda*max(0, ell-R).

So every nonterminal multi-source refinement with ell<=R is automatically
Bellman-safe for any p>=0; only singleton-producing terminal overshoot can
retain negative reduced cost.

The algebraic proof is elementary.  This file performs finite exact regression
on a large grid of integer M,ell and the worst allowed child count.
Collatz and the first universal Farey cell remain OPEN.
"""
from fractions import Fraction

LAM = Fraction(19, 503)


def R(m: int) -> int:
    if m <= 1:
        return 0
    return (m - 1).bit_length()


def ceil_div_pow2(m: int, ell: int) -> int:
    return (m + (1 << ell) - 1) >> ell


def main():
    checked = 0
    for ell in range(1, 74):
        # Dense low range plus boundary values around powers of two up to 2^73.
        vals = set(range(1, 20000))
        for j in range(0, 74):
            x = 1 << j
            for d in (-2, -1, 0, 1, 2):
                if 1 <= x + d < (1 << 74):
                    vals.add(x + d)
        for m in vals:
            rp = R(ceil_div_pow2(m, ell))
            rr = R(m)
            assert rp <= max(0, rr - ell), (m, ell, rr, rp)

            # Worst Bellman reduced value at p=0 and maximal possible R'.
            lhs = -LAM * ell + (-LAM * rp) - (-LAM * rr)
            rhs = -LAM * max(0, ell - rr)
            assert lhs >= rhs, (m, ell, lhs, rhs)
            if ell <= rr:
                assert lhs >= 0
            checked += 1

    print("checked", checked)
    print("lambda", LAM)
    print("PASS MATH-074 resolution-overshoot Bellman lemma regression")


if __name__ == "__main__":
    main()
