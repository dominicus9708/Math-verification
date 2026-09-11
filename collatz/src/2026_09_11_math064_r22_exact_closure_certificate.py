#!/usr/bin/env python3
"""
MATH-064 compatibility wrapper — superseded by MATH-065.

Audit correction (2026-09-11): the original MATH-064 program correctly
identified 752 phase/address cells whose completed parity cylinders are all
singletons, but then removed those cells from the symbolic graph without
continuing the singleton ordinary integers.  Its 18-target calculation covered
only the seven remaining multi-source-critical cells and therefore did not by
itself prove complete r=22 closure.

MATH-065 repairs the gap with a uniform exact dyadic branch-and-bound audit.
For r=22 the repaired result is:

  phase/address cells          1192
  cost-safe cells               433
  singleton-only cells          752
  multi-source critical cells     7
  negative-candidate cylinders  2184
  target occurrences            2188
  unique ordinary targets       1338
  maximum descent steps          123

Every target reaches <=2^71.  Hence r=22 closure survives, but the proof-facing
certificate is now MATH-065, not the historical MATH-064 implementation.

This wrapper intentionally delegates to the repaired certificate so that
running the historical filename can no longer emit the incomplete PASS result.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math065", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

EXPECTED_R22 = (
    1192, 433, 752, 7, 8485437, 2184, 2188, 1338, 123,
)


def main():
    result = m65.audit_layer(22, {})
    assert m65.summary_tuple(result) == EXPECTED_R22, result
    print("MATH-064 original certificate SUPERSEDED")
    print("repaired_r22", result)
    print("PASS MATH-064R via MATH-065 repaired singleton audit")


if __name__ == "__main__":
    main()
