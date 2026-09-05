#!/usr/bin/env python3
"""Reduced layered source+ballot control for A0 s=1 Route-B.

At absolute parity depth h define the ballot endpoint discrepancy

    delta = q - floor(R h / J).

The source-channel quotient usually stores

    Q_d = (Y, G) = (y mod 2^d, 3^q mod 2^d).

But at a fixed layer h, q is reconstructed exactly from delta, so G is
redundant.  The layer phase R h mod J is also determined by h.  Therefore the
online source+ballot state can use

    (Y, delta, ballot_min, critical_phase)

with h and remaining dyadic precision supplied by the layer.  Fixed-resolution
correction residues can be appended independently.

This certificate checks the reduced transition against exact affine channel,
ballot and correction updates over all short parent parity prefixes and all
short future parameter residues.
"""

from itertools import product

R = 6_586_818_670
J = 10_439_860_591
K = 8
L = 6
MOD2 = 1 << K
MOD3 = 3**L


def exact_refine_channel(state, bit: int):
    h, y, q = state
    m0 = (bit - (y & 1)) & 1
    g = 3**q
    if bit == 0:
        numer = y + g * m0
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q
    else:
        numer = 3 * (y + g * m0) + 1
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q + 1
    return (h + 1, y2, q2)


def correction_append(C: int, h: int, bit: int):
    return C if bit == 0 else 3 * C + (1 << h)


def ballot_append(bmin: int, gcrit: int, h2: int, q2: int):
    discrepancy = q2 - (R * h2) // J
    phase = (R * h2) % J
    if discrepancy < bmin:
        return discrepancy, phase
    if discrepancy == bmin and phase > gcrit:
        return bmin, phase
    return bmin, gcrit


def build_parent(bits):
    state = (0, 0, 0)  # h,y,q
    C = 0
    bmin = 0
    gcrit = 0
    for bit in bits:
        h, y, q = state
        C = correction_append(C, h, bit)
        state = exact_refine_channel(state, bit)
        h2, _y2, q2 = state
        bmin, gcrit = ballot_append(bmin, gcrit, h2, q2)
    return state, C, bmin, gcrit


def reduced_state(exact_state, C: int, bmin: int, gcrit: int, d: int):
    h, y, q = exact_state
    mod = 1 << d
    delta = q - (R * h) // J
    return (y % mod, delta, bmin, gcrit, C % MOD2, C % MOD3)


def reduced_source_bit_step(S, h: int, d: int, eta: int):
    assert d >= 1
    assert eta in (0, 1)
    Y, delta, bmin, gcrit, C2, C3 = S

    # Reconstruct the omitted q and G coordinates from layer + discrepancy.
    q = delta + (R * h) // J
    assert q >= 0
    G = pow(3, q, 1 << d)

    bit = (Y + eta) & 1
    if bit == 0:
        numer = Y + G * eta
        Gmult = 1
    else:
        numer = 3 * (Y + G * eta) + 1
        Gmult = 3
    assert numer % 2 == 0

    d2 = d - 1
    Y2 = 0 if d2 == 0 else (numer // 2) % (1 << d2)

    floor_jump = (R * (h + 1)) // J - (R * h) // J
    assert floor_jump in (0, 1)
    delta2 = delta + bit - floor_jump

    phase2 = (R * (h + 1)) % J
    if delta2 < bmin:
        bmin2, gcrit2 = delta2, phase2
    elif delta2 == bmin and phase2 > gcrit:
        bmin2, gcrit2 = bmin, phase2
    else:
        bmin2, gcrit2 = bmin, gcrit

    if bit:
        C2 = (3 * C2 + pow(2, h, MOD2)) % MOD2
        C3 = (3 * C3 + pow(2, h, MOD3)) % MOD3

    return (Y2, delta2, bmin2, gcrit2, C2, C3), bit


parents = []
for H in range(5):
    for bits in product((0, 1), repeat=H):
        parents.append((bits, *build_parent(bits)))
assert len(parents) == 31

transition_checks = 0
path_checks = 0
coefficient_reconstruction_checks = 0

for parent_bits, exact0, C0, bmin0, gcrit0 in parents:
    H0, y0, q0 = exact0

    for d in range(1, 7):
        S0 = reduced_state(exact0, C0, bmin0, gcrit0, d)
        Y0, delta0, *_rest = S0
        q_recovered = delta0 + (R * H0) // J
        assert q_recovered == q0
        assert pow(3, q_recovered, 1 << d) == pow(3, q0, 1 << d)
        coefficient_reconstruction_checks += 1

        for residue in range(1 << d):
            exact = exact0
            C = C0
            bmin = bmin0
            gcrit = gcrit0
            S = S0
            m = residue
            rem = d

            while rem:
                eta = m & 1
                h, y, q = exact
                g = 3**q
                bit = (y + g * eta) & 1
                assert bit == ((y + eta) & 1)

                # Exact affine source-bit transition.
                if bit == 0:
                    numer = y + g * eta
                    y2 = numer // 2
                    q2 = q
                else:
                    numer = 3 * (y + g * eta) + 1
                    y2 = numer // 2
                    q2 = q + 1
                exact = (h + 1, y2, q2)

                C = correction_append(C, h, bit)
                bmin, gcrit = ballot_append(bmin, gcrit, h + 1, q2)

                S, emitted = reduced_source_bit_step(S, h, rem, eta)
                assert emitted == bit
                assert S == reduced_state(exact, C, bmin, gcrit, rem - 1)
                transition_checks += 1

                m >>= 1
                rem -= 1

            path_checks += 1


assert coefficient_reconstruction_checks == 31 * 6
assert path_checks == 31 * sum(1 << d for d in range(1, 7))

print("PASS A0 s=1 Route-B reduced source+ballot control certificate")
print("parent_prefixes", len(parents))
print("max_parent_depth", 4)
print("future_precision_max", 6)
print("correction_resolution", (K, L))
print("coefficient_reconstruction_checks", coefficient_reconstruction_checks)
print("path_checks", path_checks)
print("transition_checks", transition_checks)
print(
    "reduced_state",
    "layer h + (Y, endpoint discrepancy, ballot minimum, critical phase, correction mod 2^K, correction mod 3^L)",
)
print(
    "exact_result",
    "3^q mod 2^d, q, and the ballot length phase are redundant coordinates once layer h and endpoint discrepancy are retained",
)
print(
    "dsd_audit",
    "coordinate elimination is exact for the layered finite-horizon transducer; it does not by itself bound reachable states polynomially",
)
print(
    "status",
    "redundant source/ballot control coordinates CLOSED; quantitative reachable-state growth remains OPEN",
)
