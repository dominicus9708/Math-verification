#!/usr/bin/env python3
"""MATH-086: phase-only over-approximation for the one-paid macro chain.

This certificate imports the canonical MATH-085 edge catalogue.  It deliberately
forgets dyadic address compatibility after the first multi-source macro, so the
resulting phase language is a SUPERSET of the actual same-integer language.
Therefore extinction of the phase-only multi-source language is a safe upper
bound on the actual one-paid multi-source horizon.

Two exact results are certified:

1. every canonical one-paid edge has penalty p > 1/9;
2. after 19 one-paid macros phase-compatible states with accumulated H<=71
   still exist, but after a 20th macro none remain with H<=71.

Together with MATH-084 (actual multi-source => H<=71), this implies that an
actual multi-source one-paid chain has at most 19 macros; the 20th compatible
macro, if any, is necessarily singleton-resolving.

This is not first-cell closure and not a Collatz proof.
"""
from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m85", HERE / "2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py"
)
m85 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m85)

LAM = Fraction(19, 503)


def merged_phase_edges():
    """Exact union of address-forgotten edges with identical phase law."""
    groups = defaultdict(list)
    for e in m85.EDGES:
        groups[(e.H, e.rho, e.c)].append((e.lo, e.hi))

    out = []
    for (H, rho, c), ints in groups.items():
        ints.sort()
        lo, hi = ints[0]
        for a, b in ints[1:]:
            if a <= hi:
                hi = max(hi, b)
            else:
                out.append((H, lo, hi, rho, c))
                lo, hi = a, b
        out.append((H, lo, hi, rho, c))
    return tuple(out)


def initial_phase_states():
    """Exact phase projection of the 857 actual multi-source first macros."""
    groups = defaultdict(list)
    for p in m85.initial_states():
        groups[(p.H, p.alpha)].append((p.lo, p.hi))

    out = []
    for (H, alpha), ints in groups.items():
        ints.sort()
        lo, hi = ints[0]
        for a, b in ints[1:]:
            if a <= hi:
                hi = max(hi, b)
            else:
                out.append((H, lo, hi, alpha))
                lo, hi = a, b
        out.append((H, lo, hi, alpha))
    return out


def step(states, edges):
    """Forget address, retain exact phase compatibility and H.

    States with H2>71 are terminal-crossing candidates by MATH-084 and are not
    propagated as multi-source states.  Exact duplicate phase states retain the
    smallest alpha, which only enlarges the low-cost over-approximation.
    """
    cont = {}
    crossings = []
    for H, lo, hi, alpha in states:
        for h, elo, ehi, rho, c in edges:
            a = max(lo, elo)
            b = min(hi, ehi)
            if a >= b:
                continue
            H2 = H + h
            lo2 = a * rho
            hi2 = b * rho
            alpha2 = alpha / rho + c
            if H2 > 71:
                penalty_inf = alpha2 * lo2
                margin = penalty_inf if H2 <= 73 else penalty_inf - LAM * (H2 - 73)
                crossings.append(margin)
            else:
                key = (H2, lo2, hi2)
                old = cont.get(key)
                if old is None or alpha2 < old:
                    cont[key] = alpha2
    return [(H, lo, hi, a) for (H, lo, hi), a in cont.items()], crossings


def main():
    # Stronger universal one-paid penalty floor.
    for e in m85.EDGES:
        out_lo = e.lo * e.rho
        if e.c == Fraction(1, 8):
            assert out_lo >= Fraction(8, 9)
            # Open interval: actual output phase is strictly above its infimum.
            assert e.c * out_lo >= Fraction(1, 9)
        else:
            assert e.c == Fraction(1, 4)
            assert out_lo >= Fraction(1, 2)
            assert e.c * out_lo >= Fraction(1, 8)
    print("all canonical one-paid edges have p > 1/9")

    edges = merged_phase_edges()
    states = initial_phase_states()
    assert len(edges) == 126
    assert len(states) == 113

    expected_states = {
        2:1293, 3:3127, 4:3023, 5:2890, 6:2728, 7:2543,
        8:2337, 9:2111, 10:1868, 11:1613, 12:1356, 13:1099,
        14:843, 15:607, 16:395, 17:221, 18:93, 19:13, 20:0,
    }
    expected_crossings = {
        2:2992, 3:38415, 4:94067, 5:90732, 6:86488, 7:81425,
        8:75687, 9:69315, 10:62465, 11:55143, 12:47509,
        13:39801, 14:32066, 15:24467, 16:17483, 17:11293,
        18:6259, 19:2597, 20:361,
    }

    for t in range(2, 21):
        states, crossings = step(states, edges)
        assert len(states) == expected_states[t]
        assert len(crossings) == expected_crossings[t]
        print(t, "multi_phase_states", len(states), "terminal_crossings", len(crossings))

    assert states == []
    print("PASS MATH-086: phase-only H<=71 language extinct after macro 20")


if __name__ == "__main__":
    main()
