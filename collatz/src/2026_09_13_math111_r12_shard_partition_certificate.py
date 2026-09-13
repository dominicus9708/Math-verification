#!/usr/bin/env python3
"""MATH-111 gate B: exact disjoint/exhaustive 128-shard partition certificate for r=12.

The source-record family is the exact stream emitted by the MATH-111 r=12
exporter.  Shard assignment is record_index mod 128.  This certificate proves
only that the implementation partition is disjoint and exhaustive and that its
additive occurrence mass is conserved.

No r=12 closure claim is made here.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location("exp", HERE / "2026_09_13_math111_r12_leaf_export.py")
exp = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(exp)

NSHARDS = 128
EXPECTED_CYLINDERS = 1_053_555
EXPECTED_OCCURRENCES = 580_472_268_528


def main():
    counts = [0] * NSHARDS
    masses = [0] * NSHARDS
    total_c = 0
    total_o = 0

    for i, (_target0, _coeff, count) in enumerate(exp.iter_records()):
        s = i % NSHARDS
        counts[s] += 1
        masses[s] += count
        total_c += 1
        total_o += count

    assert total_c == EXPECTED_CYLINDERS
    assert total_o == EXPECTED_OCCURRENCES
    assert sum(counts) == EXPECTED_CYLINDERS
    assert sum(masses) == EXPECTED_OCCURRENCES
    assert min(counts) > 0

    print("shard\tcylinders\toccurrences")
    for i, (c, o) in enumerate(zip(counts, masses)):
        print(i, c, o, sep="\t")
    print("TOTAL", total_c, total_o, sep="\t")
    print("PASS exact disjoint/exhaustive r12 128-shard source partition")
    print("NO r=12 CLOSURE CLAIM")


if __name__ == "__main__":
    main()
