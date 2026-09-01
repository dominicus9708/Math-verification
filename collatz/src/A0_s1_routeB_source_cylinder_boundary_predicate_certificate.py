#!/usr/bin/env python3
"""Exact source-cylinder boundary predicate quotient for A0 s=1 Route-B.

A source channel has the exact affine form

    X = r + 2^h m,
    T^h(X) = y + 3^q m.

Fix requested boundary resolutions K,L.  If h >= K and q >= L, then for
EVERY integer parameter m,

    X mod 2^K       = r mod 2^K,
    T^h(X) mod 3^L  = y mod 3^L.

Therefore a two-sided boundary predicate

    X == a (mod 2^K)  and  T^h(X) == b (mod 3^L)

is constant on the entire source-cylinder interval.  A mismatch closes the
whole interval at once; a match discharges those boundary coordinates for the
whole interval.  No singleton expansion is needed for these gates.

This is a predicate-relative quotient.  It does NOT identify exact source
transducer states with different y mod 2^d, and it does NOT prove interior
correction-language / ballot membership.
"""

from itertools import product


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def refine_channel(state, bit: int):
    h, r, y, q = state
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        y2 = (y + (3 ** q) * m0) // 2
        q2 = q
    else:
        y2 = (3 * y + (3 ** (q + 1)) * m0 + 1) // 2
        q2 = q + 1
    return h + 1, r2, y2, q2


def channel(bits):
    s = (0, 0, 0, 0)
    for bit in bits:
        s = refine_channel(s, bit)
    return s


def orbit(x: int, h: int):
    for _ in range(h):
        x = T(x)
    return x


# Exhaustive finite regression over small cylinders.  The proof is the two
# displayed divisibility identities above; these checks only guard indexing.
checks = 0
for h in range(1, 9):
    for bits in product((0, 1), repeat=h):
        sh, r, y, q = channel(bits)
        assert sh == h
        for K in range(1, h + 1):
            mod2 = 1 << K
            for L in range(0, q + 1):
                mod3 = 3 ** L
                for m in range(-4, 5):
                    X = r + (1 << h) * m
                    # Restrict direct Collatz regression to nonnegative X.
                    if X < 0:
                        continue
                    endpoint = orbit(X, h)
                    assert endpoint == y + (3 ** q) * m
                    assert X % mod2 == r % mod2
                    assert endpoint % mod3 == y % mod3
                    checks += 1

print("PASS A0 s=1 Route-B source-cylinder boundary predicate certificate")
print("regression_checks", checks)
print("exact_gate", "h>=K fixes X mod 2^K on the entire source cylinder")
print("exact_endpoint_gate", "q>=L fixes T^h(X) mod 3^L on the entire source cylinder")
print("closure", "boundary mismatch prunes the whole interval; boundary match discharges both requested coordinates")
print("dsd_audit", "predicate-relative quotient only; interior correction/ballot membership remains open")
