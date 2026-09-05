#!/usr/bin/env python3
"""Certificate for pure-ballot macroblock non-contraction.

The algebraic theorem says that a legal depth-d valuation tuple

    (a1,...,ad)

is exactly the macroblock

    0^a1 1 ... 0^ad 1,

and the existing valuation-macroblock theorem maps that block to the same
child source channel as sequential valuation refinement.

This file audits the current eight-jump control frontier and quantifies the
execution-only saving of compiling four future valuation jumps at once.
It does NOT merge source payloads and does NOT claim that every control leaf
has a nonempty source interval.
"""

from collections import Counter, defaultdict
from functools import lru_cache

import A0_s1_source_payload_control_factorization_certificate as factor
import A0_s1_valuation_jump_ballot_control_certificate as ballot

FIRST = (2, 5, 8, 10, 13, 16, 18, 21, 24, 27, 29, 32, 35, 37)
HORIZON = 4


def transitions(h: int, S: int):
    out = []
    for a in range(256 - h - 1):
        ok, S2 = ballot.jump_ballot(h, S, a)
        if not ok:
            break
        out.append((a, h + a + 1, S2))
    return tuple(out)


# Rebuild the control-path multiplicity from the 14 exact root controls.
# This contains no source merge: multiplicity counts distinct source/control
# paths that happen to land on the same (h,S) control state.
mult = Counter((f + 1, 1) for f in FIRST)
for _ in range(8):
    nxt = Counter()
    for (h, S), count in mult.items():
        for _a, h2, S2 in transitions(h, S):
            nxt[(h2, S2)] += count
    mult = nxt

assert sum(mult.values()) == 14_224
assert len(mult) == 90
assert {(st.h, st.S) for st in factor.states} == set(mult)


@lru_cache(None)
def signature(h: int, S: int, depth: int):
    if depth == 0:
        return ()
    return tuple(
        (a, signature(h2, S2, depth - 1))
        for a, h2, S2 in transitions(h, S)
    )


def leaf_blocks(h: int, S: int, depth: int):
    """All legal control macroblocks, encoded as tuples of parity bits."""
    if depth == 0:
        return ((),)
    out = []
    for a, h2, S2 in transitions(h, S):
        prefix = (0,) * a + (1,)
        for tail in leaf_blocks(h2, S2, depth - 1):
            out.append(prefix + tail)
    return tuple(out)


def is_prefix(a, b):
    return len(a) <= len(b) and b[:len(a)] == a


# Every depth-four leaf ends at the fourth one.  Audit prefix-freeness on all
# 90 current controls and count the 13 reusable control signatures.
signature_groups = defaultdict(lambda: [0, set()])
for (h, S), multiplicity in mult.items():
    blocks = leaf_blocks(h, S, HORIZON)
    assert all(sum(B) == HORIZON and B[-1] == 1 for B in blocks)
    assert len(blocks) == len(set(blocks))
    for i, A in enumerate(blocks):
        for B in blocks[i + 1:]:
            assert not is_prefix(A, B)
            assert not is_prefix(B, A)

    sig = signature(h, S, HORIZON)
    signature_groups[sig][0] += multiplicity
    signature_groups[sig][1].add((h, S))

assert len(signature_groups) == 13


# Control-path attempts after the current eight-jump frontier.  These are
# control-language counts before checking whether a particular source interval
# is empty.  Direct and sequential implementations face the same emptiness
# test at the same terminal parity leaf, so this is sufficient for the
# representation/non-contraction statement.
level_mult = mult.copy()
control_attempts = []
for depth in range(1, HORIZON + 1):
    nxt = Counter()
    for (h, S), count in level_mult.items():
        for _a, h2, S2 in transitions(h, S):
            nxt[(h2, S2)] += count
    level_mult = nxt
    control_attempts.append(sum(level_mult.values()))

assert control_attempts == [34_318, 93_000, 209_784, 609_808]

sequential_child_attempts = sum(control_attempts)
direct_macro_leaf_attempts = control_attempts[-1]
skipped_intermediate_attempts = sequential_child_attempts - direct_macro_leaf_attempts
assert sequential_child_attempts == 946_910
assert skipped_intermediate_attempts == 337_102

# Signature-level leaf accounting independently reconstructs the same terminal
# control leaf count.
signature_rows = []
weighted_leaves = 0
for sig, (parent_paths, controls) in signature_groups.items():
    representative = next(iter(controls))
    leaves = len(leaf_blocks(*representative, HORIZON))
    # Equal signatures must have equal leaf languages after erasing absolute
    # child control labels exactly as encoded by the signature recursion.
    for h, S in controls:
        assert len(leaf_blocks(h, S, HORIZON)) == leaves
    weighted_leaves += parent_paths * leaves
    signature_rows.append((parent_paths, len(controls), leaves))

assert weighted_leaves == direct_macro_leaf_attempts

EXPECTED_ROWS = [
    (4, 4, 434),
    (10, 10, 448),
    (32, 4, 280),
    (80, 10, 292),
    (140, 4, 170),
    (354, 10, 180),
    (420, 4, 95),
    (918, 4, 47),
    (1114, 10, 103),
    (1416, 4, 19),
    (2642, 10, 53),
    (2758, 6, 7),
    (4336, 10, 23),
]
assert sorted(signature_rows) == EXPECTED_ROWS

saving_fraction = skipped_intermediate_attempts / sequential_child_attempts

print("PASS A0 s=1 pure-ballot macroblock non-contraction certificate")
print("eight_jump_control_paths", sum(mult.values()))
print("eight_jump_controls_hS", len(mult))
print("horizon4_signature_classes", len(signature_groups))
for i, n in enumerate(control_attempts, 9):
    print("control_jump_depth", i, "leaf_attempts", n)
print("sequential_child_attempts", sequential_child_attempts)
print("direct_four_jump_macro_leaf_attempts", direct_macro_leaf_attempts)
print("skipped_intermediate_attempts", skipped_intermediate_attempts)
print("execution_attempt_saving_fraction", saving_fraction)
print("source_payloads_merged", False)
print("new_membership_pruning_claimed", False)
print(
    "status",
    "EXACT representation non-contraction; 4-jump control counts are finite current-frontier calculation",
)
