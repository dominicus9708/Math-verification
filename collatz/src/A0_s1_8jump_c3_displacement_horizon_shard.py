#!/usr/bin/env python3
"""One exact shard of the c=3 bounded-displacement horizon scan."""

import os
from functools import lru_cache

import A0_s1_8jump_cumulative_pruned_frontier_export as src

SHARD_ID = int(os.environ["SHARD_ID"])
SHARD_COUNT = int(os.environ.get("SHARD_COUNT", "16"))
START_HORIZON = 46
MAX_SCAN_HORIZON = 60
C = 3

assert 0 <= SHARD_ID < SHARD_COUNT


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
    for d in range(1, target - h + 1):
        ch = src.source_child(st, d)
        if ch is not None and reachable(ch, c - 1, r - 1):
            return True
    return False


all_parents = tuple(lite(st) for st in src.pruned_states)
parents = all_parents[SHARD_ID::SHARD_COUNT]
assert parents

# The canonical subset inherits the certified c<=2 horizon-46 emptiness.
assert not any(reachable(st, 2, 46) for st in parents)

first_empty = None
last_live = None
for r in range(START_HORIZON, MAX_SCAN_HORIZON + 1):
    live = sum(reachable(st, C, r) for st in parents)
    print("shard", SHARD_ID, "horizon", r, "parents_with_c3_path", live)
    if live == 0:
        first_empty = r
        break
    last_live = r

assert first_empty is not None, "increase MAX_SCAN_HORIZON"
max_h3 = first_empty - 1
print("PASS shard", SHARD_ID)
print("shard_parent_count", len(parents))
print("first_empty_horizon", first_empty)
print("max_H3_shard", max_h3)
print("reachable_cache", reachable.cache_info())
