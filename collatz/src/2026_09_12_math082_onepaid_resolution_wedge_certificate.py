#!/usr/bin/env python3
"""MATH-082: one-paid resolution-bit Bellman wedge through macro depth 3.

This certificate imports the canonical MATH-061 one-paid cylinders.  It uses
only exact integer/Fraction arithmetic.

Let H be accumulated shortcut/modulus depth from a u=0 source anchor.  Under
the audited pre-first-cell source bound Y<2^73, define the coarse unresolved
bit budget

    B(H)=max(0,73-H).

With lambda=19/503 use the potential

    H_bit=-lambda*B.

For a composed path with total penalty P, the accumulated reduced cost is

    P                         if H<=73,
    P-lambda*(H-73)           if H>73.

Each one-paid macro contains one paid event at slack u=1, hence its penalty is
Omega/6 with 1/2<Omega<=1.  A t-macro one-paid chain therefore has P>t/12.
Thus the phase-free sufficient terminal condition is

    H<=73, or 503*t >= 228*(H-73).

For an exact composed PathCylinder MATH-061 also stores

    P=penalty_beta*Omega_0, Omega_0 in (phase_lo,phase_hi),

so penalty_beta*phase_lo is a rigorous infimum and gives a stronger exact
phase-interval sufficient test.

The certificate enumerates terminal singleton handoffs at macro depths 2 and
3 while keeping multi-source states symbolic.  It does not claim that a
Bellman-safe handoff is, by itself, an ordinary Collatz descent theorem.
"""

from collections import Counter
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
LO = 1 << 71


def universal_safe(p) -> bool:
    if p.H <= 73:
        return True
    return Fraction(p.macro_count, 12) - LAM * (p.H - 73) >= 0


def phase_safe(p) -> bool:
    if p.H <= 73:
        return True
    return p.penalty_beta * p.phase_lo - LAM * (p.H - 73) >= 0


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descend_to_floor(n: int, cap: int = 1000):
    for j in range(cap + 1):
        if n <= LO:
            return j, n
        n = shortcut(n)
    raise AssertionError("descent cap exceeded")


def append_fast(p, d, inv_by_H):
    """Append canonical PathCylinder d to p, address test before Fractions."""
    H2 = d.H
    mod = 1 << H2
    inv = inv_by_H.get(H2)
    if inv is None:
        inv = pow(pow(3, p.Q, mod), -1, mod)
        inv_by_H[H2] = inv

    residue = ((d.source_A - p.target_B) * inv) % mod
    if residue >= p.count:
        return None
    count = (p.count - 1 - residue) // mod + 1

    lo = max(p.phase_lo, d.phase_lo / p.phase_scale)
    hi = min(p.phase_hi, d.phase_hi / p.phase_scale)
    if lo >= hi:
        return None

    matched = p.target_B + 3**p.Q * residue
    assert (matched - d.source_A) % mod == 0
    d_parameter_0 = (matched - d.source_A) // mod
    target_B = d.target_B + 3**d.Q * d_parameter_0
    source_A = p.source_A + (1 << p.H) * residue

    return m61.PathCylinder(
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


def classify_terminals(terminals):
    u_safe = [p for p in terminals if universal_safe(p)]
    p_safe = [p for p in terminals if phase_safe(p)]
    remain = [p for p in terminals if not phase_safe(p)]
    return u_safe, p_safe, remain


def main() -> None:
    one = m61.all_one_paid_cylinders()
    assert len(one) == 910
    atoms = [m61.from_one_paid(c) for c in one]

    # Macro depth 1 singleton sources are not expanded here; MATH-082 studies
    # new singleton handoffs created from multi-source symbolic roots.
    level = [p for p in atoms if p.count > 1]
    assert len(level) == 857

    # Depth 2.
    terminals2 = []
    multi2 = []
    for p in level:
        inv = {}
        for d in atoms:
            z = append_fast(p, d, inv)
            if z is None:
                continue
            (terminals2 if z.count == 1 else multi2).append(z)

    assert len(terminals2) == 1_137
    assert len(multi2) == 11_389
    assert Counter(p.H for p in terminals2) == Counter({
        69:128, 70:353, 71:321, 72:130, 73:139,
        74:37, 75:14, 76:11, 77:3, 78:1,
    })

    u2, p2, rem2 = classify_terminals(terminals2)
    assert len(u2) == 1_136
    assert len(p2) == 1_137
    assert rem2 == []

    universal_exception2 = [p for p in terminals2 if not universal_safe(p)]
    assert len(universal_exception2) == 1
    ex2 = universal_exception2[0]
    assert ex2.H == 78 and ex2.macro_count == 2
    exact_margin2 = ex2.penalty_beta * ex2.phase_lo - LAM * 5
    assert exact_margin2 == Fraction(
        745936686450315127, 6982634218288398336
    )
    assert exact_margin2 > 0

    # Depth 3.  Address compatibility is tested before Fraction interval work.
    terminals3 = []
    multi3_count = 0
    for p in multi2:
        inv = {}
        for d in atoms:
            z = append_fast(p, d, inv)
            if z is None:
                continue
            if z.count == 1:
                terminals3.append(z)
            else:
                multi3_count += 1

    assert len(terminals3) == 11_511
    assert multi3_count == 85_803
    assert Counter(p.H for p in terminals3) == Counter({
        69:1059, 70:3286, 71:3721, 72:1256, 73:1362,
        74:430, 75:104, 76:172, 77:63, 78:19,
        79:17, 80:6, 81:8, 82:4, 83:1, 84:3,
    })

    u3, p3, rem3 = classify_terminals(terminals3)
    assert len(u3) == 11_489
    assert len(p3) == 11_509
    assert len(rem3) == 2
    assert all(p.H == 84 and p.macro_count == 3 for p in rem3)

    # The two states not certified by the penalty infimum are retained and
    # closed by same-integer ordinary continuation.  This is a separate claim.
    tails = sorted(descend_to_floor(p.target_B)[0] for p in rem3)
    assert tails == [1, 10]

    print("one_paid_cylinders", len(one))
    print("depth2 terminals", len(terminals2), "multi", len(multi2))
    print("depth2 universal_safe", len(u2), "phase_safe", len(p2), "ordinary_needed", len(rem2))
    print("depth2 exceptional_exact_margin", exact_margin2)
    print("depth3 terminals", len(terminals3), "multi", multi3_count)
    print("depth3 universal_safe", len(u3), "phase_safe", len(p3), "ordinary_needed", len(rem3))
    print("depth3 remaining_tail_steps", tails)
    print("PASS MATH-082 one-paid resolution wedge certificate")


if __name__ == "__main__":
    main()
