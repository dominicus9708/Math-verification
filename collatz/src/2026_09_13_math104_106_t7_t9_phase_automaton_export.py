#!/usr/bin/env python3
"""MATH-104..106: exact phase-danger automaton exporter for one-paid t=9,8,7.

This is the direct target-parameterized continuation of the MATH-103 stage-A
construction.  It deliberately builds only the exact phase-danger corridor;
same-integer compatibility is then replayed by the existing MATH-102 generic
compact 2-adic carry verifier.

Usage:
    python 2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 9
    python 2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 8
    python 2026_09_13_math104_106_t7_t9_phase_automaton_export.py --target 7

Outputs are t9_*.tsv, t8_*.tsv, or t7_*.tsv in the current directory.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
S85 = spec_from_file_location(
    "m85", HERE / "2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py"
)
m85 = module_from_spec(S85)
assert S85.loader is not None
S85.loader.exec_module(m85)
S86 = spec_from_file_location(
    "m86", HERE / "2026_09_12_math086_onepaid_phase_horizon_certificate.py"
)
m86 = module_from_spec(S86)
assert S86.loader is not None
S86.loader.exec_module(m86)

LAM = Fraction(19, 503)
EDGES = m85.EDGES
MEDGES = m86.merged_phase_edges()
EXPECTED_ROOTS = {9: 373, 8: 428, 7: 486}
EXPECTED_PHASE_STATS = {
    9: (39_902, 32_732, 155),
    8: (41_916, 35_844, 155),
    7: (42_151, 39_121, 155),
}


def clog(m: int) -> int:
    return 0 if m == 1 else (m - 1).bit_length()


def danger_graph(target: int):
    levels = {1: m86.initial_phase_states()}
    adjacency = {}
    negatives = {}
    for d in range(1, target):
        children = {}
        outgoing = defaultdict(set)
        bad = set()
        for H, lo, hi, a0 in levels[d]:
            parent = (H, lo, hi)
            for h, elo, ehi, rho, c in MEDGES:
                x = max(lo, elo)
                y = min(hi, ehi)
                if x >= y:
                    continue
                H2 = H + h
                lo2 = x * rho
                hi2 = y * rho
                a2 = a0 / rho + c
                if H2 > 71:
                    margin = a2 * lo2 if H2 <= 73 else a2 * lo2 - LAM * (H2 - 73)
                    if margin < 0:
                        bad.add(parent)
                else:
                    key = (H2, lo2, hi2)
                    old = children.get(key)
                    if old is None or a2 < old:
                        children[key] = a2
                    outgoing[parent].add(key)
        levels[d + 1] = [(H, lo, hi, a) for (H, lo, hi), a in children.items()]
        adjacency[d] = outgoing
        negatives[d + 1] = bad

    danger = {target - 1: set(negatives[target])}
    for d in range(target - 2, 0, -1):
        danger[d] = {
            p for p, ch in adjacency[d].items() if ch & danger[d + 1]
        }
    return danger


def merge_danger(danger):
    out = {}
    for d, states in danger.items():
        by_H = defaultdict(list)
        for H, lo, hi in states:
            by_H[H].append((lo, hi))
        for H, intervals in by_H.items():
            intervals.sort()
            merged = []
            lo, hi = intervals[0]
            for a, b in intervals[1:]:
                if a <= hi:
                    hi = max(hi, b)
                else:
                    merged.append((lo, hi))
                    lo, hi = a, b
            merged.append((lo, hi))
            by_H[H] = merged
        out[d] = by_H
    return out


PID = {}
PHASES = []


def pid(lo, hi):
    key = (lo, hi)
    if key not in PID:
        PID[key] = len(PHASES)
        PHASES.append(key)
    return PID[key]


@lru_cache(maxsize=None)
def step(p: int, e: int) -> int:
    lo, hi = PHASES[p]
    E = EDGES[e]
    a = max(lo, E.lo)
    b = min(hi, E.hi)
    return -1 if a >= b else pid(a * E.rho, b * E.rho)


@lru_cache(maxsize=None)
def inv3(q: int, bits: int) -> int:
    mod = 1 << bits
    return pow(pow(3, q, mod), -1, mod)


def export(target: int):
    if target not in EXPECTED_ROOTS:
        raise ValueError("target must be one of 7, 8, 9")

    PID.clear()
    PHASES.clear()
    step.cache_clear()
    inv3.cache_clear()

    danger = merge_danger(danger_graph(target))

    def hit(d, H, p):
        lo, hi = PHASES[p]
        return any(
            max(lo, a) < min(hi, b)
            for a, b in danger.get(d, {}).get(H, [])
        )

    @lru_cache(maxsize=None)
    def cand(d, H, p):
        out = []
        for i, E in enumerate(EDGES):
            cp = step(p, i)
            if cp >= 0 and hit(d + 1, H + E.H, cp):
                out.append((i, cp))
        return tuple(out)

    roots = []
    for s in m85.initial_states():
        R = clog(s.count)
        P = 73 + R
        mod = 1 << P
        g = inv3(s.Q, P)
        x = s.B * g % mod
        p = pid(s.lo, s.hi)
        if hit(1, s.H, p):
            roots.append((s.H, s.count, x, g, p))

    assert len(roots) == EXPECTED_ROOTS[target]

    levels = {1: set((r[0], r[4]) for r in roots)}
    trans = []
    for d in range(1, target - 1):
        nxt = set()
        for H, p in levels[d]:
            for ei, cp in cand(d, H, p):
                nxt.add((H + EDGES[ei].H, cp))
                trans.append((d, H, p, ei, H + EDGES[ei].H, cp))
        levels[d + 1] = nxt

    term = []
    for H, p in levels[target - 1]:
        lo, hi = PHASES[p]
        for i, E in enumerate(EDGES):
            if max(lo, E.lo) < min(hi, E.hi):
                term.append((H, p, i))

    expected_trans, expected_term, expected_pid = EXPECTED_PHASE_STATS[target]
    assert len(trans) == expected_trans
    assert len(term) == expected_term
    assert len(PID) == expected_pid

    prefix = f"t{target}"
    rows_by_file = {
        f"{prefix}_edges.tsv": [(i, e.H, e.Q, e.source_A, e.target_B) for i, e in enumerate(EDGES)],
        f"{prefix}_roots.tsv": [(i, *r) for i, r in enumerate(roots)],
        f"{prefix}_trans.tsv": trans,
        f"{prefix}_term.tsv": term,
    }
    for filename, rows in rows_by_file.items():
        with open(filename, "w", encoding="utf-8") as f:
            for row in rows:
                f.write("\t".join(map(str, row)) + "\n")

    print(
        f"PASS t={target} stage A",
        "roots", len(roots),
        "trans", len(trans),
        "term", len(term),
        "phase_ids", len(PID),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, required=True, choices=(7, 8, 9))
    args = ap.parse_args()
    export(args.target)


if __name__ == "__main__":
    main()
