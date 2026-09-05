#!/usr/bin/env python3
"""Adaptive dual-adic + phase-critical ballot refinement certificate.

This certificate combines two already-established Route-B sectors:

  bridge_{K,L}(W) = (3^q, 2^h, C) mod M,  M=2^K 3^L

and the exact phase-critical ballot summary

  ballot(W) = (h,q,m,a).

For two blocks U,V with the same (h,q), equality of bridge states at (K,L)
reduces exactly to divisibility of Delta=C(U)-C(V) by 2^K 3^L. Hence the
first dyadic and ternary resolutions that can distinguish the pair are

  K* = v_2(Delta)+1,
  L* = v_3(Delta)+1.

The ballot coordinates may distinguish a bridge collision before either
resolution is raised. The combined state is compositionally closed because
both sectors are compositionally closed.

A finite exhaustive decoder audit at word length 12 starts from (K,L)=(2,2).
At every non-singleton combined-state bucket it raises exactly one resolution
by one, choosing the axis that creates the finer immediate partition. This
is a finite decoder audit, not a universal Route-B membership proof.
"""

from collections import defaultdict, Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from typing import Optional

NLOG = 90
COMPOSITION_MAX_DEPTH = 9
AUDIT_WORD_LENGTH = 12
K0 = 2
L0 = 2


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
    assert flo == fhi
    return flo


def phase_carry(a: int, b: int) -> int:
    c = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert c in (0, 1)
    return c


def frac_compare(a: int, b: int) -> int:
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def max_fractional(candidates):
    vals = [x for x in candidates if x is not None]
    if not vals:
        return None
    best = vals[0]
    for x in vals[1:]:
        if frac_compare(x, best) > 0:
            best = x
    return best


@dataclass(frozen=True)
class BallotSummary:
    length: int
    ones: int
    base_min: int
    critical_prefix: Optional[int]


def direct_ballot(bits) -> BallotSummary:
    q = 0
    m = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < m:
            m = d
            critical = u
        elif d == m:
            if critical is None or frac_compare(u, critical) > 0:
                critical = u
    return BallotSummary(len(bits), q, m, critical)


def compose_ballot(a: BallotSummary, b: BallotSummary) -> BallotSummary:
    assert a.length >= 1 and b.length >= 1
    endpoint_a = a.ones - floor_alpha(a.length)
    right_min = endpoint_a + b.base_min - (
        phase_carry(a.length, b.critical_prefix)
        if b.critical_prefix is not None
        else 0
    )
    parent_min = min(a.base_min, right_min)
    left_candidate = a.critical_prefix if a.base_min == parent_min else None
    right_candidate = None
    if right_min == parent_min:
        right_candidate = a.length + (
            b.critical_prefix if b.critical_prefix is not None else 0
        )
    return BallotSummary(
        a.length + b.length,
        a.ones + b.ones,
        parent_min,
        max_fractional((left_candidate, right_candidate)),
    )


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
    return (pow(3, q, M), pow(2, h, M), C % M)


def compose_bridge(U, V, K: int, L: int):
    M = modulus(K, L)
    Au, Bu, Cu = U
    Av, Bv, Cv = V
    return (
        Au * Av % M,
        Bu * Bv % M,
        (Av * Cu + Bu * Cv) % M,
    )


def combined_state(bits, K: int, L: int):
    return bridge_state(bits, K, L), direct_ballot(bits)


def valuation(n: int, p: int) -> int:
    assert n != 0 and p in (2, 3)
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


# ---------------------------------------------------------------------------
# 1. Combined compositional closure on arbitrary words.
# ---------------------------------------------------------------------------
composition_checks = 0
for h in range(2, COMPOSITION_MAX_DEPTH + 1):
    for bits in product((0, 1), repeat=h):
        direct_b = direct_ballot(bits)
        direct_c = bridge_state(bits, 4, 4)
        for split in range(1, h):
            lb = direct_ballot(bits[:split])
            rb = direct_ballot(bits[split:])
            assert compose_ballot(lb, rb) == direct_b
            lc = bridge_state(bits[:split], 4, 4)
            rc = bridge_state(bits[split:], 4, 4)
            assert compose_bridge(lc, rc, 4, 4) == direct_c
            composition_checks += 1

