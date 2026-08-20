#!/usr/bin/env python3
"""
Exact certificate for the Hensel-digit form of the ternary-syndrome
five-block transition and its macro generalization.

The normalized progression state is
    x = rho + e*3^a + 3^a u,  u>=0,
with 0<=rho<3^a and e in {0,1}.

For one five-step parity word, the CRT intersection can be solved on the
2-adic side by one digit j mod 32.  This certificate checks that formula
against the direct ternary-side CRT construction exhaustively for a<=6.
It also checks the B=10 macro formula against two sequential five-step
transitions on a finite exact grid.
"""

from __future__ import annotations

from itertools import product


def canonical_word(bits):
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
    return r, q, y


def direct_transition(a, rho, e, bits):
    M = 3 ** a
    A = rho + e * M
    r, q, c = canonical_word(bits)

    if M == 1:
        t0 = 0
    else:
        t0 = ((rho - r) % M) * pow(32, -1, M) % M

    x_res = r + 32 * t0
    n = 0 if x_res >= A else 1
    x0 = x_res + n * 32 * M
    t = (x0 - r) // 32
    y0 = c + (3 ** q) * t

    Mp = M * (3 ** q)
    return x0, y0, a + q, y0 % Mp, y0 // Mp


def hensel_transition(a, rho, e, bits):
    M = 3 ** a
    r, q, c = canonical_word(bits)

    # Unique CRT digit on the dyadic side.
    j = ((r - rho) * pow(M, -1, 32)) % 32

    # The normalized floor carry can only persist through j=0; it is never born.
    e2 = 1 if (e == 1 and j == 0) else 0

    # After removing the possible whole output modulus, rho' is independent of e.
    d0 = (rho - r + j * M) // 32
    rho2 = c + (3 ** q) * d0
    a2 = a + q
    M2 = 3 ** a2

    x0 = rho + (j + 32 * e2) * M
    y0 = rho2 + e2 * M2
    return x0, y0, a2, rho2, e2, j


def macro_formula(a, rho, bits):
    """Macro formula for an input with e=0."""
    B = len(bits)
    M = 3 ** a
    mod2 = 1 << B
    r, q, c = canonical_word(bits)
    J = ((r - rho) * pow(M, -1, mod2)) % mod2
    x0 = rho + J * M
    d = (rho - r + J * M) // mod2
    rho2 = c + (3 ** q) * d
    a2 = a + q
    assert 0 < rho2 < 3 ** a2
    return x0, rho2, a2, J


def sequential_two_blocks(a, rho, bits10):
    assert len(bits10) == 10
    e = 0
    x1, y1, a1, rho1, e1, _ = hensel_transition(a, rho, e, bits10[:5])
    assert e1 == 0
    x2, y2, a2, rho2, e2, _ = hensel_transition(a1, rho1, e1, bits10[5:])
    assert e2 == 0

    # y2 is the endpoint obtained after ten steps from the least start in the
    # original progression that lies in the ten-bit parity cylinder.  Verify
    # that directly rather than identifying x2 (which lives in endpoint space)
    # with the original-space macro start.
    xm, rhom, am, J = macro_formula(a, rho, bits10)
    _, q10, c10 = canonical_word(bits10)
    ym = c10 + (3 ** q10) * ((xm - canonical_word(bits10)[0]) // (1 << 10))
    assert ym == rhom
    assert am == a2
    assert rhom == rho2
    return J


def main():
    one_block_checks = 0
    carry_births = 0

    for a in range(0, 7):
        M = 3 ** a
        for rho in range(M):
            for e in (0, 1):
                if rho + e * M < 1:
                    continue
                for bits in product((0, 1), repeat=5):
                    d = direct_transition(a, rho, e, bits)
                    h = hensel_transition(a, rho, e, bits)
                    assert d == h[:5]
                    if e == 0 and h[4] != 0:
                        carry_births += 1
                    one_block_checks += 1

    assert one_block_checks == 69728
    assert carry_births == 0

    macro_checks = 0
    # Exact B=10 macro/sequential agreement on a moderate exhaustive grid.
    for a in range(1, 4):
        M = 3 ** a
        for rho in range(1, M):
            for bits10 in product((0, 1), repeat=10):
                sequential_two_blocks(a, rho, bits10)
                macro_checks += 1

    print(f"one_block_checks={one_block_checks}")
    print(f"carry_births={carry_births}")
    print(f"macro_B10_checks={macro_checks}")
    print("ternary syndrome Hensel-digit/macro certificate: PASS")


if __name__ == "__main__":
    main()
