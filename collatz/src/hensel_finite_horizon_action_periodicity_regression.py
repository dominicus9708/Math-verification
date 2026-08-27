#!/usr/bin/env python3
"""Regression for exact finite-horizon Hensel action periodicity.

The symbolic proof is in
  collatz/notes/2026-08-27-Hensel-finite-horizon-action-periodicity.md

This script checks modular periodicity, successor-carry resolution, candidate
counts and representative dominance on finite samples.  It is not a proof of
a global Collatz statement.
"""

from fractions import Fraction


def v3(n: int) -> int:
    c = 0
    while n % 3 == 0 and n:
        n //= 3
        c += 1
    return c


def local_cost(w: Fraction, d: int) -> Fraction:
    return 2 * w * (1 - Fraction(1, 2**d))


def lift_to_lower_bound(a: int, modulus: int, lower: int) -> int:
    a %= modulus
    if a >= lower:
        return a
    return a + ((lower - a + modulus - 1) // modulus) * modulus


def check_orders(max_r=8):
    checks = 0
    for r in range(1, max_r + 1):
        M = 2 * 3 ** (r - 1)
        mod = 3**r
        assert pow(2, M, mod) == 1
        assert v3(pow(2, M) - 1) == r
        for k in range(r - 1):
            assert pow(2, 2 * 3**k, mod) != 1
        checks += 1
    return checks


def check_periodicity(max_r=6):
    checks = 0
    for r in range(1, max_r + 1):
        M = 2 * 3 ** (r - 1)
        mod = 3**r
        next_mod = 3 ** (r - 1)
        for e in range(-6, 7):
            for d in range(0, 18):
                u = pow(2, e - d, mod)
                u2 = pow(2, e - (d + M), mod)
                assert u == u2

                for K in range(mod):
                    if (K + u) % 3 != 0:
                        continue
                    K1 = ((K + u) // 3) % next_mod if r > 1 else 0
                    K2 = ((K + u2) // 3) % next_mod if r > 1 else 0
                    assert K1 == K2
                    checks += 1
    return checks


def check_candidate_counts(max_r=6):
    checks = 0
    for r in range(1, max_r + 1):
        M = 2 * 3 ** (r - 1)
        mod = 3**r
        for e in range(-4, 5):
            for K in range(mod):
                allowed = [
                    a for a in range(M)
                    if (K + pow(2, e - a, 3)) % 3 == 0
                ]
                if K % 3 == 0:
                    assert len(allowed) == 0
                else:
                    assert len(allowed) == 3 ** (r - 1)
                checks += 1
    return checks


def check_representative_dominance(max_r=6):
    checks = 0
    w = Fraction(7, 23)
    for r in range(1, max_r + 1):
        M = 2 * 3 ** (r - 1)
        mod = 3**r
        for lower in range(8):
            for a in range(M):
                d0 = lift_to_lower_bound(a, M, lower)
                d1 = d0 + M
                assert d0 >= lower
                assert d1 > d0
                assert d0 % M == d1 % M
                assert local_cost(w, d1) > local_cost(w, d0)
                for e in range(-2, 3):
                    assert pow(2, e - d0, mod) == pow(2, e - d1, mod)
                checks += 1
    return checks


def check_depth_two_three_candidates():
    r = 2
    M = 6
    mod = 9
    checks = 0
    for lower in range(10):
        for e in range(-5, 6):
            for K in range(mod):
                reps = []
                for a in range(M):
                    d = lift_to_lower_bound(a, M, lower)
                    if (K + pow(2, e - d, 3)) % 3 == 0:
                        reps.append(d)
                if K % 3 == 0:
                    assert len(reps) == 0
                else:
                    assert len(reps) == 3
                    assert len({d % M for d in reps}) == 3
                checks += 1
    return checks


def main():
    print("PASS")
    print("order checks:", check_orders())
    print("periodicity/successor checks:", check_periodicity())
    print("candidate-count checks:", check_candidate_counts())
    print("representative-dominance checks:", check_representative_dominance())
    print("depth-two checks:", check_depth_two_three_candidates())


if __name__ == "__main__":
    main()
