#!/usr/bin/env python3
"""Finite regression for the exact target-displacement decomposition of S10 N.

The algebraic theorem is documented in

    ../theorems/TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md

This certificate imports the existing exact eight-jump P_min reconstruction.
After that module finishes, its ``states`` variable is the certified jump-8
frontier of 14,224 exact source cylinders.

For one representative ordinary integer from every source cylinder, this file
independently reconstructs the accelerated parity prefix, extracts ordered one
positions, and checks

    N = sum_j 3^(q-1-j) 2^a_j (2^(t_j-a_j)-1).

It also checks the exact valuation decoder

    v2(N) = earliest displaced actual one-position

whenever N>0.

The run is a finite implementation regression only.  It does not prove a
positive future defect or close Route-B.
"""

from __future__ import annotations

import A0_s1_14root_8jump_Pmin_recheck_certificate as pmin


TPOS = pmin.TPOS


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def accelerated_parity_prefix(n: int, h: int) -> tuple[int, ...]:
    """Return the first h parity bits of T(n)=n/2 or (3n+1)/2."""
    assert n > 0 and h >= 0
    bits = []
    z = n
    for _ in range(h):
        bit = z & 1
        bits.append(bit)
        if bit:
            z = (3 * z + 1) // 2
        else:
            z //= 2
        assert z > 0
    return tuple(bits)


def displacement_sum(actual: tuple[int, ...], target: tuple[int, ...]) -> int:
    assert len(actual) == len(target)
    q = len(actual)
    total = 0
    for j, (a, t) in enumerate(zip(actual, target)):
        assert a <= t
        s = t - a
        total += (3 ** (q - 1 - j)) * (1 << a) * ((1 << s) - 1)
    return total


def direct_correction(one_positions: tuple[int, ...]) -> int:
    q = len(one_positions)
    return sum(
        (3 ** (q - 1 - j)) * (1 << a)
        for j, a in enumerate(one_positions)
    )


states = pmin.states
assert len(states) == 14_224

zero_defect_cylinders = 0
positive_defect_cylinders = 0
population_zero_defect = 0
population_positive_defect = 0
max_displaced_ranks = 0

for st in states:
    # All members of an exact source cylinder share the first h parity bits;
    # X_lo is therefore a valid representative for the prefix language.
    bits = accelerated_parity_prefix(st.X_lo, st.h)
    actual = tuple(i for i, bit in enumerate(bits) if bit)
    assert len(actual) == st.q

    target = tuple(TPOS[:st.q])
    assert all(a <= t for a, t in zip(actual, target))

    Cw = direct_correction(actual)
    Ct = direct_correction(target)
    assert Ct - Cw == st.N

    N_disp = displacement_sum(actual, target)
    assert N_disp == st.N
    assert N_disp >= 0

    displaced = tuple(
        (j, a, t)
        for j, (a, t) in enumerate(zip(actual, target))
        if a < t
    )
    max_displaced_ranks = max(max_displaced_ranks, len(displaced))

    if st.N == 0:
        zero_defect_cylinders += 1
        population_zero_defect += st.count
        assert not displaced
        assert actual == target
    else:
        positive_defect_cylinders += 1
        population_positive_defect += st.count
        assert displaced
        earliest_actual_pos = displaced[0][1]
        assert v2(st.N) == earliest_actual_pos

assert zero_defect_cylinders + positive_defect_cylinders == len(states)
assert population_zero_defect + population_positive_defect == pmin.EXPECTED[8][1]

print("PASS A0 s=1 target-displacement defect decomposition certificate")
print("jump8_cylinders", len(states))
print("jump8_population", pmin.EXPECTED[8][1])
print("zero_defect_cylinders", zero_defect_cylinders)
print("positive_defect_cylinders", positive_defect_cylinders)
print("population_zero_defect", population_zero_defect)
print("population_positive_defect", population_positive_defect)
print("max_displaced_ranks_in_representative_prefix", max_displaced_ranks)
print("exact_N_equals_ordered_displacement_sum", True)
print("v2_N_decodes_earliest_displaced_actual_position", True)
print("future_forced_defect_claimed", False)
print("status", "EXACT identity; finite jump8 regression; no additive future floor")