assert composition_checks == 7_172


# ---------------------------------------------------------------------------
# 2. Pairwise valuation theorem at the coarse audit resolution.
# ---------------------------------------------------------------------------
words = tuple(product((0, 1), repeat=AUDIT_WORD_LENGTH))
coarse_bridge_buckets = defaultdict(list)
coarse_combined_buckets = defaultdict(list)

for bits in words:
    coarse_bridge_buckets[bridge_state(bits, K0, L0)].append(bits)
    coarse_combined_buckets[combined_state(bits, K0, L0)].append(bits)


def pair_count(groups):
    return sum(len(g) * (len(g) - 1) // 2 for g in groups if len(g) >= 2)


bridge_collision_pairs = pair_count(coarse_bridge_buckets.values())
combined_collision_pairs = pair_count(coarse_combined_buckets.values())
ballot_separated_pairs = bridge_collision_pairs - combined_collision_pairs

same_hq_bridge_buckets = defaultdict(list)
for bits in words:
    h, q, _ = correction_summary(bits)
    same_hq_bridge_buckets[(h, q, bridge_state(bits, K0, L0))].append(bits)
same_hq_bridge_collision_pairs = pair_count(same_hq_bridge_buckets.values())

assert bridge_collision_pairs == 246_489
assert same_hq_bridge_collision_pairs == 89_684
assert combined_collision_pairs == 27_792
assert ballot_separated_pairs == 218_697
assert same_hq_bridge_collision_pairs - combined_collision_pairs == 61_892

valuation_pair_checks = 0
extra_step_hist = Counter()
dyadic_cheaper = ternary_cheaper = equal_cost = 0

for group in coarse_combined_buckets.values():
    if len(group) < 2:
        continue
    data = [(bits, correction_summary(bits)[2]) for bits in group]
    for i in range(len(data)):
        bits_u, Cu = data[i]
        hu, qu, _ = correction_summary(bits_u)
        for j in range(i + 1, len(data)):
            bits_v, Cv = data[j]
            hv, qv, _ = correction_summary(bits_v)
            assert hu == hv
            assert qu == qv
            Delta = Cu - Cv
            assert Delta != 0
            v2 = valuation(Delta, 2)
            v3 = valuation(Delta, 3)
            assert v2 >= K0 and v3 >= L0

            assert bridge_state(bits_u, K0, L0) == bridge_state(bits_v, K0, L0)
            for K in range(1, v2 + 1):
                assert bridge_state(bits_u, K, L0) == bridge_state(bits_v, K, L0)
            assert bridge_state(bits_u, v2 + 1, L0) != bridge_state(bits_v, v2 + 1, L0)

            for L in range(1, v3 + 1):
                assert bridge_state(bits_u, K0, L) == bridge_state(bits_v, K0, L)
            assert bridge_state(bits_u, K0, v3 + 1) != bridge_state(bits_v, K0, v3 + 1)

            d2 = v2 - K0 + 1
            d3 = v3 - L0 + 1
            extra_step_hist[min(d2, d3)] += 1
            if d2 < d3:
                dyadic_cheaper += 1
            elif d3 < d2:
                ternary_cheaper += 1
            else:
                equal_cost += 1
            valuation_pair_checks += 1

assert valuation_pair_checks == combined_collision_pairs
assert extra_step_hist == Counter({1: 20_980, 2: 5_742, 3: 1_024, 4: 46})
assert dyadic_cheaper == 7_512
assert ternary_cheaper == 11_295
assert equal_cost == 8_985


# ---------------------------------------------------------------------------
# 3. Adaptive one-axis-at-a-time decoder audit.
# ---------------------------------------------------------------------------
adaptive_internal_nodes = 0
adaptive_leaves = 0
adaptive_max_steps = 0
adaptive_max_K = K0
adaptive_max_L = L0
adaptive_axis_K_steps = 0
adaptive_axis_L_steps = 0


def partition(group, K, L):
    out = defaultdict(list)
    for bits in group:
        out[combined_state(bits, K, L)].append(bits)
    return out


def adaptive_decode(group, K, L, steps=0):
    global adaptive_internal_nodes, adaptive_leaves
    global adaptive_max_steps, adaptive_max_K, adaptive_max_L
    global adaptive_axis_K_steps, adaptive_axis_L_steps

    if len(group) <= 1:
        adaptive_leaves += len(group)
        adaptive_max_steps = max(adaptive_max_steps, steps)
        return

    adaptive_internal_nodes += 1
    options = []
    for axis in ("K", "L"):
        K2, L2 = (K + 1, L) if axis == "K" else (K, L + 1)
        parts = partition(group, K2, L2)
        max_bucket = max(len(x) for x in parts.values())
        score = (len(parts), -max_bucket, 1 if axis == "K" else 0)
        options.append((score, axis, K2, L2, parts))

    _, axis, K2, L2, parts = max(options, key=lambda x: x[0])
    if axis == "K":
        adaptive_axis_K_steps += 1
    else:
        adaptive_axis_L_steps += 1

    adaptive_max_K = max(adaptive_max_K, K2)
    adaptive_max_L = max(adaptive_max_L, L2)

    for child in parts.values():
        adaptive_decode(child, K2, L2, steps + 1)


initial_collision_groups = [g for g in coarse_combined_buckets.values() if len(g) >= 2]
initial_singletons = sum(1 for g in coarse_combined_buckets.values() if len(g) == 1)
initial_collision_words = sum(len(g) for g in initial_collision_groups)

for group in initial_collision_groups:
    adaptive_decode(group, K0, L0)

assert initial_singletons == 171
assert initial_collision_words == 3_925
assert adaptive_leaves == initial_collision_words
assert adaptive_internal_nodes == 2_960
assert adaptive_max_steps == 7
assert adaptive_max_K == 9
assert adaptive_max_L == 8

assert len({combined_state(w, adaptive_max_K, adaptive_max_L) for w in words}) == len(words)


print("PASS A0 s=1 Route-B adaptive bridge + ballot refinement certificate")
print("composition_checks", composition_checks)
print("audit_word_length", AUDIT_WORD_LENGTH)
print("initial_resolution", (K0, L0))
print("bridge_collision_pairs", bridge_collision_pairs)
print("same_hq_bridge_collision_pairs", same_hq_bridge_collision_pairs)
print("ballot_separated_pairs", ballot_separated_pairs)
print("same_hq_ballot_separated_pairs", same_hq_bridge_collision_pairs - combined_collision_pairs)
print("combined_collision_pairs", combined_collision_pairs)
print("valuation_pair_checks", valuation_pair_checks)
print("extra_step_hist", dict(sorted(extra_step_hist.items())))
print("dyadic_cheaper_pairs", dyadic_cheaper)
print("ternary_cheaper_pairs", ternary_cheaper)
print("equal_cost_pairs", equal_cost)
print("initial_singletons", initial_singletons)
print("initial_collision_groups", len(initial_collision_groups))
print("initial_collision_words", initial_collision_words)
print("adaptive_internal_nodes", adaptive_internal_nodes)
print("adaptive_leaves", adaptive_leaves)
print("adaptive_max_steps", adaptive_max_steps)
print("adaptive_max_K", adaptive_max_K)
print("adaptive_max_L", adaptive_max_L)
print("adaptive_axis_K_steps", adaptive_axis_K_steps)
print("adaptive_axis_L_steps", adaptive_axis_L_steps)
print(
    "formation_audit",
    "combined state is formed compositionally from correction bridge and ballot summaries; refinement adds only requested resolution",
)
print(
    "axis_audit",
    "K and L are external resolution axes; ballot critical prefix remains intrinsic and can separate bridge collisions before resolution growth",
)
print(
    "dsd_audit",
    "adaptive refinement is exact on the finite audit domain; finite separation does not imply universal Route-B membership closure",
)
print(
    "status",
    "G4 adaptive correction+ballot decoder primitive CLOSED on finite audit domain; universal long-language closure remains OPEN",
)
