#!/usr/bin/env python3
"""Exact symbolic inverse-merge certificate inside N=36*k+27.

For x=36*k+27, let y=T(x)=54*k+41.  Starting from y, use reverse shortcut edges

    E: z -> 2z,
    O: z -> (2z-1)/3   when integral.

A reverse word with K total edges and q O-edges has asymptotic multiplier relative
to x equal to 2^(K-1)/3^(q-1).  Only words with this ratio <1 can produce a
universal smaller affine merge on an infinite k-cylinder.

The code enumerates every such reverse word with q<=16, solves the required
3-adic congruence on k exactly while walking the word, and retains cylinders on
which the resulting affine predecessor m is positive and m<x for every free
parameter t>=0.

This is a finite symbolic certificate for the listed subprogressions only.  It
does not prove that all 36*k+27 are recursive.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations


def simulate_word(K, O_positions):
    """Return (r,a,A,B) if word proves recursion on k=3^r*t+a, else None.

    Current node is represented as A*t+B after any required refinement of k.
    We start at y=T(36*k+27)=54*k+41.
    """
    Oset = set(O_positions)
    r = 0
    a = 0
    A, B = 54, 41

    for idx in range(K):
        if idx not in Oset:  # reverse even predecessor
            A, B = 2 * A, 2 * B
            continue

        # reverse odd predecessor: z -> (2z-1)/3.
        if A % 3 == 0:
            if B % 3 != 2:
                return None
            A, B = 2 * A // 3, (2 * B - 1) // 3
        else:
            # Exactly one residue t=c mod 3 makes A*t+B == 2 mod 3.
            c = next(c for c in range(3) if (A * c + B) % 3 == 2)
            A0, B0 = A, B
            a += c * (3**r)
            r += 1
            # Substitute t=3*t'+c, then apply (2z-1)/3.
            A = 2 * A0
            B = (2 * (A0 * c + B0) - 1) // 3

    XA = 36 * (3**r)
    XB = 36 * a + 27

    # Strong universal inequality for all t>=0.
    if A > 0 and B > 0 and ((A < XA and B < XB) or (A == XA and B < XB)):
        return r, a, A, B
    return None


def all_contracting_words(q):
    """Enumerate every reverse word with q odd-predecessor edges and ratio <1."""
    K = q
    while 2 ** (K - 1) < 3 ** (q - 1):
        for Opos in combinations(range(K), q):
            yield K, Opos
        K += 1


def prefix_free(cylinders):
    """Remove cylinders contained in an already retained coarser 3-adic cylinder."""
    out = []
    for r, a in sorted(cylinders):
        if any(r0 <= r and a % (3**r0) == a0 for r0, a0 in out):
            continue
        out.append((r, a))
    return out


def word_string(K, Opos):
    Oset = set(Opos)
    return ''.join('O' if i in Oset else 'E' for i in range(K))


def main():
    cylinders = set()
    witness = {}

    for q in range(2, 17):
        for K, Opos in all_contracting_words(q):
            ans = simulate_word(K, Opos)
            if ans is None:
                continue
            r, a, A, B = ans
            cylinders.add((r, a))
            witness.setdefault((r, a), (K, Opos, A, B))

    minimal = prefix_free(cylinders)
    counts = Counter(r for r, _ in minimal)
    density = sum(Fraction(1, 3**r) for r, _ in minimal)

    expected_counts = Counter({5: 1, 7: 5, 9: 25, 10: 131, 12: 580})
    assert counts == expected_counts
    assert len(minimal) == 742
    assert density == Fraction(5836, 531441)

    # Simplest cylinder: k=243*t+172.
    key = (5, 172)
    assert key in minimal
    K, Opos, A, B = witness[key]
    assert word_string(K, Opos) == 'EEOEOEOOOOOO'
    assert (A, B) == (8192, 5823)

    # x=8748*t+6219 and m=8192*t+5823, so x-m=556*t+396>0.
    assert 36 * (3**5) - A == 556
    assert 36 * 172 + 27 - B == 396

    print('SAFE finite-symbolic inverse-merge certificate')
    print('prefix-free cylinders by 3-adic depth:', dict(sorted(counts.items())))
    print('total cylinders:', len(minimal))
    print('exact k-density:', density)
    print('decimal k-density:', float(density))
    print('simplest witness: k == 172 mod 243, reverse word EEOEOEOOOOOO')
    print('x = 8748*t+6219, m = 8192*t+5823 < x')
    print('GLOBAL 36*k+27 RECURSION: OPEN')


if __name__ == '__main__':
    main()
