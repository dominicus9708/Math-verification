#!/usr/bin/env python3
"""Exact combinatorial certificate for the fixed-additive-slack reverse bound.

Let Q_*(d) be the least Q with (3/2)^Q > 3^d. At resolution
Q = Q_*(d)+c, any reverse code with potential Lambda>3^d must have
q = Q-h with 0<=h<=c and total exponent K=q+e satisfying
    2^e < (3/2)^(c-h+1).
For fixed q,e there are C(q+e-1,e) positive exponent sequences, and each
sequence determines at most one endpoint residue mod 3^q, hence at most 3^h
lifts mod 3^Q.

The resulting union bound is
    G(d,c) <= sum_{h=0}^c 3^h sum_{e=0}^{E(c,h)} C(Q-h+e-1,e),
where E(c,h) is the largest integer e satisfying the displayed inequality.
This is a scope certificate, not a Collatz proof.
"""

from math import comb


def qstar(d: int) -> int:
    Q = 1
    while 3**Q <= 3**d * 2**Q:
        Q += 1
    return Q


def e_cap(c: int, h: int) -> int:
    r = c - h + 1
    e = 0
    best = -1
    while (2**e) * (2**r) < 3**r:
        best = e
        e += 1
    return best


def union_bound(d: int, c: int):
    Q0 = qstar(d)
    Q = Q0 + c
    total = 0
    terms = []
    for h in range(c + 1):
        q = Q - h
        E = e_cap(c, h)
        subtotal = sum(comb(q + e - 1, e) for e in range(E + 1))
        lifted = (3**h) * subtotal
        total += lifted
        terms.append((h, q, E, subtotal, lifted))
    admissible = 2 * 3 ** (Q - 1)
    return Q0, Q, total, admissible, terms


def main():
    assert [qstar(d) for d in range(1, 6)] == [3, 6, 9, 11, 14]

    for d in range(1, 51):
        Q0, Q, total, admissible, terms = union_bound(d, 0)
        assert Q == Q0
        assert total == 1
        assert terms == [(0, Q, 0, 1, 1)]
        assert admissible == 2 * 3 ** (Q - 1)

    expected = {
        (1,0):(3,1,18), (1,1):(4,8,54), (1,2):(5,30,162),
        (2,0):(6,1,486), (2,1):(7,11,1458), (2,2):(8,42,4374),
        (3,0):(9,1,13122), (3,1):(10,14,39366), (3,2):(11,54,118098),
        (5,0):(14,1,3188646), (5,1):(15,19,9565938), (5,2):(16,74,28697814),
        (10,0):(28,1,15251194969974),
    }
    for (d,c),(Qexp,Gexp,Aexp) in expected.items():
        _Q0,Q,G,A,_terms = union_bound(d,c)
        assert (Q,G,A) == (Qexp,Gexp,Aexp)

    print("d c Qstar Q bound favorable_fraction_upper")
    for d in (1,2,3,5,10,20):
        for c in range(5):
            Q0,Q,G,A,_terms = union_bound(d,c)
            print(d, c, Q0, Q, G, f"{G}/{A}", f"{G/A:.15e}")

    print("PASS")


if __name__ == "__main__":
    main()
