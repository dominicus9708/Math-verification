#!/usr/bin/env python3
"""Exact regression for the constructive ternary truncation barrier (MATH-014).

The theorem itself is algebraic and valid for every q>=1 and k>=q+1.
This script regresses the witness family through q=512 using exact integers.
"""


def correction(bits):
    c = 0
    q = 0
    for i, b in enumerate(bits):
        if b:
            c = 3 * c + (1 << i)
            q += 1
    return q, c


def witnesses(q: int, k: int):
    assert 1 <= q < k
    w = [0] * k
    u = [0] * k

    # w = 1,0,1,...,1,0,... and u = 0,1,1,...,1,0,...
    w[0] = 1
    u[1] = 1
    for i in range(2, q + 1):
        w[i] = 1
        u[i] = 1
    return w, u


def main():
    for q in range(1, 513):
        k = q + 1
        w, u = witnesses(q, k)
        qw, cw = correction(w)
        qu, cu = correction(u)
        assert qw == qu == q

        # The two words share q-1 later odd positions.  Only the first
        # contribution changes from 2^0 to 2^1, hence the exact difference.
        assert cw - cu == -(3 ** (q - 1))

        coarse = 3 ** (q - 1)
        full = 3 ** q
        assert cw % coarse == cu % coarse
        assert cw % full != cu % full

    print("PASS")
    print("constructive witness family regressed for q=1..512")
    print("for every q>=1 and k>=q+1, C mod 3^(q-1) aliases two distinct exact Hensel classes")
    print("therefore no fixed truncation C mod 3^m with m<q preserves the exact class key uniformly")
    print("NO COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
