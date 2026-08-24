from fractions import Fraction

# Exact rows from m45_depth28_uniform_transversality_tv_certificate.cpp
# (p, affine block b, raw selector mass, hard mass, TV numerator, hard cardinality A_p)
ROWS = [
    (2, 0, 8_796_093_022_208, 425_671_273_258, 352_117_077_839_970_304, 1_623_807),
    (2, 1, 8_796_093_022_208, 425_671_208_248, 352_101_617_299_881_984, 1_623_807),
    (5, 0, 1_099_511_627_776, 75_207_726_976, 5_502_289_305_403_392, 286_895),
    (5, 1, 1_099_511_103_504, 75_207_677_298, 5_501_887_494_144_160, 286_895),
    (8, 0, 137_438_953_481, 13_585_605_225, 85_957_936_677_836, 51_825),
    (8, 1, 137_438_887_938, 13_585_629_098, 86_055_322_907_416, 51_825),
    (10, 0, 34_359_739_317, 3_083_595_585, 5_369_573_154_106, 11_763),
    (10, 1, 34_359_721_961, 3_083_550_671, 5_366_750_776_560, 11_763),
]

# TV = tv_num / (2*raw*M_p), u_p=A_p/M_p, hence
# TV/u_p = tv_num/(2*raw*A_p).  This cancellation lets the improved
# hard-set-independent one-window repair bound be checked by pure integers.
for p, b, raw, hard, tv_num, A in ROWS:
    M = 1 << (27 - p)
    tv = Fraction(tv_num, 2 * raw * M)
    u = Fraction(A, M)
    xi_robust = 1 + tv / u
    xi_actual = Fraction(hard * M, raw * A)

    # Strengthen the repository's coarse 76/75 bound to 82/81 using the
    # actual p-dependent hard fractions rather than only u_p >= 3/64.
    assert 81 * tv_num < 2 * raw * A
    assert xi_robust < Fraction(82, 81)

    # Exact finite calibration: positive actual same-integer amplification is
    # below two parts per million in every listed state.
    assert xi_actual < Fraction(500_001, 500_000)

    print(
        f"p={p} b={b} "
        f"TV={float(tv):.12g} "
        f"u={float(u):.12g} "
        f"Xi_robust={float(xi_robust):.12g} "
        f"Xi_actual={float(xi_actual):.12g}"
    )

# 82^56 < 2*81^56 proves log2(82/81) < 1/56 bit exactly.
assert 82**56 < 2 * 81**56
# 57 cannot be claimed from this rational envelope.
assert not (82**57 < 2 * 81**57)

# Aggregate anti-bias in each affine block, recomputed exactly.
for b, expected_gap in [
    (0, Fraction(40_266_396_981, 524_288)),
    (1, Fraction(22_103_176_379, 131_072)),
]:
    hard_total = sum(hard for p, bb, raw, hard, tv_num, A in ROWS if bb == b)
    uniform_expected = sum(
        Fraction(raw * A, 1 << (27 - p))
        for p, bb, raw, hard, tv_num, A in ROWS
        if bb == b
    )
    gap = uniform_expected - hard_total
    assert gap == expected_gap
    assert gap > 0
    print(f"block={b} aggregate_anti_bias_gap={gap}")

print("m45 depth28 statewise transversality 1/56-bit certificate: PASS")
