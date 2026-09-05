#!/usr/bin/env python3
"""Finite-horizon source/ballot quotient audit at the 8-jump frontier.

There are two nested finite-horizon quotients in this file.

(1) FULL TRANSITION TEMPLATE.
For a source channel

    Y = y + A m,   A=3^q odd,

and d future raw parameter bits, the certified source quotient

    Q_d = (y mod 2^d, A mod 2^d)

determines the emitted d-bit parity block for every parameter residue
m mod 2^d.

At absolute depth h with pure-ballot surplus S, the legality of every d-bit
parity block depends only on

    B_d(h,S) = (S, Delta_1,...,Delta_d),

where Delta_i=Q(h+i)-Q(h+i-1).  Therefore

    P_d=(B_d,Q_d)

is an exact d-horizon transition template.

(2) PREDICATE-RELATIVE ACCEPTANCE SIGNATURE.
For the pure-ballot predicate alone, preserving the entire emitted parity map
is stronger than necessary.  Define recursively the low-parameter-bit decision
tree whose two edges are the next parameter bit e=0,1; a branch is marked
REJECT as soon as pure-ballot fails, and otherwise recursion continues.  Two
states with the same tree have exactly the same accepted parameter residues
through depth d, even if rejected paths emit different parity words.

This second quotient is strictly predicate-relative and can therefore be
coarser than P_d.  The current 8-jump frontier nevertheless becomes completely
separated by d=18 even under this coarser pure-ballot-only signature.

Neither quotient merges the exact source interval/residue payload.  Both are
finite-horizon computation quotients, not horizon-independent source-family
right congruences.
"""

from collections import defaultdict, Counter
from functools import lru_cache

import A0_s1_14root_8jump_ballot_pruning_certificate as eight
import A0_s1_valuation_jump_ballot_control_certificate as ballot


MAX_D = 18
MASK_REGRESSION_D = 6
PREDICATE_DEPTHS = (4, 8, 12, 16, 18)


def ballot_signature(h: int, S: int, d: int):
    return (
        S,
        tuple(
            ballot.Q[h + i] - ballot.Q[h + i - 1]
            for i in range(1, d + 1)
        ),
    )


def product_key(st, d: int):
    mod = 1 << d
    return (
        ballot_signature(st.h, st.S, d),
        st.y % mod,
        st.A % mod,
    )


def survives_low_residue(st, residue: int, d: int) -> bool:
    """Exact first-d-bit simulation; higher parameter bits are irrelevant."""
    y = st.y
    A = st.A
    h = st.h
    q_used = ballot.Q[h] + st.S
    m = residue

    for _ in range(d):
        e = m & 1
        value = y + A * e
        bit = value & 1

        if bit:
            y = (3 * value + 1) // 2
            A *= 3
            q_used += 1
        else:
            y = value // 2

        h += 1
        if q_used < ballot.Q[h]:
            return False
        m >>= 1

    return True


def accepted_mask(st, d: int):
    mask = 0
    for residue in range(1 << d):
        if survives_low_residue(st, residue, d):
            mask |= 1 << residue
    return mask


