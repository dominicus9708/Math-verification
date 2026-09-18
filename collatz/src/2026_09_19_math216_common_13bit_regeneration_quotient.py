#!/usr/bin/env python3
"""MATH-216 common 13-bit regeneration quotient regression."""

import random

ZMIN = {2:1,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:13}
MOD = 1 << 13

def v2(n: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    return (n & -n).bit_length() - 1

def main():
    random.seed(216)
    checked = 0
    for _ in range(50000):
        Q = random.randrange(0,2048)
        u = random.randrange(1,MOD,2)
        a = random.randrange(1,MOD,2)
        R = (pow(3,Q,MOD)*u+a) % MOD
        exact = (3**Q)*u+a
        for r,z in ZMIN.items():
            direct = v2(exact) >= z
            quotient = (R % (1<<z)) == 0
            assert direct == quotient
            if r == 10:
                assert quotient == (R == 0)
            checked += 1
    assert max(ZMIN.values()) == 13
    print("PASS MATH-216 common 13-bit regeneration quotient regression")
    print("checks", checked)
    print("remaining_paid_tags", sorted(ZMIN))
    print("r10_exact_zero_residue", True)
    print("NO LAYER CLOSURE CLAIM")

if __name__ == "__main__":
    main()
