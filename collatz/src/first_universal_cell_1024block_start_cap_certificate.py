#!/usr/bin/env python3
from fractions import Fraction

B0 = 1 << 71
A0 = 114_208_327_604
Q0 = 72_057_431_991
BLOCK = 1024
BLOCK_AVG_CAP = Fraction(361, 500)
START_CAP_RATIO = Fraction(1365, 1024)


def ln_interval(x: Fraction, n: int = 260):
    """Rigorous rational interval for ln(x), x>=1, via atanh series."""
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)

    z = (x - 1) / (x + 1)
    assert 0 <= z < 1
    z2 = z * z
    term = z
    s = Fraction(0)
    for k in range(n + 1):
        s += term / (2 * k + 1)
        term *= z2

    lo = 2 * s
    tail = 2 * (z ** (2 * n + 3)) / ((2 * n + 3) * (1 - z2))
    return lo, lo + tail


LN2 = ln_interval(Fraction(2), 200)
LN3 = ln_interval(Fraction(3), 260)


def linear_form_interval(A: int, q: int):
    return A * LN2[0] - q * LN3[1], A * LN2[1] - q * LN3[0]


def phase_power(j: int) -> Fraction:
    """
    Return exactly 2^{ {j*theta} }, theta=log_2(3/2).

    Since j*theta = log_2(3^j)-j and log_2(3^j) is never an integer
    for j>0, floor(j*theta) is obtained exactly from bit_length(3^j).
    """
    if j == 0:
        return Fraction(1)

    p3 = 3**j
    floor_log2_p3 = p3.bit_length() - 1
    floor_jtheta = floor_log2_p3 - j
    return Fraction(p3, 1 << (j + floor_jtheta))


def exact_block_max(m: int) -> Fraction:
    """
    Exact maximum over x in [0,1) of

        H_m(x) = sum_{j=0}^{m-1} 2^{- {x+j*theta} }.

    Put u_j=2^{ {j*theta} } and b_j=1/u_j. Between wrap thresholds
    x=1-{j*theta}, H_m is a positive constant times 2^{-x}, hence
    strictly decreases. The maximum is therefore attained at x=0 or at
    the right side of a wrap threshold. All candidate values are rational.
    """
    us = [phase_power(j) for j in range(m)]
    bs = [Fraction(1, 1) / u for u in us]
    base = sum(bs, Fraction(0))
    best = base

    # Descending u is descending fractional phase. At a threshold belonging
    # to phase u, exactly the terms with phase >=u have wrapped.
    pairs = sorted(zip(us, bs), key=lambda z: z[0], reverse=True)
    wrapped = Fraction(0)
    for u, b in pairs:
        wrapped += b
        if u == 1:
            # phase 0 wraps only at x=1, outside [0,1)
            continue
        candidate = u * (base + wrapped) / 2
        if candidate > best:
            best = candidate

    return best


def main():
    # Exact 1024-term rotation-block maximum.
    hmax = exact_block_max(BLOCK)
    assert hmax < BLOCK_AVG_CAP * BLOCK

    blocks, remainder = divmod(Q0, BLOCK)
    assert remainder == 951

    # The latest mechanical first-crossing word maximizes the correction
    # termwise. Split its normalized rotation sum into complete 1024-blocks.
    # Every complete block is bounded by hmax; every remainder term is <=1.
    # Since S=R/3^q=(1/3)*sum 2^{-fractional_phase}, this is a universal
    # correction upper bound for the entire first-crossing language.
    s_upper = (
        blocks * (BLOCK_AVG_CAP * BLOCK) + Fraction(remainder)
    ) / 3

    # epsilon=(2^A-3^q)/3^q = exp(delta)-1.
    delta = linear_form_interval(A0, Q0)
    n_cap = START_CAP_RATIO * B0

    # Prove S_upper < epsilon*n_cap by proving
    # delta > ln(1+S_upper/n_cap).
    rhs = ln_interval(Fraction(1) + s_upper / n_cap, 180)
    assert delta[0] > rhs[1]

    # The new cap removes 683/1024 of the old interval width B0 and leaves
    # only 341/1024.  At 2^61 resolution, candidate starts occupy only the
    # 341 top-11-bit blocks numbered 1024,...,1364.
    assert START_CAP_RATIO - 1 == Fraction(341, 1024)
    assert 2 - START_CAP_RATIO == Fraction(683, 1024)
    assert START_CAP_RATIO * B0 == 1365 * (1 << 61)
    assert bin(1365) == "0b10101010101"

    print("PASS")
    print("block length =", BLOCK)
    print("exact block maximum is below (361/500)*1024")
    print("q remainder modulo 1024 =", remainder)
    print("new start cap: N < (1365/1024)*2^71 = 1365*2^61")
    print("old one-bit interval removed fraction = 683/1024")
    print("remaining top-11-bit blocks = 341")


if __name__ == "__main__":
    main()
