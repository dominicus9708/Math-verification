#!/usr/bin/env python3
"""Exact c=5 horizon-51 shard probe on the current >=5/12 frontier.

This is deliberately a decision probe, not an extrapolation from H_0..H_4.
It preserves exact source intervals and asks whether each source parent admits
an exact pure-ballot future path of 51 one-events with at most five displaced
target ranks.
"""

import os
from functools import lru_cache

import A0_s1_8jump_cumulative_pruned_frontier_export as src

SHARD_ID = int(os.environ["SHARD_ID"])
SHARD_COUNT = int(os.environ.get("SHARD_COUNT", "64"))
HORIZON = 51
C = 5
OUTPUT_PATH = os.environ.get("OUTPUT_PATH")

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

live = sum(reachable(st, C, HORIZON) for st in parents)

print("PASS c5 horizon51 shard probe", SHARD_ID)
print("shard_parent_count", len(parents))
print("parents_with_c5_path_h51", live)
print("reachable_cache", reachable.cache_info())
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)

if OUTPUT_PATH:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(f"{SHARD_ID} {len(parents)} {live}\n")
