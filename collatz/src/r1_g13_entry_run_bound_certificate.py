#!/usr/bin/env python3
"""Exact relaxed run-length bounds at the R1 -> G13 handoff.

This certificate uses U=x+1 for the accelerated Collatz map. During an odd
run, U -> 3U/2 exactly. A run of r consecutive odd steps requires 2^r | U,
so r <= floor(log2 U). An even step maps U -> (U+1)/2.

For fixed step count and fixed number of even steps, the maximal relaxed final
U is obtained by moving odd steps left until the current run-length cap forces
an even step. This follows from the exact adjacent exchange

    O(E(U)) - E(O(U)) = 1/4 > 0,

so an allowed odd-before-even ordering dominates even-before-odd.

Combined with the separately certified current-core fact e_1539 >= 12, this
script proves x_1539 < 2^954 and the corresponding 19-bit natural-cut rule.
No floating-point arithmetic is used.
"""

from fractions import Fraction

NMAX = 6 * 3**44 + 1
U0 = Fraction(NMAX + 1, 1)
T = 1539
CUT = 73
BLOCK = 19
G13_L = 20026


def floor_log2(q: Fraction) -> int:
    if q <= 0:
        raise ValueError("positive rational required")
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    if r < 0 or r > floor_log2(U):
        raise ValueError("run exceeds relaxed divisibility cap")
    return (Fraction(3, 2) ** r * U + 1) / 2


def greedy_max_final(U: Fraction, steps: int, evens: int) -> Fraction:
    """Exact maximal U in the run-cap relaxation for fixed steps/evens."""
    rem_steps = steps
    rem_e = evens
    for _ in range(evens):
        # Leave one time step for every remaining even event.
        r = min(floor_log2(U), rem_steps - rem_e)
        U = odd_run_then_even(U, r)
        rem_steps -= r + 1
        rem_e -= 1
    if rem_steps > floor_log2(U):
        raise AssertionError("requested (steps,evens) is infeasible in relaxation")
    return Fraction(3, 2) ** rem_steps * U


def upper_after_cut(k_even: int) -> Fraction:
    # Odd: U -> 3U/2 exactly. Even: (U+1)/2 <= 3U/4 for U>=2.
    # Relative to an odd step, each even therefore costs a further factor 1/2.
    return U0 * Fraction(3, 2) ** CUT / (1 << k_even)


def greedy_cover(U: Fraction, evens: int) -> int:
    """Maximum further steps coverable with at most the given even events."""
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        total += r + 1
        U = odd_run_then_even(U, r)
    total += floor_log2(U)  # terminal odd run without another even
    return total


def max_cut_even_for_total(E: int) -> int:
    best = -1
    for k in range(E + 1):
        if greedy_cover(upper_after_cut(k), E - k) >= T - CUT:
            best = k
    return best


def main() -> None:
    expected = {
        5: 964, 6: 963, 7: 961, 8: 959, 9: 958, 10: 956, 11: 955,
        12: 953, 13: 951, 14: 950, 15: 948, 16: 947, 17: 945, 18: 944,
    }
    for E, bitfloor in expected.items():
        U = greedy_max_final(U0, T, E)
        got = floor_log2(U)
        assert got == bitfloor, (E, got, bitfloor)

    # Exact post-73 cover bounds. In particular E<=11 forces k_73<=7,
    # and E=12 forces k_73<=8.
    expected_k = {5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6, 11: 7, 12: 8}
    for E, kmax in expected_k.items():
        got = max_cut_even_for_total(E)
        assert got == kmax, (E, got, kmax)

    # Current-core finite certificate gives e_1539 >= 12. For E=12..18,
    # the exact relaxed maxima above are all below 2^954. For E>=19 the
    # coarse per-step product is already enough and decreases with E.
    for E in range(12, 19):
        assert greedy_max_final(U0, T, E) < (1 << 954)

    coarse_E19 = U0 * Fraction(3, 2) ** (T - 19) * Fraction(3, 4) ** 19
    assert coarse_E19 < (1 << 954)

    # Thus x_1539+1 < 2^954, hence x_1539 < 2^954.
    # Since 954 = 50*19 + 4, chunk index 50 has only four available bits
    # and every later 19-bit canonical lift chunk must vanish.
    assert 954 == 50 * BLOCK + 4
    assert G13_L > 954
    chunk50_bound = 1 << 4
    forced_zero_high_bits = G13_L - 954
    assert chunk50_bound == 16
    assert forced_zero_high_bits == 19072

    print("R1->G13 relaxed run-bound certificate: PASS")
    print("current_core_input: e_1539 >= 12")
    print("x_1539 < 2^954")
    print("natural_cut: t_50 < 16 and t_b = 0 for all b >= 51")
    print("forced_zero_high_G13_bits", forced_zero_high_bits)
    print("cut_even_max_for_E11", max_cut_even_for_total(11))
    print("cut_even_max_for_E12", max_cut_even_for_total(12))


if __name__ == "__main__":
    main()
