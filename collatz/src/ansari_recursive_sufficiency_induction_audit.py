#!/usr/bin/env python3
"""Exact regression audit for the first nontrivial step of Ansari's printed F_n induction.

This script does NOT decide whether F_2 is recursively sufficient.  It checks only:
  1. the exact residue sets F_1 and F_2 modulo 36;
  2. the n=1 specialization of the printed auxiliary F'_n and A'_n;
  3. the failure of the printed equality F_{n+1}=F'_n\A'_n at n=1;
  4. an exact affine merge proving 36*k+31 is recursive.

The remaining progression 36*k+27 is intentionally left as an open obligation.
"""


def f_residues(n: int):
    """Residues of F_n modulo 4*3^(n+1), enough to compare F_n with F_{n+1}."""
    modulus = 4 * 3 ** (n + 1)
    step = 4 * 3**n
    residues = set()
    # quotient k modulo 3 and n ternary 0/1 digits
    for kmod3 in range(3):
        for mask in range(1 << n):
            s = 0
            for i in range(n):
                if (mask >> i) & 1:
                    s += 3**i
            residues.add((step * kmod3 + 4 * s + 3) % modulus)
    return modulus, residues


def fprime1_residues():
    """n=1 specialization of the printed F'_n, modulo 36."""
    return {4 * (3 * a1 + a0) + 3 for a0 in range(3) for a1 in range(3)}


def aprime1_residues():
    """n=1 specialization of printed A'_n: a_0=a_1=2."""
    return {4 * (3 * 2 + 2) + 3}


def affine_shortcut_odd(pair):
    """T(Ak+B) for an everywhere-odd affine class."""
    A, B = pair
    assert A % 2 == 0 and B % 2 == 1
    return (3 * A // 2, (3 * B + 1) // 2)


def affine_shortcut_even(pair):
    """T(Ak+B) for an everywhere-even affine class."""
    A, B = pair
    assert A % 2 == 0 and B % 2 == 0
    return (A // 2, B // 2)


def main():
    mod1, F1 = f_residues(1)
    assert mod1 == 36
    _, F2_direct_finer = f_residues(2)
    # Reduce F2 modulo 36.  F2 has period 108, and reduction modulo 36 is sufficient here.
    F2 = {r % 36 for r in F2_direct_finer}

    assert F1 == {3, 7, 15, 19, 27, 31}
    assert F2 == {3, 7, 15, 19}
    removed = F1 - F2
    assert removed == {27, 31}

    Fp1 = fprime1_residues()
    Ap1 = aprime1_residues()
    printed_difference = Fp1 - Ap1

    assert Fp1 == {3, 7, 11, 15, 19, 23, 27, 31, 35}
    assert Ap1 == {35}
    assert printed_difference == {3, 7, 11, 15, 19, 23, 27, 31}
    assert printed_difference != F2

    # Exact affine merge for x=36k+31:
    # m=32k+27 -> 48k+41 -> 72k+62 -> 36k+31=x under shortcut T.
    x = (36, 31)
    two_x = (72, 62)
    z = (48, 41)
    m = (32, 27)
    assert affine_shortcut_odd(m) == z
    assert affine_shortcut_odd(z) == two_x
    assert affine_shortcut_even(two_x) == x
    # x-m = 4k+4 > 0 for every k>=0.
    assert x[0] - m[0] == 4 and x[1] - m[1] == 4

    print("SAFE finite-symbolic audit")
    print("F1 mod 36 =", sorted(F1))
    print("F2 mod 36 =", sorted(F2))
    print("F1\\F2 mod 36 =", sorted(removed))
    print("printed F'_1\\A'_1 mod 36 =", sorted(printed_difference))
    print("printed equality F2 = F'_1\\A'_1: FALSE")
    print("36k+31 recursion: CLOSED by affine merge to 32k+27 < 36k+31")
    print("36k+27 recursion: OPEN (not decided by this certificate)")


if __name__ == "__main__":
    main()
