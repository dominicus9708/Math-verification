#!/usr/bin/env python3
"""Exact arithmetic certificate for the parity-RS repair gate.

This script does NOT verify Barina's external 2^71 computation.  It verifies
all arithmetic implications used after taking that published finite frontier
as an input, and it also performs a small self-contained finite-prefix check.

Shortcut map:
    T(n) = n//2                    if n is even
           (3*n + 1)//2            if n is odd
"""

from __future__ import annotations


P = 190_537
D = 301_994
H = 301_993
BARINA_BASE = 1 << 71
SELF_BASE = 1_000_000
SELF_H = 4_700


def T(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def verify_self_prefix(B: int) -> tuple[int, int]:
    """Verify convergence to the already-known set for every n<=B.

    The scan is ascending.  Once an orbit hits 1 or any value that has already
    been certified, the current start is certified.  Python integers are exact.
    Returns (largest path length before hitting certified set, largest peak).
    """
    known = {1}
    max_len = 0
    max_peak = 1

    for n in range(2, B + 1):
        x = n
        path: list[int] = []
        local = set()
        peak = n

        while x not in known:
            if x in local:
                raise AssertionError(f"cycle encountered in finite prefix: start={n}, x={x}")
            local.add(x)
            path.append(x)
            x = T(x)
            if x > peak:
                peak = x

        known.update(path)
        if len(path) > max_len:
            max_len = len(path)
        if peak > max_peak:
            max_peak = peak

    return max_len, max_peak


def verify_adjusted_multiplier(B: int, p: int, d: int) -> None:
    """Check ((3B+1)/B)^p < 2^d exactly."""
    lhs = pow(3 * B + 1, p)
    rhs = (1 << d) * pow(B, p)
    assert lhs < rhs


def verify_ballot_implies_coefficient(p: int, d: int, H: int) -> None:
    """For 1<=j<=H verify

        d*q > p*j  ==>  3^q >= 2^j

    at the smallest permitted integer q.  Exact integer arithmetic only.
    """
    q_cur = 0
    pow3 = 1
    pow2 = 1

    for j in range(1, H + 1):
        pow2 <<= 1
        q_min = (p * j) // d + 1
        while q_cur < q_min:
            pow3 *= 3
            q_cur += 1
        if pow3 < pow2:
            raise AssertionError(
                f"ballot/coefficient mismatch at j={j}: q_min={q_min}"
            )


def verify_self_base_coefficient_gate(B: int, H: int) -> None:
    """Directly verify the adjusted-base gate through H for a self base.

    Let q_c(j) be the smallest q with 3^q >= 2^j.  We check that one fewer
    odd step is already contracting under the slightly larger odd multiplier
    3+1/B.  Hence any non-descending start >B must have q>=q_c(j).
    """
    pow2 = 1
    pow3 = 1
    q_c = 0

    for j in range(1, H + 1):
        pow2 <<= 1
        while pow3 < pow2:
            pow3 *= 3
            q_c += 1

        q_bad = q_c - 1
        # ((3B+1)/B)^q_bad < 2^j
        assert pow(3 * B + 1, q_bad) < (1 << j) * pow(B, q_bad), (j, q_bad)


def main() -> None:
    # Pure coefficient comparison for the chosen lower rational gate.
    assert pow(3, P) < (1 << D)

    # Self-contained finite version: no external verification input required.
    max_len, max_peak = verify_self_prefix(SELF_BASE)
    verify_self_base_coefficient_gate(SELF_BASE, SELF_H)

    # Stronger published-frontier version.  The external statement that every
    # n<2^71 converges is an input; everything below is checked exactly here.
    verify_adjusted_multiplier(BARINA_BASE, P, D)
    verify_ballot_implies_coefficient(P, D, H)

    print("PASS parity-RS global coefficient gate")
    print(f"self_base={SELF_BASE}")
    print(f"self_max_path_to_certified={max_len}")
    print(f"self_max_peak={max_peak}")
    print(f"self_coefficient_gate_through={SELF_H}")
    print(f"published_base=2^71={BARINA_BASE}")
    print(f"ballot={D}*q > {P}*j")
    print(f"published_frontier_coefficient_gate_through={H}")


if __name__ == "__main__":
    main()
