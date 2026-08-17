#!/usr/bin/env python3
"""Exact first-defect / scaled-defect filter for different-q E=13 pullbacks.

For s=1,...,7 let E'=13-s and M=U_N-3^s U_N'.  The separate scaled-defect
certificate gives

    -113 <= M <= 3^s(2^(13-s)-1),
    M == U_N (mod 3^s),

and the m=44 ternary core leaves only the 2^s residues

    U_N == 4(1 + sum_{i<s} a_i 3^i) (mod 3^s).

The surviving R1 actual branch has first mechanical defect

    p in {2,5,8,10,13,16}.

If N_mech is the mechanical 73-bit canonical start, v2(N-N_mech)=p fixes

    N == N_mech + 2^p (mod 2^(p+1)).

Hence a proposed M fixes the alternate root residue

    U_N' == 3^(-s)(U_N-M) (mod 2^(p+1)),

so its first p+1 accelerated parity bits are determined exactly.

A class is removed if that prefix already uses more than E' even events, or if
the remaining E' events cannot cover the remaining time under the exact
relaxed odd-run maximizer.  The endpoint bound after the fixed prefix is

    U_B <= U_cap (3/2)^q_B,
    U_cap=(NMAX+115)/3^s.

No ordinary N is iterated.  The finite objects are scaled-defect values and
parity-prefix classes.
"""

from fractions import Fraction

T = 1539
NMAX = 5_908_625_413_101_667_397_287
NMECH = 4_697_939_311_072_332_635_131
CHANNELS = (2, 5, 8, 10, 13, 16)

EXPECTED = {
    1: {2:8266,5:8266,8:8105,10:7334,13:4980,16:2575},
    2: {2:8239,5:8239,8:7500,10:5980,13:3276,16:1365},
    3: {2:8217,5:8089,8:6134,10:4148,13:1712,16:620},
    4: {2:8197,5:7301,8:4099,10:2235,13:720,16:226},
    5: {2:8173,5:5365,8:2075,10:923,13:226,16:51},
    6: {2:7129,5:2805,8:734,10:277,13:45,16:9},
    7: {2:4069,5:892,8:158,10:40,13:4,16:0},
}


def pow2(k: int) -> Fraction:
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))


def floor_log2(q: Fraction) -> int:
    k = q.numerator.bit_length() - q.denominator.bit_length()
    while pow2(k) > q:
        k -= 1
    while pow2(k + 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    return (Fraction(3, 2) ** r * U + 1) / 2


def can_cover(U: Fraction, evens: int, needed: int) -> bool:
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        if total + r + 1 >= needed:
            return True
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U) >= needed


def core_residues(s: int):
    modulus = 3 ** s
    out = set()
    for mask in range(1 << s):
        z = 1
        for i in range(s):
            if (mask >> i) & 1:
                z += 3 ** i
        out.add((4 * z) % modulus)
    assert len(out) == 1 << s
    return out


def possible_M(s: int):
    upper = 3 ** s * (2 ** (13 - s) - 1)
    allowed = core_residues(s)
    modulus = 3 ** s
    return [m for m in range(-113, upper + 1) if m % modulus in allowed]


def parity_prefix(residue: int, B: int):
    x = residue
    bits = []
    for _ in range(B):
        bits.append(x & 1)
        x = (3 * x + 1) // 2 if x & 1 else x // 2
    return bits


def channel_survivors(s: int, p: int):
    Ealt = 13 - s
    B = p + 1
    modulus = 1 << B

    # v2(N-N_mech)=p fixes this complete dyadic prefix.
    Nres = (NMECH + (1 << p)) % modulus
    inv3s = pow(3 ** s, -1, modulus)

    Ucap = Fraction(NMAX + 115, 3 ** s)
    survivors = []

    for M in possible_M(s):
        Np_res = (((Nres + 1 - M) * inv3s) - 1) % modulus
        bits = parity_prefix(Np_res, B)
        used_even = bits.count(0)
        if used_even > Ealt:
            continue

        odd = B - used_even
        U_after = Ucap * Fraction(3 ** odd, 2 ** odd)
        if not can_cover(U_after, Ealt - used_even, T - B):
            continue

        survivors.append(M)

    return survivors


def main():
    print("different-q E13 first-defect/M filter: PASS")
    print("s p surviving_M")

    for s in range(1, 8):
        for p in CHANNELS:
            vals = channel_survivors(s, p)
            assert len(vals) == EXPECTED[s][p]
            print(s, p, len(vals))

    assert channel_survivors(7, 16) == []
    assert len(channel_survivors(7, 13)) == 4
    assert len(channel_survivors(7, 10)) == 40

    print("s=7,p=16 channel removed exactly")


if __name__ == "__main__":
    main()
