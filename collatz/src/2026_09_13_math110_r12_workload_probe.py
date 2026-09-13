#!/usr/bin/env python3
"""MATH-110 preliminary exact r=12 workload probe.

This script reuses the unchanged MATH-065 classifier and exact
negative-candidate cylinder generator.  It does not contain guessed workload
constants.  Its purpose is to obtain the exact r=12 source-stream totals that
will be frozen into the subsequent reproducibility certificate.

Finite exact arithmetic only.  No r=12 closure claim.
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

R = 12
EXPECTED_CLASS = (1013, 126, 457, 430)
THRESHOLDS = (1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000)


def main():
    total, safe, singleton, critical = m65.classify_cells(R)
    got_class = (total, len(safe), len(singleton), len(critical))
    assert got_class == EXPECTED_CLASS, (got_class, EXPECTED_CLASS)

    nodes = 0
    cylinders = 0
    occurrences = 0
    max_multiplicity = 0
    multiplicity_counts = {}

    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            cylinders += len(leaves)
            for leaf in leaves:
                count = leaf[1]
                occurrences += count
                max_multiplicity = max(max_multiplicity, count)
                multiplicity_counts[count] = multiplicity_counts.get(count, 0) + 1

    vals = sorted(multiplicity_counts)
    intervals = 0
    prev = None
    for m in vals:
        if prev is None or m != prev + 1:
            intervals += 1
        prev = m

    print("MATH-110 preliminary exact r=12 workload probe PASS")
    print("class", *got_class)
    print("branch_nodes", nodes)
    print("negative_ap_cylinders", cylinders)
    print("represented_occurrences", occurrences)
    print("max_multiplicity", max_multiplicity)
    print("occupied_multiplicity_intervals", intervals)
    for threshold in THRESHOLDS:
        c = 0
        o = 0
        for m, freq in multiplicity_counts.items():
            if m >= threshold:
                c += freq
                o += m * freq
        print("threshold", threshold, c, o)
    print("NO r=12 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
