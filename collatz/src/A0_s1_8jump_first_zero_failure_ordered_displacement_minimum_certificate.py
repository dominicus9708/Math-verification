#!/usr/bin/env python3
"""Exact F_min at each jump-8 parent's first zero-path failure horizon.

The zero-path certificate gives, for every jump-8 parent, a first horizon r0
at which the unique target-exact future source path becomes empty.

At that horizon any legal descendant is represented by ordered future one
positions

    u_k = t_{q+k} - d_k,

with d_k >= 0 and at least one d_k > 0.

This certificate enumerates exact source-feasible displacement vectors by the
number c of nonzero d_k.  After classes 1..c have been exhausted, every path
with at least c+1 displaced ranks has a rigorous cost lower bound L_{c+1}.
Once the best feasible enumerated cost B satisfies B <= L_{c+1}, B is the
exact global F_min and higher displacement-count classes cannot improve it.

On the current 14,224 parents every minimum is certified after checking at
most six displacement-count classes.  No source payload merge is used.
"""

from itertools import combinations

import A0_s1_8jump_zero_future_defect_residue_exclusion_certificate as zero

pmin = zero.pmin
parents = zero.parents
first_failure = zero.first_failure

MAX_DISPLACEMENT_CLASSES = 6

EXPECTED_KIND_COUNT = {
    1: 13_354,
    2: 724,
    3: 124,
    4: 21,
    5: 1,
}

EXPECTED_KIND_POPULATION = {
    1: 26_113_797_990_685_568_961,
    2: 569_741_045_565_622_691,
    3: 174_459_941_749_512_347,
    4: 1_838_390_843_599_102,
    5: 776_085,
}


def path_with_displacements(parent, horizon: int, disp: dict[int, int]):
    """Consume one fixed ordered-displacement vector exactly on the source interval."""
    st = parent
    for k in range(horizon):
        target_pos = pmin.TPOS[st.q]
        d = disp.get(k, 0)
        assert d >= 0
        actual_pos = target_pos - d
        a = actual_pos - st.h
        if a < 0:
            return None
        st = pmin.valuation_child(st, a)
        if st is None:
            return None
    return st


def displacement_candidates(parent, horizon: int, count: int):
    """All strictly ordered displacement vectors with exactly count nonzero ranks.

    Returns (final_F_cost, ((rank, displacement), ...)) sorted by cost.
    The ordering bounds make the magnitude enumeration finite and exact.
    """
    targets = [pmin.TPOS[parent.q + k] for k in range(horizon)]
    out = []

    for ranks in combinations(range(horizon), count):
        def rec(j: int, shifts: list[int], cost: int):
            k = ranks[j]

            if j == 0:
                previous_actual = parent.h - 1 if k == 0 else targets[k - 1]
            else:
                prev_rank = ranks[j - 1]
                if k == prev_rank + 1:
                    previous_actual = targets[prev_rank] - shifts[-1]
                else:
                    # At least one unshifted target-exact rank lies between.
                    previous_actual = targets[k - 1]

            max_d = targets[k] - previous_actual - 1
            for d in range(1, max_d + 1):
                atom = (
                    (3 ** (horizon - 1 - k))
                    * ((1 << targets[k]) - (1 << (targets[k] - d)))
                )
                if j + 1 == count:
                    out.append((cost + atom, tuple(zip(ranks, shifts + [d]))))
                else:
                    rec(j + 1, shifts + [d], cost + atom)

        rec(0, [], 0)

    out.sort(key=lambda item: item[0])
    return out


