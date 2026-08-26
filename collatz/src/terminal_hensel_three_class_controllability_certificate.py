#!/usr/bin/env python3
"""Exact local controllability audit for zero-target terminal Hensel lifts.

This certificate proves two facts:

1. after the required displacement parity is fixed, the three same-parity
   classes d,d+2,d+4 modulo 6 produce all three possible next ternary carry
   digits;
2. if boundary states are left arbitrary, every finite mechanical block admits
   a zero-cost d=0 Hensel path.

Therefore neither a sign-only discrepancy theorem nor a positive local block
cost theorem can close the first resonance without retaining the two boundary
states, ordering memory, and real displacement cost.

This is a structural audit, not a proof of the Collatz conjecture.
"""


def invpow2(d: int, mod: int) -> int:
    return pow(pow(2, d, mod), -1, mod)


def next_digit(K9: int, e: int, d: int) -> int:
    """Return K' mod 3 for K'=(K+2^(e-d))/3 in Z_3."""
    u = (pow(2, e, 9) * invpow2(d, 9)) % 9
    z = (K9 + u) % 9
    assert z % 3 == 0
    return (z // 3) % 3


def required_parity(K9: int, e: int) -> int:
    good = []
    for d in (0, 1):
        u3 = (pow(2, e, 3) * invpow2(d, 3)) % 3
        if (K9 + u3) % 3 == 0:
            good.append(d)
    assert len(good) == 1
    return good[0]


def zero_cost_block(exponents, terminal_carry=1):
    """Construct a d=0 Hensel path backwards across any finite block.

    Forward recurrence for d=0 is
        K_i = (K_{i-1} + 2^e_i)/3.
    Given the terminal unit K_L, define backwards
        K_{i-1} = 3 K_i - 2^e_i.
    Every predecessor is automatically a unit modulo 3 because
        K_{i-1} == -2^e_i (mod 3).
    """
    assert terminal_carry % 3 != 0
    carries = [None] * (len(exponents) + 1)
    carries[-1] = terminal_carry
    for i in range(len(exponents) - 1, -1, -1):
        carries[i] = 3 * carries[i + 1] - (1 << exponents[i])
        assert carries[i] % 3 != 0
        assert (carries[i] + (1 << exponents[i])) % 3 == 0
        assert (carries[i] + (1 << exponents[i])) // 3 == carries[i + 1]
    return carries


def main() -> None:
    for e in (0, 1):
        for K9 in range(9):
            if K9 % 3 == 0:
                continue
            p = required_parity(K9, e)

            vals = [next_digit(K9, e, p + 2*r) for r in range(3)]
            assert sorted(vals) == [0, 1, 2]

            for shift in range(0, 18, 2):
                d0 = p + shift
                vals2 = [next_digit(K9, e, d0 + 2*r) for r in range(3)]
                assert sorted(vals2) == [0, 1, 2]

    # Ordering lower-bound audit.
    for L in range(20):
        for p in (0, 1):
            d0 = L if L % 2 == p else L + 1
            assert d0 >= L and d0 % 2 == p

    # Exact arbitrary finite-block zero-cost construction.  Several unrelated
    # exponent patterns are used as regressions; the proof in zero_cost_block
    # is algebraic and does not depend on these examples.
    for exponents in (
        [0],
        [1, 0, 1, 1, 0],
        [7, 5, 4, 2, 1, 0],
        [12, 10, 9, 7, 5, 4, 2],
    ):
        zero_cost_block(exponents, terminal_carry=1)
        zero_cost_block(exponents, terminal_carry=2)

    print("PASS terminal Hensel controllability audit")
    print("same-parity actions d,d+2,d+4 exhaust next carry digits {0,1,2}")
    print("every finite mechanical block has a zero-cost path for a suitable boundary carry")
    print("therefore two-boundary conditioning is mathematically indispensable")


if __name__ == "__main__":
    main()
