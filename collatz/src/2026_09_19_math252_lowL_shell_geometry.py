#!/usr/bin/env python3
"""MATH-252 static geometry of the entire remaining low-L paid-exit AP shell."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m249", HERE/"2026_09_19_math249_lowL_paid_exit_ap_export.py"
)
m249=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m249)

def main():
    total_rows=0
    total_mass=0
    peak_mass=(None,0)
    peak_count=(None,0)
    for L in range(13,53):
        rows=m249.rows_for_L(L)
        mass=sum(x[2] for x in rows)
        mx=max(x[2] for x in rows)
        assert mass<2**64
        assert mx<2**64
        total_rows+=len(rows)
        total_mass+=mass
        if mass>peak_mass[1]:
            peak_mass=(L,mass)
        if mx>peak_count[1]:
            peak_count=(L,mx)
        print("L",L,"rows",len(rows),"mass",mass,"max_m",mx)
    print("total_rows_counted_per_L",total_rows)
    print("total_mass_counted_per_L",total_mass)
    print("peak_mass_L_value",*peak_mass)
    print("peak_single_AP_L_value",*peak_count)
    print("PASS MATH-252 low-L shell geometry")
    print("NOTE masses are per-L support counts; do not sum as a disjoint theorem family without a separate overlap audit")

if __name__=="__main__":
    main()
