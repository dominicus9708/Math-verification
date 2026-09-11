#!/usr/bin/env python3
"""
MATH-058 exact paid-macro transition certificate.

This refines MATH-057.  At a u=0 boundary anchor, a zero-penalty mechanical
segment can end in a paid odd event only if the actual same-integer endpoint
parity disagrees with the mechanically required even step while coefficient
admissibility still holds.

The certificate uses exact rational phase intervals and every dyadic endpoint
lift allowed by the current first-cell ordinary-start window.

Canonical finite results used by the note:
  * paid exit after a zero-cost segment is possible at L=72 but not for L>=73;
  * a cluster containing exactly one paid odd event is possible through L=71
    but not at L=72;
  * among one-paid macros, an outcome capable of reaching another paid macro
    exists at L=69, but none exists at L=70 or L=71.

These are over-approximating necessary-state calculations: ruling out a state
in this superset is safe.  Finite exact arithmetic only.  Collatz remains OPEN.
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
    """All t with y=R+t*2^L satisfying the phase/window necessary bounds."""
    step = 1 << L

    # Need hi*y > LO.
    x = (Fraction(LO, 1) / hi - R) / step
    tmin = max(0, x.numerator // x.denominator + 1)

    # Need lo*y < HI+Q0/3.
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


def paid_exit_outcomes(L: int):
    """All over-approximate states where the next actual bit is a paid odd."""
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

        # Next endpoint parity must be odd.  Since 3^q is odd, parity of
        # E0+t*3^q is parity(E0+t).
        wanted = (1 - E0) & 1
        t = tmin if (tmin & 1) == wanted else tmin + 1
        while t <= tmax:
            out.append((lo, hi, R, t, E0, qinc))
            t += 2
    return out


def one_paid_outcomes(L: int):
    """All exact lift classes that return to u=0 after exactly one paid odd."""
    out = []
    for lo, hi, R, _t0, E0, qinc in paid_exit_outcomes(L):
        omega = (lo + hi) / 2
        mult = phase_multiplier(qinc, omega)

        # Split by the Beatty increment of the paid odd event.
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

            # For exactly one paid odd, if eps=0 we need E==1 mod4;
            # if eps=1 we need E==5 mod8, so that the following 1 or 2
            # actual steps are the required even steps returning u to zero.
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
        if j < Lmax:
            # actual odd while mechanical requires even => next paid odd.
            if abits[j] == 1 and mbits[j] == 0:
                return True
    return False


def main():
    # Generic paid exit: 72 is possible, >=73 is not.
    assert len(paid_exit_outcomes(72)) > 0
    for L in range(73, 80):
        assert len(paid_exit_outcomes(L)) == 0, L

    # Exactly one paid odd can return to u=0 through L=71, but not L=72.
    assert len(one_paid_outcomes(71)) == 4
    assert len(one_paid_outcomes(72)) == 0

    # Full lift audit for the repeatable one-paid macro boundary.
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

    print("PASS MATH-058 exact paid-macro transition certificate")


if __name__ == "__main__":
    main()
