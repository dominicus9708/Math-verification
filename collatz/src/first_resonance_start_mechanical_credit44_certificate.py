#!/usr/bin/env python3
"""Exact start-boundary counterpart of the terminal alignment-credit theorem.

For the repaired first resonance, the all-mechanical parity prefix is compatible
with the start interval through 69 parity bits / 44 odd ordinals, but becomes
incompatible at 70 parity bits / 45 odd ordinals.

Hence every admissible first-resonance start must leave the mechanical ray
within its first 45 odd ordinals.
"""

A = 114_208_327_604
Q = 72_057_431_991
B = 1 << 71
LOW = B + 1
HIGH = (4 * B - 1) // 3
EXPECTED_69 = 2_927_051_879_996_215_679_995


def mech_pos(j: int) -> int:
    return ((j - 1) * A) // Q


def mechanical_prefix_residue(k: int):
    bits = [0] * k
    j = 1
    while True:
        p = mech_pos(j)
        if p >= k:
            break
        bits[p] = 1
        j += 1

    R = 0
    q = 0
    for i, bit in enumerate(bits):
        if bit:
            R = 3 * R + (1 << i)
            q += 1

    M = 1 << k
    rho = (-R * pow(pow(3, q), -1, M)) % M
    return rho, q


def first_in_band(rho: int, k: int):
    M = 1 << k
    n = rho
    if n < LOW:
        n += ((LOW - n + M - 1) // M) * M
    return n if n <= HIGH else None


def main() -> None:
    rho69, q69 = mechanical_prefix_residue(69)
    n69 = first_in_band(rho69, 69)
    assert q69 == 44
    assert n69 == EXPECTED_69

    rho70, q70 = mechanical_prefix_residue(70)
    n70 = first_in_band(rho70, 70)
    assert q70 == 45
    assert n70 is None

    print("PASS first-resonance start mechanical credit")
    print("k69_q", q69, "unique_start", n69)
    print("k70_q", q70, "start_candidates", 0)
    print("start mechanical odd-ordinal credit <=44")
    print("a displacement is forced within the first 45 odd ordinals")


if __name__ == "__main__":
    main()
