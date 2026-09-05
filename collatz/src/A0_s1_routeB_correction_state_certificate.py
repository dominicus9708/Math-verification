#!/usr/bin/env python3
"""Exact correction-state reduction for A0 s=1 Route-B long-membership work.

For a parity word w of length h with q odd symbols, write the accelerated
Collatz affine map on its cylinder as

    T^h(X) = (3^q X + C(w)) / 2^h.

The existing prefix-channel transducer stores (h,r,y,q), where r is the
canonical residue and y=T^h(r).  Hence

    C(w) = 2^h y - 3^q r.

Conversely, (h,q,C) reconstructs the unique canonical residue because 3^q is
invertible modulo 2^h:

    r = -C * (3^q)^(-1) mod 2^h,
    y = (3^q r + C) / 2^h.

Thus (h,q,C) is an exact sufficient state for the full prefix channel; r and y
are redundant coordinates, not additional information.

For concatenated parity blocks u,v,

    h(uv) = h(u)+h(v),
    q(uv) = q(u)+q(v),
    C(uv) = 3^q(v) C(u) + 2^h(u) C(v).

Equivalently, appending one bit b gives

    b=0: (h,q,C) -> (h+1,q,C),
    b=1: (h,q,C) -> (h+1,q+1,3C+2^h).

This is the exact integer form of the Christoffel-DAG composition already used
for normalized correction c=C/2^h, where c(uv)=m(v)c(u)+c(v).

Scope: this closes the correction-arithmetic state reduction and composition
law.  It does NOT prove that the correction language has finitely many quotient
states, nor does it prove pure-ballot/C4F/unique-target membership.
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
    """Independent copy of the exact (h,r,y,q) refinement theorem."""
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


def refine_correction(state, bit: int):
    h, q, C = state
    assert h >= 0 and q >= 0 and C >= 0
    assert bit in (0, 1)
    if bit == 0:
        return (h + 1, q, C)
    return (h + 1, q + 1, 3 * C + (1 << h))


def correction_state(bits):
    state = (0, 0, 0)
    for bit in bits:
        state = refine_correction(state, bit)
    return state


def channel_state(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def reconstruct_channel(state):
    h, q, C = state
    if h == 0:
        assert q == 0 and C == 0
        return (0, 0, 0, 0)

    modulus = 1 << h
    three_q_mod = pow(3, q, modulus)
    inv = pow(three_q_mod, -1, modulus)
    r = (-C * inv) % modulus
    numer = (3 ** q) * r + C
    assert numer % modulus == 0
    y = numer // modulus
    return (h, r, y, q)


def compose(a, b):
    h1, q1, C1 = a
    h2, q2, C2 = b
    return (
        h1 + h2,
        q1 + q2,
        (3 ** q2) * C1 + (1 << h1) * C2,
    )


# ---------------------------------------------------------------------------
# 1. Exact equivalence with the existing prefix-channel state.
# ---------------------------------------------------------------------------

EXHAUSTIVE_DEPTH = 14
prefix_checks = 0
for h in range(EXHAUSTIVE_DEPTH + 1):
    for mask in range(1 << h):
        bits = tuple((mask >> i) & 1 for i in range(h))
        cstate = correction_state(bits)
        chstate = channel_state(bits)
        assert reconstruct_channel(cstate) == chstate

        sh, r, y, q = chstate
        _, cq, C = cstate
        assert sh == h and cq == q
        assert C == (1 << h) * y - (3 ** q) * r

        direct_bits, direct_y = orbit_prefix(r, h)
        assert direct_bits == bits
        assert direct_y == y
        prefix_checks += 1

assert prefix_checks == (1 << (EXHAUSTIVE_DEPTH + 1)) - 1


# ---------------------------------------------------------------------------
# 2. Exact block-composition audit.
# ---------------------------------------------------------------------------

COMPOSITION_TOTAL_DEPTH = 12
composition_checks = 0
for n in range(COMPOSITION_TOTAL_DEPTH + 1):
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        direct = correction_state(bits)
        for cut in range(n + 1):
            left = correction_state(bits[:cut])
            right = correction_state(bits[cut:])
            assert compose(left, right) == direct
            composition_checks += 1

assert composition_checks == 98_305

# Associativity follows algebraically from the displayed composition formula;
# these exhaustive three-block splits audit implementation/indexing.
associativity_checks = 0
for n in range(9):
    for mask in range(1 << n):
        bits = tuple((mask >> i) & 1 for i in range(n))
        for i in range(n + 1):
            for j in range(i, n + 1):
                a = correction_state(bits[:i])
                b = correction_state(bits[i:j])
                c = correction_state(bits[j:])
                assert compose(compose(a, b), c) == compose(a, compose(b, c))
                assert compose(compose(a, b), c) == correction_state(bits)
                associativity_checks += 1


# ---------------------------------------------------------------------------
# 3. DSD irredundancy witnesses for the exact full-channel representation.
# ---------------------------------------------------------------------------

# C cannot be dropped: equal (h,q), distinct correction and channels.
w_c1 = (1, 0)
w_c2 = (0, 1)
s_c1 = correction_state(w_c1)
s_c2 = correction_state(w_c2)
assert s_c1[:2] == s_c2[:2] == (2, 1)
assert s_c1[2] == 1 and s_c2[2] == 2
assert reconstruct_channel(s_c1) == (2, 1, 1, 1)
assert reconstruct_channel(s_c2) == (2, 2, 2, 1)

# q cannot be dropped if the state must reconstruct the exact prefix channel:
# these words have the same (h,C) but different q, residue, and endpoint.
w_q1 = (1, 1, 1, 0, 0)
w_q2 = (1, 0, 0, 0, 1)
s_q1 = correction_state(w_q1)
s_q2 = correction_state(w_q2)
assert (s_q1[0], s_q1[2]) == (s_q2[0], s_q2[2]) == (5, 19)
assert s_q1[1] == 3 and s_q2[1] == 2
assert reconstruct_channel(s_q1) == (5, 23, 20, 3)
assert reconstruct_channel(s_q2) == (5, 5, 2, 2)

# h cannot be dropped from a compositional state unless length is supplied as
# external block metadata: trailing zero preserves (q,C), but changes the 2^h
# factor used by the next nonzero block.
w_h1 = (1,)
w_h2 = (1, 0)
s_h1 = correction_state(w_h1)
s_h2 = correction_state(w_h2)
assert (s_h1[1], s_h1[2]) == (s_h2[1], s_h2[2]) == (1, 1)
next_one = correction_state((1,))
assert compose(s_h1, next_one)[2] == 5
assert compose(s_h2, next_one)[2] == 7


print("PASS A0 s=1 Route-B exact correction-state certificate")
print("state", "(h,q,C), C=2^h*y-3^q*r")
print("reconstruction", "r=-C*(3^q)^(-1) mod 2^h; y=(3^q*r+C)/2^h")
print("composition", "C(uv)=3^q(v)*C(u)+2^h(u)*C(v)")
print("prefix_equivalence_depth", EXHAUSTIVE_DEPTH)
print("prefix_equivalence_checks", prefix_checks)
print("composition_total_depth", COMPOSITION_TOTAL_DEPTH)
print("composition_split_checks", composition_checks)
print("associativity_checks", associativity_checks)
print("drop_C_witness", w_c1, w_c2, s_c1, s_c2)
print("drop_q_witness", w_q1, w_q2, s_q1, s_q2)
print("drop_h_witness", w_h1, w_h2, s_h1, s_h2)
print("status", "EXACT correction arithmetic/composition CLOSED; finite-language quotient remains OPEN")
