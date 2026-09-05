#!/usr/bin/env python3
"""Exact Q7 fixed-reverse barrier on the formal Beatty-boundary path.

This certificate proves a proof-strategy barrier, not a Collatz counterexample.
It enumerates an overlanguage of all possible suffixes containing the most recent
seven Beatty rises, using only the already-proved no-PP and no-RRR restrictions.

For the formal path e_n = delta_n at surplus d=2, d stays exactly 2.  After seven
rise bits the old z-coordinate is annihilated modulo 3^7.  Every allowed suffix
has best Q7 reverse coefficient potential <= 729/256 < 9, while d=2 implies the
forward coefficient ratio Theta >= 3^2 = 9.  Hence the fixed-Q7 reverse-potential
mechanism cannot coefficient-wise eliminate this entire formal low-strip path.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

Q = 7
KMAX = 36
MOD = 3**Q
INV2 = pow(2, -1, MOD)


@dataclass(frozen=True)
class Entry:
    q: int = 0
    K: int = 0
    C: int = 0
    valid: bool = False


def better(a: Entry, b: Entry) -> bool:
    if not a.valid:
        return False
    if not b.valid:
        return True
    lhs = 3**a.q * 2**b.K
    rhs = 3**b.q * 2**a.K
    if lhs != rhs:
        return lhs > rhs
    return a.C > b.C


def build_best_reverse():
    prev_mod = 1
    prev = [Entry() for _ in range(prev_mod * (KMAX + 1))]

    for _depth in range(1, Q + 1):
        mod = prev_mod * 3
        cur = [Entry() for _ in range(mod * (KMAX + 1))]

        for z in range(mod):
            residue = z % 3
            if residue == 0:
                continue
            first_exp = 2 if residue == 1 else 1

            for budget in range(1, KMAX + 1):
                best = Entry()
                for invexp in range(first_exp, budget + 1, 2):
                    numerator = (1 << invexp) * z - 1
                    assert numerator % 3 == 0
                    zp = (numerator // 3) % prev_mod if prev_mod > 1 else 0
                    suffix = prev[zp * (KMAX + 1) + (budget - invexp)]

                    # Same compressed DP convention used by the existing Q7
                    # reverse-potential certificates: continue a suffix only
                    # when its own coefficient potential exceeds 1.
                    if suffix.valid and 3**suffix.q > 2**suffix.K:
                        cand = Entry(
                            suffix.q + 1,
                            suffix.K + invexp,
                            (1 << suffix.K) + 3 * suffix.C,
                            True,
                        )
                    else:
                        cand = Entry(1, invexp, 1, True)

                    if better(cand, best):
                        best = cand

                cur[z * (KMAX + 1) + budget] = best

        prev = cur
        prev_mod = mod

    return [prev[z * (KMAX + 1) + KMAX] for z in range(MOD)]


def beatty_overlanguage(word):
    """Only use proved local Beatty restrictions no PP and no RRR.

    P=0, R=1.  We intentionally do NOT use the stronger no-AA restriction, so
    the enumeration is an overlanguage of the true Beatty factor set.
    """
    s = ''.join(map(str, word))
    return '00' not in s and '111' not in s


def endpoint_z(word):
    z = 0
    for e in word:
        z = (INV2 * (z if e == 0 else 3 * z + 1)) % MOD
    return z


def main():
    best = build_best_reverse()

    candidates = []
    # A suffix beginning at the seventh-most-recent rise has exactly seven R's.
    # no-PP implies at most one P between consecutive R's and at most one
    # trailing P, hence its length is at most 14.
    for L in range(Q, 2 * Q + 1):
        for word in product((0, 1), repeat=L):
            if word[0] != 1:
                continue
            if sum(word) != Q:
                continue
            if not beatty_overlanguage(word):
                continue

            z = endpoint_z(word)
            ent = best[z]
            lam = Fraction(3**ent.q, 2**ent.K) if ent.valid else Fraction(0, 1)
            candidates.append((lam, word, z, ent))

    assert len(candidates) == 42

    lam_max, word_max, z_max, ent_max = max(candidates, key=lambda x: x[0])
    assert lam_max == Fraction(729, 256)
    assert lam_max < 3 < 9

    # Seven rise updates multiply the forgotten incoming z by 3^7; modulo 3^7
    # this coefficient is zero.  Plateau updates only add powers of 2^{-1} and
    # do not change that annihilation.
    assert 3**Q % MOD == 0

    print("Q", Q, "KMAX", KMAX)
    print("overlanguage_suffix_count", len(candidates))
    print("max_reverse_potential", f"{lam_max.numerator}/{lam_max.denominator}", float(lam_max))
    print("max_word", ''.join(map(str, word_max)))
    print("max_endpoint_z", z_max)
    print("max_entry_qK", ent_max.q, ent_max.K)
    print("d2_forward_lower_scale", 9)
    print("PASS_FIXED_Q7_PATHWISE_BARRIER")


if __name__ == "__main__":
    main()
