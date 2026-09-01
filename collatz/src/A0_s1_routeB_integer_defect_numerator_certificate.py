#!/usr/bin/env python3
"""Exact integer numerator for the Route-B normalized prefix defect.

For a strict target-dominance parity prefix W of length h and one-count q, let

    a_1 < ... < a_q

be the first q target ranked-one positions and define the target correction

    C*_q = sum_{r=1}^q 3^(q-r) 2^a_r.

The candidate prefix correction is C(W).  Its normalized irreversible defect is

    eta = (C*_q - C(W))/3^q >= 0.

If the exact source channel is

    X = r + 2^h m,
    T^h(X) = y + 3^q m,

then C(W)=2^h y-3^q r.  Therefore

    N := 3^q eta
       = C*_q + 3^q r - 2^h y

is a nonnegative INTEGER defect numerator.

This gives two useful exact updates.

If the next parity bit is 0, q is unchanged and

    N' = N.

If the next parity bit is 1 at absolute position h, with new target rank q+1
at target position a_(q+1), then

    C*_(q+1)=3 C*_q + 2^a_(q+1)

and the exact affine channel update gives

    N' = 3N + 2^a_(q+1) - 2^h.

Under strict target dominance h<=a_(q+1), so N' remains nonnegative.

At fixed (h,q), source residue and defect numerator also satisfy

    N == C*_q + 3^q r  (mod 2^h).

Thus the source/defect danger frontier can store integer (r,N) instead of
rational (r,eta), with eta=N/3^q reconstructed from the layer state.
"""

from itertools import product

MAX_H = 10


def requirements(nmax: int):
    q = [0]
    p2 = p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = requirements(80)
TH = tuple(REQ[i + 1] - REQ[i] for i in range(79))
TPOS = tuple(i for i, bit in enumerate(TH) if bit)


def target_correction(q: int) -> int:
    return sum(
        3 ** (q - r - 1) * (1 << TPOS[r])
        for r in range(q)
    )


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def refine_channel(state, bit: int):
    h, r, y, q = state
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)
    if bit == 0:
        y2 = (y + (3 ** q) * m0) // 2
        q2 = q
    else:
        y2 = (3 * y + (3 ** (q + 1)) * m0 + 1) // 2
        q2 = q + 1
    return h + 1, r2, y2, q2


def build_channel(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def strict_dominance(bits):
    q = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        if q < REQ[u]:
            return False
    return True


def numerator(bits) -> int:
    q = sum(bits)
    return target_correction(q) - correction(bits)


identity_checks = 0
congruence_checks = 0
transition_checks = 0
nonnegative_checks = 0

for h in range(1, MAX_H + 1):
    for bits in product((0, 1), repeat=h):
        if not strict_dominance(bits):
            continue

        hh, r, y, q = build_channel(bits)
        assert hh == h

        N = numerator(bits)
        affine_N = target_correction(q) + (3 ** q) * r - (1 << h) * y

        assert N == affine_N
        assert N >= 0
        identity_checks += 1
        nonnegative_checks += 1

        assert N % (1 << h) == (
            target_correction(q) + (3 ** q) * r
        ) % (1 << h)
        congruence_checks += 1

        for bit in (0, 1):
            bits2 = bits + (bit,)
            if not strict_dominance(bits2):
                continue

            N2 = numerator(bits2)
            if bit == 0:
                expected = N
            else:
                q2 = q + 1
                a = TPOS[q2 - 1]
                assert h <= a
                expected = 3 * N + (1 << a) - (1 << h)

            assert N2 == expected
            transition_checks += 1


assert identity_checks == 153
assert congruence_checks == identity_checks
assert nonnegative_checks == identity_checks
assert transition_checks > 0

print("PASS A0 s=1 Route-B integer defect numerator certificate")
print("max_h", MAX_H)
print("identity_checks", identity_checks)
print("congruence_checks", congruence_checks)
print("transition_checks", transition_checks)
print("nonnegative_checks", nonnegative_checks)
print(
    "identity",
    "N=3^q*eta=C*_q+3^q*r-2^h*y is an exact nonnegative integer on strict target-dominance prefixes",
)
print(
    "transition",
    "bit0: N'=N; bit1: N'=3N+2^a_(q+1)-2^h",
)
print(
    "dyadic_coupling",
    "N == C*_q + 3^q*r mod2^h",
)
print(
    "frontier_coordinate",
    "at fixed q, minimizing eta is exactly minimizing integer N; rational defect storage is unnecessary",
)
print(
    "dsd_audit",
    "source residue, endpoint representative, and membership defect are linked by one exact affine invariant; no independent defect degree of freedom is inferred",
)
print(
    "status",
    "integer defect coordinate CLOSED; compact root-scale frontier-width theorem remains OPEN",
)
