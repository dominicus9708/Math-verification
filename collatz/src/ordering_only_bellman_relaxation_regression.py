#!/usr/bin/env python3
"""Finite regression for the symbolic ordering-only Bellman relaxation.

The companion note proves the all-block statements.  This script checks every
binary mechanical gap word up to a small length and a range of boundary
positions, verifying:

1. the greedy ordering-only recurrence;
2. F_w(p)=max(0,p-N2(w));
3. exact weighted block composition;
4. greedy optimality against exhaustive ordering-only controls on short words.

These finite checks are regression tests, not the proof of the symbolic lemmas
and not a proof of the Collatz conjecture.
"""

from fractions import Fraction
from itertools import product


def block_summary(word, p):
    """Greedy ordering-only transform with right-boundary weight normalized to 1."""
    weight = Fraction(1)
    cost = Fraction(0)
    cur = p
    for g in word:
        weight *= Fraction(3, 2 ** g)
        cur = max(0, cur - g + 1)
        cost += 2 * weight * (1 - Fraction(1, 2 ** cur))
    return cur, cost, weight


def exhaustive_cost(word, p, dmax=8):
    """Short-horizon exhaustive ordering-only optimum for regression only."""
    best = None

    def rec(i, cur, weight, cost):
        nonlocal best
        if best is not None and cost >= best:
            return
        if i == len(word):
            best = cost if best is None or cost < best else best
            return
        g = word[i]
        new_weight = weight * Fraction(3, 2 ** g)
        lo = max(0, cur - g + 1)
        for d in range(lo, dmax + 1):
            local = 2 * new_weight * (1 - Fraction(1, 2 ** d))
            rec(i + 1, d, new_weight, cost + local)

    rec(0, p, Fraction(1), Fraction(0))
    return best


for length in range(0, 8):
    for word in product((1, 2), repeat=length):
        n2 = sum(g == 2 for g in word)
        for p in range(0, 7):
            f, b, lam = block_summary(word, p)
            assert f == max(0, p - n2)
            if length <= 5 and p <= 4:
                assert b == exhaustive_cost(word, p)

        for cut in range(length + 1):
            u = word[:cut]
            v = word[cut:]
            for p in range(0, 7):
                fu, bu, lu = block_summary(u, p)
                fv, bv, lv = block_summary(v, fu)
                fw, bw, lw = block_summary(word, p)
                assert fw == fv
                assert bw == bu + lu * bv
                assert lw == lu * lv

print("PASS ordering-only Bellman relaxation regression")
print("symbolic proof remains in companion note")
