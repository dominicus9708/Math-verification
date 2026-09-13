#!/usr/bin/env python3
"""MATH-118 regression certificate for the layer-independent AP lineage lemma.

This executable is not the proof of the algebraic lemma.  It independently
regresses the exact one-step AP formulas and finite-depth parity-word affine
form over a deterministic finite test domain, guarding the implementation used
by later closure work.
"""
from fractions import Fraction


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def ap_children(a: int, b: int, m: int):
    assert b > 0 and b % 2 == 1 and m >= 1
    out = []
    for rho in (0, 1):
        if rho >= m:
            continue
        count = (m - 1 - rho) // 2 + 1
        base = a + b * rho
        if base % 2 == 0:
            out.append((base // 2, b, count, rho))
        else:
            out.append(((3 * base + 1) // 2, 3 * b, count, rho))
    assert sum(x[2] for x in out) == m
    return out


def check_one_step():
    cases = 0
    for a in range(1, 96):
        for b in range(1, 32, 2):
            for m in range(1, 65):
                src = [a + b * k for k in range(m)]
                direct = [T(n) for n in src]
                reconstructed = []
                for aa, bb, mm, rho in ap_children(a, b, m):
                    child = [aa + bb * j for j in range(mm)]
                    parameter_direct = [T(a + b * (rho + 2 * j)) for j in range(mm)]
                    assert child == parameter_direct
                    reconstructed.extend((rho + 2 * j, child[j]) for j in range(mm))
                reconstructed.sort()
                assert [v for _, v in reconstructed] == direct
                cases += 1
    return cases


def parity_word_data(n: int, d: int):
    x = n
    q = 0
    bits = []
    for _ in range(d):
        bit = x & 1
        bits.append(bit)
        if bit:
            q += 1
        x = T(x)
    # c = 2^d*T^d(n) - 3^q*n
    c = (1 << d) * x - (3**q) * n
    return tuple(bits), q, c, x


def check_finite_depth():
    cases = 0
    for a in range(1, 80):
        for b in range(1, 24, 2):
            for m in range(1, 48):
                for d in range(1, 8):
                    groups = {}
                    for k in range(m):
                        n = a + b * k
                        w, q, c, x = parity_word_data(n, d)
                        groups.setdefault(w, []).append((k, q, c, x))
                    for w, rows in groups.items():
                        q0 = rows[0][1]
                        c0 = rows[0][2]
                        assert all(q == q0 and c == c0 for _, q, c, _ in rows)
                        for k, q, c, x in rows:
                            n = a + b * k
                            assert (3**q * n + c) == (1 << d) * x
                        # A fixed parity word fixes k modulo 2^d because b is odd.
                        residues = {k % (1 << d) for k, *_ in rows}
                        assert len(residues) == 1
                        rows.sort()
                        if len(rows) >= 2:
                            # Consecutive compatible parameters differ by 2^d,
                            # hence descendants differ by 3^q*b.
                            for left, right in zip(rows, rows[1:]):
                                assert right[0] - left[0] == (1 << d)
                                assert right[3] - left[3] == (3**q0) * b
                    assert sum(len(v) for v in groups.values()) == m
                    cases += 1
    return cases


def main():
    one = check_one_step()
    deep = check_finite_depth()
    print('one_step_cases', one)
    print('finite_depth_source_cases', deep)
    print('PASS MATH-118 AP lineage regression certificate')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__ == '__main__':
    main()
