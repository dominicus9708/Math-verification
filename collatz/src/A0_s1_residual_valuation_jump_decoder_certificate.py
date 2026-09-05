#!/usr/bin/env python3
"""Exact residual valuation jump decoder for fixed source/endpoint pairs.

For a remaining accelerated-Collatz word B of length n and one-count q,
starting at Y and ending at Z,

    R(n,q;Y,Z) = 2^n Z - 3^q Y

must equal the ordinary correction C(B).

If q>0 and the first 1 of B occurs at position a, then

    v2(R) = a.

Thus the next 1-position is forced.  The prefix 0^a 1 may be discharged in
one exact jump:

    Y' = (3Y + 2^a) / 2^(a+1),
    n' = n-a-1,
    q' = q-1,

and

    R' = (R - 3^(q-1) 2^a) / 2^(a+1)
       = 2^n' Z - 3^q' Y'.

Repeated jumps decode the unique possible word, or reject.  This is a
mathematical inverse for an exact fixed (Y,Z,n,q) instance.  It does not make
the enormous A0 source/checkpoint family computationally small by itself.
"""

from itertools import product


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def correction_from_bits(bits):
    positions = [i for i, b in enumerate(bits) if b]
    q = len(positions)
    return sum((3 ** (q-r-1)) * (1 << a)
               for r, a in enumerate(positions))


def parity_address(bits):
    n = len(bits)
    q = sum(bits)
    C = correction_from_bits(bits)
    return (-C * pow(3 ** q, -1, 1 << n)) % (1 << n)


def direct_endpoint(Y: int, bits):
    x = Y
    got = []
    for _ in bits:
        got.append(x & 1)
        x = T(x)
    return tuple(got), x


def residual_jump_decode(Y: int, Z: int, n: int, q: int):
    """Return unique one-positions, or None if no fixed-(n,q) word realizes it."""
    assert Y >= 0 and Z >= 0 and n >= 0 and 0 <= q <= n

    positions = []
    offset = 0

    while q:
        R = (1 << n) * Z - (3 ** q) * Y
        if R <= 0:
            return None

        a = v2(R)
        if a >= n:
            return None

        # Since n>a, 2^n Z vanishes modulo 2^(a+1), so v2(Y)=a too.
        if Y % (1 << a) != 0 or ((Y >> a) & 1) != 1:
            return None

        atom = (3 ** (q - 1)) * (1 << a)
        numer = R - atom
        if numer % (1 << (a + 1)) != 0:
            return None

        Y_numer = 3 * Y + (1 << a)
        if Y_numer % (1 << (a + 1)) != 0:
            return None
        Y = Y_numer // (1 << (a + 1))

        n -= a + 1
        q -= 1
        positions.append(offset + a)
        offset += a + 1

        R_next = numer // (1 << (a + 1))
        assert R_next == (1 << n) * Z - (3 ** q) * Y

    # With no ones left, the only possible remaining word is all zeros.
    if (1 << n) * Z != Y:
        return None

    return tuple(positions)


# Every genuine word through length 10 is recovered exactly from its canonical
# source address and direct endpoint.
for n in range(1, 11):
    for bits in product((0, 1), repeat=n):
        Y = parity_address(bits)
        actual, Z = direct_endpoint(Y, bits)
        assert actual == bits
        got = residual_jump_decode(Y, Z, n, sum(bits))
        want = tuple(i for i, b in enumerate(bits) if b)
        assert got == want


# Converse regression: whenever the decoder accepts an arbitrary small
# (Y,Z,n,q) tuple, the decoded word is exactly the actual parity word of Y and
# its endpoint is exactly Z.
for n in range(1, 8):
    for q in range(n + 1):
        for Y in range(64):
            for Z in range(64):
                got = residual_jump_decode(Y, Z, n, q)
                if got is None:
                    continue
                pos = set(got)
                bits = tuple(1 if i in pos else 0 for i in range(n))
                assert sum(bits) == q
                actual, endpoint = direct_endpoint(Y, bits)
                assert actual == bits
                assert endpoint == Z

print("PASS A0 s=1 residual valuation jump decoder certificate")
print("residual", "R=2^n Z-3^q Y")
print("next_one", "a=v2(R)")
print("jump", "0^a1 discharged exactly")
print("exact_pair_realizations", "zero or one")
print("genuine_word_regression_n_max", 10)
print("converse_grid", "n<=7, Y,Z<64")
print("status", "EXACT pairwise inverse; compressed family execution remains OPEN")
