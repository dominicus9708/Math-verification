#!/usr/bin/env python3
"""Exact dangerous-axis dimension for accelerated Collatz coefficient crossing.

For q odd entries at the first coefficient crossing, let
    sigma = ceil(q*log2(3)),
    D = 2**sigma - 3**q > 0.
An elementary coordinate shift at odd-position coordinate i is potentially capable
of reversing the order of canonical start x and descent margin z=x-y only if
    3**(q-i) >= D.
Hence
    h(q) = #{1<=i<=q : 3**(q-i) >= D}.

All comparisons below use Python big integers. Floating point is used only to seed
an integer exponent estimate, which is then corrected by exact comparisons.
"""

from __future__ import annotations
import argparse
import math

LOG2_3 = math.log2(3.0)


def sigma_exact(q: int) -> int:
    p = 3 ** q
    k = int(q * LOG2_3)
    while (1 << k) >= p:
        k -= 1
    while (1 << (k + 1)) < p:
        k += 1
    return k + 1


def ceil_log3_exact(n: int) -> int:
    if n <= 1:
        return 0
    # Seed from bit length, then certify with exact powers.
    e = max(0, int((n.bit_length() - 1) / LOG2_3))
    p = 3 ** e
    while p < n:
        e += 1
        p *= 3
    while e > 0 and p // 3 >= n:
        p //= 3
        e -= 1
    return e


def dangerous_dimension(q: int) -> tuple[int, int, int]:
    if q < 1:
        raise ValueError("q must be positive")
    sigma = sigma_exact(q)
    D = (1 << sigma) - 3 ** q
    e = ceil_log3_exact(D)
    h = max(0, q - e)
    return h, sigma, D


def scan_records(limit: int):
    record = -1
    for q in range(1, limit + 1):
        h, sigma, D = dangerous_dimension(q)
        if h > record:
            record = h
            yield q, h, sigma, D


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=2000,
                    help="scan record h(q) values through this q")
    ap.add_argument("--q", type=int, action="append", default=[],
                    help="also print exact h(q) for a selected q; repeatable")
    args = ap.parse_args()

    print("record increases")
    for q, h, sigma, D in scan_records(args.limit):
        print(f"q={q:8d} h={h:3d} sigma={sigma:8d} D_bits={D.bit_length():8d}")

    if args.q:
        print("\nselected q")
        for q in args.q:
            h, sigma, D = dangerous_dimension(q)
            print(f"q={q:8d} h={h:3d} sigma={sigma:8d} D_bits={D.bit_length():8d}")


if __name__ == "__main__":
    main()
