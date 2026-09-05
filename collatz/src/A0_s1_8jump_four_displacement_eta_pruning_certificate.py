#!/usr/bin/env python3
"""Certify the horizon-49 four-displacement eta floor and source-tail pruning.

Upstream exact source reachability was executed in 16 independent GitHub
Actions shards on the then-canonical eta>1/4 jump-8 frontier.  The shard maxima
for H_3, the longest future one-event horizon reachable with at most three
displaced target ranks, were

    (45,46,45,48,45,45,45,45,46,46,45,45,45,45,45,45).

Hence global max H_3=48.  Every source member surviving 49 future one-events
must therefore have at least four displaced target ranks.

The already-certified mechanical target phase bound gives normalized defect
strictly greater than 1/12 for every displaced rank.  Thus every horizon-49
survivor has future eta>1/3.  For endpoint pruning we weaken this safely to
eta_future>=1/3.

This program independently applies both the prior >=1/4 and the stronger
>=1/3 floors to the same first-75-tightened jump-8 source intervals.  The
reported 25,167,785 removal is the set difference between those two cuts; the
floors are NOT added.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

SHARD_MAX_H3 = (45, 46, 45, 48, 45, 45, 45, 45,
                46, 46, 45, 45, 45, 45, 45, 45)
GLOBAL_MAX_H3 = 48
FORCED_HORIZON = 49
FORCED_DISPLACED_RANKS = 4
ETA_QUARTER = Fraction(1, 4)
ETA_THIRD = Fraction(1, 3)

TIGHT_TOTAL = 26_859_837_368_588_270_254
QUARTER_TOTAL = 26_859_837_368_531_301_450
THIRD_TOTAL = 26_859_837_368_506_133_665
QUARTER_PRUNED = 56_968_804
THIRD_TOTAL_PRUNED = 82_136_589
INCREMENTAL_THIRD = 25_167_785
INCREMENTAL_AFFECTED = 6_310

assert max(SHARD_MAX_H3) == GLOBAL_MAX_H3
assert FORCED_HORIZON == GLOBAL_MAX_H3 + 1
assert ETA_THIRD > ETA_QUARTER


def retained_hi(st, eta_future: Fraction) -> int:
    cut = (
        Fraction(BARRIER, 1) - M_LO * (st.eta + eta_future)
    ) / DELTA_LO
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
        affected += (removed > 0)
        out.append(tail.State(
            st.r, st.y, st.lo, hi2, st.h, st.S,
            st.D, st.eta, st.root_f,
        ))
    return tuple(out), pruned, affected, whole


assert len(tail.states) == 14_224
assert sum(st.count for st in tail.states) == TIGHT_TOTAL

quarter_states, quarter_pruned, quarter_affected, quarter_whole = cut_states(ETA_QUARTER)
third_states, third_pruned, third_affected, third_whole = cut_states(ETA_THIRD)

assert quarter_pruned == QUARTER_PRUNED
assert sum(st.count for st in quarter_states) == QUARTER_TOTAL
assert quarter_whole == 0

assert third_pruned == THIRD_TOTAL_PRUNED
assert sum(st.count for st in third_states) == THIRD_TOTAL
assert third_whole == 0
assert len(third_states) == 14_224

# Sequential strengthening: compare the same original interval cuts.  Every
# 1/3-retained interval is a prefix of the corresponding 1/4-retained one.
incremental = 0
incremental_affected = 0
for qst, tst in zip(quarter_states, third_states):
    assert (qst.r, qst.y, qst.lo, qst.h, qst.S, qst.D, qst.eta, qst.root_f) == (
        tst.r, tst.y, tst.lo, tst.h, tst.S, tst.D, tst.eta, tst.root_f
    )
    assert tst.hi <= qst.hi
    removed = qst.hi - tst.hi
    incremental += removed
    incremental_affected += (removed > 0)

assert incremental == INCREMENTAL_THIRD
assert incremental_affected == INCREMENTAL_AFFECTED
assert QUARTER_TOTAL - incremental == THIRD_TOTAL
assert third_pruned - quarter_pruned == incremental

# Export the new canonical source intervals for downstream work.
pruned_states = third_states

print("PASS A0 s=1 four-displacement eta one-third pruning certificate")
print("shard_max_H3", SHARD_MAX_H3)
print("global_max_H3", GLOBAL_MAX_H3)
print("forced_horizon", FORCED_HORIZON)
print("forced_minimum_displaced_ranks", FORCED_DISPLACED_RANKS)
print("future_eta_floor", ">1/3, safely weakened to >=1/3 for endpoint cut")
print("first75_tightened_population", TIGHT_TOTAL)
print("quarter_floor_population", QUARTER_TOTAL)
print("third_floor_population", THIRD_TOTAL)
print("quarter_floor_pruned_from_first75", quarter_pruned)
print("third_floor_pruned_from_first75", third_pruned)
print("incremental_pruned_quarter_to_third", incremental)
print("incremental_affected_intervals", incremental_affected)
print("whole_intervals_removed", third_whole)
print("remaining_intervals", len(pruned_states))
print("floors_added_together", False)
print("source_payload_merging_used", False)
print("status", "EXACT finite current-frontier cumulative-displacement pruning; no universal Route-B closure claimed")
