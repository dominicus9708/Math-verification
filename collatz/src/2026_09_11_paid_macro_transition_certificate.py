#!/usr/bin/env python3
"""
MATH-058R exact paid-macro transition certificate.

Reproducibility correction (2026-09-11): the original MATH-058 certificate
emitted one paid-exit record for every parity-compatible dyadic lift t, then
one_paid_outcomes() ignored that stored t and re-enumerated the full lift
interval.  This duplicated source cylinders.

This corrected version stores each paid-exit phase/address source exactly once
and resolves the lift congruence only in one_paid_outcomes().  The canonical
MATH-058 table is restored exactly: L=69:(20,1), 70:(4,0), 71:(4,0),
72:(0,0).  The mathematical conclusions of MATH-058 are unchanged; this is a
certificate-state bookkeeping repair.

Finite exact arithmetic only. Collatz remains OPEN.
"""
from fractions import Fraction

Q0 = 72_057_431_991
LO = 1 << 71
HI = 1364 * (1 << 61)
U = Fraction(HI, 1) + Fraction(Q0, 3)
YBOUND = 2 * U
YMAX = (YBOUND.numerator - 1) // YBOUND.denominator

MAXR = 100
M = [0] * (MAXR + 1)
for q in range(MAXR + 1):
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    M[q] = d

TAU = [None] * (MAXR + 1)
for r in range(1, MAXR + 1):
    TAU[r] = Fraction(3**r, 2 ** (r + M[r] + 1))


def phase_intervals(L: int):
    cuts = {Fraction(1, 2), Fraction(1, 1)}
    for r in range(1, L + 1):
        cuts.add(TAU[r])
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def mechanical_factor(L: int, omega: Fraction):
    bits = [0] * L
    r = 0
    while True:
        if r == 0:
            pos = 0
        else:
            pos = r + M[r] + (1 if omega <= TAU[r] else 0)
        if pos >= L:
            break
        bits[pos] = 1
        r += 1
    return tuple(bits)


def correction_and_q(bits):
    C = q = 0
    for p, b in enumerate(bits):
        if b:
            C = 3 * C + (1 << p)
            q += 1
    return C, q


def start_residue(bits):
    C, q = correction_and_q(bits)
    mod = 1 << len(bits)
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def lift_bounds(L: int, R: int, lo: Fraction, hi: Fraction):
    step = 1 << L
    x = (Fraction(LO, 1) / hi - R) / step
    tmin = max(0, x.numerator // x.denominator + 1)

    x2 = (U / lo - R) / step
    if x2.numerator >= 0:
        ceilx = (x2.numerator + x2.denominator - 1) // x2.denominator
    else:
        ceilx = -((-x2.numerator) // x2.denominator)
    tmax = ceilx - 1
    tmax = min(tmax, (YMAX - R) // step)
    return tmin, tmax


def phase_multiplier(qinc: int, omega: Fraction):
    dm = M[qinc] + (1 if omega <= TAU[qinc] else 0)
    return Fraction(2 ** (qinc + dm), 3**qinc)


def first_with_parity(tmin: int, tmax: int, parity: int):
    t = tmin if (tmin & 1) == parity else tmin + 1
    return t if t <= tmax else None


def paid_exit_sources(L: int):
    """Unique phase/address sources for which a paid exit exists.

    The older certificate emitted one record for every parity-compatible lift t,
    while the downstream one-paid routine ignored that t and re-enumerated the
    full lift interval.  That duplicated source cylinders.  Here one source
    cylinder is retained exactly once; t is resolved only in one_paid_outcomes.
    """
    out = []
    for lo, hi in phase_intervals(L):
        omega = (lo + hi) / 2
        bits = mechanical_factor(L, omega)
        R = start_residue(bits)
        C, qinc = correction_and_q(bits)
        d = L - qinc
        dm = M[qinc] + (1 if omega <= TAU[qinc] else 0)
        uend = dm - d
        if uend != 1:
            continue

        E0 = (3**qinc * R + C) >> L
        tmin, tmax = lift_bounds(L, R, lo, hi)
        if tmin > tmax:
            continue

        wanted = (1 - E0) & 1
        if first_with_parity(tmin, tmax, wanted) is not None:
            out.append((lo, hi, R, E0, qinc))
    return out


def one_paid_outcomes(L: int):
    out = []
    for lo, hi, R, E0, qinc in paid_exit_sources(L):
        omega = (lo + hi) / 2
        mult = phase_multiplier(qinc, omega)

        cut = Fraction(3, 4) / mult
        cuts = [lo]
        if lo < cut < hi:
            cuts.append(cut)
        cuts.append(hi)

        for a, b in zip(cuts[:-1], cuts[1:]):
            ocur = ((a + b) / 2) * mult
            eps = 0 if ocur > Fraction(3, 4) else 1
            tmin, tmax = lift_bounds(L, R, a, b)
            if tmin > tmax:
                continue

            mod = 4 if eps == 0 else 8
            target = 1 if eps == 0 else 5
            coeff = pow(3, qinc, mod)
            tres = ((target - E0) * pow(coeff, -1, mod)) % mod
            first = tmin + ((tres - tmin) % mod)

            for t in range(first, tmax + 1, mod):
                E = E0 + t * 3**qinc
                assert E & 1
                endpoint = (3 * E + 1) // 2
                ok = True
                for _ in range(1 + eps):
                    if endpoint & 1:
                        ok = False
                        break
                    endpoint //= 2
                if not ok:
                    continue

                oa, ob = a * mult, b * mult
                if eps == 0:
                    na, nb = oa * Fraction(2, 3), ob * Fraction(2, 3)
                else:
                    na, nb = oa * Fraction(4, 3), ob * Fraction(4, 3)
                out.append((endpoint, na, nb))
    return out


def actual_bits(n: int, L: int):
    out = []
    for _ in range(L):
        b = n & 1
        out.append(b)
        n = (3 * n + 1) // 2 if b else n // 2
    return out


def can_reach_next_paid(state, Lmax: int = 12):
    endpoint, lo, hi = state
    abits = actual_bits(endpoint, Lmax)
    cuts = {lo, hi}
    for r in range(1, Lmax + 1):
        if lo < TAU[r] < hi:
            cuts.add(TAU[r])
    s = sorted(cuts)

    for a, b in zip(s[:-1], s[1:]):
        omega = (a + b) / 2
        mbits = mechanical_factor(Lmax, omega)
        j = 0
        while j < Lmax and abits[j] == mbits[j]:
            j += 1
        if j < Lmax and abits[j] == 1 and mbits[j] == 0:
            return True
    return False


def main():
    assert len(paid_exit_sources(72)) > 0
    for L in range(73, 80):
        assert len(paid_exit_sources(L)) == 0, L

    assert len(one_paid_outcomes(71)) == 4
    assert len(one_paid_outcomes(72)) == 0

    expected = {
        69: (20, 1),
        70: (4, 0),
        71: (4, 0),
        72: (0, 0),
    }
    for L in range(69, 73):
        states = one_paid_outcomes(L)
        next_paid = sum(can_reach_next_paid(s) for s in states)
        assert (len(states), next_paid) == expected[L], (
            L, len(states), next_paid, expected[L]
        )
        print(L, len(states), next_paid)

    danger = [s for s in one_paid_outcomes(69) if can_reach_next_paid(s)]
    assert danger == [(
        5_344_714_831_606_523_422_699,
        Fraction(8_388_608, 14_348_907),
        Fraction(16, 27),
    )]
    print("unique_L69_next_paid", danger[0])
    print("PASS MATH-058R unique-source paid-macro certificate")


if __name__ == "__main__":
    main()
