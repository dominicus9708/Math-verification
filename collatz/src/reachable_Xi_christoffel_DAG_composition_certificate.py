#!/usr/bin/env python3
"""Finite exact regression for reachable-Xi concatenation.

The theorem is symbolic and recorded in the companion note. This script checks
small ordered-control languages with exact Fractions and verifies the set-valued
composition law. It is not a proof of Collatz.
"""

from fractions import Fraction
from itertools import product


def pow2(k: int) -> Fraction:
    return Fraction(2**k, 1) if k >= 0 else Fraction(1, 2**(-k))


def reachable(gaps, exps, p_right, max_d=6):
    """Return dict p_left -> set raw Xi for bounded regression language."""
    assert len(gaps) == len(exps)
    states = {(p_right, tuple(), Fraction(0))}
    # Build controls. Xi is accumulated with the global 3^i indexing.
    frontier = [(p_right, [], Fraction(0))]
    for i, (g, e) in enumerate(zip(gaps, exps)):
        nxt = []
        for p, ds, xi in frontier:
            L = max(0, p - g + 1)
            for d in range(L, max_d + 1):
                nxi = xi - Fraction(3**i) * pow2(e - d)
                nxt.append((d, ds + [d], nxi))
        frontier = nxt
    out = {}
    for p, ds, xi in frontier:
        out.setdefault(p, set()).add(xi)
    return out


def compose(Ru, Rv_by_input, r):
    out = {}
    for p_mid, xs in Ru.items():
        Rv = Rv_by_input[p_mid]
        for p_left, ys in Rv.items():
            S = out.setdefault(p_left, set())
            for x in xs:
                for y in ys:
                    S.add(x + Fraction(3**r) * y)
    return out


cases = 0
for gaps in product((1, 2), repeat=4):
    # Use local exponent coordinates whose second block is shifted by the
    # preceding block length through the explicit raw-Xi factor 3^r.
    # Constant exponents suffice to regression-test the algebraic split.
    exps = (3, 2, 1, 0)
    p0 = 0
    full = reachable(gaps, exps, p0, max_d=5)

    r = 2
    ug, vg = gaps[:r], gaps[r:]
    ue = exps[:r]
    # For the local child coordinate remove the global 3^r shift from the
    # ternary index; exponents themselves remain the same absolute values.
    ve = exps[r:]
    Ru = reachable(ug, ue, p0, max_d=5)
    Rv_by_input = {p: reachable(vg, ve, p, max_d=5) for p in Ru}

    # The local reachable() starts the v ternary index at zero, exactly the
    # coordinate in which the composition law contributes 3^r R_v.
    comp = compose(Ru, Rv_by_input, r)
    assert full == comp
    cases += 1

print("PASS reachable-Xi Christoffel-DAG composition regression")
print("gap_words_checked", cases)
print("split_depth", 2)
