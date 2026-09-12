#!/usr/bin/env python3
"""MATH-085: exact current-phase replay of one-paid macro depths 4--6.

The transition is algebraically identical to MATH-061 composition, but the
phase history is stored in current-anchor coordinates:

    J = current phase interval,
    P = alpha * Omega_current,
    J' = rho_e * (J intersect I_e),
    alpha' = alpha/rho_e + c_e,
    c_e = beta_e/rho_e in {1/4,1/8}.

Exact dyadic target/source compatibility is retained.  The historical source
anchor A is not needed for future composition once the canonical current
family B+3^Q s and source count are known.

The optional --start/--stop slice applies only to the depth-4 multi-source
parent list for replaying depths 5 and 6 in exact disjoint shards.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m61", HERE / "2026_09_11_math061_onepaid_cylinder_composition_certificate.py"
)
m61 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m61)

LAM = Fraction(19, 503)


@dataclass(frozen=True)
class Edge:
    H: int
    Q: int
    source_A: int
    target_B: int
    lo: Fraction
    hi: Fraction
    rho: Fraction
    c: Fraction


@dataclass(frozen=True)
class State:
    H: int
    Q: int
    count: int
    B: int
    lo: Fraction
    hi: Fraction
    alpha: Fraction
    t: int


def build_edges():
    out = []
    for cyl in m61.all_one_paid_cylinders():
        d = m61.from_one_paid(cyl)
        c = d.penalty_beta / d.phase_scale
        assert c in (Fraction(1, 4), Fraction(1, 8))
        out.append(Edge(
            H=d.H,
            Q=d.Q,
            source_A=d.source_A,
            target_B=d.target_B,
            lo=d.phase_lo,
            hi=d.phase_hi,
            rho=d.phase_scale,
            c=c,
        ))
    assert len(out) == 910
    return tuple(out)


EDGES = build_edges()


@lru_cache(maxsize=None)
def compatible_edge_indices(lo: Fraction, hi: Fraction):
    return tuple(
        i for i, e in enumerate(EDGES)
        if max(lo, e.lo) < min(hi, e.hi)
    )


@lru_cache(maxsize=None)
def inv3(Q: int, H: int):
    mod = 1 << H
    return pow(pow(3, Q, mod), -1, mod)


def initial_states():
    out = []
    atoms = [m61.from_one_paid(c) for c in m61.all_one_paid_cylinders()]
    for d in atoms:
        if d.count <= 1:
            continue
        c = d.penalty_beta / d.phase_scale
        out.append(State(
            H=d.H,
            Q=d.Q,
            count=d.count,
            B=d.target_B,
            lo=d.phase_lo * d.phase_scale,
            hi=d.phase_hi * d.phase_scale,
            alpha=c,
            t=1,
        ))
    assert len(out) == 857
    return out


def append(p: State, e: Edge):
    lo = max(p.lo, e.lo)
    hi = min(p.hi, e.hi)
    if lo >= hi:
        return None

    mod = 1 << e.H
    residue = ((e.source_A - p.B) * inv3(p.Q, e.H)) % mod
    if residue >= p.count:
        return None

    count = (p.count - 1 - residue) // mod + 1
    matched = p.B + 3**p.Q * residue
    assert (matched - e.source_A) % mod == 0
    d_parameter_0 = (matched - e.source_A) // mod
    B = e.target_B + 3**e.Q * d_parameter_0

    return State(
        H=p.H + e.H,
        Q=p.Q + e.Q,
        count=count,
        B=B,
        lo=lo * e.rho,
        hi=hi * e.rho,
        alpha=p.alpha / e.rho + e.c,
        t=p.t + 1,
    )


def children(p: State):
    for i in compatible_edge_indices(p.lo, p.hi):
        z = append(p, EDGES[i])
        if z is not None:
            yield z


def universal_safe(p: State):
    if p.H <= 73:
        return True
    return Fraction(p.t, 12) - LAM * (p.H - 73) >= 0


def phase_safe(p: State):
    if p.H <= 73:
        return True
    # p.alpha * Omega_current is the exact accumulated penalty.
    # p.lo is an infimum of the open current-phase interval.
    return p.alpha * p.lo - LAM * (p.H - 73) >= 0


@dataclass
class Stats:
    terminal: int = 0
    universal: int = 0
    phase: int = 0
    residual: int = 0
    multi: int = 0
    terminal_Hmax: int = 0
    multi_Hmax: int = 0

    def add_terminal(self, p: State):
        self.terminal += 1
        self.terminal_Hmax = max(self.terminal_Hmax, p.H)
        if universal_safe(p):
            self.universal += 1
        if phase_safe(p):
            self.phase += 1
        else:
            self.residual += 1

    def add_multi(self, p: State):
        self.multi += 1
        self.multi_Hmax = max(self.multi_Hmax, p.H)


def expand_level(level):
    nxt = []
    st = Stats()
    for p in level:
        for z in children(p):
            if z.count == 1:
                st.add_terminal(z)
            else:
                st.add_multi(z)
                nxt.append(z)
    return nxt, st


def print_stats(depth, st):
    print(
        "depth", depth,
        "terminal", st.terminal,
        "universal_safe", st.universal,
        "phase_safe", st.phase,
        "residual", st.residual,
        "multi", st.multi,
        "terminal_Hmax", st.terminal_Hmax,
        "multi_Hmax", st.multi_Hmax,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0,
                    help="inclusive depth-4 multi-source parent index")
    ap.add_argument("--stop", type=int, default=None,
                    help="exclusive depth-4 multi-source parent index")
    args = ap.parse_args()

    # Reproduce canonical depths 2--4 first.
    level = initial_states()
    level2, s2 = expand_level(level)
    assert s2.terminal == 1_137 and len(level2) == 11_389

    level3, s3 = expand_level(level2)
    assert s3.terminal == 11_511 and len(level3) == 85_803

    level4, s4 = expand_level(level3)
    assert s4.terminal == 76_585
    assert s4.universal == 76_564
    assert s4.phase == 76_585
    assert s4.residual == 0
    assert len(level4) == 442_957
    assert s4.multi_Hmax <= 71
    print_stats(4, s4)

    start = max(0, args.start)
    stop = len(level4) if args.stop is None else min(args.stop, len(level4))
    assert 0 <= start <= stop <= len(level4)

    # Stream depth 5 and immediately stream every multi-source child to depth 6.
    # No global depth-5 state table is required.
    s5 = Stats()
    s6 = Stats()

    for p4 in level4[start:stop]:
        for p5 in children(p4):
            if p5.count == 1:
                s5.add_terminal(p5)
                continue

            s5.add_multi(p5)
            for p6 in children(p5):
                if p6.count == 1:
                    s6.add_terminal(p6)
                else:
                    s6.add_multi(p6)

    print("parent_slice", start, stop, "of", len(level4))
    print_stats(5, s5)
    print_stats(6, s6)

    if start == 0 and stop == len(level4):
        assert s5.terminal == 372_841
        assert s5.universal == 372_834
        assert s5.phase == 372_841
        assert s5.residual == 0
        assert s5.multi == 1_689_024
        assert s5.multi_Hmax <= 71

        assert s6.terminal == 1_358_935
        assert s6.universal == 1_358_914
        assert s6.phase == 1_358_935
        assert s6.residual == 0
        assert s6.multi == 4_943_810
        assert s6.terminal_Hmax == 90
        assert s6.multi_Hmax <= 71
        print("PASS MATH-085 full depth4-6 current-phase replay")
    else:
        print("PASS MATH-085 exact shard; sum disjoint shards for full depth5-6 totals")


if __name__ == "__main__":
    main()
