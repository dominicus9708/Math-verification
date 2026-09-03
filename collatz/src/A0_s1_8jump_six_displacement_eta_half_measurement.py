#!/usr/bin/env python3
"""Conditional endpoint arithmetic for a prospective eta_future >= 1/2 cut.

Interpretation is conditional on an independent exact certificate showing that
no current >=5/12 source parent admits a horizon-51 path with at most five
displaced target ranks.  If so, D_51>=6 and the strict per-displacement bound
>1/12 gives eta_future>1/2; endpoint use may safely weaken to >=1/2.

This file ONLY measures the exact endpoint set difference.  It does not prove
the c=5 reachability premise.  The >=1/2 floor would replace, not add to, the
current >=5/12 floor.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

ETA_5_12 = Fraction(5, 12)
ETA_HALF = Fraction(1, 2)
EXPECTED_5_12_TOTAL = 26_859_837_368_480_843_030


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
        out.append(tail.State(
            st.r, st.y, st.lo, hi2, st.h, st.S,
            st.D, st.eta, st.root_f,
        ))
    return tuple(out), pruned, affected, whole


five_states, five_pruned, _, five_whole = cut_states(ETA_5_12)
half_states, half_pruned, half_affected, half_whole = cut_states(ETA_HALF)

assert five_whole == 0
assert sum(st.count for st in five_states) == EXPECTED_5_12_TOTAL
assert ETA_HALF > ETA_5_12

new_population = sum(st.count for st in half_states)
incremental = EXPECTED_5_12_TOTAL - new_population
assert incremental == half_pruned - five_pruned
assert incremental >= 0

print("PASS conditional eta half endpoint measurement")
print("reachability_premise_required", "no c<=5 path at horizon 51 on current >=5/12 frontier")
print("if_premise_then_D51_at_least", 6)
print("if_premise_then_eta_future", ">1/2; endpoint >=1/2")
print("before_population", EXPECTED_5_12_TOTAL)
print("additional_pruned", incremental)
print("affected_intervals_under_half", half_affected)
print("whole_intervals_removed", half_whole)
print("remaining_intervals", len(half_states))
print("new_population", new_population)
print("double_counted_old_five_twelfths_floor", False)
