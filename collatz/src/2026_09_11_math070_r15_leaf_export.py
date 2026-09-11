#!/usr/bin/env python3
"""MATH-070 stage A: exact r=15 negative-candidate AP export.

The output is a TSV stream

    target0<TAB>step<TAB>count

for every completed r=15 cylinder whose rigorous MATH-065 lower adjusted cost
is still negative. Closure is performed by the companion multiplicity-band
AP-union engine.

Finite exact arithmetic only. This file does not prove the first universal
cell or the Collatz conjecture.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math065", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

R = 15


def main():
    total, safe, singleton_cells, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton_cells), len(critical)) == (
        1061, 206, 542, 313
    )

    nodes = 0
    cylinders = 0
    occurrences = 0
    max_multiplicity = 0
    out = sys.stdout

    for group in (singleton_cells, critical):
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

    assert nodes == 35_343_449
    assert cylinders == 2_928_669
    assert occurrences == 1_835_780_279
    assert max_multiplicity == 14_315_470

    print(
        "MATH-070 export PASS",
        nodes, cylinders, occurrences, max_multiplicity,
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
