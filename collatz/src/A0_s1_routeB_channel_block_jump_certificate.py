#!/usr/bin/env python3
"""Exact channel-block jump certificate for A0 s=1 Route-B.

For an existing prefix channel

    X = r + 2^h m,
    T^h(X) = y + 3^q m,

and a parity block B of length ell, odd count qB, correction C_B,

    T^ell(Z) = (3^qB Z + C_B) / 2^ell,

the block has canonical input residue

    rho_B = -C_B * (3^qB)^(-1) mod 2^ell.

The current endpoint Z=y+3^q m follows B iff

    y + 3^q m == rho_B mod 2^ell.

Because 3^q is odd, there is one exact parameter residue

    m_B = (rho_B-y) * (3^q)^(-1) mod 2^ell.

Writing m=m_B+2^ell n gives the jumped channel

    X = r' + 2^(h+ell) n,
    T^(h+ell)(X) = y' + 3^(q+qB) n,

with

    r' = r + 2^h m_B,
    y' = [3^qB (y + 3^q m_B) + C_B] / 2^ell.

This certificate compares the block jump against repeated exact one-bit channel
refinement on every parent/block pair through finite audit depths. It also
checks exact interval pullback for finite parameter intervals.

Scope: this closes the exact arithmetic primitive needed for a lazy block
decoder. It does not prove that Route-B membership closes universally.
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

    return (h + 1, r2, y2, q2)


def channel_state(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def block_state(bits):
    """Return exact (ell,q,C) correction state for a parity block."""
    ell = 0
    q = 0
    C = 0
    for bit in bits:
        if bit == 0:
            ell += 1
        else:
            C = 3 * C + (1 << ell)
            q += 1
            ell += 1
    return (ell, q, C)


def compose_blocks(a, b):
    ell1, q1, C1 = a
    ell2, q2, C2 = b
    return (
        ell1 + ell2,
        q1 + q2,
        (3 ** q2) * C1 + (1 << ell1) * C2,
    )


def block_residue(block):
    ell, qB, C = block
    if ell == 0:
        return 0
    modulus = 1 << ell
    return (-C * pow(pow(3, qB, modulus), -1, modulus)) % modulus


def jump_channel(channel, block):
    h, r, y, q = channel
    ell, qB, C = block
    assert h >= 0 and ell >= 0
    assert 0 <= r < (1 << h)

    if ell == 0:
        assert qB == 0 and C == 0
        return channel, 0

    modulus = 1 << ell
    rho = block_residue(block)
    mB = ((rho - y) * pow(pow(3, q, modulus), -1, modulus)) % modulus

    r2 = r + (mB << h)
    numer = (3 ** qB) * (y + (3 ** q) * mB) + C
    assert numer % modulus == 0
    y2 = numer // modulus

    state2 = (h + ell, r2, y2, q + qB)
    assert 0 <= r2 < (1 << (h + ell))
    return state2, mB


def repeated_jump(channel, bits):
    state = channel
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def jump_parameter_interval(L: int, U: int, mB: int, ell: int):
    assert L <= U and ell >= 0
    step = 1 << ell
    n_lo = ceil_div(L - mB, step)
    n_hi = (U - mB) // step
    if n_lo > n_hi:
        return None
    return (n_lo, n_hi)


# ---------------------------------------------------------------------------
# 1. Exhaustive comparison against repeated one-bit refinement.
# ---------------------------------------------------------------------------

PARENT_MAX_DEPTH = 7
BLOCK_MAX_DEPTH = 7
jump_checks = 0
lift_checks = 0
interval_checks = 0
composition_checks = 0

parent_words = []
for hp in range(PARENT_MAX_DEPTH + 1):
    for mask in range(1 << hp):
        parent_words.append(tuple((mask >> i) & 1 for i in range(hp)))

block_words = []
for ell in range(BLOCK_MAX_DEPTH + 1):
    for mask in range(1 << ell):
        block_words.append(tuple((mask >> i) & 1 for i in range(ell)))

for pbits in parent_words:
    parent = channel_state(pbits)
    h, r, y, q = parent

    for bbits in block_words:
        block = block_state(bbits)
        jumped, mB = jump_channel(parent, block)
        repeated = repeated_jump(parent, bbits)
        assert jumped == repeated
        jump_checks += 1

        ell, qB, C = block
        combined_bits = pbits + bbits
        assert jumped == channel_state(combined_bits)

        if ell == 0:
            assert mB == 0
        else:
            modulus = 1 << ell
            rho = block_residue(block)
            assert (y + (3 ** q) * mB - rho) % modulus == 0

        h2, r2, y2, q2 = jumped
        for n in range(4):
            old_m = mB + (1 << ell) * n
            X_old = r + (1 << h) * old_m
            X_new = r2 + (1 << h2) * n
            assert X_old == X_new
            got_bits, got_y = orbit_prefix(X_new, h2)
            assert got_bits == combined_bits
            assert got_y == y2 + (3 ** q2) * n
            lift_checks += 1

        for L, U in ((0, 0), (0, 5), (3, 17), (10, 41)):
            got = jump_parameter_interval(L, U, mB, ell)
            explicit = [
                m for m in range(L, U + 1)
                if (m - mB) % (1 << ell) == 0
            ]
            if not explicit:
                assert got is None
            else:
                ns = [(m - mB) // (1 << ell) for m in explicit]
                assert got == (min(ns), max(ns))
                assert ns == list(range(min(ns), max(ns) + 1))
            interval_checks += 1


# ---------------------------------------------------------------------------
# 2. Two-block jump composition.
# ---------------------------------------------------------------------------

COMPOSE_PARENT_MAX_DEPTH = 5
COMPOSE_BLOCK_TOTAL_MAX_DEPTH = 6
for hp in range(COMPOSE_PARENT_MAX_DEPTH + 1):
    for pmask in range(1 << hp):
        pbits = tuple((pmask >> i) & 1 for i in range(hp))
        parent = channel_state(pbits)

        for n in range(COMPOSE_BLOCK_TOTAL_MAX_DEPTH + 1):
            for mask in range(1 << n):
                bits = tuple((mask >> i) & 1 for i in range(n))
                direct_block = block_state(bits)
                direct_jump, _ = jump_channel(parent, direct_block)

                for cut in range(n + 1):
                    left = block_state(bits[:cut])
                    right = block_state(bits[cut:])
                    assert compose_blocks(left, right) == direct_block

                    mid, _ = jump_channel(parent, left)
                    sequential, _ = jump_channel(mid, right)
                    assert sequential == direct_jump
                    composition_checks += 1


# ---------------------------------------------------------------------------
# 3. Formation / axis / DSD audit statements.
# ---------------------------------------------------------------------------
# Formation lens:
#   jumped parent state is formed only from the parent channel, intrinsic block
#   summary (ell,qB,C), and the explicit concatenation boundary.
# Axis-property lens:
#   parent parameter m and child parameter n are coordinates of the same
#   cylinder family at different dyadic resolutions; no absolute placement
#   coordinate is hidden inside the block.
# DSD audit:
#   repeated bit refinement and block jump are extensionally identical on the
#   exhaustive audit domain. This certifies the primitive, not universal
#   language membership.

print("PASS A0 s=1 Route-B exact channel-block jump certificate")
print("parent_channel", "X=r+2^h*m; T^h(X)=y+3^q*m")
print("block", "T^ell(Z)=(3^qB*Z+C_B)/2^ell")
print("selected_parameter", "mB=(rho_B-y)*(3^q)^(-1) mod 2^ell")
print("jump", "r'=r+2^h*mB; q'=q+qB")
print("jump_endpoint", "y'=[3^qB*(y+3^q*mB)+C_B]/2^ell")
print("parent_max_depth", PARENT_MAX_DEPTH)
print("block_max_depth", BLOCK_MAX_DEPTH)
print("jump_checks", jump_checks)
print("lift_checks", lift_checks)
print("interval_checks", interval_checks)
print("composition_checks", composition_checks)
print("formation_audit", "parent + intrinsic block summary + explicit boundary")
print("axis_audit", "parameter resolution changes m=mB+2^ell*n; block remains intrinsic")
print("dsd_audit", "jump equals repeated one-bit refinement on exhaustive audit domain")
print("status", "EXACT channel-block jump CLOSED; target-aware lazy decoder remains OPEN")
