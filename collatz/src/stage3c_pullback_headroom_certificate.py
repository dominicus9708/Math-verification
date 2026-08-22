#!/usr/bin/env python3
"""Exact finite certificate for the corrected Stage 3C local-minimality rule.

The previous Stage 3C note used the valid local identity

    R_u - R_w = 3^q Delta > 0

and observed that starting the larger-correction word u at x-Delta merges with
word w started at x after the same L steps.  For a *later* block of a minimal
counterexample N, however, x is generally only known to satisfy x>=N.  Thus
x-Delta<x does not by itself contradict minimality.  The local reduction is a
minimality contradiction only when x-Delta<N, equivalently

    Delta > x-N.

This certificate enumerates the full L=7 cube, reconstructs the full-Hensel
classes, verifies the local merge identity exactly, and records the finite
headroom-conditioned language.

This is a structural audit/correction, not a proof of the Collatz conjecture.
"""

from itertools import product

L = 7
EXPECTED_COUNTS = (1, 2, 6, 15, 21, 16, 7, 1)
EXPECTED_DEFICITS = {1, 2, 4, 5, 8, 10, 16, 17, 20, 21}
EXPECTED_HEADROOM = {0: 69, 1: 93, 2: 106, 5: 118, 21: 128}


def correction(bits):
    R = 0
    q = 0
    for i, b in enumerate(bits):
        if b:
            R = 3 * R + (1 << i)
            q += 1
    return q, R


def v3(n):
    a = 0
    while n and n % 3 == 0:
        n //= 3
        a += 1
    return a


def main():
    p3 = [1]
    for _ in range(L):
        p3.append(3 * p3[-1])

    classes = [{} for _ in range(L + 1)]
    words = []
    for bits in product((0, 1), repeat=L):
        q, R = correction(bits)
        key = R % p3[q]
        words.append((bits, q, R, key))
        classes[q].setdefault(key, []).append((R, bits))

    assert tuple(len(c) for c in classes) == EXPECTED_COUNTS

    maxima = [{} for _ in range(L + 1)]
    for q, cls in enumerate(classes):
        for key, vals in cls.items():
            maxima[q][key] = max(R for R, _ in vals)

    deficits = []
    for bits, q, R, key in words:
        Rmax = maxima[q][key]
        diff = Rmax - R
        assert diff % p3[q] == 0
        Delta = diff // p3[q]

        # Exact local merge identity after multiplication by 2^L:
        # 3^q (x-Delta) + Rmax == 3^q x + R.
        assert -p3[q] * Delta + Rmax == R
        deficits.append((bits, q, R, key, Delta))

    positive = {Delta for *_, Delta in deficits if Delta > 0}
    assert positive == EXPECTED_DEFICITS
    assert max(positive) == 21

    valuations = {Delta: v3(Delta) for Delta in positive}
    assert valuations == {
        1: 0,
        2: 0,
        4: 0,
        5: 0,
        8: 0,
        10: 0,
        16: 0,
        17: 0,
        20: 0,
        21: 1,
    }

    for h, expected in EXPECTED_HEADROOM.items():
        allowed = sum(Delta <= h for *_, Delta in deficits)
        assert allowed == expected, (h, allowed, expected)

    print("L7 class counts", EXPECTED_COUNTS)
    print("positive local deficits", sorted(positive))
    print("headroom allowed word counts", EXPECTED_HEADROOM)
    print("v3 deficits", {d: valuations[d] for d in sorted(valuations)})
    print("corrected minimality rule: Delta is contradictory only when Delta > x-N")
    print("stage3c pullback/headroom certificate: PASS")


if __name__ == "__main__":
    main()
