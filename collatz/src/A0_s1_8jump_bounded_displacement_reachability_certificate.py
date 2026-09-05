#!/usr/bin/env python3
"""Exact bounded-displacement source reachability from the tightened jump-8 frontier.

Finite certified result:

* with zero displaced future ranks, the relaxed source+ballot reachability set
  is empty by horizon 41;
* with at most one displaced rank, it is empty by horizon 45;
* with at most two displaced ranks, it is empty by horizon 46.

Therefore every horizon-46 survivor has at least three displaced ranks.  Since
each displaced target rank contributes normalized defect >1/12, every such
survivor has future eta >1/4.  Composing that floor with the existing directed
physical score removes an additional exact upper source tail from the already
first-75-tightened frontier.

The reachability search intentionally omits later first-75/Hamming tightening
after its input frontier.  It is therefore a relaxed superset search; emptiness
of this larger class is safe for the stricter canonical class.

The resulting exact pruned source intervals are exported as `pruned_states`
for downstream S10 work.
"""

from fractions import Fraction
from functools import lru_cache

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail


defect = tail.defect

M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi

TIGHT_TOTAL = 26_859_837_368_588_270_254
NEW_PRUNED = 56_968_804
NEW_TOTAL = 26_859_837_368_531_301_450
AFFECTED_PARENTS = 6_728

EXPECTED_LATE = {
    0: {
        40: (1, 1, 1),
        41: (0, 0, 0),
    },
    1: {
        35: (4_110, 1_404, 4_110),
        36: (1_851, 829, 1_851),
        37: (533, 424, 533),
        38: (135, 131, 135),
        39: (60, 58, 60),
        40: (19, 19, 19),
        41: (10, 10, 10),
        42: (4, 4, 4),
        43: (1, 1, 1),
        44: (1, 1, 1),
        45: (0, 0, 0),
    },
    2: {
        35: (50_577, 2_944, 50_577),
        36: (22_204, 2_196, 22_204),
        37: (6_900, 1_630, 6_900),
        38: (1_922, 997, 1_922),
        39: (885, 603, 885),
        40: (275, 239, 275),
        41: (125, 122, 125),
        42: (48, 47, 48),
        43: (16, 16, 16),
        44: (7, 7, 7),
        45: (2, 2, 2),
        46: (0, 0, 0),
    },
}


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


@lru_cache(None)
def pow3(q: int) -> int:
    return 3 ** q


@lru_cache(None)
def inv3pow_mod_2e(q: int, e: int) -> int:
    M = 1 << e
    return pow(pow(3, q, M), -1, M)


# Lite state = (y, lo, hi, h, q).  r and the already-realized defect are not
# needed for reachability; the exact source parameter interval is retained.
def source_child(st, d: int):
    y, lo, hi, h, q = st
    target = defect.TPOS[q]
    assert target >= h
    assert 0 <= d <= target - h

    actual = target - d
    a = actual - h
    e = a + 1
    M = 1 << e
    A = pow3(q)

    rho = (((1 << a) - y) * inv3pow_mod_2e(q, e)) % M
    lo2 = ceil_div(lo - rho, M)
    hi2 = (hi - rho) // M
    if lo2 > hi2:
        return None

    y2 = (3 * (y + A * rho) + (1 << a)) // M
    return (y2, lo2, hi2, actual + 1, q + 1)


def count_state(st) -> int:
    return st[2] - st[1] + 1


def run_budget(cmax: int, max_horizon: int):
    active = [
        (i, (st.y, st.lo, st.hi, st.h, st.q), 0)
        for i, st in enumerate(tail.states)
    ]

    rows = {}
    for horizon in range(1, max_horizon + 1):
        nxt = []
        parent_ids = set()

        for parent_id, st, used in active:
            y, lo, hi, h, q = st
            target = defect.TPOS[q]
            max_d = target - h
            assert max_d >= 0

            for d in range(max_d + 1):
                used2 = used + (1 if d > 0 else 0)
                if used2 > cmax:
                    continue
                ch = source_child(st, d)
                if ch is None:
                    continue
                nxt.append((parent_id, ch, used2))
                parent_ids.add(parent_id)

        active = nxt
        rows[horizon] = (
            len(active),
            len(parent_ids),
            sum(count_state(st) for _, st, _ in active),
        )

        if not active:
            break

    return rows


assert len(tail.states) == 14_224
assert sum(st.count for st in tail.states) == TIGHT_TOTAL

rows0 = run_budget(0, 41)
rows1 = run_budget(1, 45)
rows2 = run_budget(2, 46)

for cmax, rows in ((0, rows0), (1, rows1), (2, rows2)):
    for horizon, expected in EXPECTED_LATE[cmax].items():
        assert rows[horizon] == expected

assert rows0[41] == (0, 0, 0)
assert rows1[45] == (0, 0, 0)
assert rows2[46] == (0, 0, 0)

# Mechanical target atom theorem regression over every rank touched by this
# finite execution.  The theorem itself is algebraic and documented upstream.
max_q = max(st.q for st in tail.states) + 46
for rank in range(2, max_q + 1):
    t = defect.TPOS[rank - 1]
    atom = Fraction(1 << (t - 1), 3 ** rank)
    assert atom > Fraction(1, 12)

ETA_FLOOR = Fraction(1, 4)


def count_gt_cut(st, cut: Fraction) -> int:
    z = (cut - st.r) / (1 << st.h)
    floorz = z.numerator // z.denominator
    lo2 = max(st.lo, floorz + 1)
    return max(0, st.hi - lo2 + 1)


def retained_hi(st, cut: Fraction) -> int:
    z = (cut - st.r) / (1 << st.h)
    floorz = z.numerator // z.denominator
    return min(st.hi, floorz)


pruned = 0
affected = 0
whole = 0
pruned_states = []

for st in tail.states:
    cut = (
        Fraction(BARRIER, 1) - M_LO * (st.eta + ETA_FLOOR)
    ) / DELTA_LO
    n = count_gt_cut(st, cut)
    hi2 = retained_hi(st, cut)

    pruned += n
    affected += (n > 0)
    whole += (n == st.count)

    if hi2 >= st.lo:
        pruned_states.append(tail.State(
            st.r, st.y, st.lo, hi2, st.h, st.S,
            st.D, st.eta, st.root_f,
        ))

assert pruned == NEW_PRUNED
assert affected == AFFECTED_PARENTS
assert whole == 0
assert len(pruned_states) == 14_224
assert sum(st.count for st in pruned_states) == NEW_TOTAL
assert TIGHT_TOTAL - pruned == NEW_TOTAL

print("PASS A0 s=1 jump8 bounded-displacement reachability certificate")
print("c0_last_nonempty_horizon", 40)
print("c1_last_nonempty_horizon", 44)
print("c2_last_nonempty_horizon", 45)
print("horizon46_minimum_displaced_ranks", 3)
print("horizon46_normalized_future_eta_floor", "> 1/4")
print("incremental_pruned_after_first75_tightening", NEW_PRUNED)
print("affected_parent_intervals", AFFECTED_PARENTS)
print("whole_parent_intervals_removed", whole)
print("new_tightened_population", NEW_TOTAL)
print("exported_pruned_states", len(pruned_states))
print("source_payload_merging_used", False)
print("later_first75_constraints_used_in_reachability", False)
print("status", "EXACT finite relaxed-reachability emptiness + exact incremental source-tail pruning")
