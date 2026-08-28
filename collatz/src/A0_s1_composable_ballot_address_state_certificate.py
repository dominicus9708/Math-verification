#!/usr/bin/env python3
"""Composable pure-ballot / 2-adic-address state for A0 s=1 block jumps.

For a reference block b and a candidate block w of the same length, define

    dq      = q(w)-q(b),
    s_min   = min_prefix (Q_w-Q_b),
    D       = Hamming(w,b),
    A_K(w)  = -sum_r 3^{-r} 2^{a_r} (mod 2^K),

and also keep length n and candidate odd count q(w).

The summary

    Sigma_K(w|b) = (n, q, dq, s_min, D, A_K)

is exactly composable under concatenation.  If Sigma_1 is for w1|b1 and
Sigma_2 for w2|b2, then

    n  = n1+n2,
    q  = q1+q2,
    dq = dq1+dq2,
    s_min = min(s_min1, dq1+s_min2),
    D  = D1+D2,

and the universal 2-adic parity address satisfies

    A_K(w1 w2)
      = A_K(w1) + 2^n1 3^(-q1) A_K(w2)   (mod 2^K).

Therefore, for an incoming ballot surplus S, the whole block is valid
relative to the reference iff

    S + s_min >= 0,

and the outgoing surplus is S+dq.

This is an exact quotient for PURE BALLOT + parity-address propagation.
It intentionally does not claim to preserve C4F or any other formation
predicate; those require additional state before a merge is legal.
"""

from itertools import product


def address_mod(bits, K: int) -> int:
    assert K >= 1
    M = 1 << K
    r = 0
    x = 0
    for a, bit in enumerate(bits):
        if bit:
            r += 1
            inv3r = pow(pow(3, r, M), -1, M)
            x = (x - inv3r * (1 << a)) % M
    return x


def summarize(base, cand, K: int):
    assert len(base) == len(cand)
    dq = 0
    s_min = 0
    D = 0
    q = 0
    for b, c in zip(base, cand):
        assert b in (0, 1) and c in (0, 1)
        q += c
        dq += c - b
        s_min = min(s_min, dq)
        D += (b != c)
    return (len(base), q, dq, s_min, D, address_mod(cand, K))


def compose(left, right, K: int):
    n1, q1, dq1, smin1, D1, A1 = left
    n2, q2, dq2, smin2, D2, A2 = right
    M = 1 << K
    scale = (pow(2, n1, M) * pow(pow(3, q1, M), -1, M)) % M
    return (
        n1 + n2,
        q1 + q2,
        dq1 + dq2,
        min(smin1, dq1 + smin2),
        D1 + D2,
        (A1 + scale * A2) % M,
    )


def ballot_valid_with_incoming(summary, incoming: int) -> bool:
    assert incoming >= 0
    return incoming + summary[3] >= 0


def outgoing_surplus(summary, incoming: int) -> int:
    return incoming + summary[2]


# Exhaustive small-word proof regression of every composition coordinate.
K_SMALL = 12
for n1 in range(1, 5):
    words1 = tuple(product((0, 1), repeat=n1))
    for n2 in range(1, 5):
        words2 = tuple(product((0, 1), repeat=n2))
        for b1 in words1:
            for w1 in words1:
                s1 = summarize(b1, w1, K_SMALL)
                for b2 in words2:
                    for w2 in words2:
                        s2 = summarize(b2, w2, K_SMALL)
                        got = compose(s1, s2, K_SMALL)
                        want = summarize(b1 + b2, w1 + w2, K_SMALL)
                        assert got == want

                        # Incoming-surplus criterion is also exactly composable.
                        for incoming in range(5):
                            valid_direct = True
                            s = incoming
                            for b, w in zip(b1 + b2, w1 + w2):
                                s += w - b
                                if s < 0:
                                    valid_direct = False
                                    break
                            assert ballot_valid_with_incoming(got, incoming) == valid_direct
                            if valid_direct:
                                assert outgoing_surplus(got, incoming) == s


# Target-specific 75-bit threshold regression.  This checks that composition
# reproduces the previously certified physical-address lift.
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


REQ = threshold_requirements(75)
TH = tuple(REQ[n + 1] - REQ[n] for n in range(75))
K_TARGET = 75

# Arbitrary split: the composition theorem must not depend on the cut.
for cut in (1, 17, 40, 72, 74):
    s1 = summarize(TH[:cut], TH[:cut], K_TARGET)
    s2 = summarize(TH[cut:], TH[cut:], K_TARGET)
    whole = compose(s1, s2, K_TARGET)
    direct = summarize(TH, TH, K_TARGET)
    assert whole == direct

A75 = summarize(TH, TH, K_TARGET)[5]
A72 = address_mod(TH[:72], 72)
assert A72 == 4_697_939_311_072_332_635_131
assert A75 == A72 + (1 << 74)

print("PASS A0 s=1 composable ballot-address state certificate")
print("state", "(n,q,dq,s_min,D,A mod 2^K)")
print("ballot_concat", "s_min=min(s_min1,dq1+s_min2)")
print("address_concat", "A12=A1+2^n1*3^-q1*A2 mod 2^K")
print("target_threshold_address_72", A72)
print("target_threshold_address_75", A75)
print("C4F_preserved_by_this_state", False)
print("status", "SAFE pure-ballot/address compositional quotient")
