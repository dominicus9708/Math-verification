#!/usr/bin/env python3
"""Exact two-window phase-coupled low-height Stage-4 certificate.

The one-window five-state theorem bounds every 28-step mechanical phase
separately.  Consecutive phases, however, are not independently selectable:
they are adjacent pieces of one Sturmian/mechanical word.

This certificate therefore enumerates all 57 length-56 mechanical factors,
builds the exact 5x5 low-height transition matrix for each of its two 28-step
halves, and multiplies the two matrices in the actual order.

Taking the entrywise maximum over the 57 valid products gives Pmax.  The
positive integer potential

    v = (1000,2079,3295,4436,5216)^T

satisfies exactly

    27^2 * Pmax * v < 2^56 * v

entrywise.  Hence the recurrent H<=4 dyadic language has paired-window growth
strictly below 2^56/27^2, i.e. per-window exclusion strictly above
log2(27)/28.

Combined with the exact one-window minimum low-to-low masses, incoming H=3
and H=4 are then automatic under the branch-specific K<27 allowance.  The
remaining genuinely cross-base incoming states are H=0,1,2.

This is not a proof of the Collatz conjecture.
"""

from collections import defaultdict

L = 7
W = 28
MAXH = 4
EXPECTED_CLASS_COUNTS = (1, 2, 6, 15, 21, 16, 7, 1)
EXPECTED_MIN_LOW_ROW = (961_664, 3_750_104, 7_424_983, 10_555_305, 12_076_300)
EXPECTED_PMAX = (
    (4_709_421_358_346, 7_744_866_676_304, 7_670_797_286_990, 5_999_871_745_251, 3_931_277_521_274),
    (9_521_862_039_229, 15_725_022_326_620, 15_695_964_387_979, 12_411_279_261_747, 8_577_093_938_463),
    (14_963_913_688_538, 23_124_916_672_335, 23_328_486_390_428, 20_201_136_545_720, 14_862_015_977_263),
    (20_748_223_588_891, 28_263_853_200_163, 31_082_461_023_064, 27_663_177_870_105, 20_858_027_238_992),
    (24_261_344_257_732, 32_371_839_267_296, 35_900_713_158_080, 32_627_673_098_366, 25_216_795_272_193),
)
POTENTIAL = (1000, 2079, 3295, 4436, 5216)


def correction(bits):
    R = 0
    q = 0
    for k, b in enumerate(bits):
        if b:
            R = 3 * R + (1 << k)
            q += 1
    return q, R


def residue_maximal_words():
    groups = defaultdict(list)
    for mask in range(1 << L):
        bits = tuple((mask >> k) & 1 for k in range(L))
        q, R = correction(bits)
        groups[(q, R % (3 ** q))].append((R, bits))

    out = []
    counts = [0] * (L + 1)
    for (q, _), arr in groups.items():
        _, bits = max(arr)
        out.append(bits)
        counts[q] += 1

    assert tuple(counts) == EXPECTED_CLASS_COUNTS
    assert len(out) == 69
    return tuple(out)


def ceil_alpha_count(n):
    """ceil(n log_3 2) by exact integer powers."""
    if n == 0:
        return 0
    p2 = 1 << n
    p3 = 1
    k = 0
    while p3 < p2:
        p3 *= 3
        k += 1
    return k


def mechanical_factor(start, length):
    return tuple(
        ceil_alpha_count(start + i + 1) - ceil_alpha_count(start + i)
        for i in range(length)
    )


def all_factors(length):
    # Sturmian complexity p(n)=n+1.
    seen = {}
    start = 0
    while len(seen) < length + 1:
        factor = mechanical_factor(start, length)
        seen.setdefault(factor, start)
        start += 1
        assert start < 5000
    assert len(seen) == length + 1
    return seen


def low_transition_row(mech28, words, incoming_height):
    dp = {incoming_height: 1}
    for block in range(4):
        segment = mech28[7 * block:7 * (block + 1)]
        nxt = defaultdict(int)
        for h, mass in dp.items():
            for word in words:
                hh = h
                ok = True
                for bit, mech_bit in zip(word, segment):
                    hh += bit - mech_bit
                    if hh < 0:
                        ok = False
                        break
                if ok:
                    nxt[hh] += mass
        dp = nxt
    return tuple(dp.get(h, 0) for h in range(MAXH + 1))


def matrix28(mech28, words):
    return tuple(
        low_transition_row(mech28, words, h)
        for h in range(MAXH + 1)
    )


def matmul(A, B):
    n = len(A)
    return tuple(
        tuple(
            sum(A[i][k] * B[k][j] for k in range(n))
            for j in range(n)
        )
        for i in range(n)
    )


def main():
    words = residue_maximal_words()

    factors28 = all_factors(28)
    matrices28 = {f: matrix28(f, words) for f in factors28}

    min_low_row = tuple(
        min(sum(matrix[i]) for matrix in matrices28.values())
        for i in range(MAXH + 1)
    )
    assert min_low_row == EXPECTED_MIN_LOW_ROW

    factors56 = all_factors(56)
    assert len(factors56) == 57

    pmax = [[0] * (MAXH + 1) for _ in range(MAXH + 1)]
    for factor in factors56:
        A = matrices28[factor[:28]]
        B = matrices28[factor[28:]]
        P = matmul(A, B)
        for i in range(MAXH + 1):
            for j in range(MAXH + 1):
                pmax[i][j] = max(pmax[i][j], P[i][j])

    pmax = tuple(tuple(row) for row in pmax)
    assert pmax == EXPECTED_PMAX

    for i, row in enumerate(pmax):
        pv = sum(row[j] * POTENTIAL[j] for j in range(MAXH + 1))
        lhs = 27 ** 2 * pv
        rhs = (1 << 56) * POTENTIAL[i]
        assert lhs < rhs
        print(
            "row", i,
            "27^2*Pmax*v", lhs,
            "<", rhs,
            "margin", rhs - lhs,
        )

    # H=2 remains unresolved by the trivial selector-probability <=1 bound.
    assert 27 * min_low_row[2] < (1 << 28)

    # H=3 and H=4 are automatic under the paired-window K<27 allowance.
    assert 27 * min_low_row[3] > (1 << 28)
    assert 27 * min_low_row[4] > (1 << 28)

    print("length-56 mechanical factors=57")
    print("phase-coupled low-height growth < 2^56/27^2: PASS")
    print("incoming H=3,4 automatic under K<27: PASS")
    print("remaining incoming heights: H=0,1,2")


if __name__ == "__main__":
    main()
