#!/usr/bin/env python3
"""Exact finite-horizon projective quotient for Route-B source channels.

A source channel has endpoint form

    T^h(X) = y + 3^q m.

For d future source-refinement bits, define

    Q_d = (y mod 2^d, 3^q mod 2^d).

For every common block B of length ell <= d, Q_d determines the selected
parameter residue m_B mod 2^ell and the child quotient Q_{d-ell}.  Thus Q_d
is an exact precision-consuming right congruence for the affine source-channel
control state.  Exact source intervals remain a separate payload.
"""

from itertools import product


def block_meta(bits):
    C = 0
    qB = 0
    for ell, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << ell)
            qB += 1
    return len(bits), qB, C


def block_residue(bits):
    ell, qB, C = block_meta(bits)
    mod = 1 << ell
    return (-C * pow(pow(3, qB, mod), -1, mod)) % mod


def exact_jump(y: int, q: int, bits):
    ell, qB, C = block_meta(bits)
    mod = 1 << ell
    rho = block_residue(bits)
    mB = ((rho - y) * pow(pow(3, q, mod), -1, mod)) % mod
    numer = (3**qB) * (y + (3**q) * mB) + C
    assert numer % mod == 0
    return numer // mod, q + qB, mB


def quotient(y: int, q: int, d: int):
    mod = 1 << d
    return y % mod, pow(3, q, mod)


def quotient_jump(state, bits, d: int):
    Y, A = state
    ell, qB, C = block_meta(bits)
    assert 1 <= ell <= d

    mod_ell = 1 << ell
    rho = block_residue(bits)
    mB = ((rho - (Y % mod_ell)) * pow(A % mod_ell, -1, mod_ell)) % mod_ell

    mod_d = 1 << d
    numer_mod = (pow(3, qB, mod_d) * (Y + A * mB) + C) % mod_d
    assert numer_mod % mod_ell == 0

    d2 = d - ell
    mod2 = 1 << d2
    Y2 = (numer_mod // mod_ell) % mod2
    A2 = (A * pow(3, qB, mod_d)) % mod2 if d2 else 0
    return (Y2, A2), mB


transition_checks = 0
congruence_pair_checks = 0

for d in range(1, 9):
    order = 1 if d == 1 else (2 if d == 2 else 1 << (d - 2))
    for y in range(-5, 10):
        for q in range(10):
            Q = quotient(y, q, d)

            # A deliberately different exact representative of the same Q_d.
            yp = y + 3 * (1 << d)
            qp = q + 2 * order
            assert quotient(yp, qp, d) == Q

            for ell in range(1, d + 1):
                for bits in product((0, 1), repeat=ell):
                    y2, q2, mB = exact_jump(y, q, bits)
                    got_Q, got_mB = quotient_jump(Q, bits, d)
                    assert got_mB == mB
                    assert got_Q == quotient(y2, q2, d - ell)
                    transition_checks += 1

                    yp2, qp2, mpB = exact_jump(yp, qp, bits)
                    assert mpB == mB
                    assert quotient(yp2, qp2, d - ell) == quotient(y2, q2, d - ell)
                    congruence_pair_checks += 1

assert transition_checks == 150_600
assert congruence_pair_checks == 150_600

print("PASS A0 s=1 Route-B source-channel projective quotient certificate")
print("max_precision", 8)
print("transition_checks", transition_checks)
print("congruence_pair_checks", congruence_pair_checks)
print("quotient", "Q_d=(y mod 2^d, 3^q mod 2^d)")
print("exact_result", "a block of length ell consumes ell quotient bits and preserves Q_{d-ell} equivalence")
print("payload_audit", "finite source interval is not merged into Q_d; it remains an exact payload")
print("dsd_audit", "projective finite-horizon channel equivalence is exact; horizon-independent finite-state closure remains open")