def predicate_signature_ids(states, d: int):
    """Intern exact pure-ballot accept/reject decision trees of depth d."""
    intern = {}
    next_id = [1]  # 0 = accepted horizon leaf; -1 = rejected branch

    @lru_cache(None)
    def rec(remaining: int, Y: int, A: int, h: int, S: int):
        if remaining == 0:
            return 0

        mod = 1 << remaining
        Y %= mod
        A %= mod
        threshold_increment = ballot.Q[h + 1] - ballot.Q[h]
        children = []

        for e in (0, 1):
            value = (Y + A * e) % mod
            bit = value & 1
            S2 = S + bit - threshold_increment

            if S2 < 0:
                children.append(-1)
                continue

            if bit:
                numer = (3 * value + 1) % mod
                A_full = (3 * A) % mod
            else:
                numer = value
                A_full = A

            assert numer % 2 == 0
            if remaining == 1:
                Y2 = A2 = 0
            else:
                mod2 = 1 << (remaining - 1)
                Y2 = (numer // 2) % mod2
                A2 = A_full % mod2

            children.append(rec(remaining - 1, Y2, A2, h + 1, S2))

        pair = tuple(children)
        if pair not in intern:
            intern[pair] = next_id[0]
            next_id[0] += 1
        return intern[pair]

    ids = []
    mod = 1 << d
    for st in states:
        ids.append(rec(d, st.y % mod, st.A % mod, st.h, st.S))

    return tuple(ids), rec.cache_info().currsize, len(intern)


states = tuple(eight.states)
assert len(states) == 14_224

EXPECTED_DISTINCT = {
    1: 18,
    2: 88,
    3: 203,
    4: 583,
    5: 1_964,
    6: 3_453,
    7: 5_715,
    8: 8_372,
    9: 10_888,
    10: 12_582,
    11: 13_443,
    12: 13_923,
    13: 14_102,
    14: 14_148,
    15: 14_178,
    16: 14_209,
    17: 14_213,
    18: 14_224,
}

EXPECTED_PREDICATE_DISTINCT = {
    4: 169,
    8: 7_612,
    12: 13_786,
    16: 14_207,
    18: 14_224,
}

rows = []
for d in range(1, MAX_D + 1):
    groups = defaultdict(list)
    for i, st in enumerate(states):
        groups[product_key(st, d)].append(i)

    distinct = len(groups)
    assert distinct == EXPECTED_DISTINCT[d]
    max_group = max(len(v) for v in groups.values())
    saved = len(states) - distinct
    rows.append((d, distinct, saved, max_group))


# Independent direct low-residue regression for the full-template claim.
mask_checks = 0
shared_group_checks = 0
for d in range(1, MASK_REGRESSION_D + 1):
    groups = defaultdict(list)
    for i, st in enumerate(states):
        groups[product_key(st, d)].append(i)

    for members in groups.values():
        rep_mask = accepted_mask(states[members[0]], d)
        mask_checks += 1
        if len(members) > 1:
            shared_group_checks += 1
            for i in members[1:]:
                assert accepted_mask(states[i], d) == rep_mask
                mask_checks += 1


# Predicate-relative quotient: forget rejected-path parity details and keep only
# the exact parameter-bit accept/reject decision tree.
predicate_rows = []
for d in PREDICATE_DEPTHS:
    ids, memo_states, interned_nodes = predicate_signature_ids(states, d)
    counts = Counter(ids)
    distinct = len(counts)
    assert distinct == EXPECTED_PREDICATE_DISTINCT[d]
    predicate_rows.append(
        (d, distinct, len(states) - distinct, max(counts.values()), memo_states, interned_nodes)
    )


assert rows[3] == (4, 583, 13_641, 84)
assert rows[7] == (8, 8_372, 5_852, 7)
assert rows[11] == (12, 13_923, 301, 3)
assert rows[15] == (16, 14_209, 15, 2)
assert rows[17] == (18, 14_224, 0, 1)
assert predicate_rows[0][:4] == (4, 169, 14_055, 620)
assert predicate_rows[1][:4] == (8, 7_612, 6_612, 10)
assert predicate_rows[2][:4] == (12, 13_786, 438, 3)
assert predicate_rows[3][:4] == (16, 14_207, 17, 2)
assert predicate_rows[4][:4] == (18, 14_224, 0, 1)
assert mask_checks > 0
assert shared_group_checks > 0

print("PASS A0 s=1 Route-B 8-jump source/ballot quotient certificate")
print("frontier_cylinders", len(states))
print("full_transition_templates")
for d, distinct, saved, max_group in rows:
    print(
        "horizon", d,
        "templates", distinct,
        "reused_payload_instances", saved,
        "max_payloads_per_template", max_group,
    )
print("predicate_relative_signatures")
for row in predicate_rows:
    d, distinct, saved, max_group, memo_states, interned_nodes = row
    print(
        "horizon", d,
        "acceptance_signatures", distinct,
        "reused_payload_instances", saved,
        "max_payloads_per_signature", max_group,
        "memo_states", memo_states,
        "interned_tree_nodes", interned_nodes,
    )
print("mask_regression_horizon", MASK_REGRESSION_D)
print("mask_checks", mask_checks)
print("shared_group_checks", shared_group_checks)
print(
    "full_template",
    "P_d=(S, future Q-increments, y mod 2^d, 3^q mod 2^d)",
)
print(
    "predicate_template",
    "interned binary decision tree of pure-ballot accept/reject outcomes over low parameter bits",
)
print(
    "separation",
    "at d=18 all 14,224 current payloads are distinct even under the coarser pure-ballot-only acceptance signature",
)
print(
    "dsd_audit",
    "predicate-relative forgetting gives a strictly coarser finite quotient, but exact source payloads are still not merged and no horizon-independent quotient is inferred",
)
print(
    "status",
    "finite-horizon source/ballot quotients CLOSED; global source-family contraction remains OPEN",
)
