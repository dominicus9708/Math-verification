#!/usr/bin/env python3
"""MATH-234/235 synchronized frozen r=10 full-factor exporter.

Default emits the exact MATH-235 coefficient-expanding survivor set:
    2^H < 3^Q.
Use --all to emit every MATH-206 negative-candidate factor.

Rows:
    H<TAB>Q<TAB>A<TAB>B<TAB>M
"""
import argparse
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location("m206",HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py")
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--all",action="store_true")
    args=ap.parse_args()

    rec=m206.build_frozen_factors()
    assert len(rec)==278_725
    assert sum(x[4] for x in rec)==27_557_263_803_397

    if not args.all:
        rec=[x for x in rec if (1<<x[0]) < 3**x[1]]
        assert len(rec)==95_536
        assert sum(x[4] for x in rec)==6_557_104_120_419
        assert max(x[4] for x in rec)==166_975_641_136

    for row in rec:
        print(*row,sep="\t")

    print(
        f"MATH-234 synchronized exporter PASS rows={len(rec)} "
        f"mass={sum(x[4] for x in rec)} mode={'all' if args.all else 'post-J'}",
        file=sys.stderr,
    )

if __name__=="__main__":
    main()
