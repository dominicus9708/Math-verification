#!/usr/bin/env python3
"""Finite regression for the exact singleton record-macro classification.

The companion note proves:

1. a record first-passage language is singleton iff the mechanical prefix
   d_1...d_(L-1) contains no 10;
2. the Beatty mechanical word has no 00 and no 111;
3. therefore every singleton record macro has L<=4;
4. after at most one singleton macro, an all-singleton continuation has
   parity bits all equal to one.

This script checks the finite transfer consequences on exact integer barriers.
It is a regression certificate for the elementary all-length proofs in the
note; it is not itself the proof and not a proof of Collatz.
"""

from __future__ import annotations


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(5000)


def mechanical_word(s: int, L: int) -> tuple[int, ...]:
    return tuple(B[s + j] - B[s + j - 1] for j in range(1, L + 1))


def record_words(s: int, L: int) -> list[tuple[int, ...]]:
    D = [B[s + j] - B[s] for j in range(L + 1)]
    out: list[tuple[int, ...]] = []

    def rec(j: int, q: int, bits: list[int]) -> None:
        if j == L:
            if q == D[L] + 1:
                out.append(tuple(bits))
            return

        jj = j + 1
        for bit in (0, 1):
            qq = q + bit
            if jj < L:
                if qq <= D[jj]:
                    rec(jj, qq, bits + [bit])
            elif qq == D[L] + 1:
                rec(jj, qq, bits + [bit])

    rec(0, 0, [])
    return out


def contains_10(bits: tuple[int, ...]) -> bool:
    return any(bits[i] == 1 and bits[i + 1] == 0
               for i in range(len(bits) - 1))


def main() -> None:
    # Mechanical local forbidden words, checked on a broad exact grid.
    for s in range(2000):
        assert mechanical_word(s, 2) != (0, 0)
        assert mechanical_word(s, 3) != (1, 1, 1)

    singleton_shapes: set[tuple[int, ...]] = set()

    # Exact singleton equivalence on all sampled Sturmian factors through L=20.
    # The all-length equivalence is proved in the note by the local 10->01 swap.
    for L in range(1, 21):
        seen: set[tuple[int, ...]] = set()
        for s in range(3000):
            d = mechanical_word(s, L)
            if d in seen:
                continue
            seen.add(d)
            words = record_words(s, L)
            if not words:
                continue

            singleton = len(words) == 1
            criterion = not contains_10(d[:-1])
            assert singleton == criterion, (s, L, d, len(words))

            if singleton:
                singleton_shapes.add(d)
                assert L <= 4, (s, L, d)
                # Unique record word equals the boundary prefix plus a final 1.
                assert words[0][:-1] == d[:-1]
                assert d[-1] == 0 and words[0][-1] == 1

    expected_shapes = {
        (0,),
        (1, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 1, 1, 0),
    }
    assert singleton_shapes == expected_shapes, singleton_shapes

    # If a singleton macro ends at a mechanical zero, the next mechanical bit
    # is one. Any following singleton prefix with no 10 therefore starts in a
    # one-run and its unique parity word is all ones. Check this exhaustively
    # over sampled phases and all singleton continuations.
    for s in range(2000):
        for L in range(1, 5):
            w = record_words(s, L)
            if len(w) != 1:
                continue
            s2 = s + L
            assert mechanical_word(s2, 1) == (1,), (s, L, s2)
            for L2 in range(1, 5):
                w2 = record_words(s2, L2)
                if len(w2) == 1:
                    assert all(bit == 1 for bit in w2[0]), (s2, L2, w2[0])

    # Direct all-odd integrality identity on a finite grid.
    for x in range(1, 500):
        y = x
        k = 0
        while y & 1 and k < 20:
            k += 1
            assert (x + 1) % (1 << k) == 0
            y = (3 * y + 1) // 2

    print("record singleton macro classification regression: PASS")
    print("singleton_shapes", sorted("".join(map(str, d)) for d in singleton_shapes))
    print("maximum_singleton_length", max(map(len, singleton_shapes)))


if __name__ == "__main__":
    main()
