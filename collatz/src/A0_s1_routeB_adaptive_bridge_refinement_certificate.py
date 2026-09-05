#!/usr/bin/env python3
"""Adaptive dual-adic bridge refinement for A0 s=1 Route-B.

This certificate closes the exact refinement primitive for collision classes
whose candidate words have the same length h and the same odd-count q.
For such U,V, their fixed-resolution bridge states

    S_{K,L}(W) = (3^q, 2^h, C(W)) mod M,
    M = 2^K 3^L,

have identical first two coordinates, so

    S_{K,L}(U) = S_{K,L}(V)
      iff 2^K 3^L divides Delta,

where Delta=C(U)-C(V).  Hence, for distinct words in the same (h,q) class,

    K_* = v_2(Delta)+1,
    L_* = v_3(Delta)+1

are exact first separating resolutions in the dyadic and ternary directions.
If a pair collides at (K,L), then either refinement

    (K,L) -> (K_*,L)

or

    (K,L) -> (K,L_*)

separates it.  A decoder may choose the cheaper coordinate increment.

The certificate also crosses this correction-sector refinement with the exact
phase-critical ballot summary (h,q,m,a).  A ballot difference can separate a
bridge collision without any adic refinement; if the ballot summaries also
coincide, the valuation-guided refinement still separates every distinct
same-(h,q) pair in the exhaustive audit domain.

Scope:
  * exact adaptive refinement inside a fixed (h,q) collision class: CLOSED;
  * ballot cross-filter compatibility: CLOSED on the exhaustive audit domain;
  * reduction of every Route-B survivor to such a fixed (h,q) class: NOT
    asserted here;
  * universal long-language membership: still OPEN.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations

MAX_DEPTH = 11
RESOLUTIONS = (
    (1, 1),
    (2, 2),
    (3, 2),
    (4, 3),
    (5, 4),
)
NLOG = 90


def correction_summary(bits):
    h = q = C = 0
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def modulus(K: int, L: int) -> int:
    return (1 << K) * pow(3, L)


def bridge_state(bits, K: int, L: int):
    h, q, C = correction_summary(bits)
    M = modulus(K, L)
    return pow(3, q, M), pow(2, h, M), C % M


def valuation(n: int, p: int) -> int:
    assert n != 0 and p in (2, 3)
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


# ---------------------------------------------------------------------------
# Exact phase-critical ballot summary, using the same rational log enclosure
# as the standalone ballot certificate.  No floating point enters assertions.
# ---------------------------------------------------------------------------
def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(maxsize=None)
def floor_alpha(n: int) -> int:
    assert n >= 0
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi, ("insufficient log interval", n, flo, fhi)
    return flo


def frac_compare(a: int, b: int) -> int:
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def ballot_summary(bits):
    q = 0
    base_min = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < base_min:
            base_min = d
            critical = u
        elif d == base_min:
            if critical is None or frac_compare(u, critical) > 0:
                critical = u
    return len(bits), q, base_min, critical


# ---------------------------------------------------------------------------
# Exhaustive same-(h,q) pair audit.
# ---------------------------------------------------------------------------
groups_by_depth = {}
for h in range(1, MAX_DEPTH + 1):
    groups = {}
    for address in range(1 << h):
        bits = tuple((address >> i) & 1 for i in range(h))
        hs, q, C = correction_summary(bits)
        assert hs == h
        groups.setdefault(q, []).append((bits, C, ballot_summary(bits)))
    groups_by_depth[h] = groups

pair_resolution_checks = 0
bridge_collision_checks = 0
adaptive_separation_checks = 0
ballot_split_collisions = 0
combined_remaining_collisions = 0

resolution_stats = {r: [0, 0, 0] for r in RESOLUTIONS}
# [bridge collisions, ballot-split collisions, bridge+ballot collisions]

max_dyadic_increment = 0
max_ternary_increment = 0
cheaper_direction_counts = {"dyadic": 0, "ternary": 0, "tie": 0}
remaining_direction_counts = {"dyadic": 0, "ternary": 0, "tie": 0}

for h, groups in groups_by_depth.items():
    for q, items in groups.items():
        for (u, Cu, Bu), (v, Cv, Bv) in combinations(items, 2):
            Delta = Cu - Cv

            # C is irredundant once h and q are fixed: if C were equal then
            # r=-C*(3^q)^(-1) mod 2^h would be equal, hence the realized
            # length-h parity cylinder would be the same word.
            assert Delta != 0, (h, q, u, v, Cu)

            v2 = valuation(Delta, 2)
            v3 = valuation(Delta, 3)

            for K, L in RESOLUTIONS:
                pair_resolution_checks += 1
                same_bridge = bridge_state(u, K, L) == bridge_state(v, K, L)
                divisibility_prediction = v2 >= K and v3 >= L
                assert same_bridge == divisibility_prediction

                if not same_bridge:
                    continue

                bridge_collision_checks += 1
                resolution_stats[(K, L)][0] += 1

                K_star = v2 + 1
                L_star = v3 + 1
                assert K_star > K and L_star > L

                # Each coordinate by itself can break the collision exactly at
                # the first resolution above the corresponding valuation.
                assert bridge_state(u, K_star, L) != bridge_state(v, K_star, L)
                assert bridge_state(u, K, L_star) != bridge_state(v, K, L_star)
                adaptive_separation_checks += 2

                dK = K_star - K
                dL = L_star - L
                max_dyadic_increment = max(max_dyadic_increment, dK)
                max_ternary_increment = max(max_ternary_increment, dL)

                if dK < dL:
                    direction = "dyadic"
                elif dL < dK:
                    direction = "ternary"
                else:
                    direction = "tie"
                cheaper_direction_counts[direction] += 1

                if Bu != Bv:
                    # Ballot sector already separates the correction collision.
                    ballot_split_collisions += 1
                    resolution_stats[(K, L)][1] += 1
                else:
                    # If ballot also collides, the cheaper exact adic jump
                    # still separates the combined state.
                    combined_remaining_collisions += 1
                    resolution_stats[(K, L)][2] += 1
                    remaining_direction_counts[direction] += 1

                    if dK <= dL:
                        assert (
                            bridge_state(u, K_star, L), Bu
                        ) != (
                            bridge_state(v, K_star, L), Bv
                        )
                    else:
                        assert (
                            bridge_state(u, K, L_star), Bu
                        ) != (
                            bridge_state(v, K, L_star), Bv
                        )


assert pair_resolution_checks == 2_380_725
assert bridge_collision_checks == 187_956
assert adaptive_separation_checks == 375_912
assert ballot_split_collisions == 136_952
assert combined_remaining_collisions == 51_004
assert max_dyadic_increment == 8
assert max_ternary_increment == 8

assert resolution_stats[(1, 1)] == [138_048, 103_391, 34_657]
assert resolution_stats[(2, 2)] == [31_196, 21_157, 10_039]
assert resolution_stats[(3, 2)] == [15_848, 10_479, 5_369]
assert resolution_stats[(4, 3)] == [2_704, 1_801, 903]
assert resolution_stats[(5, 4)] == [160, 124, 36]

assert cheaper_direction_counts == {
    "dyadic": 49_292,
    "ternary": 71_424,
    "tie": 67_240,
}
assert remaining_direction_counts == {
    "dyadic": 14_723,
    "ternary": 20_148,
    "tie": 16_133,
}


print("PASS A0 s=1 Route-B adaptive bridge refinement certificate")
print("max_depth", MAX_DEPTH)
print("resolutions", RESOLUTIONS)
print("pair_resolution_checks", pair_resolution_checks)
print("bridge_collision_checks", bridge_collision_checks)
print("adaptive_separation_checks", adaptive_separation_checks)
print("ballot_split_collisions", ballot_split_collisions)
print("combined_remaining_collisions", combined_remaining_collisions)
print("max_dyadic_increment", max_dyadic_increment)
print("max_ternary_increment", max_ternary_increment)
print("cheaper_direction_counts", cheaper_direction_counts)
print("remaining_direction_counts", remaining_direction_counts)
for resolution in RESOLUTIONS:
    print("resolution_stats", resolution, tuple(resolution_stats[resolution]))
print(
    "formation_audit",
    "refinement adds only the missing adic coordinate needed to distinguish an already formed fixed-(h,q) collision class",
)
print(
    "axis_audit",
    "dyadic and ternary resolution are independent external refinement axes; the cheaper axis may be raised without altering intrinsic block coordinates",
)
print(
    "dsd_audit",
    "ballot cross-filter removes many correction collisions; every remaining audited fixed-(h,q) collision is separated by one exact valuation-guided refinement",
)
print(
    "status",
    "G4 adaptive fixed-(h,q) bridge refinement CLOSED; survivor-to-fixed-class reduction and universal membership remain OPEN",
)
