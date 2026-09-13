#!/usr/bin/env python3
"""MATH-111 executable gate A: exact r=12 negative-candidate AP exporter.

Source semantics are unchanged from MATH-065/MATH-110.  Emits the complete
r=12 negative-candidate AP stream as

    target0<TAB>odd_step<TAB>count

The exact MATH-110 totals are asserted.  This exporter alone does not close
r=12, the first universal Farey cell, or Collatz.
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

R = 12
EXPECTED_CLASS = (1013, 126, 457, 430)
EXPECTED_NODES = 8_278_602
EXPECTED_CYLINDERS = 1_053_555
EXPECTED_OCCURRENCES = 580_472_268_528
EXPECTED_MAX_MULTIPLICITY = 12_976_298_271


def iter_records():
    total, safe, singleton, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton), len(critical)) == EXPECTED_CLASS

    nodes = 0
    cylinders = 0
    occurrences = 0
    max_multiplicity = 0

    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            for first, count, tres, mod, yres, coeff in leaves:
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                cylinders += 1
                occurrences += count
                max_multiplicity = max(max_multiplicity, count)
                yield target0, coeff, count

    assert nodes == EXPECTED_NODES
    assert cylinders == EXPECTED_CYLINDERS
    assert occurrences == EXPECTED_OCCURRENCES
    assert max_multiplicity == EXPECTED_MAX_MULTIPLICITY


def main():
    out = sys.stdout
    cylinders = occurrences = max_multiplicity = 0
    for target0, coeff, count in iter_records():
        out.write(f"{target0}\t{coeff}\t{count}\n")
        cylinders += 1
        occurrences += count
        max_multiplicity = max(max_multiplicity, count)

    assert cylinders == EXPECTED_CYLINDERS
    assert occurrences == EXPECTED_OCCURRENCES
    assert max_multiplicity == EXPECTED_MAX_MULTIPLICITY
    print(
        "MATH-111 r12 export PASS",
        "cylinders", cylinders,
        "occurrences", occurrences,
        "max_multiplicity", max_multiplicity,
        file=sys.stderr,
    )
    print("NO r=12 CLOSURE CLAIM", file=sys.stderr)


if __name__ == "__main__":
    main()
