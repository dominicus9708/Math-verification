#!/usr/bin/env python3
"""Finite audit for the multi-resolution plateau occupancy-halving theorem.

The general theorem is proved in the accompanying note by a dyadic lift count.
This script exhaustively checks the local lift inequality on small moduli,
checks representative joint intersections, and records the exact q=2 moment
constant 7/8. It does not prove Collatz.
"""

from fractions import Fraction
from itertools import combinations, product
from math import cos, log2, pi


def centered(x: int, mod: int) -> int:
    r = x % mod
    if r >= mod // 2:
        r -= mod
    return r


def dangerous(u: int, r: int, a: int) -> bool:
    """s=1 central-window condition, using exact integer arithmetic."""
    mod = 1 << r
    b = centered(a * u, mod)
    # |b| < 2^(r-1)/3
    return 3 * abs(b) < (1 << (r - 1))


def check_base_halving() -> None:
    for r in range(2, 11):
        mod = 1 << r
        odd_total = 1 << (r - 1)
        for a in range(1, mod, 2):
            count = sum(dangerous(u, r, a) for u in range(1, mod, 2))
            assert count <= odd_total // 2


def check_lift_halving() -> None:
    # Exhaustive local implication used in the induction.
    for r_low in range(2, 8):
        low_mod = 1 << r_low
        for r_high in range(r_low + 2, min(10, r_low + 5) + 1):
            high_mod = 1 << r_high
            lift_count = 1 << (r_high - r_low)
            cap = lift_count // 2
            for a in range(1, high_mod, 2):
                for low in range(1, low_mod, 2):
                    cnt = 0
                    for t in range(lift_count):
                        u = low + t * low_mod
                        if dangerous(u, r_high, a):
                            cnt += 1
                    assert cnt <= cap


def check_joint_examples() -> None:
    # Representative arbitrary odd multipliers on schedules with gap >= 2.
    for R in range(6, 11):
        odd = list(range(1, 1 << R, 2))
        resolutions = list(range(2, R + 1))
        schedules = []
        for k in range(1, min(4, len(resolutions)) + 1):
            for rs in combinations(resolutions, k):
                if all(rs[i + 1] - rs[i] >= 2 for i in range(k - 1)):
                    schedules.append(rs)
        for rs in schedules:
            # Several deterministic odd-unit patterns; the local audit above
            # is exhaustive in the multiplier, so these are regression tests.
            patterns = []
            for seed in (1, 3, 5, 11):
                patterns.append(tuple((pow(3, seed + i, 1 << r) or 1) for i, r in enumerate(rs)))
            for aa in patterns:
                count = 0
                for u in odd:
                    if all(dangerous(u, r, a) for r, a in zip(rs, aa)):
                        count += 1
                assert count * (1 << len(rs)) <= len(odd)


def check_actual_moment_examples() -> None:
    theta = (3.0 ** 0.5) / 2.0
    for R in range(6, 10):
        odd = list(range(1, 1 << R, 2))
        rs = tuple(range(2, R + 1, 2))
        if not rs:
            continue
        aa = tuple(pow(3, -(i + 1), 1 << r) for i, r in enumerate(rs))
        vals = []
        for u in odd:
            y = 1.0
            for r, a in zip(rs, aa):
                mod = 1 << r
                b = centered(a * u, mod)
                y *= abs(cos(pi * b / mod))
            vals.append(y)
        mean1 = sum(vals) / len(vals)
        mean2 = sum(v * v for v in vals) / len(vals)
        bound1 = ((1.0 + theta) / 2.0) ** len(rs)
        bound2 = (7.0 / 8.0) ** len(rs)
        assert mean1 <= bound1 + 1e-12
        assert mean2 <= bound2 + 1e-12


def main() -> None:
    check_base_halving()
    check_lift_halving()
    check_joint_examples()
    check_actual_moment_examples()

    q2_base = Fraction(7, 8)
    mean_exp = -log2((2 + 3 ** 0.5) / 4)
    rms_exp = -0.5 * log2(float(q2_base))

    print("multi-resolution plateau occupancy audit: PASS")
    print("q=2 moment base =", q2_base)
    print("q=1 bit exponent per mixed coordinate =", format(mean_exp, ".15f"))
    print("q=2 RMS bit exponent per mixed coordinate =", format(rms_exp, ".15f"))
    print("typical |F|>=0.10L RMS exponent >=", format(0.1 * rms_exp, ".15f"), "* L")


if __name__ == "__main__":
    main()
