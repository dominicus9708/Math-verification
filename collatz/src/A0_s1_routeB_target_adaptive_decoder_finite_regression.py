#!/usr/bin/env python3
"""Finite target-aware adaptive decoder regression for A0 s=1 Route-B.

This is a finite regression test for the G4 decoder architecture, not a proof
of universal Route-B membership.

The target is the exact threshold word of length 18.  We first restrict to
words with the same exact `(h,q,m,a)` ballot/counter metadata as the target.
Among that class, candidates that still collide with the target at bridge
resolution `(K,L)` are exactly those whose correction difference Delta obeys

    K <= v_2(Delta),   L <= v_3(Delta).

A greedy adaptive decoder compares the survivor counts obtained by increasing
`K` or `L` by one and refines only the more discriminating axis.  The resulting
path is independently checked by direct congruence of C modulo `2^K 3^L`.

Scope:
  * target-aware adaptive axis selection algorithm: finite regression CLOSED;
  * universal long-language target decoder: OPEN.
"""

from fractions import Fraction
from functools import lru_cache

N = 18


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


def requirement(n):
    return 0 if n == 0 else floor_alpha(n) + 1


def threshold_word(n):
    return tuple(requirement(i + 1) - requirement(i) for i in range(n))


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


target = threshold_word(N)
target_h, target_q, target_C = correction_summary(target)
target_ballot = ballot_summary(target)
assert target_h == N
assert target_q == target_ballot[1]

candidates = []
for address in range(1 << N):
    bits = tuple((address >> i) & 1 for i in range(N))
    h, q, C = correction_summary(bits)
    ballot = ballot_summary(bits)
    if (h, q, ballot[2], ballot[3]) == (
        target_h,
        target_q,
        target_ballot[2],
        target_ballot[3],
    ):
        candidates.append((bits, C))

assert len(candidates) == 2_652
assert sum(bits == target for bits, _ in candidates) == 1

other_valuations = []
for bits, C in candidates:
    if bits == target:
        continue
    delta = C - target_C
    other_valuations.append((valuation(delta, 2), valuation(delta, 3)))

assert len(other_valuations) == 2_651


def survivor_count(K, L):
    return sum(K <= v2 and L <= v3 for v2, v3 in other_valuations)


K = L = 1
greedy_path = []
while True:
    survivors = survivor_count(K, L)
    greedy_path.append((K, L, survivors))
    if survivors == 0:
        break
    survivors_if_K = survivor_count(K + 1, L)
    survivors_if_L = survivor_count(K, L + 1)
    if survivors_if_L <= survivors_if_K:
        L += 1
    else:
        K += 1

assert greedy_path == [
    (1, 1, 1498),
    (1, 2, 960),
    (1, 3, 476),
    (1, 4, 180),
    (1, 5, 85),
    (1, 6, 30),
    (1, 7, 12),
    (1, 8, 6),
    (1, 9, 2),
    (1, 10, 1),
    (1, 11, 0),
]

modular_checks = 0
for K_test, L_test, expected in greedy_path:
    modulus = (1 << K_test) * pow(3, L_test)
    direct = 0
    for bits, C in candidates:
        if bits == target:
            continue
        if C % modulus == target_C % modulus:
            direct += 1
        modular_checks += 1
    assert direct == expected

print("PASS A0 s=1 Route-B target-aware adaptive decoder finite regression")
print("target_length", N)
print("target_ones", target_q)
print("target_ballot", target_ballot)
print("same_hq_ballot_candidates", len(candidates))
print("initial_other_colliders", greedy_path[0][2])
print("greedy_path", greedy_path)
print("final_resolution", (K, L))
print("modular_checks", modular_checks)
print(
    "formation_audit",
    "target filtering uses only already formed correction and ballot coordinates; adaptive refinement adds observation precision without changing the candidate definition",
)
print(
    "axis_audit",
    "the decoder chooses dyadic or ternary observation axes independently according to actual collision reduction",
)
print(
    "dsd_audit",
    "finite target isolation is verified but is not promoted to a universal long-language theorem",
)
print(
    "status",
    "target-aware adaptive selection algorithm VERIFIED on finite threshold-prefix regression; universal long-language decoder remains OPEN",
)
