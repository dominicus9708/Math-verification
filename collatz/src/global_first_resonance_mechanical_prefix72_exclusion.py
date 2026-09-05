#!/usr/bin/env python3
"""Exact 72-bit formation exclusion of the mechanical equality word.

At the first global resonance (A0,q0), the first-crossing mechanical word is
the unique maximum-correction word.  Every candidate start has N<2^72, so
its first 72 parity symbols determine N exactly.  This certificate verifies
the first 72 mechanical symbols using only integer power comparisons, computes
the corresponding canonical residue mod 2^72, and proves that residue lies
above the rigorous first-cell start ceiling (4/3)*2^71.
"""

A0 = 114_208_327_604
Q0 = 72_057_431_991
H = 72
B = 1 << 71

BITS = tuple(int(c) for c in
    "110110110101101101011011011010110110101101101101011011010110110110101101"
)


def main() -> None:
    assert len(BITS) == H

    # Verify that the hard-coded prefix is exactly the mechanical Beatty word
    # m_i = ceil(i*log_3(2)) - ceil((i-1)*log_3(2)).
    prev = 0
    for i in range(1, H + 1):
        k = prev + BITS[i - 1]
        # k-1 < i*log_3(2) < k, exactly equivalent to
        # 3^(k-1) < 2^i < 3^k.
        assert pow(3, k - 1) < (1 << i) < pow(3, k)
        prev = k

    assert prev == 46

    # Correction recurrence for the first 72 symbols.
    R = 0
    q = 0
    for i, bit in enumerate(BITS):
        if bit:
            R = 3 * R + (1 << i)
            q += 1

    mod = 1 << H
    residue = (-R * pow(pow(3, q), -1, mod)) % mod

    assert residue == 4_697_939_311_072_332_635_131
    assert residue < mod

    # First-resonance global start ceiling is N < (4/3)*2^71.
    assert 3 * residue > 4 * B

    # Check the parity prefix directly as an independent sanity test.
    x = residue
    got = []
    for _ in range(H):
        got.append(x & 1)
        x = (3 * x + 1) // 2 if x & 1 else x // 2
    assert tuple(got) == BITS

    print("PASS first-resonance mechanical prefix-72 exclusion")
    print(f"mechanical_prefix={''.join(map(str, BITS))}")
    print(f"odd_count_72={q}")
    print(f"canonical_residue_72={residue}")
    print(f"2^72={mod}")
    print("3*residue > 4*2^71, hence residue > (4/3)*2^71")
    print("exact maximum-correction mechanical equality branch is excluded")


if __name__ == "__main__":
    main()
