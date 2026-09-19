#!/usr/bin/env python3
"""MATH-242 structural bound regression.

Checks only the numerical interfaces between established theorems:
- low-paid full-factor length <= 89;
- MATH-239 sign theorem valid through 183;
- MATH-237 seven-factor expanding product lower bound exceeds 2.
"""

from fractions import Fraction

def main():
    assert 89 < 183

    # MATH-237 exact extremal products.
    n5 = Fraction(3**20, 2**31)
    n6 = Fraction(3**22, 2**34)
    n7 = Fraction(3**24, 2**37)

    assert n5 < 2
    assert n6 < 2
    assert n7 > 2

    print("PASS MATH-242 theorem-interface regression")
    print("lowpaid_factor_depth_max", 89)
    print("sign_theorem_depth_max", 183)
    print("max_multisource_expanding_factors", 6)
    print("SINGLETON TAIL OPEN")
    print("FULL r10 LAYER OPEN")

if __name__ == "__main__":
    main()
