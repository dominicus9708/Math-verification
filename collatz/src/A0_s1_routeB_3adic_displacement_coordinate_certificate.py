#!/usr/bin/env python3
"""3-adic displacement coordinate for the first two ternary suffix gates.

After the first ternary gate, write the rightmost target/candidate displacement

    a_0-b_0 = 2 d_0.

Define the 3-adic coordinate

    psi(d) = (1-4^(-d))/3.

Modulo 3^(m-1), inverse powers are interpreted modulo 3^m before dividing the
multiple of 3.  Since 4 has exact order 3^(m-1) modulo 3^m,

    d mod 3^(m-1)  <->  psi(d) mod 3^(m-1)

is a bijection.  It is projectively compatible and satisfies

    psi(d) == d mod 3.

The first outgoing carry is simply

    z_1 = 2^(a_0) psi(d_0).

Thus the huge raw-carry set can be retained symbolically in displacement
coordinates.

For the second target/candidate one pair let

    e_1 = a_1-b_1 >= 0,
    s   = (-1)^(a_0+a_1) in {+1,-1}.

The second ternary gate

    z_1 + 2^(a_1)-2^(b_1) == 0 mod 3

has the exact triangular rule

    d_0 == 0 mod 3   => e_1 even,
    d_0 == s mod 3   => e_1 odd,
    d_0 == -s mod 3  => no solution.

Hence an arbitrary first displacement interval is split only by d_0 mod 3:
one residue class dies immediately and each surviving class fixes the parity of
the next displacement.  This is the first exact symbolic compression beyond
raw carry memoization.

It does not yet prove that all later gates remain bounded by a constant number
of arithmetic-progression families; that higher-depth triangular structure is
left open.
"""

SMALL_M_MAX = 7


def psi_mod(d: int, m: int) -> int:
    """psi(d) modulo 3^(m-1), computed via 4^(-d) modulo 3^m."""
    assert m >= 1 and d >= 0
    if m == 1:
        return 0
    mod_big = 3**m
    u = pow(pow(4, d, mod_big), -1, mod_big)
    numer = (1-u) % mod_big
    assert numer % 3 == 0
    return (numer//3) % (3**(m-1))


bijection_checks = 0
projection_checks = 0
mod3_checks = 0
for m in range(1, SMALL_M_MAX + 1):
    period = 3**(m-1)
    vals = [psi_mod(d,m) for d in range(period)]
    assert len(set(vals)) == period
    bijection_checks += period

    for d in range(period):
        if m >= 2:
            assert psi_mod(d,m) % 3 == d % 3
            mod3_checks += 1
        if m >= 2:
            assert psi_mod(d,m) % (3**(m-2)) == psi_mod(d % (3**(m-2)), m-1)
            projection_checks += 1


second_gate_checks = 0
for a0 in range(3, 10):
    for a1 in range(a0):
        sign = 1 if (a0+a1) % 2 == 0 else -1

        for d0 in range(a0//2 + 1):
            b0 = a0-2*d0
            if b0 < 1:
                continue
            z1 = (2**a0-2**b0)//3

            for e1 in range(a1+1):
                b1 = a1-e1
                if not (0 <= b1 < b0):
                    continue

                direct = (z1 + 2**a1-2**b1) % 3 == 0
                expected = (
                    (d0 % 3 == 0 and e1 % 2 == 0)
                    or
                    (d0 % 3 == sign % 3 and e1 % 2 == 1)
                )
                assert direct == expected
                second_gate_checks += 1

assert bijection_checks == sum(3**j for j in range(SMALL_M_MAX))
assert second_gate_checks > 0

print("PASS A0 s=1 Route-B 3-adic displacement-coordinate certificate")
print("small_m_max", SMALL_M_MAX)
print("bijection_checks", bijection_checks)
print("projection_checks", projection_checks)
print("mod3_checks", mod3_checks)
print("second_gate_checks", second_gate_checks)
print(
    "coordinate",
    "psi(d)=(1-4^(-d))/3 is a projective bijection Z/3^(m-1) -> Z/3^(m-1)",
)
print(
    "second_gate",
    "d0 mod3 splits into: even next displacement, odd next displacement, or immediate failure",
)
print(
    "dsd_audit",
    "the root-scale first carry family is represented symbolically by displacement congruence classes rather than enumerated carry residues",
)
print(
    "status",
    "first two ternary gates symbolically compressed; higher-depth triangular displacement quotient remains OPEN",
)
