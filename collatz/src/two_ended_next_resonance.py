#!/usr/bin/env python3
"""Exact rational/integer verifier for the two-ended residue core.

No floating point is used in any certified comparison.
"""
from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
N = 40
U_CERT = 36_797_925_187_243_805_015_225
EXPECTED_YMECH48 = 40_150_856_745_180_969_070_537


def log_bounds(x: Fraction):
    s = Fraction(0)
    for j in range(N + 1):
        s += Fraction(2) * x ** (2 * j + 1) / (2 * j + 1)
    tail = Fraction(2) * x ** (2 * N + 3) / ((2 * N + 3) * (1 - x * x))
    return s, s + tail


def certify_floor_log2_3_power(n: int, l2, u2, l3, u3) -> int:
    # A high-level estimate is used only to choose a tiny candidate neighborhood;
    # all returned values are then certified by exact rational inequalities.
    # For n near Q, use SIGMA and the small offset r=Q-n to avoid floats.
    r = Q - n
    # ceil(r log_2 3) lies in a very small ordinary range.
    c = 0
    while not (r * u3 < (c + 1) * l2):
        c += 1
    # Candidate k is near SIGMA-c-1 / SIGMA-c.
    for k in range(SIGMA - c - 3, SIGMA - c + 3):
        # sufficient exact certification of k ln2 < n ln3 < (k+1) ln2
        if k * u2 < n * l3 and n * u3 < (k + 1) * l2:
            return k
    raise RuntimeError((n, r, c))


def main():
    l2, u2 = log_bounds(Fraction(1, 3))
    l3, u3 = log_bounds(Fraction(1, 2))

    correction_upper = Fraction(Q, 1) / (6 * l2) + Fraction(1, 3)
    s_floor = correction_upper.numerator // correction_upper.denominator
    y_max = (U_CERT - 1) + s_floor

    assert 3**47 < y_max < 3**48

    kappas = [
        certify_floor_log2_3_power(i, l2, u2, l3, u3)
        for i in range(Q - 48, Q)
    ]

    modulus = 3**48
    r_tail = 0
    for j, i in enumerate(range(Q - 48, Q)):
        r_tail = (
            r_tail
            + pow(2, kappas[j], modulus) * pow(3, Q - 1 - i, modulus)
        ) % modulus

    inv_2_sigma = pow(pow(2, SIGMA, modulus), -1, modulus)
    y_mech = (inv_2_sigma * r_tail) % modulus

    assert y_mech == EXPECTED_YMECH48
    assert y_mech > y_max

    print("two-ended terminal certificate: PASS")
    print("endpoint ceiling:", y_max)
    print("3^47:", 3**47)
    print("3^48:", 3**48)
    print("mechanical last-48 endpoint residue:", y_mech)
    print("excess above endpoint ceiling:", y_mech - y_max)
    print("last-48 kappas:", kappas)


if __name__ == "__main__":
    main()
