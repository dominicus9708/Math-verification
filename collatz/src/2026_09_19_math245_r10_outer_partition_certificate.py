#!/usr/bin/env python3
"""MATH-245 exact outer-partition coverage certificate."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m206", HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py"
)
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

CHUNKS=16
EXPECTED_ROWS=95_536
EXPECTED_MASS=6_557_104_120_419

def main():
    rec=m206.build_frozen_factors()
    rec=[x for x in rec if (1<<x[0]) < 3**x[1]]
    assert len(rec)==EXPECTED_ROWS
    assert sum(x[4] for x in rec)==EXPECTED_MASS

    parts=[[] for _ in range(CHUNKS)]
    for i,row in enumerate(rec):
        parts[i%CHUNKS].append(row)

    assert sum(len(x) for x in parts)==EXPECTED_ROWS
    assert sum(sum(r[4] for r in x) for x in parts)==EXPECTED_MASS

    seen=set()
    for i,p in enumerate(parts):
        assert p
        for j,row in enumerate(rec):
            if j%CHUNKS==i:
                seen.add(j)
        print(
            "chunk",i,
            "rows",len(p),
            "mass",sum(r[4] for r in p),
            "max_m",max(r[4] for r in p),
        )
    assert len(seen)==EXPECTED_ROWS

    print("PASS MATH-245 exact 16-way outer coverage")
    print("rows",EXPECTED_ROWS)
    print("mass",EXPECTED_MASS)

if __name__=="__main__":
    main()
