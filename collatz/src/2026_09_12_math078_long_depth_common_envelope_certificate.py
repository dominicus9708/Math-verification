#!/usr/bin/env python3
"""MATH-078: out-of-sample long-depth common-envelope regression.

This certificate rewrites two pre-existing, independently derived results in
MATH-072/077 common coordinates:

1. the forced-OO Beatty-ballot uniform descent certificate through depth 191;
2. the first-cell normalized root-credit / endpoint-q-lock envelope through
   depth 195.

No new global Collatz claim is made.  The purpose is to test whether the common
(S,rho) coordinates preserve the old exact inequalities outside the depth-41
derivation range.
"""

from fractions import Fraction

V0 = 4 * 3**44 + 2
B0 = 1 << 71
CAP = Fraction(1364, 1024) * B0


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    p2 = 1 << k
    while p3 < p2:
        p3 *= 3
        q += 1
    return q


def rho(k: int, q: int) -> Fraction:
    return Fraction(1 << k, 3**q)


def universal_S_envelope(k: int, q: int) -> Fraction:
    d = k - q
    return Fraction(1 << d, 1) * (1 - Fraction(2, 3) ** q)


def universal_S_envelope_reduced(k: int, q: int) -> Fraction:
    d = k - q
    return Fraction(1 << d, 1) - rho(k, q)


def forced_oo_Rmax(j: int, q: int) -> int:
    m = q - 2
    return 5 * 3**m + 2 ** (j - m) * (3**m - 2**m)


def main() -> None:
    # 1. The historical normalized root-credit envelope is exactly 2^d-rho.
    for k in range(2, 300):
        for q in range(1, k + 1):
            assert universal_S_envelope(k, q) == universal_S_envelope_reduced(k, q)

    # Reproduce the historical depth-195 root-safe transition.
    last_safe = 0
    first_fail = None
    for k in range(1, 300):
        q = min_q_survival(k)
        env = universal_S_envelope_reduced(k, q)
        if env < B0:
            last_safe = k
        else:
            first_fail = (k, q)
            break
    assert last_safe == 195
    assert first_fail == (196, 124)

    # 2. Forced-OO Beatty-ballot subcritical safety is exactly an S-envelope
    # orbit-gap test: Smax < V0*(rho-1).
    for j in range(2, 192):
        qcrit = min_q_survival(j)
        for q in range(2, qcrit):
            assert 3**q < 2**j
            Rmax = forced_oo_Rmax(j, q)
            Smax = Fraction(Rmax, 3**q)
            old = Rmax < V0 * (2**j - 3**q)
            new = Smax < V0 * (rho(j, q) - 1)
            assert old == new
            assert old

    # At 192 the old simple worst-case envelope first loses uniformity; the
    # common-coordinate translation must identify exactly the same bad q-set.
    j = 192
    qcrit = min_q_survival(j)
    bad_old = []
    bad_new = []
    for q in range(2, qcrit):
        Rmax = forced_oo_Rmax(j, q)
        Smax = Fraction(Rmax, 3**q)
        if not (Rmax < V0 * (2**j - 3**q)):
            bad_old.append(q)
        if not (Smax < V0 * (rho(j, q) - 1)):
            bad_new.append(q)
    assert bad_old == bad_new
    assert bad_old and max(bad_old) == 121

    # 3. First-cell q-lock through depth195 follows from the same S envelope.
    worst = Fraction(0)
    worst_pair = None
    for k in range(1, 196):
        q = min_q_survival(k)
        env = universal_S_envelope_reduced(k, q)
        assert env < B0
        if env > worst:
            worst = env
            worst_pair = (k, q)
    assert worst_pair == (195, 124)
    assert CAP + B0 < 3 * B0

    print("root_safe_last_depth", last_safe)
    print("root_envelope_first_fail", first_fail)
    print("beatty_uniform_last_depth", 191)
    print("beatty_simple_envelope_first_loss", 192, "max_bad_q", max(bad_old))
    print("first_cell_q_lock_envelope_worst_pair", worst_pair)
    print("PASS MATH-078 long-depth common-envelope regression")


if __name__ == "__main__":
    main()
