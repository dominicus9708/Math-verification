#!/usr/bin/env python3
"""Exact universal-weak prefix first-hit bound for accelerated Collatz states.

For a coefficient-surviving state (k,q;r,y), let
    a_j = min{a: 3**a >= 2**j} = ceil(j log_3 2)
and slack s=q-a_k.

For a prefix horizon ell>=1 define the universal weak kernel by
    s + Q_j(x) >= floor(j log_3 2) = a_j-1
for every 1<=j<=ell, where Q_j(x) is the number of odd accelerated
steps in the first j steps from x.

The exact prefix first-hit lower bound is
    L_ell = min{u in [0,2**ell):
                y + 3**q*u (mod 2**ell) lies in the weak kernel}.
Then every full target descendant has canonical start at least
    r + 2**k * L_ell.

All arithmetic and barrier tests are exact integers. No floating logs are used.
"""

from __future__ import annotations

import argparse


def qmin_table(n: int) -> list[int]:
    """a[j] = least q with 3**q >= 2**j, for 0<=j<=n."""
    a = [0] * (n + 1)
    q = 0
    p3 = 1
    for j in range(1, n + 1):
        target = 1 << j
        while p3 < target:
            q += 1
            p3 *= 3
        a[j] = q
    return a


def weak_survives(x: int, s: int, ell: int, a: list[int]) -> bool:
    """Check s+Q_j(x) >= floor(j log_3 2)=a[j]-1 for j<=ell."""
    odd = 0
    v = x
    for j in range(1, ell + 1):
        if v & 1:
            odd += 1
            v = (3 * v + 1) >> 1
        else:
            v >>= 1
        if s + odd < a[j] - 1:
            return False
    return True


def prefix_first_hit(k: int, q: int, y: int, ell: int) -> tuple[int, int]:
    if ell < 1:
        raise ValueError("ell must be positive")
    a = qmin_table(max(k, ell))
    s = q - a[k]
    if s < 0:
        raise ValueError("input state is below the coefficient barrier at depth k")

    mod = 1 << ell
    eta = y % mod
    g = pow(3, q, mod)

    for u in range(mod):
        x = (eta + g * u) % mod
        if weak_survives(x, s, ell, a):
            return u, s
    raise AssertionError("weak kernel must be nonempty")


def monotone_profile(k: int, q: int, r: int, y: int, max_ell: int) -> list[tuple[int,int,int]]:
    out: list[tuple[int,int,int]] = []
    prev = -1
    for ell in range(1, max_ell + 1):
        L, _s = prefix_first_hit(k, q, y, ell)
        if L < prev:
            raise AssertionError(f"nonmonotone L at ell={ell}: {L} < {prev}")
        prev = L
        out.append((ell, L, r + (1 << k) * L))
    return out


def self_test() -> None:
    # Exact depth-five examples independently checked in Wolfram.
    p7 = monotone_profile(5, 4, 7, 20, 4)
    assert [x[1] for x in p7] == [0, 1, 1, 2], p7

    p15 = monotone_profile(5, 4, 15, 40, 2)
    assert [x[1] for x in p15] == [0, 1], p15

    p27 = monotone_profile(5, 4, 27, 71, 10)
    assert all(x[1] == 0 for x in p27), p27


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--q", type=int, default=4)
    ap.add_argument("--r", type=int, default=7)
    ap.add_argument("--y", type=int, default=20)
    ap.add_argument("--max-ell", type=int, default=10)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("self_test=ok")

    print("ell,L_ell,canonical_start_lower_bound")
    for ell, L, bound in monotone_profile(args.k, args.q, args.r, args.y, args.max_ell):
        print(f"{ell},{L},{bound}")


if __name__ == "__main__":
    main()
