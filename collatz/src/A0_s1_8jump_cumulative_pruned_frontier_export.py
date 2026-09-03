#!/usr/bin/env python3
"""Lightweight export of the canonical jump-8 frontier after cumulative pruning.

This module intentionally does NOT rerun bounded-displacement searches on
import. It imports the certified first-75-tightened states and applies the
latest certified cumulative future-defect floor.

Exact finite reachability evidence on the current >=5/12 frontier gives

    no D_51<=5 path among all 14,224 source parents,
    hence D_51>=6 for every horizon-51 survivor,
    hence eta_future>1/2.

For monotone endpoint pruning this is safely weakened to eta_future>=1/2.
The older >=1/4, >=1/3, and >=5/12 floors are superseded by this stronger
floor. These floors are nested descriptions of the same future defect and are
never added.

Important: the h51 decision proves H_5<=50, not H_5=50.
"""

from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi
ETA_FLOOR = Fraction(1, 2)
EXPECTED_TOTAL = 26_859_837_368_455_538_464
EXPECTED_PRUNED = 132_731_790


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
    print("c5_h51_live", 0)
    print("H5_upper_bound", 50)
    print("H5_exact_equality_claimed", False)
    print("forced_horizon", 51)
    print("forced_minimum_displaced_ranks", 6)
    print("future_eta_floor", ">1/2 weakened to >=1/2")
    print("states", len(pruned_states))
    print("population", sum(st.count for st in pruned_states))
    print("pruned_from_first75_tightened", pruned)
