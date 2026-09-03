#!/usr/bin/env python3
"""Lightweight export of the canonical jump-8 frontier after cumulative pruning.

This module intentionally does NOT rerun the bounded-displacement searches on
import.  It imports the certified first-75-tightened states, applies the latest
certified cumulative future-defect floor

    horizon 49 survivor => at least 4 displaced target ranks
                        => eta_future > 1/3,

and safely weakens this to eta_future>=1/3 for endpoint pruning.

The older eta_future>=1/4 cut is superseded by this stronger floor; the two
floors are not added.
"""

from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi
ETA_FLOOR = Fraction(1, 3)
EXPECTED_TOTAL = 26_859_837_368_506_133_665
EXPECTED_PRUNED = 82_136_589


def retained_hi(st, cut: Fraction) -> int:
    z = (cut - st.r) / (1 << st.h)
    return min(st.hi, z.numerator // z.denominator)


pruned_states = []
pruned = 0
for st in tail.states:
    cut = (Fraction(BARRIER, 1) - M_LO * (st.eta + ETA_FLOOR)) / DELTA_LO
    hi2 = retained_hi(st, cut)
    if hi2 >= st.lo:
        pruned += st.hi - hi2
        pruned_states.append(tail.State(
            st.r, st.y, st.lo, hi2, st.h, st.S,
            st.D, st.eta, st.root_f,
        ))
    else:
        pruned += st.count

assert pruned == EXPECTED_PRUNED
assert len(pruned_states) == 14_224
assert sum(st.count for st in pruned_states) == EXPECTED_TOTAL


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


@lru_cache(None)
def pow3(q: int) -> int:
    return 3 ** q


@lru_cache(None)
def inv3pow_mod_2e(q: int, e: int) -> int:
    M = 1 << e
    return pow(pow(3, q, M), -1, M)


# Lite state = (y, lo, hi, h, q).
def source_child(st, d: int):
    y, lo, hi, h, q = st
    target = defect.TPOS[q]
    assert target >= h
    assert 0 <= d <= target - h

    actual = target - d
    a = actual - h
    e = a + 1
    M = 1 << e
    A = pow3(q)
    rho = (((1 << a) - y) * inv3pow_mod_2e(q, e)) % M

    lo2 = ceil_div(lo - rho, M)
    hi2 = (hi - rho) // M
    if lo2 > hi2:
        return None

    y2 = (3 * (y + A * rho) + (1 << a)) // M
    return (y2, lo2, hi2, actual + 1, q + 1)


if __name__ == "__main__":
    print("PASS lightweight cumulative-pruned jump8 frontier export")
    print("future_eta_floor", ">1/3 weakened to >=1/3")
    print("states", len(pruned_states))
    print("population", sum(st.count for st in pruned_states))
    print("pruned_from_first75_tightened", pruned)
