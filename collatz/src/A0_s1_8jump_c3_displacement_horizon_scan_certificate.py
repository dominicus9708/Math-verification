#!/usr/bin/env python3
"""Exact decision scan for the c=3 bounded-displacement horizon.

Uses the lightweight canonical pruned jump-8 frontier export, so previous
c=0,1,2 breadth-first audits are not rerun on import.

R(s,c,r) asks whether one exact source path of r future one-events exists with
at most c displaced target ranks.  The scan stops at the first globally empty
horizon, which is exactly max_s H_c(s)+1.
"""

from functools import lru_cache

import A0_s1_8jump_cumulative_pruned_frontier_export as src

START_HORIZON = 46
MAX_SCAN_HORIZON = 60
C = 3


def lite(st):
    return (st.y, st.lo, st.hi, st.h, st.q)


@lru_cache(None)
def reachable(st, c: int, r: int) -> bool:
    if r == 0:
        return True

    z = src.source_child(st, 0)
    if z is not None and reachable(z, c, r - 1):
        return True

    if c == 0:
        return False

    y, lo, hi, h, q = st
    target = src.defect.TPOS[q]
    max_d = target - h
    assert max_d >= 0
    for d in range(1, max_d + 1):
        ch = src.source_child(st, d)
        if ch is not None and reachable(ch, c - 1, r - 1):
            return True
    return False


parents = tuple(lite(st) for st in src.pruned_states)
assert len(parents) == 14_224
assert sum(st.count for st in src.pruned_states) == src.EXPECTED_TOTAL

# Certified c<=2 result on the larger pre-pruning frontier implies emptiness
# here as well at horizon 46.
assert not any(reachable(st, 2, 46) for st in parents)

rows = []
first_empty = None
for r in range(START_HORIZON, MAX_SCAN_HORIZON + 1):
    live = sum(reachable(st, C, r) for st in parents)
    rows.append((r, live))
    print("horizon", r, "parents_with_c3_path", live)
    if live == 0:
        first_empty = r
        break

assert first_empty is not None, "c3 remains nonempty through scan cap; extend MAX_SCAN_HORIZON"
if len(rows) >= 2:
    assert rows[-2][1] > 0

print("PASS A0 s=1 c3 displacement horizon decision scan")
print("first_globally_empty_horizon", first_empty)
print("max_H3", first_empty - 1)
print("forced_min_displaced_ranks_at_horizon", first_empty, 4)
print("normalized_future_eta_floor", "> 1/3")
print("reachable_cache", reachable.cache_info())
print("source_payload_merging_used", False)
print("status", "EXACT finite c=3 reachability decision on canonical pruned jump-8 frontier")
