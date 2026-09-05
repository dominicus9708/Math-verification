#!/usr/bin/env python3
"""Exact ternary suffix-carry family DP for A0 s=1 Route-B.

This certificate removes full-word enumeration from the target-dominance
candidate class at fixed bridge resolution (K,L).

Let the target and candidate have the same length h and one-count q.  Write
the target one positions as

    a_1 < ... < a_q

and a target-dominating candidate as

    b_1 < ... < b_q,   b_r <= a_r.

For the ordinary Collatz correction

    C(W) = sum_r 3^(q-r) 2^(b_r),

put Delta = C(target)-C(candidate).  Processing one positions from right to
left, define

    F_t = sum_{j=0}^{t-1} 3^j (2^(a_{q-j}) - 2^(b_{q-j})).

All unseen terms of Delta are multiples of 3^t, so

    Delta == F_t (mod 3^t).

Whenever 3^t | F_t, write Z_t = F_t / 3^t.  The next ternary lift is exact:

    3^(t+1) | Delta
      iff Z_t + 2^(a_{q-t}) - 2^(b_{q-t}) == 0 (mod 3),

and then

    Z_{t+1} = (Z_t + 2^(a_{q-t}) - 2^(b_{q-t})) / 3.

At requested final resolution L, only

    Z_t mod 3^(L-t)

is needed.  Thus this is a finite carry quotient, not an exact-C state.

Inside the target-dominance class, the already proved dyadic identity

    v_2(Delta) = first moved candidate-one position

means 2^K | Delta iff the binary target prefix of length K is unchanged.
Accordingly the DP enforces the K-prefix directly and the L ternary digits by
the suffix carry.

For the exact threshold target of length 18, the family DP reproduces all
previous adaptive-decoder survivor counts without enumerating 2^18 words.
A small direct dominance enumeration is retained only as a regression audit.

Scope:
  * exact fixed-(K,L) family DP on the target-dominance language: CLOSED;
  * finite carry quotient Z_t mod 3^(L-t): CLOSED;
  * horizon-independent bound on the number of carry states: OPEN;
  * universal Route-B membership / Collatz: OPEN.
"""

from functools import lru_cache
from fractions import Fraction
from itertools import combinations

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


def correction_from_positions(pos):
    q = len(pos)
    return sum((3 ** (q - 1 - i)) * (1 << b) for i, b in enumerate(pos))


TARGET = threshold_word(N)
A = tuple(i for i, bit in enumerate(TARGET) if bit)
Q = len(A)
TARGET_C = correction_from_positions(A)

assert TARGET == (1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1)
assert A == (0, 1, 3, 4, 6, 7, 9, 11, 12, 14, 15, 17)
assert Q == 12


def prefix_target_ones(K: int) -> int:
    return sum(a < K for a in A)


@lru_cache(None)
def prefix_count(K: int, rcount: int, upper_exclusive: int) -> int:
    """Count legal first `rcount` one positions below `upper_exclusive`.

    The candidate must satisfy b_i <= a_i and binary prefix equality through
    positions 0,...,K-1.  Hence all target ones before K are fixed, while every
    later candidate one is constrained to position >= K.
    """
    if rcount == 0:
        return 1

    p = prefix_target_ones(K)
    i = rcount - 1

    if i < p:
        b = A[i]
        if b >= upper_exclusive:
            return 0
        return prefix_count(K, rcount - 1, b)

    lo = max(i, K)
    hi = min(A[i], upper_exclusive - 1)
    if lo > hi:
        return 0

    return sum(prefix_count(K, rcount - 1, b) for b in range(lo, hi + 1))


