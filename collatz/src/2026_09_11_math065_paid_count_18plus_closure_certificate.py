#!/usr/bin/env python3
"""
MATH-065 exact closure certificate for every multi-paid layer r>=18.

This certificate repairs the singleton-resolution gap found in the original
MATH-064 audit and corrects the r=23 frontier transcription error.

For 18<=r<=64 it performs one uniform exact branch-and-bound audit:

1. refine every MATH-058R paid-exit source by the next r exact phase cuts;
2. use the minimum-slack phase cost as a safe lower bound;
3. carry each parity prefix as one exact dyadic source congruence in t;
4. prune a branch only when either its source congruence is empty or its
   current cost plus the minimum possible future cost is already >=19/503 H;
5. materialize every remaining completed cylinder exactly;
6. directly continue every remaining ordinary target to the frozen floor 2^71.

The source congruence is preserved at every parity step, so this is a
same-integer audit rather than a density/count argument.

Results:
- r=18..26: every remaining negative-candidate ordinary target descends;
- r=27..64: no negative-candidate completed cylinder remains;
- r>=65: already closed analytically by MATH-062.

Therefore every multi-paid macro with r>=18 is closed for the current
first-cell minimal-counterexample calculation.  This does NOT close r<=17,
the first universal cell, later Farey cells, or the Collatz conjecture.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math058r", HERE / "2026_09_11_paid_macro_transition_certificate.py"
)
m58 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

LAMBDA = Fraction(19, 503)
LO = 1 << 71
MAX_PHASE = 200

M = [0] * (MAX_PHASE + 1)
for q in range(MAX_PHASE + 1):
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    M[q] = d

TAU = [None] * (MAX_PHASE + 1)
for q in range(1, MAX_PHASE + 1):
    TAU[q] = Fraction(3**q, 2 ** (q + M[q] + 1))


def refined_cells(lo, hi, q0, r):
    cuts = {lo, hi}
    for j in range(1, r + 1):
        t = TAU[q0 + j]
        if lo < t < hi:
            cuts.add(t)
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def phase_multiplier(qinc, omega):
    dm = M[qinc] + (1 if omega <= TAU[qinc] else 0)
    return Fraction(2 ** (qinc + dm), 3**qinc)


def phase_data(q0, lo, hi, r):
    mid = (lo + hi) / 2
    g = phase_multiplier(q0, mid)
    eps = []
    gs = []
    for _ in range(r):
        gs.append(g)
        e = 0 if g * mid > Fraction(3, 4) else 1
        eps.append(e)
        g *= Fraction(2, 3) if e == 0 else Fraction(4, 3)
    return eps, gs


def classify_cells(r):
    safe = []
    singleton = []
    critical = []
    total = 0

    for L in range(1, 73):
        for lo0, hi0, start_R, E0, q0 in m58.paid_exit_sources(L):
            for lo, hi in refined_cells(lo0, hi0, q0, r):
                total += 1
                tmin, tmax = m58.lift_bounds(L, start_R, lo, hi)
                assert tmin <= tmax

                eps, gs = phase_data(q0, lo, hi, r)
                hcl = r + 1 + sum(eps)
                H = L + hcl
                baseline = sum(gs, Fraction(0)) * lo / 6
                margin = baseline - LAMBDA * H
                cell = (
                    L, start_R, E0, q0, lo, hi, tmin, tmax,
                    eps, gs, hcl, H, margin,
                )

                if margin >= 0:
                    safe.append(cell)
                elif tmax - tmin < (1 << hcl):
                    singleton.append(cell)
                else:
                    critical.append(cell)

    return total, safe, singleton, critical


def class_first(tmin, tmax, residue, modulus):
    first = tmin + ((residue - tmin) % modulus)
    return first if first <= tmax else None


def scaled_cost_table(cell, r):
    (_, _, _, _, lo, _, _, _, eps, gs, _, H, _) = cell
    umax = 1 + sum(eps)
    target = LAMBDA * H

    costs = [[None] * (umax + 1) for _ in range(r)]
    den = target.denominator
    for j in range(r):
        for u in range(1, umax + 1):
            c = (1 - Fraction(1, 2**u)) * gs[j] * lo / 3
            costs[j][u] = c
            den = lcm(den, c.denominator)

    target_i = target.numerator * (den // target.denominator)
    cost_i = [[0] * (umax + 1) for _ in range(r)]
    for j in range(r):
        for u in range(1, umax + 1):
            c = costs[j][u]
            cost_i[j][u] = c.numerator * (den // c.denominator)

    future = [0] * (r + 1)
    for j in range(r - 1, -1, -1):
        # u=1 is the minimum possible penalty of every future paid odd.
        future[j] = future[j + 1] + cost_i[j][1]

    return target_i, cost_i, future


def negative_candidate_cylinders(cell, r):
    """Exact dyadic branch-and-bound for one phase/address cell.

    A state carries the exact residue t=tres (mod mod) and the exact affine
    endpoint y=yres+coeff*s after substituting t=tres+mod*s.
    """
    (L, start_R, E0, q0, lo, hi, tmin, tmax,
     eps, gs, hcl, H, margin) = cell

    target_i, costs, future = scaled_cost_table(cell, r)
    stack = [(0, 1, 0, 0, 1, E0, 3**q0, 0)]
    leaves = []
    nodes = 0

    while stack:
        j, u, cost, tres, mod, yres, coeff, steps = stack.pop()
        nodes += 1

        # Every future paid odd has u>=1.  Hence current cost plus the u=1
        # future baseline is a rigorous lower bound for every completion.
        if cost + future[j] >= target_i:
            continue

        if u == 0:
            if j == r:
                first = class_first(tmin, tmax, tres, mod)
                if first is not None:
                    count = (tmax - first) // mod + 1
                    assert steps == hcl
                    assert mod == 1 << hcl
                    leaves.append((first, count, tres, mod, yres, coeff))
            # u=0 before j=r is an earlier return, not an r-paid cluster.
            continue

        # Even shortcut step.  It is forbidden before the opening paid odd.
        if j > 0:
            bit = (-yres) & 1
            tr = tres + mod * bit
            mod2 = mod * 2
            if class_first(tmin, tmax, tr, mod2) is not None:
                y0 = yres + coeff * bit
                assert y0 % 2 == 0
                stack.append((
                    j, u - 1, cost, tr, mod2,
                    y0 // 2, coeff, steps + 1,
                ))

        # Paid odd shortcut step.
        if j < r:
            bit = (1 - yres) & 1
            tr = tres + mod * bit
            mod2 = mod * 2
            if class_first(tmin, tmax, tr, mod2) is not None:
                y0 = yres + coeff * bit
                assert y0 % 2 == 1
                stack.append((
                    j + 1, u + eps[j], cost + costs[j][u], tr, mod2,
                    (3 * y0 + 1) // 2, coeff * 3, steps + 1,
                ))

    return leaves, nodes


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def audit_layer(r, distance_cache=None):
    total, safe, singleton, critical = classify_cells(r)
    records = []
    nodes = 0

    for group in (singleton, critical):
        for cell in group:
            leaves, n = negative_candidate_cylinders(cell, r)
            nodes += n
            for leaf in leaves:
                records.append((cell, leaf))

    target_multiplicity = 0
    targets = set()
    for cell, leaf in records:
        (L, start_R, E0, q0, lo, hi, tmin, tmax,
         eps, gs, hcl, H, margin) = cell
        first, count, tres, mod, yres, coeff = leaf
        base_s = (first - tres) // mod
        target0 = yres + coeff * base_s
        target_multiplicity += count
        for k in range(count):
            targets.add(target0 + coeff * k)

    cache = {} if distance_cache is None else distance_cache

    def descent_steps(n):
        x = n
        path = []
        seen = set()
        while x > LO and x not in cache:
            if x in seen:
                return None
            seen.add(x)
            path.append(x)
            x = shortcut(x)
            assert len(path) < 10000

        d = 0 if x <= LO else cache[x]
        for v in reversed(path):
            d += 1
            cache[v] = d
        return cache.get(n, 0)

    max_descent = 0
    for t in targets:
        d = descent_steps(t)
        assert d is not None, t
        max_descent = max(max_descent, d)

    return {
        "r": r,
        "total_cells": total,
        "safe_cells": len(safe),
        "singleton_cells": len(singleton),
        "critical_cells": len(critical),
        "branch_nodes": nodes,
        "negative_cylinders": len(records),
        "target_multiplicity": target_multiplicity,
        "unique_targets": len(targets),
        "max_descent_steps": max_descent,
    }


EXPECTED = {
    18: (1121, 302, 621, 198, 32697784, 826110, 4593148, 2844121, 247),
    19: (1121, 318, 649, 154, 26527529, 299140, 733660, 451814, 237),
    20: (1155, 364, 690, 101, 18304737, 76138, 102512, 63017, 204),
    21: (1155, 393, 706, 56, 11180644, 13040, 13901, 8449, 127),
    22: (1192, 433, 752, 7, 8485437, 2184, 2188, 1338, 123),
    23: (1232, 490, 742, 0, 4718247, 229, 229, 150, 47),
    24: (1232, 504, 728, 0, 3629882, 53, 53, 30, 28),
    25: (1275, 567, 708, 0, 2157996, 7, 7, 4, 6),
    26: (1275, 592, 683, 0, 1351843, 2, 2, 1, 3),
}


def summary_tuple(x):
    return (
        x["total_cells"], x["safe_cells"], x["singleton_cells"],
        x["critical_cells"], x["branch_nodes"], x["negative_cylinders"],
        x["target_multiplicity"], x["unique_targets"],
        x["max_descent_steps"],
    )


def main():
    cache = {}

    for r in range(18, 27):
        result = audit_layer(r, cache)
        assert summary_tuple(result) == EXPECTED[r], (r, result)
        print("layer", result)

    # From r=27 through r=64 the exact branch-and-bound leaves no completed
    # cylinder whose lower adjusted cost can still be negative.
    for r in range(27, 65):
        result = audit_layer(r, cache)
        assert result["critical_cells"] == 0, result
        assert result["negative_cylinders"] == 0, result
        assert result["target_multiplicity"] == 0, result
        print("layer", r, "negative_candidates", 0)

    print("MATH-062 supplies the analytic closure for every r>=65")
    print("PASS MATH-065: every multi-paid layer r>=18 is closed")


if __name__ == "__main__":
    main()
