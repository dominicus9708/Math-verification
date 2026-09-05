#!/usr/bin/env python3
"""Exact multi-bit affine block transducer certificate for A0 s=1.

Suppose an already exposed Collatz prefix is represented by the exact affine
channel

    X = r + 2^h m,
    T^h(X) = y + 3^q m,

for every integer parameter m in the channel, where T is the accelerated
Collatz map

    T(x) = x/2              if x is even,
           (3x+1)/2         if x is odd.

Fix a continuation parity block v of length n with p odd steps.  Let A_n(v)
be its universal 2-adic parity address modulo 2^n.  Since 3^q is odd, the
congruence

    y + 3^q m == A_n(v)  (mod 2^n)

has one and only one residue m0 modulo 2^n:

    m0 == 3^(-q) (A_n(v)-y)  (mod 2^n).

Writing m=m0+2^n k gives exactly

    X = r' + 2^(h+n) k,
    T^(h+n)(X) = y' + 3^(q+p) k,

where

    r' = r + 2^h m0,
    z0 = y + 3^q m0,
    y' = T^n(z0).

Thus an arbitrary fixed n-bit continuation can be consumed in one exact
arithmetic jump.  The certificate exhaustively checks that this block jump is
identical to n repeated one-bit channel refinements for all channel prefixes
through depth five and all continuation blocks through length five.  It also
checks the affine identity at several parameter lifts.

This is an exact arithmetic identity only.  It does not assert that any block
alphabet is complete for the A0 branch, does not use C4F, and is not by itself
a pruning theorem.
"""


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def iterate(x: int, n: int) -> int:
    for _ in range(n):
        x = T(x)
    return x


def parity_word(x: int, n: int):
    out = []
    for _ in range(n):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


def block_address(bits):
    """Universal address A_n(bits) in [0,2^n)."""
    n = len(bits)
    if n == 0:
        return 0
    mod = 1 << n
    s = 0
    rank = 0
    for a, bit in enumerate(bits):
        assert bit in (0, 1)
        if bit:
            rank += 1
            inv3r = pow(pow(3, rank, mod), -1, mod)
            s = (s + inv3r * (1 << a)) % mod
    return (-s) % mod


def canonical_channel_from_prefix(bits):
    """Return (h,r,y,q) for the parity cylinder described by bits."""
    h = len(bits)
    r = block_address(bits)
    assert parity_word(r, h) == tuple(bits)
    y = iterate(r, h)
    q = sum(bits)
    return h, r, y, q


def refine_one(state, bit):
    """Exact one-bit affine refinement of state (h,r,y,q)."""
    h, r, y, q = state
    assert bit in (0, 1)

    # Need y+3^q*m == bit (mod 2).  As 3^q is odd,
    # m0 == bit-y (mod 2).
    m0 = (bit - y) & 1
    r2 = r + (1 << h) * m0
    z0 = y + (3 ** q) * m0
    assert (z0 & 1) == bit
    y2 = T(z0)
    q2 = q + bit
    return h + 1, r2, y2, q2


def refine_block(state, bits):
    """Consume one fixed parity block in a single exact congruence jump."""
    h, r, y, q = state
    bits = tuple(bits)
    n = len(bits)
    if n == 0:
        return state

    mod = 1 << n
    a = block_address(bits)
    inv = pow(pow(3, q, mod), -1, mod)
    m0 = ((a - y) * inv) % mod

    r2 = r + (1 << h) * m0
    z0 = y + (3 ** q) * m0
    assert z0 % mod == a
    assert parity_word(z0, n) == bits

    y2 = iterate(z0, n)
    q2 = q + sum(bits)

    assert 0 <= r2 < (1 << (h + n))
    return h + n, r2, y2, q2


def assert_affine(state, lifts=(0, 1, 2, 5, 17)):
    h, r, y, q = state
    for k in lifts:
        X = r + (1 << h) * k
        assert iterate(X, h) == y + (3 ** q) * k


# Basic address bijection and orbit-prefix regression.
for n in range(1, 9):
    seen = set()
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        a = block_address(bits)
        assert 0 <= a < (1 << n)
        assert a not in seen
        seen.add(a)
        assert parity_word(a, n) == bits
    assert len(seen) == (1 << n)


# Exhaustive block-vs-repeated-one-bit regression.
checks = 0
for h in range(0, 6):
    for pmask in range(1 << h):
        prefix = tuple((pmask >> i) & 1 for i in range(h))
        state = canonical_channel_from_prefix(prefix)
        assert_affine(state)

        for n in range(1, 6):
            for bmask in range(1 << n):
                bits = tuple((bmask >> i) & 1 for i in range(n))

                direct = refine_block(state, bits)
                repeated = state
                for bit in bits:
                    repeated = refine_one(repeated, bit)

                assert direct == repeated
                assert_affine(direct)

                h2, r2, y2, q2 = direct
                assert parity_word(r2, h2) == prefix + bits
                assert q2 == sum(prefix) + sum(bits)
                checks += 1


# A few nontrivial long-block regressions, still without enumerating the
# 2^n address space.
long_cases = (
    ((1, 1, 0, 1, 0, 1), (0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0)),
    ((1, 0, 1, 1, 0, 0, 1), (1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0)),
    ((0, 1, 0, 1, 1, 0, 1, 0), (0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1)),
)
for prefix, bits in long_cases:
    state = canonical_channel_from_prefix(prefix)
    direct = refine_block(state, bits)
    repeated = state
    for bit in bits:
        repeated = refine_one(repeated, bit)
    assert direct == repeated
    assert_affine(direct, lifts=(0, 1, 3, 11, 29))


print("PASS A0 s=1 exact multi-bit affine block transducer certificate")
print("exhaustive_block_vs_onebit_checks", checks)
print("max_exhaustive_prefix_depth", 5)
print("max_exhaustive_block_length", 5)
print("long_regression_cases", len(long_cases))
print("identity", "X=r'+2^(h+n)k; T^(h+n)(X)=y'+3^(q+p)k")
print("status", "EXACT arithmetic identity; no pruning and no C4F claim")
