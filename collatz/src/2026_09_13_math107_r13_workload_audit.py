#!/usr/bin/env python3
"""MATH-107 exact r=13 workload and representation audit.

This audit reuses the unchanged MATH-065 exact phase/address classifier and
negative-candidate cylinder generator.  It characterizes the next open
multi-paid layer r=13 after the exact r>=14 closure.

It is deliberately NOT a closure certificate.  Its role is to determine
whether the MATH-071 r=14 AP-union representation can be reused without a new
representation audit.

Finite exact arithmetic only.  The first universal Farey cell and Collatz
conjecture remain OPEN.
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

R = 13
EXPECTED_CLASS = (1035, 157, 483, 395)
EXPECTED_NODES = 15_364_524
EXPECTED_CYLINDERS = 1_959_535
EXPECTED_OCCURRENCES = 76_391_629_325
EXPECTED_MAX_MULTIPLICITY = 687_142_557
EXPECTED_INTERVALS = 276
EXPECTED_THRESHOLDS = {
    1_000: (305_062, 76_263_230_955),
    10_000: (123_925, 75_633_800_228),
    100_000: (36_955, 72_481_494_807),
    1_000_000: (8_414, 62_567_007_204),
    10_000_000: (1_130, 41_355_402_672),
    100_000_000: (65, 14_620_369_241),
}


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

    assert nodes == EXPECTED_NODES, nodes
    assert cylinders == EXPECTED_CYLINDERS, cylinders
    assert occurrences == EXPECTED_OCCURRENCES, occurrences
    assert max_multiplicity == EXPECTED_MAX_MULTIPLICITY, max_multiplicity
    assert intervals == EXPECTED_INTERVALS, intervals

    threshold_results = {}
    for threshold in EXPECTED_THRESHOLDS:
        c = 0
        o = 0
        for m, freq in multiplicity_counts.items():
            if m >= threshold:
                c += freq
                o += m * freq
        threshold_results[threshold] = (c, o)
        assert threshold_results[threshold] == EXPECTED_THRESHOLDS[threshold], (
            threshold, threshold_results[threshold], EXPECTED_THRESHOLDS[threshold]
        )

    print("MATH-107 exact r=13 workload audit PASS")
    print("class", *got_class)
    print("branch_nodes", nodes)
    print("negative_ap_cylinders", cylinders)
    print("represented_occurrences", occurrences)
    print("max_multiplicity", max_multiplicity)
    print("occupied_multiplicity_intervals", intervals)
    for threshold in sorted(threshold_results):
        print("threshold", threshold, *threshold_results[threshold])
    print("NO r=13 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
