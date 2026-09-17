#!/usr/bin/env python3
"""MATH-192 finite exact regression for singleton overshoot residue theorem.

Checks small exhaustive cylinders/prefix congruences and verifies:

- L>R gives zero or one compatible s in 0<=s<M;
- the direct compatible set equals the canonical inverse-residue test;
- when compatible, the direct source anchor equals A+2^H*r_L;
- the direct master defect equals the residue-substituted formula.

Finite regression only; no layer or Collatz closure claim.
"""

from fractions import Fraction


def ceil_log2(M: int) -> int:
    if M <= 1:
        return 0
    return (M - 1).bit_length()


def main() -> None:
    cases = 0
    compatible_cases = 0

    for M in range(1, 33):
        R = ceil_log2(M)
        for L in range(R + 1, min(R + 5, 9)):
            mod = 1 << L
            for Q in range(0, 7):
                G = pow(pow(3, Q, mod), -1, mod)
                for B in range(0, min(mod, 16)):
                    for C in range(0, min(mod, 16)):
                        r = ((C - B) * G) % mod
                        direct = [s for s in range(M) if (B + (3**Q) * s - C) % mod == 0]
                        predicted = [] if r >= M else [r]
                        assert direct == predicted, (M, R, L, Q, B, C, r, direct)
                        assert len(direct) <= 1
                        cases += 1

                        if direct:
                            compatible_cases += 1
                            s = direct[0]
                            for H in range(0, 5):
                                for A in range(0, 8):
                                    N = A + (1 << H) * s
                                    assert N == A + (1 << H) * r
                                    for rho in (Fraction(3, 2), Fraction(5, 4), Fraction(7, 4)):
                                        for Sigma in (Fraction(1, 3), Fraction(5, 2), Fraction(11, 3)):
                                            direct_defect = Sigma - (N + 1) * (rho - 1)
                                            residue_defect = Sigma - (A + (1 << H) * r + 1) * (rho - 1)
                                            assert direct_defect == residue_defect

    print("PASS MATH-192 singleton residue regression")
    print(f"overshoot_cases={cases}")
    print(f"compatible_singletons={compatible_cases}")
    print("NO NEW PAID-LAYER OR COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
