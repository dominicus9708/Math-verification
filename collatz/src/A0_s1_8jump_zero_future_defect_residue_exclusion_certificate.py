#!/usr/bin/env python3
"""Exact zero-future-defect residue exclusion from the certified jump-8 frontier.

For a current source state, zero new defect at the next odd event requires the
one to occur exactly at the next target one-position.  Therefore there is one
unique zero-defect valuation child.  Iterating it gives one unique formal
zero-defect path for each future odd-event horizon.

This certificate follows only that one path for each of the 14,224 jump-8
parents.  It does not expand positive-defect branches.

Finite result:
  * every parent keeps the zero path through horizon 11;
  * exclusions begin at horizon 12;
  * one parent remains at horizon 40;
  * no parent retains a zero-defect path at horizon 41.

After zero-path exclusion, any surviving horizon-r descendant has a universal
positive future-defect floor

    L_r(q) = min_k 3^(r-1-k) * 2^(t_{q+k}-1).

The certificate also checks that this one-displacement floor gives zero
whole-parent physical closures through horizon 41.  This is a finite negative
yield result, not a universal statement about stronger future-defect floors.
"""

import A0_s1_14root_8jump_Pmin_recheck_certificate as pmin

MAX_HORIZON = 41

# (horizon, zero_path_parent_count, zero_path_parameter_population)
EXPECTED = (
    (1, 14224, 3162093986439253934),
    (2, 14224, 793029065643633546),
    (3, 14224, 395261748304906768),
    (4, 14224, 98815437076226672),
    (5, 14224, 48799343997602275),
    (6, 14224, 12351929634528362),
    (7, 14224, 5594463474190244),
    (8, 14224, 1543991204316179),
    (9, 14224, 386002134744688),
    (10, 14224, 190630657796293),
    (11, 14224, 48249725134872),
    (12, 14051, 21858507532707),
    (13, 13298, 6031215641942),
    (14, 12510, 1512582904179),
    (15, 12153, 753901955192),
    (16, 11562, 188475488775),
    (17, 11260, 93077361979),
    (18, 10399, 23559436094),
    (19, 9471, 10670592331),
    (20, 8951, 2944929533),
    (21, 8142, 736240617),
    (22, 7800, 363599087),
    (23, 7278, 92029012),
    (24, 6994, 41691772),
    (25, 6177, 11503583),
    (26, 5396, 2885020),
    (27, 5018, 1437954),
    (28, 4450, 359469),
    (29, 4153, 177519),
    (30, 3278, 44938),
    (31, 2367, 20359),
    (32, 1848, 5614),
    (33, 1027, 1388),
    (34, 657, 657),
    (35, 153, 153),
    (36, 69, 69),
    (37, 18, 18),
    (38, 6, 6),
    (39, 3, 3),
    (40, 1, 1),
    (41, 0, 0),
)

# Exact first horizon at which each parent loses the target-exact path.
EXPECTED_FIRST_FAILURE_COUNTS = {
    12: 173,
    13: 753,
    14: 788,
    15: 357,
    16: 591,
    17: 302,
    18: 861,
    19: 928,
    20: 520,
    21: 809,
    22: 342,
    23: 522,
    24: 284,
    25: 817,
    26: 781,
    27: 378,
    28: 568,
    29: 297,
    30: 875,
    31: 911,
    32: 519,
    33: 821,
    34: 370,
    35: 504,
    36: 84,
    37: 51,
    38: 12,
    39: 3,
    40: 2,
    41: 1,
}


def zero_defect_child(st):
    """Unique next child with new atom Delta=0, or None if its source residue is empty."""
    target_pos = pmin.TPOS[st.q]
    a = target_pos - st.h
    assert a >= 0

    child = pmin.valuation_child(st, a)
    if child is not None:
        assert child.N == 3 * st.N
        assert child.h - 1 == target_pos
    return child


def minimum_positive_future_atom_floor(q: int, horizon: int) -> int:
    """Universal F_horizon floor conditional on at least one displacement."""
    vals = []
    for k in range(horizon):
        target_pos = pmin.TPOS[q + k]
        assert target_pos >= 1
        vals.append(
            (3 ** (horizon - 1 - k)) * (1 << (target_pos - 1))
        )
    return min(vals)


