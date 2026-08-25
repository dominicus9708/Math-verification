#!/usr/bin/env python3
"""Exact certificate for the DSD Beatty macrocycle / surplus Lyapunov rule.

This certificate isolates a structural fact used by the Collatz coefficient
survival language.  It is NOT a Collatz proof.

Definitions:
    b(n) = least q such that 3^q >= 2^n
    delta_n = b(n+1)-b(n), with P=0 (plateau), R=1 (rise)
    d_n = q_n-b(n) >= 0 for a coefficient-surviving parity prefix.

The exact power inequalities 4>3, 9>8, 32>27 imply:
  * PP cannot occur;
  * RRR cannot occur;
  * two short macrocycles A=PR cannot occur consecutively.

Hence from one plateau to the next the macrocycle is A=PR or B=PRR,
and every pair of consecutive macrocycles is AB, BA, or BB.

For a=3/2, the normalized weighted surplus mass over any macrocycle pair
contracts:
    AB/BA: ((1+a)/2)^5 / a^3 = 3125/3456
    BB:    ((1+a)/2)^6 / a^4 = 15625/20736.
Boundary-invalid paths only decrease these factors.

The script also rebuilds the exact Q=7,Kmax=36 compressed reverse-potential
DP used in the current certificates and verifies its maximal potential is
2187/128 < 27.  Consequently strict reverse-potential killing at fixed Q=7
cannot act at endpoint surplus d>=3.  This is a scope/obstruction audit:
the high-surplus tail must be controlled by the Beatty drift, a separate
tail theorem, or by increasing Q.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

Q = 7
KMAX = 36

@dataclass
class E:
    q: int = 0
    K: int = 0
    C: int = 0
    valid: bool = False


def better(a: E, b: E) -> bool:
    if not a.valid:
        return False
    if not b.valid:
        return True
    lhs = 3**a.q * 2**b.K
    rhs = 3**b.q * 2**a.K
    if lhs != rhs:
        return lhs > rhs
    return a.C > b.C


def build_reverse_dp():
    prev_m = 1
    prev = [E() for _ in range(prev_m * (KMAX + 1))]
    keep = [None] * (Q + 1)

    for depth in range(1, Q + 1):
        mod = prev_m * 3
        cur = [E() for _ in range(mod * (KMAX + 1))]

        for z in range(mod):
            r3 = z % 3
            if r3 == 0:
                continue
            a0 = 2 if r3 == 1 else 1

            for budget in range(1, KMAX + 1):
                best = E()
                for invexp in range(a0, budget + 1, 2):
                    numerator = (1 << invexp) * z - 1
                    assert numerator % 3 == 0
                    zp = (numerator // 3) % prev_m if prev_m > 1 else 0
                    suffix = prev[zp * (KMAX + 1) + (budget - invexp)]

                    use_suffix = (
                        suffix.valid and 3**suffix.q > 2**suffix.K
                    )
                    if use_suffix:
                        cand = E(
                            suffix.q + 1,
                            suffix.K + invexp,
                            (1 << suffix.K) + 3 * suffix.C,
                            True,
                        )
                    else:
                        cand = E(1, invexp, 1, True)

                    if better(cand, best):
                        best = cand

                cur[z * (KMAX + 1) + budget] = best

        keep[depth] = cur
        prev = cur
        prev_m = mod

    return keep


def exact_weight_ratio(d0, deltas, a=Fraction(3, 2)):
    total = Fraction(0, 1)
    L = len(deltas)
    for bits in product((0, 1), repeat=L):
        d = d0
        ok = True
        for bit, rise in zip(bits, deltas):
            d += bit - rise
            if d < 0:
                ok = False
                break
        if ok:
            total += a**d
    return total / (2**L) / (a**d0)


def main():
    # Exact arithmetic behind the Beatty local-pattern proof.
    assert 4 > 3
    assert 9 > 8
    assert 32 > 27

    # P=0, R=1.  A=PR, B=PRR.
    patterns = {
        "AB": (0, 1, 0, 1, 1),
        "BA": (0, 1, 1, 0, 1),
        "BB": (0, 1, 1, 0, 1, 1),
    }

    a = Fraction(3, 2)
    F5 = ((1 + a) / 2) ** 5 / a**3
    F6 = ((1 + a) / 2) ** 6 / a**4
    assert F5 == Fraction(3125, 3456)
    assert F6 == Fraction(15625, 20736)
    assert F6 < F5 < 1

    # For d at least the number of rises, no prefix can hit the boundary,
    # so the closed-form factors are attained exactly.  Smaller d is audited
    # by complete enumeration and can only improve the contraction.
    for name, deltas in patterns.items():
        rises = sum(deltas)
        target = F5 if len(deltas) == 5 else F6
        vals = [exact_weight_ratio(d, deltas, a) for d in range(rises + 1)]
        assert max(vals) == target
        assert vals[rises] == target
        print(name, "weighted_ratios",
              " ".join(f"{v.numerator}/{v.denominator}" for v in vals),
              "max", f"{target.numerator}/{target.denominator}")

    rev = build_reverse_dp()
    M = 3**Q
    best = None
    valid = 0
    strict_gt_1 = 0
    for z in range(M):
        e = rev[Q][z * (KMAX + 1) + KMAX]
        if not e.valid:
            continue
        valid += 1
        lam = Fraction(3**e.q, 2**e.K)
        if lam > 1:
            strict_gt_1 += 1
        item = (lam, e.C, z, e)
        if best is None or item[:2] > best[:2]:
            best = item

    assert valid == 2 * 3**(Q - 1)
    assert best is not None
    lam, _C, z, e = best
    assert lam == Fraction(2187, 128)
    assert lam < 27

    print("beatty_macro_pair_sigma", f"{F5.numerator}/{F5.denominator}",
          float(F5))
    print("q7_reverse_valid_residues", valid, "of", M)
    print("q7_reverse_lambda_gt_1", strict_gt_1, "of", M)
    print("q7_reverse_lambda_max", f"{lam.numerator}/{lam.denominator}",
          float(lam), "at_z", z, "q", e.q, "K", e.K, "C", e.C)
    print("fixed_q7_strict_reverse_blind_for_surplus_d_ge", 3)
    print("PASS")


if __name__ == "__main__":
    main()
