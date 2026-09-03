#!/usr/bin/env python3
"""Finite-horizon source/ballot product-template quotient at the 8-jump frontier.

For a source channel

    Y = y + A m,   A=3^q odd,

and d future raw parameter bits, the certified source quotient

    Q_d = (y mod 2^d, A mod 2^d)

determines the emitted d-bit parity block for every parameter residue
m mod 2^d.

At absolute depth h with pure-ballot surplus S, the legality of every d-bit
parity block depends only on

    B_d(h,S) = (S, Delta_1,...,Delta_d),

where

    Delta_i = Q(h+i)-Q(h+i-1)

and Q(n)=ceil(n log_3 2).

Therefore the product

    P_d = (B_d(h,S), Q_d)

is an exact *d-horizon transition template*: two exact source cylinders with
the same P_d have the same map from low d parameter bits to parity bits and
the same pure-ballot accept/reject decisions through that horizon.

The exact source interval/residue payload is NOT merged.  After d bits are
consumed, fresh source precision and the new absolute phase/depth are needed
for further continuation.  Thus P_d is not claimed to be a horizon-independent
right congruence.

This certificate applies the quotient to the existing exact 14,224-cylinder
8-jump frontier and measures template reuse.  A small-horizon direct residue
regression independently verifies that cylinders sharing P_d have identical
accepted low-bit masks.
"""

from collections import defaultdict

import A0_s1_14root_8jump_ballot_pruning_certificate as eight
import A0_s1_valuation_jump_ballot_control_certificate as ballot


MAX_D = 18
MASK_REGRESSION_D = 6


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


# Independent direct low-residue regression for the shared-template claim.
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

assert rows[3] == (4, 583, 13_641, 84)
assert rows[7] == (8, 8_372, 5_852, 7)
assert rows[11] == (12, 13_923, 301, 3)
assert rows[15] == (16, 14_209, 15, 2)
assert rows[17] == (18, 14_224, 0, 1)
assert mask_checks > 0
assert shared_group_checks > 0

print("PASS A0 s=1 Route-B 8-jump source/ballot product-template quotient certificate")
print("frontier_cylinders", len(states))
for d, distinct, saved, max_group in rows:
    print(
        "horizon", d,
        "templates", distinct,
        "reused_payload_instances", saved,
        "max_payloads_per_template", max_group,
    )
print("mask_regression_horizon", MASK_REGRESSION_D)
print("mask_checks", mask_checks)
print("shared_group_checks", shared_group_checks)
print(
    "exact_template",
    "P_d=(S, future Q-increments, y mod 2^d, 3^q mod 2^d)",
)
print(
    "d4_reuse_fraction",
    1 - EXPECTED_DISTINCT[4] / len(states),
)
print(
    "d8_reuse_fraction",
    1 - EXPECTED_DISTINCT[8] / len(states),
)
print(
    "separation",
    "at d=18 all 14,224 current payloads have distinct product templates",
)
print(
    "dsd_audit",
    "finite-horizon control/transducer logic may be shared, but exact source payloads are not merged and no horizon-independent quotient is inferred",
)
print(
    "status",
    "finite-horizon source/ballot template quotient CLOSED; global source-family contraction remains OPEN",
)
