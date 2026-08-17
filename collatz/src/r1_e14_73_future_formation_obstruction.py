#!/usr/bin/env python3
"""Exact current-R1 E=14 obstruction from first-73 and future-run formation.

Previously certified inputs:

* all first-73 layers with <=8 even events are closed in the current core;
* the exact run-cover theorem gives E=14 -> e_73<=10;
* the necessary even-event lower vector for total E=14 is

    [0,1,2,3,4,5,6,7,8,69,166,319,559,939].

Therefore an unresolved E=14 start can only have e_73=9 or e_73=10.

Case A: e_73=10
-----------------
The next even is rank 10 and p_10>=166, so steps73..165 are 93 consecutive
odd steps.  Write U_73=2^93 v.  The current numerical interval and the trivial
formation bound epsilon_10<=2^10-1 give

    49<=v<=72.

With q=63 first-73 odd steps and

    e_j=63-p_j+j,

the normalized correction must satisfy

    sum_{j=0}^9 2^(j-e_j)3^e_j == 2^103 v (mod 3^63).

The same finite digit automaton used in the E=13 closure rejects every v
already modulo 3^16.

Case B: e_73=9
----------------
The first post-73 even is rank9.  Put r=p_9-73.
The following even obeys p_10>=166.

If 0<=r<=92, the first post-73 odd run has length r, then one even occurs, and
the next odd run has length at least 92-r.  In U=x+1 coordinates this implies

    3^r U_73 + 2^r == 0 (mod 2^93),

hence

    U_73 == -2^r 3^(-r) (mod 2^93).

If r>=93, simply 2^93|U_73.  Thus every possible U_73 lies in one of exactly
94 residues modulo 2^93.

The numerical interval and epsilon_9<=511 produce a finite U_73 interval.
Exactly 6797 integers in that interval lie in those 94 residues.  For each,
the first-73 normalized correction must satisfy

    sum_{j=0}^8 2^(j-e_j)3^e_j == 2^9 U_73 (mod 3^64).

The digit automaton rejects all 6797 targets by K=24.

Hence both possible first-73 E=14 layers are empty, so e_1539>=15 for the
current isolated R1 core.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

T = 1539
N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287
U0MAX = Fraction(NMAX + 1, 1)


def pow2_fraction(k: int) -> Fraction:
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))


def floor_log2(q: Fraction) -> int:
    k = q.numerator.bit_length() - q.denominator.bit_length()
    while pow2_fraction(k) > q:
        k -= 1
    while pow2_fraction(k + 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    return (Fraction(3, 2) ** r * U + 1) / 2


@lru_cache(maxsize=None)
def greedy_max_final(steps: int, evens: int):
    U = U0MAX
    rem_steps = steps
    rem_e = evens
    for _ in range(evens):
        if rem_steps < rem_e:
            return None
        r = min(floor_log2(U), rem_steps - rem_e)
        U = odd_run_then_even(U, r)
        rem_steps -= r + 1
        rem_e -= 1
    if rem_steps < 0 or rem_steps > floor_log2(U):
        return None
    return Fraction(3, 2) ** rem_steps * U


def can_cover(U: Fraction, evens: int, needed: int) -> bool:
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        if total + r + 1 >= needed:
            return True
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U) >= needed


def earliest_vector(E: int) -> list[int]:
    out = []
    for j in range(E):
        remaining = E-j-1
        for p in range(j, T):
            Umax = greedy_max_final(p+1, j+1)
            if Umax is not None and can_cover(Umax, remaining, T-p-1):
                out.append(p)
                break
    return out


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator)//q.denominator)


def floor_fraction(q: Fraction) -> int:
    return q.numerator//q.denominator


def formation_survives(target: int, ranks: int, K: int) -> bool:
    # Necessary congruence for sum 2^(j-e_j)3^e_j == target mod 3^K.
    # Unassigned ranks after K levels are allowed to have e_j>=K.
    states = {(ranks, -target)}
    for _ in range(K):
        nxt = set()
        for a, carry in states:
            for a2 in range(a+1):
                z = carry + (1 << a) - (1 << a2)
                if z % 3 == 0:
                    nxt.add((a2, 2*(z//3)))
        states = nxt
        if not states:
            return False
    return True


def case_e73_10() -> None:
    q = 63
    forced_odds = 93
    scale = Fraction(3**q, 1 << (73+forced_odds))
    vlo = ceil_fraction(scale*(N0+1))
    vhi = floor_fraction(scale*(NMAX+1+(2**10-1)))
    assert (vlo, vhi) == (49,72)

    survivors = {}
    for K in (12,14,15,16):
        vals = [v for v in range(vlo,vhi+1)
                if formation_survives((1 << 103)*v, 10, K)]
        survivors[K] = vals
    assert survivors[15] == [49,69]
    assert survivors[16] == []


def case_e73_9() -> None:
    q = 64
    scale = Fraction(3**q, 1 << 73)
    Ulo = ceil_fraction(scale*(N0+1))
    Uhi = floor_fraction(scale*(NMAX+1+511))
    assert Ulo == 1_432_083_263_272_809_064_038_692_729_007
    assert Uhi == 2_148_112_768_749_759_867_080_327_368_528

    modulus2 = 1 << 93
    residues = {0}
    for r in range(93):
        residues.add((-(1 << r)*pow(pow(3,r,modulus2), -1, modulus2)) % modulus2)
    assert len(residues) == 94

    allowed = []
    for residue in residues:
        k = ceil_fraction(Fraction(Ulo-residue, modulus2))
        u = residue + k*modulus2
        while u <= Uhi:
            allowed.append(u)
            u += modulus2
    allowed = sorted(set(allowed))
    assert len(allowed) == 6797

    expected_counts = {6:4497,9:3410,12:1348,15:290,18:48,21:7,24:0}
    for K, expected in expected_counts.items():
        count = sum(formation_survives((1 << 9)*u, 9, K) for u in allowed)
        assert count == expected, (K,count,expected)


def main() -> None:
    lower = earliest_vector(14)
    assert lower == [0,1,2,3,4,5,6,7,8,69,166,319,559,939]

    # Existing first-73 <=8 closure leaves only 9 or 10 even events because
    # the run-cover theorem gives max e_73=10 at total E=14.
    case_e73_10()
    case_e73_9()

    print("R1 E=14 first73/future formation obstruction: PASS")
    print("E14 possible e_73 layers 9 and 10 are both empty")
    print("therefore e_1539 >= 15")


if __name__ == "__main__":
    main()
