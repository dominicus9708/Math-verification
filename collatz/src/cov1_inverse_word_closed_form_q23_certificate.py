#!/usr/bin/env python3
"""Closed-form COV-1 inverse-word certificate through q<=23.

For x=36*k+27 and y=T(x)=54*k+41, a reverse word w is built from
  E(z)=2z,
  O(z)=(2z-1)/3 when integral.

If w has length K, q O-letters, and its O positions are
p_0<...<p_(q-1) (0-indexed), then

  m = (2^K*y - C_w)/3^q,
  C_w = sum_{a=0}^{q-1} 3^a * 2^(K-1-p_a).

A final integer value is equivalent to integrality at every O-step: once an
invalid O introduces a denominator 3, later E/O operations cannot cancel it.
Trailing E letters never improve coverage and only worsen contraction, so a
minimal coverage word ends in O and K=p_(q-1)+1.

The leading contraction condition becomes p_(q-1) <= P_q where
P_q=floor((q-1)*log_2(3)).  We compute P_q without floating-point ambiguity
using integer powers.

The cylinder congruence is

  54*k+41 == sum_a 3^a * 2^(-p_a-1)  (mod 3^q).

For q>=3 this either has no solution or one k class modulo 3^(q-3).
Only the first three O positions matter for the mod-27 solvability test.

This script exhausts all canonical contracting words through q=23, removes
3-adic cylinders covered by earlier depths, and verifies the exact counts and
density recorded in the accompanying note.  Finite results are not extrapolated.
"""

from fractions import Fraction
from itertools import combinations


def pmax(q: int) -> int:
    """Largest p with 2^p < 3^(q-1), exactly."""
    p = 0
    target = 3 ** (q - 1)
    while (1 << (p + 1)) < target:
        p += 1
    return p


def valid_first3(p0: int, p1: int, p2: int) -> bool:
    M = 27
    s = (
        pow(2, -p0 - 1, M)
        + 3 * pow(2, -p1 - 1, M)
        + 9 * pow(2, -p2 - 1, M)
        - 41
    ) % M
    return s == 0


def q_residues(q: int):
    assert q >= 3
    P = pmax(q)
    mod = 3**q
    rmod = 3 ** (q - 3)
    inv2 = pow(2, -1, rmod)

    # Normalized terms of C_w*2^(-K): 3^a * 2^(-p_a-1).
    term = [
        [(3**a) * pow(2, -p - 1, mod) % mod for p in range(P + 1)]
        for a in range(q)
    ]

    residues = set()
    sequences = 0

    for p0, p1, p2 in combinations(range(P + 1), 3):
        if not valid_first3(p0, p1, p2):
            continue
        rem = q - 3
        if P - p2 < rem:
            continue
        base = (term[0][p0] + term[1][p1] + term[2][p2]) % mod

        for rest in combinations(range(p2 + 1, P + 1), rem):
            sequences += 1
            pos = (p0, p1, p2) + rest
            S = base
            for a, p in enumerate(rest, start=3):
                S += term[a][p]
            S %= mod

            # First-three solvability guarantees divisibility modulo 27.
            assert (S - 41) % 27 == 0
            k = (((S - 41) // 27) * inv2) % rmod

            # Verify that this cylinder really has a universal smaller merge
            # at its smallest representative k; leading contraction then keeps
            # the inequality for all k+3^r*t, t>=0.
            K = pos[-1] + 1
            C = sum((3**a) * (2 ** (K - 1 - p)) for a, p in enumerate(pos))
            numerator = (2**K) * (54 * k + 41) - C
            assert numerator % mod == 0
            m = numerator // mod
            x = 36 * k + 27
            assert 0 < m < x

            residues.add(k)

    return sequences, residues


def main():
    # Exact P_q values and nesting theorem regression.
    for q in range(3, 24):
        P = pmax(q)
        assert (1 << P) < 3 ** (q - 1)
        assert (1 << (P + 1)) > 3 ** (q - 1)
        if q >= 4:
            jump = P - pmax(q - 1)
            assert jump in (1, 2)

    prefix_free = {}  # depth r -> exact residue set
    rows = []

    for q in range(8, 24):
        sequences, residues = q_residues(q)
        r = q - 3
        new = set()
        for k in residues:
            if any(k % (3**r0) in old for r0, old in prefix_free.items()):
                continue
            new.add(k)
        if new:
            prefix_free[r] = new
        rows.append((q, pmax(q), sequences, len(residues), len(new)))

    expected_new = {
        5: 1,
        7: 5,
        9: 25,
        10: 131,
        12: 580,
        14: 2982,
        16: 16176,
        17: 90550,
        19: 428103,
    }
    assert {r: len(s) for r, s in prefix_free.items()} == expected_new

    total = sum(len(s) for s in prefix_free.values())
    density = sum(Fraction(len(s), 3**r) for r, s in prefix_free.items())
    assert total == 538553
    assert density == Fraction(561769, 43046721)

    # Exact nesting law: if P_q-P_(q-1)=1, no genuinely new cylinders appear.
    row_by_q = {q: row for q, *rest in rows for row in [(q, *rest)]}
    for q, P, sequences, nr, nnew in rows:
        if q > 8 and P - pmax(q - 1) == 1:
            assert nnew == 0

    print("SAFE closed-form finite-symbolic certificate through q=23")
    print("q, P_q, canonical_sequences, residue_cylinders, new_prefix_free")
    for row in rows:
        print(*row)
    print("prefix-free cylinders:", total)
    print("exact k-density:", density)
    print("decimal k-density:", float(density))
    print("GLOBAL 36*k+27 RECURSION: OPEN")


if __name__ == "__main__":
    main()
