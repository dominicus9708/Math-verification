#!/usr/bin/env python3
from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
NLOG = 60
M48 = 3**48
D_NEAR = 29_785_654
C_START = 3**46 + 3**43
FREE_TRITS = 40


def log_ratio_bounds(x: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


def max_cantor_leq(u: int, n: int):
    if u < 0:
        return None
    maxv = (3**n - 1) // 2
    if u >= maxv:
        return maxv
    digs = [0] * n
    x = u
    for j in range(n - 1, -1, -1):
        digs[j] = x % 3
        x //= 3
    out = 0
    loose = False
    for d in digs:
        if loose:
            a = 1
        elif d == 0:
            a = 0
        elif d == 1:
            a = 1
        else:
            a = 1
            loose = True
        out = 3*out + a
    return out


def near_start_exists(y: int):
    # x = 4(C_START + S) + 3, S in the 40-trit {0,1} Cantor set.
    low_num = y - D_NEAR - 3 - 4*C_START
    high_num = y - 3 - 4*C_START
    lo = -(-low_num // 4)
    hi = high_num // 4
    s = max_cantor_leq(hi, FREE_TRITS)
    return s is not None and s >= lo


def main():
    l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
    l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)
    alpha_lo = l3 / u2
    alpha_hi = u3 / l2

    # Exact floor certificates for the last 48 mechanical odd positions.
    kappa = []
    for i in range(Q - 48, Q):
        lo = i * alpha_lo
        hi = i * alpha_hi
        a = lo.numerator // lo.denominator
        b = hi.numerator // hi.denominator
        assert a == b
        kappa.append(a)

    gaps20 = [kappa[j] - kappa[j-1] for j in range(29, 48)]
    assert gaps20 == [1,2,2,1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2]

    inv2sigma = pow(pow(2, SIGMA, M48), -1, M48)
    pow3 = [pow(3, 47-r, M48) for r in range(48)]

    def endpoint(z20):
        z48 = [0]*28 + list(z20)
        corr = 0
        for r, (kap, z) in enumerate(zip(kappa, z48)):
            corr = (corr + pow(2, kap-z, M48) * pow3[r]) % M48
        return (inv2sigma * corr) % M48

    y_mech = endpoint([0]*20)
    assert y_mech == 40_150_856_745_180_969_070_537

    # Finite terminal transfer with no inherited amplitude: z_0=0.
    # Transition rule: z_j <= z_{j-1} + (gap_j - 1), with arbitrary drop.
    states = [([0], 0)]
    for g in gaps20:
        nxt = []
        for seq, count in states:
            zprev = seq[-1]
            for z in range(zprev + (g - 1) + 1):
                c = count + (1 if z > 0 else 0)
                if c <= 3:
                    nxt.append((seq + [z], c))
        states = nxt

    seq3 = [tuple(seq) for seq, c in states if c == 3]
    assert len(seq3) == 275
    assert max(max(seq) for seq in seq3) == 2

    hits = []
    for seq in seq3:
        y = endpoint(seq)
        if near_start_exists(y):
            hits.append((seq, y))

    assert not hits
    print("terminal three-defect transfer: PASS")
    print("exact last-20 gap pattern:", gaps20)
    print("non-inherited exactly-three amplitude sequences:", len(seq3))
    print("maximum local amplitude:", 2)
    print("near-return/Cantor hits:", len(hits))
    print("consequence: exactly-three terminal defects require z_0>0 (inherited run)")


if __name__ == "__main__":
    main()
