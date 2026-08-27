#!/usr/bin/env python3
"""DSD dependency-DAG audit for the Collatz proof program.

This is a proof-control certificate, not a Collatz proof certificate.
It checks that the declared live dependency graph is acyclic, that the
unconditional spine is not contaminated by quarantined conditional results,
that the s=1 Hensel sector cannot masquerade as all-surplus coverage, and
that complementary escape branches remain explicit.

Only Python's standard library is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, List, Set, Tuple

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
        "phase-renewal split at K1",
        True,
    ),
    "C2": Module(
        "C2", SAFE, frozenset({"C1"}),
        "first-resonance endpoint at the K1 renewal scale",
        "K1, P1, q_K1, phase defects",
        "C2E exact resonance OR E2S surplus recovery",
        True,
    ),
    "C2E": Module(
        "C2E", SAFE, frozenset({"C2"}),
        "exact second lower resonance q_K1 = P1",
        "A2, Q2, h with 2^33 < h < 7*2^33",
        "audited local J0/A0 gap corridor",
        True,
    ),
    "E2S": Module(
        "E2S", OPEN, frozenset({"C2"}),
        "surplus-recovery branch q_K1 >= P1 + 1",
        "K1 surplus and later coefficient state",
        "independent routing/closure OR later-scale survivor",
        False,
    ),
    "C3": Module(
        "C3", SAFE, frozenset({"C2E"}),
        "audited local endpoint gap bands on the exact second-resonance branch",
        "gap band, active multiplicities, scale",
        "J0 debit, A0 return, survival beyond current scale",
        True,
    ),
    "C4": Module(
        "C4", SAFE, frozenset({"C3"}),
        "all A0 first-crossing sectors with checkpoint surplus s >= 1",
        "ten-J0 checkpoint surplus s, U-tail, endpoint gap",
        "finite terminal recovery OR E4C A0-only cycle OR E4L leave A0 language",
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
    # C6A is intentionally only the minimal-surplus subdomain.
    "C6A": Module(
        "C6A", OPEN, frozenset({"C4", "C5"}),
        "s = 1 terminal-recovery Hensel sector only",
        "finite-depth congruence state plus relaxed suffix for s=1",
        "s=1 full-Hensel lower bound OR surviving s=1 language",
        False,
    ),
    # C6B is a separate all-surplus coverage theorem.  It can be proved by
    # extremality, a uniform bound, or an audited partition of all s >= 1.
    "C6B": Module(
        "C6B", OPEN, frozenset({"C4", "C5"}),
        "all A0 terminal-recovery sectors with s >= 1",
        "surplus s, Hensel state, uniform/partitioned lower-bound data",
        "all-surplus Hensel lower bound OR explicit surviving surplus sectors",
        False,
    ),
    "E4C": Module(
        "E4C", OPEN, frozenset({"C4"}),
        "infinite consecutive A0-return language classified as a nontrivial positive cycle",
        "cycle endpoint and block period",
        "independent cycle exclusion OR remain an open cycle escape",
        False,
    ),
    "E4L": Module(
        "E4L", OPEN, frozenset({"C4"}),
        "leave the present A0 language / later finite or infinite coefficient survivor",
        "later scale, coefficient state, Hensel-compatible escape data",
        "independent later-scale routing/closure",
        False,
    ),
    "C7": Module(
        "C7", OPEN, frozenset({"C1", "C2E", "C3", "C4", "C6B"}),
        "independently derived near-root budget plus full-domain C6B lower bound",
        "D_allowed and all-surplus inf T_Hensel",
        "terminal-recovery closure OR surviving recovery language",
        False,
    ),
    "C8": Module(
        "C8", OPEN, frozenset({"C7", "E2S", "E4C", "E4L"}),
        "complete exit ledger from the current resonance/Hensel language",
        "terminal recovery, K1 surplus, cycle, later-scale/infinite-survivor exits",
        "global closure only after every explicit escape is independently closed",
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
    ("C7", "C5"),
    ("C7", "C6A"),
    ("C7", "C6B"),
    ("C3", "C5"),
    ("C4", "C5"),
    ("C6A", "C4"),
    ("C6A", "C5"),
    ("C6A", "C6B"),  # no automatic s=1 -> all-surplus promotion
    ("E2S", "C2E"), # complementary K1 branch may not be folded into exact branch for free
    ("E4C", "C4"),
    ("E4L", "C4"),
    ("Q1", "C0"),
    ("Q1", "C1"),
    ("Q2", "C0"),
    ("Q2", "C1"),
    ("Q2", "C2"),
    ("Q2", "C2E"),
    ("Q2", "C3"),
    ("Q2", "C4"),
    ("Q2", "C5"),
    ("Q2", "C6A"),
    ("Q2", "C6B"),
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
    assert modules["C5"].deps == frozenset()

    # K1 split is explicit: C3 only consumes the exact-resonance child.
    assert "C2" in modules["C2E"].deps
    assert "C2" in modules["E2S"].deps
    assert "C2E" in modules["C3"].deps
    assert "E2S" not in modules["C3"].deps

    # Both terminal Hensel modules may use C4 formation data and C5 relaxation.
    assert {"C4", "C5"}.issubset(modules["C6A"].deps)
    assert {"C4", "C5"}.issubset(modules["C6B"].deps)

    # Critical surplus scope lock.
    assert "C6A" not in modules["C6B"].deps
    assert "C6B" in modules["C7"].deps
    assert "C6A" not in modules["C7"].deps

    # Global branch ledger cannot forget complementary escapes.
    for escape in ["E2S", "E4C", "E4L", "C7"]:
        assert escape in modules["C8"].deps

    # Quarantined selector family cannot enter the SAFE spine.
    for c in ["C0", "C1", "C2", "C2E", "C3", "C4", "C5"]:
        assert "Q1" not in transitive_dependencies(c, modules)
        assert "Q2" not in transitive_dependencies(c, modules)


def validate_scope_coverage(modules: Dict[str, Module]) -> None:
    assert "s >= 1" in modules["C4"].formation_domain
    assert "s = 1" in modules["C6A"].formation_domain
    assert "s >= 1" in modules["C6B"].formation_domain
    assert "C6B" in modules["C7"].deps


def main() -> None:
    validate_schema(MODULES)
    order = topo_sort(MODULES)
    validate_forbidden_edges(MODULES)
    validate_unconditional_quarantine(MODULES)
    validate_key_separations(MODULES)
    validate_scope_coverage(MODULES)

    print("DSD dependency DAG audit: PASS")
    print("topological order:", " -> ".join(order))
    print("SAFE unconditional candidates:",
          ", ".join(name for name, m in MODULES.items()
                    if m.unconditional_candidate and m.status == SAFE))
    print("OPEN gates/escapes:",
          ", ".join(name for name, m in MODULES.items() if m.status == OPEN))
    print("QUARANTINED conditional modules:",
          ", ".join(name for name, m in MODULES.items() if m.status == CONDITIONAL))
    print("forbidden reverse-edge audit: PASS")
    print("conditional-leak audit: PASS")
    print("surplus scope audit: PASS (C6A s=1 != C6B all-s)")
    print("escape-ledger audit: PASS (E2S, E4C, E4L remain explicit)")
    print("NOTE: PASS certifies proof-graph hygiene only; it does not prove Collatz.")


if __name__ == "__main__":
    main()
