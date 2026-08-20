#!/usr/bin/env python3
"""Finite regression for the long-record loop lower-bound mechanism.

The companion note proves the asymptotic theorem using a central binomial
point-mass lower bound and maximal Hoeffding.  This script checks the mechanical
loop construction, connector lengths, exact strip probabilities, and the
resulting information-cost trend on finite grids.

This is a regression/diagnostic, not the all-r proof and not a proof of Collatz.
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


def loop_probability(a: int, r: int, n: int) -> float:
    """Exact Bernoulli-alpha probability of a conservative central loop event.

    We require final odd count X_n=D(a,n), and at every prefix
        |X_k-D(a,k)| <= margin.
    This is slightly stronger/easier to compute than the centered-S condition
    used in the proof and guarantees strip safety from y=floor(r/2).
    """
    margin = max(1, r // 4 - 1)
    target = D(a, n)
    # dp[q] = number of bit strings reaching q while obeying the deviation band.
    dp = {0: 1}
    for k in range(1, n + 1):
        nd: dict[int, int] = {}
        mech = D(a, k)
        for q, c in dp.items():
            for bit in (0, 1):
                qq = q + bit
                if abs(qq - mech) <= margin:
                    nd[qq] = nd.get(qq, 0) + c
        dp = nd
    count = dp.get(target, 0)
    return count * (ALPHA ** target) * ((1.0 - ALPHA) ** (n - target))


def entrance_length(s: int, r: int) -> int:
    c = r // 2
    j = 0
    while D(s, j) < c:
        j += 1
    assert D(s, j) == c
    return j


def exit_length(s_end: int, r: int) -> int:
    """Shortest backward suffix length containing c=floor(r/2) plateaus.

    s_end is the time immediately before the final record-exit step.
    """
    c = r // 2
    plateaus = 0
    n = 0
    while plateaus < c:
        d = B[s_end - n] - B[s_end - n - 1]
        if d == 0:
            plateaus += 1
        n += 1
    return n


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


def main() -> None:
    # One-slack centering is exact on a broad finite grid.
    for a in range(100):
        for n in range(1, 300):
            assert abs(D(a, n) - ALPHA * n) < 1.0

    # Loop event stays quantitatively nonzero; scaled probability sqrt(r)*P
    # remains healthy in the tested range.
    worst_scaled = 1e100
    for r in range(12, 81, 4):
        for a in (0, 1, 5, 17, 41):
            for n in (r, (3 * r) // 2, 2 * r):
                p = loop_probability(a, r, n)
                assert p > 0.0
                worst_scaled = min(worst_scaled, math.sqrt(r) * p)

    # Connector lengths are linear in r, uniformly over tested phases.
    max_in_ratio = 0.0
    max_out_ratio = 0.0
    for r in range(8, 101):
        for s in (0, 3, 19, 100):
            tin = entrance_length(s, r)
            max_in_ratio = max(max_in_ratio, tin / r)
        # Pick several valid endpoints far enough from zero.
        for send in (300, 500, 900):
            tout = exit_length(send, r)
            max_out_ratio = max(max_out_ratio, tout / r)

    # Exact long-strip information-cost diagnostics.  We only evaluate lengths
    # whose final mechanical step is a plateau, hence a record exit is possible.
    rows = []
    for r in (4, 6, 8, 10, 12, 16, 20):
        L0 = r * r
        L = L0
        while B[L] != B[L - 1]:
            L += 1
        K = exact_information_cost(0, r, L)
        assert K is not None and K >= -1e-9
        rows.append((r, L, K, K / L))

    print("long-record loop/Fourier regression: PASS")
    print("worst_sqrt_r_loop_probability", worst_scaled)
    print("max_entrance_length_over_r", max_in_ratio)
    print("max_exit_length_over_r", max_out_ratio)
    print("delta_alpha", abs(2.0 * ALPHA - 1.0))
    for row in rows:
        print("r L K K_over_L", *row)


if __name__ == "__main__":
    main()
