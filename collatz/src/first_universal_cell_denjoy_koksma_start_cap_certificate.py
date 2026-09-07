#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
A0 = 114_208_327_604
Q0 = 72_057_431_991
CAP_UP = Fraction(1364, 1024)
CAP_BARRIER = Fraction(1363, 1024)

# Continued-fraction prefix for theta = log_2(3/2), certified below by
# rational ln intervals rather than floating-point CF decisions.
CF = [
    0, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2,
    1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2,
]


def ln_interval(x: Fraction, n: int):
    """Rigorous rational interval for ln(x), x>=1, via atanh series."""
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)

    z = (x - 1) / (x + 1)
    z2 = z * z
    term = z
    s = Fraction(0)
    for k in range(n + 1):
        s += term / (2 * k + 1)
        term *= z2

    lo = 2 * s
    tail = 2 * (z ** (2 * n + 3)) / ((2 * n + 3) * (1 - z2))
    return lo, lo + tail


LN2 = ln_interval(Fraction(2), 220)
LN3 = ln_interval(Fraction(3), 300)


def convergents(cf):
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    out = []
    for a in cf:
        p = a * p_m1 + p_m2
        q = a * q_m1 + q_m2
        out.append((p, q))
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q
    return out


def theta_minus_rational_linear_interval(p: int, q: int):
    """
    Sign certificate for theta - p/q, theta=log_2(3/2).
    The sign equals the sign of q ln 3 - (p+q) ln 2.
    """
    lo = q * LN3[0] - (p + q) * LN2[1]
    hi = q * LN3[1] - (p + q) * LN2[0]
    return lo, hi


def linear_form_interval(A: int, q: int):
    return A * LN2[0] - q * LN3[1], A * LN2[1] - q * LN3[0]


def main():
    conv = convergents(CF)
    p21, q21 = conv[21]
    p22, q22 = conv[22]
    p23, q23 = conv[23]

    assert q21 == 6_586_818_670
    assert q22 == 65_470_613_321
    assert q23 == 137_528_045_312

    # Certify the stated CF prefix through a_23=2 by showing theta lies in
    # its exact continued-fraction cylinder. The endpoints are the final
    # convergent and its mediant with the preceding convergent.
    c_lo, c_hi = theta_minus_rational_linear_interval(p23, q23)
    m_lo, m_hi = theta_minus_rational_linear_interval(
        p23 + p22, q23 + q22
    )
    assert c_hi < 0       # theta < p23/q23
    assert m_lo > 0       # theta > (p23+p22)/(q23+q22)

    # First-cell odd count is the exact two-digit Ostrowski expansion.
    assert Q0 == q22 + q21
    assert q23 == 2 * q22 + q21
    ostrowski_digit_sum = 2

    # External theorem input:
    # Denjoy-Koksma + Ostrowski decomposition for a periodic BV observable.
    # For f(x)=2^{-fractional_part(x)}, Var(f)=1 and integral f = 1/(2 ln2).
    # Therefore
    #   |sum_{n<Q0} f(x+n theta) - Q0/(2 ln2)| <= 2.
    # Since S_* = (1/3) times that rotation sum:
    #   Q0/(6 ln2)-2/3 <= S_* <= Q0/(6 ln2)+2/3.
    s_upper = Fraction(Q0, 1) / (6 * LN2[0]) + Fraction(2, 3)
    s_lower = Fraction(Q0, 1) / (6 * LN2[1]) - Fraction(2, 3)

    # epsilon = exp(delta)-1, delta=A0 ln2-Q0 ln3.
    delta = linear_form_interval(A0, Q0)

    # Positive pruning: prove S_* < epsilon * (1364/1024) B0 by proving
    # delta > ln(1 + s_upper/n_cap).
    n_cap = CAP_UP * B0
    rhs_up = ln_interval(Fraction(1) + s_upper / n_cap, 8)
    assert delta[0] > rhs_up[1]

    # Scalar barrier: prove the explicit admissible mechanical word still has
    # enough scalar correction at the lower boundary of block 1363.
    # This shows a word-independent correction-max envelope cannot eliminate
    # that block; same-integer address coupling is now mandatory.
    n_barrier = CAP_BARRIER * B0
    rhs_low = ln_interval(Fraction(1) + s_lower / n_barrier, 8)
    assert rhs_low[0] > delta[1]

    assert CAP_UP * B0 == 1364 * (1 << 61)
    assert CAP_BARRIER * B0 == 1363 * (1 << 61)

    # The old top-half interval had top-11 blocks 1024,...,2047.
    # The strict new cap leaves exactly 1024,...,1363: 340 blocks.
    assert 1363 - 1024 + 1 == 340

    print("PASS")
    print("theta CF denominators q21,q22,q23 =", q21, q22, q23)
    print("Q0 = q22 + q21; Ostrowski digit sum =", ostrowski_digit_sum)
    print("Denjoy-Koksma rotation error <= 2; normalized correction error <= 2/3")
    print("new start cap: N < (1364/1024)*2^71 = 1364*2^61")
    print("remaining top-11-bit blocks = 340 (1024..1363)")
    print("scalar correction-only barrier already active at block 1363")


if __name__ == "__main__":
    main()
