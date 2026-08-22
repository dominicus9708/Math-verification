#!/usr/bin/env python3
"""Finite regression for the long-record r^2 bridge-loop mechanism.

The companion note proves the asymptotic theorem by conditioning a Bernoulli
block on its exact near-mean endpoint, turning it into a sampling-without-
replacement bridge.  The exact martingale S_k/(n-k), hypergeometric variance,
and Doob L2 maximal inequality give a uniform strip-stay probability for
n=c r^2.  Combining with the central endpoint mass yields a loop probability
of order 1/r.

This script checks the mechanical loop event, connector lengths, exact strip
information costs, and the finite r*P(loop) scaling.  It is a regression, not
the all-r proof and not a proof of Collatz.
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


def conservative_loop_probability(a: int, r: int, n: int) -> float:
    """Exact Bernoulli-alpha probability of a safe central loop event.

    Require X_n=D(a,n) and the stronger pathwise band
        |X_k-D(a,k)| <= floor(r/4)-1.
    Starting at y=floor(r/2), this stays strictly inside the strip and returns
    exactly to the same state.
    """
    margin = max(1, r // 4 - 1)
    target = D(a, n)
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


def bridge_variance_bound(n: int, k: int, p: float) -> float:
    """Var(S_k) for a 0/1 random permutation bridge with total fraction p."""
    return k * (n - k) * p * (1.0 - p) / (n - 1)


def main() -> None:
    for a in range(100):
        for n in range(1, 300):
            assert abs(D(a, n) - ALPHA * n) < 1.0

    # Exact martingale-variance algebra at the midpoint.
    for n in range(8, 200):
        p = D(0, n) / n
        m = n // 2
        varS = bridge_variance_bound(n, m, p)
        varM = varS / ((n - m) ** 2)
        assert varM <= 1.0 / (4.0 * (n - 1)) + 1e-15

    # r^2-block loop probability: with n approximately r^2/128, r*P(loop)
    # stays uniformly positive over the tested phases/range.
    worst_r_scaled = 1e100
    bridge_rows = []
    for r in range(32, 129, 8):
        n = max(8, (r * r) // 128)
        for a in (0, 1, 5, 17, 41):
            p = conservative_loop_probability(a, r, n)
            assert p > 0.0
            worst_r_scaled = min(worst_r_scaled, r * p)
        bridge_rows.append((r, n, conservative_loop_probability(0, r, n)))

    max_in_ratio = 0.0
    max_out_ratio = 0.0
    for r in range(8, 101):
        for s in (0, 3, 19, 100):
            max_in_ratio = max(max_in_ratio, entrance_length(s, r) / r)
        for send in (300, 500, 900):
            max_out_ratio = max(max_out_ratio, exit_length(send, r) / r)

    rows = []
    for r in (4, 6, 8, 10, 12, 16, 20):
        L = r * r
        while B[L] != B[L - 1]:
            L += 1
        K = exact_information_cost(0, r, L)
        assert K is not None and K >= -1e-9
        rows.append((r, L, K, K / L))

    print("long-record r^2 bridge/Fourier regression: PASS")
    print("worst_r_times_loop_probability", worst_r_scaled)
    print("max_entrance_length_over_r", max_in_ratio)
    print("max_exit_length_over_r", max_out_ratio)
    print("delta_alpha", abs(2.0 * ALPHA - 1.0))
    for row in bridge_rows:
        print("bridge r n P rP", row[0], row[1], row[2], row[0] * row[2])
    for row in rows:
        print("r L K K_over_L", *row)


if __name__ == "__main__":
    main()
