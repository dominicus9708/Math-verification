#!/usr/bin/env python3
"""DSD sub-DAG audit for the two logically distinct s=1 routes.

This proof-control certificate separates:

A. an independent local Hensel/lower-bound route, which must not read the
   global reset/near-root budget; and
B. a direct physical-intersection route, which is allowed to read the reset
   physical boundary because it does not claim an independent lower bound.

The separation prevents the recent checkpoint/corridor reductions from being
silently fed back into the independent C6A lower-bound comparison.  This is
not a Collatz proof certificate.
"""

from collections import defaultdict, deque

SAFE = "SAFE"
OPEN = "OPEN"

nodes = {
    # Upstream abstract names retained from the canonical DAG.
    "C4F": (SAFE, set()),                    # local A0 formation grammar
    "C4R": (SAFE, {"C4F"}),               # global physical/reset routing (C3 omitted here)
    "C5":  (SAFE, set()),                   # independent ordering/Hensel relaxation

    # Common local s=1 structure, still independent of the reset budget.
    "S1L": (SAFE, {"C4F"}),
    # exact renewal point, pre 0->0 / tail 0->-1, p_int in {0,1}
    "S1I": (SAFE, {"S1L", "C5"}),
    # exact two-boundary Xi/Hensel invariant and local ordered-control algebra

    # Route A: independent lower-bound strategy.
    "S1H": (OPEN, {"S1L", "S1I", "C5"}),
    # Must remain independent of C4R and every physical corridor descendant.

    # Route B: direct physical intersection.
    "S1P0": (SAFE, {"C4R", "S1L"}),
    # instantiate reset s=1 physical X,Y domain
    "S1P1": (SAFE, {"S1P0", "S1I"}),
    # 73-bit checkpoint exposure / physical Xi boundary coordinates
    "S1P2": (SAFE, {"S1P1"}),
    # 40-bit L-/L+ debit-credit corridor
    "S1P3": (SAFE, {"S1P2"}),
    # 28x28 CRT, local 26-trit/40-bit exposure, four-window singleton formation
    "S1PX": (OPEN, {"S1P3", "S1I"}),
    # full long-bridge extension / exact digital intersection

    # A future branch-specific closure can consume either an independent
    # contradiction or a direct physical nonintersection, but neither is
    # automatically all-surplus coverage.
    "S1C": (OPEN, {"S1H", "S1PX"}),
}

# The canonical implementation may treat S1H and S1PX as alternative routes
# rather than requiring both.  Here S1C is only a bookkeeping join node; the
# assertions below are about forbidden information flow, not logical OR syntax.

for name, (status, deps) in nodes.items():
    assert status in {SAFE, OPEN}
    for d in deps:
        assert d in nodes, (name, d)

# Topological acyclicity.
indeg = {n: len(v[1]) for n, v in nodes.items()}
children = defaultdict(set)
for n, (_, deps) in nodes.items():
    for d in deps:
        children[d].add(n)
q = deque(sorted(n for n, k in indeg.items() if k == 0))
order = []
while q:
    n = q.popleft()
    order.append(n)
    for c in sorted(children[n]):
        indeg[c] -= 1
        if indeg[c] == 0:
            q.append(c)
assert len(order) == len(nodes), "s=1 sub-DAG cycle detected"


def ancestors(name):
    out = set()
    stack = list(nodes[name][1])
    while stack:
        x = stack.pop()
        if x in out:
            continue
        out.add(x)
        stack.extend(nodes[x][1])
    return out


# Critical isolation lock: independent lower-bound route cannot read physical routing.
assert "C4R" not in ancestors("S1H")
for physical in ["S1P0", "S1P1", "S1P2", "S1P3", "S1PX"]:
    assert physical not in ancestors("S1H")

# Direct route is explicitly physical and is therefore not to be advertised as
# an independent lower-bound channel.
assert "C4R" in ancestors("S1P1")
assert "C4R" in ancestors("S1P2")
assert "C4R" in ancestors("S1P3")
assert "C4R" in ancestors("S1PX")

# Both routes share only upstream local exact structure, not downstream conclusions.
assert "S1I" in ancestors("S1H")
assert "S1I" in ancestors("S1PX")
assert "S1PX" not in ancestors("S1H")
assert "S1H" not in ancestors("S1PX")

print("PASS DSD s=1 dual-route sub-DAG audit")
print("topological_order", " -> ".join(order))
print("independent_route", "C4F+C5 -> S1L/S1I -> S1H")
print("physical_route", "C4R+S1L/S1I -> S1P0 -> S1P1 -> S1P2 -> S1P3 -> S1PX")
print("physical_to_independent_reverse_leak", False)
print("all_surplus_promotion", False)
