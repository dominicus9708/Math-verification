#!/usr/bin/env python3
"""MATH-112 exact r=11 workload and representation audit.

Reuses the unchanged MATH-065 exact classifier and negative-candidate cylinder
generator.  Totals were independently cross-checked by reconstructing the same
exact arithmetic and first reproducing all frozen MATH-110 r=12 totals.

Finite workload/representation certificate only.  No r=11 closure claim.
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
EXPECTED_NODES = 3_994_436
EXPECTED_CYLINDERS = 605_972
EXPECTED_OCCURRENCES = 3_419_719_061_560
EXPECTED_MAX_MULTIPLICITY = 51_905_193_085
EXPECTED_INTERVALS = 343
EXPECTED_THRESHOLDS = {
    1_000: (241_328, 3_419_677_356_627),
    10_000: (149_504, 3_419_293_778_624),
    100_000: (77_418, 3_416_001_689_360),
    1_000_000: (36_170, 3_397_436_981_913),
    10_000_000: (13_697, 3_307_517_564_955),
    100_000_000: (3_789, 2_970_493_671_360),
    1_000_000_000: (564, 2_001_769_706_501),
    10_000_000_000: (28, 574_823_013_486),
    100_000_000_000: (0, 0),
}


def main():
    total, safe, singleton, critical = m65.classify_cells(R)
    got_class = (total, len(safe), len(singleton), len(critical))
    assert got_class == EXPECTED_CLASS, (got_class, EXPECTED_CLASS)

    nodes = cylinders = occurrences = max_multiplicity = 0
    multiplicity_counts = {}
    ordered_counts = []

    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            cylinders += len(leaves)
            for leaf in leaves:
                count = leaf[1]
                ordered_counts.append(count)
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

    for threshold, expected in EXPECTED_THRESHOLDS.items():
        c = o = 0
        for m, freq in multiplicity_counts.items():
            if m >= threshold:
                c += freq
                o += m * freq
        assert (c, o) == expected, (threshold, (c, o), expected)

    nshards = 256
    shard_counts = [0] * nshards
    shard_mass = [0] * nshards
    for i, count in enumerate(ordered_counts):
        s = i % nshards
        shard_counts[s] += 1
        shard_mass[s] += count
    assert sum(shard_counts) == EXPECTED_CYLINDERS
    assert sum(shard_mass) == EXPECTED_OCCURRENCES
    assert min(shard_counts) == 2367
    assert max(shard_counts) == 2368
    assert max(shard_mass) == 61_047_101_694

    print("MATH-112 exact r=11 workload audit PASS")
    print("class", *got_class)
    print("branch_nodes", nodes)
    print("negative_ap_cylinders", cylinders)
    print("represented_occurrences", occurrences)
    print("max_multiplicity", max_multiplicity)
    print("occupied_multiplicity_intervals", intervals)
    for threshold in sorted(EXPECTED_THRESHOLDS):
        print("threshold", threshold, *EXPECTED_THRESHOLDS[threshold])
    print("proposed_256_shards", min(shard_counts), max(shard_counts), max(shard_mass))
    print("NO r=11 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
