#!/usr/bin/env python3
"""Exact support audit of the remaining multi-paid paid-count frontier.

This script reuses the unchanged MATH-065 phase/address classifier.  It does
NOT claim closure of any r<=13 layer.  Its purpose is to reconcile the current
frontier after the historical exact closures r>=14 and the new one-paid
MATH-104--106 closures.

Regression gates:
- r=18 must reproduce MATH-065: 1121/302/621/198.
- r=14 must reproduce MATH-071 input classification: 1035/175/507/353.

Columns are:
    r, total phase/address cells, cost-safe cells,
    singleton-resolution cells, critical cells.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m65", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

REGRESSION = {
    18: (1121, 302, 621, 198),
    14: (1035, 175, 507, 353),
}

EXPECTED = {
    13: (1035, 157, 483, 395),
    12: (1013, 126, 457, 430),
    11: (1013, 119, 414, 480),
    10: (994, 91, 396, 507),
    9:  (977, 72, 349, 556),
    8:  (977, 60, 330, 587),
    7:  (963, 42, 291, 630),
    6:  (963, 34, 250, 679),
    5:  (952, 20, 226, 706),
    4:  (944, 14, 172, 758),
    3:  (944, 9, 152, 783),
    2:  (939, 3, 104, 832),
}


def counts(r: int):
    total, safe, singleton, critical = m65.classify_cells(r)
    return total, len(safe), len(singleton), len(critical)


def main():
    for r, expected in REGRESSION.items():
        got = counts(r)
        assert got == expected, ("regression", r, got, expected)
        print("REGRESSION", r, *got)

    print("r\ttotal\tcost_safe\tsingleton_resolution\tcritical")
    for r in range(13, 1, -1):
        got = counts(r)
        assert got == EXPECTED[r], (r, got, EXPECTED[r])
        print(r, *got, sep="\t")

    print("PASS support audit: exact MATH-065 classification frontier is r=2..13")
    print("NO CLOSURE CLAIM for r<=13")


if __name__ == "__main__":
    main()
