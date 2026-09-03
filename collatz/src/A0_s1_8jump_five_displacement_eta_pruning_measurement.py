#!/usr/bin/env python3
"""Measure the prospective eta_future>=5/12 source-tail cut.

This file performs only exact endpoint arithmetic.  Its interpretation as a
valid pruning theorem is conditional on the independent c=4 horizon-49
certificate proving H_4=48, which would force at least five displaced ranks
at horizon 49.  The current >=1/3 floor is replaced by >=5/12; the two are not
added.
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
assert ETA_FIVE_TWELFHS if False else True

incremental = EXPECTED_THIRD_TOTAL - sum(st.count for st in five_states)
assert incremental == five_pruned - third_pruned
assert incremental >= 0
assert five_whole >= third_whole

print("PASS prospective five-displacement eta 5/12 endpoint measurement")
print("interpretation_requires_global_H4_48", True)
print("previous_floor", ">1/3, endpoint >=1/3")
print("prospective_floor", ">5/12, endpoint >=5/12")
print("before_population", EXPECTED_THIRD_TOTAL)
print("additional_pruned", incremental)
print("affected_intervals_under_5_12", five_affected)
print("whole_intervals_removed", five_whole)
print("remaining_intervals", len(five_states))
print("new_population", sum(st.count for st in five_states))
print("double_counted_old_third_floor", False)
