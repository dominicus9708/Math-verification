#!/usr/bin/env python3
"""Exact two-ended formation certificate for the first global resonance.

External finite input is only the already-recorded published 2^71 Collatz
verification used to obtain the first-resonance start/gap band.  This script
certifies, with exact rational log intervals and modular arithmetic, that the
mechanical first-crossing word is incompatible with BOTH exposed ends:

  * its first 72 parity bits give a start above the allowed band;
  * its last 46 odd ordinals give an endpoint above the allowed near-return band.

No floating-point arithmetic is used.
"""

from fractions import Fraction

A0 = 114_208_327_604
Q0 = 72_057_431_991
B = 1 << 71
K_START = 72
K_END = 46

EXPECTED_START = 4_697_939_311_072_332_635_131
EXPECTED_END = 4_699_104_266_570_964_686_821


def log_bounds(z: Fraction, n: int = 60):
    """Bounds log((1+z)/(1-z)) by the positive atanh series."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2) * z ** (2 * n + 3)
        / ((2 * n + 3) * (1 - z * z))
    )
    return s, s + tail


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def mechanical_position(j: int, gamma_lo: Fraction, gamma_hi: Fraction) -> int:
    """Return floor((j-1) log_2 3), certified by interval coincidence."""
    n = j - 1
    lo = floor_fraction(n * gamma_lo)
    hi = floor_fraction(n * gamma_hi)
    assert lo == hi, (j, lo, hi)
    return lo


def correction_from_bits(bits):
    R = 0
    q = 0
    for i, bit in enumerate(bits):
        if bit:
            R = 3 * R + (1 << i)
            q += 1
    return q, R


def main() -> None:
    # ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2).
    l2, u2 = log_bounds(Fraction(1, 3))
    l3, u3 = log_bounds(Fraction(1, 2))
    gamma_lo = l3 / u2
    gamma_hi = u3 / l2

    # ----- Start-side exposure: first 72 mechanical bits -----
    first_positions = []
    j = 1
    while True:
        p = mechanical_position(j, gamma_lo, gamma_hi)
        if p >= K_START:
            break
        first_positions.append(p)
        j += 1

    assert len(first_positions) == 46
    bits = [0] * K_START
    for p in first_positions:
        bits[p] = 1

    q72, R72 = correction_from_bits(bits)
    assert q72 == 46
    M2 = 1 << K_START
    rho72 = (-R72 * pow(pow(3, q72), -1, M2)) % M2
    assert rho72 == EXPECTED_START
    assert 3 * rho72 > 4 * B

    # ----- Endpoint-side exposure: last 46 mechanical odd ordinals -----
    last_positions = [
        mechanical_position(j, gamma_lo, gamma_hi)
        for j in range(Q0 - K_END + 1, Q0 + 1)
    ]

    expected_positions = [
        114208327531, 114208327532, 114208327534, 114208327535,
        114208327537, 114208327539, 114208327540, 114208327542,
        114208327543, 114208327545, 114208327546, 114208327548,
        114208327550, 114208327551, 114208327553, 114208327554,
        114208327556, 114208327558, 114208327559, 114208327561,
        114208327562, 114208327564, 114208327565, 114208327567,
        114208327569, 114208327570, 114208327572, 114208327573,
        114208327575, 114208327577, 114208327578, 114208327580,
        114208327581, 114208327583, 114208327584, 114208327586,
        114208327588, 114208327589, 114208327591, 114208327592,
        114208327594, 114208327596, 114208327597, 114208327599,
        114208327600, 114208327602,
    ]
    assert last_positions == expected_positions
    assert last_positions[-1] < A0

    M3 = 3 ** K_END
    assert M3 > (1 << 72)

    # In 2^A y = 3^q N + R, modulo 3^46 only the last 46 odd
    # ordinals of R survive.  For ell=0 the contribution is the final odd.
    R_tail = 0
    for ell in range(K_END):
        pos = last_positions[-1 - ell]
        R_tail = (R_tail + (3 ** ell) * pow(2, pos, M3)) % M3

    inv_2A = pow(pow(2, A0, M3), -1, M3)
    y_mech = (inv_2A * R_tail) % M3
    assert y_mech == EXPECTED_END

    # Every first-resonance candidate has
    # N < (4/3)2^71 and 0<g<2^33, so y=N+g obeys
    # 3y < 4*2^71 + 3*2^33.
    assert 3 * y_mech > 4 * B + 3 * (1 << 33)

    print("PASS first-resonance two-ended mechanical exclusion")
    print(f"start_modulus=2^72={M2}")
    print(f"mechanical_start_residue={rho72}")
    print(f"endpoint_modulus=3^46={M3}")
    print(f"mechanical_tail_first_position={last_positions[0]}")
    print(f"mechanical_tail_last_position={last_positions[-1]}")
    print(f"mechanical_endpoint_residue={y_mech}")
    print("mechanical word violates both the start band and endpoint band")


if __name__ == "__main__":
    main()
