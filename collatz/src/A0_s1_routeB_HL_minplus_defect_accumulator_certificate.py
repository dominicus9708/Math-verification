#!/usr/bin/env python3
"""Exact fixed-resolution H/L min-plus correction-defect accumulator.

The canonical H/L grammar already gives an exact family DP for bidirectional
correction residues.  This certificate augments every residue-pair state with
minimum nonnegative target-relative correction gaps.

For the characteristic targets H*_h and L*_h define four oriented gaps:

    HF(W) = C(H*_h) - C(W)                         for W in H_h,
    HR(W) = C(reverse(W)) - C(reverse(H*_h))       for W in H_h,
    LF(W) = C(W) - C(L*_h)                         for W in L_h,
    LR(W) = C(reverse(L*_h)) - C(reverse(W))       for W in L_h.

All four are nonnegative by prefix-position dominance.

At a fixed modulus M, the state key is

    (C(W) mod M, C(reverse(W)) mod M).

For each key it is sufficient to retain two independent scalar minima for the
relevant language: (min HF,min HR) or (min LF,min LR).  No Pareto frontier is
needed.  The reason is that each canonical grammar production uses exactly one
orientation from each child in each parent orientation.

A subtle point is essential.  An arbitrary admissible grammar cut need not be
the characteristic target's own canonical cut.  Therefore each production has
a nonnegative ANCHOR OFFSET between the global characteristic target and the
characteristic child-product anchor.  These offsets are included exactly; they
must not be silently set to zero.

For every fixed M, each typed length has at most M^2 residue keys, hence at most
4*M^2 scalar min-plus entries across H/L and forward/reverse orientations.
Through lengths <=H this is at most 4*(H+1)*M^2 scalar entries.

This is a fixed-resolution family theorem.  It does not prove that the huge
root can be evaluated by iterating all lengths up to 10^10, and it does not
prove that K,L can grow with horizon at bounded cost.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product

MAX_EXHAUSTIVE_H = 8
MODULI = (2, 3, 4, 6, 9, 12)


def log_bounds(z: Fraction, n: int = 100):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(None)
def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def phase_carry(a: int, b: int) -> int:
    out = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert out in (0, 1)
    return out


def q_H(h: int) -> int:
    assert h >= 1
    return floor_alpha(h) + 1


def q_L(h: int) -> int:
    assert h >= 0
    return floor_alpha(h)


def H_target(h: int):
    assert h >= 1
    return (1,) + tuple(
        floor_alpha(u + 1) - floor_alpha(u)
        for u in range(1, h)
    )


def L_target(h: int):
    assert h >= 0
    return tuple(
        floor_alpha(u + 1) - floor_alpha(u)
        for u in range(h)
    )


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def residue_pair(bits, M: int):
    return (
        correction(bits) % M,
        correction(tuple(reversed(bits))) % M,
    )


def compose_pair(a, b, h1, q1, h2, q2, M):
    return (
        (pow(3, q2, M) * a[0] + pow(2, h1, M) * b[0]) % M,
        (pow(3, q1, M) * b[1] + pow(2, h2, M) * a[1]) % M,
    )


def primitive_H_pair(x, hx, qx, M):
    # U = 1 reverse(X)
    return (
        (pow(3, qx, M) + 2 * x[1]) % M,
        (3 * x[0] + pow(2, hx, M)) % M,
    )


def primitive_L_pair(x, M):
    # U = 0 reverse(X)
    return ((2 * x[1]) % M, x[0] % M)


def min_pair_update(table, key, a, b):
    old = table.get(key)
    if old is None:
        table[key] = (a, b)
    else:
        table[key] = (min(old[0], a), min(old[1], b))


@lru_cache(None)
def D_H(h: int, M: int):
    """key -> (minimum HF, minimum HR)."""
    assert h >= 1
    target = H_target(h)
    target_f = correction(target)
    target_r = correction(tuple(reversed(target)))
    out = {}

    for c in range(1, h + 1):
        if floor_alpha(c) != floor_alpha(c - 1):
            continue
        s = h - c
        if s and phase_carry(c, s) != 1:
            continue

        X_states = D_L(c - 1, M)
        V_states = D_H(s, M) if s else {(0, 0): (0, 0)}

        U_star = (1,) + tuple(reversed(L_target(c - 1)))
        V_star = H_target(s) if s else ()
        anchor = U_star + V_star

        # The anchor is a legal H_h word but need not equal H*_h.
        anchor_F = target_f - correction(anchor)
        anchor_R = correction(tuple(reversed(anchor))) - target_r
        assert anchor_F >= 0 and anchor_R >= 0

        qV = q_H(s) if s else 0
        for x_key, (x_LF, x_LR) in X_states.items():
            U_key = primitive_H_pair(x_key, c - 1, q_L(c - 1), M)

            for v_key, (v_HF, v_HR) in V_states.items():
                parent_key = compose_pair(
                    U_key,
                    v_key,
                    c,
                    q_H(c),
                    s,
                    qV,
                    M,
                )

                # Primitive forward H gap is 2*LR(X).
                HF = (
                    anchor_F
                    + (3 ** qV) * 2 * x_LR
                    + (2 ** c) * v_HF
                )

                # Primitive reverse H gap is 3*LF(X).
                HR = (
                    anchor_R
                    + (3 ** q_H(c)) * v_HR
                    + (2 ** s) * 3 * x_LF
                )

                min_pair_update(out, parent_key, HF, HR)

    return out


@lru_cache(None)
def D_L(h: int, M: int):
    """key -> (minimum LF, minimum LR)."""
    assert h >= 0
    if h == 0:
        return {(0, 0): (0, 0)}

    target = L_target(h)
    target_f = correction(target)
    target_r = correction(tuple(reversed(target)))
    out = {}

    for c in range(1, h + 1):
        if c > 1 and floor_alpha(c) != floor_alpha(c - 1) + 1:
            continue
        s = h - c
        if s and phase_carry(c, s) != 0:
            continue

        V_states = D_L(s, M) if s else {(0, 0): (0, 0)}
        V_star = L_target(s) if s else ()

        if c == 1:
            U_star = (0,)
            anchor = U_star + V_star
            anchor_F = correction(anchor) - target_f
            anchor_R = target_r - correction(tuple(reversed(anchor)))
            assert anchor_F >= 0 and anchor_R >= 0

            U_key = (0, 0)
            for v_key, (v_LF, v_LR) in V_states.items():
                parent_key = compose_pair(U_key, v_key, 1, 0, s, q_L(s), M)
                LF = anchor_F + 2 * v_LF
                LR = anchor_R + v_LR
                min_pair_update(out, parent_key, LF, LR)
            continue

        X_states = D_H(c - 1, M)
        U_star = (0,) + tuple(reversed(H_target(c - 1)))
        anchor = U_star + V_star
        anchor_F = correction(anchor) - target_f
        anchor_R = target_r - correction(tuple(reversed(anchor)))
        assert anchor_F >= 0 and anchor_R >= 0

        for x_key, (x_HF, x_HR) in X_states.items():
            U_key = primitive_L_pair(x_key, M)

            for v_key, (v_LF, v_LR) in V_states.items():
                parent_key = compose_pair(
                    U_key,
                    v_key,
                    c,
                    q_L(c),
                    s,
                    q_L(s),
                    M,
                )

                # Primitive forward L gap is 2*HR(X).
                LF = (
                    anchor_F
                    + (3 ** q_L(s)) * 2 * x_HR
                    + (2 ** c) * v_LF
                )

                # Primitive reverse L gap is HF(X).
                LR = (
                    anchor_R
                    + (3 ** q_L(c)) * v_LR
                    + (2 ** s) * x_HF
                )

                min_pair_update(out, parent_key, LF, LR)

    return out


def in_H(bits):
    if not bits:
        return False
    q = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        if q < floor_alpha(u) + 1:
            return False
    return q == q_H(len(bits))


def in_L(bits):
    q = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        if q > floor_alpha(u):
            return False
    return q == q_L(len(bits))


def direct_H(h, M):
    target = H_target(h)
    target_f = correction(target)
    target_r = correction(tuple(reversed(target)))
    out = {}
    for bits in product((0, 1), repeat=h):
        if not in_H(bits):
            continue
        key = residue_pair(bits, M)
        HF = target_f - correction(bits)
        HR = correction(tuple(reversed(bits))) - target_r
        assert HF >= 0 and HR >= 0
        min_pair_update(out, key, HF, HR)
    return out


def direct_L(h, M):
    target = L_target(h)
    target_f = correction(target)
    target_r = correction(tuple(reversed(target)))
    out = {}
    for bits in product((0, 1), repeat=h):
        if not in_L(bits):
            continue
        key = residue_pair(bits, M)
        LF = correction(bits) - target_f
        LR = target_r - correction(tuple(reversed(bits)))
        assert LF >= 0 and LR >= 0
        min_pair_update(out, key, LF, LR)
    return out


# ---------------------------------------------------------------------------
# Exhaustive exact word-vs-min-plus-DP regression.
# ---------------------------------------------------------------------------

H_map_checks = 0
L_map_checks = 0
state_bound_checks = 0
anchor_nonzero_seen = False

for M in MODULI:
    D_H.cache_clear()
    D_L.cache_clear()

    for h in range(1, MAX_EXHAUSTIVE_H + 1):
        exact_H = direct_H(h, M)
        exact_L = direct_L(h, M)
        dp_H = D_H(h, M)
        dp_L = D_L(h, M)

        assert exact_H == dp_H
        assert exact_L == dp_L
        H_map_checks += 1
        L_map_checks += 1

        assert len(dp_H) <= M * M
        assert len(dp_L) <= M * M
        state_bound_checks += 2

        # Verify that the zero-gap characteristic target state is present.
        assert dp_H[residue_pair(H_target(h), M)] == (0, 0)
        assert dp_L[residue_pair(L_target(h), M)] == (0, 0)

    # Explicitly witness that anchor offsets cannot generally be omitted.
    # H_4 admits c=1, whose child-product anchor differs from H*_4.
    h = 4
    c = 1
    s = h - c
    if (
        floor_alpha(c) == floor_alpha(c - 1)
        and phase_carry(c, s) == 1
    ):
        anchor = (1,) + H_target(s)
        if anchor != H_target(h):
            assert correction(H_target(h)) - correction(anchor) > 0
            anchor_nonzero_seen = True

assert H_map_checks == len(MODULI) * MAX_EXHAUSTIVE_H
assert L_map_checks == len(MODULI) * MAX_EXHAUSTIVE_H
assert state_bound_checks == 2 * len(MODULI) * MAX_EXHAUSTIVE_H
assert anchor_nonzero_seen

print("PASS A0 s=1 Route-B H/L min-plus defect accumulator certificate")
print("max_exhaustive_h", MAX_EXHAUSTIVE_H)
print("moduli", MODULI)
print("H_map_checks", H_map_checks)
print("L_map_checks", L_map_checks)
print("state_bound_checks", state_bound_checks)
print("anchor_offset_nonzero_witness", anchor_nonzero_seen)
print(
    "state",
    "bidirectional correction residue pair plus two independent scalar oriented gap minima per H/L type",
)
print(
    "bound",
    "at fixed M, <=4*M^2 scalar min-plus entries per length across H/L and forward/reverse orientations",
)
print(
    "anchor_audit",
    "arbitrary admissible grammar cuts use explicit nonnegative characteristic-target anchor offsets",
)
print(
    "dsd_audit",
    "family observation state and membership-defect lower bound are composed exactly; no Pareto frontier or target-cut identification is assumed",
)
print(
    "status",
    "fixed-resolution H/L min-plus defect accumulation CLOSED; root-scale compressed evaluation and adaptive-resolution globalization remain OPEN",
)
