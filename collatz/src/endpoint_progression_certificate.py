#!/usr/bin/env python3
"""Exact arithmetic-progression certificate for Collatz coefficient survival.

For a split state (k,q,y) and dangerous lift integers j=0,...,L-1,
endpoints are
    y + 3**q * j.
The recurrence splits j by its low binary bit and maps each subprogression
through one E/O channel, preserving the same arithmetic-progression form.

This is exactly equivalent to the transformed cyclic interval-count certificate,
but requires no modular inverses.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


def accelerated_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


@lru_cache(maxsize=None)
def count_progression(k: int, q: int, m: int, y: int, L: int) -> int:
    if L <= 0:
        return 0
    if m == 0:
        return L
    if 3**q >= 1 << (k + m):
        return L

    P = 3**q
    total = 0
    for c in (0, 1):
        Lc = (L + 1) // 2 if c == 0 else L // 2
        if Lc == 0:
            continue

        z = y + P * c
        b = z & 1
        qp = q + b
        if 3**qp < 1 << (k + 1):
            continue

        if b == 0:
            yp = z // 2
        else:
            yp = (3 * z + 1) // 2

        total += count_progression(k + 1, qp, m - 1, yp, Lc)

    return total


def direct_count(k: int, q: int, m: int, y: int, L: int) -> int:
    P = 3**q
    total = 0
    for j in range(L):
        x = y + P * j
        qq = q
        ok = True
        for s in range(1, m + 1):
            if x & 1:
                qq += 1
            x = accelerated_step(x)
            if 3**qq < 1 << (k + s):
                ok = False
                break
        if ok:
            total += 1
    return total


def self_test() -> None:
    tested = 0
    for k in range(4):
        for q in range(k + 3):
            for m in range(5):
                for y in range(21):
                    for L in range(13):
                        got = count_progression(k, q, m, y, L)
                        want = direct_count(k, q, m, y, L)
                        assert got == want, (k, q, m, y, L, got, want)
                        tested += 1
    assert tested == 24570, tested
    print(f"self_test=PASS,cases={tested}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=0)
    ap.add_argument("--q", type=int, default=0)
    ap.add_argument("--m", type=int, default=20)
    ap.add_argument("--y", type=int, default=0)
    ap.add_argument("--length", type=int, default=100)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    value = count_progression(args.k, args.q, args.m, args.y, args.length)
    info = count_progression.cache_info()
    print(
        f"count={value},cache_currsize={info.currsize},cache_hits={info.hits},"
        f"k={args.k},q={args.q},m={args.m},y={args.y},L={args.length}"
    )


if __name__ == "__main__":
    main()
