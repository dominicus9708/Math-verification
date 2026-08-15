#!/usr/bin/env python3
"""Exact H19 diagnostic for the G13 h=5233 parent-credit handoff.

The first survival-compatible nonzero transition lift at G13 neutral has

    h=5233, k=1, F-h=12,
    Delta_gate = 2^12 = 4096,
    local canonical shift = -3^12.

At 19-bit resolution

    3^12 = 2^19 + 7153,

so the low dyadic shift is the primitive length-19 integer defect 7153.

This file then audits one exact length-19 factor that blocks the locally-neutral
credit path.  The two relevant shifts have no realization when both words are
required to stay in the local neutral fibre (incoming relative height H=0), but
both acquire exact realizations as soon as one unit of incoming survival height
is allowed.  This proves that scalar credit / local-neutral tracking is too
small a state space; the accumulated height must be carried explicitly.

This is a finite diagnostic, not a Collatz proof.
"""

from itertools import combinations

L = 19
MOD = 1 << L
Q = 12
REF = "1101101011011010110"
LEFT_CREDITS = (1585, 1586)
EXPECTED = {
    1585: (1, 1604),
    1586: (1, 1603),
}


def correction(pos):
    R = 0
    for p in pos:
        R = 3 * R + (1 << p)
    return R


def records():
    ref_prefix = []
    c = 0
    for ch in REF:
        c += ch == "1"
        ref_prefix.append(c)
    assert c == Q

    by_residue = {}
    for pos in combinations(range(L), Q):
        S = set(pos)
        c = 0
        M = 10**9
        for i in range(L):
            c += i in S
            M = min(M, c - ref_prefix[i])
        R = correction(pos)
        r = R % MOD
        # Fixed (L,q) parity words have distinct correction residues mod 2^L.
        assert r not in by_residue
        by_residue[r] = (M, R, pos)
    assert len(by_residue) == 50388
    return by_residue


def minimum_height_witness(by_residue, delta_left):
    # Reverse local credit relation:
    #   delta_right = (3^q delta_left - (R_u-R_w))/2^L.
    # Therefore R_u-R_w == 3^q delta_left (mod 2^L).
    shift = (3**Q * delta_left) % MOD
    best = None

    for rw, (Mw, Rw, pw) in by_residue.items():
        ru = (rw + shift) % MOD
        ent = by_residue.get(ru)
        if ent is None:
            continue
        Mu, Ru, pu = ent
        H = max(0, -Mw, -Mu)
        num = 3**Q * delta_left - (Ru - Rw)
        assert num % MOD == 0
        delta_right = num // MOD
        if delta_right <= 0:
            continue
        item = (H, delta_right, Mw, Mu, pw, pu)
        if best is None or item[:2] < best[:2]:
            best = item

    return best


def main():
    assert 3**12 - 2**19 == 7153
    assert 7153 == 23 * 311
    assert (-3**12) % 2**19 == (-7153) % 2**19
    assert 2**12 == 4096

    R = records()

    for dl in LEFT_CREDITS:
        # H=0 corresponds to both words lying in the local neutral fibre.
        shift = (3**Q * dl) % MOD
        neutral_pairs = 0
        for rw, (Mw, _, _) in R.items():
            if Mw < 0:
                continue
            ent = R.get((rw + shift) % MOD)
            if ent is not None and ent[0] >= 0:
                neutral_pairs += 1
        assert neutral_pairs == 0

        best = minimum_height_witness(R, dl)
        assert best is not None
        H, dr = best[:2]
        assert (H, dr) == EXPECTED[dl], (dl, best[:2], EXPECTED[dl])
        assert H == 1

        print(
            "left_credit", dl,
            "neutral_pairs", neutral_pairs,
            "minimum_height", H,
            "right_credit", dr,
        )

    print("primitive_19bit_defect", 7153)
    print("G13_h5233_parent_credit", 4096)
    print("height-aware state is necessary: PASS")


if __name__ == "__main__":
    main()
