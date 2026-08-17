#!/usr/bin/env python3
"""Exact current-R1 E=16 obstruction by a sparse post-73 parity window.

Certified inputs:

* all first-73 layers with <=8 evens are closed;
* run-cover gives E=16 -> e_73<=11;
* the exact E=16 necessary even-position vector is

    [0,1,2,3,4,5,6,7,8,9,12,74,171,323,563,941].

Thus only k=e_73 in {9,10,11} remain. Rank 12 cannot occur before position
171, so the 98 accelerated positions 73..170 contain at most 12-k evens.
Therefore the possible U_73 residues modulo 2^98 are compressed to

    k=9  : sum_{i=0}^3 C(98,i) = 156948,
    k=10 : sum_{i=0}^2 C(98,i) = 4852,
    k=11 : sum_{i=0}^1 C(98,i) = 99.

Intersecting these residue classes with the exact numerical U_73 interval
leaves respectively

    354821, 3701, 33

endpoint states. For each state the first-73 k-event correction must satisfy

    sum_{j<k} 2^(j-e_j)3^e_j == 2^k U_73 (mod 3^(73-k)).

The same finite ternary formation automaton used in the E=13--15 closures
eliminates all three layers. Exact checkpoints:

    k=9  : K15 15832 -> K18 2441 -> K21 319 -> K24 40 -> K27 5 -> K30 0;
    k=10 : K21 14 -> K24 1 -> K27 0;
    k=11 : K15 2 -> K18 0.

Hence E=16 is empty in the current isolated R1 core and e_1539>=17.
This is a class-level finite formation certificate, not a global Collatz proof.
"""

from fractions import Fraction
from itertools import combinations

N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287
WINDOW = 98


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator) // q.denominator)


def floor_fraction(q: Fraction) -> int:
    return q.numerator // q.denominator


def canonical_U_residues(length: int, max_evens: int) -> set[int]:
    modulus = 1 << length
    out = set()
    for z in range(max_evens + 1):
        q = length - z
        inv = pow(pow(3, q, modulus), -1, modulus)
        for zeros_tuple in combinations(range(length), z):
            zeros = set(zeros_tuple)
            correction = 0
            for t in range(length):
                if t not in zeros:
                    correction = (3 * correction + (1 << t)) % modulus
            x = (-inv * correction) % modulus
            out.add((x + 1) % modulus)
    return out


def U73_interval(k: int) -> tuple[int, int]:
    q = 73 - k
    scale = Fraction(3**q, 1 << 73)
    lo = ceil_fraction(scale * (N0 + 1))
    hi = floor_fraction(scale * (NMAX + 1 + (2**k - 1)))
    return lo, hi


def numeric_U_states(k: int, max_window_evens: int) -> list[int]:
    lo, hi = U73_interval(k)
    modulus = 1 << WINDOW
    residues = canonical_U_residues(WINDOW, max_window_evens)
    out = []
    for residue in residues:
        m = ceil_fraction(Fraction(lo - residue, modulus))
        u = residue + m * modulus
        while u <= hi:
            out.append(u)
            u += modulus
    return sorted(set(out))


def formation_survives(target: int, ranks: int, K: int) -> bool:
    states = {(ranks, -target)}
    for _ in range(K):
        nxt = set()
        for a, carry in states:
            for a2 in range(a + 1):
                z = carry + (1 << a) - (1 << a2)
                if z % 3 == 0:
                    nxt.add((a2, 2 * (z // 3)))
        states = nxt
        if not states:
            return False
    return True


def main() -> None:
    specs = {
        9: (3, 156_948, 354_821,
            {15:15_832, 18:2_441, 21:319, 24:40, 27:5, 30:0}),
        10:(2, 4_852, 3_701,
            {21:14, 24:1, 27:0}),
        11:(1, 99, 33,
            {15:2, 18:0}),
    }

    for k, (max_evens, expected_residues, expected_numeric, checkpoints) in specs.items():
        residues = canonical_U_residues(WINDOW, max_evens)
        assert len(residues) == expected_residues
        states = numeric_U_states(k, max_evens)
        assert len(states) == expected_numeric
        for K, expected in checkpoints.items():
            count = sum(formation_survives((1 << k) * u, k, K) for u in states)
            assert count == expected, (k, K, count, expected)

    print("R1 E=16 first73 sparse-window formation obstruction: PASS")
    print("all k=e_73 in {9,10,11} are empty")
    print("therefore e_1539 >= 17")


if __name__ == "__main__":
    main()
