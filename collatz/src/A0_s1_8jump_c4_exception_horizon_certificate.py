#!/usr/bin/env python3
"""Exact deep check of the only horizon-49 c=4 exception shards.

The 32-shard horizon-49 certificate leaves exactly one <=4-displacement live
parent in shard 3 and one in shard 24.  This program continues only those two
shards and certifies:

  shard 3 : live(49)=1, live(50)=0;
  shard 24: live(49)=1, live(50)=1, live(51)=0.

Together with the horizon-49 aggregate this gives the exact global value
H_4=50 on the current canonical >=1/3 jump-8 frontier.
"""

import os
from functools import lru_cache

import A0_s1_8jump_cumulative_pruned_frontier_export as src

SHARD_ID = int(os.environ["SHARD_ID"])
SHARD_COUNT = 32
C = 4
EXPECTED = {
    3: {49: 1, 50: 0},
    24: {49: 1, 50: 1, 51: 0},
}
assert SHARD_ID in EXPECTED


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


all_parents = tuple(lite(st) for st in src.pruned_states)
parents = all_parents[SHARD_ID::SHARD_COUNT]
assert parents

for horizon, expected in EXPECTED[SHARD_ID].items():
    live = sum(reachable(st, C, horizon) for st in parents)
    print("shard", SHARD_ID, "horizon", horizon, "parents_with_c4_path", live)
    assert live == expected

print("PASS c4 exceptional-shard horizon certificate", SHARD_ID)
print("shard_parent_count", len(parents))
print("global_H4_contribution", 49 if SHARD_ID == 3 else 50)
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)
