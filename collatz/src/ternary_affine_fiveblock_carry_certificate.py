#!/usr/bin/env python3
"""Exact finite certificate for the five-block ternary-affine origin carry bound."""

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


def trajectory(x, bits):
    y = x
    got = []
    for _ in bits:
        got.append(y & 1)
        y = y // 2 if (y & 1) == 0 else (3 * y + 1) // 2
    return tuple(got), y


def transform(a, rho, e, bits):
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
    rho_p = y0 % Mp
    e_p = y0 // Mp
    return (r, q, c, x0, y0, a + q, rho_p, e_p)


def main():
    checked = 0
    max_ep = 0
    for a in range(0, 7):
        M = 3 ** a
        for rho in range(M):
            for e in (0, 1):
                A = rho + e * M
                if A < 1:
                    continue
                for bits in product((0, 1), repeat=5):
                    r, q, c, x0, y0, ap, rhop, ep = transform(
                        a, rho, e, bits
                    )
                    assert x0 >= A
                    assert (x0 - A) % M == 0
                    assert x0 % 32 == r % 32
                    assert x0 - 32 * M < A
                    got, endpoint = trajectory(x0, bits)
                    assert got == bits
                    assert endpoint == y0
                    assert 0 <= rhop < 3 ** ap
                    assert ep in (0, 1)
                    max_ep = max(max_ep, ep)
                    checked += 1

    print(f"checked={checked}")
    print(f"max_output_carry={max_ep}")


if __name__ == "__main__":
    main()
