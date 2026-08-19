#!/usr/bin/env python3
"""Exact regression certificate for selector collision-halving identities.

This is a finite exact-arithmetic certificate, not a Collatz proof.
It checks three equivalent forms of the selector sibling L2 energy:

  2 p_(r+1) - p_r
  = sum sibling-mass-difference^2
  = alternating balanced-ternary digit-weight sum.

Only Python integers/Fraction are used.
"""

from __future__ import annotations

from fractions import Fraction


def selector_counts(m: int, r: int) -> list[int]:
    """Counts of sum a_i 3^i modulo 2^r, a_i in {0,1}."""
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
    assert sum(dp) == 1 << m
    return dp


def collision_probability(m: int, r: int) -> Fraction:
    c = selector_counts(m, r)
    return Fraction(sum(x * x for x in c), 1 << (2 * m))


def sibling_energy(m: int, r: int) -> Fraction:
    """Normalized sibling energy from level r to r+1."""
    c = selector_counts(m, r + 1)
    half = 1 << r
    e = sum((c[x] - c[x + half]) ** 2 for x in range(half))
    return Fraction(e, 1 << (2 * m))


def balanced_weight(z: int) -> int:
    """Number of nonzero digits in the unique balanced ternary expansion."""
    z = abs(z)
    w = 0
    while z:
        a = z % 3
        if a == 0:
            z //= 3
        elif a == 1:
            w += 1
            z = (z - 1) // 3
        else:  # balanced digit -1
            w += 1
            z = (z + 1) // 3
    return w


def balanced_alternating_formula(m: int, r: int) -> Fraction:
    radius = (3**m - 1) // 2
    step = 1 << r
    jmax = radius // step

    s = Fraction(0, 1)
    for j in range(-jmax, jmax + 1):
        sign = 1 if (j & 1) == 0 else -1
        s += sign * Fraction(1, 1 << balanced_weight(j * step))
    return s / (1 << m)


def main() -> None:
    checked = 0
    for m in range(1, 11):
        for r in range(1, min(8, m + 3) + 1):
            p_r = collision_probability(m, r)
            p_next = collision_probability(m, r + 1)
            lhs = 2 * p_next - p_r
            sib = sibling_energy(m, r)
            bal = balanced_alternating_formula(m, r)

            assert lhs >= 0
            assert lhs == sib, (m, r, lhs, sib)
            assert lhs == bal, (m, r, lhs, bal)
            assert p_next >= p_r / 2
            checked += 1

    # A few transparent exact values.
    # For r=1, p_1=1/2 exactly for every m>=1.
    for m in range(1, 11):
        assert collision_probability(m, 1) == Fraction(1, 2)

    # For r=2 the finite data obey p_2 = 1/4 + 2^(-(m+1)).
    # This follows from the period-two selector pattern mod 4 and is useful as
    # a small indexing check for the refinement convention.
    for m in range(1, 11):
        expected = Fraction(1, 4) + Fraction(1, 1 << (m + 1))
        assert collision_probability(m, 2) == expected

    print(f"PASS exact collision-halving checks={checked}")
    print("Forms checked: collision refinement = sibling L2 = balanced-ternary alternating sum")


if __name__ == "__main__":
    main()
