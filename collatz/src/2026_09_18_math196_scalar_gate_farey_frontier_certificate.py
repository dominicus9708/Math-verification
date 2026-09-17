#!/usr/bin/env python3
"""MATH-196 scalar first-crossing gate / Farey-frontier certificate.

Finite exact checks only lock the canonical verified-floor constants and the
strict logarithmic comparison at the first Farey mediant.  The universal
implication

    scalar-hard first crossing => beta < q/A < alpha

is algebraic (MATH-196 note), using S_partial < q/3 and Bernoulli's inequality.
The Farey minimum-denominator step is the standard neighbor theorem.

No first-cell emptiness or Collatz closure claim is made.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "farey0", HERE / "universal_verified_floor_parity_spine_farey_certificate.py"
)
farey0 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(farey0)


def main() -> None:
    B0 = farey0.B0
    A0, q0 = farey0.FIRST
    PL, QL = farey0.PL, farey0.QL
    PU, QU = farey0.PU, farey0.QU

    # Canonical Farey-neighbor geometry.
    assert PU * QL - PL * QU == 1
    assert (QL + QU, PL + PU) == (A0, q0)
    assert farey0.in_open_strip(Fraction(q0, A0))

    # The first q is odd, so the universal phase-pair estimate gives
    #
    #   S_partial(q0) > (7*q0 - 1)/36.
    #
    # To prove Gamma(q0)<0 it is therefore enough to certify
    #
    #   B0 * (2^A0/3^q0 - 1) < (7*q0 - 1)/36.
    #
    # Writing lambda=A0 ln2-q0 ln3, this is equivalent to
    #
    #   lambda < ln(1 + (7*q0-1)/(36*B0)).
    assert q0 & 1
    lam_lo, lam_hi = farey0.linear_form_interval(A0, q0)
    assert lam_lo > 0  # coefficient has crossed below one.

    target = Fraction(36 * B0 + 7 * q0 - 1, 36 * B0)
    rhs_lo, rhs_hi = farey0.ln_interval(target, 220)
    assert lam_hi < rhs_lo

    # Cross-check the older coarser result: the first mediant needs B=72
    # under the q/3 correction envelope.
    assert farey0.buffered_B(A0, q0) == 72

    print("PASS MATH-196 exact scalar-gate/Farey frontier checkpoint")
    print("B0=2^71")
    print("Farey neighbors determinant=1")
    print("FIRST=(A0,q0)=", (A0, q0))
    print("FIRST lies in canonical open verified-floor strip")
    print("phase-pair envelope: S_partial(q0) > (7*q0-1)/36")
    print("rigorous log comparison: B0*(2^A0/3^q0-1) < (7*q0-1)/36")
    print("therefore Gamma(q0)<0")
    print("coarse buffered_B(FIRST)=72")
    print("NO FIRST-CELL EMPTINESS CLAIM")
    print("NO COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
