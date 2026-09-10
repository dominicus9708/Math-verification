#!/usr/bin/env python3
"""
MATH-054 finite exact certificate.

Scope
-----
1. Enumerate coefficient-valid length-72 parity prefixes with at most B positive-slack odd events, B=0..5.
2. Convert each parity prefix to its unique ordinary start residue modulo 2^72.
3. Keep only the current first-cell ordinary-start window
       2^71 < N < 1364*2^61.
4. Continue that same ordinary integer N by the actual shortcut Collatz map and test coefficient admissibility through depth 195.
5. For the seven budget-5 coefficient survivors, test nested exact Hensel class-maximality through depth 72 by a targeted fixed-candidate bounded-carry search.

Finite exact computation only. Collatz conjecture remains OPEN.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache

K0 = 72
KROOT = 195
LO = 1 << 71
HI = 1364 * (1 << 61)


def m(q: int) -> int:
    """Exact floor(q*log_2(3/2)) without floating point."""
    # m is the largest d with 3^q > 2^(q+d).
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    return d


@lru_cache(maxsize=None)
def omega(q: int) -> Fraction:
    return Fraction(2 ** (q + m(q)), 3**q)


def start_residue(C: int, q: int, k: int) -> int:
    mod = 1 << k
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def enumerate_window(B: int):
    """All coefficient-valid length-72 words with <=B positive-slack odd events whose ordinary start lies in the first-cell window."""
    out = []
    stack = [(0, 0, 0, 0, Fraction(0, 1), 0, 0)]
    # pos,q,d,C,penalty,event_count,odd_mask
    while stack:
        pos, q, d, C, pen, cnt, mask = stack.pop()
        if pos == K0:
            N = start_residue(C, q, K0)
            if LO < N < HI:
                out.append((pen, cnt, N, q, d, mask))
            continue

        u = m(q) - d

        # Odd child. Coefficient validity after the step is d <= m(q+1).
        if d <= m(q + 1):
            cnt1 = cnt + (1 if u > 0 else 0)
            if cnt1 <= B:
                term = Fraction(1, 3) * (1 - Fraction(1, 2**u)) * omega(q)
                stack.append((pos + 1, q + 1, d, 3 * C + (1 << pos),
                              pen + term, cnt1, mask | (1 << pos)))

        # Even child. Coefficient validity after the step is d+1 <= m(q).
        if d + 1 <= m(q):
            stack.append((pos + 1, q, d + 1, C, pen, cnt, mask))
    return out


def coefficient_survives_same_integer(N: int, K: int = KROOT):
    n = N
    q = d = 0
    for pos in range(K):
        if n & 1:
            n = (3 * n + 1) // 2
            q += 1
        else:
            n //= 2
            d += 1
        if 3**q <= 2 ** (pos + 1):
            return False, pos + 1
    return True, None


def target_terminal_dominated(mask: int, k: int) -> bool:
    """Exact terminal domination test for one fixed candidate using the fixed-d carry criterion."""
    evens = [i for i in range(k) if ((mask >> i) & 1) == 0]
    d = len(evens)
    q = k - d

    ca = {}
    for j, e in enumerate(evens):
        G = e - j
        ca[G] = ca.get(G, 0) + (1 << j)

    states = {(d, 0)}  # competitor remaining ranks, carry
    for r in range(q, 0, -1):
        aa = ca.get(r, 0)
        nxt = set()
        for nb, h in states:
            for lb in range(nb + 1):
                bb = (((1 << lb) - 1) << (nb - lb)) if lb else 0
                z = h + bb - aa
                if z % 3 == 0:
                    nxt.add((nb - lb, 2 * (z // 3)))
        states = nxt
        if not states:
            return False

    aa0 = ca.get(0, 0)
    for nb, h in states:
        credit = (1 << nb) - 1 - aa0 + h
        if credit > 0:
            return True
    return False


def nested_hensel_through_72(mask: int):
    for j in range(1, K0 + 1):
        pmask = mask & ((1 << j) - 1)
        q = pmask.bit_count()
        if 3**q <= 2**j:
            return False, ("coefficient", j)
        if target_terminal_dominated(pmask, j):
            return False, ("hensel", j)
    return True, None


def main():
    expected = {0: 1, 1: 5, 2: 47, 3: 585, 4: 4484, 5: 27959}
    coeff_expected = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 7}

    budget5 = []
    for B in range(6):
        rows = enumerate_window(B)
        assert len(rows) == expected[B], (B, len(rows), expected[B])
        survivors = []
        for rec in rows:
            ok, fail = coefficient_survives_same_integer(rec[2])
            if ok:
                survivors.append(rec)
        assert len(survivors) == coeff_expected[B], (B, len(survivors), coeff_expected[B])
        print(B, len(rows), len(survivors))
        if B == 5:
            budget5 = survivors

    hensel_ok = 0
    seen_failure = []
    for pen, cnt, N, q, d, mask in budget5:
        ok, why = nested_hensel_through_72(mask)
        if ok:
            hensel_ok += 1
        else:
            seen_failure.append((N, why))
        print("B5", N // (1 << 61), N, float(pen), ok, why)

    assert hensel_ok == 6
    assert seen_failure == [(2614662758027828756219, ("hensel", 56))]

    print("PASS MATH-054 finite first-cell slack-budget certificate")


if __name__ == "__main__":
    main()
