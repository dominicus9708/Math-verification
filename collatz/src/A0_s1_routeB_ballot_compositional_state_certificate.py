#!/usr/bin/env python3
"""Exact compositional ballot-state certificate for A0 s=1 Route-B.

For alpha = R/J and a binary word W, let q_W(u) be the number of ones in
its first u symbols and define

    d_W(u) = q_W(u) - floor(R u / J).

The existing Route-B ballot_summary records

    b(W) = min(0, min_u d_W(u))

and a critical prefix c(W) among minimizers, chosen by largest fractional
phase (R u mod J), with the earlier prefix retained on an exact phase tie.

The subtle point is concatenation: floor(R(h+u)/J) has a carry.  This
certificate implements the exact carry-aware composition law and checks it
against direct scans.

It also checks a compressed ballot-evolution state

    B(W) = (e, r, b, g)

where
    e = q(W) - floor(R h(W)/J),
    r = R h(W) mod J,
    g = R c(W) mod J.

B(W) is sufficient to propagate endpoint discrepancy, phase, ballot minimum,
and critical phase under concatenation.  It does NOT recover the literal
critical-prefix index c(W); any certificate that uses the absolute index must
retain c(W) itself.
"""

from dataclasses import dataclass
from itertools import product
from math import gcd

TARGET_J = 10_439_860_591
TARGET_R = 6_586_818_670


@dataclass(frozen=True)
class FullBallotState:
    h: int
    q: int
    b: int
    c: int


@dataclass(frozen=True)
class PhaseBallotState:
    e: int
    r: int
    b: int
    g: int


def phase(n: int, R: int, J: int) -> int:
    return (R * n) % J


def carry(a: int, b: int, J: int) -> int:
    return int(a + b >= J)


def direct_full(word: tuple[int, ...], R: int, J: int) -> FullBallotState:
    q = 0
    b = 0
    c = 0
    for u, bit in enumerate(word, start=1):
        q += bit
        d = q - (R * u) // J
        if d < b:
            b = d
            c = u
        elif d == b and phase(u, R, J) > phase(c, R, J):
            c = u
    return FullBallotState(len(word), q, b, c)


def full_to_phase(s: FullBallotState, R: int, J: int) -> PhaseBallotState:
    e = s.q - (R * s.h) // J
    return PhaseBallotState(e, phase(s.h, R, J), s.b, phase(s.c, R, J))


def compose_full(
    A: FullBallotState,
    B: FullBallotState,
    R: int,
    J: int,
) -> FullBallotState:
    """Exact state of UV from exact states of U and V."""
    eA = A.q - (R * A.h) // J
    rA = phase(A.h, R, J)
    gB = phase(B.c, R, J)

    # Minimum attained among prefixes h(A)+v, including v=0.
    suffix_b = eA + B.b - carry(rA, gB, J)
    suffix_c = A.h + B.c

    if A.b < suffix_b:
        b = A.b
        c = A.c
    elif suffix_b < A.b:
        b = suffix_b
        c = suffix_c
    else:
        # U prefixes are encountered first.  On an exact phase tie, preserve
        # the earlier U critical prefix exactly as direct ballot_summary does.
        if phase(suffix_c, R, J) > phase(A.c, R, J):
            b = suffix_b
            c = suffix_c
        else:
            b = A.b
            c = A.c

    return FullBallotState(A.h + B.h, A.q + B.q, b, c)


def compose_phase(
    A: PhaseBallotState,
    B: PhaseBallotState,
    J: int,
) -> PhaseBallotState:
    """Exact propagated ballot evolution, with critical phase but not index."""
    e = A.e + B.e - carry(A.r, B.r, J)
    r = (A.r + B.r) % J

    suffix_b = A.e + B.b - carry(A.r, B.g, J)
    suffix_g = (A.r + B.g) % J

    if A.b < suffix_b:
        b = A.b
        g = A.g
    elif suffix_b < A.b:
        b = suffix_b
        g = suffix_g
    else:
        b = A.b
        g = max(A.g, suffix_g)

    return PhaseBallotState(e, r, b, g)


def words(n: int):
    for bits in product((0, 1), repeat=n):
        yield bits


def regression(R: int, J: int, max_total_len: int = 8) -> tuple[int, int]:
    assert 0 < R < J
    assert gcd(R, J) == 1

    direct_checks = 0
    phase_checks = 0

    cache = {
        n: [(w, direct_full(w, R, J)) for w in words(n)]
        for n in range(max_total_len + 1)
    }

    for a in range(max_total_len + 1):
        for b in range(max_total_len + 1 - a):
            for U, AU in cache[a]:
                PA = full_to_phase(AU, R, J)
                for V, BV in cache[b]:
                    PB = full_to_phase(BV, R, J)

                    expected = direct_full(U + V, R, J)
                    got_full = compose_full(AU, BV, R, J)
                    assert got_full == expected
                    direct_checks += 1

                    expected_phase = full_to_phase(expected, R, J)
                    got_phase = compose_phase(PA, PB, J)
                    assert got_phase == expected_phase
                    phase_checks += 1

    return direct_checks, phase_checks


SLOPES = (
    (TARGET_R, TARGET_J),
    (2, 3),
    (3, 5),
    (5, 8),
    (4, 7),
    (7, 11),
)

total_full = 0
total_phase = 0
for R, J in SLOPES:
    full_checks, phase_checks = regression(R, J)
    assert full_checks == 4097
    assert phase_checks == 4097
    total_full += full_checks
    total_phase += phase_checks

assert total_full == 24_582
assert total_phase == 24_582

print("PASS A0 s=1 Route-B exact compositional ballot-state certificate")
print("slopes", len(SLOPES))
print("full_summary_composition_checks", total_full)
print("phase_state_composition_checks", total_phase)
print(
    "exact_state",
    "(h,q,base_min,critical) composes with the rational-floor carry included",
)
print(
    "compressed_state",
    "(endpoint_discrepancy,length_phase,base_min,critical_phase) "
    "propagates exact ballot evolution",
)
print(
    "scope_audit",
    "critical phase does not reconstruct the literal critical-prefix index",
)
print(
    "dsd_audit",
    "exact compositionality is proved algebraically; finite regressions are guards, "
    "not the proof and not global Route-B membership",
)