def family_collision_count(K: int, L: int) -> int:
    """Count target-dominance candidates with 2^K 3^L | Delta.

    The target itself is included.  The ternary sector uses only the quotient
    carry z = Z_t mod 3^(L-t); the exact correction is never stored.
    """
    assert 1 <= K <= N
    assert L >= 1

    p = prefix_target_ones(K)

    @lru_cache(None)
    def rec(t: int, next_b: int, z: int) -> int:
        # r is the next one-rank to choose, counted from zero on the left.
        r = Q - 1 - t

        # If all requested ternary digits have been lifted, unseen earlier
        # ranks have coefficients divisible by 3^L and can be counted in one
        # prefix-family call.
        if t == L:
            return prefix_count(K, r + 1, next_b)

        # If all q one-ranks are exhausted before L, Delta = 3^q Z_q exactly;
        # the remaining ternary condition is simply Z_q == 0 mod 3^(L-q).
        if r < 0:
            modulus = 3 ** (L - t)
            return 1 if z % modulus == 0 else 0

        m = L - t
        modulus = 3 ** m
        next_modulus = 3 ** (m - 1)
        assert 0 <= z < modulus

        if r < p:
            candidates = (A[r],)
        else:
            lo = max(r, K)
            hi = min(A[r], next_b - 1)
            candidates = range(lo, hi + 1) if lo <= hi else ()

        total = 0
        for b in candidates:
            if b >= next_b:
                continue

            atom = ((1 << A[r]) - (1 << b)) % modulus
            s = z + atom
            if s % 3:
                continue

            z_next = (s // 3) % next_modulus if next_modulus > 1 else 0
            total += rec(t + 1, b, z_next)

        return total

    return rec(0, N, 0)


# ---------------------------------------------------------------------------
# 1. Candidate-language count without 2^N word enumeration.
# ---------------------------------------------------------------------------

assert prefix_count(1, Q, N) == 2_652


# ---------------------------------------------------------------------------
# 2. Reproduce the existing K=1 adaptive ternary survivor path.
#    Counts below include the target, so subtract one to compare with the
#    previously reported number of *other* colliders.
# ---------------------------------------------------------------------------

EXPECTED_OTHER = (1498, 960, 476, 180, 85, 30, 12, 6, 2, 1, 0)
FAMILY_COUNTS = tuple(family_collision_count(1, L) for L in range(1, 12))
assert tuple(x - 1 for x in FAMILY_COUNTS) == EXPECTED_OTHER


# ---------------------------------------------------------------------------
# 3. Independent direct regression on the 2,652 dominance candidates.
#    This is only a finite audit of the implementation; the carry recurrence
#    above is algebraic and does not rely on this enumeration.
# ---------------------------------------------------------------------------

DOMINANCE = []
for pos in combinations(range(N), Q):
    if all(pos[i] <= A[i] for i in range(Q)):
        DOMINANCE.append((pos, correction_from_positions(pos)))

assert len(DOMINANCE) == 2_652
assert sum(pos == A for pos, _ in DOMINANCE) == 1

regression_checks = 0
for K in range(1, 8):
    for L in range(1, 13):
        modulus = (1 << K) * (3 ** L)
        direct = sum((C - TARGET_C) % modulus == 0 for _, C in DOMINANCE)
        via_family = family_collision_count(K, L)
        assert via_family == direct
        regression_checks += 1

assert regression_checks == 84


# ---------------------------------------------------------------------------
# 4. Exact right-tail locality witness.
# ---------------------------------------------------------------------------

# For L <= q, only the last L ranked one positions enter the ternary carry.
# Earlier ranks are counted by `prefix_count` after the L-th lift.  The final
# singleton at L=11 reproduces the existing target-specific ternary barrier.
assert FAMILY_COUNTS[-1] == 1

print("PASS A0 s=1 Route-B ternary suffix-carry family DP certificate")
print("target_length", N)
print("target_ones", Q)
print("target_positions", A)
print("dominance_candidates_via_prefix_dp", prefix_count(1, Q, N))
print("family_counts_including_target_L1_to_L11", FAMILY_COUNTS)
print("other_colliders_L1_to_L11", tuple(x - 1 for x in FAMILY_COUNTS))
print("direct_regression_checks", regression_checks)
print(
    "carry_state",
    "Z_t mod 3^(L-t), with Z_{t+1}=(Z_t+2^a-2^b)/3 after a divisible-by-3 lift",
)
print(
    "locality",
    "for L<=q, ternary collision depends only on the last L ranked one positions; the entire earlier family is counted without expansion",
)
print(
    "formation_audit",
    "the candidate language is fixed before observation refinement; K changes only the fixed target-prefix gate and L changes only carry precision",
)
print(
    "axis_audit",
    "dyadic prefix equality and ternary right-tail carry remain separate directed observation axes",
)
print(
    "dsd_audit",
    "exact family DP replaces leaf enumeration at fixed resolution, but no horizon-independent carry-state bound is inferred",
)
print(
    "status",
    "fixed-(K,L) target-dominance family collision DP CLOSED; carry-state globalization remains OPEN",
)
