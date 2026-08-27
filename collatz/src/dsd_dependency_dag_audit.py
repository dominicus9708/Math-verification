#!/usr/bin/env python3
"""DSD dependency-DAG audit for the Collatz proof program.

This is a proof-control certificate, not a Collatz proof certificate.
It checks that the declared live dependency graph is acyclic, that the
unconditional spine is not contaminated by quarantined conditional results,
and that explicitly forbidden reverse edges are absent.

Only Python's standard library is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Set, Tuple


SAFE = "SAFE"
CONDITIONAL = "CONDITIONAL"
OPEN = "OPEN"
REJECTED = "REJECTED"
ALLOWED_STATUS = {SAFE, CONDITIONAL, OPEN, REJECTED}


@dataclass(frozen=True)
class Module:
    name: str
    status: str
    deps: FrozenSet[str]
    formation_domain: str
    state: str
    exits: str
    unconditional_candidate: bool = False


MODULES: Dict[str, Module] = {
    "C0": Module(
        "C0", SAFE, frozenset(),
        "hypothetical minimal counterexample above retained published finite base",
        "N, shortcut orbit, first-descent prohibition",
        "normalized minimal-counterexample corridor",
        True,
    ),
    "C1": Module(
        "C1", SAFE, frozenset({"C0"}),
        "C0 corridor at first global coefficient crossing",
        "N, A0, Q0, g",
        "second/later crossing, coefficient survival, separately justified cycle branch",
        True,
    ),
    "C2": Module(
        "C2", SAFE, frozenset({"C1"}),
        "first-resonance endpoint with phase-renewal split",
        "A0,Q0,K1,P1,J0,R0,A2,Q2,h",
        "surplus recovery OR exact second lower resonance",
        True,
    ),
    "C3": Module(
        "C3", SAFE, frozenset({"C2"}),
        "audited local endpoint gap bands after repaired second resonance",
        "gap band, active multiplicities, scale",
        "J0 debit, A0 return, survival beyond current scale",
        True,
    ),
    "C4": Module(
        "C4", SAFE, frozenset({"C3"}),
        "A0 first-crossing sector",
        "ten-J0 checkpoint surplus s, U-tail, endpoint gap",
        "finite terminal recovery OR A0-only cycle OR leave A0 language",
        True,
    ),
    # C5 is deliberately independent of the near-root/A0/J0 budget chain.
    "C5": Module(
        "C5", SAFE, frozenset(),
        "binary gap words with ordering recurrence",
        "gap word w, displacement p, ordering Bellman cost B_w(p)",
        "finite-depth Hensel refinement",
        True,
    ),
    "C6": Module(
        "C6", OPEN, frozenset({"C4", "C5"}),
        "s=1 terminal-recovery Hensel sector",
        "finite-depth congruence state plus relaxed suffix",
        "monotone full-Hensel lower bound OR surviving Hensel language",
        False,
    ),
    "C7": Module(
        "C7", OPEN, frozenset({"C1", "C2", "C3", "C4", "C6"}),
        "independently derived near-root budget plus C6 lower bound",
        "D_allowed and inf T_Hensel",
        "terminal-recovery closure OR surviving recovery language",
        False,
    ),
    "C8": Module(
        "C8", OPEN, frozenset({"C7"}),
        "all exits from current resonance/Hensel language",
        "later scales, infinite survivor, cycles, other Hensel-compatible exits",
        "global closure only after exhaustive routing",
        False,
    ),
    "Q1": Module(
        "Q1", CONDITIONAL, frozenset(),
        "Ansari recursive-sufficiency / ternary-entry proposal",
        "F_n deletion chain",
        "repaired entry theorem OR remain quarantined",
        False,
    ),
    "Q2": Module(
        "Q2", CONDITIONAL, frozenset({"Q1"}),
        "fixed ternary selector family",
        "m44/m45 selector, carry, Fourier, same-address data",
        "conditional family conclusions only",
        False,
    ),
}


# Edges that would encode known circular/invalid proof moves.
FORBIDDEN_EDGES: FrozenSet[Tuple[str, str]] = frozenset({
    # source -> destination
    ("C7", "C5"),  # near-root comparison may not construct ordering/Hensel lower layer
    ("C7", "C6"),  # desired budget contradiction may not justify Hensel refinement
    ("C3", "C5"),  # A0/J0 macro budget may not justify ordering-only Bellman bound
    ("C4", "C5"),  # terminal near-return geometry may not be used to derive C5
    ("Q1", "C0"),
    ("Q1", "C1"),
    ("Q2", "C0"),
    ("Q2", "C1"),
    ("Q2", "C2"),
    ("Q2", "C3"),
    ("Q2", "C4"),
    ("Q2", "C5"),
    ("Q2", "C6"),
    ("Q2", "C7"),
    ("Q2", "C8"),
})


def edges(modules: Dict[str, Module]) -> Set[Tuple[str, str]]:
    """Return dependency edges in source -> destination orientation."""
    result: Set[Tuple[str, str]] = set()
    for dst, module in modules.items():
        for src in module.deps:
            result.add((src, dst))
    return result


def validate_schema(modules: Dict[str, Module]) -> None:
    for key, module in modules.items():
        assert key == module.name, (key, module.name)
        assert module.status in ALLOWED_STATUS, (key, module.status)
        assert module.formation_domain.strip(), key
        assert module.state.strip(), key
        assert module.exits.strip(), key
        for dep in module.deps:
            assert dep in modules, (key, dep)


def topo_sort(modules: Dict[str, Module]) -> List[str]:
    indeg = {name: len(module.deps) for name, module in modules.items()}
    children: Dict[str, Set[str]] = {name: set() for name in modules}
    for dst, module in modules.items():
        for src in module.deps:
            children[src].add(dst)

    ready = sorted(name for name, degree in indeg.items() if degree == 0)
    order: List[str] = []
    while ready:
        node = ready.pop(0)
        order.append(node)
        for child in sorted(children[node]):
            indeg[child] -= 1
            if indeg[child] == 0:
                ready.append(child)
                ready.sort()

    assert len(order) == len(modules), "dependency cycle detected"
    return order


def transitive_dependencies(name: str, modules: Dict[str, Module]) -> Set[str]:
    seen: Set[str] = set()
    stack = list(modules[name].deps)
    while stack:
        dep = stack.pop()
        if dep in seen:
            continue
        seen.add(dep)
        stack.extend(modules[dep].deps)
    return seen


def validate_unconditional_quarantine(modules: Dict[str, Module]) -> None:
    """No SAFE unconditional candidate may transitively depend on Q/OPEN/REJECTED."""
    for name, module in modules.items():
        if not (module.unconditional_candidate and module.status == SAFE):
            continue
        for dep in transitive_dependencies(name, modules):
            dep_status = modules[dep].status
            assert dep_status == SAFE, (
                f"unconditional leakage: {name} depends on {dep} ({dep_status})"
            )


def validate_forbidden_edges(modules: Dict[str, Module]) -> None:
    actual = edges(modules)
    bad = actual & FORBIDDEN_EDGES
    assert not bad, f"forbidden reverse/conditional edge(s): {sorted(bad)}"


def validate_key_separations(modules: Dict[str, Module]) -> None:
    # C5 must stay independent of the near-root resonance budget spine.
    assert modules["C5"].deps == frozenset()
    # The first legal join of C4 geometry and C5 lower-bound machinery is C6.
    assert {"C4", "C5"}.issubset(modules["C6"].deps)
    # C7 may compare only after C6 exists as a separate node.
    assert "C6" in modules["C7"].deps
    # Quarantined selector family cannot enter the unconditional spine.
    for c in ["C0", "C1", "C2", "C3", "C4", "C5"]:
        assert "Q1" not in transitive_dependencies(c, modules)
        assert "Q2" not in transitive_dependencies(c, modules)


def main() -> None:
    validate_schema(MODULES)
    order = topo_sort(MODULES)
    validate_forbidden_edges(MODULES)
    validate_unconditional_quarantine(MODULES)
    validate_key_separations(MODULES)

    print("DSD dependency DAG audit: PASS")
    print("topological order:", " -> ".join(order))
    print("SAFE unconditional candidates:",
          ", ".join(name for name, m in MODULES.items()
                    if m.unconditional_candidate and m.status == SAFE))
    print("OPEN gates:",
          ", ".join(name for name, m in MODULES.items() if m.status == OPEN))
    print("QUARANTINED conditional modules:",
          ", ".join(name for name, m in MODULES.items() if m.status == CONDITIONAL))
    print("forbidden reverse-edge audit: PASS")
    print("conditional-leak audit: PASS")
    print("NOTE: PASS certifies proof-graph hygiene only; it does not prove Collatz.")


if __name__ == "__main__":
    main()
