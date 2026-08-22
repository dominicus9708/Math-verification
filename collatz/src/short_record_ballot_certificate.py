#!/usr/bin/env python3
"""Finite regression for the short-record ballot lower-bound mechanism.

The companion note proves the all-large-r theorem using the finite-variance
ballot theorem plus a maximal Hoeffding estimate.  This script verifies the
mechanical connector facts and exact Bernoulli-alpha record masses on a finite
grid.  It is a regression diagnostic, not the analytic proof and not a proof
of the Collatz conjecture.
"""

from __future__ import annotations

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


B = barriers(5000)


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


def log_record_mass(s: int, r: int, L: int) -> float | None:
    c = strip_count(s, r, L)
    if c == 0:
        return None
    Q = B[s + L] - B[s] + 1
    return (
        math.log(c)
        + Q * math.log(ALPHA)
        + (L - Q) * math.log(1.0 - ALPHA)
    )


def mechanical_word(s: int, L: int) -> str:
    return "".join(str(B[s + j] - B[s + j - 1]) for j in range(1, L + 1))


def main() -> None:
    # Phase-uniform mechanical connector facts: no 00 and no 111.
    for s in range(0, 1000):
        w = mechanical_word(s, 20)
        assert "00" not in w, (s, w)
        assert "111" not in w, (s, w)

    # Exact finite masses: in the tested short regime L <= 2r, the quantity
    # P_alpha(record)*L^(3/2) stays bounded away from zero.
    rows = []
    global_min = float("inf")
    for r in (10, 20, 40, 80, 120):
        vals = []
        lo = max(10, r // 2)
        hi = 2 * r
        for s in range(20):
            for L in range(lo, hi + 1):
                lm = log_record_mass(s, r, L)
                if lm is None:
                    continue
                scaled = math.exp(lm) * (L ** 1.5)
                vals.append(scaled)
                global_min = min(global_min, scaled)
        assert vals
        rows.append((r, min(vals), max(vals), len(vals)))

    # The numerical constant is a regression checkpoint only.
    assert global_min > 0.50

    print("short-record ballot regression: PASS")
    print("alpha", ALPHA)
    print("global_min_P_times_L_3over2", global_min)
    for row in rows:
        print("r min_scaled max_scaled samples", *row)


if __name__ == "__main__":
    main()
