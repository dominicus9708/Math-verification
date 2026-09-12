#!/usr/bin/env python3
"""MATH-087: restore exact address only on the phase-danger corridor.

Targets macro depths 18, 19, and 20.

Workflow
--------
1. Import the canonical current-phase exact transition from MATH-085.
2. Import the address-forgotten 126-edge phase over-approximation from MATH-086.
3. At one target depth T, retain only phase-only terminal crossings whose
   lower-envelope Bellman margin is negative.
4. Back-propagate their phase nodes to depth 1.
5. Restore exact dyadic address and same-integer composition only inside that
   backward corridor.
6. At depth T, inspect every exact singleton child from the exact corridor.

A positive result is proof-safe: phase-only positive cells were already safe by
lower bound; phase-only negative cells are the only cells requiring address
restoration, and every exact address-compatible child in their corridor is
checked directly.

This is finite exact arithmetic and does not prove first-cell emptiness or the
Collatz conjecture.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
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
PHASE_EDGES = m86.merged_phase_edges()

EXPECTED_EXACT_COUNTS = {
    18: [20,59,169,357,811,1477,2216,4382,7264,13392,21640,28608,52112,78080,131376,206480,91437],
    19: [10,22,37,78,134,256,408,528,964,1400,2336,3616,4368,7648,10400,16256,24960,6291],
    20: [1,3,5,6,12,16,28,44,48,88,112,144,224,224,352,448,576,896,34],
}
EXPECTED_TERMINALS = {18: 50_133, 19: 2_816, 20: 12}


def phase_min_layers(T: int):
    """Address-forgotten lower-envelope states through T-1."""
    layers = {1: m86.initial_phase_states()}
    for t in range(1, T - 1):
        cont = {}
        for H, lo, hi, alpha in layers[t]:
            for h, elo, ehi, rho, c in PHASE_EDGES:
                a = max(lo, elo)
                b = min(hi, ehi)
                if a >= b:
                    continue
                H2 = H + h
                if H2 > 71:
                    continue
                key = (H2, a * rho, b * rho)
                alpha2 = alpha / rho + c
                old = cont.get(key)
                if old is None or alpha2 < old:
                    cont[key] = alpha2
        layers[t + 1] = [(H, lo, hi, a) for (H, lo, hi), a in cont.items()]
    return layers


def negative_parent_nodes(states):
    """Phase nodes having at least one negative lower-envelope terminal edge."""
    out = set()
    for H, lo, hi, alpha in states:
        for h, elo, ehi, rho, c in PHASE_EDGES:
            a = max(lo, elo)
            b = min(hi, ehi)
            if a >= b:
                continue
            H2 = H + h
            if H2 <= 71:
                continue
            lo2 = a * rho
            alpha2 = alpha / rho + c
            penalty_inf = alpha2 * lo2
            margin = penalty_inf if H2 <= 73 else penalty_inf - LAM * (H2 - 73)
            if margin < 0:
                out.add((H, lo, hi))
    return out


def phase_nodes_and_adjacency(T: int):
    nodes = {1: set((H, lo, hi) for H, lo, hi, _ in m86.initial_phase_states())}
    adj = {}
    for t in range(1, T - 1):
        nxt = set()
        amap = defaultdict(set)
        for H, lo, hi in nodes[t]:
            for idx, (h, elo, ehi, rho, c) in enumerate(PHASE_EDGES):
                a = max(lo, elo)
                b = min(hi, ehi)
                if a >= b:
                    continue
                H2 = H + h
                if H2 > 71:
                    continue
                child = (H2, a * rho, b * rho)
                nxt.add(child)
                amap[(H, lo, hi)].add(child)
        nodes[t + 1] = nxt
        adj[t] = amap
    return nodes, adj


def backward_corridor(T: int, target):
    nodes, adj = phase_nodes_and_adjacency(T)
    danger = {T - 1: set(target)}
    for t in range(T - 2, 0, -1):
        need = danger[t + 1]
        parents = set()
        for p, children in adj[t].items():
            if any(ch in need for ch in children):
                parents.add(p)
        danger[t] = parents
    return danger


def region_map(nodes):
    hm = defaultdict(list)
    for H, lo, hi in nodes:
        hm[H].append((lo, hi))
    return hm


def intersects_state(p, hm):
    return any(max(p.lo, lo) < min(p.hi, hi) for lo, hi in hm.get(p.H, ()))


def exact_corridor(T: int):
    layers = phase_min_layers(T)
    target = negative_parent_nodes(layers[T - 1])
    danger = backward_corridor(T, target)
    maps = {t: region_map(v) for t, v in danger.items()}

    level = [p for p in m85.initial_states() if intersects_state(p, maps[1])]
    counts = [len(level)]

    for t in range(1, T - 1):
        nxt = []
        hm = maps[t + 1]
        for p in level:
            for z in m85.children(p):
                if z.count <= 1:
                    continue
                if intersects_state(z, hm):
                    nxt.append(z)
        level = list(set(nxt))
        counts.append(len(level))

    assert counts == EXPECTED_EXACT_COUNTS[T], (T, counts)

    terminal = 0
    negative = 0
    min_margin = None
    for p in level:
        for z in m85.children(p):
            if z.count != 1:
                continue
            terminal += 1
            penalty_inf = z.alpha * z.lo
            margin = penalty_inf if z.H <= 73 else penalty_inf - LAM * (z.H - 73)
            if min_margin is None or margin < min_margin:
                min_margin = margin
            if margin < 0:
                negative += 1

    assert terminal == EXPECTED_TERMINALS[T]
    assert negative == 0
    assert min_margin is not None and min_margin > 0

    print("target_depth", T)
    print("negative_phase_parent_nodes", len(target))
    print("exact_corridor_counts", counts)
    print("exact_terminal_children", terminal)
    print("negative_exact_terminal_children", negative)
    print("minimum_exact_margin", min_margin, float(min_margin))
    print("PASS MATH-087 target", T)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, choices=(18, 19, 20), required=True)
    args = ap.parse_args()
    exact_corridor(args.target)


if __name__ == "__main__":
    main()
