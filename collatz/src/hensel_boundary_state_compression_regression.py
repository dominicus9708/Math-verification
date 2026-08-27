#!/usr/bin/env python3
"""Finite regression checks for the symbolic Hensel boundary-state audit.

The companion note contains the all-h symbolic proofs.  This script only
checks representative finite instances of:

1. the horizon-lift identity K_i' = K_i + 3^(h-i)t;
2. identical first h admissibility under a 3^h lift;
3. one-unit terminal residue leakage for t=1;
4. the ordering-only displacement persistence inequality.

Finite checks here are regression tests, not the proof of the symbolic lemmas
and not a proof of the Collatz conjecture.
"""

from fractions import Fraction


def lifted_constant_path(h: int, t: int = 1):
    # Universal admissible toy path: K=1, u=2 at every step.
    # The lifted start is 1 + 3^h t.  The same u=2 remains admissible for h
    # steps and the terminal carry is 1+t.
    K = 1
    L = 1 + (3 ** h) * t
    for i in range(h):
        assert (K + 2) % 3 == 0
        assert (L + 2) % 3 == 0
        assert L - K == (3 ** (h - i)) * t
        K = (K + 2) // 3
        L = (L + 2) // 3
        if i + 1 < h:
            assert K % 3 != 0
            assert L % 3 != 0
    assert K == 1
    assert L == 1 + t
    assert L - K == t
    return K, L


for h in range(1, 13):
    a, b = lifted_constant_path(h, 1)
    assert a % 3 == 1
    assert b % 3 == 2

# Ordering persistence regression.  With gaps g in {1,2}, a displacement can
# fall by at most one per leftward odd ordinal.  We test all short gap words
# and the greedy minimum recursion.
for p0 in range(0, 12):
    for mask in range(1 << 8):
        p = p0
        twos = 0
        for i in range(8):
            g = 2 if (mask >> i) & 1 else 1
            if g == 2:
                twos += 1
            dmin = max(0, p - g + 1)
            p = dmin
            assert p >= max(0, p0 - twos)

# The elementary suffix potential used in the note:
# sum_{q=1}^p (1-2^-q) = p-1+2^-p.
for p in range(1, 40):
    lhs = sum(Fraction(1) - Fraction(1, 2**q) for q in range(1, p + 1))
    rhs = Fraction(p - 1) + Fraction(1, 2**p)
    assert lhs == rhs

print("PASS Hensel boundary-state compression regression")
print("symbolic proof remains in companion note")
