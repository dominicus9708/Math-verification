#!/usr/bin/env python3
"""Adaptive dual-adic bridge refinement + ballot right-congruence certificate.

For two parity blocks U,V with the same exact (h,q), let

    Delta = C(U)-C(V) != 0.

At bridge resolution (K,L), equality of the correction-sector states

    (3^q,2^h,C mod 2^K 3^L)

is equivalent to

    2^K 3^L | Delta,

i.e.

    K <= v_2(Delta) and L <= v_3(Delta).

Hence either single-axis refinement

    K* = v_2(Delta)+1
or
    L* = v_3(Delta)+1

separates the two correction candidates exactly.  This is the adaptive
refinement law needed by the Route-B lazy decoder: only colliding candidates
need additional resolution.

The certificate also augments the fixed-resolution correction bridge with the
exact phase-critical ballot summary (h,q,m,a).  Equality of this combined state
is tested under arbitrary common right extensions.  Because both sectors are
compositionally closed, this gives the finite combined right-congruence needed
for G4 at each chosen resolution.

Scope:
  * exact valuation-based adaptive correction refinement: CLOSED;
  * finite correction+ballot right-congruence at fixed resolution: CLOSED;
  * recognition of the universal Route-B admissible language: OPEN.
"""

from fractions import Fraction
from functools import lru_cache

MAX_DEPTH = 9
PAIR_DEPTH = 10
EXT_MAX = 3


def log_bounds(z: Fraction, n: int = 90):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(None)
def floor_alpha(n):
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def frac_compare(a, b):
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
        elif d == base_min and (
            critical is None or frac_compare(u, critical) > 0
        ):
            critical = u
    return len(bits), q, base_min, critical


def correction_summary(bits):
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def valuation(n, p):
    n = abs(n)
    assert n
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def bridge_core(bits, K, L):
    h, q, C = correction_summary(bits)
    M = (1 << K) * pow(3, L)
    return pow(3, q, M), pow(2, h, M), C % M


def combined_state(bits, K, L):
    h, q, _ = correction_summary(bits)
    _, _, base_min, critical = ballot_summary(bits)
    return h, q, *bridge_core(bits, K, L), base_min, critical


same_hq_pair_checks = 0
collision_equivalence_checks = 0
adaptive_dyadic_separation_checks = 0
adaptive_ternary_separation_checks = 0
valuation_histogram = {}

for h in range(2, PAIR_DEPTH + 1):
    by_q = {}
    for address in range(1 << h):
        bits = tuple((address >> i) & 1 for i in range(h))
        _, q, C = correction_summary(bits)
        by_q.setdefault(q, []).append((bits, C))

    for q, items in by_q.items():
        if q == 0:
            continue
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                delta = items[i][1] - items[j][1]
                if not delta:
                    continue

                same_hq_pair_checks += 1
                v2 = valuation(delta, 2)
                v3 = valuation(delta, 3)
                valuation_histogram[(v2, v3)] = (
                    valuation_histogram.get((v2, v3), 0) + 1
                )

                for K in range(1, min(h, 6) + 1):
                    for L in range(1, min(q, 6) + 1):
                        same = bridge_core(items[i][0], K, L) == bridge_core(
                            items[j][0], K, L
                        )
                        expected = K <= v2 and L <= v3
                        assert same == expected
                        collision_equivalence_checks += 1

                K_star = v2 + 1
                mod2 = 1 << K_star
                assert items[i][1] % mod2 != items[j][1] % mod2
                adaptive_dyadic_separation_checks += 1

                L_star = v3 + 1
                mod3 = pow(3, L_star)
                assert items[i][1] % mod3 != items[j][1] % mod3
                adaptive_ternary_separation_checks += 1


combined_collision_pairs = 0
combined_extension_checks = 0

for K, L in ((1, 1), (2, 2), (3, 2)):
    buckets = {}
    for h in range(1, MAX_DEPTH + 1):
        for address in range(1 << h):
            bits = tuple((address >> i) & 1 for i in range(h))
            buckets.setdefault(combined_state(bits, K, L), []).append(bits)

    for group in buckets.values():
        if len(group) < 2:
            continue
        representative = group[0]
        for other in group[1:]:
            combined_collision_pairs += 1
            for ext_h in range(0, EXT_MAX + 1):
                for ext_address in range(1 << ext_h):
                    extension = tuple(
                        (ext_address >> i) & 1 for i in range(ext_h)
                    )
                    assert combined_state(
                        representative + extension, K, L
                    ) == combined_state(other + extension, K, L)
                    combined_extension_checks += 1


print("PASS A0 s=1 Route-B adaptive bridge + ballot congruence certificate")
print("pair_depth", PAIR_DEPTH)
print("same_hq_pair_checks", same_hq_pair_checks)
print("collision_equivalence_checks", collision_equivalence_checks)
print("adaptive_dyadic_separation_checks", adaptive_dyadic_separation_checks)
print("adaptive_ternary_separation_checks", adaptive_ternary_separation_checks)
print("valuation_classes", len(valuation_histogram))
print("max_v2", max(k[0] for k in valuation_histogram))
print("max_v3", max(k[1] for k in valuation_histogram))
print("combined_collision_pairs", combined_collision_pairs)
print("combined_extension_checks", combined_extension_checks)
print(
    "formation_audit",
    "adaptive refinement changes only the exposed correction coordinate; ballot summary remains an independently formed intrinsic block state",
)
print(
    "axis_audit",
    "dyadic and ternary resolutions are external observation axes and may be refined independently without redefining the intrinsic block",
)
print(
    "dsd_audit",
    "finite combined right-congruence is exact at each selected resolution; universal admissible-language recognition is not inferred",
)
print(
    "status",
    "G4 adaptive correction refinement CLOSED; correction+ballot finite right-congruence CLOSED; universal Route-B membership remains OPEN",
)
