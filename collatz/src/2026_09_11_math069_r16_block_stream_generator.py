#!/usr/bin/env python3
"""MATH-069 exact r=16 cylinder audit and streaming handoff generator.

This script is the proof-facing Python half of MATH-069.  It imports the
MATH-065 exact dyadic branch-and-bound and the MATH-066 exact AP continuation.
It never treats singleton resolution as closure.

For r=16 it:
  * reconstructs every negative-candidate completed cylinder exactly;
  * closes every cylinder with multiplicity m>=1024 as an exact AP family;
  * sends m<=64 through one exact 8-step residue block;
  * sends 65<=m<=1023 through two exact 8-step residue blocks;
  * writes every still-unclosed singleton state as one unsigned 128-bit
    little-endian integer for the companion streaming verifier.

The companion C++ verifier is
  2026_09_11_math069_u128_stream_descent.cpp
and must close all emitted records before the r=16 layer is marked closed.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse

HERE = Path(__file__).resolve().parent
SPEC65 = spec_from_file_location(
    "math065", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC65)
assert SPEC65.loader is not None
SPEC65.loader.exec_module(m65)

SPEC66 = spec_from_file_location(
    "math066", HERE / "2026_09_11_math066_r17_ap_descent_certificate.py"
)
m66 = module_from_spec(SPEC66)
assert SPEC66.loader is not None
SPEC66.loader.exec_module(m66)

LO = 1 << 71
R = 16
BLOCK_BITS = 8
BLOCK_MOD = 1 << BLOCK_BITS


def block_table():
    out = []
    for residue in range(BLOCK_MOD):
        x = residue
        A = 1
        C = 0
        for t in range(BLOCK_BITS):
            if x & 1:
                A *= 3
                C = 3 * C + (1 << t)
                x = (3 * x + 1) // 2
            else:
                x //= 2
        out.append((A, C))
    return out


BLOCK = block_table()


def block_split(a: int, b: int, count: int):
    """Exact T^8 images of an odd-step arithmetic progression."""
    for k0 in range(min(count, BLOCK_MOD)):
        c = (count - 1 - k0) // BLOCK_MOD + 1
        n0 = a + b * k0
        A, C = BLOCK[n0 & (BLOCK_MOD - 1)]
        yield (A * n0 + C) // BLOCK_MOD, A * b, c


def trim_floor(a: int, b: int, count: int):
    """Remove exactly the initial AP segment already at or below 2^71."""
    if count <= 0 or a > LO:
        return a, b, count, 0
    drop = min(count, max(0, (LO - a) // b + 1))
    return a + b * drop, b, count - drop, drop


def ap_band(count: int):
    if count >= 65_536:
        return ">=65536"
    if count >= 16_384:
        return "16384..65535"
    if count >= 4_096:
        return "4096..16383"
    return "1024..4095"


EXPECTED_AP = {
    ">=65536": (454, 52_065_578, 66_651_246, 335),
    "16384..65535": (1_197, 31_243_267, 48_270_079, 316),
    "4096..16383": (4_200, 37_228_529, 68_451_866, 348),
    "1024..4095": (18_952, 40_013_695, 88_717_314, 307),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tail-file",
        type=Path,
        default=Path("math069_r16_tail_u128.bin"),
        help="generated binary stream for the companion verifier",
    )
    args = parser.parse_args()

    total, safe, singleton, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton), len(critical)) == (1061, 229, 557, 275)

    stats = Counter()
    ap_stats = {k: Counter() for k in EXPECTED_AP}
    max_after_first_medium = 0

    with args.tail_file.open("wb", buffering=4 * 1024 * 1024) as fout:
        for group in (singleton, critical):
            for cell in group:
                cyls, branch_nodes = m65.negative_candidate_cylinders(cell, R)
                stats["branch_nodes"] += branch_nodes

                for first, count, tres, mod, yres, coeff in cyls:
                    stats["cylinders"] += 1
                    stats["occurrences"] += count
                    base_s = (first - tres) // mod
                    a = yres + coeff * base_s
                    b = coeff

                    if count >= 1024:
                        key = ap_band(count)
                        ok, depth, nodes, _live = m66.ap_descent(a, b, count)
                        assert ok
                        s = ap_stats[key]
                        s["cylinders"] += 1
                        s["occurrences"] += count
                        s["nodes"] += nodes
                        s["max_depth"] = max(s["max_depth"], depth)
                        stats["large_cylinders"] += 1
                        stats["large_occurrences"] += count
                        continue

                    if count <= 64:
                        stats["small_cylinders"] += 1
                        stats["small_occurrences"] += count
                        for a1, b1, c1 in block_split(a, b, count):
                            a1, b1, c1, drop = trim_floor(a1, b1, c1)
                            stats["small_closed_8"] += drop
                            if c1:
                                assert c1 == 1
                                stats["small_tail"] += 1
                                fout.write(a1.to_bytes(16, "little"))
                        continue

                    stats["medium_cylinders"] += 1
                    stats["medium_occurrences"] += count
                    for a1, b1, c1 in block_split(a, b, count):
                        a1, b1, c1, drop1 = trim_floor(a1, b1, c1)
                        stats["medium_closed_8"] += drop1
                        if not c1:
                            continue
                        max_after_first_medium = max(max_after_first_medium, c1)
                        assert c1 <= 4

                        for a2, b2, c2 in block_split(a1, b1, c1):
                            a2, b2, c2, drop2 = trim_floor(a2, b2, c2)
                            stats["medium_closed_16"] += drop2
                            if c2:
                                assert c2 == 1
                                stats["medium_tail"] += 1
                                fout.write(a2.to_bytes(16, "little"))

    assert stats["branch_nodes"] == 37_173_746
    assert stats["cylinders"] == 2_417_129
    assert stats["occurrences"] == 213_006_896

    assert stats["large_cylinders"] == 24_803
    assert stats["large_occurrences"] == 160_551_069
    for key, expected in EXPECTED_AP.items():
        got = ap_stats[key]
        assert (
            got["cylinders"], got["occurrences"], got["nodes"], got["max_depth"]
        ) == expected, (key, got, expected)

    assert stats["small_cylinders"] == 2_238_071
    assert stats["small_occurrences"] == 12_763_331
    assert stats["small_closed_8"] == 8_125_293
    assert stats["small_tail"] == 4_638_038

    assert stats["medium_cylinders"] == 154_255
    assert stats["medium_occurrences"] == 39_692_496
    assert stats["medium_closed_8"] == 25_273_451
    assert max_after_first_medium == 4
    assert stats["medium_closed_16"] == 7_290_855
    assert stats["medium_tail"] == 7_128_190

    tail_records = stats["small_tail"] + stats["medium_tail"]
    assert tail_records == 11_766_228
    assert args.tail_file.stat().st_size == 16 * tail_records

    print("r16_cells", total, len(safe), len(singleton), len(critical))
    print("r16_branch_nodes", stats["branch_nodes"])
    print("r16_negative_cylinders", stats["cylinders"])
    print("r16_target_occurrences", stats["occurrences"])
    print("r16_large_AP_closed", stats["large_cylinders"], stats["large_occurrences"])
    print("r16_small_after8_tail", stats["small_tail"])
    print("r16_medium_after16_tail", stats["medium_tail"])
    print("r16_stream_tail_records", tail_records)
    print("NEXT run the MATH-069 u128 streaming verifier on", args.tail_file)


if __name__ == "__main__":
    main()
