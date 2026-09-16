#!/usr/bin/env python3
"""Exact audit for the DSD-layer interface used by the Collatz notes.

This checker does *not* prove or implement the Formation Axiom System or the
realized-axis axioms.  It tests the finite application interface after those
types have been supplied:

1. each parity occurrence is represented by a distinct occurrence-channel tag;
2. many distinct occurrence channels may realize the same E or O bookkeeping line;
3. channel-indexed static terms compose to the count vector (e,q);
4. the multiplicative character determined by that aggregate is 3^q/2^h;
5. the affine cocycle retains order through R(w);
6. words with the same count vector can have different corrections;
7. the exact two-term formula agrees with direct accelerated Collatz iteration.

All arithmetic checks use fractions/integers only.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Channel = tuple[int, int]  # (occurrence index, parity bit)


def accelerated_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def occurrence_channels(word: tuple[int, ...]) -> tuple[Channel, ...]:
    """Application-level distinct tags c_j for one fixed finite parity trace."""
    return tuple((j, bit) for j, bit in enumerate(word))


def axis_line(channel: Channel) -> str:
    """Two realized bookkeeping lines; distinct tags may share one line."""
    _, bit = channel
    return "ell_O" if bit else "ell_E"


def static_term(channel: Channel) -> tuple[int, int]:
    """Singleton channel realization in the separate aggregation term space."""
    _, bit = channel
    return (0, 1) if bit else (1, 0)


def static_compose(channels: tuple[Channel, ...]) -> tuple[int, int]:
    e = 0
    q = 0
    for channel in channels:
        de, dq = static_term(channel)
        e += de
        q += dq
    return e, q


def counts(word: tuple[int, ...]) -> tuple[int, int]:
    q = sum(word)
    return len(word) - q, q


def static_character(word: tuple[int, ...]) -> Fraction:
    """Downstream multiplicative character from the E/O static aggregate."""
    e, q = counts(word)
    return Fraction(3**q, 2 ** (e + q))


def correction(word: tuple[int, ...]) -> int:
    """Exact order-sensitive Collatz correction R(w)."""
    odd_positions = [j for j, bit in enumerate(word) if bit]
    q = len(odd_positions)
    return sum((2**d) * (3 ** (q - 1 - i)) for i, d in enumerate(odd_positions))


def affine_pair(word: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Return (a,b) for F_w(n)=a*n+b by exact chronological composition."""
    a = Fraction(1, 1)
    b = Fraction(0, 1)
    for bit in word:
        if bit == 0:
            a, b = a / 2, b / 2
        else:
            a, b = 3 * a / 2, (3 * b + 1) / 2
    return a, b


def word_for_start(n: int, h: int) -> tuple[int, ...]:
    bits = []
    x = n
    for _ in range(h):
        bits.append(x & 1)
        x = accelerated_step(x)
    return tuple(bits)


def iterate(n: int, h: int) -> int:
    x = n
    for _ in range(h):
        x = accelerated_step(x)
    return x


def audit_words(max_h: int = 10) -> None:
    for h in range(max_h + 1):
        for word in product((0, 1), repeat=h):
            channels = occurrence_channels(word)

            # Literal static-aggregation support: one distinct channel per occurrence.
            assert len(channels) == h
            assert len(set(channels)) == h
            assert static_compose(channels) == counts(word)

            # Channel multiplicity is not realized-axis rank.
            realized_lines = {axis_line(c) for c in channels}
            expected_rank = 0 if h == 0 else (1 if len(set(word)) == 1 else 2)
            assert len(realized_lines) == expected_rank

            e, q = counts(word)
            chi = static_character(word)
            assert chi == Fraction(3**q, 2**h)

            a, b = affine_pair(word)
            R = correction(word)
            assert a == chi
            assert b == Fraction(R, 2**h)


def audit_actual_orbits(max_n: int = 200, max_h: int = 20) -> None:
    for n in range(1, max_n + 1):
        for h in range(max_h + 1):
            word = word_for_start(n, h)
            channels = occurrence_channels(word)
            assert static_compose(channels) == counts(word)

            _, q = counts(word)
            R = correction(word)
            rhs = Fraction(3**q * n + R, 2**h)
            assert rhs.denominator == 1
            assert rhs.numerator == iterate(n, h)


def audit_compression_obstruction() -> None:
    # Chronological E,O versus O,E. Same static aggregate; different order cocycle.
    EO = (0, 1)
    OE = (1, 0)
    assert counts(EO) == counts(OE) == (1, 1)
    assert static_compose(occurrence_channels(EO)) == (1, 1)
    assert static_compose(occurrence_channels(OE)) == (1, 1)
    assert static_character(EO) == static_character(OE) == Fraction(3, 4)
    assert correction(EO) == 2
    assert correction(OE) == 1
    assert affine_pair(EO)[1] == Fraction(1, 2)
    assert affine_pair(OE)[1] == Fraction(1, 4)


def main() -> None:
    audit_words()
    audit_actual_orbits()
    audit_compression_obstruction()
    print("DSD/Collatz layer-interface arithmetic audit: PASS")


if __name__ == "__main__":
    main()
