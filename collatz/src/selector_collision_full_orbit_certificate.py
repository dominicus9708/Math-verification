#!/usr/bin/env python3
"""Exact regression for selector collision full-orbit renormalization.

Checks
    e_r(m+M_r) = 2^(-2 M_r + 1) e_r(m)
for a finite exact-arithmetic grid, where
    e_r(m) = 2 p_(r+1)(m) - p_r(m),
    M_r = 2^(r-1).

This is a finite certificate for the algebraic implementation, not a Collatz proof.
"""

from fractions import Fraction


def counts(m: int, r: int) -> list[int]:
    n = 1 << r
    dp = [0] * n
    dp[0] = 1
    for i in range(m):
        w = pow(3, i, n)
        nd = dp.copy()
        for x, c in enumerate(dp):
            if c:
                nd[(x + w) & (n - 1)] += c
        dp = nd
    return dp


def collision(m: int, r: int) -> Fraction:
    c = counts(m, r)
    return Fraction(sum(x * x for x in c), 1 << (2 * m))


def energy(m: int, r: int) -> Fraction:
    return 2 * collision(m, r + 1) - collision(m, r)


def main() -> None:
    checked = 0
    # Keep the grid modest so the certificate remains quick, while covering
    # several complete multiplicative-orbit lengths exactly.
    for r in range(2, 5):
        M = 1 << (r - 1)
        factor = Fraction(1, 1 << (2 * M - 1))
        for m in range(0, 11):
            lhs = energy(m + M, r)
            rhs = factor * energy(m, r)
            assert lhs == rhs, (r, m, M, lhs, rhs)
            checked += 1

    # Transparent checkpoints.
    assert energy(44, 2) == Fraction(1, 1 << 66)
    assert energy(44, 3) == Fraction(1, 1 << 77)
    assert energy(44, 4) == Fraction(1, 1 << 79)

    print(f"PASS collision full-orbit recurrence checks={checked}")
    print("m=44 checkpoints: e_2=2^-66, e_3=2^-77, e_4=2^-79")


if __name__ == "__main__":
    main()
