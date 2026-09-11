#!/usr/bin/env python3
"""MATH-071 stage A: exact r=14 negative-candidate AP exporter.

Emits one TSV row

    target0<TAB>odd_step<TAB>count

for every completed r=14 cylinder whose rigorous MATH-065 reduced-cost lower
bound is still negative.

This stage also certifies the exact workload and the five occupied initial
multiplicity regions used by MATH-071.  Empty multiplicity gaps are checked
from the actual cylinder stream; they are not assumptions.

Finite exact arithmetic only.  This does not prove the first universal Farey
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

R = 14

REGIONS = (
    (1, 767_077, 2_598_422, 5_455_767_618),
    (1_526_617, 2_385_912, 856, 1_673_761_049),
    (4_579_851, 7_157_735, 344, 1_968_444_716),
    (13_739_556, 16_283_918, 20, 311_052_788),
    (17_155_074, 171_785_639, 50, 1_282_910_907),
)


def region_index(m: int):
    hits = [i for i, (lo, hi, _, _) in enumerate(REGIONS) if lo <= m <= hi]
    assert len(hits) == 1, (m, hits)
    return hits[0]


def main():
    total, safe, singleton_cells, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton_cells), len(critical)) == (
        1_035, 175, 507, 353
    )

    nodes = cylinders = occurrences = max_multiplicity = 0
    rc = [0] * len(REGIONS)
    ro = [0] * len(REGIONS)

    out = sys.stdout
    for group in (singleton_cells, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            for first, count, tres, mod, yres, coeff in leaves:
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                i = region_index(count)
                rc[i] += 1
                ro[i] += count
                cylinders += 1
                occurrences += count
                max_multiplicity = max(max_multiplicity, count)
                out.write(f"{target0}\t{coeff}\t{count}\n")

    assert nodes == 24_614_018
    assert cylinders == 2_599_692
    assert occurrences == 10_691_937_078
    assert max_multiplicity == 171_785_639

    for i, (_, _, expected_c, expected_o) in enumerate(REGIONS):
        assert (rc[i], ro[i]) == (expected_c, expected_o), (i, rc[i], ro[i])

    assert sum(rc) == cylinders
    assert sum(ro) == occurrences

    print(
        "MATH-071 export PASS",
        "cells", total, len(safe), len(singleton_cells), len(critical),
        "nodes", nodes,
        "cylinders", cylinders,
        "occurrences", occurrences,
        "max_multiplicity", max_multiplicity,
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
