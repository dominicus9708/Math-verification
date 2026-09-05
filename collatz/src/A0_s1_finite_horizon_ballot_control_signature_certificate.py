#!/usr/bin/env python3
"""Finite-horizon pure-ballot control signatures on the eight-jump frontier.

This certificate imports the source-preserving eight-jump states and quotients
ONLY the pure-ballot control factor (h,S).  Source payloads are never merged.
"""

from functools import lru_cache

import A0_s1_source_payload_control_factorization_certificate as factor
import A0_s1_valuation_jump_ballot_control_certificate as ballot


controls = {(st.h, st.S) for st in factor.states}
assert len(factor.states) == 14_224
assert len(controls) == 90


def transitions(h: int, S: int):
    out = []
    for a in range(256 - h):
        ok, S2 = ballot.jump_ballot(h, S, a)
        if not ok:
            break
        out.append((a, h + a + 1, S2))
    return tuple(out)


@lru_cache(None)
def signature(h: int, S: int, depth: int):
    if depth == 0:
        return ()
    return tuple(
        (a, signature(h2, S2, depth - 1))
        for a, h2, S2 in transitions(h, S)
    )


EXPECTED_CLASSES = {
    1: 7,
    2: 13,
    3: 13,
    4: 13,
    5: 20,
    6: 20,
    7: 26,
    8: 26,
    9: 32,
    10: 39,
    11: 39,
    12: 45,
}

for depth, expected in EXPECTED_CLASSES.items():
    got = len({signature(h, S, depth) for h, S in controls})
    assert got == expected

# Horizon-four payload accounting.  This is not a payload merge; it only
# audits how many existing source cylinders share each reusable control
# skeleton.
groups = {}
for st in factor.states:
    sig = signature(st.h, st.S, 4)
    if sig not in groups:
        groups[sig] = [0, 0, set()]
    groups[sig][0] += 1
    groups[sig][1] += st.count
    groups[sig][2].add((st.h, st.S))

assert len(groups) == 13

class_cardinality = sorted(
    (cylinders, population, len(control_set))
    for cylinders, population, control_set in groups.values()
)

EXPECTED_CARDINALITY = [
    (4,    1_673_142_835_555_350,       4),
    (10,   486_891_075_430_069_447,    10),
    (32,   6_692_571_342_221_396,       4),
    (80,   1_947_564_301_720_277_786,  10),
    (140,  14_639_999_811_109_307,      4),
    (354,  4_261_970_052_848_663_745,  10),
    (420,  21_959_999_716_663_937,      4),
    (918,  25_192_355_428_155_130,      4),
    (1114, 6_433_110_507_326_336_176,  10),
    (1416, 19_702_355_498_989_126,      4),
    (2642, 7_416_617_394_025_436_249,  10),
    (2758, 398_192_532_939_200_813,     6),
    (4336, 5_825_631_079_922_400_724,  10),
]
assert class_cardinality == EXPECTED_CARDINALITY
assert sum(x[0] for x in class_cardinality) == 14_224
assert sum(x[1] for x in class_cardinality) == 26_859_837_368_845_079_186

print("PASS A0 s=1 finite-horizon ballot-control signature certificate")
print("eight_jump_source_cylinders", len(factor.states))
print("exact_control_states_hS", len(controls))
for depth in sorted(EXPECTED_CLASSES):
    print("horizon", depth, "signature_classes", EXPECTED_CLASSES[depth])
print("horizon4_classes", len(groups))
print("source_payloads_merged", False)
print("use", "share pure-ballot transition skeleton only")
print("status", "EXACT finite-horizon control quotient; full future-equivalence remains OPEN")
