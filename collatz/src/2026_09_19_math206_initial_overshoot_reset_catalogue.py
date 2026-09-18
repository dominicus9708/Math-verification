#!/usr/bin/env python3
"""MATH-206 corrected r=10 full-boundary zero-carry audit.

The earlier draft audited zero-cost suffix factors.  Those suffixes are useful
address-language objects but are not the correct boundary-to-boundary factors
because an r=10 paid cluster lies between consecutive zero-cost prefixes.

This certificate extracts the entire zero-cost-prefix + first-return r=10
cluster as one exact affine factor from the unchanged MATH-065 generator and
audits zero-carry compatibility between the resulting frozen factors.

Finite exact audit only.  Global r=10 remains OPEN.
"""

from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m65", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

R = 10

EXPECTED_CELLS = (994, 91, 396, 507)
EXPECTED_NODES = 1_994_258
EXPECTED_LEAVES = 278_725
EXPECTED_MASS = 27_557_263_803_397
EXPECTED_MAX_M = 830_483_089_363
EXPECTED_TYPES = 258_242


def full_factor(cell, leaf):
    (
        L, start_R, E0, q0, lo, hi, tmin, tmax,
        eps, gs, hcl, H, margin,
    ) = cell
    first, count, tres, mod, yres, coeff = leaf

    assert mod == 1 << hcl
    assert H == L + hcl
    assert coeff == 3 ** (q0 + R)

    base_s = (first - tres) // mod
    B = yres + coeff * base_s
    A = start_R + (1 << L) * first
    Q = q0 + R

    # Exact family:
    # source = A + 2^H k
    # target = B + 3^Q k
    return (H, Q, A, B, count)


def build_frozen_factors():
    total, safe, singleton, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton), len(critical)) == EXPECTED_CELLS

    records = []
    nodes = 0

    for group in (singleton, critical):
        for cell in group:
            leaves, n = m65.negative_candidate_cylinders(cell, R)
            nodes += n
            for leaf in leaves:
                records.append(full_factor(cell, leaf))

    assert nodes == EXPECTED_NODES
    assert len(records) == EXPECTED_LEAVES
    assert sum(x[4] for x in records) == EXPECTED_MASS
    assert max(x[4] for x in records) == EXPECTED_MAX_M

    return records


def main():
    records = build_frozen_factors()

    type_counts = Counter((H, Q, A, B) for H, Q, A, B, count in records)
    factors = list(type_counts)

    assert len(factors) == EXPECTED_TYPES

    # Exact zero-to-zero reset requires B_e == A_f.
    source_anchors = {A for H, Q, A, B in factors}
    target_anchors = {B for H, Q, A, B in factors}
    exact_reset_anchor_intersection = source_anchors & target_anchors

    assert exact_reset_anchor_intersection == set()

    # Full zero-carry compatibility requires
    # B_e == A_f (mod 2^H_f).
    source_residue_by_H = defaultdict(set)
    H_values = set()

    for H, Q, A, B in factors:
        H_values.add(H)
        source_residue_by_H[H].add(A % (1 << H))

    # It is enough to show that for every next-factor H, no current target
    # residue occurs in the source-residue set at that H.
    compatible_residue_intersections = {}

    for H in sorted(H_values):
        mod = 1 << H
        target_residues = {B % mod for _, _, _, B in factors}
        hit = target_residues & source_residue_by_H[H]
        if hit:
            compatible_residue_intersections[H] = hit

    assert compatible_residue_intersections == {}

    print("PASS MATH-206 corrected full-boundary zero-carry audit")
    print("cells", EXPECTED_CELLS)
    print("branch_nodes", EXPECTED_NODES)
    print("leaf_records", len(records))
    print("occurrence_mass", sum(x[4] for x in records))
    print("max_multiplicity", max(x[4] for x in records))
    print("distinct_full_factor_types", len(factors))
    print("exact_zero_reset_anchor_intersection", 0)
    print("full_modulus_zero_carry_compatible_edges", 0)
    print("GLOBAL r=10 OPEN")


if __name__ == "__main__":
    main()
