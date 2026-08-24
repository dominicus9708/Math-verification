#!/usr/bin/env python3
"""Exact scope counterexample for later-block L7 residue maximality.

This certificate does NOT refute the local L7 Hensel-class arithmetic.
It refutes only the naive globalization

    later non-maximal L7 block
        => smaller predecessor than the original start N.

The ordinary start N=27 is used as a finite logical witness.  Before its first
fall below 27, the aligned block beginning at binary step 35 starts at x=719.
Its actual 7-bit word is non-maximal in its full-Hensel class.  The canonical
larger-correction sibling starts at x'=718 and merges to the same endpoint,
but 718 is still much larger than the original root 27.

Hence local predecessor credit proves x'<x, not x'<N.  Any use of L7 as a
necessary condition at arbitrary later blocks requires an additional pullback
or headroom theorem.
"""

L = 7
N = 27
START = 35


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trajectory(n: int, steps: int):
    out = [n]
    for _ in range(steps):
        out.append(T(out[-1]))
    return out


def bits_and_endpoint(n: int, L: int):
    bits = []
    x = n
    for _ in range(L):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


def correction(bits):
    R = 0
    q = 0
    for i, b in enumerate(bits):
        if b:
            R = 3 * R + (1 << i)
            q += 1
    return q, R


def class_max(bits):
    q, R = correction(bits)
    modulus = 3 ** q
    residue = R % modulus
    best_R = -1
    best_bits = None
    for mask in range(1 << L):
        u = tuple((mask >> i) & 1 for i in range(L))
        qu, Ru = correction(u)
        if qu == q and Ru % modulus == residue and Ru > best_R:
            best_R = Ru
            best_bits = u
    return q, R, residue, best_R, best_bits


def bitstring(bits):
    return "".join(str(b) for b in bits)


def main():
    root_traj = trajectory(N, 100)
    first_descent = next(i for i, x in enumerate(root_traj[1:], 1) if x < N)
    assert first_descent == 59
    assert START + L < first_descent

    x = root_traj[START]
    assert x == 719
    w, y = bits_and_endpoint(x, L)
    assert bitstring(w) == "1111001"
    assert y == 1367

    q, Rw, residue, Ru, u = class_max(w)
    assert q == 5
    assert Rw == 259
    assert residue == 16
    assert Ru == 502
    assert bitstring(u) == "0111011"
    assert Ru % (3 ** q) == Rw % (3 ** q)

    delta = (Ru - Rw) // (3 ** q)
    assert delta == 1
    xp = x - delta
    assert xp == 718
    assert N < xp < x

    ubits, uy = bits_and_endpoint(xp, L)
    assert ubits == u
    assert uy == y == 1367

    # Exact affine equality.
    lhs = 3 ** q * x + Rw
    rhs = 3 ** q * xp + Ru
    assert lhs == rhs == (1 << L) * y

    # Explicit orbit snippets, all before the first descent of the root orbit.
    assert trajectory(x, L) == [719, 1079, 1619, 2429, 3644, 1822, 911, 1367]
    assert trajectory(xp, L) == [718, 359, 539, 809, 1214, 607, 911, 1367]

    print("root", N)
    print("first_root_descent_step", first_descent)
    print("aligned_block_start", START)
    print("actual_start", x)
    print("actual_word", bitstring(w), "q", q, "R", Rw)
    print("max_sibling_start", xp)
    print("max_sibling_word", bitstring(u), "R", Ru)
    print("hensel_residue_mod_3^q", residue)
    print("credit_delta", delta)
    print("common_endpoint", y)
    print("N < x' < x", N < xp < x)
    print("L7 later-block globalization counterexample: PASS")


if __name__ == "__main__":
    main()
