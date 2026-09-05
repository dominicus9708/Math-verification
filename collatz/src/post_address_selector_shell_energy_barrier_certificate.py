#!/usr/bin/env python3
"""Exact certificate for the m=45 post-address selector shell-energy barrier.

The certificate checks two facts using only integer arithmetic:

1. every m=45 selector start lies strictly between 2^73 and 2^74 and the
   full selector span is <2^73, so for every shell K>=74 no top-bit sibling
   pair contains two selector atoms;
2. at H=900,K=74 the standard unsigned shellwise Cauchy product for one
   fixed 44-selector affine block is already >2^(2H), hence that particular
   bound is >1 and cannot close the post-address shell.

This is a proof-strategy barrier, not a proof of Collatz.
"""

from collections import defaultdict


M = 45
H = 900
K = 74
A_BLOCK = 1 << 44


def barriers(H: int) -> list[int]:
    b = [0] * (H + 1)
    q = 0
    p3 = 1
    for j in range(1, H + 1):
        while p3 < (1 << j):
            q += 1
            p3 *= 3
        b[j] = q
    return b


def forward_levels(H: int, b: list[int]):
    levels = [{0: 1}]
    cur = {0: 1}
    for j in range(1, H + 1):
        th = b[j]
        nxt = defaultdict(int)
        for q, c in cur.items():
            if q >= th:
                nxt[q] += c
            if q + 1 >= th:
                nxt[q + 1] += c
        cur = dict(nxt)
        levels.append(cur)
    return levels


def tail_counts(H: int, K: int, b: list[int]) -> dict[int, int]:
    f = {q: 1 for q in range(b[H], H + 1)}
    for j in range(H - 1, K - 1, -1):
        th = b[j + 1]
        nf: dict[int, int] = {}
        for q in range(max(0, b[j] - 1), j + 1):
            z = 0
            if q >= th:
                z += f.get(q, 0)
            if q + 1 >= th:
                z += f.get(q + 1, 0)
            if z:
                nf[q] = z
        f = nf
    return f


def survivor_boundary_square_sum(H: int, K: int, b, levels) -> int:
    F = tail_counts(H, K, b)
    a = b[K]
    total = 0
    for q, c in levels[K - 1].items():
        even = F.get(q, 0) if q >= a else 0
        odd = F.get(q + 1, 0) if q + 1 >= a else 0
        d = even - odd
        total += c * d * d
    return total


def main() -> None:
    p3 = 3**M
    nmin = 4 * p3 + 3
    nmax = 6 * p3 + 1
    span = nmax - nmin

    assert (1 << 73) < nmin
    assert nmax < (1 << 74)
    assert span < (1 << 73)

    # Therefore at K=74 all starts are in the upper half and no two starts
    # share a parent residue modulo 2^73.  For K>=75 all starts are below
    # 2^(K-1), and injectivity is immediate from nmax<2^74.
    assert nmin >= (1 << (K - 1))
    assert nmax < (1 << K)

    # Exact odd-shell energy for one fixed affine block.
    e_selector = (1 << (K - 1)) * A_BLOCK

    b = barriers(H)
    levels = forward_levels(H, b)
    sb = survivor_boundary_square_sum(H, K, b, levels)
    e_survivor = (1 << (K - 1)) * sb

    # The shellwise Cauchy contribution is
    # sqrt(E_selector*E_survivor)/2^H.  It exceeds one iff the square exceeds
    # 2^(2H).  No floating point is needed.
    assert e_selector * e_survivor > (1 << (2 * H))

    print("post-address selector shell-energy barrier: PASS")
    print("Nmin", nmin)
    print("Nmax", nmax)
    print("span", span)
    print("address shell K", K)
    print("normalized full-layer odd-shell energy = 2^(K-46) =", 1 << (K - 46))
    print("normalized one-block odd-shell energy = 2^(K-45) =", 1 << (K - 45))
    print("H=900,K=74 unsigned shellwise Cauchy bound > 1: PASS")


if __name__ == "__main__":
    main()
