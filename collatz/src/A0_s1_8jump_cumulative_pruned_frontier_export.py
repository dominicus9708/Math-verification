#!/usr/bin/env python3
"""Lightweight export of the canonical jump-8 frontier after cumulative pruning.

This module intentionally does NOT rerun the bounded-displacement searches on
import.  It imports the certified first-75-tightened states and applies the
latest certified cumulative future-defect floor

    global H_4 = 50,
    horizon 51 survivor => at least 5 displaced target ranks
                        => eta_future > 5/12,

safely weakened to eta_future>=5/12 for endpoint pruning.

The older >=1/4 and >=1/3 cuts are superseded by this stronger floor.  These
floors are not added to one another.
"""

from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi
ETA_FLOOR = Fraction(5, 12)
EXPECTED_TOTAL = 26_859_837_368_480_843_030
EXPECTED_PRUNED = 107_427_224


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
    print("global_H4", 50)
    print("forced_horizon", 51)
    print("future_eta_floor", ">5/12 weakened to >=5/12")
    print("states", len(pruned_states))
    print("population", sum(st.count for st in pruned_states))
    print("pruned_from_first75_tightened", pruned)
