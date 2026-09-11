#!/usr/bin/env python3
"""
MATH-061 exact composition certificate for one-paid macro cylinders.

This certificate uses the MATH-059 one-paid arithmetic-progression cylinders.
It proves that exact composition preserves the canonical form

  source anchor:  Y = A + 2^H s
  current anchor: Y' = B + 3^Q s,

with exact phase transport and exact accumulated penalty coefficient.

It then exhausts all ordered pairs of one-paid cylinders.  Among the exact
nonempty two-macro compositions, any state whose source parameter count has
collapsed to one is an explicit ordinary integer candidate.  Those explicit
candidates are continued under the shortcut Collatz map and checked for a
descent to the frozen theorem-facing floor 2^71.

This is finite exact arithmetic.  It does not close all longer one-paid chains,
the first universal cell, or the Collatz conjecture.
"""
from dataclasses import dataclass
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math059", HERE / "2026_09_11_math059_macro_cylinder_certificate.py"
)
m59 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m59)

LO = 1 << 71


def pow3_exponent(n: int) -> int:
    q = 0
    while n > 1:
        assert n % 3 == 0
        n //= 3
        q += 1
    return q


@dataclass(frozen=True)
class PathCylinder:
    H: int
    Q: int
    source_A: int
    count: int
    target_B: int
    phase_lo: Fraction
    phase_hi: Fraction
    phase_scale: Fraction
    penalty_beta: Fraction
    macro_count: int


def from_one_paid(c) -> PathCylinder:
    H = c.L + 2 + c.eps
    source_A = c.R + (1 << c.L) * c.first
    assert c.modulus * (1 << c.L) == (1 << H)
    Q = pow3_exponent(c.out_step)
    assert Q == c.q + 1
    return PathCylinder(
        H=H,
        Q=Q,
        source_A=source_A,
        count=c.count,
        target_B=c.out_base,
        phase_lo=c.lo,
        phase_hi=c.hi,
        phase_scale=c.phase_scale,
        penalty_beta=c.beta,
        macro_count=1,
    )


def compose(p: PathCylinder, c) -> PathCylinder | None:
    """Append one exact one-paid cylinder to an exact composed cylinder."""
    d = from_one_paid(c)

    # Exact phase compatibility: current phase is p.phase_scale * Omega_0.
    lo = max(p.phase_lo, d.phase_lo / p.phase_scale)
    hi = min(p.phase_hi, d.phase_hi / p.phase_scale)
    if lo >= hi:
        return None

    # Current endpoint is B + 3^Q s.  The next cylinder requires
    # current endpoint == d.source_A (mod 2^d.H).  Since 3^Q is odd,
    # this fixes s to one residue class modulo 2^d.H.
    mod = 1 << d.H
    coeff = pow(3, p.Q, mod)
    residue = ((d.source_A - p.target_B) * pow(coeff, -1, mod)) % mod
    if residue >= p.count:
        return None

    count = (p.count - 1 - residue) // mod + 1

    # Substitute s = residue + 2^d.H * t.  The canonical form is preserved.
    matched = p.target_B + 3**p.Q * residue
    assert (matched - d.source_A) % mod == 0
    d_parameter_0 = (matched - d.source_A) // mod
    target_B = d.target_B + 3**d.Q * d_parameter_0

    source_A = p.source_A + (1 << p.H) * residue

    return PathCylinder(
        H=p.H + d.H,
        Q=p.Q + d.Q,
        source_A=source_A,
        count=count,
        target_B=target_B,
        phase_lo=lo,
        phase_hi=hi,
        phase_scale=p.phase_scale * d.phase_scale,
        penalty_beta=p.penalty_beta + p.phase_scale * d.penalty_beta,
        macro_count=p.macro_count + 1,
    )


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descend_to_floor(n: int, cap: int = 1000):
    seen = set()
    for k in range(cap + 1):
        if n <= LO:
            return True, k, n
        if n in seen:
            return False, k, n
        seen.add(n)
        n = shortcut(n)
    return False, cap, n


def all_one_paid_cylinders():
    out = []
    for L in range(1, 72):
        out.extend(m59.one_paid_cylinders(L))
    return out


def main():
    one = all_one_paid_cylinders()
    assert len(one) == 910

    # General resolution fact for u=0 anchors from the MATH-057/058 bound:
    # every source anchor is below 2^73.  Therefore once a composed source
    # congruence has modulus 2^H with H>=73, it contains at most one ordinary
    # anchor in the audited range.  The composition formula itself is exact.

    total_pairs = 0
    singleton_pairs = 0
    max_descent_steps = 0
    singleton_failures = []

    for c1 in one:
        p1 = from_one_paid(c1)
        for c2 in one:
            p2 = compose(p1, c2)
            if p2 is None:
                continue
            total_pairs += 1

            if p2.count == 1:
                singleton_pairs += 1
                ok, steps, end = descend_to_floor(p2.target_B)
                max_descent_steps = max(max_descent_steps, steps)
                if not ok:
                    singleton_failures.append((p2, steps, end))

    assert total_pairs == 12_530
    assert singleton_pairs == 1_141
    assert max_descent_steps == 71
    assert singleton_failures == []

    print("one_paid_cylinders", len(one))
    print("two_macro_compositions", total_pairs)
    print("singleton_sources", singleton_pairs)
    print("singleton_max_descent_steps", max_descent_steps)
    print("PASS MATH-061 exact one-paid cylinder composition certificate")


if __name__ == "__main__":
    main()
