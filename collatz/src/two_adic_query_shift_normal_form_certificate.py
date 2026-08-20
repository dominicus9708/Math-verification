#!/usr/bin/env python3
"""
Exact finite certificate for the 2-adic query-shift normal form.

For a ternary progression x=rho+3^a u (zero floor carry), define the 2-adic
normalized query xi=3^{-a} rho.  For a B-bit parity word W with Q odd steps
and affine correction R_W,

    T^B(x) = (3^Q x + R_W)/2^B,

define gamma_W = 3^{-(a+Q)} R_W in Z_2.  The exact Hensel/min-plus digit is

    J_W = [-(xi+gamma_W)]_(2^B),

and the output normalized query is

    xi' = (xi + gamma_W + J_W)/2^B.

The script checks this identity against the direct CRT/canonical construction.
"""

from __future__ import annotations

from itertools import product


def canonical_data(bits):
    r = 1
    y = 1
    q = 0
    for k, bit in enumerate(bits):
        carry = bit ^ (y & 1)
        if carry:
            r += 1 << k
            y += 3 ** q
        if bit == 0:
            y //= 2
        else:
            y = (3 * y + 1) // 2
            q += 1
    B = len(bits)
    R = (1 << B) * y - (3 ** q) * r
    assert R >= 0
    return r, q, y, R


def direct_macro(a, rho, bits):
    B = len(bits)
    N = 1 << B
    M = 3 ** a
    r, q, c, R = canonical_data(bits)
    J = ((r - rho) * pow(M, -1, N)) % N
    x0 = rho + J * M
    assert x0 % N == r % N
    y0 = ((3 ** q) * x0 + R) // N
    a2 = a + q
    assert 0 < y0 < 3 ** a2
    return J, y0, a2, q, R


def shift_macro(a, rho, bits, precision_blocks=2):
    B = len(bits)
    J0, rho2, a2, q, R = direct_macro(a, rho, bits)

    P = precision_blocks * B
    MOD = 1 << P
    LOW = 1 << B

    xi = (rho * pow(3 ** a, -1, MOD)) % MOD
    gamma = (R * pow(3 ** a2, -1, MOD)) % MOD
    J = (-(xi + gamma)) % LOW
    assert J == J0
    assert (xi + gamma + J) % LOW == 0

    xi2_from_shift = ((xi + gamma + J) % MOD) >> B
    xi2_direct = (rho2 * pow(3 ** a2, -1, 1 << (P - B))) % (1 << (P - B))
    assert xi2_from_shift == xi2_direct
    return J


def main():
    checks = 0
    same_q_checks = 0

    for B in (5, 10):
        words = list(product((0, 1), repeat=B))
        for a in range(1, 4):
            M = 3 ** a
            for rho in range(1, M):
                for bits in words:
                    shift_macro(a, rho, bits, precision_blocks=2)
                    checks += 1

        # Correction-difference identity at finite 2-adic precision:
        # gamma_u-gamma_w = 3^{-(a+Q)}(R_u-R_w).
        data = [(bits, canonical_data(bits)) for bits in words]
        for a in (1, 2, 3):
            MOD = 1 << (2 * B)
            for i in range(min(len(data), 128)):
                _, (_, qi, _, Ri) = data[i]
                for j in range(min(len(data), 128)):
                    _, (_, qj, _, Rj) = data[j]
                    if qi != qj:
                        continue
                    Q = qi
                    gi = (Ri * pow(3 ** (a + Q), -1, MOD)) % MOD
                    gj = (Rj * pow(3 ** (a + Q), -1, MOD)) % MOD
                    rhs = ((Ri - Rj) * pow(3 ** (a + Q), -1, MOD)) % MOD
                    assert (gi - gj) % MOD == rhs
                    same_q_checks += 1

    print(f"query_shift_checks={checks}")
    print(f"same_q_correction_checks={same_q_checks}")
    print("2-adic query-shift normal-form certificate: PASS")


if __name__ == "__main__":
    main()
