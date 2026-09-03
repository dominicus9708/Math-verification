#!/usr/bin/env python3
"""Lightweight export of the canonical jump-8 frontier after cumulative pruning.

This module intentionally does NOT rerun the c=0,1,2 bounded-displacement
breadth-first audits on import.  It imports the certified first-75-tightened
states, reapplies only the already-certified horizon-46 eta>1/4 source-tail
cut, and exports the resulting exact 14,224 intervals plus the exact future
source-child map used by sparse reachability calculations.

The constants and resulting population are regression-checked against
A0_s1_8jump_bounded_displacement_reachability_certificate.py.
"""

from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi
ETA_FLOOR = Fraction(1, 4)
EXPECTED_TOTAL = 26_859_837_368_531_301_450
EXPECTED_PRUNED = 56_968_804


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
    print("states", len(pruned_states))
    print("population", sum(st.count for st in pruned_states))
    print("incremental_pruned", pruned)
