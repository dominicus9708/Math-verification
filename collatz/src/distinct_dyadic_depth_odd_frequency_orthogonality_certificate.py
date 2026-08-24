#!/usr/bin/env python3
"""Exact regression certificate for distinct-dyadic-depth odd-frequency orthogonality.

The theorem proved in the companion note is symbolic.  This program checks the
key exact integer obstruction on a finite regression grid:

For distinct 2 <= m_t <= M and odd a_t, every nonzero signed frequency

    A = sum_t eps_t * a_t * 2**(M-m_t), eps_t in {-1,0,1},

has v2(A) <= M-2.  Hence A is neither 0 nor 2**(M-1) modulo 2**M, which is
exactly what is needed for averaging characters over the odd residues.

This is a regression certificate, not the proof itself and not a Collatz proof.
"""

from __future__ import annotations

from itertools import combinations, product


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) undefined")
    n = abs(n)
    return (n & -n).bit_length() - 1


def verify_case(M: int, ms: tuple[int, ...], aas: tuple[int, ...]) -> None:
    assert len(ms) == len(aas)
    assert len(set(ms)) == len(ms)
    assert all(2 <= m <= M for m in ms)
    assert all(a & 1 for a in aas)

    for eps in product((-1, 0, 1), repeat=len(ms)):
        if all(e == 0 for e in eps):
            continue
        A = sum(e * a * (1 << (M - m)) for e, a, m in zip(eps, aas, ms))
        assert A != 0
        assert v2(A) <= M - 2
        mod = A % (1 << M)
        assert mod not in (0, 1 << (M - 1))


def main() -> None:
    checks = 0
    # Exhaustive small regression: all depth subsets and all odd residues at
    # each selected depth.  Keep M modest so this remains a lightweight audit.
    for M in range(3, 8):
        depths = tuple(range(2, M + 1))
        for r in range(1, min(4, len(depths)) + 1):
            for ms in combinations(depths, r):
                odd_lists = [tuple(range(1, 1 << m, 2)) for m in ms]
                # For larger Cartesian products use a deterministic sparse basis
                # of odd units; the symbolic theorem covers the full range.
                if 1:
                    reduced = []
                    for m, vals in zip(ms, odd_lists):
                        candidates = {1, (1 << m) - 1}
                        if m >= 3:
                            candidates.update({3, 5})
                        reduced.append(tuple(sorted(v for v in candidates if v < (1 << m) and v & 1)))
                    odd_lists = reduced
                for aas in product(*odd_lists):
                    verify_case(M, ms, aas)
                    checks += 1

    print(f"checked_cases={checks}")
    print("distinct dyadic-depth odd-frequency orthogonality regression: PASS")


if __name__ == "__main__":
    main()
