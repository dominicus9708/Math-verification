#!/usr/bin/env python3
"""Exact one-step ternary carry transition bijection for A0 s=1 Route-B.

At remaining ternary precision m >= 1, let

    M_m = 3^m,
    lambda_m = ord_{3^m}(2) = 2*3^(m-1).

For current carry z mod M_m, target one-position a, and candidate one-position
b, a legal lift requires

    z + 2^a - 2^b == 0 (mod 3),

and then the successor carry is

    z' = (z + 2^a - 2^b)/3 mod 3^(m-1).

Because 2 generates the unit group modulo 3^m:

  * if z + 2^a == 0 (mod 3), there is no legal b at all;
  * otherwise the parity of b is uniquely fixed;
  * on the allowed exponent residues b mod lambda_m, the map b -> z' is a
    bijection onto Z/3^(m-1)Z.

Thus an integer interval I of possible b-values has exactly as many distinct
successor carry states as parity-compatible exponent residues modulo lambda_m
that I hits.  For a contiguous interval this is

    min(parity_count(I), 3^(m-1)).

Scope: exact local carry branching theorem.  It does not by itself bound the
total number of multi-step carry states independently of resolution L.
"""


def order_3_power(m: int) -> int:
    assert m >= 1
    return 2 * (3 ** (m - 1))


def successor_map(m: int, z: int, a: int):
    modulus = 3 ** m
    next_modulus = 3 ** (m - 1)
    lam = order_3_power(m)
    z %= modulus
    a %= lam

    out = {}
    for b in range(lam):
        s = (z + pow(2, a, modulus) - pow(2, b, modulus)) % modulus
        if s % 3:
            continue
        z_next = (s // 3) % next_modulus if next_modulus > 1 else 0
        out[b] = z_next
    return out


def parity_count(lo: int, hi: int, parity: int) -> int:
    if lo > hi:
        return 0
    first = lo if lo % 2 == parity else lo + 1
    if first > hi:
        return 0
    return 1 + (hi - first) // 2


# ---------------------------------------------------------------------------
# 1. Primitive-root/order audit.
# ---------------------------------------------------------------------------

for m in range(1, 8):
    modulus = 3 ** m
    lam = order_3_power(m)
    units = {x for x in range(1, modulus) if x % 3}
    powers = {pow(2, e, modulus) for e in range(lam)}
    assert powers == units
    assert pow(2, lam, modulus) == 1
    if lam > 1:
        assert pow(2, lam // 3, modulus) != 1 if m > 1 else True


# ---------------------------------------------------------------------------
# 2. Exhaustive local bijection regression for small m.
# ---------------------------------------------------------------------------

bijection_checks = 0
empty_checks = 0

for m in range(1, 5):
    modulus = 3 ** m
    next_modulus = 3 ** (m - 1)
    lam = order_3_power(m)

    for z in range(modulus):
        for a in range(lam):
            out = successor_map(m, z, a)
            c_mod3 = (z + pow(2, a, modulus)) % 3

            if c_mod3 == 0:
                assert out == {}
                empty_checks += 1
                continue

            # Exactly one parity class modulo lambda_m survives.
            assert len(out) == 3 ** (m - 1)
            parities = {b & 1 for b in out}
            assert len(parities) == 1

            # Successor carry is a bijection onto all residues modulo 3^(m-1).
            assert set(out.values()) == set(range(next_modulus))
            assert len(set(out.values())) == len(out)
            bijection_checks += 1


# ---------------------------------------------------------------------------
# 3. Contiguous-interval successor-count formula.
# ---------------------------------------------------------------------------

interval_checks = 0
for m in range(1, 5):
    modulus = 3 ** m
    lam = order_3_power(m)
    cap = 3 ** (m - 1)

    for z in range(min(modulus, 15)):
        for a in range(min(lam, 15)):
            out = successor_map(m, z, a)
            c_mod3 = (z + pow(2, a, modulus)) % 3
            if c_mod3 == 0:
                continue

            allowed_parity = next(iter(out)) & 1

            # Test intervals spanning up to two full exponent periods.
            for lo in range(0, min(2 * lam, 24)):
                for hi in range(lo, min(2 * lam, lo + 18)):
                    states = set()
                    for b in range(lo, hi + 1):
                        br = b % lam
                        if br in out:
                            states.add(out[br])

                    expected = min(parity_count(lo, hi, allowed_parity), cap)
                    assert len(states) == expected
                    interval_checks += 1


print("PASS A0 s=1 Route-B ternary carry transition bijection certificate")
print("bijection_checks", bijection_checks)
print("empty_branch_checks", empty_checks)
print("interval_checks", interval_checks)
print("order", "ord_{3^m}(2)=2*3^(m-1)")
print(
    "empty_rule",
    "if z+2^a == 0 mod 3, no candidate exponent b can perform the next ternary lift",
)
print(
    "bijection",
    "otherwise one parity of b survives and b mod lambda_m maps bijectively to z' mod 3^(m-1)",
)
print(
    "interval_branching",
    "distinct successors = min(number of parity-compatible b in interval, 3^(m-1))",
)
print(
    "dsd_audit",
    "local branching is exactly parameterized by exponent residues; no horizon-independent multi-step state bound is inferred",
)
print(
    "status",
    "one-step ternary carry branching CLOSED; multi-step globalization remains OPEN",
)
