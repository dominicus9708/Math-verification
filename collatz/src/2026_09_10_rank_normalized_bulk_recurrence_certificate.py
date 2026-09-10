#!/usr/bin/env python3
"""Exact identity checks for the rank-normalized Collatz Hensel recurrence.

This certificate checks algebraic state transformations used after MATH-051.
It is not a Collatz proof and does not claim arbitrary-state finiteness.
"""
from __future__ import annotations
import random


def raw_step(a: int, b: int, chi: int, a2: int, b2: int):
    num = 2 * chi + (1 << b2) - (1 << a2)
    if num % 3:
        return None
    return num // 3


def p(v: int) -> int:
    return min(0, v)


def delta(v: int) -> int:
    return (1 << max(v, 0)) - (1 << max(-v, 0))


def normalize(a: int, b: int, chi: int):
    m = min(a, b)
    den = 1 << m
    assert chi % den == 0
    return b - a, chi // den


def normalized_step(v: int, c: int, t: int, v2: int):
    # a decreases by t; v=b-a changes to v2.
    # Feasibility of b2 is checked by the caller; this is the arithmetic map.
    exponent = 1 + t + p(v) - p(v2)
    assert exponent >= 0
    num = (1 << exponent) * c + delta(v2)
    if num % 3:
        return None
    return num // 3


def selftest() -> None:
    rng = random.Random(20260910)

    # Invariant and normalized transition versus raw chi transition.
    checks = 0
    for _ in range(100_000):
        a = rng.randrange(0, 16)
        b = rng.randrange(0, 16)
        m = min(a, b)
        c = rng.randrange(-5000, 5001)
        chi = (1 << m) * c
        a2 = rng.randrange(a + 1)
        b2 = rng.randrange(b + 1)
        raw = raw_step(a, b, chi, a2, b2)
        v, c0 = normalize(a, b, chi)
        t = a - a2
        v2 = b2 - a2
        norm = normalized_step(v, c0, t, v2)
        assert (raw is None) == (norm is None)
        if raw is not None:
            vv, cc = normalize(a2, b2, raw)
            assert vv == v2
            assert cc == norm
        checks += 1

    # Exact rank-shift conjugacy: (a,b,chi)->(a+s,b+s,2^s chi).
    for _ in range(20_000):
        a = rng.randrange(0, 10)
        b = rng.randrange(0, 10)
        chi = rng.randrange(-10000, 10001)
        a2 = rng.randrange(a + 1)
        b2 = rng.randrange(b + 1)
        s = rng.randrange(0, 6)
        x = raw_step(a, b, chi, a2, b2)
        y = raw_step(a + s, b + s, chi << s, a2 + s, b2 + s)
        assert (x is None) == (y is None)
        if x is not None:
            assert y == (x << s)

    # Carry-residue shift: chi -> chi + m*3^r preserves a fixed future
    # divisibility path and shifts terminal credit by m*2^r.
    for r in range(1, 9):
        for _ in range(5000):
            a = rng.randrange(0, 8)
            b = rng.randrange(0, 8)
            chi = rng.randrange(-2000, 2001)
            mshift = rng.randrange(-4, 5)
            aa, bb = a, b
            path = []
            for _level in range(r):
                a2 = rng.randrange(aa + 1)
                b2 = rng.randrange(bb + 1)
                path.append((a2, b2))
                aa, bb = a2, b2

            def follow(start):
                ca, cb, cur = a, b, start
                for a2, b2 in path:
                    cur = raw_step(ca, cb, cur, a2, b2)
                    if cur is None:
                        return None
                    ca, cb = a2, b2
                return cur + (1 << cb) - (1 << ca)

            x = follow(chi)
            y = follow(chi + mshift * (3 ** r))
            assert (x is None) == (y is None)
            if x is not None:
                assert y - x == mshift * (2 ** r)

    print(f"PASS normalized bulk recurrence identities; random transition checks={checks}")


if __name__ == "__main__":
    selftest()
