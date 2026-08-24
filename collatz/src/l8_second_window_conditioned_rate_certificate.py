from collections import defaultdict

# Exact conditioned-window calibration for the L=8 residue-maximal language.
# Candidate survivor counts are independently certified by
# l8_small_core_m23_m27_extension_certificate.cpp.
#
# This file recomputes the complete dyadic language counts at H=128,160,192
# from the exact L8 block rule, then evaluates the *conditional* overlap repair
# from H=128 to H=160.  It is finite evidence only, not an asymptotic theorem.

B = 8


def build_blocks():
    p3 = [1]
    for _ in range(B):
        p3.append(3 * p3[-1])

    maxima = [dict() for _ in range(B + 1)]
    for mask in range(1 << B):
        q = 0
        R = 0
        for i in range(B):
            if (mask >> i) & 1:
                R = 3 * R + (1 << i)
                q += 1
        key = R % p3[q]
        old = maxima[q].get(key)
        if old is None or R > old[0]:
            maxima[q][key] = (R, mask)

    expected = (1, 2, 6, 17, 34, 36, 22, 8, 1)
    assert tuple(len(x) for x in maxima) == expected

    blocks = []
    for q in range(B + 1):
        for _, mask in maxima[q].values():
            pref = [0]
            c = 0
            for i in range(B):
                c += (mask >> i) & 1
                pref.append(c)
            blocks.append((q, pref))
    return blocks


def qmins(H):
    out = [0] * (H + 1)
    p2 = 1
    p3 = 1
    q = 0
    for k in range(1, H + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


def language_count(H, blocks):
    assert H % B == 0
    qm = qmins(H)
    dp = {0: 1}
    for bi in range(H // B):
        off = bi * B
        nd = defaultdict(int)
        for q0, count in dp.items():
            for qb, pref in blocks:
                if all(q0 + pref[t] >= qm[off + t] for t in range(1, B + 1)):
                    nd[q0 + qb] += count
        dp = nd
    return sum(dp.values())


blocks = build_blocks()
L = {H: language_count(H, blocks) for H in (128, 160, 192)}

EXPECTED_LANGUAGE = {
    128: 21_743_857_700_147_672_762_453_009_957_952,
    160: 3_366_931_613_143_870_666_238_124_211_272_626_161_619,
    192: 538_739_847_013_238_234_058_807_333_725_091_128_756_700_219_273,
}
assert L == EXPECTED_LANGUAGE

# Independently certified candidate survivor counts from the companion C++ scan.
S = {
    23: {128: 2, 160: 0, 192: 0},
    24: {128: 2, 160: 0, 192: 0},
    25: {128: 11, 160: 0, 192: 0},
    26: {128: 23, 160: 2, 192: 0},
    27: {128: 26, 160: 1, 192: 0},
}

# For a nested finite candidate family, define
#
#   Xi_{H0->H1}
#     = (S_H1/S_H0) / ((L_H1/2^H1)/(L_H0/2^H0)).
#
# This is exactly the additional same-integer repair after conditioning on
# survival through H0.  The common forced N == 3 (mod 4) factor cancels.

def conditioned_ratio(m, H0=128, H1=160):
    s0, s1 = S[m][H0], S[m][H1]
    assert s0 > 0 and s1 > 0
    num = s1 * (1 << (H1 - H0)) * L[H0]
    den = s0 * L[H1]
    return num, den

# m=23,24,25 become empty in the second window.
for m in (23, 24, 25):
    assert S[m][128] > 0 and S[m][160] == 0

# m=26 and m=27 remain nonempty at H=160, so they give genuine conditioned
# second-window tests.  Prove the per-step repair exponent is < 1/25 exactly:
#
#   log2(Xi)/(160-128) < 1/25
# <=> Xi^25 < 2^32.
for m in (26, 27):
    num, den = conditioned_ratio(m)
    assert num > den  # positive repair exists, so the test is nontrivial
    assert num**25 < (1 << 32) * den**25
    # Therefore the observed conditioned repair rate is also < 7/50.
    assert 1 * 50 < 7 * 25
    print(f"m={m} conditioned_128_160_num={num}")
    print(f"m={m} conditioned_128_160_den={den}")
    print(f"m={m} conditioned repair exponent per step < 1/25 < 7/50 PASS")

# The m=27 case is much smaller: rate < 1/300 exactly.
num27, den27 = conditioned_ratio(27)
assert num27**75 < (1 << 8) * den27**75  # log2 Xi < 8/75 = 32/300

# Every tested surviving core is empty by H=192, so there is no third-window
# positive repair to audit in this finite sample.
for m in range(23, 28):
    assert S[m][192] == 0

print("L8 conditioned second-window repair-rate certificate: PASS")
