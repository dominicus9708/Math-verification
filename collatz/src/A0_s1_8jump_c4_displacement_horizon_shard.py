#!/usr/bin/env python3
"""One exact shard of the c=4 bounded-displacement horizon scan.

Input is the latest canonical eta_future>=1/3 jump-8 frontier exported by
A0_s1_8jump_cumulative_pruned_frontier_export.py.

R(s,c,r) asks whether an exact nonempty source path of r future one-events
exists with at most c displaced target ranks.  Each shard scans upward from
horizon 49 and returns its first globally empty horizon.  The maximum over
shards of (first_empty-1) is the exact global H_4.
"""

import os
from functools import lru_cache

import A0_s1_8jump_cumulative_pruned_frontier_export as src

SHARD_ID = int(os.environ["SHARD_ID"])
SHARD_COUNT = int(os.environ.get("SHARD_COUNT", "32"))
START_HORIZON = 49
MAX_SCAN_HORIZON = 65
C = 4

assert 0 <= SHARD_ID < SHARD_COUNT


def lite(st):
    return (st.y, st.lo, st.hi, st.h, st.q)


@lru_cache(None)
def reachable(st, c: int, r: int) -> bool:
    if r == 0:
        return True

    # Zero-displacement branch first for short-circuiting.
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


all_parents = tuple(lite(st) for st in src.pruned_states)
parents = all_parents[SHARD_ID::SHARD_COUNT]
assert parents

# The previously certified c=3 result was obtained on a larger frontier:
# no <=3-displacement path reaches horizon 49 there, hence not on this subset.
assert not any(reachable(st, 3, 49) for st in parents)

first_empty = None
last_live = None
rows = []
for r in range(START_HORIZON, MAX_SCAN_HORIZON + 1):
    live = sum(reachable(st, C, r) for st in parents)
    rows.append((r, live))
    print("shard", SHARD_ID, "horizon", r, "parents_with_c4_path", live)
    if live == 0:
        first_empty = r
        break
    last_live = r

assert first_empty is not None, "increase MAX_SCAN_HORIZON"

print("PASS c4 shard", SHARD_ID)
print("shard_parent_count", len(parents))
print("first_empty_horizon", first_empty)
print("max_H4_shard", first_empty - 1)
print("last_live_horizon", last_live)
print("reachable_cache", reachable.cache_info())
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)
