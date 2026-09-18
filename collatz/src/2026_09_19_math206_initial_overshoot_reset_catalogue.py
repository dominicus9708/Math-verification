#!/usr/bin/env python3
"""MATH-206 initial first-cell overshoot suffix catalogue certificate.

Exact finite audit only.  The catalogue consists of every suffix of length
z>=13 of every frozen MATH-058R legal initial zero-cost prefix.

This is not an arbitrary-depth factor catalogue and makes no r=10 closure claim.
"""

from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m58", HERE / "2026_09_11_paid_macro_transition_certificate.py"
)
m58 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

MIN_Z = 13
MOD13 = 1 << MIN_Z


def factor_from_bits(bits):
    z = len(bits)
    C, q = m58.correction_and_q(bits)
    mod = 1 << z
    A = (-C * pow(pow(3, q, mod), -1, mod)) % mod
    num = pow(3, q) * A + C
    assert num % mod == 0
    B = num // mod
    return (z, q, A, B)


def v2(n):
    if n == 0:
        return None
    n = abs(n)
    return (n & -n).bit_length() - 1


def build_catalogue():
    prefix_records = 0
    suffix_occurrences = 0
    factors = set()

    for L in range(1, 73):
        for lo, hi, R, E0, q0 in m58.paid_exit_sources(L):
            prefix_records += 1
            omega = (lo + hi) / 2
            bits = m58.mechanical_factor(L, omega)

            C, q = m58.correction_and_q(bits)
            assert q == q0
            assert m58.start_residue(bits) == R
            assert (pow(3, q) * R + C) >> L == E0

            for z in range(MIN_Z, L + 1):
                suffix_occurrences += 1
                factors.add(factor_from_bits(bits[L - z :]))

    return prefix_records, suffix_occurrences, sorted(factors)


def main():
    prefix_records, suffix_occurrences, factors = build_catalogue()

    assert prefix_records == 937
    assert suffix_occurrences == 32_508
    assert len(factors) == 924

    source_exact = defaultdict(list)
    source_mod13 = defaultdict(list)

    for f in factors:
        z, q, A, B = f
        source_exact[A].append(f)
        source_mod13[A % MOD13].append(f)

    exact_reset_edges = []
    low13_pairs = []
    compatible = []

    for e in factors:
        ze, qe, Ae, Be = e

        for f in source_exact.get(Be, ()):
            exact_reset_edges.append((e, f))

        for f in source_mod13[Be % MOD13]:
            low13_pairs.append((e, f))
            zf, qf, Af, Bf = f
            diff = Be - Af
            if diff % (1 << zf) == 0:
                d = diff // (1 << zf)
                compatible.append((e, f, d, v2(diff)))

    assert len(exact_reset_edges) == 0
    assert len(low13_pairs) == 388
    assert len(compatible) == 8

    expected_sources = {
        (32, 21, 1_922_017_147, 4_681_055_033),
        (33, 21, 3_844_034_294, 4_681_055_033),
        (34, 22, 2_562_689_529, 4_681_055_033),
        (35, 22, 5_125_379_058, 4_681_055_033),
    }
    f14 = (14, 9, 15_161, 18_218)
    f17 = (17, 11, 80_697, 109_070)

    got_sources = {e for e, f, d, vv in compatible}
    got_targets = {f for e, f, d, vv in compatible}

    assert got_sources == expected_sources
    assert got_targets == {f14, f17}

    for e, f, d, vv in compatible:
        if f == f14:
            assert d == 285_708
            assert vv == 16
        elif f == f17:
            assert d == 35_713
            assert vv == 17
        else:
            raise AssertionError(f)

    # Apply the MATH-205 carry recurrence one more time.
    second = []

    for e, f, d, vv in compatible:
        zf, qf, Af, Bf = f
        value = pow(3, qf) * d + Bf

        # Any r=10 danger continuation must first match at least 13 bits.
        for g in source_mod13.get(value % MOD13, ()):
            zg, qg, Ag, Bg = g
            diff = value - Ag
            if diff % (1 << zg) == 0:
                d2 = diff // (1 << zg)
                second.append((e, f, g, d, d2))

    assert second == []

    value14 = pow(3, 9) * 285_708 + 18_218
    value17 = pow(3, 11) * 35_713 + 109_070

    assert value14 == 5_623_608_782
    assert value14 % MOD13 == 5_582
    assert source_mod13.get(5_582, []) == []

    assert value17 == 6_326_559_881
    assert value17 % MOD13 == 1_161
    assert source_mod13.get(1_161, []) == []

    print("PASS MATH-206 initial overshoot suffix catalogue")
    print("prefix_records", prefix_records)
    print("suffix_occurrences", suffix_occurrences)
    print("unique_factors", len(factors))
    print("exact_zero_reset_edges", len(exact_reset_edges))
    print("low13_pairs", len(low13_pairs))
    print("full_compatible_zero_to_nonzero", len(compatible))
    print("second_r10_continuations", len(second))
    print("GLOBAL r=10 OPEN")


if __name__ == "__main__":
    main()
