#!/usr/bin/env python3
"""Exact-count cyclic-successor Bellman verifier for a fixed first crossing.

This is a reference verifier for the formulas in
2026-08-09-first-cross-exact-count-bellman.md.  It is exact but not intended as
an asymptotically efficient solver; q=29 can visit millions of memoized states.
"""

from functools import lru_cache
import argparse

INF = None


def sigma_of_q(q: int) -> int:
    # 3**q is never a power of two, so bit_length is ceil(log2(3**q)).
    return (3 ** q).bit_length()


def prefix_state(odd_positions):
    """Return (k,q,r,y) for the parity prefix ending at the last fixed odd."""
    if not odd_positions:
        return 0, 0, 0, 0
    positions = set(odd_positions)
    k = max(positions) + 1
    q = 0
    r = 0
    y = 0
    for j in range(k):
        b = 1 if j in positions else 0
        c = b ^ (y & 1)
        if c:
            r += 1 << j
            y += 3 ** q
        if b == 0:
            y //= 2
        else:
            y = (3 * y + 1) // 2
            q += 1
    return k, q, r, y


def solve(Q: int, odd_positions):
    sigma = sigma_of_q(Q)
    k0, q0, r0, y0 = prefix_state(odd_positions)
    m0 = sigma - k0
    u0 = Q - q0
    if m0 < 0 or u0 < 0 or u0 > m0:
        raise ValueError("prefix cannot extend to the requested first-crossing layer")

    if m0:
        mod = 1 << m0
        xi0 = (pow(3, -q0, mod) * (y0 % mod)) % mod
    else:
        xi0 = 0

    @lru_cache(maxsize=None)
    def J(k: int, q: int, m: int, u: int, xi: int):
        if m == 0:
            return 0 if u == 0 else INF
        if u < 0 or u > m:
            return INF

        M = 1 << m
        child_mod = 1 << (m - 1) if m > 1 else 1
        best = INF

        # E channel.  At m==1 this is the terminal crossing step, so the
        # intermediate coefficient-survival test is intentionally omitted.
        if u <= m - 1 and (m == 1 or 3 ** q >= 2 ** (k + 1)):
            bit = xi & 1
            h = ((xi + 1) // 2) % child_mod if child_mod > 1 else 0
            sub = J(k + 1, q, m - 1, u, h)
            if sub is not INF:
                cand = 2 * sub + bit
                best = cand if best is INF else min(best, cand)

        # O channel.
        if u >= 1 and (m == 1 or 3 ** (q + 1) >= 2 ** (k + 1)):
            g = pow(3, -(q + 1), M)
            t = (xi + g) % M
            bit = t & 1
            h = ((t + 1) // 2) % child_mod if child_mod > 1 else 0
            sub = J(k + 1, q + 1, m - 1, u - 1, h)
            if sub is not INF:
                cand = 2 * sub + bit
                best = cand if best is INF else min(best, cand)

        return best

    lift = J(k0, q0, m0, u0, xi0)
    if lift is INF:
        return {
            "Q": Q, "sigma": sigma, "prefix": tuple(odd_positions),
            "state": (k0, q0, r0, y0), "J": None, "x_star": None,
            "cache_states": J.cache_info().currsize,
        }

    return {
        "Q": Q, "sigma": sigma, "prefix": tuple(odd_positions),
        "state": (k0, q0, r0, y0), "J": lift,
        "x_star": r0 + (1 << k0) * lift,
        "cache_states": J.cache_info().currsize,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("Q", type=int)
    ap.add_argument("prefix", help="comma-separated zero-based odd positions, e.g. 0,1,2")
    args = ap.parse_args()
    positions = tuple(int(x) for x in args.prefix.split(",") if x != "")
    print(solve(args.Q, positions))


if __name__ == "__main__":
    main()
