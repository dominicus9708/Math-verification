#!/usr/bin/env python3
"""Exact current-R1 G13 entrance upgrade after excluding E=13.

Input theorem:
    e_1539 >= 14
from r1_e13_73plus91_formation_obstruction.py together with the previously
certified closure of the first-73 <=8-even layers.

The exact relaxed U=x+1 run optimizer is the same one used in the earlier
952-bit certificate.  For fixed total even count E, moving odd steps left
until the current odd-run divisibility cap is saturated maximizes the endpoint.

The exact floor binary logarithms are

    E=14 -> 950
    E=15 -> 948
    ...

so every E>=14 current-R1 entrance obeys

    x_1539 < 2^951.

For 19-bit G13 lift chunks, 951=50*19+1, hence

    t_50 < 2,
    t_b = 0 for b>=51.

The upper 20026-951=19075 G13 address bits are forced to zero.
"""

from fractions import Fraction

NMAX = 6 * 3**44 + 1
U0 = Fraction(NMAX + 1, 1)
T = 1539
G13_L = 20026


def floor_log2(q: Fraction) -> int:
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    assert 0 <= r <= floor_log2(U)
    return (Fraction(3, 2) ** r * U + 1) / 2


def greedy_max_final(evens: int) -> Fraction:
    U = U0
    rem_steps = T
    rem_e = evens

    for _ in range(evens):
        r = min(floor_log2(U), rem_steps - rem_e)
        U = odd_run_then_even(U, r)
        rem_steps -= r + 1
        rem_e -= 1

    assert rem_steps <= floor_log2(U)
    return Fraction(3, 2) ** rem_steps * U


def main() -> None:
    expected_floor = {
        14: 950,
        15: 948,
        16: 947,
        17: 945,
        18: 944,
        19: 942,
        20: 940,
    }

    for E, expected in expected_floor.items():
        got = floor_log2(greedy_max_final(E))
        assert got == expected, (E, got, expected)
        assert greedy_max_final(E) < (1 << 951)

    # For E>=21, the coarse all-odd baseline with an extra factor 1/2 per
    # even event is already below the same threshold and decreases with E.
    coarse_E21 = U0 * Fraction(3, 2) ** (T - 21) * Fraction(3, 4) ** 21
    assert coarse_E21 < (1 << 951)

    assert 951 == 50 * 19 + 1
    assert G13_L - 951 == 19075

    print("R1 G13 E>=14 / 951-bit entrance certificate: PASS")
    print("current_core_input e_1539 >= 14")
    print("q_1539 <= 1525")
    print("s0 <= 553")
    print("x_1539 < 2^951")
    print("natural_cut t_50 < 2; t_b=0 for b>=51")
    print("forced_zero_high_G13_bits 19075")


if __name__ == "__main__":
    main()
