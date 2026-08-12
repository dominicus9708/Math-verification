#!/usr/bin/env python3
"""Exact certificate for the overlapping-window defect-density bound.

No floating point and no logarithm evaluation are used.

At the current upper-CF resonance, the rational DK certificate gives
    N < U_CERT < 2^75.
For a zero-defect odd event,
    x_q < 2 (N + H/3) < 2^76.

We use odd-event windows of length m=48.  Their zero-endpoint parity words
have time-expanded length at least 76, so each exact local parity word has
at most one positive representative below 2^76.

The critical valuation word is generated exactly from
    floor(q log_2 3) = bit_length(3^q) - 1.
Sturmian complexity gives exactly m+1 length-m factors.  Once all m+1
factors have been collected, a finite DP counts every nonnegative skew path
h_0=0, h_m=0 satisfying
    h_{i+1} <= h_i + r_i - 1,
classified by the number of positive internal heights.

The resulting capacities are inserted into the exact global incidence
inequality to obtain the least possible total defect count r_*.
"""

from collections import defaultdict

H = 137_528_045_312
A = 217_976_794_617
M = 48
U_CERT = 36_797_925_187_243_805_015_225


def floor_q_gamma(q: int) -> int:
    """floor(q log_2 3), exactly."""
    if q == 0:
        return 0
    return (3 ** q).bit_length() - 1


def critical_symbol(q: int) -> int:
    """Critical odd-to-odd binary exponent increment r_q in {1,2}."""
    return floor_q_gamma(q + 1) - floor_q_gamma(q)


def collect_critical_factors(m: int):
    """Collect all m+1 Sturmian factors; exact integer arithmetic only."""
    factors = set()
    q = 0
    target = m + 1
    while len(factors) < target:
        factors.add(tuple(critical_symbol(q + i) for i in range(m)))
        q += 1
    return sorted(factors), q


def skew_path_counts(rseq):
    """Count admissible h paths by number of positive internal coordinates.

    Conditions:
      h_0 = 0,
      h_m = 0,
      h_{i+1} >= 0,
      h_{i+1} <= h_i + r_i - 1.

    The last endpoint is forced to zero and is not counted as an internal
    positive coordinate.
    """
    m = len(rseq)
    dp = {(0, 0): 1}  # (current height, positive internal count) -> count

    for i, r in enumerate(rseq):
        nxt = defaultdict(int)
        last = i == m - 1
        for (h, j), count in dp.items():
            max_h_next = h + r - 1
            candidates = (0,) if last else range(max_h_next + 1)
            for h_next in candidates:
                j_next = j + (1 if (not last and h_next > 0) else 0)
                nxt[(h_next, j_next)] += count
        dp = nxt

    out = [0] * m
    for (h, j), count in dp.items():
        assert h == 0
        out[j] += count
    return out


def capacities(m: int):
    factors, scanned = collect_critical_factors(m)
    cap = [0] * m
    parity_lengths = defaultdict(int)

    for rseq in factors:
        parity_lengths[sum(rseq)] += 1
        local = skew_path_counts(rseq)
        for j, count in enumerate(local):
            cap[j] += count

    return cap, factors, parity_lengths, scanned


def min_incidence_cost(e: int, cap):
    """Greedy minimum of sum j*n_j for sum n_j >= e, 0<=n_j<=cap_j."""
    remaining = max(0, e)
    cost = 0
    for j, capacity in enumerate(cap):
        take = min(remaining, capacity)
        cost += j * take
        remaining -= take
        if remaining == 0:
            return cost
    raise RuntimeError("capacity table did not cover requested windows")


def threshold_r(m: int, cap):
    """Least r satisfying Phi(H-m-2r) <= (m-1)r."""
    lo, hi = 0, H
    while lo < hi:
        mid = (lo + hi) // 2
        zero_endpoint_lower = H - m - 2 * mid
        lhs = min_incidence_cost(zero_endpoint_lower, cap)
        rhs = (m - 1) * mid
        if lhs <= rhs:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    # Exact state-bound check:
    # 2(U + H/3) < 2^76  <=>  6U + 2H < 3*2^76.
    state_margin = 3 * (2 ** 76) - (6 * U_CERT + 2 * H)
    assert state_margin > 0

    cap, factors, parity_lengths, scanned = capacities(M)
    assert len(factors) == M + 1
    assert min(parity_lengths) >= 76

    r = threshold_r(M, cap)
    e = H - M - 2 * r
    lhs = min_incidence_cost(e, cap)
    rhs = (M - 1) * r

    # Minimality check.
    r_prev = r - 1
    e_prev = H - M - 2 * r_prev
    lhs_prev = min_incidence_cost(e_prev, cap)
    rhs_prev = (M - 1) * r_prev
    assert lhs <= rhs
    assert lhs_prev > rhs_prev

    print("exact state-bound margin:", state_margin)
    print("critical factors:", len(factors), "collected after q <", scanned)
    print("parity-length counts:", dict(sorted(parity_lengths.items())))
    print("first capacities:", cap[:12])
    print("r_* lower bound:", r)
    print("zero-endpoint windows at threshold:", e)
    print("minimum internal incidence:", lhs)
    print("available incidence budget:", rhs)
    print("previous-r failure:", lhs_prev, ">", rhs_prev)
    print("defect fraction >", r / H)


if __name__ == "__main__":
    main()
