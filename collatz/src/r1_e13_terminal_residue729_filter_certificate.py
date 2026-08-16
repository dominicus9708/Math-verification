#!/usr/bin/env python3
"""Exact low-3-adic terminal residue filter for E=13 pre-G13 pullback.

For one E=13 pre-G13 event-position code P, define

    C(P)=sum_{j=0}^{12} 2^p_j 3^(1526-p_j+j).

Only terms with 3-exponent <=5 can affect C modulo 3^6=729.
An ordinary root N<=NMAX cannot delay its first few even events arbitrarily.
The exact maximal-cover bounds for event ranks j=0..4 are

    p_0<=72, p_1<=186, p_2<=365, p_3<=647, p_4<=1093,

all strictly below the threshold p_j>=1521+j required to affect modulo 729.
Thus ranks 0..4 vanish modulo 729.

If rank j>=5 is active modulo 729, every later rank is also active.  Write

    p_j = 1521+j+b_j.

Strict event ordering and the six terminal time slots imply

    0<=b_j<=5,
    b_j nondecreasing,

and the contribution exponent is exactly 5-b_j.

Enumerating this finite terminal suffix over-family gives exactly 462 possible
correction residues modulo 729.  Their pairwise difference set is all 729
residues, so the terminal-six-step condition alone cannot exclude every G13
credit.

However, once the actual path correction residue c is fixed, an alternate
E=13 path for terminal credit delta must satisfy

    c' == c - 2^1539 delta  (mod 729),
    c' in S_729.

For every possible actual c in S_729 and every delta in 1..397, exactly 248 to
255 credits survive this necessary test.  Therefore fixing the actual pre-gate
attachment removes at least 142 of the 397 bounded G13 credits before any
deeper 3-adic lifting is attempted.

This is an exact finite residue filter and a negative result for a universal
mod-729 obstruction.  It does not prove existence/nonexistence of the full
alternate pullback and does not prove Collatz.
"""

from fractions import Fraction

T = 1539
E = 13
Q = T - E
MOD = 3**6
MAX_CREDIT = 397
NMAX = 5_908_625_413_101_667_397_287
U0 = Fraction(NMAX + 1, 1)


def floor_log2(q: Fraction) -> int:
    n, d = q.numerator, q.denominator
    k = n.bit_length() - d.bit_length()
    while Fraction(1 << k, 1) > q:
        k -= 1
    while Fraction(1 << (k + 1), 1) <= q:
        k += 1
    return k


def odd_run_then_even(U: Fraction, r: int) -> Fraction:
    assert 0 <= r <= floor_log2(U)
    return (Fraction(3, 2) ** r * U + 1) / 2


def greedy_cover_length(U: Fraction, evens: int) -> int:
    """Maximum relaxed steps coverable with exactly `evens` even events."""
    total = 0
    for _ in range(evens):
        r = floor_log2(U)
        total += r + 1
        U = odd_run_then_even(U, r)
    return total + floor_log2(U)


def terminal_residue_set() -> set[int]:
    S = {0}  # no term affects modulo 3^6

    # Earliest possible active correction rank is five.
    for j0 in range(5, 13):
        ranks = list(range(j0, 13))

        def rec(idx: int, last_b: int, acc: int) -> None:
            if idx == len(ranks):
                S.add(acc % MOD)
                return

            j = ranks[idx]
            for b in range(last_b, 6):
                p = 1521 + j + b
                e3 = Q - p + j
                assert e3 == 5 - b
                assert 0 <= e3 <= 5
                term = pow(2, p, MOD) * (3**e3)
                rec(idx + 1, b, (acc + term) % MOD)

        rec(0, 0, 0)

    return S


def main() -> None:
    assert Q == 1526
    assert MOD == 729

    # Latest possible j-th even position before adding the event itself is the
    # maximal length coverable with j earlier evens.
    max_positions = [greedy_cover_length(U0, j) for j in range(5)]
    assert max_positions == [72, 186, 365, 647, 1093]
    for j, pmax in enumerate(max_positions):
        assert pmax < 1521 + j

    S = terminal_residue_set()
    assert len(S) == 462

    # Universal pair differences cover every residue: no stand-alone mod-729
    # obstruction exists without conditioning on the actual correction.
    differences = {(a - b) % MOD for a in S for b in S}
    assert len(differences) == MOD

    shift = pow(2, T, MOD)
    survivor_counts = []
    for c in S:
        count = sum(
            1
            for delta in range(1, MAX_CREDIT + 1)
            if (c - shift * delta) % MOD in S
        )
        survivor_counts.append(count)

    assert min(survivor_counts) == 248
    assert max(survivor_counts) == 255

    print("R1 E=13 terminal residue-729 filter: PASS")
    print("possible C mod 729 residues =", len(S))
    print("pairwise difference residues =", len(differences), "(full 729)")
    print("fixed-actual-residue surviving credits among 1..397:",
          min(survivor_counts), "..", max(survivor_counts))
    print("therefore at least", MAX_CREDIT - max(survivor_counts),
          "credits are removed for every fixed actual residue")
    print("terminal-only universal exclusion: NO (difference set is full)")


if __name__ == "__main__":
    main()
