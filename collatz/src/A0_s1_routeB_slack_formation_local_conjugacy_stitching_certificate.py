#!/usr/bin/env python3
"""Projective slack/formation local conjugacy and direct-stitch obstruction.

For equal-count target/candidate one positions, index from the right:

    A_t = a_(q-1-t),
    B_t = b_(q-1-t),
    base_t = q-t-1,
    D_t = A_t-base_t,
    s_t = B_t-base_t.

The suffix carry gate is

    z_(t+1) = (z_t + 2^A_t - 2^B_t)/3.

At remaining ternary precision m=q-t define the projective normalized carry

    c_t = 2^(-base_t) z_t  (mod 3^m).

Because base_(t+1)=base_t-1, the exact projected recurrence is

    c_(t+1)
      = [2*c_t + 2*(2^D_t-2^s_t)]/3
      (mod 3^(m-1)).

This is algebraically the same one-step recurrence as the established
formation transition from rank D_t to rank s_t.

However, consecutive local pairs do NOT in general form one standard
formation rank path.  Direct stitching of gate t and gate t+1 requires

    s_t = D_(t+1),

which is equivalent to

    B_t = A_(t+1)+1.

General dominance gives neither condition.  In particular, even target=self
fails at every target one-gap of size 2.

If D_(t+1)>s_t, a connector would require a forbidden rank increase.  If
D_(t+1)<s_t, a nonempty descending connector changes the carry by an affine
formation map and is not a state-independent relabel.  Thus local recurrence
conjugacy cannot be promoted to global formation membership without a separate
bridge theorem and its arithmetic hypotheses.

The exhaustive checks below are regression guards for the projective formula,
the stitching equivalence, and the existence of abundant non-stitching cases.
"""

from itertools import combinations

MAX_H = 8
MAX_Z_REP = 30


def gate_successor(z: int, A: int, B: int, m: int):
    M = 3 ** m
    numer = (z + pow(2, A, M) - pow(2, B, M)) % M
    if numer % 3:
        return None
    return 0 if m == 1 else (numer // 3) % (3 ** (m - 1))


def normalized_formation_step(c: int, D: int, s: int, m: int):
    M = 3 ** m
    numer = (2 * c + 2 * (pow(2, D, M) - pow(2, s, M))) % M
    if numer % 3:
        return None
    return 0 if m == 1 else (numer // 3) % (3 ** (m - 1))


local_checks = 0
stitch_checks = 0
stitch_equal = 0
stitch_fail = 0
target_self_fail = 0
rank_increase_cases = 0
rank_drop_cases = 0

for h in range(1, MAX_H + 1):
    for q in range(1, h + 1):
        for target in combinations(range(h), q):
            for candidate in combinations(range(h), q):
                if not all(candidate[i] <= target[i] for i in range(q)):
                    continue

                # 1. Exact projective one-gate conjugacy.
                for t in range(q):
                    A = target[q - 1 - t]
                    B = candidate[q - 1 - t]
                    base = q - t - 1
                    D = A - base
                    s = B - base
                    assert 0 <= s <= D

                    m = q - t
                    M = 3 ** m
                    inv_scale = pow(pow(2, base, M), -1, M)

                    for z in range(min(M, MAX_Z_REP)):
                        z_next = gate_successor(z, A, B, m)
                        c = (z * inv_scale) % M
                        c_next = normalized_formation_step(c, D, s, m)

                        if z_next is None:
                            assert c_next is None
                        elif m == 1:
                            assert c_next == 0
                        else:
                            M2 = 3 ** (m - 1)
                            expected = (
                                z_next
                                * pow(pow(2, base - 1, M2), -1, M2)
                            ) % M2
                            assert c_next == expected
                        local_checks += 1

                # 2. Consecutive local rank pairs directly stitch iff
                #    s_t=D_(t+1), equivalently B_t=A_(t+1)+1.
                for t in range(q - 1):
                    base = q - t - 1
                    s = candidate[q - 1 - t] - base
                    D_next = target[q - 2 - t] - (base - 1)

                    direct_stitch = s == D_next
                    position_rule = (
                        candidate[q - 1 - t] == target[q - 2 - t] + 1
                    )
                    assert direct_stitch == position_rule
                    stitch_checks += 1

                    if direct_stitch:
                        stitch_equal += 1
                    else:
                        stitch_fail += 1
                        if D_next > s:
                            rank_increase_cases += 1
                        else:
                            assert D_next < s
                            rank_drop_cases += 1
                        if candidate == target:
                            target_self_fail += 1

# Exact finite regression totals for this audit range.
assert local_checks == 438_144
assert stitch_checks == 19_273
assert stitch_equal == 8_399
assert stitch_fail == 10_874
assert target_self_fail == 522
assert rank_increase_cases == 7_904
assert rank_drop_cases == 2_970

# A minimal target=self witness with target one-gap 2.
target = (0, 2)
candidate = target
q = 2
t = 0
base = q - t - 1
s = candidate[1] - base
D_next = target[0] - (base - 1)
assert s == 1 and D_next == 0 and s != D_next

print("PASS A0 s=1 Route-B slack/formation local conjugacy stitching certificate")
print("max_h", MAX_H)
print("local_projective_gate_checks", local_checks)
print("direct_stitch_boundary_checks", stitch_checks)
print("direct_stitch_equal", stitch_equal)
print("direct_stitch_fail", stitch_fail)
print("target_self_stitch_fail", target_self_fail)
print("rank_increase_reset_cases", rank_increase_cases)
print("rank_drop_reset_cases", rank_drop_cases)
print(
    "local_conjugacy",
    "c_next=[2c+2(2^D-2^s)]/3 after c=2^(-base)z in the projective 3-adic quotient",
)
print(
    "direct_stitch_rule",
    "s_t=D_(t+1) iff B_t=A_(t+1)+1",
)
print(
    "global_audit",
    "local recurrence equality is not global formation-path membership; a separate carry-dependent bridge theorem would be required",
)
print(
    "status",
    "local projective conjugacy CLOSED; direct global rank-path identification REJECTED in general",
)
