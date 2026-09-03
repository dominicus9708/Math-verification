#!/usr/bin/env python3
"""Formal endpoint certificate for the six-displacement eta>=1/2 cut.

Reachability evidence is the completed exact 64-shard execution of
A0_s1_8jump_c5_h51_shard_probe.py, GitHub Actions run 33756884264.
Its aggregate result is:

    shard_count = 64
    parent_count = 14224
    parents_with_c5_path_h51 = 0
    live_shard_count = 0

Therefore, on the canonical >=5/12 jump-8 source frontier, no exact
source-preserving pure-ballot path reaches horizon 51 with <=5 displaced
ranks. Hence every horizon-51 survivor has D_51>=6. Since every displaced
rank contributes normalized future defect >1/12, eta_future>1/2. For the
monotone endpoint cut we safely weaken this to eta_future>=1/2.

This file recomputes the old >=5/12 and new >=1/2 cuts from the SAME
first-75-tightened source intervals. The floors are nested descriptions of
the same future defect and are never added.

Important: h51 emptiness proves H_5<=50 on this current frontier. It does not
by itself prove H_5=50; no exact H_5 equality is claimed here.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

REACHABILITY_RUN_ID = 33756884264
SHARD_COUNT = 64
SOURCE_PARENT_COUNT = 14_224
C5_H51_LIVE = 0
LIVE_SHARD_COUNT = 0
FORCED_HORIZON = 51
FORCED_DISPLACED_RANKS = 6

ETA_5_12 = Fraction(5, 12)
ETA_HALF = Fraction(1, 2)

FIRST75_TOTAL = 26_859_837_368_588_270_254
FIVE_TWELFTHS_TOTAL = 26_859_837_368_480_843_030
HALF_TOTAL = 26_859_837_368_455_538_464
FIVE_TWELFTHS_PRUNED_FROM_FIRST75 = 107_427_224
HALF_PRUNED_FROM_FIRST75 = 132_731_790
INCREMENTAL_HALF = 25_304_566
HALF_AFFECTED = 7_299

assert C5_H51_LIVE == 0
assert LIVE_SHARD_COUNT == 0
assert SHARD_COUNT == 64
assert SOURCE_PARENT_COUNT == 14_224
assert FORCED_DISPLACED_RANKS == 6
assert ETA_HALF > ETA_5_12


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


assert len(tail.states) == SOURCE_PARENT_COUNT
assert sum(st.count for st in tail.states) == FIRST75_TOTAL

five_states, five_pruned, _, five_whole = cut_states(ETA_5_12)
half_states, half_pruned, half_affected, half_whole = cut_states(ETA_HALF)

assert five_pruned == FIVE_TWELFTHS_PRUNED_FROM_FIRST75
assert sum(st.count for st in five_states) == FIVE_TWELFTHS_TOTAL
assert five_whole == 0

assert half_pruned == HALF_PRUNED_FROM_FIRST75
assert sum(st.count for st in half_states) == HALF_TOTAL
assert half_whole == 0
assert len(half_states) == SOURCE_PARENT_COUNT
assert half_affected == HALF_AFFECTED

incremental = 0
incremental_affected = 0
for old, new in zip(five_states, half_states):
    assert (old.r, old.y, old.lo, old.h, old.S, old.D, old.eta, old.root_f) == (
        new.r, new.y, new.lo, new.h, new.S, new.D, new.eta, new.root_f
    )
    assert new.hi <= old.hi
    removed = old.hi - new.hi
    incremental += removed
    incremental_affected += int(removed > 0)

assert incremental == INCREMENTAL_HALF
assert five_pruned + incremental == half_pruned
assert FIVE_TWELFTHS_TOTAL - incremental == HALF_TOTAL

# New canonical source intervals for downstream S10 work.
pruned_states = half_states

print("PASS A0 s=1 six-displacement eta-half pruning certificate")
print("reachability_run_id", REACHABILITY_RUN_ID)
print("shard_count", SHARD_COUNT)
print("source_parent_count", SOURCE_PARENT_COUNT)
print("parents_with_c5_path_h51", C5_H51_LIVE)
print("live_shard_count", LIVE_SHARD_COUNT)
print("H5_upper_bound", 50)
print("H5_exact_equality_claimed", False)
print("forced_horizon", FORCED_HORIZON)
print("forced_minimum_displaced_ranks", FORCED_DISPLACED_RANKS)
print("future_eta_floor", ">1/2, safely weakened to >=1/2 for endpoint cut")
print("five_twelfths_population", FIVE_TWELFTHS_TOTAL)
print("half_population", HALF_TOTAL)
print("incremental_pruned_5_12_to_half", incremental)
print("incremental_affected_intervals", incremental_affected)
print("affected_intervals_under_half", half_affected)
print("whole_intervals_removed", half_whole)
print("remaining_intervals", len(pruned_states))
print("nested_floors_added_together", False)
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)
print("status", "EXACT finite reachability result + exact endpoint arithmetic; Route-B remains OPEN")
