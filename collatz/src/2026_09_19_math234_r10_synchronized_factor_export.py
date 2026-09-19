#!/usr/bin/env python3
"""MATH-234 synchronized frozen r=10 full-factor exporter.

Emits exact rows:
    H<TAB>Q<TAB>A<TAB>B<TAB>M
for every MATH-206 frozen negative-candidate full boundary factor.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location("m206",HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py")
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

def main():
    rec=m206.build_frozen_factors()
    assert len(rec)==278725
    assert sum(x[4] for x in rec)==27_557_263_803_397
    assert max(x[4] for x in rec)==830_483_089_363
    for row in rec:
        print(*row,sep="\t")
    print("MATH-234 synchronized exporter PASS",file=sys.stderr)

if __name__=="__main__":
    main()
