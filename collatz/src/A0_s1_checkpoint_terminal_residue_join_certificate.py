#!/usr/bin/env python3
"""A0,s=1 checkpoint terminal-residue join certificate.

Scope
-----
This certificate does NOT prove long correction-language membership.
It certifies an exact interface that can be used by such a membership
engine without an independence assumption.

For a length-n parity word with q odd events at zero-based positions
    a_1 < ... < a_q,
the usual affine correction is

    2^n Z = 3^q X + C,
    C = sum_{r=1}^q 3^(q-r) 2^(a_r).

Modulo 3^k (k <= q), every term except the final k odd-ordinal terms
vanishes, and the 3^q X term vanishes as well.  Hence

    Z == 2^(-n) C_terminal,k  (mod 3^k).

Thus the terminal correction exposes the checkpoint's 3-adic address
without needing X.  In contrast,

    L_- = 3X - Z

shows that L_- mod 3^k still depends on X mod 3^(k-1).  Calling the
24-trit debit channel an independent exposure would therefore be too
strong.

The second part joins the certified first-defect shell with the exposed
27-bit checkpoint residue.  If

    X == X_th + 2^f (mod 2^(f+1))

and z2 == Z (mod 2^27), then

    L_- == 3(X_th + 2^f) - z2 (mod 2^m),
    m = min(f+1,27).

This gives a deterministic upper bound on the number of ordinary debit
integers in the current corridor.  No marginal probabilities or
independence assumptions are used.
"""

from itertools import product

# A0,s=1 constants.
J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
JODD = 10 * R0 + 1

X_TH = 4_697_939_311_072_332_635_131
X_MIN = (1 << 71) + 1
X_MAX = 3_234_977_022_306_677_631_165

Z_MIN = 7_083_549_723_369_539_339_554
Z_MAX = (1 << 73) - 1

L_MINUS_MIN = 669_562_762_561
L_MINUS_MAX = 934_928_480_993

F14 = (2, 5, 8, 10, 13, 16, 18, 21, 24, 27, 29, 32, 35, 37)

K_Z_DYADIC = 27
K_Z_TERNARY = 28
K_L_TERNARY = 24


def correction_from_positions(n, odd_positions):
    """Return q,C for the affine numerator 3^q X + C over 2^n."""
    a = tuple(odd_positions)
    assert all(0 <= x < n for x in a)
    assert all(a[i] < a[i + 1] for i in range(len(a) - 1))
    q = len(a)
    C = sum(3 ** (q - r) * 2**pos for r, pos in enumerate(a, start=1))
    return q, C


def correction_recurrence(bits):
    """Independent affine recurrence, used only as an orientation audit."""
    C = 0
    q = 0
    for n, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << n)
            q += 1
    return q, C


def terminal_correction_mod3(n, odd_positions, k):
    """C modulo 3^k using only the final k odd-ordinal terms."""
    q = len(odd_positions)
    assert 1 <= k <= q
    mod = 3**k
    start_r = q - k + 1
    total = 0
    for r in range(start_r, q + 1):
        pos = odd_positions[r - 1]
        total += 3 ** (q - r) * 2**pos
    return total % mod


def checkpoint_ternary_residue(n, odd_positions, k):
    """Exact terminal formula for Z mod 3^k."""
    mod = 3**k
    c_tail = terminal_correction_mod3(n, odd_positions, k)
    return (pow(2, -n, mod) * c_tail) % mod


def crt_checkpoint(z2, z3):
    """Return the unique checkpoint in the certified interval, or None.

    z2 is modulo 2^27 and z3 is modulo 3^28.
    The mixed-radix modulus exceeds the whole checkpoint interval span,
    so at most one ordinary integer can occur.
    """
    m2 = 1 << K_Z_DYADIC
    m3 = 3**K_Z_TERNARY
    M = m2 * m3
    z2 %= m2
    z3 %= m3
    r = z2 + m2 * (((z3 - z2) * pow(m2, -1, m3)) % m3)
    # All integers in this residue class are r + t M.  Because the
    # interval is shorter than M, there is at most one candidate.
    t = (Z_MIN - r + M - 1) // M
    z = r + t * M
    if Z_MIN <= z <= Z_MAX:
        return z
    return None


def debit_dyadic_residue(f, z2):
    """Return m,residue for L_- modulo 2^m from shell f and Z mod 2^27."""
    assert f in F14
    m = min(f + 1, K_Z_DYADIC)
    mod = 1 << m
    x_res = (X_TH + (1 << f)) % mod
    return m, (3 * x_res - z2) % mod


def max_debit_candidates(m):
    """Maximum size of one residue class inside the closed debit corridor."""
    count = L_MINUS_MAX - L_MINUS_MIN + 1
    mod = 1 << m
    return (count + mod - 1) // mod


