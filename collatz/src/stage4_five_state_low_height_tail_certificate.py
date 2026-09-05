#!/usr/bin/env python3
"""Exact five-state low-height L7 renewal-tail certificate.

After the companion high-height theorem closes every incoming H>=5, this
certificate restricts the recurrent tail to H=0,...,4.

For each of the 29 length-28 mechanical factors it counts four-block L7
residue-maximal words that:
  * never drive the relative height below zero; and
  * end again in H'=0,...,4.

Taking the entrywise maximum over all phases gives Mmax. A positive integer
potential v proves exactly

    25 * Mmax * v < 2^28 * v

entrywise, so the low-height dyadic recurrent language has weighted 28-step
growth strictly below 2^28/25.

Consequently a selector/dyadic low-height conditional amplification <25 per
window suffices for extinction of the recurrent low-height branch.

Moreover H=4 is automatic even without selector regularity, because every
phase has more than 2^28/25 low-to-low admissible words. H=3 misses the same
trivial threshold by only ~1.7% selector mass.

This is not a Collatz proof. H=0,...,3 still require cross-base control.
"""

from collections import defaultdict

L = 7
W = 28
MAXH = 4
EXPECTED_CLASS_COUNTS = (1, 2, 6, 15, 21, 16, 7, 1)
EXPECTED_MMAX = (
    (707250, 1085037, 1074609, 753120, 408810),
    (1466790, 2004684, 2090340, 1590685, 966818),
    (2079878, 2667698, 2878633, 2447289, 1711766),
    (2248621, 3088826, 3232283, 3106984, 2515663),
    (2021037, 2995290, 3332320, 3352635, 3137392),
)
EXPECTED_MIN_LOW_ROW = (961664, 3750104, 7424983, 10555305, 12076300)
POTENTIAL = (1000, 2044, 3038, 3774, 4088)


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
    if n == 0:
        return 0
    p2 = 1 << n
    p3 = 1
    k = 0
    while p3 < p2:
        p3 *= 3
        k += 1
    return k


def mechanical_factor(start, length=W):
    return tuple(
        ceil_alpha_count(start + i + 1) - ceil_alpha_count(start + i)
        for i in range(length)
    )


def all_length28_factors():
    seen = {}
    s = 0
    while len(seen) < W + 1:
        f = mechanical_factor(s)
        seen.setdefault(f, s)
        s += 1
        assert s < 1000
    assert len(seen) == 29
    return tuple(seen)


def low_transition_row(mech, words, incoming_height):
    dp = {incoming_height: 1}
    for block in range(4):
        seg = mech[7 * block: 7 * (block + 1)]
        nxt = defaultdict(int)
        for h, mass in dp.items():
            for word in words:
                hh = h
                ok = True
                for b, mb in zip(word, seg):
                    hh += b - mb
                    if hh < 0:
                        ok = False
                        break
                if ok:
                    nxt[hh] += mass
        dp = nxt
    return tuple(dp.get(h, 0) for h in range(MAXH + 1))


def main():
    words = residue_maximal_words()
    factors = all_length28_factors()

    all_mats = []
    for mech in factors:
        mat = tuple(low_transition_row(mech, words, h)
                    for h in range(MAXH + 1))
        all_mats.append(mat)

    mmax = tuple(tuple(max(mat[i][j] for mat in all_mats)
                       for j in range(MAXH + 1))
                 for i in range(MAXH + 1))
    assert mmax == EXPECTED_MMAX

    min_low_row = tuple(min(sum(mat[i]) for mat in all_mats)
                        for i in range(MAXH + 1))
    assert min_low_row == EXPECTED_MIN_LOW_ROW

    # Exact Collatz-Wielandt style positive potential certificate.
    for i, row in enumerate(mmax):
        mv = sum(row[j] * POTENTIAL[j] for j in range(MAXH + 1))
        lhs = 25 * mv
        rhs = (1 << W) * POTENTIAL[i]
        assert lhs < rhs
        print("row", i, "25*Mmax*v", lhs, "<", rhs,
              "margin", rhs - lhs)

    # H=4 low-to-low probability is >1/25 in every phase: automatic K<25.
    assert 25 * min_low_row[4] > (1 << W)

    # H=3 is the first unresolved state for the trivial mu<=1 argument.
    assert 25 * min_low_row[3] < (1 << W)

    print("min low-to-low row counts", min_low_row)
    print("H=4 automatic low-tail K<25: PASS")
    print("low-height weighted growth < 2^28/25: PASS")
    print("remaining incoming heights: H=0,1,2,3")


if __name__ == "__main__":
    main()
