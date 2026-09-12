#!/usr/bin/env python3
"""MATH-083: exact current-phase quotient for one-paid chains through depth 5.

This certificate is an exact re-coordinate of MATH-061/MATH-082.  It keeps
ordinary dyadic address lineage, but replaces the accumulated source-phase
coordinates by the current anchor phase interval J and the current-phase
penalty coefficient alpha.

For a composed state, if current phase is Omega, accumulated penalty is
    P = alpha * Omega.
For a one-paid edge e,
    Omega' = rho_e * Omega,
    rho_e = 2^h / 3^q,
and beta_e/rho_e is exactly 1/4 or 1/8.  Therefore
    J'     = rho_e * (J intersect I_e),
    alpha' = alpha/rho_e + c_e,
where c_e in {1/4,1/8}.

The dyadic address condition is unchanged:
    r = (A_e-B) * 3^{-Q} mod 2^h,
with r<count.  The child count is exact.

The certificate reproduces MATH-082 depths 2--3, closes all depth-4 and
all depth-5 singleton handoffs analytically for the Bellman reduced-cost
claim, and keeps every multi-source state exact.  Bellman-safe is not, by
itself, an ordinary Collatz descent theorem.  Collatz and the first universal
Farey cell remain open.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m61", HERE / "2026_09_11_math061_onepaid_cylinder_composition_certificate.py"
)
m61 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m61)

LAM = Fraction(19, 503)
MOD73 = 1 << 73
MASK73 = MOD73 - 1


@dataclass(frozen=True)
class State:
    H: int
    Q: int
    source_A: int
    count: int
    target_B: int
    Jlo: Fraction
    Jhi: Fraction
    alpha: Fraction
    macro_count: int


one = m61.all_one_paid_cylinders()
assert len(one) == 910
base = [m61.from_one_paid(c) for c in one]

# Edge constants:
# (h,q,A,B,domain_lo,domain_hi,rho,1/rho,c,beta)
edges = []
for d in base:
    rho = d.phase_scale
    assert rho == Fraction(2**d.H, 3**d.Q)
    c = d.penalty_beta / rho
    assert c in (Fraction(1, 4), Fraction(1, 8))
    edges.append((
        d.H, d.Q, d.source_A, d.target_B,
        d.phase_lo, d.phase_hi, rho, 1/rho, c, d.penalty_beta,
    ))

atoms = []
for d, e in zip(base, edges):
    h, q, A, B, lo, hi, rho, invrho, c, beta = e
    atoms.append(State(
        h, q, A, d.count, B,
        rho * lo, rho * hi,
        c, 1,
    ))

# Current-phase overlap plans are shared by all ordinary-address states with
# the same current phase interval.
plans = {}


def plan_for(Jlo, Jhi):
    key = (Jlo, Jhi)
    if key in plans:
        return plans[key]
    out = []
    for i, e in enumerate(edges):
        h, q, A, B, lo, hi, rho, invrho, c, beta = e
        klo = max(Jlo, lo)
        khi = min(Jhi, hi)
        if klo < khi:
            out.append((
                i, h, (1 << h) - 1, q,
                invrho, c,
                rho * klo, rho * khi,
            ))
    plans[key] = out
    return out


invQ = {}
src_hat = {}


def address_cache(Q):
    if Q not in invQ:
        inv = pow(pow(3, Q, MOD73), -1, MOD73)
        invQ[Q] = inv
        src_hat[Q] = [(d.source_A * inv) & MASK73 for d in base]
    return invQ[Q], src_hat[Q]


def next_level(level, keep_multi=True):
    multi = []
    nterm = nmulti = universal = phase_safe = 0
    Hterm = Counter()
    Hmulti = Counter()
    remaining = []

    for p in level:
        inv, sh = address_cache(p.Q)
        target_hat = (p.target_B * inv) & MASK73

        for di, h, mask, q, invrho, c, Jlo2, Jhi2 in plan_for(p.Jlo, p.Jhi):
            r = (sh[di] - target_hat) & mask
            if r >= p.count:
                continue

            mod = mask + 1
            count = (p.count - 1 - r) // mod + 1
            H = p.H + h
            Q = p.Q + q
            alpha = p.alpha * invrho + c

            if count == 1:
                nterm += 1
                Hterm[H] += 1
                if H <= 73 or Fraction(p.macro_count + 1, 12) - LAM * (H - 73) >= 0:
                    universal += 1
                if H <= 73 or alpha * Jlo2 - LAM * (H - 73) >= 0:
                    phase_safe += 1
                else:
                    d = base[di]
                    matched = p.target_B + 3**p.Q * r
                    d_parameter_0 = (matched - d.source_A) // mod
                    target_B = d.target_B + 3**d.Q * d_parameter_0
                    remaining.append((H, Q, target_B, Jlo2, Jhi2, alpha))
                continue

            nmulti += 1
            Hmulti[H] += 1
            if keep_multi:
                d = base[di]
                matched = p.target_B + 3**p.Q * r
                d_parameter_0 = (matched - d.source_A) // mod
                target_B = d.target_B + 3**d.Q * d_parameter_0
                source_A = p.source_A + (1 << p.H) * r
                multi.append(State(
                    H, Q, source_A, count, target_B,
                    Jlo2, Jhi2, alpha, p.macro_count + 1,
                ))

    return multi, nterm, nmulti, universal, phase_safe, remaining, Hterm, Hmulti


def main():
    level1 = [p for p in atoms if p.count > 1]
    assert len(level1) == 857

    m2, t2, n2, u2, p2, r2, _, _ = next_level(level1)
    assert (t2, n2, u2, p2, len(r2)) == (1137, 11389, 1136, 1137, 0)

    m3, t3, n3, u3, p3, r3, _, _ = next_level(m2)
    assert (t3, n3, u3, p3, len(r3)) == (11511, 85803, 11489, 11509, 2)
    assert sorted(x[0] for x in r3) == [84, 84]

    m4, t4, n4, u4, p4, r4, Ht4, Hm4 = next_level(m3)
    assert (t4, n4, u4, p4, len(r4)) == (76585, 442957, 76564, 76585, 0)
    assert max(Ht4) == 84
    assert max(Hm4) == 71

    m5, t5, n5, u5, p5, r5, Ht5, Hm5 = next_level(m4, keep_multi=False)
    assert m5 == []
    assert (t5, n5, u5, p5, len(r5)) == (372841, 1689024, 372834, 372841, 0)
    assert Ht5[85] == 6
    assert Ht5[87] == 1
    assert max(Ht5) == 87
    assert max(Hm5) == 71

    # Only seven depth-5 terminals need the exact current-phase penalty
    # infimum beyond the universal t/12 wedge; all seven pass it.
    assert t5 - u5 == 7

    print("one_paid_edges", len(base))
    print("current_phase_plan_count", len(plans))
    print("depth4 terminals", t4, "multi", n4,
          "universal_safe", u4, "phase_safe", p4,
          "ordinary_needed", len(r4))
    print("depth5 terminals", t5, "multi", n5,
          "universal_safe", u5, "phase_safe", p5,
          "ordinary_needed", len(r5))
    print("depth5 universal_exceptions", t5-u5,
          "H85", Ht5[85], "H87", Ht5[87])
    print("max multi-source H through depth5", max(Hm5))
    print("PASS MATH-083 current-phase quotient through depth5")


if __name__ == "__main__":
    main()
