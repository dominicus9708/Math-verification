#!/usr/bin/env python3
"""MATH-109 candidate support certificate: exact r=13 shard coverage.

This does NOT close r=13.  It verifies only that the deterministic 16-way
source-record partition used by the GitHub Actions closure gate is disjoint and
exhaustive over the exact MATH-107/MATH-108 r=13 source stream.

Partition rule:
    source record i belongs to shard i mod 16.

The full exact stream is regenerated from the unchanged MATH-065 classifier.
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
NSHARDS = 16
EXPECTED_CYLINDERS = 1_959_535
EXPECTED_OCCURRENCES = 76_391_629_325


def iter_source_records():
    total, safe, singleton, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton), len(critical)) == (1035, 157, 483, 395)
    for group in (singleton, critical):
        for cell in group:
            leaves, _ = m65.negative_candidate_cylinders(cell, R)
            for first, count, tres, mod, yres, coeff in leaves:
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                yield target0, coeff, count


def main():
    counts = [0] * NSHARDS
    occurrences = [0] * NSHARDS
    seen = 0
    total_occurrences = 0

    for i, (_, _, m) in enumerate(iter_source_records()):
        s = i % NSHARDS
        counts[s] += 1
        occurrences[s] += m
        seen += 1
        total_occurrences += m

    assert seen == EXPECTED_CYLINDERS, seen
    assert total_occurrences == EXPECTED_OCCURRENCES, total_occurrences
    assert sum(counts) == EXPECTED_CYLINDERS
    assert sum(occurrences) == EXPECTED_OCCURRENCES

    # Index modulo NSHARDS is a function, so each record has exactly one shard.
    # The congruence classes 0..NSHARDS-1 partition all nonnegative indices.
    print("shard\tcylinders\toccurrences")
    for s in range(NSHARDS):
        print(s, counts[s], occurrences[s], sep="\t")
    print("TOTAL", seen, total_occurrences, sep="\t")
    print("PASS exact disjoint/exhaustive r13 16-shard source partition")
    print("NO r13 CLOSURE CLAIM")


if __name__ == "__main__":
    main()
