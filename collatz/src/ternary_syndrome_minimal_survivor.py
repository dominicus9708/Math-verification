#!/usr/bin/env python3
"""
Exact ternary-syndrome best-first certificate for the coefficient-survivor problem.

For
    S_{s,h}(J) = {x>=1 : q_j(x) >= b_{s+j}-b_s-h for 1<=j<=J},
define nu_{s,h}^{(a,c)}(J) as the least x in S_{s,h}(J) with
x == c (mod 3^a).

At a parity cylinder of depth k with least canonical representative r,
all starts in the cylinder are r + 2^k t. Because gcd(2^k,3^a)=1,
the least member of that cylinder in the target ternary residue class is
an exact monotone lower key. Best-first search by this key is therefore exact.
"""

from __future__ import annotations

import argparse
import heapq


def barrier_table(n: int) -> list[int]:
    b = [0] * (n + 1)
    p3 = 1
    q = 0
    for k in range(1, n + 1):
        p2 = 1 << k
        while p3 < p2:
            p3 *= 3
            q += 1
        b[k] = q
    return b


def syndrome_key(k: int, r: int, modulus: int, residue: int) -> int:
    if modulus == 1:
        return r
    p2 = 1 << k
    t = ((residue - r) % modulus) * pow(p2, -1, modulus) % modulus
    return r + p2 * t


def syndrome_min(s: int, h: int, J: int, a: int, c: int) -> tuple[int, int]:
    if min(s, h, J, a) < 0:
        raise ValueError("s,h,J,a must be nonnegative")

    modulus = 3 ** a
    residue = c % modulus if modulus > 1 else 0
    barrier = barrier_table(s + J + 2)

    # (syndrome-adjusted key, r, k, q, y)
    pq: list[tuple[int, int, int, int, int]] = [
        (syndrome_key(0, 1, modulus, residue), 1, 0, 0, 1)
    ]
    pops = 0

    while pq:
        key, r, k, q, y = heapq.heappop(pq)
        pops += 1
        if k == J:
            assert key % modulus == residue
            return key, pops

        p2k = 1 << k
        p3q = 3 ** q
        for bit in (0, 1):
            carry = bit ^ (y & 1)
            rr, yy, qq = r, y, q
            if carry:
                rr += p2k
                yy += p3q

            kk = k + 1
            if bit == 0:
                yy //= 2
            else:
                yy = (3 * yy + 1) // 2
                qq += 1

            required = barrier[s + kk] - barrier[s] - h
            if qq >= required:
                child_key = syndrome_key(kk, rr, modulus, residue)
                assert child_key >= key
                heapq.heappush(pq, (child_key, rr, kk, qq, yy))

    raise RuntimeError("empty survivor set in requested syndrome")


def ordinary_mu(J: int) -> tuple[int, int]:
    return syndrome_min(0, 0, J, 0, 0)


FIRST5 = (
    # r, q5, endpoint c, incoming h at phase s=5
    (7, 4, 20, 0),
    (15, 4, 40, 0),
    (27, 4, 71, 0),
    (31, 5, 242, 1),
)


def first5_branch_minima(K: int) -> list[tuple[int, int, int, int]]:
    if K < 5:
        raise ValueError("K must be at least 5")
    J = K - 5
    out = []
    for r, q5, c, hp in FIRST5:
        nu, pops = syndrome_min(5, hp, J, q5, c)
        delta = nu - c
        assert delta >= 0 and delta % (3 ** q5) == 0
        t = delta // (3 ** q5)
        x = r + 32 * t
        out.append((r, x, nu, pops))
    return out


def selfcheck() -> None:
    expected = {
        55: 27,
        105: 35655,
        155: 270271,
        200: 1126015,
        220: 1126015,
    }
    for K, want in expected.items():
        rows = first5_branch_minima(K)
        got = min(x for _, x, _, _ in rows)
        direct, _ = ordinary_mu(K)
        assert got == direct == want, (K, got, direct, want)
        print(f"K={K}: mu={got}")
        for r, x, nu, pops in rows:
            print(
                f"  r={r:2d} mod32: branch_min={x}, "
                f"syndrome_min={nu}, pops={pops}"
            )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selfcheck", action="store_true")
    ap.add_argument("--s", type=int)
    ap.add_argument("--h", type=int)
    ap.add_argument("--J", type=int)
    ap.add_argument("--a", type=int, default=0)
    ap.add_argument("--c", type=int, default=0)
    args = ap.parse_args()

    if args.selfcheck:
        selfcheck()
        return
    if args.s is None or args.h is None or args.J is None:
        ap.error("use --selfcheck or provide --s --h --J [--a --c]")

    value, pops = syndrome_min(args.s, args.h, args.J, args.a, args.c)
    print(f"nu={value}")
    print(f"pops={pops}")


if __name__ == "__main__":
    main()
