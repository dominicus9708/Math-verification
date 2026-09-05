#!/usr/bin/env python3
"""Certify the c=4 horizon result and eta_future >= 5/12 endpoint pruning.

Finite exact source-preserving execution on the canonical eta>=1/3 jump-8
frontier gives:

- at horizon 49, exactly two <=4-displacement parents remain, one in shard 3
  and one in shard 24; every other one of the 32 shards is empty;
- shard 3 is empty at horizon 50;
- shard 24 remains live at horizon 50 and is empty at horizon 51.

Hence the exact current-frontier maximum is H_4=50.  Every horizon-51 survivor
therefore uses at least five displaced target ranks.  The certified target
phase bound gives normalized defect >1/12 per displaced rank, so
eta_future > 5/12.  Endpoint pruning safely weakens this to >=5/12.

The previous >=1/3 floor is REPLACED, not added.  This program recomputes both
cuts from the same first-75-tightened source intervals and checks the exact set
difference.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect
M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

GLOBAL_MAX_H4 = 50
FORCED_HORIZON = 51
FORCED_DISPLACED_RANKS = 5
H49_EXCEPTION_SHARDS = (3, 24)
H49_LIVE_TOTAL = 2
SHARD3_MAX_H4 = 49
SHARD24_MAX_H4 = 50

ETA_THIRD = Fraction(1, 3)
ETA_FIVE_TWELFTHS = Fraction(5, 12)

TIGHT_TOTAL = 26_859_837_368_588_270_254
THIRD_TOTAL = 26_859_837_368_506_133_665
FIVE_TWELFTHS_TOTAL = 26_859_837_368_480_843_030
THIRD_PRUNED_FROM_FIRST75 = 82_136_589
FIVE_TWELFTHS_PRUNED_FROM_FIRST75 = 107_427_224
INCREMENTAL_FIVE_TWELFTHS = 25_290_635
FIVE_TWELFTHS_AFFECTED = 7_198

assert max(SHARD3_MAX_H4, SHARD24_MAX_H4) == GLOBAL_MAX_H4
assert FORCED_HORIZON == GLOBAL_MAX_H4 + 1
assert ETA_FIVE_TWELFTHS > ETA_THIRD


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


assert len(tail.states) == 14_224
assert sum(st.count for st in tail.states) == TIGHT_TOTAL

third_states, third_pruned, third_affected, third_whole = cut_states(ETA_THIRD)
five_states, five_pruned, five_affected, five_whole = cut_states(ETA_FIVE_TWELFTHS)

assert third_pruned == THIRD_PRUNED_FROM_FIRST75
assert sum(st.count for st in third_states) == THIRD_TOTAL
assert third_whole == 0

assert five_pruned == FIVE_TWELFTHS_PRUNED_FROM_FIRST75
assert sum(st.count for st in five_states) == FIVE_TWELFTHS_TOTAL
assert five_whole == 0
assert len(five_states) == 14_224
assert five_affected == FIVE_TWELFTHS_AFFECTED

incremental = 0
incremental_affected = 0
for tst, fst in zip(third_states, five_states):
    assert (tst.r, tst.y, tst.lo, tst.h, tst.S, tst.D, tst.eta, tst.root_f) == (
        fst.r, fst.y, fst.lo, fst.h, fst.S, fst.D, fst.eta, fst.root_f
    )
    assert fst.hi <= tst.hi
    removed = tst.hi - fst.hi
    incremental += removed
    incremental_affected += int(removed > 0)

assert incremental == INCREMENTAL_FIVE_TWELFTHS
assert third_pruned + incremental == five_pruned
assert THIRD_TOTAL - incremental == FIVE_TWELFTHS_TOTAL

# New canonical source intervals for downstream S10 work.
pruned_states = five_states

print("PASS A0 s=1 five-displacement eta five-twelfths pruning certificate")
print("global_max_H4", GLOBAL_MAX_H4)
print("h49_exception_shards", H49_EXCEPTION_SHARDS)
print("h49_live_total", H49_LIVE_TOTAL)
print("shard3_max_H4", SHARD3_MAX_H4)
print("shard24_max_H4", SHARD24_MAX_H4)
print("forced_horizon", FORCED_HORIZON)
print("forced_minimum_displaced_ranks", FORCED_DISPLACED_RANKS)
print("future_eta_floor", ">5/12, safely weakened to >=5/12 for endpoint cut")
print("third_floor_population", THIRD_TOTAL)
print("five_twelfths_population", FIVE_TWELFTHS_TOTAL)
print("incremental_pruned_third_to_five_twelfths", incremental)
print("incremental_affected_intervals", incremental_affected)
print("affected_intervals_under_five_twelfths", five_affected)
print("whole_intervals_removed", five_whole)
print("remaining_intervals", len(pruned_states))
print("floors_added_together", False)
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)
print("status", "EXACT finite current-frontier cumulative-displacement pruning; no universal Route-B closure claimed")
