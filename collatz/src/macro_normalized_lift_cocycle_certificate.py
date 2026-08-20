#!/usr/bin/env python3
"""
Exact finite certificate for the Archimedean-normalized macro lift cocycle.

For v_s = 2^s rho / 3^a and a B-step block with lift digit J,

    v_{s+B} = v_s + 2^s J + 2^s R / 3^(a+Q).

For a zero-lift block J=0 in a coefficient-surviving state, the increment is
bounded by 2^(B-1)/3.  The script also exhaustively verifies the sharp block
correction bound R/3^Q <= 2^(B-1)/3 for B<=10.

This is a structural certificate, not a Collatz proof.
"""

from fractions import Fraction
from itertools import product


def barrier_table(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        p2 = 1 << k
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


BARRIER = barrier_table(128)


def T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def canonical_start(bits) -> int:
    B = len(bits)
    for r in range(1, (1 << B) + 1):
        y = r
        ok = True
        for bit in bits:
            if (y & 1) != bit:
                ok = False
                break
            y = T(y)
        if ok:
            return r
    raise AssertionError("missing canonical start")


def affine_data_from_bits(bits):
    B = len(bits)
    r = canonical_start(bits)
    y = r
    q = 0
    for bit in bits:
        assert (y & 1) == bit
        q += bit
        y = T(y)
    R = (1 << B) * y - (3 ** q) * r
    return r, q, R, y


def affine_data_from_start(x: int, B: int):
    y = x
    q = 0
    bits = []
    for _ in range(B):
        bit = y & 1
        bits.append(bit)
        q += bit
        y = T(y)
    R = (1 << B) * y - (3 ** q) * x
    return tuple(bits), q, R, y


def main() -> None:
    # Sharp absolute correction bound on a B-step parity word.
    word_checks = 0
    for B in range(1, 11):
        bound = Fraction(1 << (B - 1), 3)
        maximum = Fraction(0, 1)
        argmax = None
        for bits in product((0, 1), repeat=B):
            _, q, R, _ = affine_data_from_bits(bits)
            value = Fraction(R, 3 ** q)
            assert value <= bound
            if value > maximum:
                maximum = value
                argmax = bits
            word_checks += 1
        assert maximum == bound
        assert argmax == (0,) * (B - 1) + (1,)
        print(f"B={B}: max(R/3^Q)={maximum} at {''.join(map(str,argmax))}")

    # Exact cocycle check on normalized actual-prefix states.
    B = 5
    transition_checks = 0
    zero_checks = 0
    zero_bound = Fraction(1 << (B - 1), 3)

    for s in range(5, 11):
        for h in range(3):
            a = BARRIER[s] + h
            M = 3 ** a
            for rho in range(1, min(M, 50)):
                for J in range(1 << B):
                    seed = rho + M * J
                    _, q, R, rho_next = affine_data_from_start(seed, B)

                    v = Fraction((1 << s) * rho, M)
                    v_next = Fraction((1 << (s + B)) * rho_next, 3 ** (a + q))
                    rhs = v + (1 << s) * J + Fraction((1 << s) * R, 3 ** (a + q))
                    assert v_next == rhs
                    transition_checks += 1

                    if J == 0:
                        increment = v_next - v
                        assert increment >= 0
                        assert increment <= zero_bound
                        zero_checks += 1

    assert word_checks == sum(1 << B for B in range(1, 11))
    assert transition_checks == 28224
    print(f"word_checks={word_checks}")
    print(f"transition_checks={transition_checks}")
    print(f"zero_lift_checks={zero_checks}")
    print(f"B=5 sharp zero-lift increment bound={zero_bound}")
    print("macro normalized lift cocycle certificate: PASS")


if __name__ == "__main__":
    main()
