#!/usr/bin/env python3
"""Exact proof-control certificate: terminal ballot projection saturates through 47 trits.

For the s=1 pre renewal bridge, the last m odd events alone can realize every
3-adic unit residue modulo 3^m for m=26,28,47.  The proof is inductive and
uses only the six-cycle of powers of 2 modulo 9 plus a large early-placement
buffer that keeps the complete 0->0 ballot condition valid.

At m=47, 3^47 > 2^73, so terminal-ballot information by itself allows every
ordinary checkpoint Z in (2^72,2^73) with 3 not dividing Z.  This is a
negative/pruning audit: deeper terminal trits do not create a sparse endpoint
language.  It does NOT construct a physical small-X Collatz bridge.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
t0 = 10 * J0
j0 = 10 * R0 + 1

assert 3**47 > 2**73

# Powers of 2 modulo 9 are exactly the six 3-adic units.
cycle = [pow(2, e, 9) for e in range(6)]
assert cycle == [1, 2, 4, 8, 7, 5]
assert set(cycle) == {1, 2, 4, 5, 7, 8}

# For each possible unit target digit mod 9, exactly two exponent classes mod 6
# match modulo 3 while avoiding equality modulo 9.  Those choices make the
# quotient (S-2^e)/3 a unit, closing the induction step.
for s in (1, 2, 4, 5, 7, 8):
    valid = [e for e in range(6)
             if pow(2, e, 3) == s % 3 and pow(2, e, 9) != s]
    assert len(valid) == 2


def log_bounds(z: Fraction, n: int = 90):
    acc = Fraction(0)
    for k in range(n + 1):
        acc += Fraction(2) * z**(2*k+1) / (2*k+1)
    tail = Fraction(2) * z**(2*n+3) / ((2*n+3) * (1-z*z))
    return acc, acc + tail

l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# If all terminal m odd events are placed before t0-6m, then before that point
# the already accumulated j0-m odd events are enough to dominate the renewal
# barrier.  A dense initial placement provides those earlier events.
for m in (26, 28, 47):
    n = t0 - 6*m
    assert n * u2 < (j0-m) * l3  # ceil(alpha*n) <= j0-m
    assert j0-m < t0 - 12*m      # ample room for dense prefix + suffix


def construct_unit_sum(target: int, m: int, ceiling: int):
    """Construct m increasing exponents representing target mod 3^m."""
    mod = 3**m
    s = target % mod
    assert s % 3
    latest_to_earliest = []
    c = ceiling
    for r in range(m, 0, -1):
        mr = 3**r
        s %= mr
        choices = []
        for e in range(c-1, c-7, -1):
            if pow(2, e, 3) != s % 3:
                continue
            if r > 1 and pow(2, e, 9) == s % 9:
                continue
            choices.append(e)
        assert choices
        e = choices[0]
        latest_to_earliest.append(e)
        if r > 1:
            diff = (s - pow(2, e, mr)) % mr
            assert diff % 3 == 0
            s = (diff // 3) % (3**(r-1))
            assert s % 3
        c = e
    pos = list(reversed(latest_to_earliest))
    assert all(a < b for a, b in zip(pos, pos[1:]))
    got = sum((3**k) * pow(2, a, mod)
              for k, a in enumerate(reversed(pos))) % mod
    assert got == target % mod
    return pos

# Deterministic regression at the full exposure depth.  Universality is proved
# by the local six-class induction above, not by these samples.
m = 47
M = 3**m
for target in [1, 2, 4, 5, 7, 8, M-1, M-2,
               12345678901234567890 % M,
               9876543210987654321 % M]:
    if target % 3 == 0:
        target += 1
    pos = construct_unit_sum(target, m, t0 - 6*m)
    assert pos[-1] < t0 - 6*m
    assert pos[0] > j0 - m

print("PASS A0 s=1 pre terminal 47-trit saturation certificate")
print("projection_mod_3^47", "all 3-adic units")
print("ordinary_checkpoint_consequence", "all Z in (2^72,2^73) with 3∤Z survive terminal-ballot projection")
print("audit", "terminal-trie pruning beyond unit/nonunit is REJECTED")
print("warning", "full physical small-X arithmetic bridge remains OPEN")
