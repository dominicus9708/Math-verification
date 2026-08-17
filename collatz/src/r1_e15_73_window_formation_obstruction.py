#!/usr/bin/env python3
"""Exact current-R1 E=15 obstruction by a sparse post-73 parity window.

Certified inputs:

* all first-73 layers with <=8 evens are already closed;
* run-cover gives E=15 -> e_73<=11;
* the E=15 necessary event-position vector is

    [0,1,2,3,4,5,6,7,8,9,71,168,321,561,940].

Hence only k=e_73 in {9,10,11} can remain.  Rank 11 cannot occur before
position168, so the 95 accelerated steps at positions73..167 contain at most

    11-k

even events.  A length-95 parity word with at most m evens determines one
exact U_73 residue modulo 2^95.  The residue counts are therefore

    k=9  : sum_{i=0}^2 C(95,i) = 4561,
    k=10 : sum_{i=0}^1 C(95,i) = 96,
    k=11 : 1.

Intersect these dyadic classes with the exact numerical U_73 interval implied
by the current N range and epsilon_k<=2^k-1.  For each remaining U_73, the
first-73 k-event correction must satisfy

    sum_{j=0}^{k-1} 2^(j-e_j)3^e_j == 2^k U_73  (mod 3^(73-k)).

The same finite ternary formation automaton used for E=13/E=14 eliminates all
three layers.  Exact checkpoints:

k=9: 82436 numeric U states -> 8 at K=24 -> 0 at K=27.
k=10: 578 numeric U states -> 1 at K=21 -> 0 at K=24.
k=11: 2 numeric U states -> 1 through K=12 -> 0 at K=15.

Thus E=15 is empty in the current isolated R1 core and e_1539>=16.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator)//q.denominator)


def floor_fraction(q: Fraction) -> int:
    return q.numerator//q.denominator


def canonical_U_residues(length: int, max_evens: int) -> set[int]:
    """All U=x+1 residues modulo 2^length for parity words with <=max_evens zeros."""
    modulus = 1 << length
    out = set()

    for z in range(max_evens+1):
        q = length-z
        inv = pow(pow(3,q,modulus), -1, modulus)
        for zeros_tuple in combinations(range(length), z):
            zeros = set(zeros_tuple)
            correction = 0
            for t in range(length):
                if t not in zeros:
                    correction = (3*correction + (1 << t)) % modulus
            x = (-inv*correction) % modulus
            out.add((x+1) % modulus)

    return out


def U73_interval(k: int) -> tuple[int,int]:
    q = 73-k
    scale = Fraction(3**q, 1 << 73)
    lo = ceil_fraction(scale*(N0+1))
    hi = floor_fraction(scale*(NMAX+1+(2**k-1)))
    return lo,hi


def numeric_U_states(k: int, window: int, max_window_evens: int) -> list[int]:
    lo,hi = U73_interval(k)
    modulus = 1 << window
    residues = canonical_U_residues(window, max_window_evens)
    out = []
    for residue in residues:
        m = ceil_fraction(Fraction(lo-residue, modulus))
        u = residue + m*modulus
        while u <= hi:
            out.append(u)
            u += modulus
    return sorted(set(out))


def formation_survives(target: int, ranks: int, K: int) -> bool:
    states = {(ranks, -target)}
    for _ in range(K):
        nxt = set()
        for a,carry in states:
            for a2 in range(a+1):
                z = carry + (1 << a) - (1 << a2)
                if z % 3 == 0:
                    nxt.add((a2, 2*(z//3)))
        states = nxt
        if not states:
            return False
    return True


def main() -> None:
    # Rank11 lower bound168 gives a 95-step post-73 window.
    window = 95

    specs = {
        9:  (2, 4561, 82436, {18:563,21:66,24:8,27:0}),
        10: (1,   96,   578, {18:10,21:1,24:0}),
        11: (0,    1,     2, {6:1,9:1,12:1,15:0}),
    }

    for k,(max_window_evens, expected_residues, expected_numeric, checkpoints) in specs.items():
        residues = canonical_U_residues(window, max_window_evens)
        assert len(residues) == expected_residues

        states = numeric_U_states(k, window, max_window_evens)
        assert len(states) == expected_numeric

        for K,expected in checkpoints.items():
            count = sum(formation_survives((1 << k)*u, k, K) for u in states)
            assert count == expected, (k,K,count,expected)

    print("R1 E=15 first73 sparse-window formation obstruction: PASS")
    print("all k=e_73 in {9,10,11} are empty")
    print("therefore e_1539 >= 16")


if __name__ == "__main__":
    main()