def audit_small_words():
    """Exhaustive small-word regression for signs, powers, and inverses."""
    for n in range(1, 9):
        for bits in product((0, 1), repeat=n):
            odd_positions = tuple(i for i, b in enumerate(bits) if b)
            q1, C1 = correction_recurrence(bits)
            q2, C2 = correction_from_positions(n, odd_positions)
            assert (q1, C1) == (q2, C2)
            if q1 == 0:
                continue

            # Choose the unique X modulo 2^n that makes the affine
            # numerator divisible by 2^n; this is only an algebra audit,
            # not a claim that every such word is a legal Collatz prefix.
            m2 = 1 << n
            X = (-C1 * pow(3**q1, -1, m2)) % m2
            numerator = 3**q1 * X + C1
            assert numerator % m2 == 0
            Z = numerator // m2

            for k in range(1, q1 + 1):
                mod3 = 3**k
                c_tail = terminal_correction_mod3(n, odd_positions, k)
                assert C1 % mod3 == c_tail
                assert Z % mod3 == checkpoint_ternary_residue(
                    n, odd_positions, k
                )


def main():
    # Structural orientation check independent of the large constants.
    audit_small_words()

    assert T0 == 104_398_605_910
    assert JODD == 65_868_186_701
    assert JODD > K_Z_TERNARY

    # The terminal 28 odd-ordinal correction terms are sufficient for
    # Z mod 3^28 because the 3^JODD X contribution vanishes modulo 3^28.
    assert JODD >= K_Z_TERNARY

    # The same algebra gives the exact debit dependency
    #   L_- == 3 X - Z (mod 3^k).
    # Therefore X only needs k-1 ternary digits, but it is not eliminated.
    assert K_L_TERNARY - 1 == 23
    assert (3 * (3 ** (K_L_TERNARY - 1))) % (3**K_L_TERNARY) == 0
    assert 3 % (3**K_L_TERNARY) != 0

    # The certified checkpoint mixed-radix exposure is injective on the
    # current ordinary interval.
    z_span = Z_MAX - Z_MIN
    z_modulus = (1 << K_Z_DYADIC) * 3**K_Z_TERNARY
    assert z_span == 2_361_183_242_369_751_087_837
    assert z_modulus == 3_070_471_107_232_407_748_608
    assert z_modulus > z_span

    # Current debit corridor arithmetic.
    l_span = L_MINUS_MAX - L_MINUS_MIN
    l_count = l_span + 1
    assert l_span == 265_365_718_432
    assert l_count == 265_365_718_433

    expected = {
        2:  (3,  33_170_714_805),
        5:  (6,   4_146_339_351),
        8:  (9,     518_292_419),
        10: (11,    129_573_105),
        13: (14,     16_196_639),
        16: (17,      2_024_580),
        18: (19,        506_145),
        21: (22,         63_269),
        24: (25,          7_909),
        27: (27,          1_978),
        29: (27,          1_978),
        32: (27,          1_978),
        35: (27,          1_978),
        37: (27,          1_978),
    }

    print("A0,s=1 checkpoint terminal-residue join certificate")
    print(f"checkpoint span      = {z_span}")
    print(f"2^27*3^28            = {z_modulus}")
    print("terminal correction: Z mod 3^k is X-independent for k <= j0")
    print("debit ternary audit : L_- mod 3^k still needs X mod 3^(k-1)")
    print()
    print("f   dyadic debit bits   max ordinary L_- candidates")

    for f in F14:
        m, _ = debit_dyadic_residue(f, 0)
        cap = max_debit_candidates(m)
        assert (m, cap) == expected[f]
        print(f"{f:2d}  {m:2d}                  {cap:>14,d}")

    # A few exact CRT regressions at the interval endpoints.  These test
    # the join kernel itself; they do not assert language realizability.
    for z in (Z_MIN, Z_MAX, (Z_MIN + Z_MAX) // 2):
        recovered = crt_checkpoint(
            z % (1 << K_Z_DYADIC), z % (3**K_Z_TERNARY)
        )
        assert recovered == z

    print()
    print("PASS")
    print("Classification:")
    print("  EXACT: terminal correction -> checkpoint 3-adic residue")
    print("  EXACT: 27x28 checkpoint CRT is injective on current interval")
    print("  EXACT: shell + checkpoint dyadic residue -> debit dyadic class")
    print("  SAFE : displayed debit counts are deterministic upper bounds")
    print("  REJECTED: treating 24-trit L_- as X-independent exposure")
    print("  OPEN : simultaneous long correction-language realizability")


if __name__ == "__main__":
    main()
