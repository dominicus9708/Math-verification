#!/usr/bin/env python3
"""Exact interval-count certificates for transformed Collatz suffix sets.

For
    S_{k,q,m} = 3^{-q} A_{k,q,m} mod 2^m,
this program computes
    N(k,q,m;a,L) = |S_{k,q,m} intersect I_{2^m}(a,L)|
without explicitly materializing S.

The E/O inverse images of a cyclic interval are cyclic intervals of roughly half
length, and their lengths sum to at most L.  Hence the uncached recursion has at
most O(m*L) nonempty nodes (ignoring integer bit complexity).

This is an exact finite certificate tool, not a Collatz proof.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


class IntervalCounter:
    def __init__(self, Kmax: int) -> None:
        self.pow3 = [1]
        for _ in range(Kmax + 3):
            self.pow3.append(3 * self.pow3[-1])

    @staticmethod
    def preimage_interval(a: int, L: int, c: int, m: int) -> tuple[int, int]:
        """Preimage of I(a,L) under u -> 2u+c mod 2^m."""
        assert m >= 1
        M = 1 << m
        Mh = 1 << (m - 1)
        t = (a - c) % M
        eps = t & 1
        ap = ((t + eps) >> 1) % Mh
        Lp = (L + 1 - eps) // 2
        return ap, Lp

    @lru_cache(maxsize=None)
    def count(self, k: int, q: int, m: int, a: int, L: int) -> int:
        if L == 0:
            return 0
        M = 1 << m
        if not (0 <= a < M and 0 <= L <= M):
            raise ValueError("invalid cyclic interval")
        if m == 0:
            return 1

        # Entire remaining tail is coefficient-safe.
        if self.pow3[q] >= 1 << (k + m):
            return L

        total = 0

        # E branch: c=0.
        if self.pow3[q] >= 1 << (k + 1):
            ap, Lp = self.preimage_interval(a, L, 0, m)
            total += self.count(k + 1, q, m - 1, ap, Lp)

        # O branch: c=-g, g=3^{-(q+1)} mod 2^m.
        if self.pow3[q + 1] >= 1 << (k + 1):
            g = pow(self.pow3[q + 1], -1, M)
            c = (-g) % M
            ap, Lp = self.preimage_interval(a, L, c, m)
            total += self.count(k + 1, q + 1, m - 1, ap, Lp)

        return total

    def certifies_J_ge(self, k: int, q: int, m: int, xi: int, L: int) -> bool:
        """Exact certificate for J_{k,q,m}(xi) >= L."""
        if L <= 0:
            return True
        M = 1 << m
        if L > M:
            return False
        return self.count(k, q, m, xi % M, L) == 0

    def certifies_block_J_ge(
        self, k: int, q: int, m: int, a: int, block_len: int, L: int
    ) -> bool:
        """Certify J(xi)>=L for every xi in I(a,block_len)."""
        M = 1 << m
        total_len = block_len + L - 1
        if block_len <= 0:
            return True
        if L <= 0:
            return True
        if total_len > M:
            return False
        return self.count(k, q, m, a % M, total_len) == 0


def accelerated_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def future_allowed_residues(k: int, q0: int, m: int) -> list[int]:
    """Direct exponential construction used only by self-test."""
    out = []
    for rho in range(1 << m):
        x = rho
        q = q0
        ok = True
        for j in range(1, m + 1):
            if x & 1:
                q += 1
            x = accelerated_step(x)
            if 3 ** q < 1 << (k + j):
                ok = False
                break
        if ok:
            out.append(rho)
    return out


def transformed_set(k: int, q: int, m: int) -> set[int]:
    if m == 0:
        return {0}
    M = 1 << m
    inv = pow(3 ** q, -1, M)
    return {(inv * rho) % M for rho in future_allowed_residues(k, q, m)}


def direct_count(S: set[int], a: int, L: int, M: int) -> int:
    return sum(1 for j in range(L) if (a + j) % M in S)


def self_test() -> None:
    C = IntervalCounter(16)
    for k in range(4):
        for q in range(k + 1):
            if 3 ** q < 1 << k:
                continue
            for m in range(6):
                M = 1 << m
                S = transformed_set(k, q, m)
                for a in range(M):
                    for L in range(M + 1):
                        got = C.count(k, q, m, a, L)
                        expected = direct_count(S, a, L, M)
                        assert got == expected, (k, q, m, a, L, got, expected)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=0)
    ap.add_argument("--q", type=int, default=0)
    ap.add_argument("--m", type=int, default=20)
    ap.add_argument("--a", type=int, default=0)
    ap.add_argument("--length", type=int, default=100)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("self_test=PASS")
        return

    C = IntervalCounter(args.k + args.m + 4)
    value = C.count(args.k, args.q, args.m, args.a % (1 << args.m), args.length)
    info = C.count.cache_info()
    print(
        f"count={value},cache_currsize={info.currsize},cache_hits={info.hits},"
        f"k={args.k},q={args.q},m={args.m},a={args.a},L={args.length}"
    )


if __name__ == "__main__":
    main()
