#!/usr/bin/env python3
"""Exact terminal-residue -> final-L-block -> critical right-H transfer certificate.

This certificate closes the ternary dependency chain

    Z mod 3^ell
      -> full threshold correction defect N_J mod 3^ell
      -> final L-block correction defect Delta_L mod 3^ell
      -> critical-cut right-H defect Delta_H mod 3^ell
      -> backward-chart root carry z_req mod 3^ell.

Conventions
-----------
For words A,B written left-to-right with A first,

    C(AB) = 3^{q(B)} C(A) + 2^{|A|} C(B).

For a target/candidate pair with equal length/count, the forward defect is

    Delta = C(target) - C(candidate).

The backward exponential carry chart uses candidate-minus-target atoms,
so its root carry is -Delta_H modulo 3^ell.

No statistical independence is used.  The terminal ternary observation is an
affine synchronization coordinate with Z, not an independently multiplicative
filter.

Exact root parameters
---------------------
    J0 = 10,439,860,591
    R0 =  6,586,818,670
    t0 = 10*J0
    j0 = 10*R0 + 1

Threshold word:
    W_th = U L^9.

The final L block has length J0 and R0 ones.  At the certified critical cut

    c = 9,809,721,694
    s =   630,138,897
    c+s = J0

the right factor is H_s^* and has

    q_H = 397,573,380

ones.

For every ternary precision ell <= min(R0,q_H),

    N_J      = C(W_th) - C(W)
    Delta_L  = C(L^*)  - C(L_candidate)
    Delta_H  = C(H_s^*)- C(H_candidate)

obey

    N_J     == C(W_th) - 2^t0 Z                     (mod 3^ell)
    Delta_L == 2^(-9J0) N_J                         (mod 3^ell)
    Delta_H == 2^(-c) Delta_L                       (mod 3^ell)

and therefore

    Delta_H == C(H_s^*) - 2^s Z                     (mod 3^ell)
    C(H_candidate) == 2^s Z                         (mod 3^ell).

The backward-chart root carry is

    z_req == -Delta_H == 2^s Z - C(H_s^*)           (mod 3^ell).

The practical precisions ell = 18,24,28,47 are certified below without
constructing the 630,138,897-bit H word.  Only its last ell ranked-one
positions contribute modulo 3^ell.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product

J0 = 10_439_860_591
R0 = 6_586_818_670
t0 = 104_398_605_910
j0 = 65_868_186_701

c = 9_809_721_694
s = 630_138_897
qH = 397_573_380

PRECISIONS = (18, 24, 28, 47)

EXPECTED = {
    18: {
        "M": 387_420_489,
        "two_s": 139_937_030,
        "C_H": 20_406_043,
        "minus_C_H": 367_014_446,
        "inv_two_s": 38_405_528,
        "first_tail_one": 630_138_870,
        "last_tail_one": 630_138_896,
    },
    24: {
        "M": 282_429_536_481,
        "two_s": 169_442_690_723,
        "C_H": 135_230_156_704,
        "minus_C_H": 147_199_379_777,
        "inv_two_s": 117_039_393_206,
        "first_tail_one": 630_138_860,
        "last_tail_one": 630_138_896,
    },
    28: {
        "M": 22_876_792_454_961,
        "two_s": 12_596_342_295_887,
        "C_H": 2_677_095_985_033,
        "minus_C_H": 20_199_696_469_928,
        "inv_two_s": 17_062_811_582_066,
        "first_tail_one": 630_138_854,
        "last_tail_one": 630_138_896,
    },
    47: {
        "M": 26_588_814_358_957_503_287_787,
        "two_s": 16_163_172_281_939_751_936_170,
        "C_H": 5_836_864_555_257_551_064_118,
        "minus_C_H": 20_751_949_803_699_952_223_669,
        "inv_two_s": 5_262_100_326_525_769_175_294,
        "first_tail_one": 630_138_824,
        "last_tail_one": 630_138_896,
    },
}


def log_bounds(z: Fraction, n: int = 100):
    acc = Fraction(0)
    for k in range(n + 1):
        acc += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2)
        * z ** (2 * n + 3)
        / ((2 * n + 3) * (1 - z * z))
    )
    return acc, acc + tail


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


def h_target_bit(i: int) -> int:
    assert i >= 0
    if i == 0:
        return 1
    return floor_alpha(i + 1) - floor_alpha(i)


def last_h_one_positions(h: int, ell: int):
    assert h >= 1 and ell >= 1
    out = []
    i = h - 1
    while i >= 0 and len(out) < ell:
        if h_target_bit(i):
            out.append(i)
        i -= 1
    assert len(out) == ell
    return tuple(reversed(out))


def h_target_correction_mod(h: int, ell: int) -> int:
    M = 3 ** ell
    pos = last_h_one_positions(h, ell)
    return sum(
        pow(3, ell - 1 - j, M) * pow(2, a, M)
        for j, a in enumerate(pos)
    ) % M


def correction(bits):
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def q(bits):
    return sum(bits)


def compose_correction(A, B):
    return (3 ** q(B)) * correction(A) + (2 ** len(A)) * correction(B)


composition_checks = 0
suffix_projection_checks = 0
critical_projection_checks = 0
sign_checks = 0

for hA in range(0, 4):
    for hB in range(1, 5):
        for A in product((0, 1), repeat=hA):
            for B in product((0, 1), repeat=hB):
                assert correction(A + B) == compose_correction(A, B)
                composition_checks += 1

for Astar in product((0, 1), repeat=3):
    for A in product((0, 1), repeat=3):
        if q(Astar) != q(A):
            continue
        for Bstar in product((0, 1), repeat=4):
            for B in product((0, 1), repeat=4):
                if q(Bstar) != q(B):
                    continue
                Delta_full = correction(Astar + Bstar) - correction(A + B)
                Delta_B = correction(Bstar) - correction(B)
                qb = q(Bstar)
                for ell in range(1, qb + 1):
                    M = 3 ** ell
                    projected = (
                        pow(pow(2, len(A), M), -1, M) * Delta_full
                    ) % M
                    assert projected == Delta_B % M
                    suffix_projection_checks += 1

for LeftStar in product((0, 1), repeat=3):
    for Left in product((0, 1), repeat=3):
        if q(LeftStar) != q(Left):
            continue
        for Hstar in product((0, 1), repeat=4):
            for H in product((0, 1), repeat=4):
                if q(Hstar) != q(H):
                    continue
                Delta_L = (
                    correction(LeftStar + Hstar) - correction(Left + H)
                )
                Delta_H = correction(Hstar) - correction(H)
                qh = q(Hstar)
                for ell in range(1, qh + 1):
                    M = 3 ** ell
                    projected = (
                        pow(pow(2, len(Left), M), -1, M) * Delta_L
                    ) % M
                    assert projected == Delta_H % M
                    critical_projection_checks += 1

                    z_req = (-Delta_H) % M
                    assert z_req == (correction(H) - correction(Hstar)) % M
                    sign_checks += 1


assert t0 == 10 * J0
assert j0 == 10 * R0 + 1
assert c + s == J0
assert floor_alpha(J0) == R0
assert floor_alpha(s) + 1 == qH
assert 9 * J0 + c + s == t0
assert all(ell <= min(R0, qH) for ell in PRECISIONS)

rows = []
for ell in PRECISIONS:
    M = 3 ** ell
    positions = last_h_one_positions(s, ell)
    C_H = h_target_correction_mod(s, ell)
    two_s = pow(2, s, M)
    inv_two_s = pow(two_s, -1, M)

    got = {
        "M": M,
        "two_s": two_s,
        "C_H": C_H,
        "minus_C_H": (-C_H) % M,
        "inv_two_s": inv_two_s,
        "first_tail_one": positions[0],
        "last_tail_one": positions[-1],
    }
    assert got == EXPECTED[ell]

    assert (two_s * inv_two_s) % M == 1
    for Z in (0, 1, 2, M // 2, M - 1):
        delta_H = (C_H - two_s * Z) % M
        z_req = (-delta_H) % M
        assert z_req == (two_s * Z - C_H) % M
        recovered_Z = (inv_two_s * (z_req + C_H)) % M
        assert recovered_Z == Z % M

    rows.append((ell, M, two_s, C_H, (-C_H) % M, inv_two_s))


print("PASS A0 s=1 Route-B terminal residue -> right-H transfer certificate")
print("parameters", J0, R0, t0, j0, c, s, qH)
print("composition_checks", composition_checks)
print("suffix_projection_checks", suffix_projection_checks)
print("critical_projection_checks", critical_projection_checks)
print("backward_sign_checks", sign_checks)
for row in rows:
    print(
        "join",
        "ell", row[0],
        "M", row[1],
        "two_s", row[2],
        "C_H", row[3],
        "minus_C_H", row[4],
        "inv_two_s", row[5],
    )
print(
    "exact_chain",
    "N_J -> final-L defect -> critical right-H defect -> z_req = -Delta_H",
)
print(
    "terminal_join",
    "z_req == 2^s * Z - C(H_s*) (mod 3^ell); "
    "equivalently C(H_candidate) == 2^s * Z (mod 3^ell)",
)
print(
    "dsd_audit",
    "terminal ternary residue is an affine synchronization coordinate with Z; "
    "no marginal-density independence multiplication is licensed",
)
print(
    "status",
    "terminal-residue/right-H transfer CLOSED for every ell<=min(R0,qH); "
    "projective-path inverse compression and physical root closure remain OPEN",
)
