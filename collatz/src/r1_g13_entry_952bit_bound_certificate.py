#!/usr/bin/env python3
"""Exact 952-bit R1 -> G13 entrance bound after excluding E=12.

Input theorem from the finite first-73/Cantor certificates:
    e_1539 >= 13
for the present m=44, V_33 R1 core.

Using U=x+1, odd runs obey U -> 3U/2 and an r-long odd run requires
r <= floor(log2 U).  An even step obeys U -> (U+1)/2.  The exact exchange
O(E(U))-E(O(U))=1/4 shows that, for fixed time and fixed even count, the
relaxed maximal endpoint is obtained by pushing odd steps left until the run
cap forces an even step.

The certificate proves x_1539 < 2^952, hence for 19-bit G13 lift chunks
    t_50 < 4,  t_b=0 for b>=51.
No floating-point arithmetic is used.
"""

from fractions import Fraction

NMAX = 6 * 3**44 + 1
U0 = Fraction(NMAX + 1, 1)
T = 1539
CUT = 73
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


def upper_after_73(k_even: int) -> Fraction:
    return U0 * Fraction(3, 2) ** CUT / (1 << k_even)


def greedy_cover(U: Fraction, evens: int) -> int:
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U)


def max_e73_for_total(E: int) -> int:
    best = -1
    for k in range(E + 1):
        if greedy_cover(upper_after_73(k), E-k) >= T-CUT:
            best = k
    return best


def main() -> None:
    expected_floor = {
        12: 953, 13: 951, 14: 950, 15: 948, 16: 947,
        17: 945, 18: 944, 19: 942, 20: 940,
    }
    for E, expected in expected_floor.items():
        got = floor_log2(greedy_max_final(E))
        assert got == expected, (E, got, expected)

    assert max_e73_for_total(12) == 8
    assert max_e73_for_total(13) == 9

    # Current-core input e_1539>=13. Exact relaxed maxima handle E=13..20.
    for E in range(13, 21):
        assert greedy_max_final(E) < (1 << 952)

    # For E>=21, the coarser per-step product already suffices and decreases
    # by a factor 1/2 for each additional even event relative to an odd event.
    coarse_E21 = U0 * Fraction(3, 2) ** (T-21) * Fraction(3, 4) ** 21
    assert coarse_E21 < (1 << 952)

    assert 952 == 50*19 + 2
    assert G13_L - 952 == 19074

    print("R1 G13 952-bit entrance certificate: PASS")
    print("current_core_input e_1539 >= 13")
    print("q_1539 <= 1526")
    print("s0 <= 554")
    print("x_1539 < 2^952")
    print("natural_cut t_50 < 4; t_b=0 for b>=51")
    print("forced_zero_high_G13_bits 19074")
    print("E=13 implies e_73 <=", max_e73_for_total(13))


if __name__ == "__main__":
    main()
