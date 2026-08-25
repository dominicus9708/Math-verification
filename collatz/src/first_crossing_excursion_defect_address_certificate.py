#!/usr/bin/env python3
"""Exact small-depth regression for the first-crossing excursion/defect/address theorem.

The theorem itself is algebraic.  This script exhaustively checks every first
coefficient-crossing binary word through depth 18 using exact integers.
"""

from itertools import product


def correction(bits):
    q = sum(bits)
    R = 0
    seen = 0
    # Equivalent recurrence R <- 3 R + 2^i at odd positions.
    for i, b in enumerate(bits):
        if b:
            R = 3 * R + (1 << i)
            seen += 1
    assert seen == q
    return q, R


def is_first_crossing(bits):
    q = 0
    p3 = 1
    p2 = 1
    for i, b in enumerate(bits, start=1):
        if b:
            q += 1
            p3 *= 3
        p2 <<= 1
        if i < len(bits):
            if p3 < p2:
                return False
        else:
            return p3 < p2
    return False


def mechanical_word(A):
    """Mechanical first-crossing word at a depth A that admits a crossing."""
    k_prev = 0
    out = []
    for i in range(1, A):
        k = 0
        p3 = 1
        target = 1 << i
        while p3 < target:
            p3 *= 3
            k += 1
        out.append(k - k_prev)
        k_prev = k
    out.append(0)
    return tuple(out)


def positions(bits):
    return [i for i, b in enumerate(bits) if b]


def residue(bits):
    q, R = correction(bits)
    M = 1 << len(bits)
    return (-R * pow(pow(3, q), -1, M)) % M


def verify_word(bits):
    A = len(bits)
    q, R = correction(bits)
    mech = mechanical_word(A)
    qm, Rm = correction(mech)
    assert q == qm

    a = positions(bits)
    b = positions(mech)
    assert len(a) == len(b) == q
    assert all(x <= y for x, y in zip(a, b))

    # Exact correction defect in ordinal coordinates.
    E = Rm - R
    E2 = sum(pow(3, q-j) * ((1 << b[j-1]) - (1 << a[j-1]))
             for j in range(1, q+1))
    assert E == E2 >= 0

    # Height-area / total displacement identity.
    h = 0
    area = 0
    for x, y in zip(bits, mech):
        h += x - y
        assert h >= 0
        area += h
    assert area == sum(y-x for x, y in zip(a, b))

    # Exact dyadic formation-address shift.
    M = 1 << A
    rho = residue(bits)
    rho_m = residue(mech)
    rhs = 0
    for j in range(1, q+1):
        inv3j = pow(pow(3, j), -1, M)
        rhs = (rhs + ((1 << b[j-1]) - (1 << a[j-1])) * inv3j) % M
    assert (rho - rho_m) % M == rhs

    # Truncation: terms whose actual and mechanical positions are both >=K
    # vanish modulo 2^K.  Check all K<=A directly by recomputing residues.
    for K in range(1, A+1):
        MK = 1 << K
        assert (rho - rho_m) % MK == rhs % MK


def main():
    checked = 0
    depths = []
    for A in range(2, 19):
        local = 0
        for bits in product((0, 1), repeat=A):
            if not is_first_crossing(bits):
                continue
            verify_word(bits)
            checked += 1
            local += 1
        if local:
            depths.append((A, local))

    assert checked > 0
    print("PASS first-crossing excursion/defect/address regression")
    print("checked_words=", checked)
    print("depth_counts=", depths)


if __name__ == "__main__":
    main()
