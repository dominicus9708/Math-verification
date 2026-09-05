#!/usr/bin/env python3
"""Exact single-class Hensel audit for the neutral Beatty tail.

This is a finite certificate / recurrence regression, NOT a Collatz proof.

Target parity word:
    first six bits are 1;
    thereafter e_j = b(j+1)-b(j),
where b(k)=min{q:3^q>=2^k}.
Hence for every k>=6 its odd count is q_k=b(k)+2 and its Beatty surplus is d=2.

For a length-k parity word with q ones and correction R, define its full-Hensel
class by R mod 3^q.  Let

    M(k,q,r) = maximum correction in that class,
    C(k,q,r) = number of words in that class.

The exact recurrence is

    (append 0) : (k-1,q,r) -> (k,q,r), R'=R
    (append 1) : R'=3R+2^(k-1).

Thus

    M(k,q,r)=max(
        M(k-1,q,r),
        3 M(k-1,q-1,(r-2^(k-1))/3 mod 3^(q-1)) + 2^(k-1)
    )

when the second branch satisfies r == 2^(k-1) (mod 3).  Counts satisfy the
same recursion with max replaced by sum.

Default MAX_K=75 is intentionally conservative for memory.  --max-k 95
reproduces the deeper audit recorded in the accompanying note, but Python's
memo table can be large.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations


def beatty_table(K: int) -> list[int]:
    b = [0] * (K + 1)
    q = 0
    p3 = 1
    for k in range(K + 1):
        target = 1 << k
        while p3 < target:
            p3 *= 3
            q += 1
        b[k] = q
    return b


def correction_from_positions(k: int, positions: tuple[int, ...]) -> int:
    S = set(positions)
    R = 0
    for i in range(k):
        if i in S:
            R = 3 * R + (1 << i)
    return R


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-k", type=int, default=75)
    ap.add_argument("--brute-check", type=int, default=18)
    args = ap.parse_args()
    K = args.max_k
    if K < 6:
        raise SystemExit("max-k must be at least 6")

    b = beatty_table(K)
    p3 = [1] * (K + 2)
    for i in range(1, len(p3)):
        p3[i] = p3[i - 1] * 3

    @lru_cache(maxsize=None)
    def class_count_max(k: int, q: int, r: int) -> tuple[int, int]:
        if q < 0 or q > k:
            return (0, -1)
        r %= p3[q]
        if k == 0:
            return (1, 0) if (q == 0 and r == 0) else (0, -1)

        count = 0
        max_R = -1

        # Last parity bit 0.
        if q <= k - 1:
            c0, m0 = class_count_max(k - 1, q, r)
            count += c0
            if m0 > max_R:
                max_R = m0

        # Last parity bit 1.
        if q >= 1:
            tw = 1 << (k - 1)
            if (r - tw) % 3 == 0:
                rp = ((r - tw) // 3) % p3[q - 1]
                c1, m1 = class_count_max(k - 1, q - 1, rp)
                if c1:
                    count += c1
                    cand = 3 * m1 + tw
                    if cand > max_R:
                        max_R = cand

        return count, max_R

    # Independent small-depth brute regression.
    brute_lim = min(max(0, args.brute_check), K)

    R = 0
    q = 0
    first_collision = None
    first_not_max = None

    print("k,q,b(k),d,class_count,is_max")
    for k in range(1, K + 1):
        # Position j=k-1.
        bit = 1 if k <= 6 else b[k] - b[k - 1]
        if bit:
            R = 3 * R + (1 << (k - 1))
            q += 1

        if k >= 6:
            assert q == b[k] + 2

        residue = R % p3[q]
        count, max_R = class_count_max(k, q, residue)

        if k <= brute_lim:
            brute_count = 0
            brute_max = -1
            for pos in combinations(range(k), q):
                Ru = correction_from_positions(k, pos)
                if Ru % p3[q] == residue:
                    brute_count += 1
                    brute_max = max(brute_max, Ru)
            assert (count, max_R) == (brute_count, brute_max)

        if count > 1 and first_collision is None:
            first_collision = k
        if max_R != R and first_not_max is None:
            first_not_max = k

        if k <= 22 or k % 5 == 0 or k == K:
            print(k, q, b[k], q - b[k], count, int(max_R == R), sep=",")

    info = class_count_max.cache_info()
    print("first_collision", first_collision)
    print("first_not_max", first_not_max)
    print("cache_misses", info.misses)
    print("cache_hits", info.hits)

    # The finite certificate claimed here: no collision and target remains
    # class-max throughout the requested horizon.
    assert first_collision is None
    assert first_not_max is None
    print("PASS")


if __name__ == "__main__":
    main()
