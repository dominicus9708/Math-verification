#!/usr/bin/env python3
"""
MATH-057 exact phase/address mechanical-run barrier certificate.

Scope
-----
For a hypothetical first-cell path before its first coefficient crossing,
consider an anchor with boundary slack u=0.  If no positive-slack odd event
occurs, the continuation is the zero-penalty mechanical/Sturmian boundary
word driven by theta=log_2(3/2).

This certificate partitions the complete phase range Omega in (1/2,1) into
exact rational intervals, constructs the corresponding length-L mechanical
factor, computes the unique dyadic endpoint residue for that factor, and
checks whether the same phase can still be compatible with the current
first-cell ordinary-start window.

Canonical result:
  * L=78 still has two compatible phase intervals.
  * L=79 has zero compatible intervals.
Therefore every zero-penalty mechanical segment beginning at a u=0 anchor has
length at most 78 within the audited first-cell scope.

The q=0 endpoint phase Omega=1 is checked separately.
Finite exact arithmetic only. Collatz conjecture remains OPEN.
"""
from fractions import Fraction

A0 = 114_208_327_604
Q0 = 72_057_431_991
LO = 1 << 71
HI = 1364 * (1 << 61)
QBOUND = Fraction(Q0, 3)


def m(q: int) -> int:
    """Exact floor(q*log_2(3/2)) by integer inequalities."""
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    return d


def threshold_omega(r: int) -> Fraction:
    """
    Phase threshold for floor(x+r*theta), written in Omega=2^-x.

    If theta=log_2(3/2) and x in [0,1), the floor changes at
      x = 1 - {r theta}.
    Since 2^-{r theta} = 2^(r+m(r))/3^r, the corresponding Omega threshold is
      3^r / 2^(r+m(r)+1).
    """
    return Fraction(3**r, 2 ** (r + m(r) + 1))


def factor_from_omega(L: int, omega: Fraction) -> tuple[int, ...]:
    """Length-L zero-penalty mechanical factor at a boundary anchor."""
    bits = [0] * L
    r = 0
    while True:
        if r == 0:
            pos = 0
        else:
            pos = r + m(r) + (1 if omega <= threshold_omega(r) else 0)
        if pos >= L:
            break
        bits[pos] = 1
        r += 1
    return tuple(bits)


def correction_and_q(bits: tuple[int, ...]) -> tuple[int, int]:
    C = 0
    q = 0
    for p, b in enumerate(bits):
        if b:
            C = 3 * C + (1 << p)
            q += 1
    return C, q


def start_residue(bits: tuple[int, ...]) -> int:
    """Unique starting residue mod 2^L that realizes the parity factor."""
    C, q = correction_and_q(bits)
    mod = 1 << len(bits)
    inv = pow(pow(3, q, mod), -1, mod)
    return (-C * inv) % mod


def phase_intervals(L: int) -> list[tuple[Fraction, Fraction]]:
    """Complete rational partition of Omega in (1/2,1)."""
    cuts = {Fraction(1, 2), Fraction(1, 1)}
    for r in range(1, L + 1):
        cuts.add(threshold_omega(r))
    s = sorted(cuts)
    return [(s[i], s[i + 1]) for i in range(len(s) - 1)]


def compatible_intervals(L: int):
    out = []
    for lo, hi in phase_intervals(L):
        omega = (lo + hi) / 2
        bits = factor_from_omega(L, omega)
        R = start_residue(bits)

        # At u=0, endpoint y=(N+S)/Omega and S<q/3<=Q0/3.
        # The first-cell window requires LO<N<HI.  Hence necessarily
        #   LO < Omega*R < HI + Q0/3.
        # For L>=73 the exact endpoint bound y<2^73<=2^L makes y=R,
        # not merely y congruent to R mod 2^L.
        low = max(lo, Fraction(LO, R))
        high = min(hi, Fraction(HI, R) + QBOUND / R)
        if low < high:
            out.append((lo, hi, R, low, high))

    # q=0 has Omega=1, which is not inside the open phase partition.
    initial_bits = factor_from_omega(L, Fraction(1, 1))
    initial_R = start_residue(initial_bits)
    initial_ok = LO < initial_R < HI  # here S=0, so N=R exactly.
    return out, initial_R, initial_ok


def main() -> None:
    # Uniform endpoint bound at every u=0 anchor before the first cell crossing.
    assert 2 * (Fraction(HI, 1) + QBOUND) < 2**73

    expected = {
        73: 15,
        74: 7,
        75: 5,
        76: 4,
        77: 2,
        78: 2,
        79: 0,
    }

    for L in range(73, 80):
        comp, initial_R, initial_ok = compatible_intervals(L)
        assert len(phase_intervals(L)) == L + 1
        assert len(comp) == expected[L], (L, len(comp), expected[L])
        assert not initial_ok
        vals = []
        for lo, hi in phase_intervals(L):
            vals.append(start_residue(factor_from_omega(L, (lo + hi) / 2)))
        print(L, len(phase_intervals(L)), len(comp), min(vals), initial_R)

    assert len(compatible_intervals(78)[0]) == 2
    assert len(compatible_intervals(79)[0]) == 0

    # Combinatorial paid-cluster consequence used in the MATH-057 note.
    # A positive-slack odd event has cost >1/12.  If P is the number of such
    # events, paid clusters contribute at most 2P+C residual steps, C<=P,
    # while the C+1 zero-penalty mechanical segments contribute <=78(C+1).
    # Thus K<=81P+78 and P>=ceil((K-78)/81).
    K = A0 - 1
    pmin = max(0, (K - 78 + 80) // 81)
    assert pmin == 1_409_979_353
    print("A0_minus_1", K, "positive_event_lower_bound", pmin,
          "penalty_gt", Fraction(pmin, 12))

    print("PASS MATH-057 exact phase-address mechanical barrier certificate")


if __name__ == "__main__":
    main()
