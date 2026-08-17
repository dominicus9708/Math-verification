#!/usr/bin/env python3
"""Exact E=13 obstruction from the 73-step formation class plus 91 forced odds.

Dependencies already certified in the current R1 program:

1. every unresolved E=13 current-core start has at most nine even events in
   the first 73 accelerated steps;
2. every first-73 layer with at most eight evens is already closed;
3. the exact run-cover theorem gives p_9 >= 164 for the tenth even event of
   any E=13 path below the current numerical ceiling.

Hence an unresolved E=13 candidate would have exactly nine evens in steps
0..72 and no even event in steps 73..163.  In U=x+1 coordinates, 91
consecutive odd steps require

    2^91 | U_73.

Write U_73=2^91 v.  With q=64 odd steps among the first 73 and even-event
positions p_0<...<p_8, the exact formation identity is

    2^73 U_73
      = 3^64 U_0
        + sum_{j=0}^8 2^p_j 3^(64-p_j+j).

Because p_j>=j,

    epsilon_9
      = sum 3^j (2/3)^p_j
      <= sum 2^j = 511.

The current numerical interval therefore confines v to exactly

    579 <= v <= 867.

Put

    e_j = 64-p_j+j.

Since the first 73 bits contain exactly nine evens,

    e_0 >= e_1 >= ... >= e_8 >= 0.

Reducing the formation equation modulo 3^64 and dividing by the 3-adic unit
2^64 gives

    sum_{j=0}^8 2^(j-e_j) 3^e_j
      == 2^100 v  (mod 3^64).

A digit-by-digit formation automaton checks this necessary relation.  At
ternary level t, state (a,c) means ranks 0,...,a-1 remain unassigned and c is
the scaled residual carry.  Assigning the suffix ranks a',...,a-1 to exponent
t contributes

    2^a - 2^a'.

The next state exists iff

    c + 2^a - 2^a' == 0 (mod 3),

and then

    c' = (2/3)(c + 2^a - 2^a').

Ranks not assigned within the tested K digits simply have e_j>=K, so the
finite-K automaton is an over-family of every physical first-73 event pattern.

Exact result:

    K=18: only v=591 survives;
    K=19: only v=591 survives;
    K=20: only v=591 survives;
    K=21: no v in 579..867 survives.

Thus the contradiction already occurs modulo 3^21, long before any complete
73-bit parity word or ordinary start is enumerated.

Consequently the current E=13 R1 layer is empty, and the entrance theorem may
be upgraded to e_1539>=14.

This is current-R1/current-numerical-interval specific through its dependency
on the previously certified first-73 <=8 closure and run-cover bounds.  It is
not a proof of the global Collatz conjecture.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache

T = 1539
E = 13
N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287


def pow2_fraction(k: int) -> Fraction:
    if k >= 0:
        return Fraction(1 << k, 1)
    return Fraction(1, 1 << (-k))


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
    """Exact relaxed maximal endpoint under the odd-run divisibility cap."""
    U = Fraction(NMAX + 1, 1)
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


def earliest_even_position(j: int) -> int:
    """Relaxed necessary lower bound for the zero-based j-th even position."""
    remaining_e = E - j - 1
    for p in range(j, T):
        Umax = greedy_max_final(p + 1, j + 1)
        if Umax is None:
            continue
        if can_cover(Umax, remaining_e, T - p - 1):
            return p
    raise AssertionError("no feasible event position")


def ceil_fraction(q: Fraction) -> int:
    return -((-q.numerator) // q.denominator)


def floor_fraction(q: Fraction) -> int:
    return q.numerator // q.denominator


def possible_v_interval() -> tuple[int, int]:
    # 2^164 v = 3^64 (U_0 + epsilon_9), 0<epsilon_9<=511.
    scale = Fraction(3**64, 1 << 164)
    lo = ceil_fraction(scale * (N0 + 1))
    hi = floor_fraction(scale * (NMAX + 1 + 511))
    return lo, hi


def formation_survives(v: int, K: int) -> bool:
    """Necessary normalized first-73 formation congruence modulo 3^K.

    Remaining ranks after K levels are deliberately allowed to have e_j>=K,
    so this is an over-family and any rejection is safe.
    """
    states = {(9, -(1 << 100) * v)}

    for _t in range(K):
        nxt = set()
        for a, carry in states:
            # Assign suffix ranks a2,...,a-1 to the current exponent.
            for a2 in range(a + 1):
                block = (1 << a) - (1 << a2)
                z = carry + block
                if z % 3 == 0:
                    nxt.add((a2, 2 * (z // 3)))
        states = nxt
        if not states:
            return False

    return True


def death_depth(v: int, Kmax: int = 21) -> int:
    states = {(9, -(1 << 100) * v)}
    for t in range(Kmax):
        nxt = set()
        for a, carry in states:
            for a2 in range(a + 1):
                block = (1 << a) - (1 << a2)
                z = carry + block
                if z % 3 == 0:
                    nxt.add((a2, 2 * (z // 3)))
        states = nxt
        if not states:
            return t + 1
    return 0


def explicit_residue_set(K: int) -> set[int]:
    """Independent small-K enumeration audit of the automaton.

    e=K represents every invisible exponent >=K.  Nonincreasing exponent
    vectors are enumerated directly and their normalized formation sums are
    evaluated modulo 3^K.
    """
    modulus = 3**K
    inv2 = pow(2, -1, modulus)
    inv2pow = [1]
    for _ in range(K):
        inv2pow.append((inv2pow[-1] * inv2) % modulus)

    out: set[int] = set()
    exps = [0] * 9

    def rec(j: int, ceiling: int) -> None:
        if j == 9:
            s = 0
            for rank, e in enumerate(exps):
                if e >= K:
                    continue
                s += (pow(2, rank, modulus) * inv2pow[e] * pow(3, e, modulus)) % modulus
            out.add(s % modulus)
            return

        # e_j is nonincreasing, so the next exponent is <= the previous one.
        for e in range(ceiling, -1, -1):
            exps[j] = e
            rec(j + 1, e)

    # e=K is the one symbolic invisible value.
    rec(0, K)
    return out


def main() -> None:
    # Recompute the exact future-cover position theorem locally.  The tenth
    # even event is zero-based rank 9.
    lower = [earliest_even_position(j) for j in range(E)]
    assert lower == [0, 1, 2, 3, 4, 5, 6, 7, 66, 164, 317, 558, 938]
    assert lower[9] == 164

    vlo, vhi = possible_v_interval()
    assert (vlo, vhi) == (579, 867)

    # Independent recurrence audit at a small modulus.
    K_AUDIT = 6
    residues = explicit_residue_set(K_AUDIT)
    modulus = 3**K_AUDIT
    for v in range(vlo, vhi + 1):
        target = ((1 << 100) * v) % modulus
        assert formation_survives(v, K_AUDIT) == (target in residues)

    survivors = {}
    for K in (18, 19, 20, 21):
        vals = [v for v in range(vlo, vhi + 1) if formation_survives(v, K)]
        survivors[K] = vals

    assert survivors[18] == [591]
    assert survivors[19] == [591]
    assert survivors[20] == [591]
    assert survivors[21] == []

    hist = Counter(death_depth(v, 21) for v in range(vlo, vhi + 1))
    assert hist[21] == 1
    assert sum(hist.values()) == 289
    assert all(k > 0 for k in hist)

    print("R1 E=13 73+91 formation obstruction: PASS")
    print("tenth-even lower bound p_9 =", lower[9])
    print("forced odd steps after depth73 = 91")
    print("possible v interval =", (vlo, vhi), "count=", vhi - vlo + 1)
    for K in (18, 19, 20, 21):
        print("K=", K, "surviving v=", survivors[K])
    print("death-depth histogram =", dict(sorted(hist.items())))
    print("E=13 current R1 layer: EMPTY")
    print("therefore e_1539 >= 14")


if __name__ == "__main__":
    main()
