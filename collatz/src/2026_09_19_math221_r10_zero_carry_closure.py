#!/usr/bin/env python3
"""MATH-221 exact r=10 zero-carry singleton closure certificate."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m58", HERE / "2026_09_11_paid_macro_transition_certificate.py"
)
m58 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

LO = 1 << 71
EXPECTED = {
    2923998483521551607675: (80, 1736361812508308967506),
    3684363727262161628267: (79, 1458593661034558542377),
}

def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def main():
    rows = m58.paid_exit_sources(72)
    assert len(rows) == 4

    anchors = set()
    for lo, hi, R, E0, q0 in rows:
        tmin, tmax = m58.lift_bounds(72, R, lo, hi)
        assert q0 == 46
        assert tmin == tmax == 0
        anchors.add(R)

    assert anchors == set(EXPECTED)

    for y in sorted(anchors):
        x = y
        steps = 0
        while x > LO:
            x = shortcut(x)
            steps += 1
            assert steps < 1000
        assert (steps, x) == EXPECTED[y], (y, steps, x, EXPECTED[y])

    print("PASS MATH-221 r10 zero-carry singleton closure")
    print("phase_rows", len(rows))
    print("unique_zero_carry_anchors", len(anchors))
    for y in sorted(anchors):
        print("anchor", y, "descent", EXPECTED[y][0],
              "floor_hit", EXPECTED[y][1])
    print("r10_zero_carry_branch CLOSED")
    print("FULL r10 LAYER OPEN")

if __name__ == "__main__":
    main()
