#!/usr/bin/env python3
"""Regression certificate for the mixed forward/reverse constant-state identity.

For x=36*k+27, fix h>=2 and a dyadic k-cylinder

    k = 2^(h-2) u + c.

If the fixed h-step shortcut parity prefix has s odd states, then

    T^h(x) = 3^(s+2) u + B_h.

Writing the ordinary parity-affine formula

    T^h(n) = (3^s n + C_h)/2^h,

one has the exact congruence

    2^h B_h == C_h  (mod 3^(s+2)).

Thus the inverse-turn target B_h mod 3^(s+2) is recoverable from the standard
forward parity constant C_h.  The program checks every branch through h<=12.
"""


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def parity_affine_data(n: int, h: int):
    """Return (T^h(n), s, C, parity_bits) with 2^h*T^h(n)=3^s*n+C."""
    z = n
    s = 0
    C = 0
    bits = []
    for j in range(h):
        bit = z & 1
        bits.append(bit)
        if bit:
            C = 3 * C + (1 << j)
            s += 1
        z = T(z)
    assert (1 << h) * z == (3 ** s) * n + C
    return z, s, C, tuple(bits)


def branch_data(h: int, c: int):
    assert h >= 2
    scale = 1 << (h - 2)

    n0 = 36 * c + 27
    z0, s0, C0, bits0 = parity_affine_data(n0, h)

    n1 = 36 * (scale + c) + 27
    z1, s1, C1, bits1 = parity_affine_data(n1, h)

    assert bits0 == bits1
    assert s0 == s1
    # C depends only on the parity word, hence agrees too.
    assert C0 == C1

    A = z1 - z0
    B = z0
    assert A == 3 ** (s0 + 2)

    v = s0 + 2
    mod = 3 ** v
    assert ((1 << h) * B - C0) % mod == 0

    return s0, C0, B, bits0


def main():
    checked = 0
    for h in range(2, 13):
        for c in range(1 << (h - 2)):
            s, C, B, bits = branch_data(h, c)
            checked += 1

            # Check target evolution directly along one additional child bit.
            v = s + 2
            target = B % (3 ** v)

            for d in (0, 1):
                # Refine u=2u'+d.  The parity of the turning value is fixed by d.
                bit = (d + B) & 1
                if bit == 0:
                    Bnext = ((3 ** v) * d + B) // 2
                    vnext = v
                    target_expected = (target * pow(2, -1, 3 ** v)) % (3 ** v)
                else:
                    Bnext = ((3 ** (v + 1)) * d + 3 * B + 1) // 2
                    vnext = v + 1
                    target_expected = ((3 * target + 1) * pow(2, -1, 3 ** vnext)) % (3 ** vnext)
                assert Bnext % (3 ** vnext) == target_expected

    print("SAFE mixed-state regression")
    print("branches checked:", checked)
    print("identity: 2^h B_h == C_h mod 3^(s_h+2)")
    print("forward target child maps: even B/2, odd (3B+1)/2 in the appropriate 3-adic modulus")


if __name__ == "__main__":
    main()
