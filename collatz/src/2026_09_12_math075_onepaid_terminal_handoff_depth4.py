#!/usr/bin/env python3
"""MATH-075: exact one-paid terminal handoff catalogue through macro depth 4.

This extends MATH-061's two-macro composition without changing its exact
cylinder law.  Symbolic states are continued only while source multiplicity is
>1.  As soon as the exact source count collapses to one, the ordinary target
integer is continued directly to the frozen floor 2^71.

Certified counts reproduced by this file:
  depth 2: 1,137 new singleton handoffs, 11,389 multi-source survivors;
  depth 3: 11,511 new singleton handoffs, 85,803 multi-source survivors;
  depth 4: 76,585 new singleton handoffs, 442,957 multi-source survivors.

Unique singleton ordinary targets and maximum additional shortcut descent:
  depth 2: 576 unique, max 71;
  depth 3: 6,562 unique, max 202;
  depth 4: 46,845 unique, max 185.

Every audited singleton descends to <=2^71.  This is a finite exact checkpoint,
not closure of arbitrary one-paid chains, the first universal cell, or Collatz.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math061", HERE / "2026_09_11_math061_onepaid_cylinder_composition_certificate.py"
)
m61 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m61)

LO = 1 << 71

@dataclass(frozen=True)
class State:
    H: int
    Q: int
    source_A: int
    count: int
    target_B: int
    phase_lo: Fraction   # current endpoint phase interval
    phase_hi: Fraction
    macro_count: int


def from_edge(c):
    p = m61.from_one_paid(c)
    return State(
        p.H, p.Q, p.source_A, p.count, p.target_B,
        p.phase_lo * p.phase_scale,
        p.phase_hi * p.phase_scale,
        1,
    )


@lru_cache(None)
def inv3q(Q: int, H: int) -> int:
    mod = 1 << H
    return pow(pow(3, Q, mod), -1, mod)


def compose(p: State, c):
    d = m61.from_one_paid(c)
    lo = max(p.phase_lo, d.phase_lo)
    hi = min(p.phase_hi, d.phase_hi)
    if lo >= hi:
        return None

    mod = 1 << d.H
    residue = ((d.source_A - p.target_B) * inv3q(p.Q, d.H)) % mod
    if residue >= p.count:
        return None
    count = (p.count - 1 - residue) // mod + 1

    matched = p.target_B + 3**p.Q * residue
    assert (matched - d.source_A) % mod == 0
    t0 = (matched - d.source_A) // mod
    target_B = d.target_B + 3**d.Q * t0
    source_A = p.source_A + (1 << p.H) * residue

    return State(
        p.H + d.H,
        p.Q + d.Q,
        source_A,
        count,
        target_B,
        lo * d.phase_scale,
        hi * d.phase_scale,
        p.macro_count + 1,
    )


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descend(n: int, cache: dict[int, int], cap: int = 2000):
    x = n
    path = []
    seen = set()
    while x > LO and x not in cache:
        if x in seen or len(path) >= cap:
            return None
        seen.add(x)
        path.append(x)
        x = shortcut(x)
    d = 0 if x <= LO else cache[x]
    for v in reversed(path):
        d += 1
        cache[v] = d
    return cache.get(n, 0)


def advance(front, edges):
    nxt = []
    terminal = []
    for p in front:
        for c in edges:
            x = compose(p, c)
            if x is None:
                continue
            if x.count <= 1 or x.H >= 73:
                assert x.count <= 1
                terminal.append(x)
            else:
                nxt.append(x)
    return nxt, terminal


def main():
    edges = m61.all_one_paid_cylinders()
    assert len(edges) == 910

    first = [from_edge(c) for c in edges]
    front = [x for x in first if x.count > 1 and x.H < 73]
    assert len(front) == 857

    expected = {
        2: (1_137, 11_389, 576, 71),
        3: (11_511, 85_803, 6_562, 202),
        4: (76_585, 442_957, 46_845, 185),
    }

    cache = {}
    for depth in range(2, 5):
        front, terminal = advance(front, edges)
        unique = {x.target_B for x in terminal}
        max_descent = 0
        for n in unique:
            d = descend(n, cache)
            assert d is not None, n
            max_descent = max(max_descent, d)

        exp_terminal, exp_front, exp_unique, exp_max = expected[depth]
        got = (len(terminal), len(front), len(unique), max_descent)
        assert got == (exp_terminal, exp_front, exp_unique, exp_max), (depth, got)
        print("depth", depth,
              "singleton_handoffs", len(terminal),
              "multi_source", len(front),
              "unique_targets", len(unique),
              "max_descent", max_descent)

    print("PASS MATH-075 exact one-paid terminal handoff audit through depth 4")


if __name__ == "__main__":
    main()
