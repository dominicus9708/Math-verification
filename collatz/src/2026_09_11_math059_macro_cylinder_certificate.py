#!/usr/bin/env python3
"""
MATH-059 exact arithmetic-progression macro-cylinder certificate.

Goals
-----
1. Replace lift-by-lift enumeration in the one-paid macro calculation by a
   single congruence cylinder t = tau + 2^h s.
2. Reproduce the corrected MATH-058 20/4/4/0 table exactly.
3. Identify the unique long L=69 cylinder capable of reaching another paid
   macro and propagate it exactly to coefficient failure.
4. Audit the proposed edgewise slope test J_e(Omega)>0 at lambda=17/450.
   The long L=69 edge is a rigorous counterexample to edgewise positivity,
   so the proof target must be a Bellman/potential or minimum-mean-cycle
   statement rather than positivity of every individual edge.

The cylinder representation is exact finite arithmetic. It is a compression
of the same-integer lift calculation, not a proof of Collatz or first-cell
emptiness.
"""
from dataclasses import dataclass
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

BASE_PATH = Path(__file__).with_name("2026_09_11_paid_macro_transition_certificate.py")
spec = spec_from_file_location("math058r", BASE_PATH)
m58 = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(m58)


@dataclass(frozen=True)
class OnePaidCylinder:
    L: int
    lo: Fraction
    hi: Fraction
    R: int
    E0: int
    q: int
    eps: int
    modulus: int
    tres: int
    first: int
    last: int
    count: int
    out_base: int
    out_step: int
    phase_scale: Fraction
    beta: Fraction

    def target(self, j: int) -> int:
        assert 0 <= j < self.count
        return self.out_base + self.out_step * j

    def source_t(self, j: int) -> int:
        assert 0 <= j < self.count
        return self.first + self.modulus * j


