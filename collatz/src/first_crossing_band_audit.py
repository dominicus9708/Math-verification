#!/usr/bin/env python3
"""Exact finite audit of the first coefficient-crossing band.

For a coefficient-surviving canonical parent at depth j, a first coefficient
crossing can occur only on an even child, with
    2^j < 3^q < 2^(j+1).
For the child canonical start n and its actual depth-j predecessor z, actual
descent at the crossing is equivalent to z < 2n.

Define the correction occupancy
    theta = R / (n * (2^(j+1) - 3^q)).
Then z < 2n is exactly theta < 1.

This script enumerates exact coefficient-surviving canonical parents, generates
their first-crossing even children, and records the minimum integer descent
margin H=2n-z and the maximum exact theta by crossing depth.
"""

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class State:
    r: int
    y: int
    q: int


def run(max_child_depth: int = 26) -> None:
    states = [State(0, 0, 0)]
    stats = {}
    total = 0
    failures = 0

    for parent_depth in range(max_child_depth):
        v = 1 << parent_depth
        nxt = []

        for s in states:
            u = 3 ** s.q

            for p in (0, 1):
                c = p ^ (s.y & 1)
                r2 = s.r + c * v
                pre = s.y + c * u
                y2 = (3 * pre + 1) // 2 if p else pre // 2
                q2 = s.q + p

                # First coefficient crossing from a surviving parent.
                if (
                    p == 0
                    and parent_depth >= 1
                    and u > v
                    and u < 2 * v
                    and r2 > 1
                ):
                    child_depth = parent_depth + 1
                    H = 2 * r2 - pre
                    R = v * pre - u * r2
                    theta_num = R
                    theta_den = r2 * (2 * v - u)

                    row = stats.setdefault(
                        child_depth,
                        {
                            "count": 0,
                            "min_H": None,
                            "theta_num": 0,
                            "theta_den": 1,
                            "arg_r": None,
                        },
                    )
                    row["count"] += 1
                    row["min_H"] = H if row["min_H"] is None else min(row["min_H"], H)
                    if theta_num * row["theta_den"] > row["theta_num"] * theta_den:
                        row["theta_num"] = theta_num
                        row["theta_den"] = theta_den
                        row["arg_r"] = r2

                    total += 1
                    if H <= 0 or theta_num >= theta_den:
                        failures += 1

                # Retain coefficient-surviving child.
                if 3 ** q2 > 2 * v:
                    nxt.append(State(r2, y2, q2))

        states = nxt

    print("depth,crossing_candidates,min_H,max_theta_num,max_theta_den,arg_r")
    for depth in sorted(stats):
        row = stats[depth]
        g = gcd(row["theta_num"], row["theta_den"])
        print(
            f"{depth},{row['count']},{row['min_H']},"
            f"{row['theta_num']//g},{row['theta_den']//g},{row['arg_r']}"
        )

    print(f"# total_candidates={total}")
    print(f"# crossing_failures={failures}")


if __name__ == "__main__":
    import sys
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    run(K)
