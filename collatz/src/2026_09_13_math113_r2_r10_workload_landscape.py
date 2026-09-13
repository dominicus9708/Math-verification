#!/usr/bin/env python3
"""MATH-113 exact remaining-frontier workload landscape, r=2..10.

Reuses unchanged MATH-065 exact classifier and negative-candidate cylinder
generator.  The expected totals were obtained with an independently
reconstructed exact implementation that first reproduced the frozen MATH-110
r=12 totals exactly.

This certificate is a resource/representation audit.  It makes no closure
claim for r=2..10, the first universal Farey cell, or Collatz.
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

EXPECTED = {
    10: ((994, 91, 396, 507), 1_994_258, 278_725, 27_557_263_803_397, 830_483_089_363, 376),
     9: ((977, 72, 349, 556),   915_218, 141_002, 172_107_496_438_700, 3_381_256_733_001, 400),
     8: ((977, 60, 330, 587),   436_659, 65_811, 1_281_026_785_265_013, 67_269_130_238_384, 444),
     7: ((963, 42, 291, 630),   201_298, 29_342, 8_499_072_326_407_060, 807_229_562_860_607, 473),
     6: ((963, 34, 250, 679),    95_577, 15_133, 53_251_059_016_858_758, 3_228_918_251_442_427, 517),
     5: ((952, 20, 226, 706),    46_721, 6_525, 407_471_475_426_308_081, 51_662_692_023_078_828, 551),
     4: ((944, 14, 172, 758),    23_058, 3_675, 1_845_330_088_960_999_169, 227_070_381_217_324_903, 580),
     3: ((944, 9, 152, 783),     12_133, 1_873, 13_093_636_650_601_823_230, 1_816_563_049_738_599_228, 627),
     2: ((939, 3, 104, 832),      6_218, 1_116, 74_283_701_945_452_943_666, 21_350_398_233_904_928_148, 662),
}

U64_MAX = (1 << 64) - 1


def audit(r):
    total, safe, singleton, critical = m65.classify_cells(r)
    got_class = (total, len(safe), len(singleton), len(critical))
    nodes = cylinders = occurrences = max_m = 0
    mc = {}
    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, r)
            nodes += n
            cylinders += len(leaves)
            for leaf in leaves:
                m = leaf[1]
                occurrences += m
                max_m = max(max_m, m)
                mc[m] = mc.get(m, 0) + 1
    vals = sorted(mc)
    intervals = 0
    prev = None
    for m in vals:
        if prev is None or m != prev + 1:
            intervals += 1
        prev = m
    got = (got_class, nodes, cylinders, occurrences, max_m, intervals)
    assert got == EXPECTED[r], (r, got, EXPECTED[r])
    return got


def main():
    print("r\ttotal\tsafe\tsingleton\tcritical\tnodes\tcylinders\toccurrences\tmax_multiplicity\tintervals\tu64_engine_compatible")
    for r in range(10, 1, -1):
        cls, nodes, cylinders, occurrences, max_m, intervals = audit(r)
        u64_ok = occurrences <= U64_MAX and max_m <= U64_MAX
        print(r, *cls, nodes, cylinders, occurrences, max_m, intervals, int(u64_ok), sep="\t")
    assert EXPECTED[3][3] <= U64_MAX and EXPECTED[3][4] <= U64_MAX
    assert EXPECTED[2][3] > U64_MAX and EXPECTED[2][4] > U64_MAX
    print("PASS MATH-113 exact r2-r10 workload landscape")
    print("REPRESENTATION CEILING: current u64 AP engine is numerically compatible through r=3 but not r=2")
    print("NO r=2..10 CLOSURE CLAIM")
    print("FIRST UNIVERSAL FAREY CELL OPEN")
    print("COLLATZ OPEN")


if __name__ == "__main__":
    main()
