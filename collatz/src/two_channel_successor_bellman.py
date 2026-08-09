#!/usr/bin/env python3
"""Memoized two-channel Bellman verifier for the Collatz coefficient-survivor minimum.

The recurrence is derived from the transformed future suffix sets
    S_{k,q,m} = 3^{-q} A_{k,q,m} (mod 2^m)
and their E/O affine recursion.

For a cyclic successor query xi, J(k,q,m,xi) is the minimum future lift integer.
At the root,
    mu(K) = J(0,0,K,0).

This is an exact integer verifier.  It is not an asymptotic proof and may still
use exponentially many memo states for large K.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


class Solver:
    def __init__(self, K: int) -> None:
        if K < 1:
            raise ValueError("K must be positive")
        self.K = K
        self.pow3 = [1]
        for _ in range(K + 2):
            self.pow3.append(3 * self.pow3[-1])

    @lru_cache(maxsize=None)
    def J(self, k: int, q: int, m: int, xi: int) -> int:
        if m == 0:
            assert xi == 0
            return 0

        M = 1 << m
        Mh = 1 << (m - 1)
        best: int | None = None

        # E channel: transformed child set is 2*S_{k+1,q,m-1}.
        if self.pow3[q] >= 1 << (k + 1):
            bit = xi & 1
            h = ((xi + bit) >> 1) % Mh
            cand = 2 * self.J(k + 1, q, m - 1, h) + bit
            best = cand

        # O channel: transformed child set is
        # 2*S_{k+1,q+1,m-1} - 3^{-(q+1)} (mod 2^m).
        if self.pow3[q + 1] >= 1 << (k + 1):
            g = pow(self.pow3[q + 1], -1, M)
            t = (xi + g) % M
            bit = t & 1
            h = ((t + bit) >> 1) % Mh
            cand = 2 * self.J(k + 1, q + 1, m - 1, h) + bit
            if best is None or cand < best:
                best = cand

        if best is None:
            raise AssertionError("reachable Bellman state has no admissible child")
        return best

    def candidates(self, k: int, q: int, m: int, xi: int):
        """Return exact channel candidates for trace reconstruction."""
        if m == 0:
            return []
        M = 1 << m
        Mh = 1 << (m - 1)
        out = []

        if self.pow3[q] >= 1 << (k + 1):
            bit = xi & 1
            h = ((xi + bit) >> 1) % Mh
            child = self.J(k + 1, q, m - 1, h)
            out.append((2 * child + bit, 0, bit, k + 1, q, m - 1, h))

        if self.pow3[q + 1] >= 1 << (k + 1):
            g = pow(self.pow3[q + 1], -1, M)
            t = (xi + g) % M
            bit = t & 1
            h = ((t + bit) >> 1) % Mh
            child = self.J(k + 1, q + 1, m - 1, h)
            out.append((2 * child + bit, 1, bit, k + 1, q + 1, m - 1, h))

        return out

    def solve(self) -> int:
        return self.J(0, 0, self.K, 0)

    def trace(self):
        k = 0
        q = 0
        m = self.K
        xi = 0
        channels: list[int] = []
        lift_bits: list[int] = []

        while m > 0:
            target = self.J(k, q, m, xi)
            cands = sorted(self.candidates(k, q, m, xi), key=lambda z: (z[0], z[1]))
            chosen = next(z for z in cands if z[0] == target)
            _value, channel, bit, k, q, m, xi = chosen
            channels.append(channel)
            lift_bits.append(bit)

        return channels, lift_bits


def accelerated_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def verify_trace(K: int, mu: int, channels: list[int], lift_bits: list[int]) -> None:
    # Bellman lift bits are least-significant first and must reconstruct mu.
    reconstructed = sum(b << j for j, b in enumerate(lift_bits))
    assert reconstructed == mu, (reconstructed, mu)

    # Channel choices must be the actual K-step parity vector of mu.
    x = mu
    q = 0
    for j, b in enumerate(channels, start=1):
        assert (x & 1) == b, (j, x, b)
        if b:
            q += 1
        x = accelerated_step(x)
        assert 3 ** q >= 1 << j


def self_test() -> None:
    known = {
        5: 7,
        6: 7,
        7: 27,
        10: 27,
        15: 27,
        20: 27,
        24: 27,
        25: 27,
        28: 27,
        30: 27,
    }
    for K, expected in known.items():
        solver = Solver(K)
        got = solver.solve()
        assert got == expected, (K, got, expected)
        channels, bits = solver.trace()
        verify_trace(K, got, channels, bits)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("K", type=int, nargs="?", default=25)
    ap.add_argument("--trace", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("self_test=PASS")
        return

    solver = Solver(args.K)
    mu = solver.solve()
    info = solver.J.cache_info()
    print(f"K={args.K},mu={mu},cache_currsize={info.currsize},cache_hits={info.hits}")

    if args.trace:
        channels, bits = solver.trace()
        verify_trace(args.K, mu, channels, bits)
        print("parity_channels_lsf_time=" + "".join(map(str, channels)))
        print("binary_lift_bits_lsb_first=" + "".join(map(str, bits)))


if __name__ == "__main__":
    main()
