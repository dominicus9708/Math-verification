#!/usr/bin/env python3
"""MATH-201 exact audit of the 53 initial singleton one-paid cylinders.

Imports the canonical MATH-061 catalogue, isolates the macro-depth-1 source
cylinders with multiplicity one, and continues their exact ordinary targets to
B_pub=2^71.

Finite exact audit only. Collatz remains open.
"""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math061",
    HERE / "2026_09_11_math061_onepaid_cylinder_composition_certificate.py",
)
m61 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m61)

LO = 1 << 71


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descend(n: int, cap: int = 10_000):
    seen = set()
    for k in range(cap + 1):
        if n <= LO:
            return True, k, n
        if n in seen:
            return False, k, n
        seen.add(n)
        n = shortcut(n)
    return False, cap, n


def main():
    edges = m61.all_one_paid_cylinders()
    assert len(edges) == 910

    singleton = []
    for c in edges:
        p = m61.from_one_paid(c)
        if p.count == 1:
            singleton.append((c, p))

    assert len(singleton) == 53

    unique_targets = set()
    max_descent = 0
    failures = []
    by_L = Counter()

    for c, p in singleton:
        unique_targets.add(p.target_B)
        by_L[c.L] += 1

        ok, steps, end = descend(p.target_B)
        max_descent = max(max_descent, steps)

        if not ok:
            failures.append((c.L, p.target_B, steps, end))

    assert failures == []
    assert len(unique_targets) == 26
    assert max_descent == 25
    assert by_L == Counter({67: 16, 68: 9, 69: 20, 70: 4, 71: 4})

    print("one_paid_cylinders", len(edges))
    print("depth1_singletons", len(singleton))
    print("unique_targets", len(unique_targets))
    print("max_additional_descent", max_descent)
    print("by_L", dict(sorted(by_L.items())))
    print("PASS MATH-201 initial one-paid singleton audit")


if __name__ == "__main__":
    main()
