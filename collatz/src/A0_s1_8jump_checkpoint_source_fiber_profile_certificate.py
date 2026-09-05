#!/usr/bin/env python3
"""Exact per-checkpoint source-fiber capacity profile on the canonical jump-8 frontier.

For a fixed ordinary checkpoint Z and one exact current source cylinder

    X = r + 2^h m,   m in [lo,hi],

use only the independent SAFE debit corridor

    75*2^33 < L_- < 112*2^33,
    L_- = 3X-Z.

Then m lies in an open real interval of width

    (37*2^33)/(3*2^h).

Hence the integer source-parameter fiber inside one current cylinder has
cardinality at most ceil(width), further capped by the cylinder's own count.
This is a deterministic per-Z upper bound. It is NOT same-orbit membership.
"""

from collections import Counter

import A0_s1_8jump_cumulative_pruned_frontier_export as frontier

G = 1 << 33
L_LO = 75 * G
L_HI = 112 * G
WIDTH = L_HI - L_LO
EXPECTED_STATES = 14_224
EXPECTED_POPULATION = 26_859_837_368_455_538_464


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def uniform_m_cap(h: int) -> int:
    assert h >= 0
    return ceil_div(WIDTH, 3 * (1 << h))


states = tuple(frontier.pruned_states)
assert len(states) == EXPECTED_STATES
assert sum(st.count for st in states) == EXPECTED_POPULATION

h_state_counts = Counter()
h_population = Counter()
h_cap = {}

per_z_total_cap = 0
singleton_states = 0
singleton_population = 0
le2_states = 0
le10_states = 0
le100_states = 0
le1000_states = 0

for st in states:
    cap = uniform_m_cap(st.h)
    effective = min(st.count, cap)
    per_z_total_cap += effective
    h_state_counts[st.h] += 1
    h_population[st.h] += st.count
    h_cap[st.h] = cap

    if effective <= 1:
        singleton_states += 1
        singleton_population += st.count
    if effective <= 2:
        le2_states += 1
    if effective <= 10:
        le10_states += 1
    if effective <= 100:
        le100_states += 1
    if effective <= 1000:
        le1000_states += 1

# Pure width threshold: h>=37 makes the open m-window shorter than 1.
assert uniform_m_cap(36) == 2
assert uniform_m_cap(37) == 1
assert all(uniform_m_cap(h) == 1 for h in range(37, 60))

reduction_factor_floor = EXPECTED_POPULATION // per_z_total_cap

print("PASS A0 s=1 jump8 checkpoint source-fiber profile certificate")
print("states", len(states))
print("population", EXPECTED_POPULATION)
print("debit_width", WIDTH)
print("singleton_width_threshold_h", 37)
print("per_single_Z_total_source_parameter_cap", per_z_total_cap)
print("population_to_perZ_cap_floor_ratio", reduction_factor_floor)
print("effective_cap_le_1_states", singleton_states)
print("population_in_effective_cap_le_1_states", singleton_population)
print("effective_cap_le_2_states", le2_states)
print("effective_cap_le_10_states", le10_states)
print("effective_cap_le_100_states", le100_states)
print("effective_cap_le_1000_states", le1000_states)
print("h  state_count  population  uniform_m_cap")
for h in sorted(h_state_counts):
    print(h, h_state_counts[h], h_population[h], h_cap[h])
print("classification", "EXACT deterministic source-fiber upper bound for one already-exposed ordinary Z")
print("rejected_inference", "small or singleton debit fiber does not imply T^t(X)=Z")
print("next_gate", "apply paired source-activation provenance criterion to candidates or construct a compressed late-activation exporter")
