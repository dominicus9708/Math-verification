#!/usr/bin/env python3
"""Exact scaled-root defect reduction for different-q E=13 pullbacks.

Actual pre-gate path:
    E=13, Q=1526.
Alternate path:
    E'=13-s, Q'=Q+s, 1<=s<=7.

Put U=x+1 and let d>0 be the G13 entrance displacement.  Subtracting the two
1539-step affine equations gives

    3^Q M = 2^T d + C(P') - C(P),
    M := U_N - 3^s U_N'.

The actual E=13 formation filter gives epsilon_actual=C(P)/3^Q<114.
For the alternate path, ordered even positions satisfy p'_j>=j, hence

    epsilon_alt = C(P')/3^(Q+s) <= 2^(13-s)-1.

Since every transition-parent credit obeys d<=6859 and

    2^T*6859 < 3^Q,

the coefficient 2^T d / 3^Q is strictly below one.  Therefore the integer M
satisfies

    -113 <= M <= 3^s(2^(13-s)-1).

Moreover M == U_N (mod 3^s).  For the current m=44 core,

    U_N = N+1
        = 4(3^44 + 1 + sum a_i 3^i),  a_i in {0,1},

so for s<=7

    M == 4(1 + sum_{i=0}^{s-1} a_i 3^i) (mod 3^s).

The 2^s admissible residues are distinct, so any compatible M determines the
low s ternary selector bits uniquely.  This converts a different-q ordinary
predecessor relation into a small integer defect plus a finite low-ternary
address.
"""

T = 1539
Q = 1526
MAX_PARENT_CREDIT = 6859


def core_residue_map(s: int):
    modulus = 3**s
    out = {}
    for mask in range(1 << s):
        z = 1
        for i in range(s):
            if (mask >> i) & 1:
                z += 3**i
        residue = (4 * z) % modulus
        assert residue not in out
        out[residue] = mask
    return out


def possible_M_values(s: int):
    upper = 3**s * (2**(13-s) - 1)
    allowed = core_residue_map(s)
    return [m for m in range(-113, upper + 1) if m % (3**s) in allowed]


def main():
    assert (1 << T) * MAX_PARENT_CREDIT < 3**Q

    expected_upper = {
        1: 12_285,
        2: 18_423,
        3: 27_621,
        4: 41_391,
        5: 61_965,
        6: 92_583,
        7: 137_781,
    }
    expected_counts = {
        1: 8266,
        2: 8239,
        3: 8217,
        4: 8197,
        5: 8173,
        6: 8137,
        7: 8073,
    }

    print("different-q E13 scaled-defect coordinate: PASS")
    print("s upper_M admissible_M_count low_ternary_residues")

    for s in range(1, 8):
        upper = 3**s * (2**(13-s) - 1)
        assert upper == expected_upper[s]

        residue_map = core_residue_map(s)
        assert len(residue_map) == 1 << s

        vals = possible_M_values(s)
        assert len(vals) == expected_counts[s]
        assert all(-113 <= m <= upper for m in vals)

        print(s, upper, len(vals), len(residue_map))

    print("every compatible M uniquely fixes a_0,...,a_(s-1)")


if __name__ == "__main__":
    main()
