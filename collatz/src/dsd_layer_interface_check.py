#!/usr/bin/env python3
"""Exact audit for the DSD-layer interface used by the Collatz notes.

This checker does *not* model the Formation Axiom System or the realized-axis
axioms themselves.  It checks only the downstream arithmetic claims made by
`2026-08-09-dsd-layer-interface-spec.md`:

1. indexed E/O occurrences aggregate to the count vector (e,q);
2. the multiplicative character determined by that aggregate is 3^q/2^h;
3. the affine cocycle retains order through R(w);
4. words with the same count vector can have different corrections;
5. the exact two-term formula agrees with direct accelerated Collatz iteration.

All arithmetic checks use fractions/integers only.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def accelerated_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def counts(word: tuple[int, ...]) -> tuple[int, int]:
    q = sum(word)
    return len(word) - q, q


def static_character(word: tuple[int, ...]) -> Fraction:
    """Downstream multiplicative character from the E/O occurrence aggregate."""
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
        if bit == 0:  # E after current map
            a, b = a / 2, b / 2
        else:  # O after current map
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
            _, q = counts(word)
            R = correction(word)
            rhs = Fraction(3**q * n + R, 2**h)
            assert rhs.denominator == 1
            assert rhs.numerator == iterate(n, h)


def audit_compression_obstruction() -> None:
    # Chronological E,O versus O,E.  Same count vector and character; different R.
    EO = (0, 1)
    OE = (1, 0)
    assert counts(EO) == counts(OE) == (1, 1)
    assert static_character(EO) == static_character(OE) == Fraction(3, 4)
    assert correction(EO) != correction(OE)
    assert affine_pair(EO)[1] != affine_pair(OE)[1]


def main() -> None:
    audit_words()
    audit_actual_orbits()
    audit_compression_obstruction()
    print("DSD/Collatz layer-interface arithmetic audit: PASS")


if __name__ == "__main__":
    main()
