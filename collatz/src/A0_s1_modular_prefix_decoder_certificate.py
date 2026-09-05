#!/usr/bin/env python3
"""Exact target-aware modular prefix decoder for A0 s=1.

For a fixed length-t, odd-count-j correction

    C = sum_{r=1}^j 3^(j-r) 2^(a_r),

and an endpoint bridge

    2^t Z = 3^j X + C,

fix any shallow depth h <= t.  Modulo 2^h,

    C == -3^j X                 (mod 2^h),

because 2^t Z vanishes.  Therefore the odd positions a_r<h can be decoded
without materializing C and without knowing Z.

Let R_0 = C mod 2^h.  Repeatedly:

    a_r = v2(R_{r-1}),
    R_r = R_{r-1} - 3^(j-r) 2^(a_r)   (mod 2^h).

Every term with a>=h is zero modulo 2^h.  Among the surviving terms the
least position has an odd coefficient plus an even tail, so its 2-adic
valuation is exactly that least position.  The process terminates at zero
after recovering precisely all a_r<h.

For the A0 s=1 target this supplies an exact prefix-ballot oracle from X
alone:

    C_req mod 2^h = -3^j0 X mod 2^h.

It is a local necessary-condition oracle; the full long bridge and C4F
formation conditions remain open.
"""

from itertools import product
from math import gcd

T0 = 104_398_605_910
J0_ODD = 65_868_186_701


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def ceil_alpha_n(n: int) -> int:
    """Exact ceil(n log_3 2), via powers 2 and 3."""
    assert n >= 0
    if n == 0:
        return 0
    p3 = 1
    k = 0
    target = 1 << n
    while p3 <= target:
        p3 *= 3
        k += 1
    return k


def correction_from_bits(bits):
    positions = [i for i, b in enumerate(bits) if b]
    j = len(positions)
    return sum((3 ** (j-r-1)) * (1 << a)
               for r, a in enumerate(positions))


def parity_address(bits):
    h = len(bits)
    j = sum(bits)
    C = correction_from_bits(bits)
    if h == 0:
        return 0
    return (-C * pow(3 ** j, -1, 1 << h)) % (1 << h)


def decode_positions_below_h_from_X(X: int, j: int, h: int):
    """Decode all correction odd positions <h from X, total j, and depth h."""
    assert j >= 0
    assert h >= 1
    M = 1 << h
    rem = (-pow(3, j, M) * (X % M)) % M
    out = []
    r = 1

    while rem:
        if r > j:
            return None
        a = v2(rem)
        if a >= h:
            raise AssertionError("nonzero residue cannot have valuation >= h")
        if out and a <= out[-1]:
            return None
        out.append(a)
        atom = (pow(3, j-r, M) * (1 << a)) % M
        rem = (rem - atom) % M
        r += 1

    return tuple(out)


def prefix_ballot_from_positions(positions, h: int) -> bool:
    """Exact pure-ballot check through prefix depth h."""
    if positions is None:
        return False
    if len(positions) < ceil_alpha_n(h):
        return False
    for r, a in enumerate(positions, start=1):
        # Equivalent to a <= floor((r-1)/alpha).
        if (1 << a) > 3 ** (r - 1):
            return False
    return True


def target_prefix_ballot_ok(X: int, h: int) -> bool:
    assert 1 <= h <= T0
    positions = decode_positions_below_h_from_X(X, J0_ODD, h)
    return prefix_ballot_from_positions(positions, h)


# Exhaustive proof-regression on all small complete words and all truncation
# depths.  The modular decoder must recover exactly the positions below h.
for t in range(1, 11):
    for bits in product((0, 1), repeat=t):
        j = sum(bits)
        X = parity_address(bits)
        true_positions = tuple(i for i, b in enumerate(bits) if b)
        for h in range(1, t + 1):
            got = decode_positions_below_h_from_X(X, j, h)
            want = tuple(a for a in true_positions if a < h)
            assert got == want

# For fixed target total j, shallow residue counts must agree with direct
# pure-ballot word counts.  The total j only twists the address bijection by
# an odd 2-adic unit; it does not change the number of accepted residues.
def direct_ballot(bits):
    q = 0
    for n, b in enumerate(bits, start=1):
        q += b
        if q < ceil_alpha_n(n):
            return False
    return True

for h in range(1, 13):
    accepted_by_decoder = 0
    for X in range(1 << h):
        if target_prefix_ballot_ok(X, h):
            accepted_by_decoder += 1
    accepted_words = sum(1 for bits in product((0, 1), repeat=h)
                         if direct_ballot(bits))
    assert accepted_by_decoder == accepted_words

# Immediate target residue consequence at depth two.
accepted_mod4 = [X for X in range(4) if target_prefix_ballot_ok(X, 2)]
assert accepted_mod4 == [3]

print("PASS A0 s=1 modular prefix decoder certificate")
print("target_identity", "C_req mod 2^h = -3^j0 X mod 2^h")
print("endpoint_Z_needed_for_shallow_decode", False)
print("giant_C_req_materialized", False)
print("depth_2_residue", "X == 3 (mod 4)")
print("small_exhaustive_word_depth", 10)
print("small_target_residue_count_depth", 12)
print("status", "SAFE local necessary-condition oracle")
