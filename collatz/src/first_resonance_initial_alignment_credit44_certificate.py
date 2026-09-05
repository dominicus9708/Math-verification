#!/usr/bin/env python3
"""Exact first-resonance endpoint certificate for initial mechanical-alignment credit.

A length-m terminal zero-displacement Hensel run requires the ordinary endpoint
y to lie in one residue class modulo 3^m.  Combining that class with y==3 mod4
and the already-certified first-resonance near-return interval shows:

    m=44: exactly one endpoint candidate remains;
    m=45: no endpoint candidate remains.

Hence every first-resonance candidate has initial mechanical alignment depth
at most 44 and must use a positive repair displacement within the first 45
terminal odd ordinals.

No floating point, ternary selector, or local-pullback assumption is used.
"""

A = 114_208_327_604
Q = 72_057_431_991
B = 1 << 71
LOW = B + 1
HIGH = (4 * B + 3 * (1 << 33) - 1) // 3
EXPECTED_44 = 2_729_562_462_203_742_221_059


def mech(j: int) -> int:
    # Farey-floor identity is exact throughout the first-resonance cell.
    return ((j - 1) * A) // Q


def mechanical_tail_endpoint_residue(m: int) -> int:
    M = 3**m
    total = 0
    for ell in range(m):
        pos = mech(Q - ell)
        total = (total + pow(3, ell, M) * pow(2, pos, M)) % M
    inv_2A = pow(pow(2, A, M), -1, M)
    return (inv_2A * total) % M


def crt_with_mod4_three(r: int, m: int):
    M = 3**m
    k = ((3 - r) * pow(M, -1, 4)) % 4
    return r + k * M, 4 * M


def first_in_band(res: int, mod: int):
    k = max(0, (LOW - res + mod - 1) // mod)
    y = res + k * mod
    return y if y <= HIGH else None


def main() -> None:
    r44 = mechanical_tail_endpoint_residue(44)
    c44, mod44 = crt_with_mod4_three(r44, 44)
    y44 = first_in_band(c44, mod44)
    assert y44 == EXPECTED_44

    r45 = mechanical_tail_endpoint_residue(45)
    c45, mod45 = crt_with_mod4_three(r45, 45)
    y45 = first_in_band(c45, mod45)
    assert y45 is None

    # Any deeper zero-control alignment would imply the impossible m=45
    # congruence by reduction modulo 3^45.
    assert LOW <= EXPECTED_44 <= HIGH
    assert EXPECTED_44 % 4 == 3

    print("PASS first-resonance initial mechanical-alignment credit")
    print("endpoint_band", LOW, HIGH)
    print("m44_unique_endpoint", EXPECTED_44)
    print("m45_endpoint_candidates", 0)
    print("initial_alignment_depth<=44")
    print("first positive Hensel repair occurs within 45 terminal odd ordinals")


if __name__ == "__main__":
    main()
