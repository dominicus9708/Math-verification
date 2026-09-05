#!/usr/bin/env python3
"""Regression certificate for exact valuation-tuple macroblock compilation.

A valuation tuple (a1,...,ad) emits the fixed parity block

    B = 0^a1 1 0^a2 1 ... 0^ad 1.

For an exact source channel

    X = r + 2^h m,
    T^h(X) = y + 3^q m,

the existing bitwise refinement and one exact multibit transition must produce
identical child channels and identical parameter intervals.

The theorem is algebraic uniqueness of the required m residue modulo 2^|B|.
The finite checks below are regression guards.
"""

from itertools import product


def T(x: int) -> int:
    assert x >= 0
    return (3*x + 1)//2 if x & 1 else x//2


def orbit_prefix(x: int, h: int):
    bits = []
    for _ in range(h):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


def correction(bits):
    pos = [i for i, b in enumerate(bits) if b]
    q = len(pos)
    return sum((3 ** (q-r-1)) * (1 << a)
               for r, a in enumerate(pos))


def refine_channel(state, bit: int):
    h, r, y, q = state
    assert bit in (0, 1)
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        numer = y + (3 ** q) * m0
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q
    else:
        numer = 3*y + (3 ** (q+1))*m0 + 1
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q + 1
    return h+1, r2, y2, q2


def build_channel(bits):
    st = (0, 0, 0, 0)
    for bit in bits:
        st = refine_channel(st, bit)
    return st


def macro_bits(vals):
    out = []
    for a in vals:
        assert a >= 0
        out.extend((0,) * a)
        out.append(1)
    return tuple(out)


def macro_child(state, bits):
    h, r, y, q = state
    b = len(bits)
    p = sum(bits)
    assert b >= 1
    M = 1 << b
    gamma = correction(bits)
    unit = pow(3, q+p, M)
    m0 = (-(pow(3, p) * y + gamma) * pow(unit, -1, M)) % M
    numer = pow(3, p) * y + gamma + pow(3, q+p) * m0
    assert numer % M == 0
    return (h+b, r + (m0 << h), numer//M, q+p), m0


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a)//b)


def sequential_interval(state, bits, lo, hi):
    st = state
    for bit in bits:
        h, r, y, q = st
        m0 = (bit - (y & 1)) & 1
        lo = ceil_div(lo-m0, 2)
        hi = (hi-m0)//2
        st = refine_channel(st, bit)
    return st, lo, hi


# Prefix channels used as varied affine entrances.
prefix_states = []
for h in range(0, 6):
    for pref in product((0, 1), repeat=h):
        prefix_states.append((pref, build_channel(pref)))

checked = 0
interval_checked = 0
for pref, state in prefix_states:
    for d in range(1, 5):
        for vals in product(range(4), repeat=d):
            bits = macro_bits(vals)

            # Bitwise channel transition.
            seq = state
            for bit in bits:
                seq = refine_channel(seq, bit)

            # One compiled multibit transition.
            mac, m0 = macro_child(state, bits)
            assert seq == mac

            # The compiled residue realizes exactly the supplied block for
            # several lifts in the resulting source cylinder.
            h2, r2, y2, q2 = mac
            for k in range(4):
                X = r2 + (1 << h2) * k
                got_bits, endpoint = orbit_prefix(X, h2)
                assert got_bits == pref + bits
                assert endpoint == y2 + (3 ** q2) * k

            # Exact interval composition agrees with sequential one-bit
            # reparameterization.
            for lo, hi in ((0, 0), (0, 17), (3, 31), (-7, 22)):
                st_i, lo_i, hi_i = sequential_interval(state, bits, lo, hi)
                assert st_i == mac
                M = 1 << len(bits)
                want_lo = ceil_div(lo-m0, M)
                want_hi = (hi-m0)//M
                assert (lo_i, hi_i) == (want_lo, want_hi)
                interval_checked += 1

            checked += 1

print("PASS A0 s=1 valuation macroblock compilation certificate")
print("entrance_channels", len(prefix_states))
print("valuation_tuple_depth_max", 4)
print("zero_run_value_max", 3)
print("macroblocks_checked", checked)
print("interval_compositions_checked", interval_checked)
print("equivalence", "sequential valuation/bit refinement == one multibit block transition")
print("source_payload_merge_claimed", False)
print("status", "EXACT transition-equivalence theorem; finite checks are regression evidence")
