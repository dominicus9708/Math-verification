#!/usr/bin/env python3
"""Exact projective ternary carry law for block-recursive Route-B decoding.

For equal-length/equal-one-count target/candidate blocks define

    Delta(T,W)=C(T)-C(W),
    R_{T,W}(z)=Delta(T,W)+2^{|T|} z,

where z is the carry imported from already processed material to the right.

Split corresponding target/candidate words as

    T=A B,  W=A' B',

with |A|=|A'|, q(A)=q(A'), |B|=|B'|, q(B)=q(B')=q_B.
Writing Delta_A, Delta_B for the component correction differences gives

    R_{T,W}(z)
      = 3^{q_B} Delta_A + 2^{|A|}(Delta_B+2^{|B|}z).

Let

    G_B(z)=Delta_B+2^{|B|}z.

Then for ternary precision m:

1. if m<=q_B,

       3^m | R_{T,W}(z)  iff  3^m | G_B(z);

2. if m>q_B, first require 3^{q_B}|G_B(z), define

       z' = G_B(z)/3^{q_B},

   and then

       3^m | R_{T,W}(z)
       iff
       3^{m-q_B} | (Delta_A+2^{|A|}z').

Hence a fully processed right block consumes exactly q_B ternary digits.  The
projective carry needed by the left child is only

    z' mod 3^{m-q_B}.

Changing the incoming representative z by a multiple of 3^m changes z' only by
a multiple of 3^{m-q_B}, so the transition is well defined on projective carry
classes.

This is a block lift of the previously certified one-position suffix-carry
recurrence. It does not assume that arbitrary candidates share the target's
Christoffel hierarchy; it applies whenever a grammar production supplies a
corresponding equal-count block split.
"""

from itertools import product

MAX_A = 4
MAX_B = 4


def correction(bits):
    C = 0
    q = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3*C + (1 << h)
            q += 1
    return C, q


def residual(T, W, z):
    CT, qT = correction(T)
    CW, qW = correction(W)
    assert len(T) == len(W) and qT == qW
    return (CT-CW) + (1 << len(T))*z


recurrence_checks = 0
projective_checks = 0

for hA in range(MAX_A + 1):
    for hB in range(1, MAX_B + 1):
        for TA in product((0,1), repeat=hA):
            CA, qA = correction(TA)
            for WA in product((0,1), repeat=hA):
                CWA, qAw = correction(WA)
                if qAw != qA:
                    continue

                for TB in product((0,1), repeat=hB):
                    CB, qB = correction(TB)
                    if qB == 0:
                        continue
                    for WB in product((0,1), repeat=hB):
                        CWB, qBw = correction(WB)
                        if qBw != qB:
                            continue

                        T = TA + TB
                        W = WA + WB
                        deltaA = CA-CWA
                        deltaB = CB-CWB

                        for m in range(1, qA+qB+2):
                            mod = 3**m
                            # Enough representatives to exercise zero/nonzero
                            # carry classes without exploding the regression.
                            for z in range(min(mod, 30)):
                                direct = residual(T,W,z) % mod == 0
                                G = deltaB + (1 << hB)*z

                                if m <= qB:
                                    recursive = G % mod == 0
                                else:
                                    if G % (3**qB):
                                        recursive = False
                                    else:
                                        zp = G // (3**qB)
                                        recursive = (
                                            deltaA + (1 << hA)*zp
                                        ) % (3**(m-qB)) == 0

                                        z2 = z + 3**m
                                        zp2 = (
                                            deltaB + (1 << hB)*z2
                                        ) // (3**qB)
                                        assert (zp2-zp) % (3**(m-qB)) == 0
                                        projective_checks += 1

                                assert direct == recursive
                                recurrence_checks += 1

assert recurrence_checks == 829_854
assert projective_checks == 107_343

print("PASS A0 s=1 Route-B projective block ternary-carry certificate")
print("recurrence_checks", recurrence_checks)
print("projective_checks", projective_checks)
print(
    "block_law",
    "G_B=Delta_B+2^hB*z; accepted full block consumes q_B ternary digits",
)
print(
    "projective_state",
    "after the block only z'=G_B/3^qB mod 3^(m-qB) is required",
)
print(
    "dsd_audit",
    "precision decreases only after an exact divisibility gate; no candidate hierarchy is assumed",
)
print(
    "status",
    "block-level ternary precision consumption CLOSED; compact family transition representation remains OPEN",
)
