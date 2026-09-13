#!/usr/bin/env python3
"""Finite regression for the exact MATH-119 affine gates.

The algebraic lemmas are proved in the note. This executable independently
checks that the affine recurrence, self-descent gate, and generalized floor gate
agree with direct shortcut iteration over a deterministic finite domain.
"""


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def affine_descriptor(n: int, d: int):
    x = n
    q = 0
    c = 0
    for i in range(d):
        if x % 2 == 0:
            x //= 2
        else:
            x = (3 * x + 1) // 2
            c = 3 * c + (1 << i)
            q += 1
    return x, q, c


def main():
    cases = 0
    floor_cases = 0
    floors = (1, 2, 3, 5, 8, 13, 21, 34, 64, 127, 255, 511, 1024, 2048)

    for n in range(1, 4097):
        for d in range(1, 13):
            x, q, c = affine_descriptor(n, d)
            assert (1 << d) * x == (3**q) * n + c

            # Gate A: exact self-descent.
            assert (x < n) == (((1 << d) - 3**q) * n > c)
            cases += 1

            # Gate B, generalized to an arbitrary finite floor L:
            # T^d(n) <= L iff 3^q*n+c <= 2^d*L.
            for L in floors:
                assert (x <= L) == ((3**q) * n + c <= (1 << d) * L)
                floor_cases += 1

    print('self_descent_cases', cases)
    print('floor_gate_cases', floor_cases)
    print('PASS MATH-119 affine self-descent and floor-gate regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__ == '__main__':
    main()
