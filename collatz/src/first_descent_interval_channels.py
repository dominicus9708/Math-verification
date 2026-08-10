#!/usr/bin/env python3
"""Exact first-descent interval-channel dynamics for the accelerated Collatz map.

Each depth-k residue cylinder is represented as
    n = r + 2^k m,  m >= 0.
The channel stores the subset of m for which the trajectory has not yet fallen
below its own starting value during the first k accelerated Collatz steps.
That survivor subset is always an integer interval, possibly unbounded.

This script uses only exact integer arithmetic.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Channel:
    k: int
    r: int
    y: int
    q: int
    lower: int
    upper: Optional[int]  # None means +infinity


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def refine(ch: Channel, lift_bit: int) -> Optional[Channel]:
    """Refine one depth-k channel to one depth-(k+1) binary child."""
    k, r, y, q = ch.k, ch.r, ch.y, ch.q
    c = lift_bit

    # Inherited interval under m = c + 2 m'.
    inherited_lower = max(0, ceil_div(ch.lower - c, 2))
    inherited_upper = None if ch.upper is None else (ch.upper - c) // 2
    if inherited_upper is not None and inherited_lower > inherited_upper:
        return None

    v = 1 << k
    u = 3 ** q

    r2 = r + c * v
    lifted_predecessor = y + c * u
    p = lifted_predecessor & 1
    y2 = (3 * lifted_predecessor + 1) // 2 if p else lifted_predecessor // 2
    q2 = q + p

    # New no-descent condition for n = r2 + 2^(k+1) m':
    # T^(k+1)(n) - n
    #   = (y2-r2) + (3^q2 - 2^(k+1)) m' >= 0.
    A = y2 - r2
    B = 3 ** q2 - (1 << (k + 1))

    new_lower = 0
    new_upper: Optional[int] = None

    if B > 0:
        new_lower = max(0, ceil_div(-A, B))
    elif B < 0:
        new_upper = A // (-B)
        if new_upper < 0:
            return None
    else:
        # For k+1 >= 1, equality 3^q2 = 2^(k+1) cannot occur, but keep exact logic.
        if A < 0:
            return None

    lower = max(inherited_lower, new_lower)
    if inherited_upper is None:
        upper = new_upper
    elif new_upper is None:
        upper = inherited_upper
    else:
        upper = min(inherited_upper, new_upper)

    if upper is not None and lower > upper:
        return None

    return Channel(k + 1, r2, y2, q2, lower, upper)


def run(max_depth: int = 24) -> None:
    # n > 1 at depth 0 means m=n in [2,+infinity).
    states = [Channel(0, 0, 0, 0, 2, None)]

    print("k,channels,bounded,unbounded,nonzero_lower")
    for k in range(max_depth + 1):
        bounded = sum(ch.upper is not None for ch in states)
        unbounded = len(states) - bounded
        nonzero_lower = sum(ch.lower != 0 for ch in states)
        print(f"{k},{len(states)},{bounded},{unbounded},{nonzero_lower}")

        if k == max_depth:
            break

        nxt = []
        for ch in states:
            for c in (0, 1):
                child = refine(ch, c)
                if child is not None:
                    nxt.append(child)
        states = nxt


if __name__ == "__main__":
    import sys
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    run(K)
