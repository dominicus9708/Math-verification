#!/usr/bin/env python3
"""Exact split / cyclic-successor verifier for coefficient-surviving Collatz states.

This is a proof-oriented finite verifier, not a scalable global solver.

For a target K and split k, m=K-k.  A split state (r,q,y) has final lifts
    r_C = r + 2**k * C,
and
    T**k(r_C) = y + 3**q * C.

Let A_{k,q,m} be the canonical suffix residues rho mod 2**m that preserve the
coefficient barrier through the remaining m steps.  Then the unique lift that
realizes rho is
    C = 3**(-q) * (rho-y) mod 2**m.
After transforming A by 3**(-q), the minimum C is a cyclic successor query.

All arithmetic and all barrier decisions are exact integers.
"""

from __future__ import annotations

import argparse
import bisect
from collections import defaultdict


def step(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def survives_with_initial_q(x: int, k: int, q: int, m: int) -> bool:
    """Whether the next m steps from x preserve the coefficient barrier."""
    for j in range(1, m + 1):
        if x & 1:
            q += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
        if 3 ** q < 1 << (k + j):
            return False
    return True


def prefix_states(k: int) -> list[tuple[int, int, int]]:
    """All canonical coefficient-surviving states (r,q,y) at depth k."""
    states = [(0, 0, 0)]
    pow3 = [1]
    for depth in range(k):
        while len(pow3) <= depth + 1:
            pow3.append(3 * pow3[-1])
        nxt: list[tuple[int, int, int]] = []
        for r, q, y in states:
            for b in (0, 1):
                c = b ^ (y & 1)
                rr = r + (c << depth)
                yy = y + c * pow3[q]
                qq = q
                if b == 0:
                    yy //= 2
                else:
                    yy = (3 * yy + 1) // 2
                    qq += 1
                if 3 ** qq >= 1 << (depth + 1):
                    nxt.append((rr, qq, yy))
        states = nxt
    return states


def future_residues(k: int, q: int, m: int) -> list[int]:
    """Explicit A_{k,q,m}; exponential diagnostic implementation."""
    return [
        rho
        for rho in range(1 << m)
        if survives_with_initial_q(rho, k, q, m)
    ]


def transformed_suffix_set(k: int, q: int, m: int) -> list[int]:
    M = 1 << m
    inv = pow(3 ** q, -1, M)
    return sorted((inv * rho) % M for rho in future_residues(k, q, m))


def cyclic_successor(S: list[int], xi: int, M: int) -> tuple[int, int]:
    """Return (distance, successor mod M)."""
    i = bisect.bisect_left(S, xi)
    if i < len(S):
        return S[i] - xi, S[i]
    return S[0] + M - xi, S[0]


def split_mu(K: int, k: int, show_profile: bool = False) -> tuple[int, dict[int, tuple[int, int, int]]]:
    if not (0 <= k <= K):
        raise ValueError("require 0 <= split <= K")
    m = K - k
    states = prefix_states(k)
    byq: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for st in states:
        byq[st[1]].append(st)

    best: int | None = None
    profile: dict[int, tuple[int, int, int]] = {}

    for q, layer in sorted(byq.items()):
        M = 1 << m
        inv = 1 if m == 0 else pow(3 ** q, -1, M)
        if m == 0:
            S = [0]
        else:
            S = transformed_suffix_set(k, q, m)

        # Same optimal successor is a certified dominance cell.
        cells: dict[int, tuple[int, int, int, int, int]] = {}
        for r, _q, y in layer:
            xi = 0 if m == 0 else (inv * (y % M)) % M
            J, s = cyclic_successor(S, xi, M)
            value = r + (1 << k) * J
            old = cells.get(s)
            if old is None or value < old[0]:
                cells[s] = (value, r, y, xi, J)
            if best is None or value < best:
                best = value

        profile[q] = (len(layer), len(S), len(cells))
        if show_profile:
            print(
                f"q={q},prefix={len(layer)},future={len(S)},"
                f"successor_cells={len(cells)}"
            )

    assert best is not None
    # r=0 represents the zero residue.  For K>=1 the coefficient barrier forces
    # positive odd starts for the global minimum, so the returned best is positive
    # in the intended uses.
    return best, profile


def brute_lift_J(k: int, q: int, y: int, m: int) -> int:
    """Independent direct lift scan for small self-tests."""
    for C in range(1 << m):
        if survives_with_initial_q(y + (3 ** q) * C, k, q, m):
            return C
    raise AssertionError("all-odd continuation should always give a feasible lift")


def self_test() -> None:
    # Endpoint-dominance counterexample: cyclic successor must recover J=2 and 1.
    for k, q, r, y, m, expected in [
        (10, 8, 127, 820, 5, 2),
        (10, 7, 383, 820, 5, 1),
    ]:
        M = 1 << m
        inv = pow(3 ** q, -1, M)
        S = transformed_suffix_set(k, q, m)
        xi = inv * (y % M) % M
        J, _ = cyclic_successor(S, xi, M)
        assert J == expected
        assert J == brute_lift_J(k, q, y, m)
        assert r + (1 << k) * J in (2175, 1407)

    # Exhaustive small split: compare cyclic formula with direct lift scans.
    K, k = 12, 6
    m = K - k
    cache: dict[int, list[int]] = {}
    for r, q, y in prefix_states(k):
        M = 1 << m
        inv = pow(3 ** q, -1, M)
        S = cache.setdefault(q, transformed_suffix_set(k, q, m))
        xi = inv * (y % M) % M
        J, _ = cyclic_successor(S, xi, M)
        assert J == brute_lift_J(k, q, y, m)

    # Known early minimal-survivor values.
    known = {5: 7, 6: 7, 7: 27, 10: 27, 15: 27, 20: 27}
    for K, expected in known.items():
        k = K // 2
        got, _ = split_mu(K, k)
        assert got == expected, (K, got, expected)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("K", type=int, nargs="?", default=20)
    ap.add_argument("--split", type=int, default=None)
    ap.add_argument("--profile", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("self_test=PASS")
        return

    k = args.K // 2 if args.split is None else args.split
    mu, profile = split_mu(args.K, k, args.profile)
    total_prefix = sum(x[0] for x in profile.values())
    total_cells = sum(x[2] for x in profile.values())
    print(f"K={args.K},split={k},mu={mu}")
    print(f"prefix_states={total_prefix},successor_cells={total_cells}")


if __name__ == "__main__":
    main()
