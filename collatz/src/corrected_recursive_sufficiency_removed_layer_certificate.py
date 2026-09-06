#!/usr/bin/env python3
"""Regression certificate for the exact removed layer F_n \ F_{n+1}.

Definitions (reduced coordinate Y=(N-3)/4):

  F_n^Y = {3^n p + sum_{i<n} a_i 3^i : p>=0, a_i in {0,1}}.

Writing p=3p'+d with d in {0,1,2}, the next set F_{n+1} is exactly the
subfamily d in {0,1}.  Hence the removed layer is exactly d=2:

  A_n^Y = {3^(n+1)p' + 2*3^n + sum_{i<n} a_i 3^i}.

This finite program checks the residue identity for n=0..8.  The theorem is
algebraic and does not rely on the finite loop.
"""


def lower_01_sums(n: int):
    out = set()
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1:
                s += 3**i
        out.add(s)
    return out


def reduced_F_residues(n: int):
    """F_n^Y residues modulo 3^(n+1)."""
    M = 3 ** (n + 1)
    out = set()
    for d in range(3):
        for s in lower_01_sums(n):
            out.add((d * 3**n + s) % M)
    return M, out


def reduced_Fnext_residues(n: int):
    """F_{n+1}^Y residues modulo 3^(n+1)."""
    M = 3 ** (n + 1)
    out = set()
    for d in (0, 1):
        for s in lower_01_sums(n):
            out.add((d * 3**n + s) % M)
    return M, out


def removed_formula_residues(n: int):
    M = 3 ** (n + 1)
    return M, {(2 * 3**n + s) % M for s in lower_01_sums(n)}


def main():
    for n in range(9):
        M, Fn = reduced_F_residues(n)
        _, Fnext = reduced_Fnext_residues(n)
        _, removed = removed_formula_residues(n)
        assert Fn - Fnext == removed
        assert len(removed) == 2**n
        # Restore N=4Y+3.  The removed layer has 2^n residue classes modulo
        # 4*3^(n+1), one for each lower ternary 0/1 pattern.
        Nres = {(4 * y + 3) % (4 * M) for y in removed}
        assert len(Nres) == 2**n
        print(f"n={n}: modulus={4*M}, removed_classes={len(Nres)}, residues={sorted(Nres) if n<=3 else 'omitted'}")

    print("SAFE: F_n\\F_(n+1) is exactly the first-lowest ternary-digit-2 layer.")


if __name__ == "__main__":
    main()
