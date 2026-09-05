#!/usr/bin/env python3
"""Audit the missing pullback step in repeated local residue-maximality.

A local length-L sibling replacement with the same local odd count q has

    R_u - R_w = 3^q * Delta.

If the block starts after a fixed earlier prefix of length t containing p odd
steps, preserving that earlier prefix and asking the *root* starts to merge at
the end of the replaced block gives

    Delta_root = 2^t * Delta / 3^p.

Since gcd(2^t,3^p)=1, an integer root predecessor requires 3^p | Delta.
Consequently a bounded local credit cannot be independently pulled back after
many earlier odd steps.  A global Hensel/credit construction is needed.

This file also verifies an explicit L=7 sibling pair showing that local
minimality at a later state is not by itself minimality at the original root.
"""

from math import gcd


def correction(mask, L):
    R = 0
    q = 0
    for k in range(L):
        if (mask >> k) & 1:
            R = 3 * R + (1 << k)
            q += 1
    return q, R


def orbit_with_word(x, mask, L):
    out = [x]
    for k in range(L):
        b = (mask >> k) & 1
        assert (x & 1) == b
        x = (3 * x + 1) // 2 if b else x // 2
        out.append(x)
    return out


# Exact L=7 full-Hensel sibling pair.
L = 7
w = 31   # bits 1111100 in time order: positions 0,...,4 odd, then two even
u = 94   # bits 0111101 in time order
qw, Rw = correction(w, L)
qu, Ru = correction(u, L)
assert qw == qu == 5
assert Rw == 211
assert Ru == 454
assert Ru - Rw == 3**5
DELTA = (Ru - Rw) // (3**5)
assert DELTA == 1
assert Rw % (3**5) == Ru % (3**5) == 211

# Choose two valid local starts in their canonical mod-2^7 cylinders.
xw = 12_895
xu = xw - DELTA
ow = orbit_with_word(xw, w, L)
ou = orbit_with_word(xu, u, L)
assert ow[-1] == ou[-1] == 24_482
assert min(ow) == 12_895
assert min(ou) == 6_447

# Thus for, e.g., an original minimal root N=6000, the entire alternate local
# prefix stays above N.  It creates another smaller-than-xw continuation, but
# not a smaller-than-N counterexample merely from this local argument.
N_demo = 6_000
assert N_demo > 21
assert min(ou) > N_demo
assert xu > N_demo

# Pullback divisibility thresholds for the certified local credit maxima.
# L7: Delta_max=21, so p>=3 gives 3^p>Delta_max and no nonzero Delta can be
# divisible by 3^p.
assert 3**2 <= 21 < 3**3
# L14: Delta_max=2730, so p>=8.
assert 3**7 <= 2730 < 3**8
# L19: Delta_max=87381, so p>=11.
assert 3**10 <= 87_381 < 3**11

# Algebraic denominator cannot be cancelled by 2^t.
for p in range(1, 12):
    for t in range(0, 20):
        assert gcd(1 << t, 3**p) == 1

print("local sibling pair: PASS")
print("same endpoint:", ow[-1])
print("alternate local minimum:", min(ou), "> demo root", N_demo)
print("L7 independent integer pullback impossible once prior odd count p>=3")
print("L14 threshold p>=8; L19 threshold p>=11")
print("repeated local maximality therefore requires a global Hensel/credit pullback theorem")
