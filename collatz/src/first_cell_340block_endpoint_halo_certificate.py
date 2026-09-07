#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
Q0 = 72_057_431_991
BLOCK_WIDTH = 1 << 61
FIRST_BLOCK = 1024
LAST_BLOCK = 1363
BLOCK_COUNT = LAST_BLOCK - FIRST_BLOCK + 1
INTERNAL_BOUNDARIES = BLOCK_COUNT - 1
CAP = 1364 * BLOCK_WIDTH


def main():
    assert B0 == FIRST_BLOCK * BLOCK_WIDTH
    assert CAP - B0 == BLOCK_COUNT * BLOCK_WIDTH
    assert BLOCK_COUNT == 340
    assert INTERNAL_BOUNDARIES == 339

    # Candidate-spine same-endpoint displacement is an integer t with
    #   |t| < q/3 <= q0/3.
    # q0 is divisible by 3, hence the maximal possible positive integer
    # displacement is q0/3 - 1.
    assert Q0 % 3 == 0
    halo = Q0 // 3 - 1
    assert halo == 24_019_143_996
    assert halo < (1 << 35)
    assert 2 * halo < BLOCK_WIDTH

    # Around each internal block boundary, only starts within `halo` on either
    # side can belong to one same-endpoint fiber crossing that boundary.
    # Since 2*halo < block width, these 339 two-sided boundary halos are disjoint.
    halo_integer_count = 2 * halo * INTERNAL_BOUNDARIES
    assert halo_integer_count == 16_284_979_629_288

    candidate_integer_count = CAP - B0 - 1  # strict open interval
    assert candidate_integer_count == BLOCK_COUNT * BLOCK_WIDTH - 1

    # Cross-block endpoint coupling therefore occupies less than one part in
    # 48.14 million of the current candidate integer window.
    assert Fraction(halo_integer_count, candidate_integer_count) < Fraction(1, 48_140_000)

    print("PASS")
    print("surviving top-address blocks =", BLOCK_COUNT)
    print("block width = 2^61 =", BLOCK_WIDTH)
    print("max same-endpoint candidate displacement =", halo)
    print("internal block boundaries =", INTERNAL_BOUNDARIES)
    print("total two-sided internal boundary-halo integer count =", halo_integer_count)
    print("cross-block coupling fraction < 1/48,140,000")
    print("endpoint block-coupling graph is nearest-neighbor only")


if __name__ == "__main__":
    main()
