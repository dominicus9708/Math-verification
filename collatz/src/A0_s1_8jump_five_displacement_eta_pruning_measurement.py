#!/usr/bin/env python3
"""Historical endpoint measurement for eta_future>=5/12.

The first run of this file was intentionally conditional while H_4 was still
being resolved.  Subsequent exact c=4 scans established global H_4=50, so a
horizon-51 survivor must use at least five displaced target ranks and the
5/12 endpoint floor is now formalized in
A0_s1_8jump_five_displacement_eta_pruning_certificate.py.

This file is retained only as a lightweight arithmetic regression.  The old
>=1/3 floor is replaced by >=5/12; the floors are not added.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

ETA_THIRD = Fraction(1, 3)
ETA_FIVE_TWELFTHS = Fraction(5, 12)
EXPECTED_THIRD_TOTAL = 26_859_837_368_506_133_665
EXPECTED_FIVE_TWELFTHS_TOTAL = 26_859_837_368_480_843_030
EXPECTED_INCREMENTAL = 25_290_635


def retained_hi(st, eta_future: Fraction) -> int:
    cut = (Fraction(BARRIER, 1) - M_LO * (st.eta + eta_future)) / DELTA_LO
    z = (cut - st.r) / (1 << st.h)
    return min(st.hi, z.numerator // z.denominator)


def cut_states(eta_future: Fraction):
    out = []
    pruned = 0
    affected = 0
    whole = 0
    for st in tail.states:
        hi2 = retained_hi(st, eta_future)
        if hi2 < st.lo:
            pruned += st.count
            affected += 1
            whole += 1
            continue
        removed = st.hi - hi2
        pruned += removed
        affected += int(removed > 0)
        out.append(tail.State(st.r, st.y, st.lo, hi2, st.h, st.S, st.D, st.eta, st.root_f))
    return tuple(out), pruned, affected, whole


third_states, third_pruned, _, third_whole = cut_states(ETA_THIRD)
five_states, five_pruned, five_affected, five_whole = cut_states(ETA_FIVE_TWELFTHS)

assert third_whole == 0
assert sum(st.count for st in third_states) == EXPECTED_THIRD_TOTAL
assert ETA_FIVE_TWELFTHS > ETA_THIRD

new_population = sum(st.count for st in five_states)
incremental = EXPECTED_THIRD_TOTAL - new_population
assert incremental == five_pruned - third_pruned
assert incremental == EXPECTED_INCREMENTAL
assert new_population == EXPECTED_FIVE_TWELFTHS_TOTAL

print("PASS five-displacement eta 5/12 endpoint regression")
print("global_H4", 50)
print("forced_horizon", 51)
print("previous_floor", ">1/3, endpoint >=1/3")
print("current_floor", ">5/12, endpoint >=5/12")
print("before_population", EXPECTED_THIRD_TOTAL)
print("additional_pruned", incremental)
print("affected_intervals_under_5_12", five_affected)
print("whole_intervals_removed", five_whole)
print("remaining_intervals", len(five_states))
print("new_population", new_population)
print("double_counted_old_third_floor", False)
print("formal_certificate", "A0_s1_8jump_five_displacement_eta_pruning_certificate.py")
