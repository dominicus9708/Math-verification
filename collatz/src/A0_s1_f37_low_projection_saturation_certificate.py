#!/usr/bin/env python3
"""
A0 s=1 f=37 low-projection saturation certificate.

Purpose
-------
The f=37 ordinary-checkpoint sieve is nontrivial modulo 3*2^38, but its
allowed band is much longer than every lower checkpoint modulus presently
exposed on the dyadic side.

This certificate proves that projecting the f=37 allowed checkpoint band to
Z mod 2^27 (and several other low moduli) is surjective. Therefore the
27-bit checkpoint residue alone cannot prune the f=37 branch.

This is an exact negative audit result. It is independent of whether the
8,478,475 necessary tail-27 words have already been proved to be checkpoint
Z-addresses.

EXACT:
  * f=37 allowed band length = L_- corridor inclusive size;
  * projection of any integer interval of length >= m onto Z/mZ is surjective;
  * all residues occur at mod 2^27, 3*2^27, 2^28, 3*2^28, and 2^37;
  * 2^38 is the first pure dyadic modulus at which the f=37 band may have gaps.

REJECTED shortcut:
  * use f=37 arithmetic alone to remove any Z mod 2^27 residue.

OPEN:
  * coherent production of (Z mod 2^27, Z mod 3^28) by one admissible
    long correction/tail object;
  * full correction-language membership.
"""

from __future__ import annotations

L_MINUS_MIN = 669_562_762_561
L_MINUS_MAX = 934_928_480_993
BAND_LEN = L_MINUS_MAX - L_MINUS_MIN + 1

M2_27 = 2**27
M3_2_27 = 3 * 2**27
M2_28 = 2**28
M3_2_28 = 3 * 2**28
M2_37 = 2**37
M2_38 = 2**38
M3_2_38 = 3 * 2**38

EXPECTED_DIVMODS = {
    M2_27: (1977, 17_270_177),
    M3_2_27: (659, 17_270_177),
    M2_28: (988, 151_487_905),
    M3_2_28: (329, 419_923_361),
    M2_37: (1, 127_926_764_961),
    M2_38: (0, 265_365_718_433),
    M3_2_38: (0, 265_365_718_433),
}


def residue_multiplicities_for_interval(length: int, modulus: int) -> tuple[int, int]:
    """For length=q*m+r, every residue occurs q or q+1 times."""
    assert length >= 1
    assert modulus >= 1
    return divmod(length, modulus)


def main() -> None:
    assert BAND_LEN == 265_365_718_433

    for modulus, expected in EXPECTED_DIVMODS.items():
        got = residue_multiplicities_for_interval(BAND_LEN, modulus)
        assert got == expected

    # Current checkpoint dyadic exposure is completely saturated by the
    # f=37 ordinary-checkpoint band.
    q27, r27 = divmod(BAND_LEN, M2_27)
    assert q27 == 1977
    assert r27 == 17_270_177
    assert q27 >= 1

    # Even adjoining one ternary digit to the 27-bit modulus leaves a fully
    # saturated projection.
    q3_27, r3_27 = divmod(BAND_LEN, M3_2_27)
    assert q3_27 == 659
    assert r3_27 == 17_270_177
    assert q3_27 >= 1

    # Saturation persists through pure dyadic depth 37.
    assert M2_37 < BAND_LEN < M2_38
    q37, r37 = divmod(BAND_LEN, M2_37)
    assert (q37, r37) == (1, 127_926_764_961)

    # Hence depth 38 is the first pure dyadic depth at which a contiguous
    # f=37 band can have missing residue classes.
    assert BAND_LEN < M2_38
    assert all(2**k <= BAND_LEN for k in range(1, 38))

    print("A0 s=1 f37 low-projection saturation: PASS")
    print("band length:", BAND_LEN)
    for modulus in (
        M2_27, M3_2_27, M2_28, M3_2_28, M2_37, M2_38, M3_2_38
    ):
        q, r = divmod(BAND_LEN, modulus)
        print(f"mod {modulus}: every residue at least {q} times; extra classes={r}")
    print("first non-saturated pure dyadic depth: 38")


if __name__ == "__main__":
    main()
