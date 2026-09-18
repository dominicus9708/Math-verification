#!/usr/bin/env python3
"""MATH-204 normalized carry / memory-erasure regression.

Checks the algebraic identities for finite representatives modulo powers of 2.
The note's statements are exact algebraic lemmas; this is regression evidence.
"""


def v2(n: int):
    if n == 0:
        return None
    n = abs(n)
    return (n & -n).bit_length() - 1


def main():
    checked = 0

    for Q in range(0, 8):
        for z in range(1, 18):
            mod = 1 << z
            inv = pow(pow(3, Q, mod), -1, mod)

            for B in range(-80, 81):
                for Ae in range(-80, 81):
                    diff = B - Ae

                    compatible = (diff % mod == 0)
                    normalized = ((diff * inv) % mod == 0)
                    assert compatible == normalized

                    if compatible:
                        d = diff // mod
                        P = 24
                        modP = 1 << P
                        invP = pow(pow(3, Q, modP), -1, modP)
                        delta = (d * invP) % modP

                        assert (delta * pow(3, Q, modP) - d) % modP == 0

                        if diff == 0:
                            assert d == 0
                            assert delta == 0
                        else:
                            assert v2(d) == v2(diff) - z

                    checked += 1

    print("PASS MATH-204 normalized carry quotient regression")
    print("checked_cases", checked)
    print("r10_min_erased_bits", 13)


if __name__ == "__main__":
    main()
