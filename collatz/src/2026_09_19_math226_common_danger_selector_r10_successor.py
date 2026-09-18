#!/usr/bin/env python3
"""MATH-226 common mechanical danger selector.

Reconstruct the frozen r=10 negative-candidate output exactly, then test every
possible *immediate next* Bellman-dangerous low-paid tag r=2..10 by one common
mechanical-prefix selector law.

No ordinary AP member is scanned.

For current child
    Y = B + 3^Q s, 0 <= s < M
and next dangerous emitted paid count r,
    Lmin = ceil(log2 M) + zmin(r).
Every dangerous successor must realize a zero-cost mechanical word of length
Lmin.  For each exact phase-compatible word with canonical source residue A,
compatibility selects
    s = (A-B) * 3^(-Q) mod 2^Lmin.
Since M <= 2^R < 2^Lmin, each word contributes at most one ordinary source.

The selected ordinary anchors are then exact-iterated to the frozen floor.
This is a successor regression/application, not a full r=10 closure theorem.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent

SPEC = spec_from_file_location(
    "m206", HERE / "2026_09_19_math206_initial_overshoot_reset_catalogue.py"
)
m206 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

m65 = m206.m65
m58 = m65.m58

LO = 1 << 71
R0 = 10

ZMIN = {2:1, 3:2, 4:3, 5:6, 6:7, 7:8, 8:10, 9:11, 10:13}

EXPECTED_SOURCE = {
    "cells": (994, 91, 396, 507),
    "nodes": 1_994_258,
    "leaves": 278_725,
    "mass": 27_557_263_803_397,
    "max_m": 830_483_089_363,
}

EXPECTED = {
    2:  (118896, 128986, 65625, 212),
    3:  (62924,   64694, 32972, 212),
    4:  (32501,   32890, 16885, 154),
    5:  (4237,     4237,  2234, 118),
    6:  (2077,     2077,  1120, 118),
    7:  (1014,     1014,   544, 118),
    8:  (239,       239,   134,  92),
    9:  (122,       122,    69,  61),
    10: (22,         22,    14,  53),
}

EXPECTED_R10_PHASE_WORD_COUNTS = {
    1: 201409,
    2: 44689,
    3: 31396,
    4: 1231,
}
EXPECTED_R10_RAW_WORD_SELECTORS = 389899


def ceil_log2_m(m):
    assert m >= 1
    return 0 if m == 1 else (m - 1).bit_length()


def child_phase_interval(cell):
    (L, start_R, E0, q0, lo, hi, tmin, tmax,
     eps, gs, hcl, H, margin) = cell

    mid = (lo + hi) / 2
    g = m65.phase_multiplier(q0, mid)
    for e in eps:
        g *= Fraction(2, 3) if e == 0 else Fraction(4, 3)

    a, b = lo * g, hi * g
    assert Fraction(1, 2) <= a <= 1
    assert Fraction(1, 2) <= b <= 1
    assert a < b
    return a, b


def phase_words(L, lo, hi):
    """All mechanical words attained on exact phase interval (lo,hi).

    The project convention uses <= at threshold cuts.  We include open-cell
    representatives plus all internal/right cut points and deduplicate words.
    This is conservative at interval endpoints and exact for the frozen cells.
    """
    cuts = {lo, hi}
    for j in range(1, L + 1):
        t = m58.TAU[j]
        if lo < t < hi:
            cuts.add(t)

    s = sorted(cuts)
    words = set()

    for a, b in zip(s[:-1], s[1:]):
        words.add(m58.mechanical_factor(L, (a + b) / 2))

    for x in s:
        if Fraction(1, 2) < x <= 1:
            words.add(m58.mechanical_factor(L, x))

    return words


def build_children():
    total, safe, singleton, critical = m65.classify_cells(R0)
    assert (total, len(safe), len(singleton), len(critical)) == EXPECTED_SOURCE["cells"]

    children = []
    nodes = 0
    leaves = 0
    mass = 0
    max_m = 0

    for group in (singleton, critical):
        for cell in group:
            out, n = m65.negative_candidate_cylinders(cell, R0)
            nodes += n
            plo, phi = child_phase_interval(cell)

            for leaf in out:
                H, Q, A, B, count = m206.full_factor(cell, leaf)
                children.append((B, Q, count, plo, phi))
                leaves += 1
                mass += count
                max_m = max(max_m, count)

    assert nodes == EXPECTED_SOURCE["nodes"]
    assert leaves == EXPECTED_SOURCE["leaves"]
    assert mass == EXPECTED_SOURCE["mass"]
    assert max_m == EXPECTED_SOURCE["max_m"]
    return children


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descent_steps(n, cache):
    x = n
    path = []
    seen = set()

    while x > LO and x not in cache:
        assert x not in seen
        seen.add(x)
        path.append(x)
        x = shortcut(x)
        assert len(path) < 10000

    d = 0 if x <= LO else cache[x]
    for y in reversed(path):
        d += 1
        cache[y] = d
    return cache.get(n, 0)


def selectors(children, r):
    z = ZMIN[r]
    hit_families = 0
    selector_records = 0
    anchors = set()

    word_count_hist = {}
    raw_word_selectors = 0

    for B, Q, count, plo, phi in children:
        R = ceil_log2_m(count)
        Lm = R + z
        mod = 1 << Lm

        words = phase_words(Lm, plo, phi)
        if r == 10:
            word_count_hist[len(words)] = word_count_hist.get(len(words), 0) + 1
            raw_word_selectors += len(words)

        inv = pow(pow(3, Q, mod), -1, mod)
        local = set()

        for w in words:
            A = m58.start_residue(w)
            s = ((A - B) * inv) % mod
            if s < count:
                local.add(B + (3 ** Q) * s)

        if local:
            hit_families += 1
            selector_records += len(local)
            anchors.update(local)

    if r == 10:
        assert word_count_hist == EXPECTED_R10_PHASE_WORD_COUNTS, word_count_hist
        assert raw_word_selectors == EXPECTED_R10_RAW_WORD_SELECTORS

    return hit_families, selector_records, anchors


def main():
    children = build_children()
    cache = {}

    for r in range(2, 11):
        hit, recs, anchors = selectors(children, r)
        maxd = max((descent_steps(y, cache) for y in anchors), default=0)
        got = (hit, recs, len(anchors), maxd)
        assert got == EXPECTED[r], (r, got, EXPECTED[r])
        print(
            "next_r", r,
            "hit_families", hit,
            "selector_records", recs,
            "unique_anchors", len(anchors),
            "max_descent", maxd,
        )

    print("PASS MATH-226 common danger selector successor audit")
    print("ALL immediate dangerous next tags r=2..10 descend to <=2^71")
    print("FULL r10 LAYER OPEN: arbitrary intervening safe transfers not yet closed")


if __name__ == "__main__":
    main()
