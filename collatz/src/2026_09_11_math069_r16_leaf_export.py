#!/usr/bin/env python3
"""MATH-069 stage A: exact r=16 negative-candidate AP export.

The output is a TSV stream

    target0<TAB>step<TAB>count

for every completed r=16 cylinder whose rigorous MATH-065 lower adjusted cost
is still negative.  This is only a representation export; closure is performed
by the companion hybrid-union engine.
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

R = 16


def main():
    total, safe, singleton_cells, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton_cells), len(critical)) == (
        1061, 229, 557, 275
    )

    nodes = 0
    cylinders = 0
    occurrences = 0
    bands = {
        "small": [0, 0],
        "medium": [0, 0],
        "large": [0, 0],
    }

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
                if count <= 64:
                    key = "small"
                elif count <= 1023:
                    key = "medium"
                else:
                    key = "large"
                bands[key][0] += 1
                bands[key][1] += count

    assert nodes == 37_173_746
    assert cylinders == 2_417_129
    assert occurrences == 213_006_896
    assert tuple(bands["small"]) == (2_238_071, 12_763_331)
    assert tuple(bands["medium"]) == (154_255, 39_692_496)
    assert tuple(bands["large"]) == (24_803, 160_551_069)

    print(
        "MATH-069 export PASS",
        nodes, cylinders, occurrences, bands,
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
