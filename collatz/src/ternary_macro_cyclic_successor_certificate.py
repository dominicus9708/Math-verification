#!/usr/bin/env python3
"""
Exact finite certificate for the cyclic-successor form of the ternary-syndrome
macro min-plus problem.

For an admissible B-bit canonical residue set R, current ternary modulus M=3^a,
and syndrome rho, the least progression member surviving B steps is

    rho + M * min_{r in R} [(r-rho) M^{-1}]_(2^B).

After scaling R and rho by M^{-1} modulo 2^B, the bracketed minimum is exactly
cyclic successor distance.  The script cross-checks this set formula against an
independent best-first parity-cylinder solver on a finite grid and verifies the
translation/query conjugacy identity exactly.
"""

from __future__ import annotations

import heapq
from itertools import product


def barrier_table(n: int) -> list[int]:
    out = [0] * (n + 1)
    p3 = 1
    q = 0
    for k in range(1, n + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


def canonical_word(bits):
    r = 1
    y = 1
    q = 0
    for k, bit in enumerate(bits):
        carry = bit ^ (y & 1)
        if carry:
            r += 1 << k
            y += 3 ** q
        if bit == 0:
            y //= 2
        else:
            y = (3 * y + 1) // 2
            q += 1
    return r


def admissible_residues(s: int, h: int, B: int) -> list[int]:
    barrier = barrier_table(s + B + 2)
    out = []
    for bits in product((0, 1), repeat=B):
        q = 0
        ok = True
        for k, bit in enumerate(bits, 1):
            q += bit
            if q < barrier[s + k] - barrier[s] - h:
                ok = False
                break
        if ok:
            out.append(canonical_word(bits))
    return sorted(set(out))


def cyclic_successor_distance(xi: int, A: list[int], N: int) -> int:
    return min((z - xi) % N for z in A)


def set_formula(s: int, h: int, B: int, a: int, rho: int) -> int:
    N = 1 << B
    M = 3 ** a
    invM = pow(M, -1, N)
    R = admissible_residues(s, h, B)
    A = sorted({(invM * r) % N for r in R})
    xi = (invM * rho) % N
    J = cyclic_successor_distance(xi, A, N)
    return rho + M * J


def best_first(s: int, h: int, B: int, a: int, rho: int) -> int:
    M = 3 ** a
    barrier = barrier_table(s + B + 2)

    def key(k: int, r: int) -> int:
        p2 = 1 << k
        t = ((rho - r) % M) * pow(p2, -1, M) % M
        return r + p2 * t

    # key, r, k, q, endpoint
    pq = [(key(0, 1), 1, 0, 0, 1)]
    while pq:
        kval, r, k, q, y = heapq.heappop(pq)
        if k == B:
            return kval

        for bit in (0, 1):
            rr, yy, qq = r, y, q
            carry = bit ^ (yy & 1)
            if carry:
                rr += 1 << k
                yy += 3 ** qq

            kk = k + 1
            if bit == 0:
                yy //= 2
            else:
                yy = (3 * yy + 1) // 2
                qq += 1

            if qq >= barrier[s + kk] - barrier[s] - h:
                heapq.heappush(pq, (key(kk, rr), rr, kk, qq, yy))

    raise RuntimeError("empty admissible language")


def translation_check(A: list[int], xi: int, delta: int, N: int) -> None:
    shifted = [((z + delta) % N) for z in A]
    lhs = cyclic_successor_distance(xi, shifted, N)
    rhs = cyclic_successor_distance((xi - delta) % N, A, N)
    assert lhs == rhs


def main() -> None:
    formula_checks = 0
    translation_checks = 0

    for B in (5, 7, 10):
        N = 1 << B
        for s in range(0, 4):
            for h in range(0, 2):
                R = admissible_residues(s, h, B)
                if not R:
                    continue
                for a in range(1, 4):
                    M = 3 ** a
                    invM = pow(M, -1, N)
                    A = sorted({(invM * r) % N for r in R})
                    for rho in range(1, M):
                        got = set_formula(s, h, B, a, rho)
                        want = best_first(s, h, B, a, rho)
                        assert got == want
                        formula_checks += 1

                        xi = (invM * rho) % N
                        for delta in (0, 1, 2, 4, N // 2, N - 1):
                            translation_check(A, xi, delta % N, N)
                            translation_checks += 1

    print(f"formula_checks={formula_checks}")
    print(f"translation_checks={translation_checks}")
    print("ternary macro cyclic-successor certificate: PASS")


if __name__ == "__main__":
    main()
