#!/usr/bin/env python3
"""Exact jump-8 partition by global future reachability of the directed P_min gate.

The theorem is documented in

    ../theorems/PMIN_GLOBAL_FUTURE_REACHABILITY_CUTOFF.md

For each first-75-tightened jump-8 source cylinder this certificate computes a
source-value cutoff X_noP below which even the largest possible remaining
target-correction defect cannot ever make the directed physical P_min
inequality fire.

This is a predicate-availability partition, not Collatz closure.
"""

from fractions import Fraction

import A0_s1_14root_8jump_tail_defect_tightening_certificate as tail
import A0_s1_14root_8jump_Pmin_recheck_certificate as pmin


defect = tail.defect

M_LO = defect.mW_lo
DELTA_LO = defect.delta_lo
BARRIER = defect.L_MAX * defect.QFP + defect.cW_hi
J0 = 65_868_186_701

TOTAL_TARGET_UPPER = Fraction(defect.cW_hi, defect.mW_lo)

TAIL_TOTAL = 26_859_837_368_588_270_254
PURE_TOTAL = 26_859_837_368_845_079_186
NO_P_EXPECTED = 22_050_571_214_544_220_515
P_REACH_TAIL_EXPECTED = 4_809_266_154_044_049_739
P_REACH_PURE_EXPECTED = 4_809_266_154_300_858_671
TAIL_EXTRA = 256_808_932


def target_prefix_sum(q: int) -> Fraction:
    return sum(
        Fraction(1 << defect.TPOS[r - 1], 3 ** r)
        for r in range(1, q + 1)
    )


def future_target_cap(q: int) -> Fraction:
    assert 0 <= q <= J0
    return TOTAL_TARGET_UPPER - target_prefix_sum(q)


def no_p_cutoff(q: int, eta: Fraction) -> Fraction:
    cap = future_target_cap(q)
    return Fraction(BARRIER, 1) - M_LO * (eta + cap)


def cutoff_x(q: int, eta: Fraction) -> Fraction:
    return no_p_cutoff(q, eta) / DELTA_LO


def count_le_cut(r: int, h: int, lo: int, hi: int, cut: Fraction) -> int:
    z = (cut - r) / (1 << h)
    mmax = z.numerator // z.denominator
    hi2 = min(hi, mmax)
    return max(0, hi2 - lo + 1)


def count_gt_cut(r: int, h: int, lo: int, hi: int, cut: Fraction) -> int:
    z = (cut - r) / (1 << h)
    floorz = z.numerator // z.denominator
    lo2 = max(lo, floorz + 1)
    return max(0, hi - lo2 + 1)


def x_lo(st) -> int:
    return st.r + (1 << st.h) * st.lo


def x_hi(st) -> int:
    return st.r + (1 << st.h) * st.hi


# ---------------------------------------------------------------------------
# 1. First-75-tightened canonical frontier partition.
# ---------------------------------------------------------------------------

states = list(tail.states)
assert len(states) == 14_224
assert sum(st.count for st in states) == TAIL_TOTAL

no_p_total = 0
p_reach_total = 0
current_p_rejected = 0
whole_no_p = 0
whole_p_reach = 0
cut_floors = []

for st in states:
    q = st.q
    eta = st.eta
    cap = future_target_cap(q)
    assert cap > 0

    cut = cutoff_x(q, eta)
    nlo = count_le_cut(st.r, st.h, st.lo, st.hi, cut)
    nhi = st.count - nlo
    assert nlo >= 0 and nhi >= 0

    no_p_total += nlo
    p_reach_total += nhi
    cut_floors.append(cut.numerator // cut.denominator)

    if x_hi(st) <= cut:
        whole_no_p += 1
    if x_lo(st) > cut:
        whole_p_reach += 1

    # The already-realized exact defect alone is weaker than the first-75
    # tightening on the canonical tightened frontier: no additional upper-tail
    # integer survives tail tightening while already satisfying the current
    # strict P rejection inequality.
    current_cut = (
        Fraction(BARRIER, 1) - M_LO * eta
    ) / DELTA_LO
    current_p_rejected += count_gt_cut(
        st.r, st.h, st.lo, st.hi, current_cut
    )

assert no_p_total == NO_P_EXPECTED
assert p_reach_total == P_REACH_TAIL_EXPECTED
assert no_p_total + p_reach_total == TAIL_TOTAL
assert current_p_rejected == 0
assert whole_no_p == 0
assert whole_p_reach == 0


# ---------------------------------------------------------------------------
# 2. Non-independence audit against the untightened pure-ballot frontier.
# ---------------------------------------------------------------------------

pure_no_p = 0
pure_p_reach = 0
for st in pmin.states:
    eta = Fraction(st.N, 3 ** st.q)
    cut = cutoff_x(st.q, eta)
    nlo = count_le_cut(st.r, st.h, st.lo, st.hi, cut)
    pure_no_p += nlo
    pure_p_reach += st.count - nlo

assert pure_no_p == NO_P_EXPECTED
assert pure_p_reach == P_REACH_PURE_EXPECTED
assert pure_no_p + pure_p_reach == PURE_TOTAL

# The first-75 tail tightening removes population only from the P-reachable
# upper region; the permanently no-P lower region is unchanged.
assert pure_p_reach - p_reach_total == TAIL_EXTRA
assert PURE_TOTAL - TAIL_TOTAL == TAIL_EXTRA

print("PASS A0 s=1 jump8 global future P_min reachability-cutoff certificate")
print("tightened_jump8_total", TAIL_TOTAL)
print("permanently_no_P_population", no_p_total)
print("future_P_reachable_population", p_reach_total)
print("no_P_fraction", f"{no_p_total / TAIL_TOTAL:.12f}")
print("P_reachable_fraction", f"{p_reach_total / TAIL_TOTAL:.12f}")
print("current_exact_P_additional_pruning_after_tail_tightening", current_p_rejected)
print("whole_cylinders_entirely_no_P", whole_no_p)
print("whole_cylinders_entirely_P_reachable", whole_p_reach)
print("first75_removed_from_P_reachable_region", pure_p_reach - p_reach_total)
print("cutoff_floor_min", min(cut_floors))
print("cutoff_floor_max", max(cut_floors))
print("status", "EXACT predicate-availability partition; no Collatz closure inferred")
