#!/usr/bin/env python3
"""Exact proof-control certificate for terminal ternary saturation in the s=1 pre bridge.

The mathematical lemma proved in the companion note is:

For m>=1 and any unit S mod 3^m, one can choose m strictly increasing odd-event
positions a_1<...<a_m so that

    sum_{k=0}^{m-1} 3^k 2^{a_{m-k}} == S (mod 3^m).

The induction is right-to-left.  At depth r>1, among every six consecutive
exponents there are exactly two choices e for which

    2^e == S_r (mod 3),
    2^e != S_r (mod 9).

Then S_{r-1}=(S_r-2^e)/3 is again a 3-adic unit.  The r=1 step only needs the
mod-3 match.

For the A0 s=1 checkpoint we place all 28 terminal odd events before t0-168.
The exact ballot margin below certifies that q=j0-28 already stays above the
renewal barrier there.  Hence the terminal construction can be completed to a
full combinatorial 0->0 ballot bridge by putting the earlier q-28 odd events
densely at the beginning.  This is a combinatorial projection theorem only;
it does NOT produce a physical small-X Collatz bridge.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
t0 = 10 * J0
j0 = 10 * R0 + 1
m = 28
BUFFER = 6 * m

# Powers of two mod 9 form the full unit group in six steps.
pow2_mod9 = [pow(2, e, 9) for e in range(6)]
assert pow2_mod9 == [1, 2, 4, 8, 7, 5]
assert set(pow2_mod9) == {1, 2, 4, 5, 7, 8}

# Universal one-digit induction gate: for every unit s mod 9 there are exactly
# two exponent classes mod 6 that match s mod 3 but avoid equality mod 9.
for s in (1, 2, 4, 5, 7, 8):
    valid = [e for e in range(6)
             if (pow(2, e, 3) == s % 3 and pow(2, e, 9) != s)]
    assert len(valid) == 2, (s, valid)

# Exact log bounds for alpha=ln2/ln3, used only for the checkpoint ballot margin.
def log_bounds(z: Fraction, n: int = 90):
    acc = Fraction(0)
    for k in range(n + 1):
        acc += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return acc, acc + tail

l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# To certify ceil(alpha*n) <= j0-m it suffices to prove
# n*ln2 < (j0-m)*ln3.
n = t0 - BUFFER
assert n * u2 < (j0 - m) * l3

# There is enormous room for the q-m earlier odd events before the constructed
# terminal suffix.  A dense initial placement uses positions 0,...,j0-m-1.
assert j0 - m < t0 - 2 * BUFFER

# Constructive regression for representative unit targets.  The proof of
# universality is the six-class lemma above; these cases only audit indexing.
def construct(target: int, depth: int, ceiling: int):
    mod = 3 ** depth
    s = target % mod
    assert s % 3 != 0
    rev = []  # latest to earliest
    c = ceiling
    for r in range(depth, 0, -1):
        mr = 3 ** r
        s %= mr
        choices = []
        # Any six consecutive candidates contain the required local classes.
        for e in range(c - 1, c - 7, -1):
            if pow(2, e, 3) != s % 3:
                continue
            if r > 1 and pow(2, e, 9) == s % 9:
                continue
            choices.append(e)
        assert choices
        e = choices[0]
        rev.append(e)
        if r > 1:
            # Integer representative may be adjusted by a multiple of 3^r;
            # divisibility by 3 and unit quotient are residue-invariant.
            diff = (s - pow(2, e, mr)) % mr
            assert diff % 3 == 0
            s = (diff // 3) % (3 ** (r - 1))
            assert s % 3 != 0
        c = e
    pos = list(reversed(rev))
    assert all(pos[i] < pos[i+1] for i in range(len(pos)-1))
    value = sum((3 ** k) * pow(2, a, mod)
                for k, a in enumerate(reversed(pos))) % mod
    assert value == target % mod
    return pos

ceiling = t0 - BUFFER
M = 3 ** m
# Deterministic edge/sample regression; no finite sample is used as universality proof.
for target in [1, 2, 4, 5, 7, 8, M-1, M-2, M//2 if (M//2)%3 else M//2+1,
               1234567890123 % M, 9876543219877 % M]:
    if target % 3 == 0:
        target += 1
    pos = construct(target, m, ceiling)
    assert pos[-1] < t0 - BUFFER
    assert pos[0] > j0 - m

print("PASS A0 s=1 pre terminal unit-saturation certificate")
print("depth", m)
print("terminal_projection", "all units modulo 3^28")
print("ballot_buffer_steps", BUFFER)
print("local_hensel_gate", "2 valid exponent classes mod 6 at every r>1")
print("warning", "combinatorial ballot projection only; physical small-X bridge remains OPEN")
