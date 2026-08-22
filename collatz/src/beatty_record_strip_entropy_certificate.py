#!/usr/bin/env python3
"""Exact finite regression for record first-passage words in a Beatty strip.

Let b_k=ceil(k log_3 2).  At record height r and mechanical phase s,
write

    g_j = q_j - (b_(s+j)-b_s).

A record first-passage word of length L stays in the strip

    -r <= g_j <= 0   for j<L,

and exits through g_L=1.  Equivalently y_j=-g_j stays in {0,...,r}
and exits through y=-1 on the final plateau-odd step.

The companion note proves a uniform O((r+1)^(-2)) entropy gap using a
Bernoulli(alpha) interval anti-concentration bound.  This script checks the
exact finite transfer counts and canonical-residue minima used as regression
examples.  It is not the proof of the all-L analytic bound.
"""

from __future__ import annotations


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        target = 1 << k
        while p3 < target:
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(1600)


def strip_count(L: int, r: int, s: int = 0) -> int:
    if min(L, r, s) < 0:
        raise ValueError
    # y = D-q = -g in {0,...,r}; record starts at y=0.
    dp = [0] * (r + 1)
    dp[0] = 1

    for j in range(1, L):
        d = B[s + j] - B[s + j - 1]
        nd = [0] * (r + 1)
        for y, c in enumerate(dp):
            if not c:
                continue
            # parity 0: q unchanged, so y increases by d.
            y0 = y + d
            if y0 <= r:
                nd[y0] += c
            # parity 1: q increases, so y changes by d-1.
            y1 = y + d - 1
            if 0 <= y1 <= r:
                nd[y1] += c
        dp = nd

    # Exit to g=+1 means y=-1. This is possible only from y=0 by an odd
    # step on a mechanical plateau d=0.
    dlast = B[s + L] - B[s + L - 1]
    return dp[0] if dlast == 0 else 0


def unrestricted_first_passage_count(L: int, s: int = 0) -> int:
    # Same upper first-passage condition g<=0, but no lower strip wall.
    dp = [1]  # y=0
    for j in range(1, L):
        d = B[s + j] - B[s + j - 1]
        nd = [0] * (len(dp) + 1)
        for y, c in enumerate(dp):
            if not c:
                continue
            y0 = y + d
            nd[y0] += c
            y1 = y + d - 1
            if y1 >= 0:
                nd[y1] += c
        dp = nd
    return dp[0] if B[s + L] == B[s + L - 1] else 0


def canonical_residue(bits: list[int]) -> int:
    L = len(bits)
    Q = sum(bits)
    R = 0
    odd_pos = [i for i, bit in enumerate(bits) if bit]
    for i, p in enumerate(odd_pos, start=1):
        R += 3 ** (Q - i) * (1 << p)
    mod = 1 << L
    r = (-R * pow(3, -Q, mod)) % mod
    return mod if r == 0 else r


def brute_count_min(L: int, r: int, s: int = 0) -> tuple[int, int | None]:
    if L > 20:
        raise ValueError("brute residue scan is intentionally limited to L<=20")
    count = 0
    best = None
    for mask in range(1 << L):
        q = 0
        ok = True
        bits = [(mask >> j) & 1 for j in range(L)]
        for j, bit in enumerate(bits, start=1):
            q += bit
            g = q - (B[s + j] - B[s])
            if j < L:
                if not (-r <= g <= 0):
                    ok = False
                    break
            elif g != 1:
                ok = False
        if not ok:
            continue
        count += 1
        rr = canonical_residue(bits)
        if best is None or rr < best:
            best = rr
    return count, best


def main() -> None:
    expected_min = {
        0: {3: 7, 6: 27, 9: 251, 11: 2043, 14: 15355, 17: 89083, 19: 154619},
        1: {3: 7, 6: 27, 9: 54, 11: 73, 14: 94, 17: 82, 19: 110},
        2: {3: 7, 6: 27, 9: 54, 11: 73, 14: 94, 17: 82, 19: 108},
    }

    for r, rows in expected_min.items():
        for L, want_min in rows.items():
            count, got_min = brute_count_min(L, r)
            assert count == strip_count(L, r), (r, L, count, strip_count(L, r))
            assert got_min == want_min, (r, L, got_min, want_min)

    # Long exact transfer checkpoints.
    expected_counts = {
        (1, 120): 52021196476823417565319,
        (2, 120): 7874686249316026299051996699,
        (3, 120): 544957853673420220948411316659,
        (5, 120): 8163921856070439501923931001099,
    }
    for key, want in expected_counts.items():
        r, L = key
        got = strip_count(L, r)
        assert got == want, (r, L, got, want)

    assert unrestricted_first_passage_count(120) == 17254727620070642311953234924713

    print("Beatty record-strip transfer regression: PASS")
    for r in (1, 2, 3, 5, 10):
        L = 1201
        while B[L] != B[L - 1]:
            L += 1
        c = strip_count(L, r)
        rate = c.bit_length() / L  # coarse exact-bit diagnostic only
        print("r", r, "L", L, "count_bits", c.bit_length(), "coarse_rate", rate)


if __name__ == "__main__":
    main()
