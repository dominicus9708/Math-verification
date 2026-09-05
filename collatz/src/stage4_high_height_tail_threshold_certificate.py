#!/usr/bin/env python3
"""Exact high-height 28-step L7 tail threshold certificate.

This certificate uses only:
  * the length-7 full-Hensel residue-maximal word rule;
  * exact Sturmian/mechanical factors for alpha=log_3(2);
  * the dyadic parity-vector bijection.

For each length-28 mechanical factor and incoming relative height H, it counts
concatenations of four residue-maximal length-7 words whose cumulative
actual-minus-mechanical odd count never makes the relative height negative.

The minimum over all 29 length-28 mechanical factors is:
  H=0:  1,010,201
  H=1:  4,000,391
  H=2:  8,172,518
  H=3: 12,307,179
  H=4: 15,918,777
  H=5: 18,633,853

Since 15*18,633,853 > 2^28, every incoming H>=5 has a dyadic next-window
admissible probability >1/15. Therefore for ANY conditioned selector measure,
the selector/dyadic likelihood ratio of the coarse required next-window event
is <15. This closes the high-height tail sector for the current Stage-4 budget.

This is not a Collatz proof. H=0,...,4 remain a cross-base problem.
"""

from collections import defaultdict

L = 7
W = 28
EXPECTED_CLASS_COUNTS = (1, 2, 6, 15, 21, 16, 7, 1)
EXPECTED_MIN = (1_010_201, 4_000_391, 8_172_518,
                12_307_179, 15_918_777, 18_633_853)


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
        R, bits = max(arr)
        out.append(bits)
        counts[q] += 1
    assert tuple(counts) == EXPECTED_CLASS_COUNTS
    assert len(out) == 69
    return tuple(out)


def ceil_alpha_count(n):
    """ceil(n log_3 2), exact for integer n."""
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
    # Sturmian complexity is p(n)=n+1, so exactly 29 factors exist.
    seen = {}
    s = 0
    while len(seen) < W + 1:
        f = mechanical_factor(s)
        seen.setdefault(f, s)
        s += 1
        assert s < 1000
    assert len(seen) == 29
    return seen


def admissible_count(mech, words, incoming_height):
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
    return sum(dp.values())


def main():
    words = residue_maximal_words()
    factors = all_length28_factors()

    mins = []
    for H in range(6):
        vals = [(admissible_count(f, words, H), start, f)
                for f, start in factors.items()]
        best = min(vals)
        mins.append(best[0])
        print("H", H, "min", best[0], "phase_start", best[1],
              "mechanical", "".join(map(str, best[2])))

    assert tuple(mins) == EXPECTED_MIN

    # The high-height threshold is exactly H=5 for this universal 1/15 test.
    assert 15 * EXPECTED_MIN[4] < (1 << W)
    assert 15 * EXPECTED_MIN[5] > (1 << W)

    # Monotonicity in incoming height makes H=5 sufficient for every H>=5.
    print("15*min_H5 =", 15 * EXPECTED_MIN[5])
    print("2^28       =", 1 << W)
    print("inverse probability upper < 15: PASS")
    print("high-height tail H>=5 automatic Stage-4 threshold: PASS")


if __name__ == "__main__":
    main()
