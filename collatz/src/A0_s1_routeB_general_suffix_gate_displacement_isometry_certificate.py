#!/usr/bin/env python3
"""General 3-adic displacement isometry for every ternary suffix gate.

At one target-relative suffix step let

    a = target one position,
    z = incoming integer carry,
    b = candidate one position.

The next ternary digit passes iff

    z + 2^a - 2^b == 0 mod 3.

Since 2^b mod3 is in {+1,-1}, the residue z+2^a mod3 either

  * is 0, in which case no candidate parity can pass; or
  * is nonzero, in which case the parity of b is uniquely determined.

For the surviving parity write

    epsilon = (a-b) mod2 in {0,1},
    b = a-epsilon-2d,

with d in the ordinary integer interval forced by b>=0 and by neighboring-one
ordering constraints.

The outgoing carry is

    Phi(d) = (z + 2^a - 2^(a-epsilon-2d))/3.

For any two legal displacement coordinates d,e,

    v_3(Phi(d)-Phi(e)) = v_3(d-e).

Proof: after factoring the unit 2^(a-epsilon), the difference is

    (4^(-e)-4^(-d))/3,

and LTE gives

    v_3(4^n-1)=1+v_3(n).

Thus Phi is a 3-adic isometry on the displacement coordinate.  At remaining
precision m, Phi(d) mod3^(m-1) is therefore in bijection with

    d mod3^(m-1).

This upgrades the first-step psi coordinate to every suffix gate.  A scalable
family decoder should carry displacement cylinders/congruence classes rather
than enumerate raw carry residues.  The remaining problem is to compose these
isometric local coordinates with the strict ordering constraints between
successive candidate one positions.
"""

MAX_A = 14
MAX_Z = 12
MAX_M = 5


def v3(n: int) -> int:
    n = abs(n)
    assert n
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def gate_parity(a: int, z: int):
    rhs = (z + pow(2,a,3)) % 3
    if rhs == 0:
        return None
    # 2^b mod3 = +1 for even b and -1 for odd b.
    return 0 if rhs == 1 else 1


def outgoing(a: int, z: int, b: int) -> int:
    numer = z + 2**a - 2**b
    assert numer % 3 == 0
    return numer//3


parity_checks = 0
isometry_checks = 0
projective_checks = 0

for a in range(MAX_A + 1):
    for z in range(-MAX_Z, MAX_Z + 1):
        required_b_parity = gate_parity(a,z)

        passing_b = []
        for b in range(a + 1):
            direct = (z + 2**a - 2**b) % 3 == 0
            expected = (
                required_b_parity is not None
                and b % 2 == required_b_parity
            )
            assert direct == expected
            parity_checks += 1
            if direct:
                passing_b.append(b)

        if required_b_parity is None:
            assert not passing_b
            continue

        epsilon = (a-required_b_parity) % 2
        coords = []
        for b in passing_b:
            assert (a-b) % 2 == epsilon
            d = (a-epsilon-b)//2
            assert b == a-epsilon-2*d
            coords.append((d,outgoing(a,z,b)))

        for i in range(len(coords)):
            d,zd = coords[i]
            for j in range(i+1,len(coords)):
                e,ze = coords[j]
                assert v3(zd-ze) == v3(d-e)
                isometry_checks += 1

        for m in range(1,MAX_M+1):
            mod = 3**(m-1)
            seen = {}
            for d,zd in coords:
                key = d % mod if mod > 1 else 0
                val = zd % mod if mod > 1 else 0
                if key in seen:
                    assert seen[key] == val
                else:
                    seen[key] = val
                projective_checks += 1
            # Isometry implies distinct d residues give distinct carry residues.
            assert len(set(seen.values())) == len(seen)

assert parity_checks > 0
assert isometry_checks > 0
assert projective_checks > 0

print("PASS A0 s=1 Route-B general suffix-gate displacement-isometry certificate")
print("parity_checks", parity_checks)
print("isometry_checks", isometry_checks)
print("projective_checks", projective_checks)
print(
    "gate",
    "incoming z either rejects immediately or uniquely fixes candidate exponent parity",
)
print(
    "isometry",
    "v3(Phi(d)-Phi(e))=v3(d-e)",
)
print(
    "projective_coordinate",
    "outgoing carry mod3^(m-1) is equivalent to half-displacement d mod3^(m-1)",
)
print(
    "dsd_audit",
    "raw carry state and symbolic displacement state are separated; only the latter is suitable for root-scale family work",
)
print(
    "status",
    "local suffix-gate symbolic coordinate CLOSED; multi-gate ordering/cylinder composition remains OPEN",
)
