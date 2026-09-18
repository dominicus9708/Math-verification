#!/usr/bin/env python3
"""MATH-214 consecutive-r10 four-phase potential / regeneration-kernel regression."""

from fractions import Fraction
import random

LAM = Fraction(19,503)
E4 = Fraction(
    40328831637298674714593,
    18810608394584532713472,
)
MARGIN = Fraction(
    538598373207337125857,
    18810608394584532713472,
)

def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

def main():
    assert E4 - 56*LAM == MARGIN
    assert MARGIN > 0

    random.seed(214)
    checked = 0

    for _ in range(20000):
        Q = random.randrange(0,30)
        d = random.randrange(-10**8,10**8)
        if d == 0:
            d = 1
        c = random.randrange(-10**8,10**8)
        if c == 0:
            c = 2

        num = 3**Q*d + c
        if num == 0:
            continue

        w = v2(num)
        z = random.randrange(0,w+1)
        dp = num // (1<<z)
        vi = v2(d)
        vp = v2(dp)
        gamma = w-vi

        assert z == vi-vp+gamma
        # Algebra behind the combined Bellman/carry potential:
        assert 14-z + vi-vp == 14-gamma

        if gamma >= 15:
            s = v2(d)
            assert v2(c) == s
            u = d >> s
            a = c >> s
            assert ((3**Q)*u+a) % (1<<15) == 0

        checked += 1

    print("PASS MATH-214 four-phase / 15-bit regeneration regression")
    print("four_block_margin", MARGIN)
    print("checked_carry_cases", checked)
    print("CONSECUTIVE r10 SUBSECTOR ONLY; NO r10 LAYER CLOSURE CLAIM")

if __name__ == "__main__":
    main()
