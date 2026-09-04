#!/usr/bin/env python3
"""Regression certificate for terminal defect/projective-observation redundancy.

For equal-count target/candidate right blocks with q_H >= L,

    z_H = 2^s Z - C(H*) (mod 3^L)

on a realized candidate block, and

    E_L = sum_{i=0}^{L-1} 3^i (2^A_i - 2^B_i)

for the final L right-indexed one-events.  The exact theorem is

    z_H = -E_L (mod 3^L).

If the right block begins at full-word offset p_R and F_L=2^p_R E_L, then

    z_H = -2^(-p_R) F_L (mod 3^L).

The finite examples below are implementation/orientation guards only.
"""


def correction(positions):
    q = len(positions)
    return sum((3 ** (q - 1 - j)) * (1 << a) for j, a in enumerate(positions))


def check_case(s, target_positions, candidate_positions, L, p_R):
    q_H = len(target_positions)
    assert len(candidate_positions) == q_H
    assert q_H >= L
    assert all(a < b for a, b in zip(target_positions, target_positions[1:]))
    assert all(a < b for a, b in zip(candidate_positions, candidate_positions[1:]))
    assert target_positions[-1] < s
    assert candidate_positions[-1] < s

    C_T = correction(target_positions)
    C_W = correction(candidate_positions)

    # Final ranked events, indexed from the right.
    A = [target_positions[-1 - i] for i in range(L)]
    B = [candidate_positions[-1 - i] for i in range(L)]
    E_L = sum((3 ** i) * ((1 << A[i]) - (1 << B[i])) for i in range(L))

    mod3 = 3 ** L

    # Earlier ranked events vanish modulo 3^L.
    assert (C_W - C_T) % mod3 == (-E_L) % mod3

    # Choose the canonical right-block entrance residue Y modulo 2^s so that
    # the candidate block is realized and the affine endpoint Z is integral.
    mod2 = 1 << s
    inv_3q = pow(pow(3, q_H, mod2), -1, mod2)
    Y = (-C_W * inv_3q) % mod2
    numerator = (3 ** q_H) * Y + C_W
    assert numerator % mod2 == 0
    Z = numerator // mod2

    z_H = (mod2 * Z - C_T) % mod3
    assert z_H == (C_W - C_T) % mod3
    assert z_H == (-E_L) % mod3

    # Absolute-coordinate form.
    F_L = (1 << p_R) * E_L
    inv_2p = pow(pow(2, p_R, mod3), -1, mod3)
    assert z_H == (-inv_2p * F_L) % mod3


# Deterministic small-block orientation and offset guards.
CASES = [
    (12, [0, 2, 4, 6, 8, 10], [0, 1, 3, 5, 7, 9], 4, 5),
    (14, [1, 3, 5, 8, 10, 12], [0, 2, 4, 7, 9, 11], 5, 7),
    (16, [0, 2, 5, 7, 10, 13, 15], [0, 1, 4, 6, 9, 12, 14], 6, 11),
]

for case in CASES:
    check_case(*case)

# Current A0 s=1 Route-B checkpoint constants.
T0 = 104_398_605_910
RIGHT_H_LENGTH = 630_138_897
P_R = T0 - RIGHT_H_LENGTH
L = 28
MOD = 3 ** L

assert P_R == 103_768_467_013
assert MOD == 22_876_792_454_961

POW2_P = pow(2, P_R, MOD)
INV_POW2_P = pow(POW2_P, -1, MOD)
assert POW2_P == 11_083_441_862_549
assert INV_POW2_P == 1_051_701_240_047
assert (POW2_P * INV_POW2_P) % MOD == 1

print("PASS terminal defect/projective observation redundancy certificate")
print("checkpoint_precision", L)
print("right_H_absolute_offset", P_R)
print("modulus", MOD)
print("2^p_mod_3^28", POW2_P)
print("2^-p_mod_3^28", INV_POW2_P)
print("state_consequence", "exact terminal defect => derived z_H; do not Cartesian-pair")
print("status", "EXACT state minimization; formation membership remains OPEN")
