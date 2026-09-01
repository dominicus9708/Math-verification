#!/usr/bin/env python3
"""First-step ternary carry displacement coordinate and raw-state no-go.

For the rightmost target/candidate one positions a>=b, the first suffix-carry
lift starts from z=0 and requires

    2^a-2^b == 0 mod 3.

This holds iff a-b is even.  Write

    a-b=2d,  d>=0.

The outgoing carry is

    z_1=(2^a-2^b)/3
       =2^(a-2d)(4^d-1)/3.

Modulo 3^(m-1), equivalently

    z_1 = 2^a (1-4^(-d))/3.

Because 4 has exact order 3^(m-1) modulo 3^m, the map

    d mod 3^(m-1)  ->  z_1 mod 3^(m-1)

is a bijection.  Indeed equality of two carries mod 3^(m-1), after multiplying
by the unit 2^(-a) and by 3, is exactly equality of 4^(-d) modulo 3^m.

Therefore raw carry values cannot merge distinct displacement residues.  If an
allowed d-interval has length below 3^(m-1), every d in that interval produces
a distinct carry state.

For the actual right critical factor

    h = 630,138,897
    q = 397,573,380
    target last one a = h-1 = 630,138,896,

and m=28, a colliding candidate last one b must have the same parity as a and
must satisfy q-1<=b<=a.  Hence

    b = a-2d,
    0 <= d <= 116,282,758,

so there are 116,282,759 admissible first-step displacement/carry states.
Since

    116,282,759 < 3^27 = 7,625,597,484,987,

all of these carry residues are distinct.

Consequence: the small h=84 memoized-carry regression must NOT be extrapolated
as a raw-z state-count bound for the gigantic root.  A scalable decoder must
retain d symbolically (interval/congruence/hierarchy coordinate) or exploit a
later multi-step relation; direct enumeration of first-step carry residues is
structurally rejected.
"""

SMALL_M_MAX = 6
ROOT_H = 630_138_897
ROOT_Q = 397_573_380
ROOT_M = 28


def first_carry(a, d):
    assert d >= 0 and a >= 2*d
    return (2**a - 2**(a-2*d)) // 3


bijection_checks = 0
for m in range(1, SMALL_M_MAX + 1):
    period = 3**(m-1)
    # Keep all integer exponents nonnegative in this finite regression.
    a = 2*(period-1) + 5
    vals = []
    mod = 3**(m-1)
    for d in range(period):
        z = first_carry(a,d)
        vals.append(z % mod if mod > 1 else 0)
        bijection_checks += 1
    assert len(set(vals)) == period

assert bijection_checks == 364

ROOT_A = ROOT_H - 1
ROOT_B_MIN = ROOT_Q - 1
if ROOT_B_MIN % 2 != ROOT_A % 2:
    ROOT_B_MIN += 1
ROOT_D_MAX = (ROOT_A-ROOT_B_MIN)//2
ROOT_FIRST_STATES = ROOT_D_MAX + 1

assert ROOT_A == 630_138_896
assert ROOT_B_MIN == 397_573_380
assert ROOT_D_MAX == 116_282_758
assert ROOT_FIRST_STATES == 116_282_759
assert ROOT_FIRST_STATES < 3**27
assert 3**27 == 7_625_597_484_987

print("PASS A0 s=1 Route-B first ternary carry displacement no-go certificate")
print("bijection_checks", bijection_checks)
print("root_m", ROOT_M)
print("root_first_displacement_states", ROOT_FIRST_STATES)
print("root_3pow27", 3**27)
print(
    "bijection",
    "d mod 3^(m-1) <-> first outgoing carry z1 mod 3^(m-1)",
)
print(
    "root_nogo",
    "all 116,282,759 first-step m=28 root carry residues are distinct",
)
print(
    "dsd_audit",
    "raw carry memoization is rejected at root scale; symbolic displacement structure is required",
)
print(
    "status",
    "first-step carry no-go CLOSED; symbolic multi-step displacement quotient remains OPEN",
)
