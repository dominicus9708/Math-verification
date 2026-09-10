#!/usr/bin/env python3
"""
MATH-053 boundary-phase / integer-slack / normalized-correction certificate.

Finite algebraic regression certificate.  This file does not prove Collatz.

Let theta = log_2(3/2), m(q)=floor(q*theta), d=#even shortcut steps,
and u=m(q)-d.  Coefficient admissibility 3^q>2^(q+d) is equivalent to u>=0.

Define
    Omega_q = 2^(q+m(q))/3^q = 2^{-frac(q log_2 3)}.
Then an odd shortcut step taken with current odd count q and slack u adds
    Omega_q / (3*2^u)
to the normalized correction S=C/3^q.
Hence for a coefficient-valid parity word
    S = (1/3) sum_{n=0}^{q-1} 2^{-u_n} Omega_n,
where u_n is the slack immediately before the (n+1)-st odd step.

The checks below use integer/rational arithmetic for every asserted equality.
Only m(q) is obtained by an exact integer comparison, not floating point.
"""
from fractions import Fraction
from itertools import product


def m(q: int) -> int:
    """floor(q log_2(3/2)) via exact powers: largest d with 2^(q+d)<3^q."""
    if q < 0:
        raise ValueError(q)
    d = 0
    while (1 << (q + d + 1)) < 3 ** q:
        d += 1
    return d


def omega(q: int) -> Fraction:
    return Fraction(1 << (q + m(q)), 3 ** q)


def correction_and_slacks(bits: tuple[int, ...]):
    """bits: 1=odd shortcut, 0=even shortcut. Return C,q,d,odd-step slacks."""
    C = 0
    q = d = 0
    us = []
    prefix_valid = True
    for p, bit in enumerate(bits):
        if bit:
            us.append(m(q) - d)
            C = 3 * C + (1 << p)
            q += 1
        else:
            d += 1
        # Strict coefficient gate at every nonempty prefix.
        if not (3 ** q > (1 << (q + d))):
            prefix_valid = False
    return C, q, d, tuple(us), prefix_valid


def formula_S(us: tuple[int, ...]) -> Fraction:
    return sum((omega(n) / (3 * (1 << u)) for n, u in enumerate(us)), Fraction(0, 1))


def selftest():
    # Exact m(q), coefficient equivalence and Omega recurrence.
    for q in range(0, 300):
        mq = m(q)
        assert (1 << (q + mq)) <= 3 ** q
        # q*theta is irrational for q>0, hence strict when q>0.
        if q > 0:
            assert (1 << (q + mq)) < 3 ** q
        assert not ((1 << (q + mq + 1)) < 3 ** q)
        for d in range(0, min(q + 3, mq + 3)):
            assert (3 ** q > (1 << (q + d))) == (mq - d >= 0)
        if q < 299:
            eps = m(q + 1) - mq
            assert eps in (0, 1)
            ratio = omega(q + 1) / omega(q)
            assert ratio == (Fraction(2, 3) if eps == 0 else Fraction(4, 3))
            if omega(q) > Fraction(3, 4):
                assert eps == 0
            elif omega(q) < Fraction(3, 4):
                assert eps == 1
            else:
                assert q == 0  # Omega_0=1, so equality is not reached here either.

    # Exhaustive small parity words: transition law and correction formula.
    checked_valid = 0
    for k in range(1, 15):
        for bits in product((0, 1), repeat=k):
            C, qf, df, us, valid = correction_and_slacks(bits)
            # Direct scan of the slack transition.
            q = d = 0
            for bit in bits:
                u0 = m(q) - d
                if bit:
                    eps = m(q + 1) - m(q)
                    q += 1
                    assert m(q) - d == u0 + eps
                else:
                    d += 1
                    assert m(q) - d == u0 - 1
            assert (q, d) == (qf, df)

            if valid:
                checked_valid += 1
                assert all(u >= 0 for u in us)
                assert Fraction(C, 3 ** qf) == formula_S(us)

    # First coefficient crossing in the integer-slack coordinate.
    # If u=0 then an even step takes u exactly to -1 and violates the gate.
    for q in range(1, 300):
        d = m(q)
        assert 3 ** q > (1 << (q + d))
        assert not (3 ** q > (1 << (q + d + 1)))
        assert m(q) - d == 0
        assert m(q) - (d + 1) == -1

    print(f"PASS MATH-053 exact boundary/slack/correction bridge; valid_words={checked_valid}")


if __name__ == "__main__":
    selftest()
