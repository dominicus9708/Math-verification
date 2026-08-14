#!/usr/bin/env python3
"""Exact mod-19 selector certificate for the current R1 resonance."""

v0 = (235_984_999, 19_131_826_526)
v1 = (350_384_211, 28_406_424_013)
partial_quotient = 13
EXPECTED = (217_976_794_617, 137_528_045_312)


def chi(v):
    p, r = v
    return (12 * r - p) % 19


assert chi(v0) == 8
assert chi(v1) == 7

hits = []
for k in range(1, partial_quotient + 1):
    p = v0[0] + k * v1[0]
    r = v0[1] + k * v1[1]
    numer = 12 * r - p
    if numer % 19 == 0:
        A = r
        H = numer // 19
        hits.append((k, A, H, p))

assert hits == [(
    7,
    217_976_794_617,
    137_528_045_312,
    2_688_674_476,
)]
assert hits[0][1:3] == EXPECTED

print("epsilon mod-19 current resonance selector: PASS")
print("chi(v0), chi(v1):", chi(v0), chi(v1))
print("partial quotient:", partial_quotient)
print("unique compatible semiconvergent k:", hits[0][0])
print("recovered (A,H):", hits[0][1], hits[0][2])