def one_paid_cylinders(L: int):
    """Return exact arithmetic-progression cylinders, not individual lifts."""
    out = []
    for lo, hi, R, E0, qinc in m58.paid_exit_sources(L):
        mult = m58.phase_multiplier(qinc, (lo + hi) / 2)

        cut = Fraction(3, 4) / mult
        cuts = [lo]
        if lo < cut < hi:
            cuts.append(cut)
        cuts.append(hi)

        for a, b in zip(cuts[:-1], cuts[1:]):
            eps = 0 if ((a + b) / 2) * mult > Fraction(3, 4) else 1
            tmin, tmax = m58.lift_bounds(L, R, a, b)
            if tmin > tmax:
                continue

            modulus = 4 if eps == 0 else 8
            endpoint_class = 1 if eps == 0 else 5
            coeff = pow(3, qinc, modulus)
            tres = ((endpoint_class - E0) * pow(coeff, -1, modulus)) % modulus
            first = tmin + ((tres - tmin) % modulus)
            if first > tmax:
                continue
            last = first + ((tmax - first) // modulus) * modulus
            count = (last - first) // modulus + 1

            denom = 4 if eps == 0 else 8
            Efirst = E0 + first * 3**qinc
            out_base = (3 * Efirst + 1) // denom
            out_step = 3 ** (qinc + 1)

            phase_scale = mult * (Fraction(2, 3) if eps == 0 else Fraction(4, 3))
            beta = mult / 6

            out.append(OnePaidCylinder(
                L, a, b, R, E0, qinc, eps, modulus, tres,
                first, last, count, out_base, out_step, phase_scale, beta,
            ))
    return out


def materialize(cylinders):
    """Regression helper only; the cylinder calculation itself does not need this."""
    out = []
    for c in cylinders:
        for j in range(c.count):
            out.append((
                c.target(j),
                c.lo * c.phase_scale,
                c.hi * c.phase_scale,
            ))
    return out


def split_at(interval, cut):
    lo, hi = interval
    if lo < cut < hi:
        return [(lo, cut), (cut, hi)]
    return [(lo, hi)]


def next_macro(Y: int, interval, maxsteps: int = 500):
    """Exact phase-interval propagation from one u=0 anchor.

    Returns the next u=0 anchor after at least one paid event, or coefficient
    failure. beta is the exact coefficient in penalty=beta*Omega_source.
    """
    states = [(Y, interval, Fraction(1), 0, Fraction(0), 0, 0, False)]
    done = []

    for _ in range(maxsteps + 1):
        nxt = []
        for y, I, g, u, beta, steps, paid, had_paid in states:
            if had_paid and u == 0:
                done.append(("anchor", y, I, g, beta, steps, paid))
                continue

            if y % 2 == 0:
                if u == 0:
                    done.append(("fail", y, I, g, beta, steps, paid))
                    continue
                nxt.append((y // 2, I, g, u - 1, beta, steps + 1, paid, had_paid))
                continue

            cut = Fraction(3, 4) / g
            for a, b in split_at(I, cut):
                eps = 0 if g * ((a + b) / 2) > Fraction(3, 4) else 1
                beta2 = beta
                paid2 = paid
                had2 = had_paid
                if u > 0:
                    beta2 += (1 - Fraction(1, 2**u)) * g / 3
                    paid2 += 1
                    had2 = True
                g2 = g * (Fraction(2, 3) if eps == 0 else Fraction(4, 3))
                nxt.append(((3 * y + 1) // 2, (a, b), g2, u + eps,
                            beta2, steps + 1, paid2, had2))
        states = nxt
        if not states:
            return done

    raise AssertionError("macro propagation exceeded maxsteps")


def main():
    expected = {69: 20, 70: 4, 71: 4, 72: 0}
    for L, total in expected.items():
        cylinders = one_paid_cylinders(L)
        assert sum(c.count for c in cylinders) == total
        assert sorted(materialize(cylinders)) == sorted(m58.one_paid_outcomes(L))
        print("one_paid", L, "cylinders", len(cylinders), "states", total)

    danger_target = 5_344_714_831_606_523_422_699
    danger = []
    for c in one_paid_cylinders(69):
        delta = danger_target - c.out_base
        if delta >= 0 and delta % c.out_step == 0:
            j = delta // c.out_step
            if 0 <= j < c.count:
                danger.append((c, j))
    assert len(danger) == 1
    c, j = danger[0]
    assert c.count == 1 and j == 0
    assert c.source_t(0) == 7
    assert c.lo == Fraction(205_891_132_094_649, 281_474_976_710_656)
    assert c.hi == Fraction(109_418_989_131_512_359_209, 147_573_952_589_676_412_928)
    assert c.phase_scale == Fraction(2_361_183_241_434_822_606_848,
                                     2_954_312_706_550_833_698_643)
    assert c.beta == Fraction(590_295_810_358_705_651_712,
                              2_954_312_706_550_833_698_643)
    assert c.lo * c.phase_scale == Fraction(8_388_608, 14_348_907)
    assert c.hi * c.phase_scale == Fraction(16, 27)

    source = c.R + c.source_t(0) * (1 << c.L)
    assert source == 4_271_670_721_469_145_272_313

    lam = Fraction(17, 450)
    macro_length = 71
    assert c.beta * c.hi - lam * macro_length < 0
    print("edgewise_17_over_450_REJECTED",
          "J_interval", c.beta * c.lo - lam * macro_length,
          c.beta * c.hi - lam * macro_length)

    I1 = (Fraction(8_388_608, 14_348_907), Fraction(16, 27))
    d1 = next_macro(danger_target, I1)
    assert d1 == [(
        "anchor",
        6_012_804_185_557_338_850_537,
        I1,
        Fraction(8, 9),
        Fraction(2, 9),
        3,
        1,
    )]
    _, Y2, I1src, g1, _, _, _ = d1[0]
    I2 = (I1src[0] * g1, I1src[1] * g1)
    assert I2 == (Fraction(67_108_864, 129_140_163), Fraction(128, 243))

    d2 = next_macro(Y2, I2)
    assert d2 == [(
        "anchor",
        4_280_599_854_757_128_927_776,
        I2,
        Fraction(1024, 729),
        Fraction(776, 729),
        10,
        4,
    )]
    _, Y3, I2src, g2, _, _, _ = d2[0]
    I3 = (I2src[0] * g2, I2src[1] * g2)
    assert I3 == (
        Fraction(68_719_476_736, 94_143_178_827),
        Fraction(131_072, 177_147),
    )

    d3 = next_macro(Y3, I3)
    assert d3 == [("fail", Y3, I3, Fraction(1), Fraction(0), 0, 0)]
    print("long_L69_chain", "71 + 3 + 10 steps, then coefficient failure")

    print("PASS MATH-059 macro-cylinder compression and Bellman-target audit")


if __name__ == "__main__":
    main()
