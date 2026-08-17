#!/usr/bin/env python3
"""Exact current-R1 G13 entrance upgrade after excluding E<=19.

Input theorem from the finite formation certificates:
    e_1539 >= 20.

For E=20..31, the exact relaxed run-cap optimizer is evaluated directly.
For E>=32, the coarse per-step product bound is already below 2^941 and
shrinks by a factor 1/2 whenever E is increased by one.

Therefore U_1539=x_1539+1 < 2^941 and hence x_1539 < 2^941.
Since 941=49*19+10, the natural 19-bit G13 cut obeys
    t_49 < 2^10,
    t_b = 0 for b>=50.
Thus 20026-941=19085 high address bits are forced to zero.
"""

from fractions import Fraction

NMAX = 6 * 3**44 + 1
U0 = Fraction(NMAX + 1, 1)
T = 1539
G13_L = 20026
BLOCK = 19


def floor_log2(q: Fraction) -> int:
    k = q.numerator.bit_length() - q.denominator.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
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


def coarse(evens: int) -> Fraction:
    return U0 * Fraction(3, 2) ** (T - evens) * Fraction(3, 4) ** evens


def main() -> None:
    expected = {
        20: 940, 21: 939, 22: 937, 23: 936,
        24: 934, 25: 932, 26: 931, 27: 929,
        28: 928, 29: 926, 30: 925, 31: 923,
    }
    for E, bitfloor in expected.items():
        U = greedy_max_final(E)
        assert floor_log2(U) == bitfloor
        assert U < (1 << 941)

    # At E=32 the coarse bound is already enough; every additional even
    # event replaces one 3/2 factor by 3/4, multiplying the bound by 1/2.
    assert floor_log2(coarse(32)) == 940
    assert coarse(32) < (1 << 941)
    for E in range(33, 80):
        assert coarse(E) == coarse(E - 1) / 2
        assert coarse(E) < (1 << 941)

    assert 941 == 49 * BLOCK + 10
    assert G13_L - 941 == 19085

    print("R1 G13 E>=20 / 941-bit entrance certificate: PASS")
    print("e_1539 >= 20; q_1539 <= 1519")
    print("x_1539 < 2^941")
    print("natural_cut t_49 < 2^10; t_b=0 for b>=50")
    print("forced_zero_high_G13_bits 19085")


if __name__ == "__main__":
    main()
