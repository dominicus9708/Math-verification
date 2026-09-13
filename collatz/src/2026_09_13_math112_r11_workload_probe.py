#!/usr/bin/env python3
"""MATH-112 preliminary exact r=11 workload probe.

Reuses the unchanged MATH-065 exact classifier and negative-candidate cylinder
generator. No guessed workload constants are used beyond the already-audited
classifier inventory. This probe determines the exact finite source-stream
size and multiplicity structure for the next multi-paid layer.

No r=11 closure claim. First universal Farey cell and Collatz remain OPEN.
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

R = 11
EXPECTED_CLASS = (1013, 119, 414, 480)
THRESHOLDS = (1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000,
              1_000_000_000, 10_000_000_000, 100_000_000_000)


def main():
    total, safe, singleton, critical = m65.classify_cells(R)
    got_class = (total, len(safe), len(singleton), len(critical))
    assert got_class == EXPECTED_CLASS, (got_class, EXPECTED_CLASS)

    nodes = cylinders = occurrences = max_multiplicity = 0
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

    print("MATH-112 preliminary exact r=11 workload probe PASS")
    print("class", *got_class)
    print("branch_nodes", nodes)
    print("negative_ap_cylinders", cylinders)
    print("represented_occurrences", occurrences)
    print("max_multiplicity", max_multiplicity)
    print("occupied_multiplicity_intervals", intervals)
    for threshold in THRESHOLDS:
        c = o = 0
        for m, freq in multiplicity_counts.items():
            if m >= threshold:
                c += freq
                o += m * freq
        print("threshold", threshold, c, o)
    print("NO r=11 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
