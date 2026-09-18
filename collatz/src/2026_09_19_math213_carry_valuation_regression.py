#!/usr/bin/env python3
"""MATH-213 carry-valuation regeneration identity regression."""

import random

def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

def main():
    random.seed(213)
    checked = 0
    positive = 0

    for _ in range(20000):
        Q = random.randrange(0, 30)
        d = random.randrange(-10**9, 10**9)
        if d == 0:
            d = 1
        c = random.randrange(-10**9, 10**9)
        if c == 0:
            c = 2

        n = (3**Q) * d + c
        if n == 0:
            continue

        w = v2(n)
        z = random.randrange(0, w + 1)
        dp = n // (1 << z)
        assert dp != 0

        vi = v2(d)
        vp = v2(dp)
        g = w - vi

        assert z == vi - vp + g

        s = v2(c)
        if s != vi:
            assert w == min(s, vi)
            assert g <= 0
        elif g > 0:
            u = d >> vi
            a = c >> vi
            assert u & 1 and a & 1
            assert g == v2((3**Q) * u + a)
            positive += 1

        checked += 1

    print("PASS MATH-213 carry-valuation regeneration regression")
    print("checked", checked)
    print("positive_regeneration_cases", positive)
    print("NO r10 CLOSURE CLAIM")

if __name__ == "__main__":
    main()
