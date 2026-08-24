#!/usr/bin/env python3
"""Exact finite audit of neutral-return entropy inside the aligned L7 language.

This certificate checks two things that are useful for the current Stage-4
architecture:

1. at length 28 every mechanical phase has a strong finite neutral-return cost;
2. that cost dilutes with excursion length, and every audited mechanical factor
   through length 140 still admits a one-excursion neutral word.

Therefore a fixed per-time exponential penalty cannot be inferred merely from
requiring a neutral return.  This is a negative-control certificate, not a
Collatz proof.
"""
from itertools import product
from collections import defaultdict


def critical_word(T):
    """Exact coefficient-critical word b_{j+1}-b_j, b_j=ceil(j log_3 2)."""
    b = [0] * (T + 1)
    p3 = 1
    k = 0
    for j in range(1, T + 1):
        target = 1 << j
        while p3 < target:
            p3 *= 3
            k += 1
        b[j] = k
    return [b[j + 1] - b[j] for j in range(T)]


def correction(bits):
    R = 0
    q = 0
    for i, bit in enumerate(bits):
        if bit:
            R = 3 * R + (1 << i)
            q += 1
    return q, R


# Exact locally residue-maximal L7 representatives.
classes = [{} for _ in range(8)]
for word in product((0, 1), repeat=7):
    q, R = correction(word)
    r = R % (3 ** q)
    old = classes[q].get(r)
    if old is None or R > old[0]:
        classes[q][r] = (R, word)

assert tuple(len(c) for c in classes) == (1, 2, 6, 15, 21, 16, 7, 1)
ALLOWED = [word for cls in classes for _, word in cls.values()]
assert len(ALLOWED) == 69


def transitions(ref7):
    out = defaultdict(int)
    for word in ALLOWED:
        h = 0
        hmin = 0
        departures = 0
        for bit, ref in zip(word, ref7):
            old = h
            h += bit - ref
            hmin = min(hmin, h)
            if old == 0 and h > 0:
                departures += 1
        out[(hmin, h, departures)] += 1
    return [(a, b, d, c) for (a, b, d), c in out.items()]


TRANS = {}


def audit_factor(ref):
    # state = (current relative height, number of positive excursions)
    dp = {(0, 0): 1}
    for off in range(0, len(ref), 7):
        rr = tuple(ref[off:off + 7])
        tr = TRANS.setdefault(rr, transitions(rr))
        nd = defaultdict(int)
        for (hin, excursions), count in dp.items():
            for hmin, delta, dep, mult in tr:
                if hin + hmin >= 0:
                    nd[(hin + delta, excursions + dep)] += count * mult
        dp = nd

    neutral = sum(count for (h, _), count in dp.items() if h == 0)
    one_excursion = sum(
        count for (h, e), count in dp.items() if h == 0 and e == 1
    )
    return neutral, one_excursion


# A Sturmian word has L+1 factors of length L.  Sampling starts at multiples
# of seven is still an irrational rotation, so the aligned orbit visits every
# factor cylinder.  We scan until all L+1 factors have appeared.
MAX_K = 20
WORD = critical_word(7 * 20000 + 7 * MAX_K + 10)


def factors(L):
    out = set()
    for n in range(20000):
        start = 7 * n
        out.add(tuple(WORD[start:start + L]))
        if len(out) == L + 1:
            break
    assert len(out) == L + 1
    return out


EXPECTED = {
    # k: (number of factors, maximum neutral language size)
    4: (29, 707250),
    6: (43, 1690594220),
    8: (57, 4989609817953),
    12: (85, 64757661195102841815),
    20: (141, 7172314386354445045524576689173865),
}

for k, (expected_nf, expected_max) in EXPECTED.items():
    L = 7 * k
    fs = factors(L)
    vals = [audit_factor(f) for f in fs]
    max_neutral = max(n for n, _ in vals)

    assert len(fs) == expected_nf
    assert max_neutral == expected_max

    # Every audited phase admits at least one word consisting of one single
    # positive excursion before the final neutral return.  Therefore L7 does
    # not force a linear number of returns.
    assert min(one for _, one in vals) > 0

    if k == 4:
        # -log2(max_neutral / 69^4)/28 > 7/50, checked without logs.
        assert (69 ** 4) ** 25 > (max_neutral ** 25) * (2 ** 98)

    print(k, L, len(fs), max_neutral, min(one for _, one in vals))

print("L7 neutral-excursion entropy audit: PASS")
