#!/usr/bin/env python3
"""Exact depth-28 root-globalized excursion/translation audit.

This certificate distinguishes two notions that must not be conflated:

1. local replacement of a later parity segment; and
2. replacement that is Hensel-compatible all the way back to the original
   start (root-globalized replacement).

Let a positive finite-return excursion first differ from the mechanical word at
position p, let q0 be the number of mechanical odd symbols before p, and let s
be the common number of odd symbols in the actual/mechanical segments through
the first return.  If dR is the difference of the two segment corrections, then
for ANY common suffix the full corrections differ by 3^q_suffix*dR.  Therefore
an integer same-endpoint replacement at the original start exists exactly when

    3^(q0+s) | dR,

and then the initial-start difference is dR / 3^(q0+s), independent of the
suffix.

Modulo 2^28 the canonical-residue translation is likewise suffix-independent:

    D == - dR * 3^(-(q0+s))  (mod 2^28)

(up to the fixed orientation convention used below).

The script exhausts EVERY positive first-return excursion contained in the
first 28 symbols of the current H19 mechanical phase.  It proves:

* there are 118,265 such nontrivial excursions;
* none satisfies the root-globalized Hensel divisibility condition;
* all 118,265 canonical translations are distinct;
* every translation has exact 2-adic valuation equal to the first-defect
  position p.

This is a local/root-globalization audit and a cocycle-structure theorem.  It is
not a Collatz proof and it does not say that every hard Hensel sibling is a
mechanical-segment normalization.
"""

from collections import defaultdict

H19 = "1101101101011011010"
L = 28
MECH = (H19 * 3)[:L]
MOD = 1 << L


def correction(positions):
    R = 0
    for x in positions:
        R = 3 * R + (1 << x)
    return R


def v3(n):
    assert n != 0
    n = abs(n)
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def v2(n):
    assert n != 0
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


# Each record is (p, ret, s, v3(dR), root_q, dR, translation).
records = []
by_p = defaultdict(int)
max_v3_by_p = defaultdict(lambda: -1)
min_deficit_by_p = defaultdict(lambda: 10**9)
translations = set()
root_hensel = []

for p, ch in enumerate(MECH):
    if ch != "0":
        continue

    q0 = MECH[:p].count("1")

    # First mismatch is necessarily mechanical 0 -> actual 1, hence h=1.
    # State: next position, current positive relative height, actual segment.
    stack = [(p + 1, 1, [1])]

    while stack:
        i, h, bits = stack.pop()
        if i >= L:
            continue

        mech_bit = int(MECH[i])
        for bit in (0, 1):
            h2 = h + bit - mech_bit
            if h2 < 0:
                continue

            bits2 = bits + [bit]

            if h2 == 0:
                # Because h was positive before this step, i is the first return.
                ret = i
                actual_positions = [
                    p + j for j, b in enumerate(bits2) if b
                ]
                mechanical_positions = [
                    x for x in range(p, ret + 1) if MECH[x] == "1"
                ]
                assert len(actual_positions) == len(mechanical_positions)
                s = len(actual_positions)

                R_actual = correction(actual_positions)
                R_mech = correction(mechanical_positions)
                dR = R_actual - R_mech
                assert dR != 0

                root_q = q0 + s
                val3 = v3(dR)
                deficit = root_q - val3

                # 3^root_q is odd, so its inverse exists modulo 2^L.
                inv3 = pow(3**root_q, -1, MOD)
                D = (-dR * inv3) % MOD
                assert D != 0

                records.append((p, ret, s, val3, root_q, dR, D))
                by_p[p] += 1
                max_v3_by_p[p] = max(max_v3_by_p[p], val3)
                min_deficit_by_p[p] = min(min_deficit_by_p[p], deficit)
                translations.add(D)

                if val3 >= root_q:
                    root_hensel.append((p, ret, dR, root_q))

                # The earliest changed parity bit is p.  The parity-vector
                # bijection therefore forces the canonical-residue difference
                # to have exact dyadic valuation p.
                assert v2(D) == p
                continue

            # Keep only strictly positive excursions until their first return.
            stack.append((i + 1, h2, bits2))


EXPECTED_BY_P = {
    2: 93_999,
    5: 18_698,
    8: 4_403,
    10: 889,
    13: 198,
    16: 56,
    18: 15,
    21: 5,
    24: 2,
}
EXPECTED_MAX_V3 = {
    2: 9,
    5: 9,
    8: 7,
    10: 5,
    13: 4,
    16: 3,
    18: 3,
    21: 3,
    24: 0,
}
EXPECTED_MIN_DEFICIT = {
    2: 2,
    5: 4,
    8: 6,
    10: 7,
    13: 9,
    16: 11,
    18: 12,
    21: 14,
    24: 17,
}

assert dict(by_p) == EXPECTED_BY_P
assert dict(max_v3_by_p) == EXPECTED_MAX_V3
assert dict(min_deficit_by_p) == EXPECTED_MIN_DEFICIT
assert len(records) == 118_265
assert root_hensel == []
assert len(translations) == len(records) == 118_265

print("depth28 root-globalized excursion translation: PASS")
print("mechanical", MECH)
print("total_positive_finite_return_excursions", len(records))
print("root_globalized_hensel_excursions", len(root_hensel))
print("distinct_normalization_translations", len(translations))
print("by_first_defect", dict(sorted(by_p.items())))
print("max_v3_dR_by_first_defect", dict(sorted(max_v3_by_p.items())))
print("minimum_root_divisibility_deficit", dict(sorted(min_deficit_by_p.items())))
print("all_translation_v2_equal_first_defect", True)
