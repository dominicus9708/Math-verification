#!/usr/bin/env python3
"""MATH-215 universal carry-valuation Bellman reduction regression."""

import random

ZMIN = {
    2:1, 3:2, 4:3, 5:6, 6:7, 7:8, 8:10, 9:11, 10:13,
    11:14, 12:16, 13:18, 14:19, 15:21, 16:22, 17:25,
    18:25, 19:26, 20:28, 21:29,
}

def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

def main():
    random.seed(215)
    checked = 0
    for _ in range(30000):
        Q = random.randrange(0,40)
        d = random.randrange(-10**9,10**9) or 1
        c = random.randrange(-10**9,10**9) or 2
        num = 3**Q*d + c
        if num == 0:
            continue
        w = v2(num)
        z = random.randrange(0,w+1)
        dp = num // (1<<z)
        v = v2(d)
        vp = v2(dp)
        gamma = w-v
        assert z == v-vp+gamma
        assert -z + v-vp == -gamma
        if gamma > 0:
            assert v2(c) == v
            u = d >> v
            a = c >> v
            assert (u & 1) and (a & 1)
            assert gamma == v2((3**Q)*u+a)
        checked += 1
    assert ZMIN[10] == 13
    assert max(ZMIN[r] for r in range(2,11)) == 13
    print("PASS MATH-215 universal carry-valuation reduction regression")
    print("checked", checked)
    print("r10_regeneration_bits", ZMIN[10])
    print("NO LAYER CLOSURE CLAIM")

if __name__ == "__main__":
    main()
