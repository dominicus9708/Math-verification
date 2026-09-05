#!/usr/bin/env python3
"""Exact prefix-channel transducer for A0 s=1 long-membership work.

For an accelerated-Collatz parity prefix of depth h, let r be its canonical
start residue in [0,2^h), q its odd count, and y=T^h(r).  Then every integer
in the same dyadic cylinder has the exact affine form

    X = r + 2^h m,
    T^h(X) = y + 3^q m.

This file certifies the exact one-bit refinement of that channel.  If the next
parity bit is b, choose the unique m0 in {0,1} satisfying

    b == y + m0 (mod 2),

and write m=m0+2k.  The child channel is

    r' = r + 2^h m0,

and

    b=0: q'=q,
         y'=(y+3^q m0)/2,

    b=1: q'=q+1,
         y'=(3y+3^(q+1)m0+1)/2.

Then exactly

    X = r' + 2^(h+1) k,
    T^(h+1)(X) = y' + 3^q' k.

Thus a channel can be refined without iterating every integer in the cylinder.
This is a structural theorem only.  It does not by itself prove pure-ballot,
C4F, correction-language membership, or a full A0 bridge.
"""


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def orbit_prefix(x: int, h: int):
    bits = []
    for _ in range(h):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


def refine_channel(state, bit: int):
    h, r, y, q = state
    assert h >= 0
    assert 0 <= r < (1 << h)
    assert bit in (0, 1)

    # 3^q is odd, so parity(y+3^q m) = parity(y+m).
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)

    if bit == 0:
        numer = y + (3 ** q) * m0
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q
    else:
        numer = 3 * y + (3 ** (q + 1)) * m0 + 1
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q + 1

    assert 0 <= r2 < (1 << (h + 1))
    return (h + 1, r2, y2, q2)


# ---------------------------------------------------------------------------
# Exhaustive finite regression.
# ---------------------------------------------------------------------------
# The proof is the affine calculation in the module docstring.  The exhaustive
# checks below audit indexing, canonical residues, child partitioning, and the
# exact lift coefficient independently through depth 10.

states = {(0, 0, 0, 0): ()}
for h in range(10):
    next_states = {}
    for state, bits in states.items():
        sh, r, y, q = state
        assert sh == h
        assert q == sum(bits)
        direct_bits, direct_y = orbit_prefix(r, h)
        assert direct_bits == bits
        assert direct_y == y

        for bit in (0, 1):
            child = refine_channel(state, bit)
            h2, r2, y2, q2 = child
            bits2 = bits + (bit,)

            got_bits, got_y = orbit_prefix(r2, h2)
            assert got_bits == bits2
            assert got_y == y2
            assert q2 == sum(bits2)

            # Every tested lift in the child cylinder has the same prefix and
            # the exact affine endpoint y'+3^q' k.
            for k in range(12):
                X = r2 + (1 << h2) * k
                lift_bits, lift_y = orbit_prefix(X, h2)
                assert lift_bits == bits2
                assert lift_y == y2 + (3 ** q2) * k

            assert child not in next_states
            next_states[child] = bits2

    # Every binary prefix has exactly one canonical channel.
    assert len(next_states) == (1 << (h + 1))
    assert len({s[1] for s in next_states}) == (1 << (h + 1))
    states = next_states


# ---------------------------------------------------------------------------
# A0 handoff consequence.
# ---------------------------------------------------------------------------
# In the physical shell 2^71<X<2^72, depth 72 is already singleton: a
# canonical residue r in that interval is the ordinary integer X itself.
# Hence channel refinement before depth 72 is a lossless symbolic grouping;
# after depth 72 the actual future orbit is deterministic.

X_LO = 1 << 71
X_HI = 1 << 72
assert X_HI - X_LO == (1 << 71)

print("PASS A0 s=1 exact prefix-channel transducer certificate")
print("channel", "X=r+2^h*m; T^h(X)=y+3^q*m")
print("child_parameter", "m=m0+2k, m0=(b-y) mod 2")
print("exhaustive_depth", 10)
print("physical_singleton_depth", 72)
print("state_merge_warning", "merge only when every future predicate is invariant")
print("status", "EXACT structural theorem; long membership remains OPEN")
