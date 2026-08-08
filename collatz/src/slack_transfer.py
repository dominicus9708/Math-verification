#!/usr/bin/env python3
"""Sparse transfer-matrix model for admissible odd-position prefixes.

For odd-position coordinates alpha_i at coefficient-stopping order, define
    kappa(i)=floor(i*log2(3))
    s_i=kappa(i-1)-alpha_i >= 0.
Since alpha_{i+1}>alpha_i and
    d_i=kappa(i)-kappa(i-1) in {1,2},
we obtain the exact transition
    0 <= s_{i+1} <= s_i+d_i-1.

This script propagates the count vector without enumerating alpha-vectors.
The resulting product is the sparse transfer-matrix formulation of the
admissibility tree.
"""

from __future__ import annotations
import argparse
import math
from collections import defaultdict

LOG2_3 = math.log2(3.0)


def kappa(i: int) -> int:
    # For practical ranges this float seed is safe; exact applications can replace
    # this with integer comparison between 2^k and 3^i.
    return math.floor(i * LOG2_3)


def step(v: dict[int, int], d: int) -> dict[int, int]:
    out: dict[int, int] = defaultdict(int)
    for s, count in v.items():
        for t in range(s + d):  # t <= s+d-1
            out[t] += count
    return dict(out)


def prefix_count(h: int) -> tuple[int, dict[int, int]]:
    if h <= 0:
        return 1, {0: 1}
    v = {0: 1}  # s_1=0 because alpha_1=kappa(0)=0
    for i in range(1, h):
        d = kappa(i) - kappa(i - 1)
        assert d in (1, 2)
        v = step(v, d)
    return sum(v.values()), v


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-h", type=int, default=12)
    args = ap.parse_args()

    print("h, admissible_prefixes, slack_states")
    for h in range(args.max_h + 1):
        count, v = prefix_count(h)
        print(f"{h}, {count}, {len(v)}")


if __name__ == "__main__":
    main()