def physical_floor_closes_parent(parent, horizon: int, future_floor: int) -> bool:
    """Safe common physical lower bound for all legal horizon descendants."""
    descendant_N_floor = (3 ** horizon) * parent.N + future_floor
    descendant_q = parent.q + horizon

    score_floor = (
        pmin.M_LO * descendant_N_floor
        + pmin.DELTA_LO * (3 ** descendant_q) * parent.X_lo
    )
    return score_floor > pmin.BARRIER * (3 ** descendant_q)


def required_future_defect(parent, horizon: int) -> int:
    """Smallest extra F that would make the parent-level physical floor strict."""
    descendant_q = parent.q + horizon
    base = (
        pmin.M_LO * ((3 ** horizon) * parent.N)
        + pmin.DELTA_LO * (3 ** descendant_q) * parent.X_lo
    )
    rhs = pmin.BARRIER * (3 ** descendant_q)
    if base > rhs:
        return 0
    return (rhs - base) // pmin.M_LO + 1


parents = list(pmin.states)
assert len(parents) == 14_224
assert sum(st.count for st in parents) == 26_859_837_368_845_079_186

zero_states = list(parents)
first_failure = [None] * len(parents)
rows = []

for horizon in range(1, MAX_HORIZON + 1):
    next_zero_states = []
    for i, st in enumerate(zero_states):
        if st is None:
            next_zero_states.append(None)
            continue
        child = zero_defect_child(st)
        if child is None and first_failure[i] is None:
            first_failure[i] = horizon
        next_zero_states.append(child)
    zero_states = next_zero_states

    zero_parent_count = sum(st is not None for st in zero_states)
    zero_parameter_population = sum(
        st.count for st in zero_states if st is not None
    )

    expected = EXPECTED[horizon - 1]
    assert expected == (
        horizon,
        zero_parent_count,
        zero_parameter_population,
    )

    excluded = [
        (parent, zero)
        for parent, zero in zip(parents, zero_states)
        if zero is None
    ]

    # Conditional on any legal horizon survivor existing, an excluded parent
    # must have positive new defect.  Test the universal one-displacement floor
    # against the directed physical parent gate.
    physical_floor_closures = 0
    for parent, _ in excluded:
        L = minimum_positive_future_atom_floor(parent.q, horizon)
        if physical_floor_closes_parent(parent, horizon, L):
            physical_floor_closures += 1

    # Exact finite negative-yield finding through horizon 41.
    assert physical_floor_closures == 0

    rows.append((
        horizon,
        zero_parent_count,
        zero_parameter_population,
        len(excluded),
        physical_floor_closures,
    ))

# Every current jump-8 parent loses the target-exact path by horizon 41.
assert all(x is not None for x in first_failure)
assert all(x is None for x in zero_states)

failure_counts = {}
for h in first_failure:
    failure_counts[h] = failure_counts.get(h, 0) + 1
assert failure_counts == EXPECTED_FIRST_FAILURE_COUNTS

# At horizon 41 the weak one-displacement floor is not merely below the
# physical threshold; it is about 10^12 below the required extra future defect
# for every parent.  Keep the exact integer quotient range as an audit signal.
ratios = []
for parent in parents:
    L = minimum_positive_future_atom_floor(parent.q, 41)
    need = required_future_defect(parent, 41)
    assert need > L
    ratios.append(need // L)

assert min(ratios) == 1_049_362_201_040
assert max(ratios) == 1_049_364_901_399
assert min(ratios) > 10 ** 12

print("PASS A0 s=1 jump8 zero-future-defect residue-exclusion certificate")
for row in rows:
    print(
        "horizon", row[0],
        "zero_path_parents", row[1],
        "zero_path_parameter_population", row[2],
        "zero_path_excluded_parents", row[3],
        "whole_parent_closures_from_one_displacement_floor", row[4],
    )
print("first_failure_counts", EXPECTED_FIRST_FAILURE_COUNTS)
print("horizon41_zero_path_parents", 0)
print("horizon41_zero_path_excluded_parents", 14_224)
print("horizon41_required_over_weak_floor_min", min(ratios))
print("horizon41_required_over_weak_floor_max", max(ratios))
print("source_payload_merging_used", False)
print("positive_defect_branch_expansion_used", False)
print("status", "EXACT finite zero-path execution; stronger cumulative future-defect floor remains OPEN")
