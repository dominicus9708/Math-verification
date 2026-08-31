#!/usr/bin/env python3
"""Online parameter-residue <-> parity transducer for A0 s=1 Route-B.

A source channel has

    T^h(X) = y + g m,    g = 3^q odd.

Write the current parameter as m = e + 2 n with e in {0,1}.  Then the next
parity bit is

    b = (y + e) mod 2,

and the child affine channel is obtained exactly by dividing out this source
parameter bit.  Thus parameter bits and parity bits are related by an online
triangular bijection, not merely by a batch permutation at depth ell.

At finite precision d the transition depends only on

    Q_d = (y mod 2^d, g mod 2^d)

and consumes one bit of precision.  The certificate compares the online
transition with exact integer representatives and with the existing batch
block-to-parameter residue formula.
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


def block_residue_for_parent(y: int, q: int, bits):
    ell, qB, C = block_meta(bits)
    mod = 1 << ell
    rho = (-C * pow(pow(3, qB, mod), -1, mod)) % mod
    return ((rho - y) * pow(pow(3, q, mod), -1, mod)) % mod


def exact_parameter_bit_step(y: int, q: int, e: int):
    assert e in (0, 1)
    g = 3**q
    b = (y + e) & 1
    if b == 0:
        numer = y + g * e
        assert numer % 2 == 0
        return numer // 2, q, b
    numer = 3 * (y + g * e) + 1
    assert numer % 2 == 0
    return numer // 2, q + 1, b


def quotient(y: int, q: int, d: int):
    if d == 0:
        return (0, 0)
    mod = 1 << d
    return (y % mod, pow(3, q, mod))


def quotient_parameter_bit_step(Q, d: int, e: int):
    assert d >= 1
    assert e in (0, 1)
    Y, G = Q
    b = (Y + e) & 1
    if b == 0:
        numer = Y + G * e
        assert numer % 2 == 0
        G2_full = G
    else:
        numer = 3 * (Y + G * e) + 1
        assert numer % 2 == 0
        G2_full = 3 * G

    d2 = d - 1
    if d2 == 0:
        Q2 = (0, 0)
    else:
        mod2 = 1 << d2
        Q2 = ((numer // 2) % mod2, G2_full % mod2)
    return Q2, b


def online_from_parameter_residue(y: int, q: int, residue: int, d: int):
    bits = []
    yy, qq = y, q
    m = residue
    for _ in range(d):
        e = m & 1
        yy, qq, b = exact_parameter_bit_step(yy, qq, e)
        bits.append(b)
        m >>= 1
    return tuple(bits), yy, qq


def online_from_quotient(Q, residue: int, d: int):
    bits = []
    state = Q
    m = residue
    remaining = d
    while remaining:
        e = m & 1
        state, b = quotient_parameter_bit_step(state, remaining, e)
        bits.append(b)
        m >>= 1
        remaining -= 1
    return tuple(bits), state


def recover_parameter_residue(Q, parity_bits):
    """Online inverse: output parity bit b determines e=(b-Y) mod 2."""
    state = Q
    d = len(parity_bits)
    residue = 0
    for i, b in enumerate(parity_bits):
        Y, _G = state
        e = (b - Y) & 1
        residue |= e << i
        state2, emitted = quotient_parameter_bit_step(state, d - i, e)
        assert emitted == b
        state = state2
    return residue, state


MAX_D = 8
exact_transition_checks = 0
quotient_transition_checks = 0
batch_bijection_checks = 0
inverse_checks = 0
equivalent_representative_checks = 0

for d in range(1, MAX_D + 1):
    order = 1 if d == 1 else (2 if d == 2 else 1 << (d - 2))
    for y in range(-5, 10):
        for q in range(10):
            Q = quotient(y, q, d)

            yp = y + 3 * (1 << d)
            qp = q + 2 * order
            assert quotient(yp, qp, d) == Q

            for e in (0, 1):
                y2, q2, b = exact_parameter_bit_step(y, q, e)
                Q2, qb = quotient_parameter_bit_step(Q, d, e)
                assert qb == b
                assert Q2 == quotient(y2, q2, d - 1)
                exact_transition_checks += 1
                quotient_transition_checks += 1

            # Exhaust every d-bit parameter residue.  The emitted parity words
            # must be a permutation and must agree with the batch formula.
            seen_words = set()
            for residue in range(1 << d):
                bits, y2, q2 = online_from_parameter_residue(y, q, residue, d)
                qbits, Qend = online_from_quotient(Q, residue, d)
                assert qbits == bits
                assert Qend == quotient(y2, q2, 0)

                batch_residue = block_residue_for_parent(y, q, bits)
                assert batch_residue == residue
                batch_bijection_checks += 1

                recovered, recovered_end = recover_parameter_residue(Q, bits)
                assert recovered == residue
                assert recovered_end == Qend
                inverse_checks += 1

                bits_p, _yp2, _qp2 = online_from_parameter_residue(yp, qp, residue, d)
                assert bits_p == bits
                equivalent_representative_checks += 1

                seen_words.add(bits)

            assert len(seen_words) == 1 << d


print("PASS A0 s=1 Route-B online parameter/parity transducer certificate")
print("max_precision", MAX_D)
print("exact_transition_checks", exact_transition_checks)
print("quotient_transition_checks", quotient_transition_checks)
print("batch_bijection_checks", batch_bijection_checks)
print("inverse_checks", inverse_checks)
print("equivalent_representative_checks", equivalent_representative_checks)
print(
    "exact_result",
    "parameter residue bits and parity bits are related by an online triangular bijection; Q_d is sufficient and one bit of precision is consumed per step",
)
print(
    "family_cover_consequence",
    "a parity-state classifier can be pulled back to parameter residues by a product transducer/DAG rather than by materializing all residue addresses first",
)
print(
    "dsd_audit",
    "the transducer gives exact recursive generation, not a proof that the number of reachable quotient nodes is polynomial or horizon-independent",
)
print(
    "status",
    "online residue-language generation primitive CLOSED; quantitative state-merging/global membership remains OPEN",
)
