#!/usr/bin/env python3
"""Exact phase-sensitive pure-ballot block state for A0 s=1 Route-B.

Define
    mu_h(B)=min_{0<=u<=|B|}(Q_B(u)-(REQ[h+u]-REQ[h])).
If entering slack is s=q-REQ[h]>=0, block B is ballot-legal exactly when
s+mu_h(B)>=0. Adjacent blocks compose by
    mu_h(UV)=min(mu_h(U), k(U)-DeltaREQ_h(U)+mu_{h+|U|}(V)).
The same local block can have different margins at different threshold phases,
so an exact decoder must carry h or equivalent Christoffel location data.
"""


def threshold_requirements(nmax: int):
    q = [0]
    p2 = 1
    p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


NMAX = 96
REQ = threshold_requirements(NMAX)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(NMAX))
assert set(TH) == {0, 1}


def ballot_margin(h: int, bits):
    assert 0 <= h <= NMAX - len(bits)
    qlocal = 0
    mu = 0
    for u, bit in enumerate(bits, start=1):
        qlocal += bit
        mu = min(mu, qlocal - (REQ[h + u] - REQ[h]))
    return mu


def compose_margin(h: int, left, right):
    l1 = len(left)
    k1 = sum(left)
    return min(
        ballot_margin(h, left),
        k1 - (REQ[h + l1] - REQ[h]) + ballot_margin(h + l1, right),
    )


def legal_direct(h: int, entering_q: int, bits):
    assert entering_q >= REQ[h]
    q = entering_q
    for u, bit in enumerate(bits, start=1):
        q += bit
        if q < REQ[h + u]:
            return False
    return True


MAX_BLOCK = 9
composition_checks = 0
legality_checks = 0
for h in range(24):
    for n in range(MAX_BLOCK + 1):
        for mask in range(1 << n):
            bits = tuple((mask >> i) & 1 for i in range(n))
            direct_mu = ballot_margin(h, bits)
            for cut in range(n + 1):
                assert compose_margin(h, bits[:cut], bits[cut:]) == direct_mu
                composition_checks += 1
            for slack in range(5):
                entering_q = REQ[h] + slack
                assert (slack + direct_mu >= 0) == legal_direct(h, entering_q, bits)
                legality_checks += 1

zero_block = (0,)
h_one = next(h for h, b in enumerate(TH) if b == 1)
h_zero = next(h for h, b in enumerate(TH) if b == 0)
assert h_one == 0 and h_zero == 2
assert ballot_margin(h_one, zero_block) == -1
assert ballot_margin(h_zero, zero_block) == 0
assert not legal_direct(h_one, REQ[h_one], zero_block)
assert legal_direct(h_zero, REQ[h_zero], zero_block)

print("PASS A0 s=1 Route-B phase-sensitive ballot-state certificate")
print("composition_checks", composition_checks)
print("legality_checks", legality_checks)
print("phase_witness", h_one, -1, h_zero, 0)
print("design_constraint", "carry h or exact Christoffel location")
print("status", "EXACT ballot composition CLOSED; finite quotient remains OPEN")
