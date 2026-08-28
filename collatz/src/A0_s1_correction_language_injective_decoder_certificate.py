#!/usr/bin/env python3
"""Exact regression certificate for the fixed-(h,q) correction language.

For a length-h accelerated-Collatz parity word with odd positions

    0 <= a_1 < ... < a_q < h,

define

    C = sum_{r=1}^q 3^(q-r) 2^(a_r).

Then the exact affine identity is

    2^h T^h(x) = 3^q x + C.

At fixed h and q, C determines the parity word uniquely.  More strongly,
C mod 2^h already determines the unique start address mod 2^h, while the
ordinary correction can be decoded deterministically from the left:

    C_0 = C,
    a_r = v_2(C_{r-1}),
    C_r = C_{r-1} - 3^(q-r) 2^(a_r).

For a genuine correction this returns the strictly increasing odd positions
and terminates at C_q=0.

The exhaustive checks below are finite regressions only; the theorem is the
algebraic valuation argument above.  No statement about full A0 extension or
the Collatz conjecture is made.
"""

from itertools import combinations, product


def correction_from_positions(h, positions):
    q = len(positions)
    assert all(0 <= a < h for a in positions)
    assert list(positions) == sorted(set(positions))
    return sum((3 ** (q - r - 1)) * (1 << a) for r, a in enumerate(positions))


def correction_from_bits(bits):
    positions = [i for i, b in enumerate(bits) if b]
    return correction_from_positions(len(bits), positions)


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def decode_correction(C, q):
    positions = []
    rem = C
    for r in range(1, q + 1):
        if rem <= 0:
            return None
        a = v2(rem)
        if positions and a <= positions[-1]:
            return None
        positions.append(a)
        rem -= (3 ** (q - r)) * (1 << a)
    if rem != 0:
        return None
    return tuple(positions)


def parity_address(bits):
    h = len(bits)
    q = sum(bits)
    C = correction_from_bits(bits)
    return (-C * pow(3 ** q, -1, 1 << h)) % (1 << h)


def actual_parity_word(x, h):
    out = []
    for _ in range(h):
        eps = x & 1
        out.append(eps)
        x = (3 * x + 1) // 2 if eps else x // 2
    return tuple(out)


# Exhaustive fixed-(h,q) injectivity and exact decoder regression.
for h in range(1, 13):
    for q in range(h + 1):
        seen_C = {}
        seen_C_mod = {}
        for positions in combinations(range(h), q):
            C = correction_from_positions(h, positions)
            if q == 0:
                assert C == 0
                assert positions == ()
            else:
                assert decode_correction(C, q) == positions

            # Ordinary corrections are injective.
            assert C not in seen_C
            seen_C[C] = positions

            # At fixed q, even the residue C mod 2^h is injective, because it
            # is equivalent to the unique parity start address modulo 2^h.
            cmod = C % (1 << h)
            assert cmod not in seen_C_mod
            seen_C_mod[cmod] = positions

# Exhaustive parity-address realization regression through depth 12.
for h in range(1, 13):
    addresses = set()
    for bits in product((0, 1), repeat=h):
        x = parity_address(bits)
        assert actual_parity_word(x, h) == bits
        addresses.add(x)
    assert len(addresses) == (1 << h)

# Exact concatenation law regression:
# C(uv) = 3^{q(v)} C(u) + 2^{|u|} C(v).
for a in range(0, 6):
    for b in range(0, 6):
        for u in product((0, 1), repeat=a):
            Cu = correction_from_bits(u)
            for v in product((0, 1), repeat=b):
                Cv = correction_from_bits(v)
                Cuv = correction_from_bits(u + v)
                assert Cuv == (3 ** sum(v)) * Cu + (1 << a) * Cv

print("PASS fixed-(h,q) correction-language injective decoder certificate")
print("decoder", "a_r = v2(remainder), subtract weighted atom, repeat")
print("fixed_q_C_mod_2h_injective", True)
print("concatenation_law", "C(uv)=3^q(v) C(u)+2^|u| C(v)")
print("exhaustive_regression_h_max", 12)
