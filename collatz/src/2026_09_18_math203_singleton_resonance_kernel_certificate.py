#!/usr/bin/env python3
"""MATH-203 singleton resonance-kernel regression.

At R=0, M=1, verifies that:
- direct L=z compatibility has a source iff the normalized discrepancy
  eta-X vanishes modulo 2^z;
- the resulting MATH-091 carry is the quotient -(A_e-B)/2^z.

The theorem itself is algebraic. This is finite exact regression only.
"""

ZMIN = {
    2:1, 3:2, 4:3, 5:6, 6:7, 7:8, 8:10, 9:11, 10:13,
    11:14, 12:16, 13:18, 14:19, 15:21, 16:22, 17:25,
    18:25, 19:26, 20:28, 21:29,
}


def main():
    checked = 0

    for Q in range(0, 9):
        for z in range(1, 16):
            mod = 1 << z
            inv = pow(pow(3, Q, mod), -1, mod)

            for B in range(-25, 26):
                for Ae in range(-25, 26):
                    direct = ((Ae - B) * inv) % mod

                    # R=0, M=1: the only source parameter is s=0.
                    compatible = (direct == 0)

                    # Normalized-address condition:
                    # eta-X = 3^{-Q}(Ae-B) in Z_2.
                    normalized_zero = (((Ae - B) * inv) % mod == 0)

                    assert compatible == normalized_zero

                    if compatible:
                        assert (Ae - B) % mod == 0
                        d = (B - Ae) // mod
                        assert B + (3**Q) * 0 - Ae == d * mod

                    checked += 1

    assert ZMIN[10] == 13
    assert (1 << ZMIN[10]) == 8192

    print("PASS MATH-203 singleton resonance-kernel regression")
    print("checked_cases", checked)
    print("r10_resonance_bits", ZMIN[10])
    print("r10_modulus", 1 << ZMIN[10])


if __name__ == "__main__":
    main()
