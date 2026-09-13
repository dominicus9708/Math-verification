#!/usr/bin/env python3
"""Finite regression for the exact MATH-120 normalized affine floor margin.

This checks the exact rational transducer against direct shortcut iteration on a
finite deterministic domain. It is an implementation regression, not the proof
of a paid-layer closure theorem.
"""
from fractions import Fraction

LO = 1 << 71


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def main():
    cases = 0
    for n in range(1, 4097):
        x = n
        z = Fraction(1, 1)
        u = Fraction(0, 1)
        for _d in range(1, 13):
            if x % 2 == 0:
                x //= 2
                z = 2 * z
            else:
                x = (3 * x + 1) // 2
                u = u + z / 3
                z = 2 * z / 3

            assert Fraction(x, 1) == (Fraction(n, 1) + u) / z
            F = z * LO - n - u
            assert (x <= LO) == (F >= 0)
            cases += 1

    print('cases', cases)
    print('PASS MATH-120 normalized affine floor-margin regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__ == '__main__':
    main()
