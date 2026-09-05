#!/usr/bin/env python3
"""Scaling regression for the exact ternary suffix-carry family DP.

This is deliberately a regression on the same threshold-dominance language as
the length-18 target audit.  It is NOT a proof that the huge Christoffel root
has the same ballot language.

At threshold length h=84 the target has q=53 ones.  The exact dominance family
contains more than 10^21 candidates, yet the memoized suffix-carry DP evaluates
selected ternary resolutions without enumerating those candidates.

Certified finite outputs:

    total dominance family = 1,122,428,422,670,255,691,408
    L=28 colliders          = 4,326,432,820
    L=52 colliders          = 1

The target is included in all counts.

Scope:
  * exact finite scaling regression for the threshold-dominance model: CLOSED;
  * transfer to the long Christoffel/critical-prefix Route-B language: OPEN;
  * horizon-independent carry quotient: OPEN.
"""

from fractions import Fraction
from functools import lru_cache

N = 84
K = 1


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
def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def requirement(n: int) -> int:
    return 0 if n == 0 else floor_alpha(n) + 1


def threshold_word(n: int):
    return tuple(requirement(i + 1) - requirement(i) for i in range(n))


TARGET = threshold_word(N)
A = tuple(i for i, bit in enumerate(TARGET) if bit)
Q = len(A)
assert Q == 53
assert A[:12] == (0, 1, 3, 4, 6, 7, 9, 11, 12, 14, 15, 17)
assert A[-10:] == (68, 69, 71, 72, 74, 76, 77, 79, 80, 82)


def make_prefix_counter(K: int):
    p = sum(a < K for a in A)

    @lru_cache(None)
    def prefix_count(rcount: int, upper_exclusive: int) -> int:
        if rcount == 0:
            return 1

        i = rcount - 1
        if i < p:
            b = A[i]
            if b >= upper_exclusive:
                return 0
            return prefix_count(rcount - 1, b)

        lo = max(i, K)
        hi = min(A[i], upper_exclusive - 1)
        if lo > hi:
            return 0
        return sum(prefix_count(rcount - 1, b) for b in range(lo, hi + 1))

    return prefix_count


PREFIX = make_prefix_counter(K)
DOMINANCE_TOTAL = PREFIX(Q, N)
assert DOMINANCE_TOTAL == 1_122_428_422_670_255_691_408


def family_collision_count(L: int):
    p = sum(a < K for a in A)

    @lru_cache(None)
    def rec(t: int, next_b: int, z: int) -> int:
        r = Q - 1 - t

        if t == L:
            return PREFIX(r + 1, next_b)

        if r < 0:
            modulus = 3 ** (L - t)
            return 1 if z % modulus == 0 else 0

        m = L - t
        modulus = 3 ** m
        next_modulus = 3 ** (m - 1)

        if r < p:
            candidates = (A[r],)
        else:
            lo = max(r, K)
            hi = min(A[r], next_b - 1)
            candidates = range(lo, hi + 1) if lo <= hi else ()

        pa = pow(2, A[r], modulus)
        total = 0
        for b in candidates:
            atom = (pa - pow(2, b, modulus)) % modulus
            s = z + atom
            if s % 3:
                continue
            z_next = (s // 3) % next_modulus if next_modulus > 1 else 0
            total += rec(t + 1, b, z_next)

        return total

    value = rec(0, N, 0)
    return value, rec.cache_info().currsize


L28_COUNT, L28_STATES = family_collision_count(28)
assert L28_COUNT == 4_326_432_820
assert L28_STATES == 652_215

L52_COUNT, L52_STATES = family_collision_count(52)
assert L52_COUNT == 1
assert L52_STATES == 877_661

print("PASS A0 s=1 Route-B threshold-84 ternary carry scaling regression")
print("length", N)
print("ones", Q)
print("dominance_family", DOMINANCE_TOTAL)
print("L28_colliders_including_target", L28_COUNT)
print("L28_memo_states", L28_STATES)
print("L52_colliders_including_target", L52_COUNT)
print("L52_memo_states", L52_STATES)
print(
    "compression_audit",
    "a >10^21 finite dominance family is counted through <9e5 memoized carry states at the tested resolutions",
)
print(
    "dsd_audit",
    "this scaling result belongs only to the threshold-dominance language; it is not transferred to the long Christoffel critical-prefix language without a separate equivalence proof",
)
print(
    "status",
    "finite threshold-family scaling regression CLOSED; long-language globalization remains OPEN",
)
