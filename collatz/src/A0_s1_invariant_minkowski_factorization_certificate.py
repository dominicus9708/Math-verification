#!/usr/bin/env python3
"""Exact arithmetic certificate for the s=1 pre/tail interface factorization.

The proof is symbolic; this script fixes the first-resonance arithmetic and the
cross-ordering inequalities.  No finite scan is promoted to a global proof.
"""

A0 = 114_208_327_604
Q0 = 72_057_431_991
J0 = 10_439_860_591
R0 = 6_586_818_670
U = 9_809_721_694
P = 6_189_245_291

t0 = 10 * J0
j0 = 10 * R0 + 1

assert A0 == t0 + U
assert Q0 == 10 * R0 + P
assert Q0 - j0 == P - 1

# Mechanical odd-event position in the 1-based time convention used by the
# ordered-position defect notes.
def n(j: int) -> int:
    return ((j - 1) * A0) // Q0 + 1

assert n(j0) == t0
assert n(j0 + 1) == t0 + 2
assert n(j0 + 1) - n(j0) == 2

# s=1 means tau_j0<=t0<tau_{j0+1}.  Since tau_{j0+1} is integral,
# d_{j0+1}=n_{j0+1}-tau_{j0+1} is 0 or 1.
for tau_tail in (t0 + 1, t0 + 2):
    d_tail = n(j0 + 1) - tau_tail
    assert d_tail in (0, 1)

# The cross-ordering condition is automatic for every pre-side displacement
# d_pre>=0 and d_tail in {0,1}:
#   tau_pre < tau_tail
# <=> t0-d_pre < t0+2-d_tail
# <=> d_tail <= d_pre+1.
for d_pre in range(1000):
    for d_tail in (0, 1):
        assert d_tail <= d_pre + 1
        tau_pre = t0 - d_pre
        tau_tail = t0 + 2 - d_tail
        assert tau_pre < tau_tail

print("PASS A0 s=1 invariant/Minkowski factorization certificate")
print("checkpoint", t0, j0)
print("mechanical_interface_positions", n(j0), n(j0 + 1))
print("tail_first_displacement", "{0,1}")
print("cross_ordering", "automatic for all pre displacement >=0")
