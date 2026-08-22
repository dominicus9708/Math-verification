#!/usr/bin/env python3
"""Packed-terminal s=1 alternate-predecessor certificate.

This file implements a deterministic original-start elimination rule that is
compatible with the corrected Stage 3C logic.

At a Beatty plateau

    qmin(L) = qmin(L-1) = q,

consider a coefficient-surviving length-L word w with exactly q odd symbols
and final bit 0.  Define the packed-terminal alternate

    u* = 0^(L-q) 1^q.

For fixed (L,q), u* maximizes the affine correction and

    R*(L,q) = 2^(L-q) (3^q - 2^q).

If

    v3(R* - R_w) = 1,

then s=1, d=q-1.  The (q-1)-th odd of u* occurs at time t_d=L-1, and the
plateau identity implies

    2^(L-1) > 3^(q-1).

Hence the exact alternate-predecessor integerization theorem produces a smaller
integer original-coordinate predecessor in the large-start regime used by the
m=45 proof program.

The s=1 test is terminal: if p_{q-1}<p_q are the last two zero-indexed odd
positions of w, then

    R_w mod 9 = 3*2^p_{q-1} + 2^p_q mod 9,

while

    R* mod 9 = 3*2^(L-2) + 2^(L-1) mod 9.

Thus v3(R*-R_w)=1 is determined by (p_{q-1},p_q,L) mod 6.

The dynamic program below counts this safe elimination rule without storing
full corrections.  It is a finite calibration, not an asymptotic theorem and
not a proof of the Collatz conjecture.
"""

from collections import defaultdict

EXPECTED = {
    6:  (4, 8, 3, 1),
    9:  (6, 38, 12, 4),
    11: (7, 128, 30, 13),
    14: (9, 734, 173, 61),
    17: (11, 4228, 961, 337),
    19: (12, 14990, 2652, 1101),
    22: (14, 93222, 17637, 6199),
    25: (16, 573162, 108950, 38119),
    28: (18, 3524586, 663535, 231515),
    30: (19, 12771274, 1900470, 775398),
    38: (24, 1934757182, 257978502, 104198298),
    49: (31, 1991314765702, 248369601964, 100037865953),
}


def qmins(H: int):
    out = [0] * (H + 1)
    q = 0
    p3 = 1
    for L in range(1, H + 1):
        while p3 < (1 << L):
            q += 1
            p3 *= 3
        out[L] = q
    return out


def v3(n: int) -> int:
    s = 0
    while n and n % 3 == 0:
        n //= 3
        s += 1
    return s


def correction(mask: int, L: int):
    R = 0
    q = 0
    pos = []
    for i in range(L):
        if (mask >> i) & 1:
            R = 3 * R + (1 << i)
            q += 1
            pos.append(i)
    return q, R, pos


def coefficient_survives(mask: int, L: int) -> bool:
    q = 0
    p3 = 1
    for i in range(L):
        if (mask >> i) & 1:
            q += 1
            p3 *= 3
        if p3 < (1 << (i + 1)):
            return False
    return True


def packed_correction(L: int, q: int) -> int:
    direct = 0
    for i in range(L - q, L):
        direct = 3 * direct + (1 << i)
    closed = (1 << (L - q)) * (3**q - 2**q)
    assert direct == closed
    return closed


def terminal_s1(L: int, a: int, b: int) -> bool:
    target = (3 * pow(2, L - 2, 9) + pow(2, L - 1, 9)) % 9
    actual = (3 * pow(2, a, 9) + pow(2, b, 9)) % 9
    diff = (target - actual) % 9
    return diff % 3 == 0 and diff != 0


def brute_terminal_equivalence(maxL: int = 14) -> None:
    qm = qmins(maxL)
    for L in range(3, maxL + 1):
        if qm[L] != qm[L - 1]:
            continue
        q = qm[L]
        Rstar = packed_correction(L, q)
        for mask in range(1 << L):
            if not coefficient_survives(mask, L):
                continue
            qw, Rw, pos = correction(mask, L)
            if qw != q or ((mask >> (L - 1)) & 1):
                continue
            assert len(pos) >= 2
            exact = Rstar > Rw and v3(Rstar - Rw) == 1
            terminal = terminal_s1(L, pos[-2], pos[-1])
            assert exact == terminal
    print("terminal_mod9_equivalence_through_L", maxL, "PASS")


def run(maxL: int = 120) -> None:
    qm = qmins(maxL)

    # State: (odd count, previous-to-last odd position mod 6,
    # last odd position mod 6).  -1 marks an unavailable older odd.
    dp = {(0, -1, -1): 1}

    print("L q total_survivors boundary_even_q packed_s1_removed removed_over_total removed_over_boundary")

    for L in range(1, maxL + 1):
        threshold = qm[L]

        plateau_row = None
        if L >= 3 and qm[L] == qm[L - 1]:
            q = qm[L]
            boundary = 0
            killed = 0
            for (qq, a, b), count in dp.items():
                if qq != q:
                    continue
                boundary += count
                assert a >= 0 and b >= 0
                if terminal_s1(L, a, b):
                    killed += count
            plateau_row = (q, boundary, killed)

        nd = defaultdict(int)
        pos = (L - 1) % 6
        for (q, a, b), count in dp.items():
            # even child
            if q >= threshold:
                nd[(q, a, b)] += count
            # odd child
            if q + 1 >= threshold:
                nd[(q + 1, b, pos)] += count
        dp = nd

        if plateau_row is not None:
            q, boundary, killed = plateau_row
            total = sum(dp.values())

            if L in EXPECTED:
                expected = EXPECTED[L]
                assert (q, total, boundary, killed) == expected, (
                    L, (q, total, boundary, killed), expected
                )

            if L in EXPECTED or L in (68, 84, 103, 120):
                print(
                    L,
                    q,
                    total,
                    boundary,
                    killed,
                    killed / total,
                    killed / boundary,
                )

    print("packed-terminal s=1 predecessor certificate: PASS")


def main():
    brute_terminal_equivalence()
    run()


if __name__ == "__main__":
    main()
