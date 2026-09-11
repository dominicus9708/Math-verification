#!/usr/bin/env python3
"""
MATH-067 hybrid multiplicity reduction for the r=17 layer.

This certificate extends MATH-066.  Small target cylinders are cheaper to
materialize and continue with the MATH-065 memoized ordinary descent, while
very large cylinders are cheaper to propagate as exact arithmetic-progressions.

Certified bands:
  m = 1          : closed (MATH-066)
  2 <= m <= 4   : closed by ordinary continuation
  5 <= m <= 16  : closed by ordinary continuation
 17 <= m <= 32  : closed by ordinary continuation
 33 <= m <= 64  : closed by ordinary continuation
  m >= 1024     : closed by exact AP continuation (MATH-066)

The remaining r=17 range is exactly 65<=m<=1023.
This does not close r=17 or Collatz.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math066", HERE / "2026_09_11_math066_r17_ap_descent_certificate.py"
)
m66 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m66)
m65 = m66.m65

LO = 1 << 71

BANDS = {
    (2, 4): (341_488, 980_832, 283),
    (5, 16): (205_594, 1_865_597, 297),
    (17, 32): (74_170, 2_010_731, 283),
    (33, 64): (12_151, 462_694, 243),
}


def descent(n: int, cache: dict[int, int]):
    x = n
    path = []
    seen = set()
    while x > LO and x not in cache:
        if x in seen:
            return None
        seen.add(x)
        path.append(x)
        x = m65.shortcut(x)
        assert len(path) < 10000

    d = 0 if x <= LO else cache[x]
    for v in reversed(path):
        d += 1
        cache[v] = d
    return cache.get(n, 0)


def audit_band(lo_count: int, hi_count: int):
    _, _, singleton_cells, critical = m65.classify_cells(17)
    cache = {}
    cylinders = 0
    occurrences = 0
    max_descent = 0

    for group in (singleton_cells, critical):
        for cell in group:
            leaves, _ = m65.negative_candidate_cylinders(cell, 17)
            for first, count, tres, mod, yres, coeff in leaves:
                if not (lo_count <= count <= hi_count):
                    continue
                cylinders += 1
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                for k in range(count):
                    d = descent(target0 + coeff * k, cache)
                    assert d is not None
                    max_descent = max(max_descent, d)
                    occurrences += 1

    return cylinders, occurrences, max_descent


def main():
    for band, expected in BANDS.items():
        got = audit_band(*band)
        assert got == expected, (band, got, expected)
        print("closed_band", band, got)

    # MATH-066 exact counts.
    total_cylinders = 1_728_083
    total_occurrences = 38_457_239
    singleton_cylinders = 1_013_728
    singleton_occurrences = 1_013_728
    large_cylinders = 4_086
    large_occurrences = 17_143_582

    small_cylinders = singleton_cylinders + sum(v[0] for v in BANDS.values())
    small_occurrences = singleton_occurrences + sum(v[1] for v in BANDS.values())
    assert small_cylinders == 1_647_131
    assert small_occurrences == 6_333_582

    remaining_cylinders = total_cylinders - small_cylinders - large_cylinders
    remaining_occurrences = total_occurrences - small_occurrences - large_occurrences
    assert remaining_cylinders == 76_866
    assert remaining_occurrences == 14_980_075

    print("r17_small_m_le_64_closed_cylinders", small_cylinders)
    print("r17_small_m_le_64_closed_occurrences", small_occurrences)
    print("r17_large_m_ge_1024_closed_cylinders", large_cylinders)
    print("r17_large_m_ge_1024_closed_occurrences", large_occurrences)
    print("r17_remaining_cylinders", remaining_cylinders)
    print("r17_remaining_occurrences", remaining_occurrences)
    print("OPEN multiplicity range: 65..1023")
    print("PASS MATH-067 r=17 hybrid multiplicity reduction")


if __name__ == "__main__":
    main()
