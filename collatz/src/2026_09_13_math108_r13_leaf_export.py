#!/usr/bin/env python3
"""MATH-108 executable gate A: exact r=13 negative-candidate AP exporter.

The source semantics are unchanged from MATH-065/MATH-071.  This exporter
removes the r=14 five-region scheduling assumption and emits the complete
r=13 negative-candidate AP stream as

    target0<TAB>odd_step<TAB>count

for every completed cylinder whose rigorous reduced-cost lower bound remains
negative.

This is an input certificate for the generalized AP-union engine.  It does
NOT close r=13, the first universal Farey cell, or Collatz.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m65", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

R = 13
EXPECTED_CLASS = (1035, 157, 483, 395)
EXPECTED_NODES = 15_364_524
EXPECTED_CYLINDERS = 1_959_535
EXPECTED_OCCURRENCES = 76_391_629_325
EXPECTED_MAX_MULTIPLICITY = 687_142_557


def main():
    total, safe, singleton, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton), len(critical)) == EXPECTED_CLASS

    nodes = 0
    cylinders = 0
    occurrences = 0
    max_multiplicity = 0
    out = sys.stdout

    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            for first, count, tres, mod, yres, coeff in leaves:
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                out.write(f"{target0}\t{coeff}\t{count}\n")
                cylinders += 1
                occurrences += count
                max_multiplicity = max(max_multiplicity, count)

    assert nodes == EXPECTED_NODES
    assert cylinders == EXPECTED_CYLINDERS
    assert occurrences == EXPECTED_OCCURRENCES
    assert max_multiplicity == EXPECTED_MAX_MULTIPLICITY

    print(
        "MATH-108 r13 export PASS",
        "cells", total, len(safe), len(singleton), len(critical),
        "nodes", nodes,
        "cylinders", cylinders,
        "occurrences", occurrences,
        "max_multiplicity", max_multiplicity,
        file=sys.stderr,
    )
    print("NO r=13 CLOSURE CLAIM", file=sys.stderr)


if __name__ == "__main__":
    main()
