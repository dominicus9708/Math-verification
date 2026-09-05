#!/usr/bin/env python3
"""Regression certificate for the normalized relative-discrete-log Hensel branches.

For r>=2 and t odd with 3 not dividing t, define

    Phi_r(t) = ind_2((1+2^t)/3 mod 3^(r-1))

in Z/(2*3^(r-2)).  Splitting t into the two live residue classes

    t = 1 + 6k,   t = 5 + 6k,

and normalizing the forced parity of Phi gives maps Psi_1,Psi_5 on
Z/3^(r-2).  The accompanying note proves for all r that these maps are
3-adic isometries and that their first differing ternary digit has fixed
slope -1 and +1 respectively.

This file exhaustively checks the theorem through r=8.  It is a regression
certificate, not the proof and not a proof of the Collatz conjecture.
"""


def dlog_table(n: int):
    mod = 3**n
    order = 2 * 3 ** (n - 1)
    tab = {}
    x = 1
    for h in range(order):
        tab[x] = h
        x = (2 * x) % mod
    assert len(tab) == order
    return tab


def phi(t: int, r: int, tab) -> int:
    # Work one ternary digit deeper so the exact division by 3 is visible.
    M = 3**r
    z = (1 + pow(2, t, M)) % M
    assert z % 3 == 0
    q = (z // 3) % (3 ** (r - 1))
    assert q % 3 != 0
    return tab[q]


def main() -> None:
    for r in range(2, 9):
        N = 3 ** (r - 2)
        tab = dlog_table(r - 1)

        for a in (1, 5):
            values = []
            for k in range(N):
                t = a + 6 * k
                ph = phi(t, r, tab)
                expected_parity = 0 if a == 1 else 1
                assert ph % 2 == expected_parity
                ps = ph // 2 if a == 1 else (ph - 1) // 2
                values.append(ps % N)

            # Each live branch is a permutation of the depth-(r-2) ternary tree.
            assert sorted(values) == list(range(N))

            # Fixed child slope at every checked ternary level.
            # If the first differing input digit is u in {1,2}, the first
            # differing output digit is -u for a=1 and +u for a=5.
            for s in range(r - 2):
                step = 3**s
                for k in range(N):
                    for u in (1, 2):
                        k2 = k + u * step
                        if k2 >= N:
                            continue
                        outdiff = (values[k2] - values[k]) % N
                        assert outdiff % step == 0
                        lead = (outdiff // step) % 3
                        expected = (-u) % 3 if a == 1 else u
                        assert lead == expected

    print("PASS relative-discrete-log Hensel tree isometry regression")
    print("t=1 mod 6 branch: ternary child slope -1")
    print("t=5 mod 6 branch: ternary child slope +1")
    print("checked exhaustively through r=8")


if __name__ == "__main__":
    main()
