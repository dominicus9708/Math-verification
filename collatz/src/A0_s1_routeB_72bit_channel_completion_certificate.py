#!/usr/bin/env python3
"""72-bit physical channel-completion certificate for A0 s=1 Route-B.

The physical A0 shell satisfies

    2^71 < X <= X_MAX < 2^72.

Let a prefix channel at depth h<=72 be

    X = r + 2^h m,
    T^h(X) = y + 3^q m.

Set ell=72-h.  Because 0<=r<2^h and X<2^72, every physical parameter in
this channel satisfies

    0 <= m < 2^ell.

The exact channel/block jump writes

    m = m_B + 2^ell n,
    0 <= m_B < 2^ell.

Therefore, at the 72-bit completion depth,

    n = 0,
    m = m_B.

So each surviving physical parameter m corresponds to exactly one length-ell
suffix block, exactly one 72-bit address, and exactly one physical integer X.
After those 72 parity bits are exposed, the later Collatz parity sequence is
deterministic from X; there is no further finite-address branching.

This does NOT solve the long Route-B membership predicate.  It removes a
representation ambiguity: the remaining long decoder may work with one fixed
physical X per completed 72-bit address rather than an infinite family inside
that address.
"""

K_A0 = 72
X_MIN = (1 << 71) + 1
X_MAX = 3_295_414_002_074_039_191_016

assert X_MIN <= X_MAX < (1 << K_A0)


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def collatz_bits(x: int, n: int):
    out = []
    for _ in range(n):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


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
        numer = 3 * y + (3 ** (q + 1)) * m0 + 1
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q + 1

    return h + 1, r2, y2, q2


def channel_state(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def block_state(bits):
    ell = qB = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << ell)
            qB += 1
        ell += 1
    return ell, qB, C


def block_residue(block):
    ell, qB, C = block
    if ell == 0:
        return 0
    modulus = 1 << ell
    return (-C * pow(pow(3, qB, modulus), -1, modulus)) % modulus


def jump_channel(parent, block):
    h, r, y, q = parent
    ell, qB, C = block
    if ell == 0:
        assert qB == 0 and C == 0
        return parent, 0

    modulus = 1 << ell
    rho = block_residue(block)
    mB = ((rho - y) * pow(pow(3, q, modulus), -1, modulus)) % modulus

    r2 = r + (mB << h)
    numer = (3 ** qB) * (y + (3 ** q) * mB) + C
    assert numer % modulus == 0
    y2 = numer // modulus
    return (h + ell, r2, y2, q + qB), mB


# General physical-range inequality for every possible prefix depth.
for h in range(K_A0 + 1):
    ell = K_A0 - h
    # The worst possible nonnegative parameter occurs at r=0.
    m_hi = X_MAX >> h
    if ell == 0:
        # At depth 72, any represented X<2^72 is its own residue and m=0.
        assert m_hi == 0
    else:
        assert m_hi < (1 << ell)


# Direct physical regressions at representative shell points and many prefix
# depths.  At depth 72 the channel residue is exactly X; for every earlier
# depth the actual suffix block selects exactly the physical parameter m and
# the completed child has parameter n=0.
SAMPLE_X = (
    X_MIN,
    X_MIN + 1,
    (X_MIN + X_MAX) // 2,
    X_MAX - 1,
    X_MAX,
)
PREFIX_DEPTHS = (0, 1, 2, 5, 10, 20, 38, 40, 60, 71, 72)
completion_checks = 0

for X in SAMPLE_X:
    bits72 = collatz_bits(X, K_A0)
    full = channel_state(bits72)
    assert full[0] == K_A0
    assert full[1] == X

    for h in PREFIX_DEPTHS:
        parent_bits = bits72[:h]
        parent = channel_state(parent_bits)
        hh, r, y, q = parent
        assert hh == h
        assert (X - r) % (1 << h) == 0

        m = (X - r) // (1 << h)
        ell = K_A0 - h
        if ell == 0:
            assert m == 0
        else:
            assert 0 <= m < (1 << ell)
            suffix = bits72[h:]
            jumped, mB = jump_channel(parent, block_state(suffix))
            assert mB == m
            assert jumped[0] == K_A0
            assert jumped[1] == X
            # X = r' + 2^72*n and 0<=X<2^72, hence n=0.
            assert X == jumped[1]

        completion_checks += 1

assert completion_checks == 55

print("PASS A0 s=1 Route-B 72-bit physical channel-completion certificate")
print("physical_shell", "2^71 < X <= X_MAX < 2^72")
print("X_MAX", X_MAX)
print("sample_X_count", len(SAMPLE_X))
print("prefix_depth_count", len(PREFIX_DEPTHS))
print("completion_checks", completion_checks)
print("completion_rule", "ell=72-h; 0<=m<2^ell; m=mB+2^ell*n => n=0 and m=mB")
print(
    "formation_audit",
    "at the physical 72-bit address depth every surviving channel member is a fully formed singleton integer address",
)
print(
    "axis_audit",
    "the parameter axis terminates at n=0 when the dyadic resolution reaches the physical 72-bit shell width",
)
print(
    "dsd_audit",
    "finite-address branching ends at 72 bits, but the deterministic long-orbit membership predicate remains a separate gate",
)
print(
    "status",
    "G4 physical 72-bit channel completion CLOSED; compressed deterministic long-membership test remains OPEN",
)
