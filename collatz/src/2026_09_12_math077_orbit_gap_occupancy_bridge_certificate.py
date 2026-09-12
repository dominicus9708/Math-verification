#!/usr/bin/env python3
"""MATH-077: exact orbit-gap / first-crossing occupancy bridge.

Universal algebra:

    T^k(N) = (N+S)/rho,
    T^k(N)-N = [S-N(rho-1)]/rho,

where S=C/3^q and rho=2^k/3^q for the parity word followed by N.

For the historical first-crossing audit, this certificate regenerates every
candidate through depth 26 and checks exactly that

    theta_old = Rcorr/[n(2^k-3^q)] = S/[n(rho-1)],

and

    H_old = 2n-pre = 2[n(rho-1)-S]/rho.

Finite regression is implementation evidence only; the identities themselves
are algebraic.
"""

from dataclasses import dataclass
from fractions import Fraction

MAX_DEPTH = 26


@dataclass(frozen=True)
class State:
    r: int
    y: int
    q: int


def main() -> None:
    states = [State(0, 0, 0)]
    total = 0
    occupancy_failures = 0
    margin_failures = 0
    descent_failures = 0
    depth_counts = {}

    for parent_depth in range(MAX_DEPTH):
        v = 1 << parent_depth
        nxt = []

        for s in states:
            u = 3 ** s.q
            for p in (0, 1):
                lift = p ^ (s.y & 1)
                r2 = s.r + lift * v
                pre = s.y + lift * u
                y2 = (3 * pre + 1) // 2 if p else pre // 2
                q2 = s.q + p

                # Historical first coefficient crossing: surviving parent,
                # even child, 2^j < 3^q < 2^(j+1).
                if (
                    p == 0
                    and parent_depth >= 1
                    and u > v
                    and u < 2 * v
                    and r2 > 1
                ):
                    child_depth = parent_depth + 1
                    Rcorr = v * pre - u * r2
                    S = Fraction(Rcorr, u)
                    rho = Fraction(2 * v, u)

                    theta_old = Fraction(Rcorr, r2 * (2 * v - u))
                    theta_new = S / (r2 * (rho - 1))
                    if theta_old != theta_new:
                        occupancy_failures += 1

                    H_old = 2 * r2 - pre
                    H_new = 2 * (r2 * (rho - 1) - S) / rho
                    if H_new.denominator != 1 or H_new.numerator != H_old:
                        margin_failures += 1

                    endpoint = Fraction(r2 + S, 1) / rho
                    assert endpoint.denominator == 1
                    assert endpoint.numerator == y2
                    gap = endpoint - r2
                    gap_formula = (S - r2 * (rho - 1)) / rho
                    assert gap == gap_formula

                    # The historical audit found strict descent at every first
                    # crossing through depth 26.
                    if not (S < r2 * (rho - 1)):
                        descent_failures += 1

                    total += 1
                    depth_counts[child_depth] = depth_counts.get(child_depth, 0) + 1

                # Retain coefficient-surviving child for future first crossings.
                if 3 ** q2 > 2 * v:
                    nxt.append(State(r2, y2, q2))

        states = nxt

    expected = {
        4: 1, 5: 2, 7: 3, 8: 7, 10: 12, 12: 30, 13: 85,
        15: 173, 16: 476, 18: 961, 20: 2652, 21: 8045,
        23: 17637, 24: 51033, 26: 108950,
    }
    assert depth_counts == expected
    assert total == 190_067
    assert occupancy_failures == 0
    assert margin_failures == 0
    assert descent_failures == 0

    print("crossing_candidates", total)
    print("occupancy_failures", occupancy_failures)
    print("margin_failures", margin_failures)
    print("descent_failures", descent_failures)
    print("PASS MATH-077 orbit-gap/occupancy bridge")


if __name__ == "__main__":
    main()
