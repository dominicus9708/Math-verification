#!/usr/bin/env python3
"""Sparse exact bounded-displacement horizon from the canonical pruned jump-8 frontier.

Implements SPARSE_FIRST_DISPLACEMENT_REACHABILITY_RECURSION.md on the exported
`pruned_states` produced after first-75 tightening plus the certified horizon-46
three-displacement pruning.

For c=0..3, H_c(s) is the maximum future one-event horizon reachable from one
exact source interval with at most c displaced target ranks.  Hence horizon
max_s H_c(s)+1 forces at least c+1 displaced ranks on every surviving source.

This is a finite exact source calculation.  No payload merge and no linear
extrapolation in c are used.
"""

from functools import lru_cache
from collections import Counter

import A0_s1_8jump_bounded_displacement_reachability_certificate as bd


def lite(st):
    return (st.y, st.lo, st.hi, st.h, st.q)


@lru_cache(None)
def zero_chain(st):
    chain = [st]
    cur = st
    while True:
        ch = bd.source_child(cur, 0)
        if ch is None:
            break
        chain.append(ch)
        cur = ch
    return tuple(chain)


@lru_cache(None)
def H(st, c: int) -> int:
    chain = zero_chain(st)
    L0 = len(chain) - 1
    if c == 0:
        return L0

    best = L0
    for k, z in enumerate(chain):
        y, lo, hi, h, q = z
        target = bd.defect.TPOS[q]
        max_d = target - h
        assert max_d >= 0
        for d in range(1, max_d + 1):
            ch = bd.source_child(z, d)
            if ch is None:
                continue
            cand = k + 1 + H(ch, c - 1)
            if cand > best:
                best = cand
    return best


parents = tuple(lite(st) for st in bd.pruned_states)
assert len(parents) == 14_224
assert sum(st.count for st in bd.pruned_states) == bd.NEW_TOTAL

rows = []
for c in range(4):
    vals = [H(st, c) for st in parents]
    mx = max(vals)
    hist = dict(sorted(Counter(vals).items()))
    rows.append((c, mx, hist))
    print("budget", c, "max_H", mx, "forced_min_displacements_at_horizon", mx + 1, c + 1)
    print("H_histogram", hist)
    print("H_cache", H.cache_info())
    print("zero_chain_cache", zero_chain.cache_info())

# Regression against the already-certified relaxed-source results.  The new
# frontier is a subset, so these maxima cannot increase.  c=0 is known to keep
# a one-element zero path through horizon 40 even after the previous pruning.
assert rows[0][1] == 40
assert rows[1][1] <= 44
assert rows[2][1] <= 45

print("PASS A0 s=1 sparse cumulative displacement horizon certificate")
print("canonical_parent_count", len(parents))
print("canonical_population", bd.NEW_TOTAL)
print("maxima", {c: mx for c, mx, _ in rows})
print("source_payload_merging_used", False)
print("linear_extrapolation_used", False)
print("status", "EXACT finite sparse reachability for c<=3 on canonical pruned jump-8 frontier")