def at_least_c_displacements_lower_bound(parent, horizon: int, count: int) -> int:
    """SAFE lower bound for every path having at least count displaced ranks."""
    assert count >= 1

    weights = [
        (3 ** (horizon - 1 - k))
        * (1 << (pmin.TPOS[parent.q + k] - 1))
        for k in range(horizon)
    ]

    first_allowed = []
    for k in range(horizon):
        target = pmin.TPOS[parent.q + k]
        previous = parent.h - 1 if k == 0 else pmin.TPOS[parent.q + k - 1]
        if target - 1 > previous:
            first_allowed.append(k)

    best = None
    for k in first_allowed:
        later = sorted(weights[j] for j in range(k + 1, horizon))
        if len(later) < count - 1:
            continue
        value = weights[k] + sum(later[:count - 1])
        if best is None or value < best:
            best = value

    assert best is not None
    return best


def exact_parent_minimum(parent, horizon: int):
    best = None
    best_count = None
    checked_classes = 0

    for count in range(1, MAX_DISPLACEMENT_CLASSES + 1):
        checked_classes = count
        class_best = None

        for cost, pattern in displacement_candidates(parent, horizon, count):
            # Candidates are sorted.  Once cost cannot improve the current
            # class best, remaining patterns of this class cannot either.
            if class_best is not None and cost >= class_best:
                break

            leaf = path_with_displacements(parent, horizon, dict(pattern))
            if leaf is not None:
                class_best = cost
                break

        if class_best is not None and (best is None or class_best < best):
            best = class_best
            best_count = count

        if best is not None:
            next_lower = at_least_c_displacements_lower_bound(
                parent, horizon, count + 1
            )
            if best <= next_lower:
                return best, best_count, checked_classes

    raise AssertionError("six displacement-count classes did not certify the minimum")


kind_count = {}
kind_population = {}
checked_histogram = {}
exact_rows = []
physical_closures = 0
ratio_floor = []

for i, parent in enumerate(parents):
    horizon = first_failure[i]
    assert horizon is not None

    # The zero path is present one horizon earlier and absent here.
    st = parent
    for _ in range(1, horizon):
        st = zero.zero_defect_child(st)
        assert st is not None
    assert st.count == 1
    assert zero.zero_defect_child(st) is None

    F_min, displaced_count, checked = exact_parent_minimum(parent, horizon)
    assert F_min > 0

    kind_count[displaced_count] = kind_count.get(displaced_count, 0) + 1
    kind_population[displaced_count] = (
        kind_population.get(displaced_count, 0) + parent.count
    )
    checked_histogram[checked] = checked_histogram.get(checked, 0) + 1

    if zero.physical_floor_closes_parent(parent, horizon, F_min):
        physical_closures += 1

    need = zero.required_future_defect(parent, horizon)
    assert need > F_min
    ratio_floor.append(need // F_min)

    exact_rows.append((horizon, F_min, displaced_count, checked))

assert kind_count == EXPECTED_KIND_COUNT
assert kind_population == EXPECTED_KIND_POPULATION
assert sum(kind_count.values()) == 14_224
assert sum(kind_population.values()) == 26_859_837_368_845_079_186
assert physical_closures == 0

# One parent has a five-displacement minimum and requires class six only as a
# proof that no >=6-displacement path can beat it.
assert max(row[3] for row in exact_rows) == 6
assert kind_count.get(6, 0) == 0

assert min(ratio_floor) == 145_742_202_315
assert max(ratio_floor) == 920_214_076_930

print("PASS A0 s=1 jump8 first-zero-failure ordered-displacement minimum certificate")
print("parents", len(parents))
print("minimum_path_displacement_count", EXPECTED_KIND_COUNT)
print("minimum_path_parent_population", EXPECTED_KIND_POPULATION)
print("checked_class_histogram", checked_histogram)
print("maximum_displacement_class_checked", max(row[3] for row in exact_rows))
print("whole_parent_physical_closures", physical_closures)
print("required_over_exact_Fmin_min", min(ratio_floor))
print("required_over_exact_Fmin_max", max(ratio_floor))
print("source_payload_merging_used", False)
print("status", "EXACT finite first-failure F_min on all 14,224 parents; cumulative post-failure floor remains OPEN")
