#!/usr/bin/env python3
"""Exact first valuation-jump pure-ballot pruning on the retained 14 roots.

Input is the already SAFE-pruned exact 14-root affine forest.  Each root has

    X = r + 2^h m,
    Y = T^h(X) = y + 3^q m,

with a finite exact m interval.

Every retained first-defect root has incoming pure-ballot surplus S=1.
Partition the parameter interval by

    a = v2(Y),

using the exact affine valuation cylinder

    m == (2^a-y) (3^q)^(-1) mod 2^(a+1).

The complete next parity block is then forced to be 0^a1.  Apply the exact
jump-ballot criterion to that whole block.  Branches failing it are rigorous
necessary-condition rejections; no endpoint, H/L, C4F, or probabilistic
assumption is used.
"""

import A0_s1_14root_long_membership_forest_certificate as forest
import A0_s1_valuation_jump_ballot_control_certificate as ballot


def count_residue(lo: int, hi: int, rho: int, modulus: int) -> int:
    if hi < lo:
        return 0
    first = lo + ((rho - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


def valuation_partition(root):
    y = root["y"]
    A = 3 ** root["q"]
    lo = root["m_lo"]
    hi = root["m_hi"]
    total = root["count"]
    assert A & 1
    assert y + A * lo > 0

    out = {}
    recovered = 0
    maxY = y + A * hi
    for a in range(maxY.bit_length()):
        M = 1 << (a + 1)
        rho = (((1 << a) - y) * pow(A, -1, M)) % M
        c = count_residue(lo, hi, rho, M)
        if c:
            out[a] = c
            recovered += c
    assert recovered == total
    return out


EXPECTED = {
    # f: (allowed valuations, surviving count)
    2:  ((0, 1),    81_918_166_956_707_613_549),
    5:  ((0, 1),    10_239_770_869_590_357_244),
    8:  ((0, 1, 2), 1_493_299_918_482_174_113),
    10: ((0, 1),       319_992_839_674_610_443),
    13: ((0, 1),        39_999_104_959_334_148),
    16: ((0, 1, 2),      5_833_202_806_570_579),
    18: ((0, 1),          1_249_972_029_978_830),
    21: ((0, 1),            156_246_503_747_386),
    24: ((0, 1),             19_530_812_968_427),
    27: ((0, 1, 2),           2_848_243_557_896),
    29: ((0, 1),                 610_337_905_263),
    32: ((0, 1),                  76_292_238_158),
    35: ((0, 1, 2),               11_125_951_399),
    37: ((0, 1),                    2_384_132_443),
}

rows = []
total_before = 0
total_after = 0

for root in forest.roots:
    f = root["f"]
    h = root["h"]
    q = root["q"]
    S = q - ballot.Q[h]
    assert S == 1

    parts = valuation_partition(root)
    surviving = {}
    for a, count in parts.items():
        ok, _S2 = ballot.jump_ballot(h, S, a)
        if ok:
            surviving[a] = count

    allowed = tuple(surviving)
    after = sum(surviving.values())
    assert (allowed, after) == EXPECTED[f]

    before = root["count"]
    assert after <= before
    total_before += before
    total_after += after
    rows.append((f, h, before, allowed, after, before - after))

assert total_before == 125_072_439_875_999_947_649
assert total_after == 94_018_492_189_951_139_878
assert total_before - total_after == 31_053_947_686_048_807_771

print("PASS A0 s=1 14-root first valuation-ballot pruning certificate")
print("root_count", len(rows))
for f, h, before, allowed, after, pruned in rows:
    print("root", f, "depth", h,
          "before", before,
          "allowed_next_v2", allowed,
          "after", after,
          "pruned", pruned)
print("total_before", total_before)
print("total_after", total_after)
print("additional_pruned", total_before - total_after)
print("pruned_fraction", f"{(total_before-total_after)/total_before:.12f}")
print("endpoint_used", False)
print("status", "SAFE exact pure-ballot pruning after existing 14-root SAFE inputs")
