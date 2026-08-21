#!/usr/bin/env python3
"""Finite regression for the sqrt-L corridor bridge construction.

The companion note proves the all-length statement. This script checks:
- exact Beatty centering |D_a(n)-alpha*n|<1;
- no-00 / no-111 mechanical connector bounds;
- exact conditioned bridge martingale identity in rational arithmetic on small n;
- finite record-strip information-cost trends in the short-width regime.

This is a regression certificate, not the all-length proof and not a proof of
Collatz.
"""

from __future__ import annotations

from fractions import Fraction
import math

ALPHA = math.log(2.0) / math.log(3.0)


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(8000)


def D(a: int, n: int) -> int:
    return B[a + n] - B[a]


def strip_count(s: int, r: int, L: int) -> int:
    dp = [0] * (r + 1)
    dp[0] = 1
    for j in range(1, L):
        d = B[s + j] - B[s + j - 1]
        nd = [0] * (r + 1)
        for y, c in enumerate(dp):
            if not c:
                continue
            y0 = y + d
            y1 = y + d - 1
            if 0 <= y0 <= r:
                nd[y0] += c
            if 0 <= y1 <= r:
                nd[y1] += c
        dp = nd
    return dp[0] if B[s + L] == B[s + L - 1] else 0


def exact_information_cost(s: int, r: int, L: int) -> float | None:
    count = strip_count(s, r, L)
    if count == 0:
        return None
    Q = D(s, L) + 1
    log_mass = (
        math.log(count)
        + Q * math.log(ALPHA)
        + (L - Q) * math.log(1.0 - ALPHA)
    )
    return -log_mass


def check_bridge_martingale(n: int, total: int) -> None:
    """Check E[S_{k+1}/(n-k-1)|X_k=x]=S_k/(n-k)."""
    assert 0 < total < n
    for k in range(0, n - 1):
        xmin = max(0, total - (n - k))
        xmax = min(k, total)
        for x in range(xmin, xmax + 1):
            remain = n - k
            p1 = Fraction(total - x, remain)
            p0 = 1 - p1

            S = Fraction(x * n - k * total, n)
            lhs = Fraction(0, 1)

            # next bit zero
            S0 = Fraction(x * n - (k + 1) * total, n)
            lhs += p0 * S0 / (n - k - 1)

            # next bit one
            S1 = Fraction((x + 1) * n - (k + 1) * total, n)
            lhs += p1 * S1 / (n - k - 1)

            rhs = S / (n - k)
            assert lhs == rhs, (n, total, k, x, lhs, rhs)


def main() -> None:
    # Exact mechanical forbidden patterns and centering regression.
    for s in range(500):
        for j in range(1, 500):
            assert abs(D(s, j) - ALPHA * j) < 1.0
        for j in range(1, 500):
            if j + 2 <= 500:
                bits2 = [B[s + j + z] - B[s + j + z - 1] for z in range(2)]
                assert bits2 != [0, 0]
            if j + 3 <= 500:
                bits3 = [B[s + j + z] - B[s + j + z - 1] for z in range(3)]
                assert bits3 != [1, 1, 1]

    # Exact conditional bridge martingale on small rational examples.
    for n in range(4, 30):
        target = round(ALPHA * n)
        target = max(1, min(n - 1, target))
        check_bridge_martingale(n, target)

    # Finite information-cost trend with r chosen larger than sqrt(L).
    rows = []
    for L0 in (60, 100, 160, 240, 360, 500):
        L = L0
        while B[L] != B[L - 1]:
            L += 1
        r = max(8, math.ceil(3.0 * math.sqrt(L)))
        K = exact_information_cost(0, r, L)
        assert K is not None and K >= -1e-9
        rows.append((r, L, K, K / L, K / math.sqrt(L)))

    print("unbounded record corridor bridge regression: PASS")
    for row in rows:
        print("r L K K_over_L K_over_sqrtL", *row)


if __name__ == "__main__":
    main()
