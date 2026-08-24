#!/usr/bin/env python3
"""Finite regression certificate for root-translation ultrametric locking.

The accompanying theorem is algebraic and applies at arbitrary length.  This
script exhaustively checks all relative-nonnegative words through length 14
against the repeated H19 mechanical reference.

For an actual word w and mechanical word m with equal total odd count, assume
h_k = q_w(k)-q_m(k) never becomes negative and returns to zero at the end.
Partition the mismatch set into maximal positive neutral excursions.  For
excursion j let [a_j,b_j) be its interval, p_j its first mismatch position,
Q_j the cumulative odd count through b_j, and DeltaR_j its correction
difference computed with absolute dyadic positions.  Then the root-coordinate
canonical translation is

    D = -3^{-q}(R_w-R_m) = sum_j D_j  (mod 2^L),
    D_j = -3^{-Q_j} DeltaR_j          (mod 2^L).

Since the first changed parity symbol in excursion j is at p_j,

    v_2(D_j)=v_2(DeltaR_j)=p_j.

The p_j are strictly increasing, so non-Archimedean dominance gives

    v_2(D)=p_1,

and later excursions cannot alter the residue already fixed below their first
mismatch depth.

This is a same-integer/canonical-residue statement.  It does not by itself
exclude an open-positive tail that never returns to relative height zero.
"""

from itertools import product

H19 = "1101101101011011010"


def correction(bits, offset=0):
    R = 0
    for j, bit in enumerate(bits):
        if bit:
            R = 3 * R + (1 << (offset + j))
    return R


def v2(n):
    assert n != 0
    n = abs(n)
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def excursions(bits, mech):
    h = 0
    start = None
    out = []
    for i, (bit, ref) in enumerate(zip(bits, mech)):
        old = h
        h += bit - ref
        if h < 0:
            return None
        if old == 0 and h > 0:
            start = i
        if start is not None and h == 0:
            out.append((start, i + 1))
            start = None
    if h != 0:
        return None
    return out


def check_length(L):
    mech = tuple(int(c) for c in (H19 * ((L + 18) // 19))[:L])
    q = sum(mech)
    MOD = 1 << L
    inv3q = pow(3**q, -1, MOD)
    checked = 0

    for bits in product((0, 1), repeat=L):
        if sum(bits) != q:
            continue
        ex = excursions(bits, mech)
        if ex is None:
            continue

        checked += 1
        Rw = correction(bits)
        Rm = correction(mech)
        D = (-(Rw - Rm) * inv3q) % MOD

        Q = [0]
        for bit in bits:
            Q.append(Q[-1] + bit)

        parts = []
        first_positions = []
        for a, b in ex:
            dR = correction(bits[a:b], a) - correction(mech[a:b], a)
            assert dR != 0
            Dj = (-dR * pow(3**Q[b], -1, MOD)) % MOD
            p = next(i for i in range(a, b) if bits[i] != mech[i])
            assert v2(dR) == p
            assert v2(Dj) == p
            parts.append(Dj)
            first_positions.append(p)

        assert D == sum(parts) % MOD

        if parts:
            assert v2(D) == first_positions[0]
            partial = 0
            for j in range(len(parts) - 1):
                partial = (partial + parts[j]) % MOD
                # All later translations are divisible by 2^p_(j+1).
                assert (D - partial) % (1 << first_positions[j + 1]) == 0

    return checked


EXPECTED = {
    3: 1,
    4: 2,
    5: 3,
    6: 3,
    7: 7,
    8: 12,
    9: 12,
    10: 30,
    11: 30,
    12: 85,
    13: 173,
    14: 173,
}

counts = {L: check_length(L) for L in range(3, 15)}
assert counts == EXPECTED

print("root translation ultrametric locking: PASS")
print("exhaustive_relative_nonnegative_neutral_counts", counts)
print("max_checked_length", 14)
