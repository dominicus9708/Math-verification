#!/usr/bin/env python3
"""MATH-110 exact r=12 workload and representation audit.

This certificate reuses the unchanged MATH-065 exact phase/address classifier
and negative-candidate cylinder generator.  All totals below were first
obtained by the preliminary exact probe and are frozen here as assertions.

This is a finite workload/representation certificate only.  It does not close
r=12, the first universal Farey cell, or Collatz.
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
EXPECTED_NODES = 8_278_602
EXPECTED_CYLINDERS = 1_053_555
EXPECTED_OCCURRENCES = 580_472_268_528
EXPECTED_MAX_MULTIPLICITY = 12_976_298_271
EXPECTED_INTERVALS = 305
EXPECTED_THRESHOLDS = {
    1_000: (271_732, 580_373_566_138),
    10_000: (145_303, 579_804_318_984),
    100_000: (65_979, 576_712_999_139),
    1_000_000: (24_175, 562_035_216_524),
    10_000_000: (6_347, 507_000_843_603),
    100_000_000: (1_118, 368_990_167_363),
    1_000_000_000: (75, 141_078_443_336),
}


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

    assert nodes == EXPECTED_NODES
    assert cylinders == EXPECTED_CYLINDERS
    assert occurrences == EXPECTED_OCCURRENCES
    assert max_multiplicity == EXPECTED_MAX_MULTIPLICITY
    assert intervals == EXPECTED_INTERVALS

    threshold_results = {}
    for threshold in EXPECTED_THRESHOLDS:
        c = o = 0
        for m, freq in multiplicity_counts.items():
            if m >= threshold:
                c += freq
                o += m * freq
        threshold_results[threshold] = (c, o)
        assert threshold_results[threshold] == EXPECTED_THRESHOLDS[threshold]

    print("MATH-110 exact r=12 workload audit PASS")
    print("class", *got_class)
    print("branch_nodes", nodes)
    print("negative_ap_cylinders", cylinders)
    print("represented_occurrences", occurrences)
    print("max_multiplicity", max_multiplicity)
    print("occupied_multiplicity_intervals", intervals)
    for threshold in sorted(threshold_results):
        print("threshold", threshold, *threshold_results[threshold])
    print("NO r=12 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
