#!/usr/bin/env python3
"""MATH-181 joint paid-count first-return executor prototype.

Purpose
-------
Replace the target-r outer loop of the MATH-065/115 paid-layer calculation by
one exact dyadic first-return tree that tags terminal leaves by r=1..21.

This is a PROTOTYPE / REGRESSION TARGET only.  It makes no new closure claim.
Before promotion it must be regressed against the canonical target-r workloads
by exact represented-set / occurrence-mass coverage and downstream closure.
Raw AP record counts are not required to match because the common 21-cut phase
partition is generally finer than the target-specific partitions.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m65", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

MAX_R = 21
LAMBDA = Fraction(19, 503)


def common_refined_cells(lo: Fraction, hi: Fraction, q0: int):
    """Refine once by every future exact phase cut through paid count 21."""
    cuts = {lo, hi}
    for j in range(1, MAX_R + 1):
        t = m65.TAU[q0 + j]
        if lo < t < hi:
            cuts.add(t)
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def exact_phase_schedule(q0: int, lo: Fraction, hi: Fraction):
    """Return eps, g, local first-return depths h_r for the common cell."""
    eps, gs = m65.phase_data(q0, lo, hi, MAX_R)
    h = [None] * (MAX_R + 1)
    e = 0
    for r in range(1, MAX_R + 1):
        e += eps[r - 1]
        h[r] = r + 1 + e
    return eps, gs, h


def scaled_joint_tables(L: int, lo: Fraction, eps, gs, h):
    """Common integer-scaled cost tables and all-layer future potential.

    best[j] is the minimum, over every possible terminal paid count r>=j,
    of (minimum future paid cost from j to r) - lambda*(L+h_r).
    Therefore cost+best[j]>=0 is sufficient to prune the branch for every
    future target layer simultaneously.
    """
    umax = 1 + sum(eps)

    target = [None] * (MAX_R + 1)
    costs = [[None] * (umax + 1) for _ in range(MAX_R)]

    den = 1
    for r in range(1, MAX_R + 1):
        target[r] = LAMBDA * (L + h[r])
        den = lcm(den, target[r].denominator)

    for j in range(MAX_R):
        for u in range(1, umax + 1):
            c = (1 - Fraction(1, 2**u)) * gs[j] * lo / 3
            costs[j][u] = c
            den = lcm(den, c.denominator)

    target_i = [None] * (MAX_R + 1)
    for r in range(1, MAX_R + 1):
        x = target[r]
        target_i[r] = x.numerator * (den // x.denominator)

    cost_i = [[0] * (umax + 1) for _ in range(MAX_R)]
    for j in range(MAX_R):
        for u in range(1, umax + 1):
            x = costs[j][u]
            cost_i[j][u] = x.numerator * (den // x.denominator)

    # prefix1[r] = sum_{i=0}^{r-1} c_i(1)
    prefix1 = [0] * (MAX_R + 1)
    for r in range(1, MAX_R + 1):
        prefix1[r] = prefix1[r - 1] + cost_i[r - 1][1]

    best = [None] * (MAX_R + 1)
    for j in range(MAX_R + 1):
        r0 = max(1, j)
        vals = []
        for r in range(r0, MAX_R + 1):
            future = prefix1[r] - prefix1[j]
            vals.append(future - target_i[r])
        best[j] = min(vals)

    return target_i, cost_i, best


def joint_negative_cylinders(
    *,
    L: int,
    start_R: int,
    E0: int,
    q0: int,
    lo: Fraction,
    hi: Fraction,
):
    """Exact one-tree first-return enumeration for a common phase cell.

    Returns tagged negative-candidate AP rows
        (r, target0, odd_step, count, local_depth)
    and the number of branch nodes visited.
    """
    tmin, tmax = m65.lift_bounds(L, start_R, lo, hi)
    if tmin > tmax:
        return [], 0

    eps, gs, h = exact_phase_schedule(q0, lo, hi)
    target_i, cost_i, best = scaled_joint_tables(L, lo, eps, gs, h)

    # j, u, cost, tres, mod, yres, steps
    stack = [(0, 1, 0, 0, 1, E0, 0)]
    leaves = []
    nodes = 0

    while stack:
        j, u, cost, tres, mod, yres, steps = stack.pop()
        nodes += 1

        # First return is terminal and is never extended into a larger r layer.
        if u == 0:
            if 1 <= j <= MAX_R and cost < target_i[j]:
                first = m65.class_first(tmin, tmax, tres, mod)
                if first is not None:
                    count = (tmax - first) // mod + 1
                    assert steps == h[j], (j, steps, h[j])
                    assert mod == 1 << steps
                    coeff = 3 ** (q0 + j)
                    base_s = (first - tres) // mod
                    target0 = yres + coeff * base_s
                    leaves.append((j, target0, coeff, count, steps))
            continue

        # Proof-neutral all-layer pruning.
        if cost + best[j] >= 0:
            continue

        coeff = 3 ** (q0 + j)

        # Even shortcut: forbidden before the opening paid odd.
        if j > 0:
            bit = (-yres) & 1
            tr = tres + mod * bit
            mod2 = mod * 2
            if m65.class_first(tmin, tmax, tr, mod2) is not None:
                y0 = yres + coeff * bit
                assert y0 % 2 == 0
                stack.append((
                    j,
                    u - 1,
                    cost,
                    tr,
                    mod2,
                    y0 // 2,
                    steps + 1,
                ))

        # Paid odd shortcut.
        if j < MAX_R:
            bit = (1 - yres) & 1
            tr = tres + mod * bit
            mod2 = mod * 2
            if m65.class_first(tmin, tmax, tr, mod2) is not None:
                y0 = yres + coeff * bit
                assert y0 % 2 == 1
                stack.append((
                    j + 1,
                    u + eps[j],
                    cost + cost_i[j][u],
                    tr,
                    mod2,
                    (3 * y0 + 1) // 2,
                    steps + 1,
                ))

    return leaves, nodes


def iter_joint_cells():
    for L in range(1, 73):
        for lo0, hi0, start_R, E0, q0 in m65.paid_exit_sources(L):
            for lo, hi in common_refined_cells(lo0, hi0, q0):
                yield L, start_R, E0, q0, lo, hi


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--emit",
        action="store_true",
        help="emit tagged AP rows r<TAB>target0<TAB>odd_step<TAB>count<TAB>local_depth",
    )
    ap.add_argument(
        "--max-cells",
        type=int,
        default=None,
        help="prototype/debug limit; omit for the full common phase partition",
    )
    args = ap.parse_args()

    stats = defaultdict(lambda: {"cylinders": 0, "occurrences": 0, "max_m": 0})
    cells = 0
    nodes = 0

    for cell in iter_joint_cells():
        cells += 1
        if args.max_cells is not None and cells > args.max_cells:
            break

        leaves, n = joint_negative_cylinders(
            L=cell[0],
            start_R=cell[1],
            E0=cell[2],
            q0=cell[3],
            lo=cell[4],
            hi=cell[5],
        )
        nodes += n

        for r, target0, step, count, depth in leaves:
            s = stats[r]
            s["cylinders"] += 1
            s["occurrences"] += count
            s["max_m"] = max(s["max_m"], count)
            if args.emit:
                print(r, target0, step, count, depth, sep="\t")

    print(
        f"MATH-181 prototype cells={cells} branch_nodes={nodes}",
        file=sys.stderr,
    )
    for r in range(1, MAX_R + 1):
        s = stats[r]
        print(
            "layer",
            r,
            "negative_cylinders",
            s["cylinders"],
            "occurrences",
            s["occurrences"],
            "max_multiplicity",
            s["max_m"],
            file=sys.stderr,
        )

    print("NO NEW LAYER CLOSURE CLAIM", file=sys.stderr)


if __name__ == "__main__":
    main()
