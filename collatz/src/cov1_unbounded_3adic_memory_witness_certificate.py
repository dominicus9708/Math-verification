#!/usr/bin/env python3
"""Regression certificate for the unbounded 3-adic memory witness family.

Define coefficient-surviving parity prefixes

  A_t = 11111001 1^t
  B_t = 11011011 1^t.

Both have h=t+8, s=t+6, v=s+2=h.  Let C be the standard forward parity
affine constant and R=2^(-h) C mod 3^h, which is the inverse-turn target.

For every t>=0:
  * v_3(R_B-R_A)=t+4;
  * A_t passes the minimal q=v reverse-congruence gate;
  * B_t fails it.

Thus for every fixed Q>=1 there are two coefficient-surviving states with the
same Beatty slack and same R mod 3^Q but different reverse compatibility.
No fixed finite number of low ternary target digits can decide this gate.

The general noncompatibility proof for B_t is in the accompanying note.  This
script exhaustively checks the base case B_0 and regressions through t<=80.
"""

from itertools import combinations

BASE_A = tuple(map(int, "11111001"))
BASE_B = tuple(map(int, "11011011"))


def beatty_b(j: int) -> int:
    q = 0
    while 3 ** q < 2 ** j:
        q += 1
    return q


def parity_state(bits):
    C = 0
    s = 0
    for j, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << j)
            s += 1
    h = len(bits)
    v = s + 2
    R = (C * pow(2, -h, 3 ** v)) % (3 ** v)
    return h, s, v, C, R


def coefficient_survives(bits) -> bool:
    s = 0
    for j, bit in enumerate(bits, start=1):
        s += bit
        if s < beatty_b(j):
            return False
    return True


def reverse_sum(positions, v: int) -> int:
    mod = 3 ** v
    return sum((3 ** a) * pow(2, -p - 1, mod) for a, p in enumerate(positions)) % mod


def minimal_compatible(bits) -> bool:
    h, s, v, C, R = parity_state(bits)
    # q=v=s+2, and the contraction budget is P=h+2 because floor(2 log_2 3)=3.
    P = h + 2
    for pos in combinations(range(P + 1), v):
        if reverse_sum(pos, v) == R:
            return True
    return False


def valuation3_mod_difference(a: int, b: int, modulus: int) -> int:
    d = (a - b) % modulus
    assert d != 0
    v = 0
    while d % 3 == 0:
        d //= 3
        v += 1
    return v


def main():
    assert coefficient_survives(BASE_A)
    assert coefficient_survives(BASE_B)

    hA, sA, vA, CA, RA = parity_state(BASE_A)
    hB, sB, vB, CB, RB = parity_state(BASE_B)
    assert (hA, sA, vA, CA, RA) == (8, 6, 8, 761, 4283)
    assert (hB, sB, vB, CB, RB) == (8, 6, 8, 1085, 5822)
    assert CB - CA == 4 * 3 ** 4

    # Explicit A_0 witness: positions 0..10 except 2,7,10.
    posA0 = (0, 1, 3, 4, 5, 6, 8, 9)
    assert reverse_sum(posA0, 8) == RA

    # Exact finite base obstruction for B_0: all C(11,8)=165 candidates fail.
    candidates = list(combinations(range(11), 8))
    assert len(candidates) == 165
    assert all(reverse_sum(pos, 8) != RB for pos in candidates)

    for t in range(81):
        bitsA = BASE_A + (1,) * t
        bitsB = BASE_B + (1,) * t
        assert coefficient_survives(bitsA)
        assert coefficient_survives(bitsB)

        h1, s1, v1, C1, R1 = parity_state(bitsA)
        h2, s2, v2, C2, R2 = parity_state(bitsB)
        assert (h1, s1, v1) == (t + 8, t + 6, t + 8)
        assert (h2, s2, v2) == (t + 8, t + 6, t + 8)
        assert C2 - C1 == 4 * 3 ** (t + 4)
        assert valuation3_mod_difference(R2, R1, 3 ** v1) == t + 4
        assert R2 % 9 == 8

        # General A_t witness: prepend t O's to A_0, equivalently shift A_0
        # positions by t and fill positions 0..t-1 with O.
        posA = tuple(range(t)) + tuple(p + t for p in posA0)
        assert len(posA) == v1
        assert posA[-1] <= h1 + 2
        assert reverse_sum(posA, v1) == R1

        # Full B_t enumeration remains polynomial here because v=h and only
        # three of h+3 available positions are omitted.  This is regression,
        # not the proof of the all-t statement.
        assert not minimal_compatible(bitsB)

    print("SAFE unbounded-memory regression through t=80")
    print("A_t and B_t share target digits through depth t+4 but differ in minimal reverse compatibility.")
    print("Base B_0 candidates checked: 165")
    print("General all-t proof is recorded in the companion note.")


if __name__ == "__main__":
    main()
