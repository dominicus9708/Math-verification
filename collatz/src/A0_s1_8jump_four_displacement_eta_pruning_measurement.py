#!/usr/bin/env python3
"""Measure the exact incremental source-tail cut from the certified c=3 result.

The completed 16-shard execution gives max H_3=48 on the current canonical
jump-8 frontier. Therefore every horizon-49 survivor has at least four future
displaced target ranks. Each displaced mechanical rank contributes normalized
eta > 1/12, hence every survivor has future eta > 1/3.

For pruning we safely weaken >1/3 to >=1/3 and replace the previously used
>=1/4 future floor.  The input `src.pruned_states` already incorporates the
1/4 cut, so this program applies only the stronger resulting upper endpoint
and reports the *additional* exact removal; it never adds 1/3 to 1/4.
"""

from fractions import Fraction

import A0_s1_8jump_cumulative_pruned_frontier_export as src

ETA_OLD = Fraction(1, 4)
ETA_NEW = Fraction(1, 3)
assert ETA_NEW > ETA_OLD

before = sum(st.count for st in src.pruned_states)
assert before == src.EXPECTED_TOTAL

new_states = []
additional_pruned = 0
affected = 0
whole = 0

for st in src.pruned_states:
    cut = (
        Fraction(src.BARRIER, 1)
        - src.M_LO * (st.eta + ETA_NEW)
    ) / src.DELTA_LO
    hi2 = src.retained_hi(st, cut)

    if hi2 < st.lo:
        additional_pruned += st.count
        affected += 1
        whole += 1
        continue

    removed = st.hi - hi2
    additional_pruned += removed
    affected += (removed > 0)
    new_states.append(src.tail.State(
        st.r, st.y, st.lo, hi2, st.h, st.S,
        st.D, st.eta, st.root_f,
    ))

new_total = sum(st.count for st in new_states)
assert before - additional_pruned == new_total
assert new_total >= 0

print("PASS A0 s=1 c3 four-displacement eta-floor pruning measurement")
print("global_max_H3", 48)
print("forced_horizon", 49)
print("forced_minimum_displaced_ranks", 4)
print("future_eta_floor_used", ">1/3 weakened to >=1/3")
print("previous_future_eta_floor", ">1/4")
print("before_population", before)
print("additional_pruned", additional_pruned)
print("affected_intervals", affected)
print("whole_intervals_removed", whole)
print("remaining_intervals", len(new_states))
print("new_population", new_total)
print("double_counted_old_quarter_floor", False)
print("status", "EXACT finite endpoint calculation conditional only on the certified c3 shard result")
