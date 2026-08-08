#!/usr/bin/env python3
"""Weighted transfer computation for coefficient-surviving Collatz parity words.

Accelerated map:
    T(n)=n/2            if n is even
    T(n)=(3n+1)/2       if n is odd

For a length-k parity word b_0,...,b_{k-1}, let q_j be the number of odd
entries through position j.  The word survives coefficient contraction through
all k steps iff
    3**q_j >= 2**(j+1)    for every j=0,...,k-1.

The canonical start residue modulo 2**k is
    r(w) == - sum_{b_j=1} 2**j * 3**(-q_j)   (mod 2**k),
where q_j is the ordinal number of that odd entry.

Hence, for a Fourier frequency t, the character sum over surviving words can be
computed without enumerating residues.  The transfer state is only the current
odd count q.  An even step has weight 1; an odd step ending at odd count q has
weight
    exp(-2*pi*i*t*3**(-q) / 2**(k-j))
after cancelling the factor 2**j against the final modulus 2**k.

This program propagates both the unweighted count distribution and the complex
weighted sum, normalized after every step to avoid overflow.  The result is the
normalized Fourier coefficient of the quotient variable y=(r-3)/4; the global
phase from subtracting 3 does not affect its magnitude.

This is a computational verifier / diagnostic.  Observed Fourier decay is NOT a
proof of a uniform spectral gap.
"""

from __future__ import annotations

import argparse
import cmath
import math


def qmins_exact(k: int) -> list[int]:
    """qmin[j] = smallest q with 3**q >= 2**j, using exact integers."""
    out = [0] * (k + 1)
    q = 0
    p3 = 1
    for j in range(1, k + 1):
        target = 1 << j
        while p3 < target:
            q += 1
            p3 *= 3
        out[j] = q
    return out


def normalized_fourier(k: int, t: int) -> complex:
    """Normalized Fourier coefficient for the length-k survival language."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if t == 0:
        return 1.0 + 0.0j

    qmin = qmins_exact(k)

    # p[q] = unweighted count mass / previous total count
    # a[q] = weighted character sum / previous total count
    p = [1.0]
    a = [1.0 + 0.0j]

    for j in range(k):
        threshold = qmin[j + 1]
        remaining = k - j
        modulus = 1 << remaining
        inv3 = pow(3, -1, modulus)

        # Sequential powers of 3^{-1} modulo 2**remaining.
        invpow = [1] * (j + 2)
        for q in range(1, j + 2):
            invpow[q] = (invpow[q - 1] * inv3) % modulus

        np = [0.0] * (j + 2)
        na = [0.0j] * (j + 2)

        for q_old in range(j + 1):
            pv = p[q_old]
            av = a[q_old]
            if pv == 0.0 and av == 0.0j:
                continue

            # Even transition: q stays unchanged.
            if q_old >= threshold:
                np[q_old] += pv
                na[q_old] += av

            # Odd transition: q increases by one.
            q_new = q_old + 1
            if q_new >= threshold:
                frac = invpow[q_new] / modulus
                phase = cmath.exp(-2j * math.pi * t * frac)
                np[q_new] += pv
                na[q_new] += av * phase

        z = sum(np)
        if z == 0.0:
            return 0.0j
        p = [x / z for x in np]
        a = [x / z for x in na]

    return sum(a)


def survival_count(k: int) -> int:
    """Exact number of length-k coefficient-surviving parity words."""
    qmin = qmins_exact(k)
    counts = [1]
    for j in range(k):
        threshold = qmin[j + 1]
        nxt = [0] * (j + 2)
        for q_old, c in enumerate(counts):
            if c == 0:
                continue
            if q_old >= threshold:
                nxt[q_old] += c
            if q_old + 1 >= threshold:
                nxt[q_old + 1] += c
        counts = nxt
    return sum(counts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("k", type=int, help="survival depth")
    ap.add_argument("--t", type=int, action="append", default=[],
                    help="Fourier frequency; repeatable")
    ap.add_argument("--odd-max", type=int, default=0,
                    help="also scan positive odd t up to this value")
    args = ap.parse_args()

    freqs = list(args.t)
    if args.odd_max > 0:
        freqs.extend(range(1, args.odd_max + 1, 2))
    if not freqs:
        freqs = [1, 3, 5]
    freqs = sorted(set(freqs))

    count = survival_count(args.k)
    print(f"k={args.k}")
    print(f"survival_count={count}")
    print(f"log2_count_per_k={math.log2(count)/args.k:.15f}")

    best = None
    for t in freqs:
        coeff = normalized_fourier(args.k, t)
        mag = abs(coeff)
        rate = float("inf") if mag == 0.0 else -math.log2(mag) / args.k
        print(f"t={t:6d} abs_hat={mag:.17e} rate_bits_per_step={rate:.15f}")
        if best is None or mag > best[1]:
            best = (t, mag, rate)

    if best is not None:
        print(f"worst_t={best[0]} worst_abs_hat={best[1]:.17e} "
              f"worst_rate={best[2]:.15f}")


if __name__ == "__main__":
    main()
