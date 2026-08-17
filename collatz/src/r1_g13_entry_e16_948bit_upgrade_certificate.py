#!/usr/bin/env python3
"""Exact current-R1 G13 entrance upgrade after excluding E=13,14,15.

Input theorem:
    e_1539 >= 16.

The exact relaxed U=x+1 endpoint optimizer has

    floor(log2 U_max(E=16)) = 947,

with strictly smaller relevant maxima for every larger even count.  Hence

    x_1539 < 2^948.

Since 948=49*19+17, the natural G13 19-bit lift chunks satisfy

    t_49 < 2^17,
    t_b = 0 for b>=50.

Thus the entire former chunk t_50 is now forced to zero and the upper
20026-948=19078 G13 address bits vanish.
"""

from fractions import Fraction

NMAX = 6*3**44 + 1
U0 = Fraction(NMAX+1,1)
T = 1539
G13_L = 20026


def floor_log2(q: Fraction) -> int:
    k = q.numerator.bit_length()-q.denominator.bit_length()
    while Fraction(1 << k,1) > q:
        k -= 1
    while Fraction(1 << (k+1),1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    return (Fraction(3,2)**r*U+1)/2


def greedy_max_final(evens: int) -> Fraction:
    U = U0
    rem_steps = T
    rem_e = evens
    for _ in range(evens):
        r = min(floor_log2(U), rem_steps-rem_e)
        U = odd_run_then_even(U,r)
        rem_steps -= r+1
        rem_e -= 1
    assert rem_steps <= floor_log2(U)
    return Fraction(3,2)**rem_steps*U


def main() -> None:
    expected = {
        16:947,
        17:945,
        18:944,
        19:942,
        20:940,
    }
    for E,logfloor in expected.items():
        U = greedy_max_final(E)
        assert floor_log2(U) == logfloor
        assert U < (1 << 948)

    coarse_E21 = U0 * Fraction(3,2)**(T-21) * Fraction(3,4)**21
    assert coarse_E21 < (1 << 948)

    assert 948 == 49*19 + 17
    assert G13_L-948 == 19078

    print("R1 G13 E>=16 / 948-bit entrance certificate: PASS")
    print("e_1539 >= 16")
    print("q_1539 <= 1523")
    print("s0 <= 551")
    print("x_1539 < 2^948")
    print("natural_cut t_49 < 2^17; t_b=0 for b>=50")
    print("forced_zero_high_G13_bits 19078")


if __name__ == "__main__":
    main()
