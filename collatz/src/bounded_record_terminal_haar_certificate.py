#!/usr/bin/env python3
"""Exact finite calibration for bounded-record terminal Haar contraction.

For each length L<=50 we enumerate all L+1 Sturmian mechanical factors by
scanning the exact Beatty word until L+1 distinct factors have appeared.
For every non-singleton record factor we verify that its terminal mechanical
tail is 1010 or 10110, propagate the prefix deficit counts A=f(0), B=f(1),
and compute the exact local Haar contraction B/(2A+B).

The companion note proves the all-length structural statements. This script is
an exact finite regression/calibration and not a proof of Collatz.
"""

from __future__ import annotations

from fractions import Fraction


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(10000)


def mechanical_word(s: int, L: int) -> tuple[int, ...]:
    return tuple(B[s + j] - B[s + j - 1] for j in range(1, L + 1))


def factor_types(L: int) -> dict[tuple[int, ...], int]:
    """Return all L+1 Sturmian factors with one witness phase each."""
    seen: dict[tuple[int, ...], int] = {}
    for s in range(9000):
        d = mechanical_word(s, L)
        if d not in seen:
            seen[d] = s
            if len(seen) == L + 1:
                break
    assert len(seen) == L + 1, (L, len(seen))
    return seen


def contains_10(bits: tuple[int, ...]) -> bool:
    return any(bits[i:i + 2] == (1, 0) for i in range(len(bits) - 1))


def prefix_deficit_counts(s: int, n: int) -> list[int]:
    # y=D-q >=0 under the upper first-passage boundary.
    dp = [1]
    for j in range(1, n + 1):
        d = B[s + j] - B[s + j - 1]
        nd = [0] * (len(dp) + 1)
        for y, c in enumerate(dp):
            # parity 0: y -> y+d
            nd[y + d] += c
            # parity 1: y -> y+d-1, provided the upper boundary is not crossed
            yy = y + d - 1
            if yy >= 0:
                nd[yy] += c
        dp = nd
    return dp


def tail_data(s: int, L: int):
    d = mechanical_word(s, L)
    if d[-1] != 0 or not contains_10(d[:-1]):
        return None

    if L >= 4 and d[-4:] == (1, 0, 1, 0):
        tail_len = 4
    elif L >= 5 and d[-5:] == (1, 0, 1, 1, 0):
        tail_len = 5
    else:
        raise AssertionError((s, L, d))

    dp = prefix_deficit_counts(s, L - tail_len)
    A = dp[0]
    B1 = dp[1] if len(dp) > 1 else 0
    assert A >= 1
    return d, tail_len, A, B1


def local_completions(dtail: tuple[int, ...], y0: int) -> set[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    L = len(dtail)
    for mask in range(1 << L):
        bits = tuple((mask >> j) & 1 for j in range(L))
        g = -y0
        ok = True
        for j, (e, d) in enumerate(zip(bits, dtail), start=1):
            g += e - d
            if j < L and g > 0:
                ok = False
                break
        if ok and g == 1:
            out.add(bits)
    return out


def main() -> None:
    # Exact local completion tables.
    assert local_completions((1, 0, 1, 0), 0) == {
        (0, 1, 1, 1), (1, 0, 1, 1)
    }
    assert local_completions((1, 0, 1, 0), 1) == {(1, 1, 1, 1)}
    assert local_completions((1, 0, 1, 0), 2) == set()

    assert local_completions((1, 0, 1, 1, 0), 0) == {
        (0, 1, 1, 1, 1), (1, 0, 1, 1, 1)
    }
    assert local_completions((1, 0, 1, 1, 0), 1) == {(1, 1, 1, 1, 1)}
    assert local_completions((1, 0, 1, 1, 0), 2) == set()

    checkpoints = {
        5: Fraction(1, 3),
        10: Fraction(8, 15),
        20: Fraction(3111, 2 * 961 + 3111),
        30: Fraction(2401483, 2 * 663535 + 2401483),
        50: Fraction(327501070154, 2 * 84141805077 + 327501070154),
    }

    running_max = Fraction(0, 1)
    running_arg = None
    non_singleton_count = 0

    for L in range(1, 51):
        for d, s in factor_types(L).items():
            td = tail_data(s, L)
            if td is None:
                continue
            non_singleton_count += 1
            d2, tail_len, A, B1 = td
            assert d2 == d
            assert tail_len in (4, 5)
            ratio = Fraction(B1, 2 * A + B1)
            assert ratio < 1
            if ratio > running_max:
                running_max = ratio
                running_arg = (L, d, tail_len, A, B1)

        if L in checkpoints:
            assert running_max == checkpoints[L], (L, running_max, checkpoints[L])
            print(
                "M", L,
                "kappa", float(running_max),
                "arg", running_arg,
            )

    assert running_arg is not None
    L, d, tail_len, A, B1 = running_arg
    assert L == 49
    assert A == 84_141_805_077
    assert B1 == 327_501_070_154

    print("bounded record terminal Haar calibration: PASS")
    print("non_singleton_factor_count_through_50", non_singleton_count)
    print("kappa_50_exact", running_max)
    print("kappa_50_float", float(running_max))


if __name__ == "__main__":
    main()
