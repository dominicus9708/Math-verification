#!/usr/bin/env python3
"""Finite regression certificate for the pure-ballot correction-language recursion.

The theorem is algebraic.  This script independently compares its recursive
language against direct binary-word enumeration on a finite grid and checks the
first-one valuation partition and unrestricted extrema.

No finite regression in this file is promoted to Route-B or Collatz closure.
"""

from functools import lru_cache
from itertools import combinations
from math import comb


@lru_cache(maxsize=None)
def Q(n: int) -> int:
    """Exact threshold Q(0)=0; for n>0, least q with 3^q > 2^n."""
    assert n >= 0
    if n == 0:
        return 0
    target = 1 << n
    q = 0
    p3 = 1
    while p3 <= target:
        p3 *= 3
        q += 1
    return q


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def correction_from_positions(n: int, positions) -> int:
    positions = tuple(positions)
    p = len(positions)
    assert all(0 <= a < n for a in positions)
    assert positions == tuple(sorted(set(positions)))
    return sum((3 ** (p - r - 1)) * (1 << a)
               for r, a in enumerate(positions))


def jump_ballot(h: int, S: int, a: int):
    """Return outgoing (h,S), or None when forced 0^a1 is illegal."""
    assert h >= 0 and S >= 0 and a >= 0
    zero_need = Q(h + a) - Q(h)
    final_need = Q(h + a + 1) - Q(h)
    if S < zero_need or S + 1 < final_need:
        return None
    return h + a + 1, S + 1 - final_need


@lru_cache(maxsize=None)
def ballot_language_recursive(n: int, p: int, h: int, S: int):
    """Exact recursive set C^bal_{n,p}(h,S), for finite regression sizes."""
    assert n >= 0 and h >= 0 and S >= 0
    if p < 0 or p > n:
        return frozenset()

    if p == 0:
        if S >= Q(h + n) - Q(h):
            return frozenset((0,))
        return frozenset()

    out = set()
    for a in range(0, n - p + 1):
        nxt = jump_ballot(h, S, a)
        if nxt is None:
            continue
        h2, S2 = nxt
        tail = ballot_language_recursive(n - a - 1, p - 1, h2, S2)
        first_atom = (3 ** (p - 1)) * (1 << a)
        scale = 1 << (a + 1)
        for C2 in tail:
            out.add(first_atom + scale * C2)
    return frozenset(out)


def ballot_language_direct(n: int, p: int, h: int, S: int):
    """Direct word enumeration, independent of the recursive implementation."""
    assert n >= 0 and 0 <= p <= n and h >= 0 and S >= 0
    out = set()
    q0 = Q(h) + S

    for positions in combinations(range(n), p):
        pos = set(positions)
        q = q0
        legal = True
        for t in range(1, n + 1):
            if (t - 1) in pos:
                q += 1
            if q < Q(h + t):
                legal = False
                break
        if legal:
            out.add(correction_from_positions(n, positions))
    return frozenset(out)


def unrestricted_language_direct(n: int, p: int):
    return frozenset(
        correction_from_positions(n, positions)
        for positions in combinations(range(n), p)
    )


# 1. Recursive language equals direct pure-ballot word enumeration.
regression_cases = 0
for n in range(0, 11):
    for p in range(0, n + 1):
        for h in range(0, 21):
            for S in range(0, 5):
                recursive = ballot_language_recursive(n, p, h, S)
                direct = ballot_language_direct(n, p, h, S)
                assert recursive == direct
                regression_cases += 1


# 2. The p=0 base is exactly the all-zero endpoint condition.
zero_base_cases = 0
for n in range(0, 41):
    for h in range(0, 41):
        for S in range(0, 8):
            got = ballot_language_recursive(n, 0, h, S)
            expected = frozenset((0,)) if S >= Q(h + n) - Q(h) else frozenset()
            assert got == expected
            zero_base_cases += 1


# 3. Unrestricted fixed-(n,p) language is injective, has the stated extrema,
#    and its first one-position is exactly v2(C).
unrestricted_cases = 0
for n in range(0, 13):
    for p in range(0, n + 1):
        language = unrestricted_language_direct(n, p)
        assert len(language) == comb(n, p)

        if p == 0:
            assert language == frozenset((0,))
        else:
            assert min(language) == (3 ** p) - (2 ** p)
            assert max(language) == (1 << (n - p)) * ((3 ** p) - (2 ** p))

            seen_first_branches = {}
            for positions in combinations(range(n), p):
                C = correction_from_positions(n, positions)
                first = positions[0]
                assert v2(C) == first
                seen_first_branches.setdefault(first, set()).add(C)

            # Different first-one branches are disjoint because v2(C) differs.
            branch_sets = list(seen_first_branches.values())
            for i in range(len(branch_sets)):
                for j in range(i + 1, len(branch_sets)):
                    assert branch_sets[i].isdisjoint(branch_sets[j])

        unrestricted_cases += 1


# 4. Exact residual restart is the same first-one recursion algebra.
restart_cases = 0
for n in range(1, 13):
    for p in range(1, n + 1):
        for positions in combinations(range(n), p):
            C = correction_from_positions(n, positions)
            a = v2(C)
            assert a == positions[0]
            numer = C - (3 ** (p - 1)) * (1 << a)
            assert numer % (1 << (a + 1)) == 0
            C2 = numer // (1 << (a + 1))
            tail_positions = tuple(x - a - 1 for x in positions[1:])
            assert C2 == correction_from_positions(n - a - 1, tail_positions)
            restart_cases += 1


print("PASS pure-ballot correction-language recursion certificate")
print("recursive_vs_direct_cases", regression_cases)
print("all_zero_base_cases", zero_base_cases)
print("unrestricted_fixed_np_cases", unrestricted_cases)
print("residual_restart_word_cases", restart_cases)
print("max_direct_language_length", 12)
print("max_recursive_language_length", 10)
print("first_branch_decoder", "a=v2(C)")
print("union_disjoint", True)
print("independent_pruning_factor", False)
print("status", "SAFE finite regression for an EXACT algebraic recursion")
